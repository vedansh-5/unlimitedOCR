# Experiment log

Chronological. One entry per meaningful action or decision.

## 2026-10-23: Project start, Step 1 plan

- **Task:** run Unlimited-OCR on the Mac and log per-document runtime, memory and
  failures.
- **Instruction:** use the community MLX port, do not reimplement the model; explain
  design choices before implementing; small reviewed steps; no web UI.
- **Action:** checked the machine (M5, 16 GB, macOS 27.0.1, uv missing, Python 3.14.7)
  and wrote the Step 1 plan in `docs/plan.md`.
- **Decision:** call the port's CLI as a subprocess per document, so peak memory is
  measured per document and one crash does not stop a batch.
- **Outcome:** plan proposed, awaiting approval.

## 2026-10-23: Scope widened to "improve on the paper"

- **Instruction:** improve performance beyond the paper's reported results; establish
  a baseline first; keep `report.md`, `summary.md`, `findings.md`, `experiment_log.md`
  current; change one variable at a time; no API models yet.
- **Action:** read the paper (arXiv 2606.23050), the model `config.json`, and the MLX
  port's README, TRAINING notes and CLI (R-001 in `findings.md`).
- **Result:** decoder confirmed as MoE (64 experts, top-6). Paper gains came from GPU
  cluster training. The port states LoRA training does not fit in 16 GB.
- **Decision (proposed):** keep Step 1 as the base. Add an OmniDocBench baseline as
  E-002, and rank inference-time improvements first. Training-based ideas are deferred
  unless more memory or a paid GPU is approved.
- **Docs:** created `docs/report.md`, `docs/summary.md`, `docs/findings.md`, this log.
  `docs/decisions.md` and `STATUS.md` from the first plan are dropped; this log and
  `summary.md` replace them.
- **Outcome:** awaiting approval of the plan and first experiment.

## 2026-10-23: No training

- **Instruction:** do not train or fine-tune the model. Use the released weights as
  published; improve only what happens around the model.
- **Decision:** LoRA and any other training are removed from the plan, not deferred.
  All improvements are inference-time: input preparation, decoding settings, page
  grouping, failure detection and retry, output cleanup, quantization, expert count.
- **Consequence:** results are compared against the paper on equal weights. Any gain
  is attributable to the pipeline, not to new training data.

## 2026-10-23: Contained setup, pinned versions, public repo

- **Instruction:** everything must be removable with one command and must not touch
  the system or other dev environments; use a folder named `unlimitedOCRvenv`.
- **Action:** uv installed into `unlimitedOCRvenv/uv` (a venv made with the system
  python3); Python 3.12.15, packages, uv cache and Hugging Face cache all redirected
  into `unlimitedOCRvenv/` through `env.sh`. Removal: `rm -rf unlimitedOCRvenv`.
- **Finding:** a plain `uv sync` resolved newer packages than the port was tested with
  (e.g. huggingface-hub 2.2.0 vs 1.28.0, pillow 13.0.0 vs 12.3.0, mlx 0.32.4 vs
  0.32.1).
- **Decision:** constrain every package to the port's own `uv.lock` (Python 3.12
  entries) so the baseline matches the port's tested environment. Newer versions
  become experiment I-5, tested after the baseline, one package at a time.
- **Instruction:** publish the project as a public GitHub repository.
- **Action:** created `vedansh-5/unlimitedOCR` (public). `rules.md`, the venv folder and
  rendered inputs are not committed.

## 2026-10-23: E-001 first attempt failed; port bug fixed locally

- **Problem:** the first model run crashed on its first generated token.
- **Action:** traced it to a shape bug in the port's no-repeat guard (details in
  `findings.md`, E-001a). Added a failing test, then `run_ocr.py`, which fixes the
  output shape and otherwise runs the port's CLI unchanged.
- **Decision:** fix in our repo instead of editing installed packages, so the fix is
  versioned, visible and reproducible. All runs now go through `run_ocr.py`.
- **Outcome:** test passes; E-001 rerun started.

## 2026-10-23: E-001 done

- **Result:** both runs completed. 17 s for a dense gundam page, about 8 s per page in
  base mode, peak 9.6 GB. Details and quality notes in `findings.md`, E-001.
- **Issues found:** text missing or made up at the start of the output in both runs;
  `/usr/bin/time` around `uv run` does not measure the model process.
- **Decision:** E-002 (OmniDocBench subset) is affordable at under an hour. The batch
  runner will launch the venv Python directly so process memory is measured correctly.
- **Results:** `results/E-001/`.

## 2026-10-23: E-001b, second port bug; pipeline code

- **Problem:** E-001 output had errors at the very start (missing paragraph, made-up
  date).
- **Action:** compared the port's prompt tokens with Baidu's `infer()`; the port adds a
  trailing space token. Ran E-001b with only that removed.
- **Outcome:** both errors gone; the rest of the output unchanged (findings E-001b).
- **Decision:** Baidu's exact prompt is the default from now on. This is a fidelity fix,
  not an improvement: it brings the setup closer to the paper's conditions.
