# Plan

## Machine (checked 2026-10-23)

| Item | Value | What it means |
|---|---|---|
| Mac | MacBook Air, Apple M5, 10 cores, **16 GB** | Model weights alone are 6.7 GB (BF16). The port recommends 32 GB+ for long PDFs. |
| OS | macOS 27.0.1, arm64 | Fine. |
| Disk | 208 GB free | Fine (checkpoint ~6.7 GB). |
| uv | **missing** | Install with `brew install uv`. |
| Python | 3.14.7 (Homebrew) | Pin the project to 3.12 through uv. Upstream was tested on 3.12; 3.14 wheels for mlx / mlx-vlm 0.6.16 are not certain. |
| Already present | git, tesseract, pdftoppm | Tesseract helps the later eval-harness option. |
| HF cache | no Unlimited-OCR weights yet | First run downloads `baidu/Unlimited-OCR` at the pinned revision. |

Fanless Air: long runs will slow down from heat. Timings in the CSV get a
start timestamp and run order, so the report can mention this.

## What the MLX port actually does (read from its source)

- CLI `unlimited-ocr-mlx` (entry `infer_mlx:main`), pins `mlx-vlm==0.6.16`, Python >=3.10.
- Loads `baidu/Unlimited-OCR` at revision `07dea832...`. No separate MLX weights.
- `--pdf` renders pages at `--dpi 300` and sends **all pages in one request** unless
  `--max-pages-per-request N` is set. Each chunk is an independent request.
- Writes `<stem>_pages_00001-00012.md` (raw model text, markers included) plus a
  `.json` sidecar: `elapsed_seconds, prompt_tokens, generation_tokens, prompt_tps,
  generation_tps, peak_memory_gb, finish_reason, image_count, mode, complete`.
- Exit codes: 0 ok, 2 bad input/runtime error, 3 hit `--max-tokens` (incomplete), 130 Ctrl-C.
- Decoding: temperature 0, no-repeat 35-gram guard, window 128 (single image) or 1024 (multi-page).
  Matches the upstream README settings. Whether the guard and the R-SWA cache match the
  upstream code is **not yet checked** (see 1.2).

## Step 1

### 1.1 Environment
- `brew install uv`, `git init` (local only, no remote), add `rules.md` to `.git/info/exclude`.
- `uv init` a project pinned to Python 3.12.
- Add the wrapper as a **git dependency pinned to one commit** of
  `https://huggingface.co/shubhxho/Unlimited-OCR-MLX`. Teammates get the same version,
  and there is no copied code in our repo to keep in sync.
- Smoke test: `uv run unlimited-ocr-mlx --pdf <one short pdf> --output-dir results/raw`.

### 1.2 Check the unverified parts (reading only, about 30 min)
- Compare the port's no-repeat processor with upstream `SlidingWindowNoRepeatNgramProcessor`
  (in the `baidu/Unlimited-OCR` model repo code).
- Find where mlx-vlm 0.6.16 implements the R-SWA decode cache and compare with upstream.
- Check how multi-page output marks page breaks, if at all. This decides whether per-page
  retry is possible later.
- Findings go in `docs/findings.md`.

### 1.3 `ocr_to_md.py`
- `run_model(pdf, out_dir, max_pages_per_request, dpi)`: calls the wrapper CLI as a
  subprocess and collects its `.md` and `.json` files.
- `remove_det(raw)`: the upstream function, adapted (adds the missing `import re`; drops
  `image` blocks as upstream does).
- CLI: `uv run python ocr_to_md.py file.pdf -o out.md`.
- Test: `tests/test_remove_det.py` on a hand-written raw sample (no model needed).

Why a subprocess and not importing the wrapper's functions:
- Each document gets its own process, so peak memory is measured per document.
- A crash or out-of-memory kill on one file does not stop the batch.
- Cost: the model reloads per document (seconds to tens of seconds). Logged separately as
  wall time minus model time.

### 1.4 Test documents in `tests/data/`
Target 6 to 8 files, with `tests/data/SOURCES.md` listing origin and licence of each:

| Kind | Candidate |
|---|---|
| 50+ page PDF | A long public-domain report or book scan (e.g. Internet Archive) |
| Scanned forms (2) | FUNSD sample pages, or your own phone scans |
| Tables + math | An arXiv paper with equations and tables |
| Two-column layout | A conference paper |
| Low quality scan | A skewed or noisy scan |
| Short control | A clean 1 to 2 page digital PDF |

### 1.5 `run_batch.py` and `checks.py`
`run_batch.py` loops over `tests/data/`, calls `ocr_to_md`, writes `results/md/` and
appends one row per document to `results/runs.csv`.

CSV columns:
`doc, pages, chunks, started_at, wall_s, model_s, prompt_tokens, gen_tokens, gen_tps,
peak_mlx_gb, peak_rss_gb, exit_code, complete, repetition_flag, table_flag, empty_chunks, error`

