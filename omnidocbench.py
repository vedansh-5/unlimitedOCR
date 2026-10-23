import argparse
import csv
import json
import os
import random
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import checks
from loops import is_loop
from ocr_to_md import ROOT, to_markdown

DATASET = "opendatalab/OmniDocBench"
DATASET_REVISION = "aa1ee96d106dbe53d0ae59474d75c6e6d9b53fec"
EVALUATOR = ROOT / "unlimitedOCRvenv" / "third_party" / "OmniDocBench"
EVALUATOR_PYTHON = ROOT / "unlimitedOCRvenv" / "omnidocbench-env" / "bin" / "python"


def ground_truth():
    from huggingface_hub import hf_hub_download

    path = hf_hub_download(DATASET, "OmniDocBench.json", repo_type="dataset", revision=DATASET_REVISION)
    return json.loads(Path(path).read_text())


def image_name(page):
    return Path(page["page_info"]["image_path"]).name


def select(pages, per_type, seed, exclude=()):
    by_type = defaultdict(list)
    for page in pages:
        if image_name(page) in exclude:
            continue
        by_type[page["page_info"]["page_attribute"]["data_source"]].append(page)
    chosen = []
    for kind in sorted(by_type):
        group = sorted(by_type[kind], key=image_name)
        chosen += random.Random(f"{seed}-{kind}").sample(group, min(per_type, len(group)))
    return sorted(chosen, key=image_name)


def cmd_select(args, out):
    exclude = set()
    for other in args.exclude:
        exclude |= set((ROOT / "results" / other / "subset.txt").read_text().splitlines())
    subset = select(ground_truth(), args.per_type, args.seed, exclude)
    (out / "gt_subset.json").write_text(json.dumps(subset, ensure_ascii=False))
    (out / "subset.txt").write_text("".join(image_name(p) + "\n" for p in subset))
    print(f"{len(subset)} pages -> {out / 'subset.txt'}")


def cmd_fetch(args, out):
    from huggingface_hub import hf_hub_download

    inputs = out / "inputs"
    inputs.mkdir(exist_ok=True)
    for name in (out / "subset.txt").read_text().splitlines():
        path = hf_hub_download(DATASET, f"images/{name}", repo_type="dataset", revision=DATASET_REVISION)
        link = inputs / name
        if not link.exists():
            # A hard link keeps the file extension; the port rejects symlinks to extensionless cache blobs.
            os.link(Path(path).resolve(), link)
    print(f"{len(list(inputs.iterdir()))} images in {inputs}")


def run_images(images_dir, out, extra):
    cmd = [sys.executable, str(ROOT / "run_ocr.py"), "--image-dir", str(images_dir), "--output-dir", str(out / "raw"), *extra]
    with (out / "predict.log").open("a") as log:
        return subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT).returncode


def cmd_predict(args, out, extra):
    (out / "raw").mkdir(exist_ok=True)
    return write_predictions(out, run_images(out / "inputs", out, extra), args.repair_markers)


def cmd_retry(args, out, extra):
    base = ROOT / "results" / args.base
    (out / "raw").mkdir(exist_ok=True)
    retry_inputs = out / "inputs"
    retry_inputs.mkdir(exist_ok=True)
    for name in ("subset.txt", "gt_subset.json"):
        shutil.copy(base / name, out / name)
    retried = []
    for md in sorted((base / "raw").glob("*.md")):
        if needs_retry(md):
            image = next((base / "inputs").glob(f"{glob_escape(md.stem)}.*"))
            if not (retry_inputs / image.name).exists():
                os.link(image, retry_inputs / image.name)
            retried.append(image.name)
        else:
            for f in (md, md.with_suffix(".json")):
                shutil.copy(f, out / "raw" / f.name)
    (out / "retried.txt").write_text("".join(n + "\n" for n in retried))
    print(f"{len(retried)} flagged pages re-run, the rest copied from {args.base}")
    code = run_images(retry_inputs, out, extra) if retried else 0
    return write_predictions(out, code, args.repair_markers)


def needs_retry(md):
    meta = md.with_suffix(".json")
    capped = meta.exists() and json.loads(meta.read_text()).get("finish_reason") == "length"
    return capped or is_loop(md.read_text(encoding="utf-8"))


def glob_escape(name):
    return "".join(f"[{c}]" if c in "[]*?" else c for c in name)


def cmd_rescore(args, out):
    base = ROOT / "results" / args.base
    shutil.copytree(base / "raw", out / "raw", dirs_exist_ok=True)
    for name in ("subset.txt", "gt_subset.json"):
        shutil.copy(base / name, out / name)
    return write_predictions(out, 0, args.repair_markers)


