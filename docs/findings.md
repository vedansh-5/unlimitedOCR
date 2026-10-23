# Findings

Experiment entries use the format: what and why, hypothesis, configuration, observed
result, hypothesis supported or not, lessons, follow-ups. IDs match
`experiment_log.md` and `plan.md`.

## R-001: Source review before any run (2026-10-23)

Reading only, no model run.

| Question | Finding | Source |
|---|---|---|
| Is the decoder MoE? | Yes. 12 layers, 64 routed experts, top-6, 2 shared, first layer dense, hidden 1280, R-SWA window 128 | `baidu/Unlimited-OCR` `config.json` at `8249d20` |
| What was the main benchmark? | OmniDocBench v1.5 and v1.6, official evaluator | Paper section 5.1 |
| How were the gains obtained? | Continued training on 128 A800 GPUs | Paper section 4.2 |
| Can we train on this Mac? | Not safely. The port's own notes say BF16 weights plus LoRA state do not fit in 16 GB; 32 GB for small LoRA runs, 64 GB+ in practice | Port `TRAINING.md` at `e4c39cd` |
| Is the MLX port checked against the CUDA model? | No published parity check; the author says a quantized checkpoint waits on one | Port `README.md` |
| Does the port support both image modes? | Yes: `--mode gundam/base/auto`, plus `--no-repeat-ngram-size`, `--ngram-window`, `--max-pages-per-request`, `--prefill-step-size`, `--adapter-path` | Port `infer_mlx.py` |
| Is the long-document test set public? | No, in-house | Paper section 5.1 |
| Known long-document failure | Repetition on small text at 40+ pages, blamed on Base mode resolution | Paper section 5.4 |
| Dataset size | OmniDocBench on Hugging Face: about 1.55 GB, about 1,650 images (v1.6). v1.5 has 1,355 pages | HF API, paper |

Lessons:
- "Beating the paper" on OmniDocBench accuracy through training is not feasible on
  this hardware. Inference-time changes are the realistic lever.
- The paper's own stated weakness (long-document repetition) is the clearest target.
- Every comparison to the paper's numbers must first account for a possible MLX vs
  CUDA gap, which E-002 measures.

Checked later (R-002 below): the no-repeat guard and the R-SWA cache.
- Whether the OmniDocBench evaluator's formula metric (CDM) runs on macOS.

## E-001a: First run crashed on the first generated token (2026-10-23)

- **What:** single page (paper p.10, gundam mode) with the port's CLI, default settings.
- **Observed:** exit code 2 after 47 s: `ValueError: not enough values to unpack
  (expected 3, got 2)` in the decoder attention, on the first decode step. Log kept in
  `results/E-001/a_time_failed.txt`.
- **Root cause:** the port's `SlidingWindowNoRepeatNgramProcessor.__call__` decides
  whether the input is batched from the token ids only. mlx-vlm 0.6.16 passes 1-D token
  ids with `(1, vocab)` logits, so the guard returns `(vocab,)`. Sampling then gives a
  scalar token, and the next step feeds a 2-D tensor into the model.
- **Evidence:** `tests/test_ngram_guard_shape.py` fails on the unpatched class
  (`(10,) != (1, 10)`) and passes with the fix.
- **Fix:** `run_ocr.py` wraps the guard so its output keeps the shape of the logits it
  was given, then calls the port's CLI unchanged. The banned-token rule itself is not
  touched.
- **Lesson:** the port's tests never load the model, and its end-to-end path did not
  run with its own pinned versions. Everything downstream of the port needs our own
  end-to-end check.
- **Follow-up:** reported upstream: https://huggingface.co/shubhxho/Unlimited-OCR-MLX/discussions/1

## E-001: Smoke test and cost (2026-10-23)

- **What and why:** two small runs to measure speed and memory on this Mac before
  sizing any benchmark run. Script: `results/E-001/run.sh`, run through `run_ocr.py`.
- **Hypothesis:** the model fits in 16 GB and runs at a usable speed.
- **Configuration:** port `e4c39cd`, model `07dea83`, mlx 0.32.1, mlx-vlm 0.6.16,
  defaults (temperature 0, 35-gram guard, window 128 gundam / 1024 base, DPI 300).

