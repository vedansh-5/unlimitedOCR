# Summary

Last updated: 2026-10-23, night (after E-006)

## Objective

Run Baidu's Unlimited-OCR (arXiv 2606.23050) on an Apple Silicon Mac through the
community MLX port, reproduce a baseline, and improve on the paper's results where
the improvement can be measured fairly.

## Status

Scope: no training. The released weights are used as published.

Baseline done: on 140 OmniDocBench v1.6 pages the Mac setup matches the paper within sampling error (E-002). Next: E-001c, dev baseline, long documents, then improvements.

| Item | State |
|---|---|
| Paper read, reported results recorded | Done (`report.md`, section 2) |
| Model architecture checked against config | Done: DeepSeek-OCR encoder + 3B MoE decoder (64 experts, top-6, 2 shared) with R-SWA |
| Environment | Done: contained in `unlimitedOCRvenv/`, versions pinned to the port's lock |
| Port bug blocking every run | Fixed in `run_ocr.py`, with a test (findings E-001a) |
| Port prompt differs from Baidu's (extra trailing space) | Fixed by default in `run_ocr.py`; removed both start-of-output errors (findings E-001b) |
| `ocr_to_md.py`, `checks.py` | Done, with tests |
| Smoke test (E-001) | Done: 17 s per dense gundam page, about 8 s per base page, peak 9.6 GB |
| Test baseline (E-002, 140 OmniDocBench v1.6 pages) | Done: matches the paper within sampling error |
| Dev baseline (E-004, 45 pages) | Done: Text Edit 0.053, TEDS 93.5, R-order 0.134; 1 runaway loop |
| I-1 loop repair | Kept. Dev text edit 0.053 to 0.042; neutral on test (its 2 loop pages are unreadable scans) |
| I-6 broken-marker repair | No effect on scores (E-007); kept as a clean-output option only |

## Baseline

| Source | OmniDocBench v1.5 overall | v1.6 overall | Long-doc 40+ pages edit distance |
|---|---|---|---|
| Paper (A800 GPUs, reported) | 93.23 | 93.92 | 0.1069 |
| This project (M5, MLX), E-002 | not measured | Text Edit 0.036, TEDS 92.4, R-order 0.107 (CDM and Overall not measured) | not measured yet (E-003) |

## Best result so far

Dev: Text Edit 0.042 with I-1 (from 0.053). Test: unchanged within noise.

## Key findings so far (from reading, not experiments)

- The paper's accuracy gain came from continued training on 128 A800 GPUs. That
  cannot be repeated on a 16 GB Mac; the port's own notes say even LoRA does not fit
  safely in 16 GB.
- The MLX port has no published parity check against the official CUDA model. Our
  baseline is also the first parity check.
- The paper names its own main long-document failure: repetition on small text in
  40+ page documents, caused by the low-resolution "Base" mode used for multi-page
  input. This is the most promising target for an improvement.
- The paper's long-document test set is in-house and not released. Long-document
  results can only be compared by trend, not number for number.

## Outstanding issues

- Repetition loops on 2 of 140 pages, invisible to the 35-gram guard because box
  coordinates change on every repeat. Target of I-1.
- mlx-vlm chunked prefill treats the last prompt token as output for prompts over
  2,048 tokens (R-002); E-001c tests whether it matters.

- Port bugs reported upstream (discussion 1); waiting on the author.

- Deadline and rubric not yet known.
- Per-page runtime on this machine unknown; it decides how much of OmniDocBench can
  be run.
- OmniDocBench's formula metric (CDM) needs a LaTeX toolchain; not yet checked.
- Hugging Face currently serves OmniDocBench v1.6; the v1.5 revision still has to be
  located.

## Waiting on you

- Full OmniDocBench run (1,651 pages, about 8 to 10 h overnight): on hold until you say
  go. Reminder will come up now and then.
- Also needing a go (see `plan.md`): formula CDM via Docker, Tesseract fallback,
  batched R-SWA.

## Next steps (where to pick up)

1. E-003: long documents (`long_docs.py make` is done; run
   `run_batch.py --exp E-003 --inputs results/E-003/inputs`, then `long_docs.py score`).
   About 30 to 35 min. Not started overnight on purpose.
2. Apply I-1 to long documents: per-page retry of looping pages in gundam mode.
3. Next improvements from `plan.md`: I-2 quantization, I-3 fewer experts.
