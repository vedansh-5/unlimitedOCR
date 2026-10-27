# Fix log

Every fix idea in one place, with what it targets and how it is tested. Started
2026-10-26, after the full run (E-027 predictions, E-028 retry).

## Goal

Beat the paper's OmniDocBench v1.6 row on the full benchmark (added 2026-10-26, after
E-028 came in below it):

| Metric | Paper | E-028 | Headroom seen in E-028 |
|---|---|---|---|
| Text Edit (lower is better) | 0.042 | 0.051 | 36 pages at 0.5 or worse carry 37% of it; without them 0.033 |
| Table TEDS | 90.2 | 87.8 | 71 of 665 tables under 0.5 carry 59% of the lost TEDS; 28 score 0 (17 pages: 6 with no table written, 11 with a table that does not match) |
| Table TEDS-S | 93.3 | 91.5 | as above |
| Reading-order Edit (lower is better) | 0.129 | 0.137 | inside our interval already |
| Formula CDM, Overall | 95.79, 93.92 | not measured | needs S-3 |

## How a fix is tried

Work happens on small runs only; the next full run comes once several fixes are kept,
possibly on another machine (see "Where to run").

1. **Problem set first.** 50 pages from E-028: P-4, P-5, the two never-flagged
   P-2 pages and the 17 pages with a zero-TEDS table (P-6). The baseline is E-028's own
   output on those pages, so it costs no run. A fix that needs no model is tried by
   rescoring (`omnidocbench.py rescore`, then `compare.py diff`). A fix that needs the
   model reruns only these pages.
2. **Then the dev subset** (E-004, 45 pages) against E-029 (dev under the same cap), to
   check that pages which were fine stay fine.
3. **Then the test subset** (E-002, 140 pages), only if kept on dev.

One change per run. Every model run on this Mac uses `--memory-limit-gb 7.5`.

## Problem page sets

**P-1: counting loops.** The model repeats a block with a number that goes up each time:
`(2354) \( \Delta \)` up to 2,367 on a Chicago Tribune page, `\( PD_{1513} \)` up to
1,513 on a scihub page. A scan of the E-028 Markdown (a 6-word run repeated 40 or more
times, digits ignored) finds 24 pages; some may be real repetition such as tables, so
the list needs a look by eye. Largest:

| Page | Repeats | Size |
|---|---|---|
| `newspaper_Chicago Tribune_0801@magazinesclubnew_page_015` | 4,371 | 29 KB |
| `scihub_j.1528-1167.2008.01552.x.pdf_3` | 2,415 | 104 KB |
| `newspaper_Chicago Tribune_0801@magazinesclubnew_page_019` | 2,366 | 81 KB |
| `yanbaopptmerge_yanbaoPPT_4570` | 1,571 | 72 KB |
| `docstructbench_llm-raw-scihub-o.O-j.jcp.2010.12.006.pdf_5` | 1,443 | 70 KB |
| `page-b2cc5729-a6b2-49ba-af62-788bf069b617` | 553 | 71 KB |
| `newspaper_Daily Star 2025-1-8@magazinesclubnew_page_060` | 419 | 123 KB |

**P-2: pages that pushed the evaluator into its timeout fallback.** Six pages, all with
far more predicted pieces than the ground truth (for example 2,401 against 69). Four
of them were in the E-028 retry and still loop, so the retry's repeat guard does not
stop counting loops. Two were never flagged: `jiaocaineedrop_jiaocai_needrop_en_349`
and `newspaper_The Wall Street Journal - 2025-01-08@magazinesclubnew_page_018`.

**P-3: the Daily Star crossword page.** Under the memory cap its fallback writes the
grid as an endless table of empty cells and hits the token cap (E-029).

**P-4: the 36 pages with Text Edit 0.5 or worse in E-028.** They are 2% of the pages
and carry 37% of the text error; without them the mean is 0.033 instead of 0.051.
Fifteen are newspapers. The list comes from
`eval/result/pred_quick_match_text_block_per_page_edit.json` (pages at 0.5 or above).
Most overlap P-1.

**P-5: test pages that got worse under the memory cap.** On the 140 test pages E-028 is
0.014 worse than E-006. Four pages make up the gap:
`newspaper_e62730aaeb9b509119e0c3699ac18201_1` (stops early),
`newspaper_02912feb79994ae24665509d964ad9ce_1` (`[Non-Text]` loop, the retry made it longer),
`newspaper_a105e3b0ddb10be6a596f76407c79180_1` (loop, unchanged by the retry), and
textbook page 055 of the 人教新起点英语5A set (cut short). They show whether a fix
recovers what the cap lost.

**P-6: pages with a zero-TEDS table.** 17 pages, 28 tables. On 6 the model wrote no
table at all; on 11 it wrote one that does not match (for example one table split in
two, see the error analysis in `findings.md`). Listed by
`eval/result/pred_quick_match_table_per_table_TEDS.json` (TEDS 0).

## Scoring (no effect on scores)

