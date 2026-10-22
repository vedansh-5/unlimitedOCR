#!/bin/zsh
# E-001: smoke test and cost. Run from the repo root after `source env.sh`.
set -eu
OUT=results/E-001
PDF=tests/data/unlimited_ocr_paper.pdf

{ date -u +%FT%TZ; sw_vers -productVersion; sysctl -n machdep.cpu.brand_string hw.memsize; git rev-parse --short HEAD 2>/dev/null || true; } > $OUT/env.txt
mkdir -p $OUT/inputs
pdftoppm -r 300 -f 10 -l 10 -png $PDF $OUT/inputs/paper_p10
vm_stat > $OUT/vm_stat_before.txt

/usr/bin/time -l uv run python run_ocr.py --keep-prompt-space --image $OUT/inputs/paper_p10-10.png \
  --output-dir $OUT/a_gundam_p10 2> $OUT/a_time.txt

/usr/bin/time -l uv run python run_ocr.py --keep-prompt-space --pdf $PDF --first-page 1 --last-page 3 \
  --output-dir $OUT/b_base_p1-3 2> $OUT/b_time.txt
