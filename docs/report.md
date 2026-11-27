# Unlimited-OCR on a 16 GB Mac: Reproduction and Improvements

2026-10-29. Full method, tables and every experiment are in
`report_detailed.md` and `experiment_log.md`.

## Summary

Baidu's Unlimited-OCR reads document pages into Markdown and claims state-of-the-art
accuracy on OmniDocBench v1.6. We ran the released model, unchanged, on a 16 GB Apple
Silicon laptop through MLX. On a 140-page sample it matched the paper within sampling
error. On the full 1,651-page benchmark, run under an 8 GB memory cap, it was behind the
paper (text edit 0.051 against 0.042), and most of the gap came from a few dozen pages
where the model loops, stops early or merges layouts. We built inference-time fixes for
those failures. On the 50 worst pages, text edit fell from 0.685 to 0.427 and table
TEDS rose from 29.3 to 45.2 under kept fixes (E-055), with no page made worse on a
separate 45-page dev set. Earlier E-049 reached 0.397 by including prose unwrapping and
the unconstrained splitter, which both caused full-set regressions and were rejected.
With kept post-processing fixes and safer table splitter on the full 1,651-page
benchmark (E-053), stratified text edit reached 0.0494 (pooled 0.0504), reading order
0.1355 and table TEDS 88.09. The full set remains behind the paper (0.042 text edit,
90.2 TEDS), as full-set model retries on all flagged pages have not yet been run.
The formula score (CDM) is 87.10 against the paper's 95.79. That gives an Overall score
of 90.08 against 93.92, and formulas are now the largest part of the gap.

## 1. The paper and what it claims

"Unlimited OCR Works" (Baidu, arXiv 2606.23050, 2026). The model is the DeepSeek-OCR
vision encoder plus a 3B mixture-of-experts decoder (0.5B active per token). Its main
idea is Reference Sliding Window Attention (R-SWA): each output token sees the whole
image but only the last 128 output tokens, so memory stays flat however long the
output gets. That is what lets it read long, multi-page documents.

Claims we can test:

| OmniDocBench v1.6 | Text edit (lower is better) | Formula CDM | Table TEDS | TEDS-S | Reading-order edit | Overall |
|---|---|---|---|---|---|---|
| Paper | 0.042 | 95.79 | 90.2 | 93.3 | 0.129 | 93.92 |

### Primary Evaluation Metrics

- **Text Edit Distance:** Character-level Levenshtein distance between predicted text blocks and ground truth, normalized by text length. Measures transcription error rate (lower is better).
- **Table TEDS (Tree-Edit-Distance-based Similarity):** Tree edit distance comparing table HTML DOM structure and cell text content against ground truth (higher is better, 0 to 100).
- **TEDS-S (Structure-only TEDS):** Evaluates table grid structure and cell spans (rowspan/colspan) while ignoring cell text content.
- **Formula CDM (Constrained Distance Metric):** Compares display formulas by rendering predicted LaTeX to images using TeX Live and evaluating pixel alignment against rendered ground truth (higher is better, 0 to 100).
- **Reading-order Edit Distance:** Sequence edit distance measuring whether extracted text paragraphs, tables, and figures follow the correct logical reading order of the document (lower is better).

The paper also reports long-document scores on an in-house set that is not public. It
names its own main weakness: repetition loops on small text in long documents.

## 2. How we ran it

- **Machine:** MacBook Air, Apple M5, 16 GB memory. The official code is NVIDIA-only, so we
  used a community MLX port with the released weights in bf16 and greedy decoding.
- **Port fixes:** two bugs had to be fixed before anything ran correctly. One crashed on
  the first token. The other added a space to the prompt, which made the model skip the
  opening paragraph.
- **Memory:** every run is capped at 7.5 GB so the laptop stays usable. This needed
  changes to how image crops are processed. Peak memory dropped from 10 GB to under 8 GB.
- **Benchmark:** OmniDocBench v1.6 with the official evaluator. The formula score (CDM)
  needs a Linux TeX setup, so it was run in the evaluator's own Docker image on a second
  machine, on the 313 pages that contain display formulas.
- **Fair comparison:** each change is compared page by page with its baseline, with 95%
  bootstrap intervals. A change counts only if the interval excludes zero.