| Run | Pages | Mode | Prompt tokens | Output tokens | Model time | Output speed | Peak MLX memory | Wall time |
|---|---|---|---|---|---|---|---|---|
| a | paper p.10 | gundam | 2,738 | 981 | 16.9 s | 83 tok/s | 9.62 GB | 19.5 s |
| b | paper p.1-3 | base, one request | 825 | 2,154 | 24.3 s | 93 tok/s | 8.35 GB | 28.9 s |

Both finished normally (`finish_reason: stop`, `complete: true`).

- **Hypothesis supported:** yes. Peak 9.6 GB leaves headroom on 16 GB; about 17 s for
  a dense gundam page, about 8 s per page in base mode.
- **Quality, checked by eye against the PDF:**
  - Run a: all 54 numbers in the table match the PDF. Two-line column headers were
    merged wrongly ("Colorful Exam Textbook", "Paper" instead of "Colorful Textbook",
    "Exam Paper").
  - Run a: the paragraph at the top of the page (4 lines) is missing, and the first
    output line has no `<|det|>` marker.
  - Run b: output starts with a date, "2018年1月1日", that is not in the PDF. Pages 1 to 3
    are otherwise present, separated by `<PAGE>`.
  - Both content errors are at the very start of the output. Not yet known whether this
    is the model, the port, or the prompt; to be checked against the paper's own
    examples and measured at scale in E-002.
- **Measurement problem:** `/usr/bin/time -l` measured the `uv` launcher, not the model
  process (it reported a 10 MB footprint). Only the port's MLX peak memory is reliable
  here. The batch runner must start the venv's Python directly to measure process
  memory.
- **Cost estimate update:** OmniDocBench pages run in gundam mode. At 15 to 25 s per
  page, the full v1.5 set (1,355 pages) takes about 6 to 9.5 h; a 135-page subset about
  35 to 55 min.

## E-001b: Trailing space in the prompt (2026-10-23)

- **What and why:** both E-001 content errors were at the very start of the output.
  Comparing prompts showed the port sends one token more than Baidu's code: the
  mlx-vlm template returns `'<image>document parsing. '`, ending in a space (token 223).
  Baidu's `infer()` uses the plain template and `.strip()`, giving
  `[0, 128815, 34030, 76466, 16]`.
- **Hypothesis:** the stray space puts the model off its trained start, so the first
  output tokens go wrong. Removing it should fix the start and change nothing else.
- **Change (one variable):** strip trailing spaces from the formatted prompt.
  Script: `results/E-001b/run.sh`.

| Run | Prompt tokens | Output tokens | Model time | Start of output |
|---|---|---|---|---|
| E-001 a, p.10 | 2,738 | 981 | 16.9 s | first paragraph and first title marker missing |
| E-001b a, p.10 | 2,737 | 1,096 | 15.9 s | first paragraph present, title marker present |
| E-001 b, p.1-3 | 825 | 2,154 | 24.3 s | made-up date "2018年1月1日" |
| E-001b b, p.1-3 | 824 | 2,149 | 26.5 s | `<PAGE>` then the real page header |

- **Result:** after stripping markers, the clean Markdown of each pair differs only in
  those opening lines; everything else is identical line for line.
- **Hypothesis supported:** yes, on these two inputs.
- **Decision:** keep. `run_ocr.py` now uses Baidu's prompt by default;
  `--keep-prompt-space` reproduces the port's behaviour (used by E-001's script).
- **Lesson:** a one-token prompt difference changes output. Any MLX-vs-paper gap must be
  checked against prompt format first.

## R-002: Port vs upstream code, guard and R-SWA cache (2026-10-23)

Reading only. Upstream = `modeling_unlimitedocr.py` / `modeling_deepseekv2.py` at model
revision `07dea83`; port = `unlimited_ocr_mlx.py` at `e4c39cd` plus mlx-vlm 0.6.16.

