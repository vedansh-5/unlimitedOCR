# Team tasks for the evaluation (2026-10-29)

Repository: https://github.com/vedansh-5/unlimitedOCR, branch `dev/table-split-and-dedup`.
`master` has everything up to the full run (E-028); this branch adds the problem-set
fixes (E-030 to E-049).

Each teammate also has a zip file with the data for their task and a README with the
exact steps. Those READMEs are the instructions; this page says where things are in the
repository.

## Where to look

| What | Where |
|---|---|
| Short report for the evaluators (source of every number) | `docs/report.md` (arrives with the next push; until then use the copy in `slides.zip`) |
| Full method and tables | `docs/report_detailed.md` |
| One-page status | `docs/summary.md` |
| Every experiment, in order | `docs/experiment_log.md` |
| Fix ideas and what each one targets | `docs/fixes.md` |
| Per-experiment output and scores | `results/E-xxx/` (`summary.json`, `score.txt`, `pred/`) |

## Who does what

| Person | Machine | Task | Instructions |
|---|---|---|---|
| Vedansh | M5, 16 GB | Full-set rescore with all kept fixes (no model run), final report, review | `docs/report.md` |
| Windows teammate | Windows, Docker | Formula score (CDM) on the 313 formula pages of E-028 | `formula_score/README.md` in the zip |
| M1 teammate | M1, 8 GB | Slides, two charts, three before/after examples, cold read of the report | `slides/README.md` in the zip |

## Rules for everyone

- Nobody runs the OCR model except on Vedansh's machine, and there are no full-set model
  runs before the evaluation.
- Every number comes from a results file. If a number is missing, leave it blank and say
  so; never estimate it.
- Answer-key files (`gt*.json`), page images and the match cache are never committed.
- Send results to Vedansh rather than pushing to this repository.

## Expected results

- Formula score: the CDM value and formula Edit distance from
  `result/predictions_quick_match_run_summary.json`, plus the run time. Our local
  formula Edit distance on the full run is 0.110, so the new one should be close to it.
  Vedansh combines CDM with the full-set text and table scores to get the Overall score.
- Slides: about 10 slides following the report's six sections, with a blank, marked row
  for the full-set score with fixes until that number is final.
