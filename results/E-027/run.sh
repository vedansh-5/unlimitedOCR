#!/bin/sh
# Full OmniDocBench v1.6 (1,651 pages) in bf16 with memory held under 8 GB, then
# re-run of flagged pages (loop, token cap, near-empty) with the coordinate-blind guard
# (E-028), the local evaluator, and formula CDM in the evaluator's Docker image.
# Each step can be re-run: fetched images, finished pages and matched pages are skipped.
# Start it with nice -n 10. The model steps run in background mode so the Mac stays usable;
# scoring is CPU-only and would crawl on the efficiency cores, so it keeps normal priority.
set -u
cd "$(dirname "$0")/../.."
. ./env.sh
CAP="--memory-limit-gb 7.5"
uv run python omnidocbench.py select --exp E-027 --per-type 100000
uv run python omnidocbench.py fetch --exp E-027
# A Metal GPU timeout kills the process mid-run; finished pages are skipped, so try again.
for attempt in 1 2 3 4 5; do
  taskpolicy -b uv run python omnidocbench.py predict --exp E-027 $CAP
  missing=$(( $(wc -l < results/E-027/subset.txt) - $(ls results/E-027/raw/*.json | wc -l) ))
  [ "$missing" -le 0 ] && break
  echo "attempt $attempt: $missing pages missing, trying again"
done
mkdir -p results/E-028
taskpolicy -b uv run python omnidocbench.py retry --exp E-028 --base E-027 --content-guard $CAP
uv run python omnidocbench.py evaluate --exp E-028
uv run python omnidocbench.py summary --exp E-028
uv run python compare.py score --exp E-028
uv run python omnidocbench.py evaluate-cdm --exp E-028