| Part | Same as upstream? | Detail |
|---|---|---|
| No-repeat rule | Yes | Same window, same prefix match, same whitelist; only the code style differs |
| Tokens the guard sees | Yes | Prompt plus generated tokens in both |
| Length limit | No | Upstream `max_length=32768` counts prompt + output; the port's `--max-tokens 32768` counts output only, so the port can generate past upstream's limit on long inputs |
| R-SWA cache layout | Yes | Full prompt KV kept, then a ring of the last 128 output tokens, overwritten in order |
| Where "prompt" ends in the cache | **Only for prompts up to 2,048 tokens** | Upstream records the prompt length after the one-shot prefill. mlx-vlm chunks prompts longer than `DEFAULT_PREFILL_STEP_SIZE = 2048` and feeds the last prompt token as a single step; the ring cache then treats that token as output and overwrites it after 128 generated tokens |

Affected by the last row: dense gundam pages (prompt about 2,700 tokens) and every base
request of 8 or more pages (275 prompt tokens per page). Likely small, since the token
lost is the final `.` of the prompt, but untested. Test: E-001c, page 10 with chunking
disabled (`--prefill-step-size 100000`), one change.

## R-003: mlx-vlm batch generation drops R-SWA (2026-10-23)

Reading only. In mlx-vlm 0.6.16, `batch_generate` builds caches with `_make_cache`
(`generate/ar.py`), which converts each layer's cache to a batch cache.
`RingSlidingKVCache` subclasses `KVCache` and has no `to_batch`, so it becomes a plain
`BatchKVCache`: every generated token stays in the cache and attention is full, not
R-SWA. Batched output would therefore not be the paper's model behaviour.

Consequence: batching (speed idea 4) needs its own batch R-SWA cache: left-padded
prompts, the same prompt length for every row after padding, a shared ring of 128
decode slots, and a mask that hides the padding even in the ring phase. Expected
gain is below linear: rows usually pick different experts, so each decode step reads
more expert weights.

## E-002: OmniDocBench v1.6 test baseline, 140 pages (2026-10-23)

- **What and why:** score the unchanged model (plus the two port fixes) with the
  official evaluator, to check the MLX setup against the paper before any improvement.
- **Hypothesis:** scores fall within sampling error of the paper's v1.6 row.
- **Configuration:** dataset `aa1ee96`, evaluator `f133a71` (quick_match, 4 workers,
  CDM off), 15 pages per document type with seed 42 (all 5 historical pages), gundam
  mode, Baidu prompt, defaults otherwise. Scripts: `omnidocbench.py` steps
  select / fetch / predict / evaluate / summary.

| Metric | E-002 (raw mean) | E-002 reweighted to full-set type mix, 95% CI | Paper v1.6 | Leaderboard v1.6 |
|---|---|---|---|---|
| Text Edit (down) | 0.0589 | 0.0362 [0.0243, 0.0510] | 0.042 | 0.0394 |
| Table TEDS (up) | 92.35 | 92.37 [88.69, 95.67] (51 tables, not reweighted) | 90.16 | 90.21 |
| Table TEDS-S (up) | 94.91 | 94.90 [91.86, 97.46] | 93.32 | 93.36 |
| Read-order Edit (down) | 0.1271 | 0.1069 [0.0784, 0.1425] | 0.129 | 0.128 |
| Formula CDM (up) | not measured | | 95.79 | 95.72 |

Reweighting: the subset over-samples `historical_document` (5 of 140 pages vs 5 of
1,651) whose text edit is 0.558, so per-type means are weighted by full-set page counts.
CIs: 2,000 stratified bootstrap resamples, seed 0.

Text edit by document type (raw): PPT 0.006, academic 0.018, book 0.020, colorful
textbook 0.050, exam 0.052, historical 0.558, magazine 0.019, newspaper 0.093, note
0.095, research report 0.001.

- **Cost:** 42.3 min model time (18.1 s per page, max 121 s), 75 tok/s, peak 10.0 GB,
  no page hit the token limit. Scoring about 10 min on CPU.
- **Hypothesis supported:** yes. Every paper and leaderboard value lies inside the 95%
  interval. The MLX port with our fixes reproduces the paper on this subset.
- **Repetition loops found:** 2 of 140 pages, both historical documents
  (`page-8e2f…`: one formula line repeated 58 times, Distinct-35 = 0.33; `page-0708…`:
  a numbered list cycling, Distinct-35 = 0.43, ending in a broken `<|det|>` marker that
  leaks into the Markdown). Two more pages are borderline (Distinct-35 0.75 and 0.84),
  to inspect in I-1.
