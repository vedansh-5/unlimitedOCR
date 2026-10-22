# Experiment log

Chronological. One entry per meaningful action or decision.

## 2026-10-23: Project start, Step 1 plan

- **Task:** run Unlimited-OCR on the Mac and log per-document runtime, memory and
  failures.
- **Instruction:** use the community MLX port, do not reimplement the model; explain
  design choices before implementing; small reviewed steps; no web UI.
- **Action:** checked the machine (M5, 16 GB, macOS 27.0.1, uv missing, Python 3.14.7)
  and wrote the Step 1 plan in `docs/plan.md`.
- **Decision:** call the port's CLI as a subprocess per document, so peak memory is
  measured per document and one crash does not stop a batch.
- **Outcome:** plan proposed, awaiting approval.

## 2026-10-23: Scope widened to "improve on the paper"

- **Instruction:** improve performance beyond the paper's reported results; establish
  a baseline first; keep `report.md`, `summary.md`, `findings.md`, `experiment_log.md`
  current; change one variable at a time; no API models yet.
- **Action:** read the paper (arXiv 2606.23050), the model `config.json`, and the MLX
  port's README, TRAINING notes and CLI (R-001 in `findings.md`).
- **Result:** decoder confirmed as MoE (64 experts, top-6). Paper gains came from GPU
  cluster training. The port states LoRA training does not fit in 16 GB.
- **Decision (proposed):** keep Step 1 as the base. Add an OmniDocBench baseline as
  E-002, and rank inference-time improvements first. Training-based ideas are deferred
  unless more memory or a paid GPU is approved.
- **Docs:** created `docs/report.md`, `docs/summary.md`, `docs/findings.md`, this log.
  `docs/decisions.md` and `STATUS.md` from the first plan are dropped; this log and
  `summary.md` replace them.
- **Outcome:** awaiting approval of the plan and first experiment.

## 2026-10-23: No training

- **Instruction:** do not train or fine-tune the model. Use the released weights as
  published; improve only what happens around the model.
- **Decision:** LoRA and any other training are removed from the plan, not deferred.
  All improvements are inference-time: input preparation, decoding settings, page
  grouping, failure detection and retry, output cleanup, quantization, expert count.
- **Consequence:** results are compared against the paper on equal weights. Any gain
  is attributable to the pipeline, not to new training data.

## 2026-10-23: Contained setup, pinned versions, public repo

- **Instruction:** everything must be removable with one command and must not touch
  the system or other dev environments; use a folder named `unlimitedOCRvenv`.
- **Action:** uv installed into `unlimitedOCRvenv/uv` (a venv made with the system
  python3); Python 3.12.15, packages, uv cache and Hugging Face cache all redirected
  into `unlimitedOCRvenv/` through `env.sh`. Removal: `rm -rf unlimitedOCRvenv`.
- **Finding:** a plain `uv sync` resolved newer packages than the port was tested with
  (e.g. huggingface-hub 2.2.0 vs 1.28.0, pillow 13.0.0 vs 12.3.0, mlx 0.32.4 vs
  0.32.1).
- **Decision:** constrain every package to the port's own `uv.lock` (Python 3.12
  entries) so the baseline matches the port's tested environment. Newer versions
  become experiment I-5, tested after the baseline, one package at a time.
- **Instruction:** publish the project as a public GitHub repository.
- **Action:** created `vedansh-5/unlimitedOCR` (public). `rules.md`, the venv folder and
  rendered inputs are not committed.

## 2026-10-23: E-001 first attempt failed; port bug fixed locally

- **Problem:** the first model run crashed on its first generated token.
- **Action:** traced it to a shape bug in the port's no-repeat guard (details in
  `findings.md`, E-001a). Added a failing test, then `run_ocr.py`, which fixes the
  output shape and otherwise runs the port's CLI unchanged.
- **Decision:** fix in our repo instead of editing installed packages, so the fix is
  versioned, visible and reproducible. All runs now go through `run_ocr.py`.
- **Outcome:** test passes; E-001 rerun started.

## 2026-10-23: E-001 done

- **Result:** both runs completed. 17 s for a dense gundam page, about 8 s per page in
  base mode, peak 9.6 GB. Details and quality notes in `findings.md`, E-001.
- **Issues found:** text missing or made up at the start of the output in both runs;
  `/usr/bin/time` around `uv run` does not measure the model process.
- **Decision:** E-002 (OmniDocBench subset) is affordable at under an hour. The batch
  runner will launch the venv Python directly so process memory is measured correctly.
- **Results:** `results/E-001/`.
