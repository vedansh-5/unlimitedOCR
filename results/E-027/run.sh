#!/bin/sh
# Full OmniDocBench v1.6 (1,651 pages) in bf16 with memory held under 8 GB, then
# re-run of flagged pages (loop, token cap, near-empty) with the coordinate-blind guard
# (E-028), the local evaluator, and formula CDM in the evaluator's Docker image.
# Each step can be re-run: fetched images and finished pages are skipped.
set -u
cd "$(dirname "$0")/../.."
. ./env.sh
CAP="--memory-limit-gb 7.5"
uv run python omnidocbench.py select --exp E-027 --per-type 100000
uv run python omnidocbench.py fetch --exp E-027
uv run python omnidocbench.py predict --exp E-027 $CAP
mkdir -p results/E-028
uv run python omnidocbench.py retry --exp E-028 --base E-027 --content-guard $CAP
uv run python omnidocbench.py evaluate --exp E-028
uv run python omnidocbench.py summary --exp E-028
uv run python compare.py score --exp E-028
uv run python omnidocbench.py evaluate-cdm --exp E-028
