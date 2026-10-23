import argparse
import json
import random
import statistics
from collections import defaultdict
from pathlib import Path

from ocr_to_md import ROOT

# Pages per data_source in OmniDocBench v1.6 (dataset revision aa1ee96), 1,651 in all.
FULL_SET = {
    "book": 276, "PPT2PDF": 253, "academic_literature": 215, "exam_paper": 193, "colorful_textbook": 159,
    "newspaper": 151, "magazine": 149, "research_report": 132, "note": 118, "historical_document": 5,
}
PAGE_METRICS = ("text_block", "reading_order")
TABLE_METRICS = {"table_TEDS": "TEDS", "table_TEDS_S": "TEDS_structure_only"}
RESAMPLES = 2000


def result_file(exp, name):
    return json.loads((ROOT / "results" / exp / "eval" / "result" / f"pred_quick_match_{name}.json").read_text())


def page_types(exp):
    gt = json.loads((ROOT / "results" / exp / "gt_subset.json").read_text())
    return {Path(p["page_info"]["image_path"]).name: p["page_info"]["page_attribute"]["data_source"] for p in gt}


def page_scores(exp, metric):
    return result_file(exp, f"{metric}_per_page_edit")


# Each page's tables are averaged first, as in the evaluator's page-level headline.
def page_means(tables):
    pages = defaultdict(list)
    for key, value in tables.items():
        pages[key.rsplit("_[", 1)[0]].append(value)
    return {page: statistics.mean(values) for page, values in pages.items()}


def table_scores(exp, key="TEDS"):
    return page_means({k: v[key] for k, v in result_file(exp, "table_per_table_TEDS").items()})


def by_type(values, types):
    groups = defaultdict(list)
    for name, value in values.items():
        groups[types[name]].append(value)
    return groups


def reweighted(groups):
    total = sum(FULL_SET[k] for k in groups)
    return sum(FULL_SET[k] * statistics.mean(v) for k, v in groups.items()) / total


def pooled(groups):
    return statistics.mean(v for values in groups.values() for v in values)


# Stratified percentile bootstrap: pages are resampled within each type.
def interval(stat, groups, n=RESAMPLES, seed=0):
    rng = random.Random(seed)
    boots = sorted(stat({k: rng.choices(v, k=len(v)) for k, v in groups.items()}) for _ in range(n))
    return boots[int(0.025 * n)], boots[int(0.975 * n) - 1]


def paired(before, after):
    return {k: after[k] - before[k] for k in before if k in after}


def estimate(stat, groups, scale=1):
    lo, hi = interval(stat, groups)
    return {"value": round(stat(groups) * scale, 4), "ci95": [round(lo * scale, 4), round(hi * scale, 4)],
            "n": sum(map(len, groups.values()))}


def cmd_score(args):
    types = page_types(args.exp)
    stats = {m: estimate(reweighted, by_type(page_scores(args.exp, m), types)) for m in PAGE_METRICS}
    for name, key in TABLE_METRICS.items():
        stats[name] = estimate(pooled, {"all": list(table_scores(args.exp, key).values())}, scale=100)
    return stats


def cmd_diff(args):
    types = page_types(args.exp)
    stats = {m: estimate(reweighted, by_type(paired(page_scores(args.base, m), page_scores(args.exp, m)), types))
             for m in PAGE_METRICS}
    for name, key in TABLE_METRICS.items():
        diffs = paired(table_scores(args.base, key), table_scores(args.exp, key))
        stats[name] = estimate(pooled, {"all": list(diffs.values())}, scale=100)
    return stats


def main(argv=None):
    parser = argparse.ArgumentParser(description="OmniDocBench subset scores reweighted to the full set, with 95% bootstrap intervals.")
    parser.add_argument("step", choices=["score", "diff"])
    parser.add_argument("--exp", required=True)
    parser.add_argument("--base", help="diff: the experiment to subtract (paired by page)")
    args = parser.parse_args(argv)
    stats = cmd_score(args) if args.step == "score" else cmd_diff(args)
    name = "stats.json" if args.step == "score" else f"diff_vs_{args.base}.json"
    (ROOT / "results" / args.exp / name).write_text(json.dumps(stats, indent=2) + "\n")
    for metric, s in stats.items():
        print(f"{metric:14} {s['value']:9.4f}  [{s['ci95'][0]:.4f}, {s['ci95'][1]:.4f}]  n={s['n']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
