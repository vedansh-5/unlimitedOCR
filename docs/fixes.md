# Fix log

Every fix idea in one place, with what it targets and how it is tested. Started
2026-10-26, after the full run (E-027 predictions, E-028 retry).

How a fix is tried:

1. **Problem pages first.** Each fix names the page set it targets (below). A fix that
   needs no model is tried by rescoring (`omnidocbench.py rescore`, then
   `compare.py diff` against E-028). A fix that needs the model reruns only those pages.
2. **Then the dev subset** (E-004, 45 pages), as one change against the dev baseline.
3. **Then the test subset** (E-002, 140 pages), only if kept on dev.

One change per run. Every model run uses `--memory-limit-gb 7.5`.

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

**P-4: worst pages per type** from the error analysis of E-028. To fill in once its
scores are in.

## Scoring (no effect on scores)

| ID | Change | Status |
|---|---|---|
| S-1 | Per-page match cache (`match_cache.py`): each page's match is stored under a hash of its ground truth, prediction, match settings and evaluator code, so a stopped scoring run resumes and a rescore only matches changed pages | Done. E-004 result files identical; 4 min 19 s cold, 15 s cached |
| S-2 | LaTeX-to-text without a fresh process for short formulas, and each result kept. The evaluator starts a new Python process per conversion so it can cut off a stuck one; on macOS that costs about 2 s each, and a looping page converts the same formulas thousands of times | Done. E-004 result files identical; 13 s from an empty cache. The two P-1 pages that held up E-028 for over an hour are the test |
| S-3 | CDM from the local matches: run only the formula CDM in Docker, on the formula pairs the local run already matched, instead of the image re-matching all 1,651 pages | Idea. The image's evaluator code differs from our local copy and runs under x86 emulation, so a plain CDM run is estimated at 11 to 20 h. Time a plain CDM run on E-004 first and check S-3 against it |

## Accuracy, no model run (rescore)

| ID | Change | Targets | Status |
|---|---|---|---|
| I-9 | Cut counting loops in the Markdown: find a block that repeats with only its numbers changing, keep the first few repeats, drop the rest | P-1, P-2 | Idea. Try on P-1, then rescore E-028 in full (cheap with S-1 and S-2) |
| I-10 | Cut runaway empty tables: a table that goes on with rows of empty cells past the point where the page could hold them | P-3 | Idea |

## Accuracy, model run on flagged pages only

| ID | Change | Targets | Status |
|---|---|---|---|
| I-11 | Number-blind loop check and repeat guard: `loops.py` and `--content-guard` treat digits as equal, so counting loops are flagged for the retry and blocked during it | P-1, P-2; also the two never flagged | Idea. Retry P-1 only, then dev |
| I-12 | Retry looping pages in the other resolution mode (Base for Gundam) and keep the reading that does not loop | P-1 | Idea. The paper blames resolution for loops |
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

## Order

1. Finish E-028 scoring with S-2 (running).
2. I-9 on P-1, then a full rescore of E-028.
3. I-11 on P-1 and P-2, then dev.
4. Error analysis of E-028, which fills P-4 and may add fixes here.
5. S-3, then CDM.
6. I-10, I-12, I-7 and the speed items, in that order.
