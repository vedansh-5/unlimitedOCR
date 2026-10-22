#!/bin/zsh
# E-001c: E-001b page 10 with chunked prefill disabled (one change). Run from the repo root after `source env.sh`.
set -eu
OUT=results/E-001c
PDF=tests/data/unlimited_ocr_paper.pdf

mkdir -p $OUT/inputs
pdftoppm -r 300 -f 10 -l 10 -png $PDF $OUT/inputs/paper_p10
uv run python run_ocr.py --image $OUT/inputs/paper_p10-10.png --prefill-step-size 100000 \
  --output-dir $OUT/a_gundam_p10_noprefillchunk > $OUT/a_log.txt 2>&1