- `peak_mlx_gb`: from the wrapper's JSON (memory MLX allocated on the GPU side).
- `peak_rss_gb`: from `os.wait4` on the child process. Logged both because on Apple
  Silicon the two do not always agree.

`checks.py` (pure functions, unit tested):
- **Truncated**: `complete == false` or exit code 3.
- **Repetition loop**: the guard only bans exact 35-token repeats inside its window, so
  loops with small changes or a longer cycle still get through. Flag when one non-empty
  line repeats more than N times, or when the text compresses unusually well (zlib ratio).
- **Garbled table**: rows in one table with different cell counts.
- **Empty chunk**: a request that returned almost no text for its pages.
Thresholds are starting guesses and get tuned on the real outputs; the CSV keeps the raw
numbers, not only the yes/no flags.

### 1.6 Defaults for 16 GB
- `--max-pages-per-request 8` (also keeps output under the 32768 `--max-tokens` cap; a
  dense 50-page doc in one request would likely be cut off).
- `--prefill-step-size 512` if memory is tight.
- DPI stays 300 to match upstream (base mode resizes to 1024 anyway; DPI mainly costs render time).

### 1.7 Docs
`README.md` (setup and run). Project record in `docs/`: `summary.md` (status, best
result, next), `experiment_log.md` (dated decisions and reasons), `findings.md` (one
entry per experiment), `report.md` (report-ready text).

Code layout after Step 1:
```
pyproject.toml  uv.lock
ocr_to_md.py    run_batch.py    checks.py
tests/test_remove_det.py  tests/test_checks.py  tests/data/
results/        (raw/ md/ runs.csv; raw outputs gitignored)
README.md
docs/plan.md  docs/summary.md  docs/experiment_log.md  docs/findings.md  docs/report.md
```
Teammate split later: model runner, post-processing, failure checks, batch and logging.

## Experiments (added 2026-10-23, after the scope widened to "improve on the paper")

No training or fine-tuning (decided 2026-10-23). The released weights stay fixed; every
change is inference-time.
One variable changes per experiment. Every run logs config, model and port revisions,
and raw outputs under `results/<experiment id>/`; nothing is overwritten.

### Baselines (must come first)

| ID | What | Why | Rough cost |
|---|---|---|---|
| E-001 | One page (gundam) and one short PDF (base), default settings | Measures seconds per page and peak memory, which sets the budget for everything else | ~30 min plus 6.7 GB download |
| E-002 | Fixed OmniDocBench v1.6 subset, 15 pages per type, 140 pages, official evaluator without CDM | First parity check of MLX against the paper (v1.6 row) and the official leaderboard | About 35 to 60 min (from E-001 timings) |
| E-003 | Own long-document set (2, 5, 10, 20, 40+ pages) from born-digital PDFs, text layer as reference; Distinct-20/35 and edit distance | Reproduces the shape of the paper's Table 3; needed for the loop work | Guess 2 to 4 h |

The full OmniDocBench v1.6 run (1,651 pages) is only for final numbers. At 15 to 25 s
per page (E-001) it is about 7 to 11.5 h, so it runs overnight once, near the end.

### Improvement candidates, ranked

| Rank | ID | Change | Targets | Why it may help |
|---|---|---|---|---|
| 1 | I-1 | Loop detection (`loops.py`: a block repeated 6+ times with box coordinates ignored, or an unclosed marker) plus retry of only the flagged pages with a coordinate-blind repeat guard (`--content-guard`) | OmniDocBench text edit on looping pages; long-doc edit distance and Distinct-n | E-002 showed the 35-gram guard misses loops because each repeat has new box coordinates. Multi-page: retry flagged pages alone in gundam mode (the paper blames Base-mode resolution) |
| 2 | I-2 | 8-bit and 4-bit quantization of the decoder | Memory and speed on 16 GB | MoE decoding reads expert weights for every token; smaller weights mean less to read. Accuracy cost measured on E-002 |
| 3 | I-3 | Fewer active experts per token (6 to 4) and expert-usage profiling | Speed | Tests whether OCR needs all 6 experts. MoE-specific; reverted if accuracy drops beyond a set margin |
| 4 | I-4 | Page grouping: chunk size and overlap across `--max-pages-per-request` | Long-doc accuracy and peak memory | Chunks break R-SWA's continuity; sizes are a guess today |
| 1b | I-6 | Cut unclosed `<|det|>` markers from the Markdown (`--repair-markers`) | Text edit on pages where the model broke its own format | E-002 had a half-written marker leaking into the output. Post-processing only, so it is rescored without a model run; reported separately from Baidu's `remove_det` |
| 5 | I-5 | Newer dependencies, one at a time: `mlx` 0.32.1 to latest first, then Pillow and transformers | Speed; accuracy checked for drift | Newer MLX may have faster kernels. Weights are unchanged, so accuracy should not move; Pillow (image resizing) and tokenizer changes could shift it slightly |

Deferred: Tesseract comparison, API models. Each needs a separate go. Training is out
of scope.
