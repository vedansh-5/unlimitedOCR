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


def cut_counting_loops(text, min_repeats=10, keep=3, max_k=10):
    parts = re.split(r"(\d+)", text)
    non_digits = parts[0::2]
    n = len(non_digits)
    i = 0
    kept_parts = []
    while i < n:
        best_k, best_reps = None, 0
        for k in range(1, max_k + 1):
            if i + 2 * k > n:
                continue
            chunk = non_digits[i : i + k]
            raw_chunk = "".join(chunk)
            if any(t in raw_chunk.lower() for t in ("<td", "<tr", "<table")):
                continue
            stripped = raw_chunk.strip()
            if not stripped:
                continue
            thresh = 25 if not any(c.isalnum() for c in stripped) else min_repeats
            reps = 1
            idx = i + k
            while idx + k <= n and non_digits[idx : idx + k] == chunk:
                reps += 1
                idx += k
            if reps >= thresh and reps > best_reps:
                best_k = k
                best_reps = reps
        if best_k is not None:
            keep_count = min(keep, best_reps)
            for j in range(i, i + best_k * keep_count):
                kept_parts.append(parts[2 * j])
                if 2 * j + 1 < len(parts):
                    kept_parts.append(parts[2 * j + 1])
            i += best_k * best_reps
        else:
            kept_parts.append(parts[2 * i])
            if 2 * i + 1 < len(parts):
                kept_parts.append(parts[2 * i + 1])
            i += 1
    return "".join(kept_parts)


def to_markdown(raw, repair=False, skip=(), cut_counting_loops_opt=False, cut_empty_tables_opt=False, **kwargs):
    cut_loops = cut_counting_loops_opt or kwargs.get("cut_counting_loops", False)
    cut_tables = cut_empty_tables_opt or kwargs.get("cut_empty_tables", False)
    text = "\n\n".join(page for page in (remove_det(p, repair, skip) for p in split_pages(raw)) if page)
    if cut_loops:
        text = cut_counting_loops(text)
    if cut_tables:
        text = cut_empty_tables(text)
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
