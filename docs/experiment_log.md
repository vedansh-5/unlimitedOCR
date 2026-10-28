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
- **E-017/E-018** (8-bit + 4 experts, then bf16 fallback, dev): matches bf16 + loop
  repair (TEDS +0.9 [0.04, 1.9]), 38% less model time. Candidate final setup.
- **E-019/E-020** started: final setup on the 140-page test subset, about 30 min.
- **E-019 to E-021** (fast setup on test): worse before fallback; with fallback and a
  new empty-page rule, within noise of bf16 but leaning worse, 26% faster. Decision:
  bf16 + loop repair for accuracy runs; fast setup as a speed option.
- **E-022** (drop page furniture): slightly worse. Rejected.
- **Error analysis:** newspapers and notes dominate text error; worst reading-order
  pages are a metric quirk (single-item pages). Next idea: higher resolution for small
  print.
- **E-023 to E-025** (best of two by confidence, dev): logging verified harmless
  (identical output); confidence pick 0.0497 against 0.0504 Gundam, ceiling 0.0404.
  Rejected. Single-page accuracy ideas exhausted for now; see findings summary.
- **Memory cap** (user request: keep under 8 GB): crop grouping, row-chunked SAM
  attention, 256 MB cache. Footprint 10 GB to 7.75 GB. E-026/E-029 on dev: rounding
  differences only; one fragile page (crossword) tips worse.
- **Full run approved** by the user (with formula CDM, under 8 GB). Started as E-027
  (`results/E-027/run.sh`): select all 1,651 pages, fetch, predict with the cap, retry
  flagged pages (E-028), local evaluation, then CDM in Docker.
- **Restarted** the full run after making image fetching parallel (8 at a time); the first start was downloading about 30 images a minute.
- **Stops and resumes** (user requests): scoring has no saved progress, so the first stop
  lost 3 h of matching. Added `match_cache.py` (per-page match cache). The last two pages
  then took over an hour: the evaluator starts a fresh Python process for every
  LaTeX-to-text call, about 2 s each on macOS, and both pages are counting loops. Short
  formulas are now converted in place and results kept: E-004 rescored in 13 s instead of
  4 min 19 s, result files identical.
- **E-028 scored** (1,651 pages, no CDM): Text Edit 0.051, TEDS 87.8, TEDS-S 91.5,
  R-order 0.137. Worse than the paper (0.042, 90.2, 93.3, 0.129) and worse than our
  140-page test runs on the same pages (+0.014 Text Edit). 36 pages scoring 0.5 or worse
  carry 37% of the text error. CDM deferred by the user. Fix ideas in `fixes.md`.
- **E-030** (problem set baseline, 50 pages): explicit selection added (`select --pages`),
  50 problem pages populated from E-028 output and scored. Text Edit 0.6846, Table TEDS 29.33.
- **E-031** (I-9 `--cut-counting-loops` on problem set): Text Edit -0.0024 [-0.0057, 0.0000],
  three severe loop pages improved (-0.053, -0.024, -0.014), none degraded. Kept.
- **E-032** (I-10 `--cut-empty-tables` on problem set): Daily Star page 60 drops from 0.9996
  to 0.3714 (-0.6282). Text Edit -0.0032 [-0.0096, 0.0000]. Kept.
- **E-033** (dev E-029 rescored with kept fixes): Text Edit -0.0115 [-0.0346, 0.0000] down to
  0.0438 [0.0206, 0.0756]. Recovers memory cap regression on dev.
- **E-034** (full E-028 rescored with kept fixes): Text Edit -0.0004 [-0.0012, -0.0000] down
  to 0.0496. 1,639 pages byte-identical, only 12 changed.
- **I-11 code** (number-blind loop check and repeat guard): implemented and unit tested.
  Adds 8 newly flagged pages on E-028 (57 vs 49). 22 problem-set pages flagged for retry.
- **E-039** (I-11 retry on problem set, 50 pages, `--memory-limit-gb 7.5`): retried 22 flagged pages
  with number-blind guard, bounded row cells (`MAX_ROW_CELLS = 35`), and `--ngram-window 512`.
  All 22 pages stopped cleanly without length cap. Peak memory 7.30 to 7.74 GB.
  Text Edit -0.1210 [-0.2384, -0.0044] (0.6846 -> 0.5636). Table TEDS +1.2287 [-1.0787, 4.0413] (29.33 -> 30.56).
  Reading-order Edit -0.0534 (0.5910 -> 0.5376). Kept.
- **E-040** (E-039 rescored with kept post-processing): confirms stability with `--cut-counting-loops`
  and `--cut-empty-tables`.
