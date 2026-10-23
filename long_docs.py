import argparse
import csv
import json
import re
import shutil
from pathlib import Path

import pymupdf
from rapidfuzz.distance import Levenshtein

import checks
from loops import is_loop
from ocr_to_md import ROOT, remove_det, split_pages

BUCKETS = (2, 5, 10, 20, 40)
DPI = 300
MARKUP_RE = re.compile(r"\\[()\[\]]|\$+|[#*|_`>]+")


def normalize(text):
    return " ".join(MARKUP_RE.sub(" ", checks.strip_tags(text)).split())


def edit_distance(prediction, reference):
    return Levenshtein.normalized_distance(normalize(prediction), normalize(reference))


def cmd_make(args, out):
    inputs, refs = out / "inputs", out / "reference"
    inputs.mkdir(parents=True, exist_ok=True)
    refs.mkdir(exist_ok=True)
    for source in args.sources:
        with pymupdf.open(source) as doc:
            for n in (b for b in BUCKETS if b <= doc.page_count):
                name = f"{source.stem}_p{n:02d}"
                part = pymupdf.open()
                part.insert_pdf(doc, from_page=0, to_page=n - 1)
                part.save(inputs / f"{name}.pdf")
                (refs / f"{name}.txt").write_text("\n".join(doc[i].get_text() for i in range(n)), encoding="utf-8")
                print(name)


def cmd_score(args, out):
    with (out / "runs.csv").open() as f:
        runs = {Path(r["doc"]).stem: r for r in csv.DictReader(f)}
    rows = []
    for ref in sorted((out / "reference").glob("*.txt")):
        md = out / "md" / f"{ref.stem}.md"
        run = runs.get(ref.stem, {})
        rows.append({
            "doc": ref.stem,
            "pages": int(ref.stem.rsplit("_p", 1)[1]),
            "edit_distance": round(edit_distance(md.read_text(encoding="utf-8"), ref.read_text(encoding="utf-8")), 4) if md.exists() else "",
            "distinct_20": run.get("distinct_20", ""),
            "distinct_35": run.get("distinct_35", ""),
            "gen_tokens": run.get("gen_tokens", ""),
            "model_s": run.get("model_s", ""),
            "peak_mlx_gb": run.get("peak_mlx_gb", ""),
            "complete": run.get("complete", ""),
        })
    with (out / "scores.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} documents scored -> {out / 'scores.csv'}")


def flag_pages(raw, pages_in, finish_reason):
    pages = split_pages(raw)
    flags = {}
    for i in range(pages_in):
        if i >= len(pages):
            flags[i] = "missing"
        elif is_loop(pages[i]):
            flags[i] = "loop"
        elif finish_reason == "length" and i == len(pages) - 1:
            flags[i] = "cut off"
        elif len(remove_det(pages[i])) < 20:
            flags[i] = "empty"
    return flags


def splice(pages, pages_in, replacements):
    pages = (pages + [""] * pages_in)[:pages_in]
    return [replacements.get(i, page) for i, page in enumerate(pages)]


def read_raw(folder):
    return "\n".join(md.read_text(encoding="utf-8") for md in sorted(folder.glob("*.md")))


def cmd_retry(args, out, extra):
    from omnidocbench import run_images

    base = ROOT / "results" / args.base
    with (base / "runs.csv").open() as f:
        runs = {Path(r["doc"]).stem: r for r in csv.DictReader(f)}
    images = out / "inputs"
    images.mkdir(parents=True, exist_ok=True)
    (out / "raw").mkdir(exist_ok=True)
    shutil.copytree(base / "reference", out / "reference", dirs_exist_ok=True)
    flagged = {}
    for stem, run in runs.items():
        finish = run["finish_reasons"].split("|")[-1]
        flags = flag_pages(read_raw(base / "raw" / stem), int(run["pages_in"]), finish)
        flagged[stem] = flags
        with pymupdf.open(base / "inputs" / f"{stem}.pdf") as doc:
            for i in flags:
                doc[i].get_pixmap(dpi=DPI).save(images / f"{stem}__p{i + 1:03d}.png")
    total = sum(map(len, flagged.values()))
    print(f"{total} flagged pages to re-run")
    code = run_images(images, out, extra) if total else 0

    (out / "md").mkdir(exist_ok=True)
    retried, rows = [], []
    for stem, run in runs.items():
        pages_in = int(run["pages_in"])
        replacements, model_s, gen_tokens = {}, float(run["model_s"]), int(run["gen_tokens"])
        complete = True
        for i, reason in flagged[stem].items():
            md = out / "raw" / f"{stem}__p{i + 1:03d}.md"
            meta = json.loads(md.with_suffix(".json").read_text()) if md.exists() else {}
            if md.exists():
                replacements[i] = md.read_text(encoding="utf-8")
            complete = complete and bool(meta.get("complete"))
            model_s += meta.get("elapsed_seconds", 0)
            gen_tokens += meta.get("generation_tokens", 0)
            retried.append({"doc": stem, "page": i + 1, "reason": reason, "model_s": round(meta.get("elapsed_seconds", 0), 2),
                            "gen_tokens": meta.get("generation_tokens", ""), "finish_reason": meta.get("finish_reason", "")})
        pages = splice(split_pages(read_raw(base / "raw" / stem)), pages_in, replacements)
        text = "\n\n".join(p for p in map(remove_det, pages) if p)
        (out / "md" / f"{stem}.md").write_text(text + "\n", encoding="utf-8")
        plain = checks.strip_tags(text)
        rows.append({**run, "pages_out": len(pages), "model_s": round(model_s, 2), "gen_tokens": gen_tokens,
                     "distinct_20": round(checks.distinct_n(plain, 20), 4), "distinct_35": round(checks.distinct_n(plain, 35), 4),
                     "complete": complete if flagged[stem] else run["complete"]})
    for name, table in (("retried.csv", retried), ("runs.csv", rows)):
        if table:
            with (out / name).open("w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=list(table[0]))
                writer.writeheader()
                writer.writerows(table)
    return code


def main(argv=None):
    parser = argparse.ArgumentParser(description="Long-document set: page-prefix inputs with text-layer references.")
    parser.add_argument("step", choices=["make", "score", "retry"])
    parser.add_argument("--exp", required=True)
    parser.add_argument("--base", help="retry: experiment whose flagged pages are re-run one at a time")
    parser.add_argument("sources", nargs="*", type=Path)
    args, extra = parser.parse_known_args(argv)
    out = ROOT / "results" / args.exp
    if args.step == "retry":
        return cmd_retry(args, out, extra)
    return cmd_make(args, out) if args.step == "make" else cmd_score(args, out)


if __name__ == "__main__":
    raise SystemExit(main())
