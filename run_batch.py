import argparse
import csv
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path

import pymupdf

import checks
from ocr_to_md import ROOT, remove_det, run_model, split_pages

SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg"}
COLUMNS = [
    "doc", "pages_in", "pages_out", "chunks", "started_at", "wall_s", "model_s",
    "prompt_tokens", "gen_tokens", "gen_tps", "peak_mlx_gb", "peak_rss_gb", "exit_code",
    "complete", "finish_reasons", "max_repeated_line", "compression_ratio", "distinct_20",
    "distinct_35", "ragged_tables", "empty_pages", "error",
]


def page_count(path):
    if path.suffix.lower() != ".pdf":
        return 1
    with pymupdf.open(path) as doc:
        return doc.page_count


def git_state():
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return commit + ("-dirty" if dirty else "")


def summarize(doc, result, started_at):
    metas = [meta for _, meta in result["outputs"]]
    pages = [remove_det(page) for raw, _ in result["outputs"] for page in split_pages(raw)]
    text = "\n\n".join(pages)

    def total(key):
        return sum(m.get(key, 0) for m in metas)

    error = "" if result["exit_code"] == 0 else result["log"].strip().splitlines()[-1:]
    return {
        "doc": doc.name,
        "pages_in": page_count(doc),
        "pages_out": len(pages),
        "chunks": len(metas),
        "started_at": started_at,
        "wall_s": round(result["wall_s"], 2),
        "model_s": round(total("elapsed_seconds"), 2),
        "prompt_tokens": total("prompt_tokens"),
        "gen_tokens": total("generation_tokens"),
        "gen_tps": round(total("generation_tokens") / total("elapsed_seconds"), 1) if metas else 0,
        "peak_mlx_gb": round(max((m.get("peak_memory_gb", 0) for m in metas), default=0), 2),
        "peak_rss_gb": round(result["peak_rss_gb"], 2),
        "exit_code": result["exit_code"],
        "complete": bool(metas) and all(m.get("complete") for m in metas),
        "finish_reasons": "|".join(m.get("finish_reason", "") for m in metas),
        "max_repeated_line": checks.max_repeated_line(text),
        "compression_ratio": round(checks.compression_ratio(text), 2),
        "distinct_20": round(checks.distinct_n(text, 20), 4),
        "distinct_35": round(checks.distinct_n(text, 35), 4),
        "ragged_tables": checks.ragged_tables(text),
        "empty_pages": checks.empty_pages(pages),
        "error": " ".join(error),
    }, "\n\n".join(p for p in pages if p)


def main(argv=None):
    parser = argparse.ArgumentParser(description="OCR every document in a folder and log one CSV row per document.")
    parser.add_argument("--exp", required=True, help="Experiment ID, e.g. E-003")
    parser.add_argument("--inputs", type=Path, default=ROOT / "tests" / "data")
    args, extra = parser.parse_known_args(argv)

    out = ROOT / "results" / args.exp
    (out / "md").mkdir(parents=True, exist_ok=True)
    config = {
        "exp": args.exp,
        "inputs": str(args.inputs),
        "model_args": extra,
        "git": git_state(),
        "python": platform.python_version(),
        "machine": platform.platform(),
        "packages": {p: version(p) for p in ("mlx", "mlx-vlm", "unlimited-ocr-mlx", "pillow", "transformers")},
        "started_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    (out / "config.json").write_text(json.dumps(config, indent=2) + "\n")

    csv_path = out / "runs.csv"
    new_file = not csv_path.exists()
    docs = sorted(p for p in args.inputs.iterdir() if p.suffix.lower() in SUFFIXES)
    with csv_path.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        if new_file:
            writer.writeheader()
        for i, doc in enumerate(docs, 1):
            md_path = out / "md" / f"{doc.stem}.md"
            if md_path.exists():
                print(f"[{i}/{len(docs)}] skip {doc.name} (done)")
                continue
            print(f"[{i}/{len(docs)}] {doc.name}", flush=True)
            started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
            result = run_model(doc, out / "raw" / doc.stem, extra)
            row, markdown = summarize(doc, result, started_at)
            writer.writerow(row)
            f.flush()
            if row["exit_code"] == 0:
                md_path.write_text(markdown + "\n", encoding="utf-8")
            print(f"    {row['wall_s']} s, {row['gen_tokens']} tokens, peak {row['peak_mlx_gb']} GB, exit {row['exit_code']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
