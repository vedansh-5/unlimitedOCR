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


def to_markdown(raw, repair=False, skip=()):
    return "\n\n".join(page for page in (remove_det(p, repair, skip) for p in split_pages(raw)) if page)


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
