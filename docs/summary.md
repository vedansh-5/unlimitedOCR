# Summary

Last updated: 2026-10-23, afternoon (after E-010)

## Objective

Run Baidu's Unlimited-OCR (arXiv 2606.23050) on an Apple Silicon Mac through the
community MLX port, reproduce a baseline, and improve on the paper's results where
the improvement can be measured fairly.

## Status

Scope: no training. The released weights are used as published.

Baseline done: on 140 OmniDocBench v1.6 pages the Mac setup matches the paper within sampling error (E-002). Long documents measured (E-003) and improved by decoding page by page (E-009, E-010). Next: speed changes (I-2 quantization, I-3 fewer experts) on the dev subset.

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
| Statistics from code (`compare.py`, `make_tables.py`) | Done; reproduces the report; corrected TEDS intervals (R-004) |
| Long-document baseline (E-003) | Done: wrong page count in 10 of 15 documents, 2 of 3 forty-page documents hit the token cap, recall 0.92 at 40 pages |
| I-2 quantized weights (E-011 to E-015) | 8-bit + bf16 fallback kept: same accuracy as bf16, 33% less model time, peak 8.6 GB. 4-bit rejected (tables -4.7 TEDS) |
| I-3 four experts per token (E-016) | Kept: ties bf16 + loop repair, 16% faster per page; combined with 8-bit in E-017/E-018 |
| Fast setup on test (E-019 to E-021) | Within noise of bf16 but leaning worse, 26% faster; option only. Accuracy runs stay bf16 + loop repair |
| Drop page furniture (E-022) | Rejected (slightly worse) |
| I-8 page-by-page decoding for long documents (E-009, E-010) | Kept. 40 pages: edit 0.228 to 0.077, recall 0.917 to 0.968, 44% less time (Base); Gundam slightly more accurate, 19% slower |

## Baseline

| Source | OmniDocBench v1.5 overall | v1.6 overall | Long-doc 40+ pages edit distance |
|---|---|---|---|
| Paper (A800 GPUs, reported) | 93.23 | 93.92 | 0.1069 |
| This project (M5, MLX), E-002 / E-003 | not measured | Text Edit 0.036, TEDS 92.4, R-order 0.107 (CDM and Overall not measured) | 0.228 (NIST, text-layer reference; not comparable) |

## Best result so far

- OmniDocBench dev: Text Edit 0.042 with I-1 (from 0.053, raw mean); the paired
  interval touches zero, so it is a fix for a rare failure, not an average gain.
- Long documents: page-by-page decoding (I-8) at 40 pages, edit distance 0.228 to
  0.062 to 0.077 and recall 0.917 to 0.967, in 44% less time (Base).

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

- Loop pages that are unreadable scans (2 of 140 test pages): repair cuts the loop but
  cannot make the text right. A classic OCR fallback needs your go.
- Long-document scores use the PDF text layer as reference, which misses text inside
  images; fine for comparing runs, not for comparing with the paper.
- Long-document set is three NIST reports; more varied long documents would make I-8
  more convincing.
- Formula CDM (and so the Overall score) not computed: needs Docker or Linux TeX.
- Port bugs reported upstream (discussion 1); no reply yet.
- Deadline and rubric not yet known.

## Waiting on you

- Full OmniDocBench run (1,651 pages, about 8 to 10 h overnight): on hold until you say
  go. Reminder will come up now and then.
- Also needing a go (see `plan.md`): formula CDM via Docker, Tesseract fallback,
  batched R-SWA.

## Next steps (where to pick up)

1. Done: I-2 (8-bit + fallback kept, 4-bit rejected).
2. Done: I-3 (4 experts kept). Running: 8-bit + 4 experts + fallback on dev (E-017/E-018).
3. E-008: decode speed over a long request (`--log-speed`).
4. I-5 newer mlx, I-7 resolution routing (may be moot after I-8).
5. Final test-subset run with all kept changes.
