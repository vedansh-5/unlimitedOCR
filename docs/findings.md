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
