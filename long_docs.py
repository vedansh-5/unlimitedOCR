import argparse
import csv
import re
from pathlib import Path

import pymupdf
from rapidfuzz.distance import Levenshtein

import checks
from ocr_to_md import ROOT

BUCKETS = (2, 5, 10, 20, 40)
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


def main(argv=None):
    parser = argparse.ArgumentParser(description="Long-document set: page-prefix inputs with text-layer references.")
    parser.add_argument("step", choices=["make", "score"])
    parser.add_argument("--exp", required=True)
    parser.add_argument("sources", nargs="*", type=Path)
    args = parser.parse_args(argv)
    out = ROOT / "results" / args.exp
    return cmd_make(args, out) if args.step == "make" else cmd_score(args, out)


if __name__ == "__main__":
    raise SystemExit(main())