- **Why the 35-gram guard misses them:** each repeat is its own block with new box
  coordinates (`[875, 190, …]`, `[875, 240, …]`, …), so no 35-token sequence ever
  repeats exactly. The guard cannot see a loop that walks down the page.
- **Lesson for I-1:** detect repeats on the text with `<|det|>` markers and coordinates
  removed; this catches exactly the loops the guard misses.
- **Check fix:** the first version of the loop checks counted a sparse HTML table as a
  loop (compression 7.6). Checks now run on tag-stripped text; regression test added.

## E-001c: Chunked prefill vs one-shot prefill (2026-10-23)

- **What and why:** R-002 found that for prompts over 2,048 tokens mlx-vlm feeds the last
  prompt token as a decode step, so the R-SWA ring treats it as output. Test whether
  that changes the result.
- **Hypothesis:** small or no effect, since only the final prompt token is affected.
- **Change (one variable):** `--prefill-step-size 100000` (no chunking, like upstream)
  on E-001b's page 10 (prompt 2,737 tokens). Script: `results/E-001c/run.sh`.
- **Result:** same 1,096 output tokens, same text; the only difference in the raw output
  is one box coordinate (`340` vs `339`). Time 15.9 s vs 16.9 s, peak 9.62 GB in both.
- **Hypothesis supported:** yes. The coordinate change may come from the different order
  of floating-point operations in chunked vs one-shot prefill rather than from the cache;
  this test cannot separate the two.
- **Decision:** keep mlx-vlm's default chunked prefill, so all runs stay comparable with
  E-002. Revisit only if long multi-page inputs (E-003) show a problem.

## E-004: Dev baseline, 45 pages (2026-10-23)

- **What and why:** reference point for trying fixes quickly. 5 pages per document type,
  seed 42, none shared with E-002 (no historical documents left, all 5 are in E-002).
  Same settings as E-002.
- **Scores (raw means, not reweighted):** Text Edit 0.0526, Table TEDS 93.50, TEDS-S
  95.59, Read-order Edit 0.1343. By type, text edit: PPT 0.090, academic 0.004, book
  0.004, colorful textbook 0.020, exam 0.078, magazine 0.045, newspaper 0.213, note
  0.002, research report 0.008.
- **Cost:** 18.3 min model time, 24.4 s per page on average; one page alone took 377 s.
- **Loop found:** `newspaper_Daily Star 2025-1-8…page_060` repeated "The image contains
  no text. The horizontal lines are stylistic or background elements and must be
  ignored…" 555 times as `image_footnote` blocks with new coordinates each time, ran
  into the 32,768-token cap (`finish_reason: length`), and scored text edit 0.829. Same
  mechanism as E-002: the 35-gram guard never fires because coordinates change.
- **Detector:** `loops.py` flags exactly this page (max repeat 555) and nothing else
  among the 45.
- **Lesson:** loops are not limited to old scans; one loop page costs as much time as
  15 normal pages and drives the newspaper average from about 0.05 to 0.21.

## E-005: I-1 loop fix on the dev subset (2026-10-23)

- **Problem:** E-004 page `newspaper_Daily Star…page_060` looped 555 times, hit the
  token cap and scored text edit 0.829.
- **Change (one variable):** `omnidocbench.py retry --base E-004 --content-guard`.
  Pages flagged by `loops.is_loop` (only this one) are re-run with the coordinate-blind
  guard; all other 44 outputs are copied from E-004 unchanged.
- **Hypothesis:** with box coordinates ignored, the 35-gram rule sees the repeat and
  blocks it, so the page finishes normally and its text edit drops.

| | E-004 | E-005 |
|---|---|---|
| Looping page: output tokens / time | 32,768 (cap) / 377 s | 1,290 / 19 s |
| Looping page: finish | length | stop |
| Looping page: text edit | 0.829 | 0.371 |
| Dev Text Edit | 0.0526 | 0.0422 |
| Dev Read-order Edit | 0.1343 | 0.1306 |
| Dev Table TEDS / TEDS-S | 93.50 / 95.59 | 93.50 / 95.59 |