- **Three page sets:**
  - the full 1,651 pages, run once because it takes about 10 hours;
  - a 45-page dev set, used to check that a fix hurts nothing;
  - a 50-page "problem set", the worst pages of the full run, used to build fixes.

## 3. What we changed

Every change works at inference time on the released weights. Training is out of
reach on a laptop: the paper used 128 A800 GPUs.

| Change | What it does | Result |
|---|---|---|
| Loop repair | Re-decodes looping pages with a repeat guard that ignores box coordinates. The model's own guard misses loops because each repeat gets new coordinates. | Kept |
| Number-blind loop guard | Also catches loops that only change a number each time ("( 1 ) item", "( 2 ) item"...). | Kept: biggest single gain |
| Base-mode fallback | Pages that come back empty or cut short in high-resolution mode are re-read in the low-resolution mode. | Kept |
| Fallback guard | Stops dense newspapers from being sent to the low-resolution mode, which blurs them. | Kept |
| Clean-up of output | Cuts counting loops, runaway empty tables, and repeated lines. | Kept |
| Safer table splitter | Splits stacked tables only when column count changes or next row repeats header words. | Kept: +0.26 TEDS on full set, zero regressions |
| Page-by-page long documents | Reads a long document one page per request instead of all at once. | Kept |
| 8-bit weights with a bf16 fallback | Faster decoder. Pages it gets wrong are re-run in bf16. | Kept as a speed option |
| 4 experts per token instead of 6 | Less work per token. | Kept as a speed option |
| 4-bit weights | Even faster. | Rejected: loses tables |
| Drop headers and page numbers | Removes page furniture. | Rejected: slightly worse |
| Best of two decodes | Keeps the more confident of two readings. | Rejected: no gain |

## 4. Results: what we gained

**Reproduction.** On a 140-page sample (15 pages per document type), our setup matched
the paper within sampling error: text edit 0.036 [0.024, 0.051] against the paper's
0.042, and TEDS 92.4 [88.1, 95.9] against 90.2.

**Problem set (50 worst full-run pages).** Weighted text edit, step by step:

| Step | Text edit | Table TEDS |
|---|---|---|
| Baseline (E-030) | 0.685 | 29.3 |
| + number-blind loop guard (E-039) | 0.564 | 30.6 |
| + Base fallback for empty pages (E-043) | 0.500 | 30.6 |
| + table splitting, repeated lines (E-044) | 0.500 | 35.4 |
| + Base fallback for cut-short pages (E-046) | 0.438 | 40.3 |
| + prose-table unwrapping (E-047) | 0.408 | 40.3 |
| + fallback guard (E-049) | 0.397 | 45.3 |
| kept fixes only, safer splitter (E-055) | 0.427 | 45.2 |

- Under kept fixes (E-055), text edit improved by 0.258 [0.107, 0.412] (down to 0.427),
  reading order improved by 0.198 [0.080, 0.317], and tables gained 15.9 TEDS [4.3, 30.1]
  (up to 45.2).
- E-049 reached lower text edit (0.397) by including prose-table unwrapping and the
  unconstrained table splitter, which were both rejected after failing on the full set,
  whereas E-055 reflects only the validated, kept fixes.
- The last two exploratory steps (E-048, E-049) are replays: they reuse earlier model
  output rather than a fresh retry.
- The table gains from E-044 do not carry over to the full set (see section 5).

**Dev set (45 normal pages).** The same fixes changed only one page, which got better.
No page got worse. Text edit 0.055 to 0.054.

**Long documents.** Reading 40 pages one page at a time instead of in one request cut
edit distance from 0.228 to 0.077 and raised recall from 0.917 to 0.968, in 44% less
time. In one request the model added or dropped pages in 10 of 15 documents.

**Speed.** 8-bit weights with a bf16 fallback gave the same accuracy as bf16 on the dev
set in a third less time.

**Full set with kept clean-up fixes and safer table splitter (E-053, no model retry).** Rescored E-034 with kept post-processing flags and safer table splitter (`--cut-counting-loops`, `--cut-empty-tables`, `--cut-repeated-lines`, `--split-merged-tables`):