- **E-041** (I-11 retry on dev set E-029, 45 pages, `--memory-limit-gb 7.5`): retried 1 flagged page
  (Daily Star page 60). Text Edit -0.0011 [-0.0033, 0.0000] (0.0553 -> 0.0542), Reading order 0.0000,
  TEDS 0.0000. Confirmed zero regressions across all 44 non-flagged dev pages. Kept.
- **E-042** (E-041 rescored with kept post-processing): Text Edit -0.0011 [-0.0033, 0.0000].
- **E-043** (I-12 Base mode fallback on problem set): pages that produced fewer than 20 markdown
  characters in Gundam mode (PPT slides 770 and 4330) retried in Base mode. Both succeeded in under
  2 s total. Diff vs E-030 baseline: Text Edit -0.1845 [-0.3272, -0.0613] (0.6846 -> 0.5001),
  Reading-order Edit -0.1300 [-0.2386, -0.0227] (0.5910 -> 0.4610). PPT2PDF text edit halved
  from 0.9595 to 0.5448. Kept.
- **E-044** (I-16 table splitting and repeat truncation on problem set): rescored E-043 with
  `--split-merged-tables` and `--cut-repeated-lines`.
  - Stratified reweighted score (`compare.py score` / `stats.json`): Text Edit 0.5001 [0.3788, 0.6244] (n=46),
    Reading-order Edit 0.4339 [0.3309, 0.5375] (n=49), Table TEDS 35.3780 [23.0574, 47.5578] (n=22),
    Table TEDS-S 43.1911 [29.3837, 56.6922] (n=22).
  - Pooled headline (`summary.json`): Text Edit 0.5704, Reading-order Edit 0.5395, Table TEDS 36.2346,
    Table TEDS-S 43.2008.
  - Weighted paired diff vs E-030 baseline (`compare.py diff`): Text Edit -0.1845 [-0.3272, -0.0613] (n=46),
    Reading-order Edit -0.1546 [-0.2610, -0.0460] (n=49), Table TEDS +6.9037 [1.1431, 14.0382] (n=22),
    Table TEDS-S +7.9539 [1.4837, 14.9912] (n=22).
  - Weighted paired diff vs E-043: Table TEDS +5.6750 [0.3703, 12.6512] (n=22), Reading-order Edit -0.0246 [-0.0490, -0.0058] (n=49). Kept.
- **E-045** (I-16 table splitting and repeat truncation on 45-page dev subset): rescored E-041 with
  `--split-merged-tables` and `--cut-repeated-lines`.
  - Stratified reweighted score (`compare.py score`): Text Edit 0.0542 [0.0209, 0.0984] (n=44),
    Reading-order Edit 0.1251 [0.0696, 0.1920] (n=45), Table TEDS 93.5020 [89.4641, 96.7235] (n=17),
    Table TEDS-S 95.5853 [91.4287, 98.6931] (n=17).
  - Pooled headline (`summary.json`): Text Edit 0.0574, Reading-order Edit 0.1317, Table TEDS 93.5020,
    Table TEDS-S 95.5853.
  - Weighted paired diff vs E-041: 0.0000 across Text Edit [0.0, 0.0] (n=44), Reading order [0.0, 0.0] (n=45),
    Table TEDS [0.0, 0.0] (n=17), Table TEDS-S [0.0, 0.0] (n=17). Zero regressions on normal pages. Kept.
- **E-046** (margin cut-short detection and Base ladder fallback on problem set): retried flagged pages from E-044
  with `is_cut_short_or_misclassified` and `box_repeats`, falling back to Base mode for cut-short/looping pages.
  Exam papers recovered (jiaocai_1349 from 58 chars to 2,037 chars; jiaocai_2839 from math loop to 1,629 tokens).
  - Stratified reweighted score (`compare.py score` / `stats.json`): Text Edit 0.4380 [0.3060, 0.5640] (n=46),
    Reading-order Edit 0.3926 [0.2929, 0.4880] (n=49), Table TEDS 40.3413 [26.6773, 54.6423] (n=22),
    Table TEDS-S 48.1757 [34.4286, 62.2959] (n=22).
  - Pooled headline (`summary.json`): Text Edit 0.5673, Reading-order Edit 0.5406, Table TEDS 40.3413,
    Table TEDS-S 48.1757.
  - Weighted paired diff vs E-030 baseline (`compare.py diff`): Text Edit -0.2466 [-0.4010, -0.0949] (n=46),
    Reading-order Edit -0.1985 [-0.3160, -0.0788] (n=49), Table TEDS +11.0104 [-4.9907, 26.7591] (n=22),
    Table TEDS-S +12.9288 [-1.6990, 28.5820] (n=22).
  - Weighted paired diff vs E-044: Text Edit -0.0621 [-0.1041, 0.0072] (n=46), Table TEDS +4.1067 [-9.9685, 19.2624] (n=22). Kept.