- **Hypothesis supported:** yes. The retried page now transcribes the puzzles page
  (title, sudoku grid) instead of looping; the remaining error on it is ordinary OCR
  error. Dev text edit improves by 20% from one page.
- **Decision:** keep; confirm on the test subset (E-006).

## E-006: I-1 loop fix on the test subset (2026-10-23)

- **Change:** `omnidocbench.py retry --base E-002 --content-guard`; only the 2 flagged
  pages re-run, 138 copied from E-002.

| | E-002 | E-006 |
|---|---|---|
| `page-8e2f…`: max repeat / text edit / read-order | 58 / 0.959 / 0.290 | 30 / 0.955 / 0.290 |
| `page-0708…`: max repeat / text edit / read-order / broken marker | 30 / 0.976 / 0.714 / yes | 6 / 0.950 / 0.929 / no |
| Time on the 2 pages | 21 s + 24 s | 16 s + 7 s |
| Test Text Edit (raw mean) | 0.0589 | 0.0587 |
| Test Read-order Edit | 0.1271 | 0.1286 |
| Test Table TEDS / TEDS-S | 92.35 / 94.91 | 92.35 / 94.91 |

- **Hypothesis supported:** only partly. The guard cuts the repeats and removes the
  broken marker, but both pages stay almost entirely wrong (text edit about 0.95).
- **Why:** these are not runaway loops but reading failures. Both are warped scans of
  vertical classical Chinese; for each column it cannot read, the model writes the same
  made-up line (`\( \therefore m = \frac{3}{11} \)`). Each copy is short and in its own
  block, so even the coordinate-blind guard only blocks exact 35-token repeats and the
  model produces near copies.
- **Contrast with E-005:** there the page was readable and the loop was the failure;
  removing it recovered the page. Here the loop is a symptom of not being able to read.
- **Decision:** keep I-1. Large gain where the loop is the failure (dev), neutral on
  aggregate where it is not (test: text edit -0.0002, read-order +0.0015 from one page
  that is wrong either way), and it saves time on every looping page.
- **Lesson for the report:** loop repair fixes runaway decoding, not unreadable input.
- **Correction (same night):** the per-page values in this table were first written
  against the wrong page (read in file order, not by name). Re-checked by page name;
  totals and conclusion unchanged.

## E-007: I-6 broken-marker repair on the test subset (2026-10-23)

- **Problem:** `page-0708…` in E-002 ended with an unclosed `<|det|>text [768, 189,`
  that leaked into the Markdown.
- **Change (one variable):** `omnidocbench.py rescore --base E-002 --repair-markers`;
  no model run. Only that page's Markdown changed.
- **Result:** page text edit 0.9755 to 0.9760, read-order unchanged; all headline
  metrics identical to E-002 (Text Edit 0.0589, TEDS 92.35, R-order 0.1271).
- **Hypothesis supported:** no measurable effect. The leaked fragment was tiny next to
  a page that is wrong everywhere else.
- **Decision:** keep the option (it makes the Markdown clean for users) but it is not a
  benchmark improvement; not counted as one in the report. Dev has no broken markers,
  so there is nothing to measure there.

## R-004: reweighted scores and paired differences from code (2026-10-23)

- **Problem:** the reweighted E-002 scores and their intervals in `report.md` were
  computed by a one-off script that was not saved, so they could not be regenerated.
  Changes were also judged by comparing two separate means, which hides how much of
  the difference is noise.
- **Change:** `compare.py score` (reweighted mean and 95% stratified bootstrap
  interval per metric, written to `stats.json`) and `compare.py diff` (the same for
  per-page differences between two experiments on the same pages, written to
  `diff_vs_<base>.json`). Same method as before: per-type means weighted by the full
  benchmark's type counts, 2,000 resamples within type, `random.Random(0)`.
- **Check:** `compare.py score --exp E-002` reproduces the report's edit metrics
  exactly (Text Edit 0.0362 [0.0243, 0.0510], R-order 0.1069 [0.0784, 0.1425]).
