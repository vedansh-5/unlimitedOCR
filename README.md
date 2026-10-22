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

# One image, high-resolution "gundam" mode
uv run unlimited-ocr-mlx --image page.png --output-dir results/out

# A PDF, all pages in one request, "base" mode
uv run unlimited-ocr-mlx --pdf doc.pdf --output-dir results/out

# Long PDF in independent chunks of 8 pages
uv run unlimited-ocr-mlx --pdf doc.pdf --max-pages-per-request 8 --output-dir results/out
```

Each request writes a Markdown file with the raw model output and a JSON file with
timing, token counts, peak memory and finish reason.

## Pinned versions

- MLX port: commit `e4c39cde12444991663c8d75a5b8c96d2e78d8e4`
- Model: `baidu/Unlimited-OCR` at `07dea832e22aefee32ad281d4b80551282e1c168` (set by the port)
- All other packages are constrained to the versions in the port's own `uv.lock`
  (`[tool.uv] constraint-dependencies` in `pyproject.toml`), so results match the
  environment the port was tested in.

## Project record

`docs/plan.md` (plan and experiment list), `docs/summary.md` (current status),
`docs/experiment_log.md`, `docs/findings.md`, `docs/report.md`.