- **E-047** (single-row prose table unwrapping on problem set): rescored E-046 with `--unwrap-prose-tables`.
  Abstract and bibliography entries wrapped in 1-row fake tables unwrapped back to plain paragraphs.
  - Stratified reweighted score (`compare.py score` / `stats.json`): Text Edit 0.4076 [0.2827, 0.5306] (n=46),
    Reading-order Edit 0.3709 [0.2800, 0.4628] (n=49), Table TEDS 40.3413 [26.6773, 54.6423] (n=22),
    Table TEDS-S 48.1757 [34.4286, 62.2959] (n=22).
  - Pooled headline (`summary.json`): Text Edit 0.5470, Reading-order Edit 0.5202, Table TEDS 40.3413,
    Table TEDS-S 48.1757.
  - Weighted paired diff vs E-030 baseline (`compare.py diff`): Text Edit -0.2770 [-0.4328, -0.1269] (n=46),
    Reading-order Edit -0.2202 [-0.3401, -0.0946] (n=49), Table TEDS +11.0104 [-4.9907, 26.7591] (n=22),
    Table TEDS-S +12.9288 [-1.6990, 28.5820] (n=22).
  - Weighted paired diff vs E-046: Text Edit -0.0304 [-0.0911, 0.0] (n=46), Reading-order Edit -0.0217 [-0.0651, 0.0] (n=49),
    Table TEDS 0.0000 (n=22). Academic literature text edit dropped from 0.4110 to 0.1778. Kept.
- **E-048** (Base fallback guard with 500-char threshold, replay on problem set): replay: Gundam raw taken from E-044, not a fresh retry.
  Guarded `cmd_retry` with `should_fallback_to_base(raw, max_chars_for_base=500)` so looping pages with >500 chars do not degrade to Base mode.
  - Stratified reweighted score (`compare.py score` / `stats.json`): Text Edit 0.4340 [0.3040, 0.5594] (n=46),
    Reading-order Edit 0.3985 [0.2952, 0.5035] (n=49), Table TEDS 40.7801 [28.0305, 54.1109] (n=22),
    Table TEDS-S 47.7463 [33.5849, 61.7075] (n=22).
  - Pooled headline (`summary.json`): Text Edit 0.5303, Reading-order Edit 0.5106, Table TEDS 40.7801,
    Table TEDS-S 47.7463.
  - Weighted paired diff vs E-047 (`compare.py diff`): Text Edit +0.0264 [-0.0159, 0.0936] (n=46); plain paired mean: -0.0168.
  - Weighted paired diff vs E-030 baseline (`compare.py diff`): Text Edit -0.2506 [-0.4063, -0.1001] (n=46).
  - Outcome: superseded by E-049 because `jiaocai_2839` (which had an unstopped margin loop of 5,333 chars of only `aside_text` tags) evaded the length check and flipped back to Gundam, regressing from 0.0075 to 0.9361.
- **E-049** (Base fallback guard with body tag check, replay on problem set): replay: Gundam raw taken from E-044, not a fresh retry.
  Updated `should_fallback_to_base` to also route to Base mode when the page has no body tags (`text`, `title`, `table`, `equation`), regardless of text length.
  This kept `jiaocai_2839` (0.0075), `jiaocai_1349` (0.0773), and `newspaper_eb569707` (0.7959) on Base, while restoring the other 8 newspapers to Gundam.
  - Stratified reweighted score (`compare.py score` / `stats.json`): Text Edit 0.3968 [0.2722, 0.5178] (n=46),
    Reading-order Edit 0.3671 [0.2742, 0.4599] (n=49), Table TEDS 45.3255 [32.0611, 58.5595] (n=22),
    Table TEDS-S 52.2918 [38.5996, 65.8885] (n=22).
  - Pooled headline (`summary.json`): Text Edit 0.5029, Reading-order Edit 0.4940, Table TEDS 45.3255,
    Table TEDS-S 52.2918.
  - Weighted paired diff vs E-047 (`compare.py diff`): Text Edit -0.0108 [-0.0195, -0.0037] (n=46), Reading-order Edit -0.0038 [-0.0135, 0.0068] (n=49), Table TEDS +4.9842 [0.0000, 13.4333] (n=22).
  - Plain paired mean vs E-047: -0.0441 (n=46).