- Stratified reweighted score: text edit 0.0494 [0.0435, 0.0558] (pooled headline 0.0504), reading order 0.1355 [0.1256, 0.1458], table TEDS 88.09 [85.58, 90.31], structure TEDS 91.74 [89.70, 93.54].
- Weighted paired diff vs E-028 baseline: text edit -0.0006 [-0.0016, -0.0000] (plain paired mean -0.0007), reading order -0.0010 [-0.0021, -0.0002], table TEDS +0.2621 [0.0053, 0.6441].
- Weighted paired diff vs E-052: text edit -0.0000 [-0.0000, 0.0000] (plain paired mean -0.000002), reading order -0.0009 [-0.0021, -0.0001], table TEDS +0.2621 [0.0053, 0.6441].
- E-051 tested earlier splitter and prose unwrapping on the full set, but was rejected after dropping table TEDS by 3.6 points (84.20 vs 87.82). The safer rule splits only on column count changes or header repeats, yielding zero table regressions.
- Full-set model retry for all flagged pages has not been run.

**Formula score and Overall (full set).** CDM was run in the evaluator's Docker image on
the 313 formula pages of E-028 (2,352 formulas, no timeouts or errors, 1 h 50 min). The
clean-up fixes do not change formula output, so the score holds for E-053 too. Overall is
the mean of 100 x (1 - text edit), table TEDS and formula CDM.

| Full set | Text edit | Formula CDM | Table TEDS | Overall |
|---|---|---|---|---|
| Paper | 0.042 | 95.79 | 90.2 | 93.92 |
| E-028 | 0.0500 | 87.10 | 87.82 | 89.97 |
| E-053 | 0.0494 | 87.10 | 88.09 | 90.08 |

Of the 3.84-point Overall gap, formulas account for 2.90, tables 0.70 and text 0.25.
CDM pooled over all formulas is 90.07; the table uses the page average, as the
evaluator's summary does. Formula edit distance is 0.188 (page average).

## 5. What we lost, and limits

- **The full run is behind the paper.** With kept fixes (E-053): text edit 0.049 against
  0.042, TEDS 88.1 against 90.2, reading order 0.136 against 0.129. The first full run
  (E-028) was 0.050, 87.8 and 0.137. Our 140-page sample was too small to show this.
- **Two clean-up fixes cost 3.6 TEDS on the full set.** The first table splitter and
  prose-table unwrapping helped the problem set and the dev set but cost 3.6 TEDS on the
  full set (E-051). Both were rejected, and the splitter was replaced by the safer rule.
  This is why we check on the full set before keeping a fix.
- **The memory cap costs a little accuracy** on fragile pages. The clean-up fixes won it
  back on the dev set.
- **The problem set was picked from the worst pages,** so its gains show how much we
  repair, not the full-set score. The fixes might fit those 50 pages too closely; the dev
  set check is our guard against that.
- **One fix made things worse before it was caught.** E-048 sent an exam page back to
  the wrong mode (0.008 to 0.936). E-049 fixed it.
- **Formulas are the weakest part.** CDM is 87.10 against 95.79, which is most of the
  Overall gap (90.08 against 93.92). None of our fixes targeted formulas.
- **Unreadable scans** (warped vertical classical Chinese): repair stops the loop but
  cannot make the text right.
- **Long-document test** uses three NIST reports scored against the PDF text layer, so
  it can be compared only by trend, not with the paper's numbers.

## 6. Plan going forward

1. **Full-set retry of flagged pages (model run).** E-053 applied the kept clean-up fixes
   to all 1,651 pages, but the retry ladder (number-blind loop guard, Base-mode fallback
   for empty or cut-short pages) has only been run on the 50 problem pages. On the full set
   52 pages are flagged; 23 already have problem-set output and 29 need a new model run of
   about 47 minutes. This is the next test of whether we can reach the paper.
2. **Formulas.** They are now the largest part of the gap. Look at the lowest-scoring
   formula pages first to see whether formulas are missed, mis-written or mis-matched.
3. **Column slicing for broadsheet newspapers.** The model reads very large pages at too
   low a resolution. Splitting them into columns and stitching the output back together
   is the largest remaining source of error.
4. **Resolution routing:** send small-print pages to high resolution before decoding,
   instead of repairing them afterwards.