def write_predictions(out, code, repair=False):
    raw, pred = out / "raw", out / "pred"
    pred.mkdir(exist_ok=True)
    rows = []
    for md in sorted(raw.glob("*.md")):
        meta = json.loads(md.with_suffix(".json").read_text())
        text = to_markdown(md.read_text(encoding="utf-8"), repair)
        (pred / md.name).write_text(text + "\n", encoding="utf-8")
        plain = checks.strip_tags(text)
        rows.append({
            "image": md.stem,
            "prompt_tokens": meta["prompt_tokens"],
            "gen_tokens": meta["generation_tokens"],
            "model_s": round(meta["elapsed_seconds"], 2),
            "gen_tps": round(meta["generation_tps"], 1),
            "peak_mlx_gb": round(meta["peak_memory_gb"], 2),
            "finish_reason": meta["finish_reason"],
            "complete": meta["complete"],
            "max_repeated_line": checks.max_repeated_line(plain),
            "compression_ratio": round(checks.compression_ratio(plain), 2),
            "distinct_35": round(checks.distinct_n(plain, 35), 4),
            "ragged_tables": checks.ragged_tables(text),
        })
    if not rows:
        print(f"exit {code}; no pages predicted, see {out / 'predict.log'}")
        return code or 1
    with (out / "pages.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"exit {code}; {len(rows)} pages predicted")
    return code


def cmd_evaluate(args, out):
    import yaml

    config = yaml.safe_load((EVALUATOR / "configs" / "end2end.yaml").read_text())
    cfg = config["end2end_eval"]
    cfg["metrics"]["display_formula"]["metric"] = ["Edit_dist"]
    cfg["metrics"]["display_formula"].pop("cdm_workers", None)
    cfg["metrics"]["table"]["teds_workers"] = args.workers
    cfg["dataset"]["match_workers"] = args.workers
    cfg["dataset"]["ground_truth"]["data_path"] = str(out / "gt_subset.json")
    cfg["dataset"]["prediction"]["data_path"] = str(out / "pred")
    eval_dir = out / "eval"
    (eval_dir / "result").mkdir(parents=True, exist_ok=True)
    (eval_dir / "config.yaml").write_text(yaml.safe_dump(config, sort_keys=False))
    cmd = [str(EVALUATOR_PYTHON), str(EVALUATOR / "pdf_validation.py"), "--config", "config.yaml"]
    with (eval_dir / "evaluate.log").open("w") as log:
        return subprocess.run(cmd, cwd=eval_dir, stdout=log, stderr=subprocess.STDOUT).returncode


def cmd_summary(args, out):
    result = out / "eval" / "result"
    report = json.loads((result / "pred_quick_match_run_summary.json").read_text())
    metrics = json.loads((result / "pred_quick_match_metric_result.json").read_text())
    headline = {k: v["notebook_value"] for k, v in report["notebook_metric_summary"]["metrics"].items()}
    by_type = {}
    for element in ("text_block", "reading_order"):
        for key, value in metrics[element]["page"]["Edit_dist"].items():
            if key.startswith("data_source: "):
                by_type.setdefault(key.removeprefix("data_source: "), {})[element] = round(value, 4)
    summary = {"headline": headline, "edit_by_type": by_type}
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run Unlimited-OCR on an OmniDocBench subset and score it.")
    parser.add_argument("step", choices=["select", "fetch", "predict", "retry", "rescore", "evaluate", "summary"])
    parser.add_argument("--exp", required=True)
    parser.add_argument("--per-type", type=int, default=15)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--base", help="Baseline experiment for retry or rescore")
    parser.add_argument("--repair-markers", action="store_true", help="Cut unclosed <|det|> markers from the Markdown")
    parser.add_argument("--exclude", nargs="*", default=[], help="Experiments whose subset pages must not be selected")
    args, extra = parser.parse_known_args(argv)
    out = ROOT / "results" / args.exp
    out.mkdir(parents=True, exist_ok=True)
    if args.step == "select":
        return cmd_select(args, out)
    if args.step == "fetch":
        return cmd_fetch(args, out)
    if args.step == "predict":
        return cmd_predict(args, out, extra)
    if args.step == "rescore":
        return cmd_rescore(args, out)
    if args.step == "retry":
        return cmd_retry(args, out, extra)
    if args.step == "evaluate":
        return cmd_evaluate(args, out)
    return cmd_summary(args, out)


if __name__ == "__main__":
    raise SystemExit(main())
