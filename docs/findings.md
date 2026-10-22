# Findings

Experiment entries use the format: what and why, hypothesis, configuration, observed
result, hypothesis supported or not, lessons, follow-ups. IDs match
`experiment_log.md` and `plan.md`.

## R-001: Source review before any run (2026-10-23)

Reading only, no model run.

| Question | Finding | Source |
|---|---|---|
| Is the decoder MoE? | Yes. 12 layers, 64 routed experts, top-6, 2 shared, first layer dense, hidden 1280, R-SWA window 128 | `baidu/Unlimited-OCR` `config.json` at `8249d20` |
| What was the main benchmark? | OmniDocBench v1.5 and v1.6, official evaluator | Paper section 5.1 |
| How were the gains obtained? | Continued training on 128 A800 GPUs | Paper section 4.2 |
| Can we train on this Mac? | Not safely. The port's own notes say BF16 weights plus LoRA state do not fit in 16 GB; 32 GB for small LoRA runs, 64 GB+ in practice | Port `TRAINING.md` at `e4c39cd` |
| Is the MLX port checked against the CUDA model? | No published parity check; the author says a quantized checkpoint waits on one | Port `README.md` |
| Does the port support both image modes? | Yes: `--mode gundam/base/auto`, plus `--no-repeat-ngram-size`, `--ngram-window`, `--max-pages-per-request`, `--prefill-step-size`, `--adapter-path` | Port `infer_mlx.py` |
| Is the long-document test set public? | No, in-house | Paper section 5.1 |
| Known long-document failure | Repetition on small text at 40+ pages, blamed on Base mode resolution | Paper section 5.4 |
| Dataset size | OmniDocBench on Hugging Face: about 1.55 GB, about 1,650 images (v1.6). v1.5 has 1,355 pages | HF API, paper |

Lessons:
- "Beating the paper" on OmniDocBench accuracy through training is not feasible on
  this hardware. Inference-time changes are the realistic lever.
- The paper's own stated weakness (long-document repetition) is the clearest target.
- Every comparison to the paper's numbers must first account for a possible MLX vs
  CUDA gap, which E-002 measures.

Not yet checked:
- Whether the port's no-repeat guard and R-SWA cache match the upstream code line for
  line (plan item 1.2).
- Whether the OmniDocBench evaluator's formula metric (CDM) runs on macOS.
