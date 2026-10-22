# Summary

Last updated: 2026-10-23 (after E-001)

## Objective

Run Baidu's Unlimited-OCR (arXiv 2606.23050) on an Apple Silicon Mac through the
community MLX port, reproduce a baseline, and improve on the paper's results where
the improvement can be measured fairly.

## Status

Scope: no training. The released weights are used as published.

Environment set up; model runs end to end on this Mac (E-001). No benchmark run yet.

| Item | State |
|---|---|
| Paper read, reported results recorded | Done (`report.md`, section 2) |
| Model architecture checked against config | Done: DeepSeek-OCR encoder + 3B MoE decoder (64 experts, top-6, 2 shared) with R-SWA |
| Environment | Done: contained in `unlimitedOCRvenv/`, versions pinned to the port's lock |
| Port bug blocking every run | Fixed in `run_ocr.py`, with a test (findings E-001a) |
| Port prompt differs from Baidu's (extra trailing space) | Fixed by default in `run_ocr.py`; removed both start-of-output errors (findings E-001b) |
| `ocr_to_md.py`, `checks.py` | Done, with tests |
| Smoke test (E-001) | Done: 17 s per dense gundam page, about 8 s per base page, peak 9.6 GB |
| Baseline on this machine | Not run |
| Improvements | None tried |

## Baseline

| Source | OmniDocBench v1.5 overall | v1.6 overall | Long-doc 40+ pages edit distance |
|---|---|---|---|
| Paper (A800 GPUs, reported) | 93.23 | 93.92 | 0.1069 |
| This project (M5, MLX) | not measured | not measured | not measured |

## Best result so far

None.

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

- Bug report to the port author drafted; posting needs a Hugging Face login.

- Deadline and rubric not yet known.
- Per-page runtime on this machine unknown; it decides how much of OmniDocBench can
  be run.
- OmniDocBench's formula metric (CDM) needs a LaTeX toolchain; not yet checked.
- Hugging Face currently serves OmniDocBench v1.6; the v1.5 revision still has to be
  located.

## Next steps

1. Baseline on a fixed OmniDocBench subset with the official evaluator (E-002).
2. Choose the first improvement from the ranked list in `plan.md`.