- **Instruction:** report both port bugs on the port's Hugging Face page, written
  plainly. Draft ready; posting waits on a Hugging Face login.
- **Action:** added `ocr_to_md.py` (runs the model in a separate process, splits pages
  at `<PAGE>`, strips markers with Baidu's `remove_det`) and `checks.py` (repeat,
  compression, Distinct-n, ragged tables, empty pages), with tests.

## 2026-10-23: E-002 setup (OmniDocBench)

- **Decision: v1.6, not v1.5.** The evaluator's current code is v1.6 (`omnidocbench-eval
  1.6.0`, commit `f133a71`); the paper reports v1.6 (93.92 overall); and the official
  OmniDocBench leaderboard independently lists Unlimited-OCR on v1.6_full at 94.00
  overall, Text Edit 0.0394, CDM 95.72, TEDS 90.21, TEDS-S 93.36, Read-order Edit 0.128.
  v1.5 would only add the DeepSeek-OCR comparison, which this project does not need.
  Dataset revision `aa1ee96` (1,651 pages, 10 document types).
- **Decision: no CDM for now.** CDM needs Linux, TeX Live, ImageMagick and Ghostscript,
  which do not fit a contained macOS setup. Text Edit, Table TEDS / TEDS-S, Read-order
  Edit and formula Edit distance are measured; Formula CDM and Overall are reported as
  not measured.
- **Subset:** 15 pages per document type (all 5 of `historical_document`), seed 42, 140
  pages. Selection code: `omnidocbench.py select`; list in `results/E-002/subset.txt`.
- **Evaluator environment:** Python 3.11 venv at `unlimitedOCRvenv/omnidocbench-env`.
  Its pins leave `pyarrow` and `datasets` open; the newest `pyarrow` needs NumPy 2 while
  the evaluator pins NumPy 1.24.4. Resolved with `--exclude-newer 2025-09-26` (the v1.5
  evaluation-code release date). Exact versions: `results/omnidocbench-env-freeze.txt`.
- **Containment:** `NLTK_DATA` added to `env.sh` so the METEOR metric's data stays in
  `unlimitedOCRvenv/`.

## 2026-10-23: Port bugs reported upstream

- **Action:** reported both port bugs (decode crash, trailing prompt space) with a
  minimal repro and a suggested fix:
  https://huggingface.co/shubhxho/Unlimited-OCR-MLX/discussions/1
- **Next:** if the port fixes them, drop the matching patches from `run_ocr.py` and pin
  the new port commit, after checking the output is unchanged.

## 2026-10-23: Faster iteration, dev/test split

- **Problem:** about 30 min per 140-page run makes a dozen experiments cost 6 h.
- **Instruction:** work on all four speed-ups: a small dev subset, re-running only
  affected pages, rescoring without a model run when only post-processing changes, and
  batching. No queued background runs unless asked. No training.
- **Decision:** E-002 (140 pages) is the test baseline and is not re-run until final
  confirmation. Ideas are tried on a 45-page dev subset (5 per document type) drawn from
  pages outside E-002, so the test numbers stay unbiased.
- **Order:** E-001c (prefill chunking check), then batching checked for identical output
  against about 20 E-002 pages, then the dev baseline (with batching if it passed), then
  improvements.
- **Rejected:** running several model processes in parallel. One GPU is the bottleneck
  and two copies (about 9.6 GB each) do not fit in 16 GB.
- **Rejected for speed:** quantization as a speed-up for other experiments, because it
  changes outputs; it stays a separate experiment (I-2 in the plan).

## 2026-10-23: Batching postponed

- **Finding:** mlx-vlm's batch path drops R-SWA (findings R-003), so batching needs a
  custom batch cache (about half a day, 1.5 to 2x expected).
- **Instruction:** skip batching for now; suggest it again if runs feel slow.
- **Decision:** speed comes from the dev subset, re-running only affected pages, and
  rescoring without model runs.

## 2026-10-23: E-002 done

- **Result:** reproduction confirmed. Reweighted Text Edit 0.036 [0.024, 0.051], TEDS
  92.4 [88.7, 95.7], Read-order 0.107 [0.078, 0.143]; paper and leaderboard values all
  inside the intervals (findings E-002, report 5.1).
- **Found:** 2 looping pages (historical documents); the 35-gram guard misses them
  because box coordinates change per repeat. This sets the design of I-1.
- **Fixed:** loop checks now ignore HTML tags (a sparse table had looked like a loop).
- **Repo:** benchmark ground truth and evaluator files that quote it are not
  committed; our predictions, scores and configs are.
- **Next:** E-001c, then the dev baseline (E-004), then E-003.

## 2026-10-23: E-001c done

- **Result:** disabling chunked prefill changed one box coordinate by 1 on page 10 and
  nothing else (findings E-001c).
- **Decision:** keep the default; the deviation is measured and negligible here.

## 2026-10-23: Fixes for what E-002 found

- **Instruction:** be fix-oriented: after each test, implement the fix for what it
  found and measure it.
- **I-1 (loops):** `loops.py` detects loops on raw output with box coordinates ignored
  (6+ repeats of one block, or an unclosed marker; threshold fixed in advance, not
  tuned on test pages). On E-002 it flags exactly the 2 real loops and nothing else.
  `ContentNoRepeatGuard` applies Baidu's 35-gram rule to the text with `<|det|>` spans
  removed; `run_ocr.py --content-guard` enables it. `omnidocbench.py retry` copies a
  baseline's clean pages and re-runs only flagged ones with the guard.
- **I-6 (broken markers):** `to_markdown(repair=True)` cuts unclosed `<|det|>`
  markers. Behind `--repair-markers` so the baseline keeps Baidu's exact post-processing;
  `omnidocbench.py rescore` applies it without a model run.
- **Order:** dev (E-004) first, then test (E-002). If the dev subset has no flagged
  pages, the fix is applied to the test pages directly, since nothing is tuned.

## 2026-10-23: E-004, E-005, E-006 (dev baseline and loop repair)

- **E-004 dev baseline:** Text Edit 0.0526, TEDS 93.5, R-order 0.134. One newspaper page
  looped 555 times and hit the token cap (377 s).
- **E-005 (I-1 on dev):** the looping page re-run with the coordinate-blind guard
  finished in 19 s; dev Text Edit 0.0526 to 0.0422.
- **E-006 (I-1 on test):** the 2 looping pages are unreadable vertical Chinese scans;
  repetition dropped but text stayed wrong. Test Text Edit 0.0589 to 0.0587, R-order
  0.1271 to 0.1286.
- **Decision:** keep I-1 (helps runaway loops, neutral otherwise, saves time).
- **Instruction:** user going to sleep; stop at a clean point, no long run overnight.
  E-003 deferred to the next session.
- **E-007 (I-6 on test):** marker repair changed only the broken page and moved no
  metric. Kept as an output-cleaning option, not reported as an improvement.
- **Correction:** E-006 per-page values were first attributed to the wrong pages;
  fixed after re-checking by page name. Totals unchanged.

## 2026-10-23 (morning): E-003 started, compare.py, I-1L code

- **E-003** (long-document baseline, 15 NIST prefixes, defaults) started.
- **compare.py** added (R-004). Reproduces the report's E-002 numbers exactly. Paired
  differences for I-1 and I-6 recorded in findings.
- **I-1L code:** `long_docs.py retry --base E-003` flags missing, looping, cut-off and
  empty pages from the base run's output (never from the reference), renders each
  flagged page at 300 dpi, re-runs them in one model call (gundam mode, single page),
  and splices them back in place. Tests for flagging and splicing.
- **E-003 done** (37.8 min model time): wrong page count in 10 of 15 documents (corrected from 9), 2 of 3
  40-page documents hit the 32,768-token cap, recall 0.95 to 0.92 with length. Details
  in findings. `run_batch.py` fixed to keep output of capped requests; word recall
  added to `long_docs.py score`.
- **Plan change:** I-1L (positional splice) dropped as unsound under page shifts;
  replaced by E-009, page-by-page Gundam over the first 40 pages of each source
  (`long_docs.py retry --exp E-009 --base E-003 --all-pages`), about 30 to 35 min.
- **E-009 done** (31.2 min model time): page-by-page Gundam beats one request per
  document from 5 pages up (40 pages: edit 0.228 to 0.062, recall 0.917 to 0.967,
  model time 502 to 337 s, no shifts, no cap). Mode and batching changed together, so
  **E-010** (page by page in Base mode, about 15 min) was started to separate them.
- **E-010 false start:** `long_docs.py` took the word `base` in `--mode base` as a
  source file name (catch-all positional argument for `make`), so the model got a bare
  `--mode` and exited at once; `retry` then assembled and scored empty output. Fixed:
  only `make` reads file names, and `retry` stops when the model run fails. Test added.
  The empty outputs were deleted and E-010 restarted; checked that pages run in Base
  mode.
- **E-010 done** (23.6 min): page by page in Base mode matches Gundam on recall and
  nearly on edit distance, and is the fastest (40 pages: 283 s against 337 s Gundam and
  502 s one request). Page splitting is the gain; mode is a small speed/accuracy
  trade. Kept as I-8.
- **E-011** (8-bit on dev): 1.6x output speed, -2.7 GB peak; one page lost to a
  `[Non-Text]` loop (TEDS -5.6, interval touching zero).
- **E-012** (8-bit + loop repair with 8-bit): loop stopped, table still missing.
- **E-013** (8-bit + bf16 fallback on flagged pages): matches bf16 + I-1 on every
  metric (all paired intervals contain zero, all within 0.003 edit / 0.1 TEDS), 33%
  less model time. Kept.
- **E-014/E-015** (4-bit on dev, then with bf16 fallback): fastest (395 s against 740 s)
  but tables lose 4.7 TEDS with an interval excluding zero, from pages that do not
  loop. Rejected. Retry now also flags pages cut off at the token cap (gap found
  here).
- **E-016** (4 experts per token, bf16, dev): ties bf16 + loop repair on every metric,
  16% faster per page. Kept. 5 experts skipped (dominated).
