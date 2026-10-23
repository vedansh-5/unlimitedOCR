import argparse
import json
import shutil
from pathlib import Path

from ocr_to_md import ROOT
from omnidocbench import write_predictions

RESULTS = ROOT / "results"


def confidences(exp):
    out = {}
    for meta in (RESULTS / exp / "raw").glob("*.json"):
        value = json.loads(meta.read_text()).get("mean_logprob")
        if value is not None:
            out[meta.stem] = value
    return out


def choose(confidence, runs):
    pages = confidence[runs[0]]
    return {page: max(runs, key=lambda r: confidence[r].get(page, float("-inf"))) for page in pages}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Per page, keep the output of the run the model was most confident in.")
    parser.add_argument("--exp", required=True)
    parser.add_argument("--runs", nargs="+", required=True, help="Experiments over the same pages, first one is the default")
    args = parser.parse_args(argv)
    out = RESULTS / args.exp
    (out / "raw").mkdir(parents=True, exist_ok=True)
    for name in ("subset.txt", "gt_subset.json"):
        shutil.copy(RESULTS / args.runs[0] / name, out / name)
    picks = choose({r: confidences(r) for r in args.runs}, args.runs)
    for page, run in picks.items():
        for suffix in (".md", ".json"):
            shutil.copy(RESULTS / run / "raw" / f"{page}{suffix}", out / "raw" / f"{page}{suffix}")
    (out / "picks.json").write_text(json.dumps(picks, indent=2, ensure_ascii=False) + "\n")
    counts = {r: list(picks.values()).count(r) for r in args.runs}
    print(f"{len(picks)} pages: {counts}")
    return write_predictions(out, 0)


if __name__ == "__main__":
    raise SystemExit(main())
