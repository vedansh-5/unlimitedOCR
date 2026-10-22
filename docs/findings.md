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

Not yet checked:
- Whether the port's no-repeat guard and R-SWA cache match the upstream code line for
  line (plan item 1.2).
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
- **Follow-up:** report the bug to the port author (needs approval: outward-facing).

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