- **E-050** (prose-table unwrapping on 45-page dev subset): rescored E-045 with
  `--unwrap-prose-tables` added to existing post-processing flags.
  - Stratified reweighted score (`compare.py score` / `stats.json`): Text Edit 0.0542 [0.0209, 0.0984] (n=44),
    Reading-order Edit 0.1251 [0.0696, 0.1920] (n=45), Table TEDS 93.5020 [89.4641, 96.7235] (n=17),
    Table TEDS-S 95.5853 [91.4287, 98.6931] (n=17).
  - Pooled headline (`summary.json`): Text Edit 0.0574, Reading-order Edit 0.1317, Table TEDS 93.5020,
    Table TEDS-S 95.5853.
  - Weighted paired diff vs E-045 (`compare.py diff`): 0.0000 across Text Edit [0.0, 0.0] (n=44),
    Reading order [0.0, 0.0] (n=45), Table TEDS [0.0, 0.0] (n=17), Table TEDS-S [0.0, 0.0] (n=17).
    Zero pages changed. Zero regressions. Kept.
- **E-051** (full 1,651-page OmniDocBench run rescored with all post-processing fixes): rescored E-034
  with `--cut-counting-loops`, `--cut-empty-tables`, `--split-merged-tables`, `--cut-repeated-lines`, and `--unwrap-prose-tables`.
  62 pages changed prediction vs E-034.
  - Stratified reweighted score (`compare.py score` / `stats.json`): Text Edit 0.0487 [0.0428, 0.0554] (n=1557),
    Reading-order Edit 0.1321 [0.1210, 0.1441] (n=1638), Table TEDS 84.1962 [81.9804, 86.3919] (n=458),
    Table TEDS-S 87.8352 [85.7652, 89.8105] (n=458).
  - Pooled headline (`summary.json`): Text Edit 0.0498, Reading-order Edit 0.1323, Table TEDS 84.1962,
    Table TEDS-S 87.8352.
  - Weighted paired diff vs E-034 (`compare.py diff`): Text Edit -0.0008 [-0.0025, -0.0000] (n=1557),
    Reading-order Edit -0.0046 [-0.0074, -0.0022] (n=1638), Table TEDS -3.6262 [-5.1710, -2.2831] (n=458),
    Table TEDS-S -3.6203 [-5.1458, -2.2650] (n=458). Plain paired mean vs E-034: -0.0008 (n=1557).
  - Weighted paired diff vs E-028 baseline (`compare.py diff`): Text Edit -0.0013 [-0.0030, -0.0001] (n=1557),
    Reading-order Edit -0.0045 [-0.0073, -0.0022] (n=1638), Table TEDS -3.6276 [-5.1739, -2.2845] (n=458),
    Table TEDS-S -3.6203 [-5.1458, -2.2650] (n=458). Plain paired mean vs E-028: -0.0013 (n=1557).
  - Decision: Rejected on full set because Table TEDS fell by 3.6 points. Table splitting and prose unwrapping overfit to small sets.
- **E-052** (full 1,651-page OmniDocBench run rescored with safe kept fixes only): rescored E-034
  with `--cut-counting-loops`, `--cut-empty-tables`, and `--cut-repeated-lines` (no table split, no prose unwrap).
  Exactly 15 pages changed prediction vs E-034.
  - Stratified reweighted score (`compare.py score` / `stats.json`): Text Edit 0.0494 [0.0433, 0.0561] (n=1557),
    Reading-order Edit 0.1366 [0.1251, 0.1486] (n=1638), Table TEDS 87.8238 [85.8793, 89.6606] (n=458),
    Table TEDS-S 91.4555 [89.7128, 93.0335] (n=458).
  - Pooled headline (`summary.json`): Text Edit 0.0504, Reading-order Edit 0.1368, Table TEDS 87.8238,
    Table TEDS-S 91.4555.
  - Weighted paired diff vs E-034 (`compare.py diff`): Text Edit -0.0002 [-0.0006, 0.0000] (n=1557),
    Reading-order Edit -0.0001 [-0.0004, 0.0001] (n=1638), Table TEDS +0.0014 [0.0000, 0.0043] (n=458),
    Table TEDS-S 0.0000 [0.0000, 0.0000] (n=458). Plain paired mean vs E-034: -0.0002 (n=1557).
  - Weighted paired diff vs E-028 baseline (`compare.py diff`): Text Edit -0.0006 [-0.0016, -0.0000] (n=1557),
    Reading-order Edit -0.0000 [-0.0003, 0.0002] (n=1638), Table TEDS 0.0000 [0.0000, 0.0000] (n=458),
    Table TEDS-S 0.0000 [0.0000, 0.0000] (n=458). Plain paired mean vs E-028: -0.0007 (n=1557). Kept.
