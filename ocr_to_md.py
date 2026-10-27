import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DET_RE = re.compile(r"<\|det\|>([^<\s]+)(?:\s*\[[^\]]*\])?\s*<\|/det\|>(.*)", re.DOTALL)
PAGE_RE = re.compile(r"<page>", re.IGNORECASE)
# Block types OmniDocBench sets aside when scoring.
PAGE_FURNITURE = ("header", "footer", "page_number", "page_footnote")


def cut_unclosed_marker(line):
    start = line.rfind("<|det|>")
    return line[:start] if start != -1 and "<|/det|>" not in line[start:] else line


# Adapted from remove_det in the Unlimited-OCR README (github.com/baidu/Unlimited-OCR, MIT).
def remove_det(raw, repair=False, skip=()):
    blocks = []
    cur = None
    skipping = False
    for line in raw.splitlines():
        line = (cut_unclosed_marker(line) if repair else line).rstrip()
        if not line:
            continue
        m = DET_RE.match(line)
        if m:
            category, content = m.group(1).strip(), m.group(2).strip()
            skipping = category in skip
            if category == "image" or skipping:
                continue
            if cur is not None:
                blocks.append(cur)
            cur = [content] if content else []
            continue
        if skipping:
            continue
        if cur is None:
            cur = []
        cur.append(line)
    if cur is not None:
        blocks.append(cur)
    return "\n\n".join("\n".join(b) for b in blocks).strip()


def split_pages(raw):
    pages = PAGE_RE.split(raw)
    return pages[1:] if len(pages) > 1 and not pages[0].strip() else pages


def is_empty_row(row_html):
    clean = re.sub(r"<[^>]+>", "", row_html).strip()
    return not clean or clean == "&nbsp;"


def cut_empty_tables(text, max_empty_rows=10, max_page_rows=40):
    def replace_table(match):
        tbl = match.group(0)
        rows = re.findall(r"<tr\b[^>]*>.*?</tr>", tbl, re.DOTALL | re.IGNORECASE)
        if not rows:
            rows = [f"<tr>{r}" for r in re.split(r"<tr\b[^>]*>", tbl, flags=re.IGNORECASE)[1:]]
        empty_count = sum(1 for r in rows if is_empty_row(r))
        if len(rows) > max_page_rows and empty_count / len(rows) > 0.7:
            non_empty = [r for r in rows if not is_empty_row(r)]
            if len(non_empty) <= 3:
                return ""
            return "<table>" + "".join(rows[:max_page_rows]) + "</table>"
        consecutive_empty = 0
        cutoff = None
        for idx, r in enumerate(rows):
            if is_empty_row(r):
                consecutive_empty += 1
                if consecutive_empty > max_empty_rows and cutoff is None:
                    cutoff = idx
            else:
                consecutive_empty = 0
        if cutoff is not None and len(rows) > max_page_rows:
            return "<table>" + "".join(rows[:cutoff]) + "</table>"
        return tbl

    pattern = re.compile(r"<table\b[^>]*>(?:.*?</table>|.*?$)", re.DOTALL | re.IGNORECASE)
    return pattern.sub(replace_table, text)


NUMBER_OR_CHAR = re.compile(r"(\d+)|\D", re.DOTALL)
REPEATED_UNIT = re.compile(r"(.{4,200}?)\1{9,}", re.DOTALL)


def cut_counting_loops(text, keep=3, min_repeats=10, min_bare_repeats=25, min_plain_repeats=50):
    # A block written over and over with only its numbers changing. Compare with every number
    # as #, keep the first few whole copies and drop the rest. Table rows are left alone, and a
    # block with no number in it must repeat many more times, since short lines can repeat for real.
    shape, where = [], []
    for m in NUMBER_OR_CHAR.finditer(text):
        shape.append("#" if m.group(1) else m.group())
        where.append(m.start())
    where.append(len(text))
    shape = "".join(shape)
    out, last, pos = [], 0, 0
    while m := REPEATED_UNIT.search(shape, pos):
        unit = m.group(1)
        copies = (m.end() - m.start()) // len(unit)
        if "#" not in unit:
            needed = min_plain_repeats
        else:
            needed = min_repeats if any(c.isalnum() for c in unit) else min_bare_repeats
        end = m.end()
        if "<t" not in unit.lower() and copies >= needed:
            # The last copy is often unfinished; it goes too.
            while end < len(shape) and end - m.end() < len(unit) and shape[end] == unit[end - m.end()]:
                end += 1
            out.append(text[where[last] : where[m.start() + keep * len(unit)]])
            last = end
        pos = end
    out.append(text[where[last] :])
    return "".join(out)


def cut_consecutive_repeats(text):
    lines = text.split("\n")
    out = []
    prev_line = None
    repeat_count = 0
    for line in lines:
        stripped = line.strip()
        if stripped and stripped == prev_line:
            repeat_count += 1
        else:
            prev_line = stripped if stripped else None
            repeat_count = 1

        if "[non-text]" in stripped.lower() or "[non--text]" in stripped.lower():
            max_allowed = 2
        elif len(stripped) <= 2:
            max_allowed = 1
        elif len(stripped) <= 10:
            max_allowed = 4
        else:
            max_allowed = 6

        if repeat_count <= max_allowed or not stripped:
            out.append(line)
    return "\n".join(out)