- **Correction to E-002's table intervals:** the one-off script averaged TEDS over
  tables (51). The evaluator's headline averages over pages (37 pages with tables;
  each page's tables averaged first). The two match on E-002 (92.37 against 92.35) but
  not on E-004 (92.40 against 93.50), which is how the mismatch showed up.
  `compare.py` now uses the evaluator's page average. E-002 TEDS is 92.35
  [88.14, 95.89] (was [88.69, 95.67]) and TEDS-S 94.91 [91.67, 97.58] (was
  [91.9, 97.5]). The paper and leaderboard values stay inside both intervals, so the
  reproduction conclusion is unchanged. Report section 5.1 updated.
- **Paired results so far (after minus before, reweighted):**

| Change | Subset | Text Edit diff [95% CI] | R-order diff [95% CI] | TEDS diff |
|---|---|---|---|---|
| I-1 loop repair (E-005 vs E-004) | dev, 45 | -0.0084 [-0.0252, 0.0000] | -0.0031 [-0.0092, 0.0000] | 0 |
| I-1 loop repair (E-006 vs E-002) | test, 140 | -0.0000 [-0.0000, 0.0000] | +0.0001 [0.0000, 0.0004] | 0 |
| I-6 marker repair (E-007 vs E-006) | test, 140 | 0.0000 | -0.0001 [-0.0004, 0.0000] | 0 |

- **Reading:** I-1 changes one dev page a lot and nothing else, so the interval touches
  zero (resamples that miss that page show no change). The test pages it changes are
  historical documents, which are 5 of 1,651 pages in the full set and so carry almost
  no weight. I-1 is a fix for a rare failure, not a measurable gain in the average;
  the report says so.
- **Decision:** all future comparisons use `compare.py diff`; a change counts as an
  improvement only if its interval excludes zero.

## E-003: Long-document baseline (2026-10-23)

- **What:** 15 documents, page prefixes (2, 5, 10, 20, 40) of three NIST PDFs, each
  sent as one request in Base mode with the port's defaults (32,768-token cap). Scored
  against the PDF text layer. 37.8 min of model time.
- **Results (`results/E-003/scores.csv`):**

| Pages | Mean edit distance | Mean word recall | Pages out differ from pages in | Hit token cap | Model s (mean) |
|---|---|---|---|---|---|
| 2 | 0.138 | 0.934 | 0 of 3 | 0 | 9 |
| 5 | 0.104 | 0.973 | 2 of 3 | 0 | 31 |
| 10 | 0.200 | 0.959 | 3 of 3 | 0 | 85 |
| 20 | 0.110 | 0.953 | 2 of 3 | 0 | 194 |
| 40 | 0.228 | 0.917 | 3 of 3 | 2 of 3 | 502 |

  Correction (same day): the page-count column was first read by eye as 9 of 15 off;
  `make_tables.py` counts 10 of 15 (2 of them the capped documents). Fixed here and in
  the log and plan.

- **Failure 1, page shifts:** the model often writes one more or one fewer `<PAGE>`
  than the input has, from 5 pages up. Checked against the PDF on the 5-page AI 100-1
  prefix: after the title page it wrote a page that mixes the top of page 3 with the
  bottom of page 2, then the real page 3.
- **Failure 2, token cap:** NIST pages take about 800 output tokens each, so 40 pages
  do not fit in 32,768 tokens; two of three 40-page documents stopped at the cap
  around page 38 to 39. This is a budget limit, not memory: peak memory never went
  above 11.4 GB (R-SWA keeps the cache flat), and was lower at 40 pages (9.5 GB) than
  at 10 to 20 (11.3 GB).
- **Failure 3, slow recall loss:** recall falls from about 0.95 to 0.92 between short
  and 40-page inputs.
- **Speed:** output tokens per second (including prefill) drop from about 82 at 2 to
  10 pages to about 58 at 40 pages. E-008 will separate decode speed from prefill.
- **Measurement limit:** the text layer lacks text drawn inside images (cover logos,
  "Check for updates"), so correct output is charged as extra; the 2-page documents
  already score 0.09 to 0.18. Absolute values are therefore not comparable with the
  paper's Table 3 (in-house set, human references). Paired comparisons on the same
  documents are unaffected. Word recall (share of reference words found in the
  output) was added because it ignores extra text and still catches dropped or
  truncated pages. Remaining quirk: the text layer spells some headings letter by
  letter ("C O M P U T E R"), which costs recall on the 2-page SP 800-207 prefix.
