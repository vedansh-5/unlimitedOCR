# Unlimited-OCR on Apple Silicon

Runs Baidu's [Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) (arXiv 2606.23050)
on a Mac through the MLX port
[`shubhxho/Unlimited-OCR-MLX`](https://huggingface.co/shubhxho/Unlimited-OCR-MLX),
using the released weights unchanged.

## Setup

Requirements: Apple Silicon Mac, any `python3` (only used once to install uv), git,
about 10 GB free disk.

Everything (uv, Python 3.12, packages, caches, model weights) is kept in
`unlimitedOCRvenv/` inside this folder. Nothing is installed system-wide and no shell
profile is changed.

```bash
python3 -m venv unlimitedOCRvenv/uv
unlimitedOCRvenv/uv/bin/pip install --no-cache-dir uv
source env.sh
uv python install 3.12
uv sync
```

`source env.sh` is needed in every new terminal before running anything here.

The first model run downloads `baidu/Unlimited-OCR` (6.7 GB) into
`unlimitedOCRvenv/hf/`.

### Remove everything

```bash
rm -rf unlimitedOCRvenv
```

## Run

```bash
source env.sh

# PDF or image to clean Markdown
uv run python ocr_to_md.py doc.pdf -o doc.md

# Raw model output: one image ("gundam" mode), or a PDF in one request ("base" mode)
uv run python run_ocr.py --image page.png --output-dir results/out
uv run python run_ocr.py --pdf doc.pdf --max-pages-per-request 8 --output-dir results/out
```

`run_ocr.py` runs the port's CLI with two fixes (see `docs/findings.md`, E-001a and
E-001b) and accepts all of its options.

Each request writes a Markdown file with the raw model output and a JSON file with
timing, token counts, peak memory and finish reason.

## Batch runs and OmniDocBench

```bash
# OCR every PDF/image in a folder; one CSV row per document in results/<exp>/runs.csv
uv run python run_batch.py --exp E-003 --inputs tests/data --max-pages-per-request 8

# OmniDocBench v1.6 subset (15 pages per document type, seed 42)
uv run python omnidocbench.py select   --exp E-002
uv run python omnidocbench.py fetch    --exp E-002
uv run python omnidocbench.py predict  --exp E-002
uv run python omnidocbench.py evaluate --exp E-002
```

`evaluate` needs the official evaluator in its own Python 3.11 environment, also kept in
`unlimitedOCRvenv/`:

```bash
git clone https://github.com/opendatalab/OmniDocBench unlimitedOCRvenv/third_party/OmniDocBench
git -C unlimitedOCRvenv/third_party/OmniDocBench checkout f133a71
uv venv --python 3.11 unlimitedOCRvenv/omnidocbench-env
uv pip install --no-config --exclude-newer 2025-09-26 \
  --python unlimitedOCRvenv/omnidocbench-env/bin/python ./unlimitedOCRvenv/third_party/OmniDocBench
```

Formula CDM is not computed: it needs Linux, TeX Live, ImageMagick and Ghostscript.

## Pinned versions

- MLX port: commit `e4c39cde12444991663c8d75a5b8c96d2e78d8e4`
- Model: `baidu/Unlimited-OCR` at `07dea832e22aefee32ad281d4b80551282e1c168` (set by the port)
- All other packages are constrained to the versions in the port's own `uv.lock`
  (`[tool.uv] constraint-dependencies` in `pyproject.toml`), so results match the
  environment the port was tested in.

## Project record

`docs/plan.md` (plan and experiment list), `docs/summary.md` (current status),
`docs/experiment_log.md`, `docs/findings.md`, `docs/report.md`.