def _parse_row_cells(row_html):
    cells = []
    for m in re.finditer(r"<t[dh]\b([^>]*)>(.*?)</t[dh]>", row_html, re.DOTALL | re.IGNORECASE):
        attrs = m.group(1)
        content = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        cspan = 1
        cm = re.search(r'colspan="?(\d+)"?', attrs, re.IGNORECASE)
        if cm:
            cspan = int(cm.group(1))
        rspan = 1
        rm = re.search(r'rowspan="?(\d+)"?', attrs, re.IGNORECASE)
        if rm:
            rspan = int(rm.group(1))
        cells.append((content, cspan, rspan))
    return cells


def _find_table_splits(table_html):
    rows = re.findall(r"<tr\b[^>]*>.*?</tr>", table_html, re.DOTALL | re.IGNORECASE)
    if len(rows) < 8:
        return []

    parsed_rows = [_parse_row_cells(r) for r in rows]
    total_cols = max((sum(c[1] for c in pr) for pr in parsed_rows if pr), default=1)

    h_tokens = set()
    for pr in parsed_rows[:2]:
        for content, _, _ in pr:
            clean = content.lower().strip()
            if len(clean) >= 2 and not clean.isdigit():
                h_tokens.add(clean)

    splits = []
    i = 3
    while i < len(rows) - 2:
        pr = parsed_rows[i]
        if not pr:
            i += 1
            continue

        # Skip if any cell has a large rowspan (> 2) indicating data grouping
        if any(c[2] > 2 for c in pr):
            i += 1
            continue

        # Full-width banner or section header (e.g. US corporate bonds)
        if len(pr) == 1 and pr[0][1] >= total_cols - 1:
            next_pr = parsed_rows[i + 1] if i + 1 < len(rows) else []
            if len(next_pr) >= 2 and not any(c[2] > 2 for c in next_pr):
                splits.append(i)
                i += 3
                continue

        # Multi-level header restart: pr has title cells with colspan >= 3 and next row has matching sub-headers
        next_pr = parsed_rows[i + 1] if i + 1 < len(rows) else []
        next_matched = sum(1 for c, _, _ in next_pr if c.lower().strip() in h_tokens)
        if any(c[1] >= 3 and c[2] <= 2 for c in pr) and next_matched >= 2 and not any(c[2] > 2 for c in next_pr):
            splits.append(i)
            i += 3
            continue

        # Check repeating headers starting at or near column 0
        matched_tokens = sum(1 for c, _, _ in pr if c.lower().strip() in h_tokens)
        left_has_header = any(c[0].lower().strip() in h_tokens or "表" in c[0] for c in pr[:2])

        if left_has_header:
            if matched_tokens >= 3 or (matched_tokens >= 2 and len(pr) <= 5) or (matched_tokens >= 1 and next_matched >= 2):
                splits.append(i)
                i += 3
                continue

        i += 1

    return splits


def split_merged_tables(text):
    def replace_table(match):
        tbl = match.group(0)
        splits = _find_table_splits(tbl)
        if not splits:
            return tbl
        rows = re.findall(r"<tr\b[^>]*>.*?</tr>", tbl, re.DOTALL | re.IGNORECASE)
        chunks = []
        last = 0
        for s in splits:
            chunks.append("<table>" + "".join(rows[last:s]) + "</table>")
            last = s
        chunks.append("<table>" + "".join(rows[last:]) + "</table>")
        return "\n\n".join(chunks)

    pattern = re.compile(r"<table\b[^>]*>.*?</table>", re.DOTALL | re.IGNORECASE)
    return pattern.sub(replace_table, text)


def to_markdown(raw, repair=False, skip=(), cut_loops=False, cut_tables=False, split_tables=False, cut_repeated_lines=False):
    text = "\n\n".join(page for page in (remove_det(p, repair, skip) for p in split_pages(raw)) if page)
    if cut_loops:
        text = cut_counting_loops(text)
    if cut_tables:
        text = cut_empty_tables(text)
    if split_tables:
        text = split_merged_tables(text)
    if cut_repeated_lines:
        text = cut_consecutive_repeats(text)
    return text


def run_model(source, out_dir, extra_args=()):
    source = Path(source)
    flag = "--pdf" if source.suffix.lower() == ".pdf" else "--image"
    cmd = [sys.executable, str(ROOT / "run_ocr.py"), flag, str(source), "--output-dir", str(out_dir), *extra_args]
    started = time.perf_counter()
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    log = proc.stdout.read()
    _, status, usage = os.wait4(proc.pid, 0)
    outputs = []
    for md in sorted(Path(out_dir).glob("*.md")):
        meta = md.with_suffix(".json")
        outputs.append((md.read_text(encoding="utf-8"), json.loads(meta.read_text()) if meta.exists() else {}))
    return {
        "exit_code": os.waitstatus_to_exitcode(status),
        "wall_s": time.perf_counter() - started,
        "peak_rss_gb": usage.ru_maxrss / 1e9,
        "outputs": outputs,
        "log": log,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="OCR a PDF or image to clean Markdown.")
    parser.add_argument("source", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--raw-dir", type=Path, help="Keep the raw model output here")
    args, extra = parser.parse_known_args(argv)

    with tempfile.TemporaryDirectory() as tmp:
        result = run_model(args.source, args.raw_dir or Path(tmp), extra)
    if result["exit_code"] != 0 or not result["outputs"]:
        sys.stderr.write(result["log"])
        return result["exit_code"] or 1
    args.output.write_text("\n\n".join(to_markdown(raw) for raw, _ in result["outputs"]) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