- **Bug found and fixed:** `run_batch.py` saved Markdown only when the request exited
  with code 0, so the two capped documents had no output to score. It now saves
  whenever the model produced output; the two files were rebuilt from the saved raw
  output with `to_markdown` (same conversion, no model run).
- **Consequence for I-1L:** splicing re-run pages back by position is unsound,
  because a page shift moves every later page. Replaced by E-009: every page run on
  its own in Gundam mode and joined in order, which has no shifts and no cap by
  construction, and directly tests the paper's case for multi-page decoding.

## E-009: Page-by-page Gundam on the long-document set (2026-10-23)

- **Problem:** E-003 showed page shifts, the token cap at 40 pages, and recall loss
  with length when all pages go in one request.
- **Change:** each of the first 40 pages of each NIST source is run alone in Gundam
  mode (the port's single-image default) and the outputs are joined in page order.
  Each prefix document reuses the same page outputs. 120 page requests, 31.2 min model
  time in all.
- **Hypothesis:** no shifts and no cap by construction; accuracy at least as good
  (higher resolution per page); time similar, since output length is similar.
- **Results (means per bucket, E-003 then E-009):**

| Pages | Edit distance | Word recall | Model s | Peak GB |
|---|---|---|---|---|
| 2 | 0.138, 0.137 | 0.934, 0.934 | 9, 10 | 8.0, 8.6 |
| 5 | 0.104, 0.038 | 0.973, 0.977 | 31, 33 | 9.1, 8.6 |
| 10 | 0.200, 0.096 | 0.959, 0.960 | 85, 80 | 11.3, 8.6 |
| 20 | 0.110, 0.091 | 0.953, 0.961 | 194, 166 | 11.4, 8.6 |
| 40 | 0.228, 0.062 | 0.917, 0.967 | 502, 337 | 9.5, 8.6 |

- Page count right in 15 of 15 documents (E-003: 5 of 15); no request hit a cap.
- **Hypothesis supported:** yes, and faster than expected from 10 pages up. Likely
  reason: in one request, every output token attends to all prefix tokens (256 per
  page in Base mode), so per-token cost grows with page count; a single page keeps the
  prefix short.
- **Caveats:** (1) two things changed at once: one page per request, and Gundam
  instead of Base resolution. E-010 (page by page in Base mode) separates them.
  (2) 15 documents are nested prefixes of 3 sources, so they are not independent; no
  interval is given. (3) Scores are against the text layer (see E-003).
- **Decision:** see E-010.

## E-010: Page by page in Base mode (2026-10-23)

- **Problem:** E-009 changed two things at once (one page per request, and Gundam
  resolution). Which one gives the gain?
- **Change (one variable against E-009):** same 120 pages, each alone, with
  `--mode base` (one 1024 view, no crops; the Base preset also widens the no-repeat
  window from 128 to 1024 tokens). 23.6 min model time.
- **Results at 40 pages (means of 3 documents):**

| Run | Edit distance | Word recall | Page count off | Model s | Peak GB |
|---|---|---|---|---|---|
| E-003 one request, Base | 0.228 | 0.917 | 3 of 3 | 502 | 9.5 |
| E-010 page by page, Base | 0.077 | 0.968 | 0 of 3 | 283 | 8.2 |
| E-009 page by page, Gundam | 0.062 | 0.967 | 0 of 3 | 337 | 8.6 |

  Full per-bucket tables in `docs/tables.md`.
- **Reading:** splitting into single-page requests gives almost all of the gain:
  no page shifts, no token cap, higher recall, and 44% less model time than one
  request at 40 pages. Gundam adds a small edit-distance gain at 20 and 40 pages (0.091
  against 0.104, 0.062 against 0.077) for about 19% more time; with three sources this
  difference is too small to call.
- **Limits:** three clean, born-digital English reports; the text-layer reference
  cannot reward cross-page work (a table or paragraph continued over a page break),
  which is one reason the paper decodes pages together. Multi-page decoding may still
  win on documents where that matters.
- **Decision:** keep page-by-page decoding (I-8) as the default for long documents on
  this machine. Base mode when speed matters, Gundam when accuracy matters; both are
  in the report.
