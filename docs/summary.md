# Summary

Last updated: 2026-10-28 (after full-set clean-up rescore, E-052)

## Objective

Run Baidu's Unlimited-OCR (arXiv 2606.23050) on an Apple Silicon Mac through the
community MLX port, reproduce a baseline, and improve on the paper's results where
the improvement can be measured fairly.

## Status

Scope: no training. The released weights are used as published.

Full benchmark (E-028, 1,651 pages under 7.5 GB cap): Text Edit 0.0500 (pooled 0.0511),
TEDS 87.82, R-order 0.1366, behind the paper (0.042, 90.2, 0.129). Kept post-processing
clean-up on the full run (E-052) reduced text edit to 0.0494 (pooled 0.0504) while
preserving table TEDS (87.82). E-051 tested table splitting and prose unwrapping on the
full set but was rejected after dropping table TEDS by 3.6 points (87.82 to 84.20). On
the 50-page problem set, the retry ladder (E-049) cut text edit from 0.6846 to 0.3968
(-0.2878) and raised table TEDS from 29.33 to 45.33 (+15.99). Dev set checks (E-041,
E-045, E-050) confirmed zero regressions on normal pages. Full-set model retry for all
flagged pages is pending.

| Item | State |
|---|---|
| Paper read, reported results recorded | Done (`report_detailed.md`, section 2) |
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
| Problem set repair ladder (E-030 to E-049) | Kept. 50 pages: Text Edit 0.6846 to 0.3968 (-0.2878), Table TEDS 29.33 to 45.33 (+15.99) |
| Full run table splitting & prose unwrapping (E-051) | Rejected: dropped full-set table TEDS by 3.6 points (87.82 to 84.20) |
| Full run clean-up rescore (E-052) | Kept. 1,651 pages: Text Edit 0.0500 to 0.0494 (-0.0006), TEDS 87.82 (preserved) |

## Baseline

| Source | OmniDocBench v1.5 overall | v1.6 overall | Long-doc 40+ pages edit distance |
|---|---|---|---|
| Paper (A800 GPUs, reported) | 93.23 | 93.92 | 0.1069 |
| This project, full run E-028 (1,651 pages, 8 GB cap) | not measured | Text Edit 0.0500, TEDS 87.82, R-order 0.1366 (CDM and Overall not measured) | - |
| This project, full run clean-up E-052 (1,651 pages) | not measured | Text Edit 0.0494, TEDS 87.82, R-order 0.1366 (CDM and Overall not measured) | - |
| This project (M5, MLX), E-002 / E-003 | not measured | Text Edit 0.036, TEDS 92.4, R-order 0.107 (CDM and Overall not measured) | 0.228 (NIST, text-layer reference; not comparable) |

## Best result so far

- OmniDocBench problem set (50 worst pages): Text Edit 0.3968 with E-049 (down from 0.6846 baseline, delta -0.2878 [-0.4430, -0.1379]), Table TEDS 45.33 (up from 29.33, +15.99 points), Reading order 0.3671 (down from 0.5910, delta -0.2240).
- OmniDocBench full run (1,651 pages): Text Edit 0.0494 with E-052 (down from 0.0500 baseline, delta -0.0006 [-0.0016, -0.0000]), Table TEDS 87.82.
- Dev subset (45 pages): Text Edit 0.0542, TEDS 93.50, zero regressions across 44 non-flagged pages.

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

- Full-set retry run: retrying all flagged pages across the 1,651 pages with
  the number-blind loop guard and Base ladder fallback.
- Formula CDM via Docker container to produce the official Overall score.

## Next steps (where to pick up)

1. Full-set retry run: execute the retry ladder across all flagged full-set pages.
2. Official Docker CDM evaluation for formula recognition and Overall benchmark score.
3. Gutter-aware column slicing for broadsheet newspapers.