| ID | Change | Status |
|---|---|---|
| S-1 | Per-page match cache (`match_cache.py`): each page's match is stored under a hash of its ground truth, prediction, match settings and evaluator code, so a stopped scoring run resumes and a rescore only matches changed pages | Done. E-004 result files identical; 4 min 19 s cold, 15 s cached |
| S-2 | LaTeX-to-text without a fresh process for short formulas, and each result kept. The evaluator starts a new Python process per conversion so it can cut off a stuck one; on macOS that costs about 2 s each, and a looping page converts the same formulas thousands of times | Done. E-004 result files identical; 13 s from an empty cache. The two P-1 pages that held up E-028 for over an hour are the test |
| S-3 | CDM from the local matches: run only the formula CDM in Docker, on the formula pairs the local run already matched, instead of the image re-matching all 1,651 pages | Idea. The image's evaluator code differs from our local copy and runs under x86 emulation, so a plain CDM run is estimated at 11 to 20 h. Time a plain CDM run on E-004 first and check S-3 against it |

## Accuracy, no model run (rescore)

| ID | Change | Targets | Status |
|---|---|---|---|
| I-9 | Cut counting loops in the Markdown: find a block that repeats with only its numbers changing, keep the first few repeats, drop the rest | P-1, P-2 | Done / kept. Tested in E-031 on problem set (Text Edit -0.0024 [-0.0057, 0.0000]) and E-034 full run |
| I-10 | Cut runaway empty tables: a table that goes on with rows of empty cells past the point where the page could hold them | P-3 | Done / kept. Tested in E-032 on problem set (Daily Star -0.6282, Text Edit -0.0032 [-0.0096, 0.0000]), E-033 dev (-0.0115), and E-034 full run |

## Accuracy, model run on flagged pages only

| ID | Change | Targets | Status |
|---|---|---|---|
| I-11 | Number-blind loop check and repeat guard: `loops.py` and `--content-guard` treat digits as equal, so counting loops are flagged for the retry and blocked during it | P-1, P-2; also the two never flagged | Tested on problem set (E-039: Text Edit -0.1210 [-0.2384, -0.0044], Table TEDS +1.23) and dev (E-041: Text Edit -0.0011, zero regressions). Kept |
| I-12 | Retry looping pages in the other resolution mode (Base for Gundam) and keep the reading that does not loop | P-1 | Idea. The paper blames resolution for loops |
| I-13 | Retry ladder: a flagged page tries the guard, then the other mode (I-12), then split reading (I-14), and keeps the first reading that passes the checks (no loop, not cut short, not at the token cap) | P-4, P-5 | Idea. Needs I-11, I-15 first |
| I-14 | Split reading for dense pages: cut the page into overlapping strips or columns, read each, join in order. Each piece has fewer, larger characters and its own token budget | Newspapers (25% of the text error), the 14 pages still at the token cap | Idea. Join order and overlap removal are the hard part |
| I-15 | Cut-short check: flag a page whose output is much shorter than its text should be (from a Base reading, or ink density) so it is retried | P-5 (early stop, textbook page 055) | Idea |
| I-16 | Table repair from the error analysis of P-6: first find why each zero-TEDS table fails (no table, split, merged, wrong HTML), then fix the largest group | P-6, TEDS | Analysis first |
| I-17 | Measure what the memory cap costs: rerun P-5 and the problem set without the cap on a machine with more memory | P-5 | Needs another machine |
| I-7 | Resolution routing: pages with small text to Gundam, the rest to Base | Newspapers, small print | Planned earlier, not run |
| - | Tesseract fallback for pages the model cannot read | Unreadable scans | Needs your go (vertical Chinese data download) |

## Speed

| ID | Change | Status |
|---|---|---|
| I-5 | Newer mlx (0.32.1 to 0.32.4) in a separate env | Planned, not run |
| E-008 | Decode speed over a long request (`--log-speed`), for the paper's constant-speed claim | Planned, not run |
| - | Batched R-SWA | Needs your go (about half a day) |

## Already tried

See `findings.md` for each: loop repair I-1 (kept), broken-marker repair I-6 (no
effect), page-by-page decoding for long documents I-8 (kept), leaving page furniture
out E-022 (slightly worse), reading-order re-sorting (worst pages are a metric quirk),
higher resolution (newspapers already near the tile limit), ragged-table repair (2 of
37 table pages), best of two by confidence E-023 to E-025 (gain too small), 8-bit
weights and four experts I-2, I-3 (speed).

## Where to run

- **This Mac (M5, 16 GB):** dev and problem-set runs, under the 7.5 GB cap.
- **A lab Mac over SSH:** the best option for the next full run. MLX needs Apple
  Silicon. With 32 GB or more the cap can go (I-17), and this Mac stays free.
- **A rented cloud Mac:** same, but it costs money, so it needs a go first.
- **A Linux GPU machine:** cannot run the MLX port. It could run Baidu's original
  PyTorch model as a reference for the paper's numbers, and CDM runs there without
  emulation. It does not answer "on a Mac".

## Order

Done: E-028 scored (S-2), error analysis enough to fill P-4 to P-6.

1. Build the problem set (50 pages) with E-028 as its baseline.
2. I-9 and I-10 by rescoring (no model): a quick safety net and a first number.
3. I-11 on the problem set, then dev.
4. I-15, then I-13 (with I-12 inside it) on the problem set, then dev.
5. I-16: table analysis on P-6, then the fix it points to.
6. I-14 on newspapers and token-cap pages.
7. S-3, so CDM and Overall can be measured.
8. Next full run with every kept fix, on a lab Mac if one is available (I-17 there).
9. I-7 and the speed items.
