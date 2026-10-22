# Unlimited-OCR on Apple Silicon: Reproduction and Improvements

Status of each section is marked: **[verified]** (from a source we checked or our own
measurement), **[planned]** (not yet done), **[draft]** (preliminary).

## 1. Problem statement and objectives [draft]

End-to-end OCR models with an LLM decoder keep a key-value (KV) cache that grows with
every output token. Long documents therefore get slower and use more memory as
decoding goes on. Unlimited-OCR addresses this with Reference Sliding Window Attention
(R-SWA), which keeps the cache at a fixed size.

The official release targets NVIDIA GPUs only. This project:

1. runs the released model on a 16 GB Apple Silicon laptop through the MLX framework;
2. checks how closely that setup reproduces the paper's reported results;
3. tests changes that improve accuracy, robustness or efficiency, and reports each
   against a measured baseline.

## 2. Original method and reported results [verified: taken from the paper]

Source: Baidu, "Unlimited OCR Works", arXiv 2606.23050 (2026); code and weights at
github.com/baidu/Unlimited-OCR (MIT).

### 2.1 Architecture

| Part | Detail |
|---|---|
| Vision encoder | DeepEncoder from DeepSeek-OCR: SAM ViT-B (window attention) then CLIP-L (global attention), 16x token compression; a 1024x1024 page becomes 256 visual tokens |
| Projector | Linear, 2048 to 1280 |
| Decoder | DeepSeek-V2-style MoE, 12 layers, hidden size 1280, 64 routed experts, 6 active per token, 2 shared experts, first layer dense; about 3B total and 0.5B active parameters |
| Attention | R-SWA in every decoder layer: each output token attends to all prefix tokens (image and prompt) plus the previous n = 128 output tokens |
| Image modes | "Gundam" (1024 global view plus 640 crops) for single pages; "Base" (one 1024 view per page) for multi-page input |
| Decoding | Greedy; a no-repeat guard bans any 35-token sequence already seen in the last 128 (single page) or 1024 (multi-page) tokens |

The KV cache after T output tokens is L_m + min(n, T), where L_m is the prefix length,
instead of L_m + T for standard attention.

### 2.2 Training (not reproducible here)

Continued training from DeepSeek-OCR: about 2M samples (90% single page, 10% synthetic
multi-page of 2 to 50 pages), 4,000 steps, global batch 256, 32K sequence length,
8x16 A800 GPUs, AdamW, cosine schedule, learning rate 1e-4. Encoder frozen.

### 2.3 Reported results

OmniDocBench (Table 1 of the paper):

| Version | Overall up | Text Edit down | Formula CDM up | Table TEDS up | Table TEDS-S up | Read-order Edit down |
|---|---|---|---|---|---|---|
| v1.5, DeepSeek-OCR | 87.01 | 0.073 | 83.37 | 84.97 | 88.80 | 0.086 |
| v1.5, Unlimited-OCR | 93.23 | 0.038 | 92.61 | 90.93 | 94.07 | 0.045 |
| v1.6, Unlimited-OCR | 93.92 | 0.042 | 95.79 | 90.16 | 93.32 | 0.129 |

Text edit distance per document type, v1.5 (Table 2):

| Type | PPT | Academic paper | Book | Colorful textbook | Exam paper | Magazine | Newspaper | Note | Research report |
|---|---|---|---|---|---|---|---|---|---|
| Text | 0.025 | 0.023 | 0.019 | 0.046 | 0.049 | 0.020 | 0.081 | 0.066 | 0.008 |
| Reading order | 0.023 | 0.012 | 0.025 | 0.051 | 0.049 | 0.061 | 0.134 | 0.018 | 0.013 |

Column order checked against the rendered PDF page.

Long-document parsing on an in-house set (Table 3, not released):

| Pages | 2 | 5 | 10 | 15 | 20 | 40+ |
|---|---|---|---|---|---|---|
| Distinct-20 up | 99.76% | 99.78% | 97.49% | 99.92% | 98.73% | 96.08% |
| Distinct-35 up | 99.87% | 99.98% | 99.83% | 99.99% | 99.89% | 96.90% |
| Edit distance down | 0.0362 | 0.0452 | 0.0526 | 0.0787 | 0.0572 | 0.1069 |

The authors attribute most 40+ page errors to repetition on small text, caused by the
1024x1024 "Base" mode used for multi-page input.

Speed: 5,580 tokens/s on OmniDocBench at 512 concurrent requests on GPU, versus 4,951
for DeepSeek-OCR. These numbers are not comparable to a single laptop.

## 3. Proposed modifications [planned]

Ranked candidates are in `docs/plan.md`. Each one gets a technical justification here
once it is selected and tested.

## 4. Experimental setup [planned]

- Hardware: MacBook Air, Apple M5, 10 cores, 16 GB unified memory, macOS 27.0.1.
- Software: MLX port `shubhxho/Unlimited-OCR-MLX` at commit `e4c39cd`, `mlx-vlm==0.6.16`,
  Python 3.12 via uv. Model `baidu/Unlimited-OCR` at the revision the port pins.
- Benchmarks: OmniDocBench (official evaluator, version to be fixed) and a long-document
  set built for this project.
- Metrics: the paper's metrics, plus runtime, peak memory and failure flags per document.

### 4.1 Corrections to the MLX port [verified]

Two defects in the port were found and fixed before any measurement. Both are applied
in `run_ocr.py`, which otherwise runs the port's code unchanged.

1. **Decoding crash.** The port's no-repeat guard returned logits without their batch
   dimension when called by mlx-vlm 0.6.16, so every run failed on the first generated
   token. The fix restores the shape; the banned-token rule is unchanged. A unit test
   reproduces the defect.
2. **Prompt mismatch.** The port's prompt ended with a space token that Baidu's
   reference code strips. On the smoke-test pages this caused a skipped opening
   paragraph and a hallucinated date at the start of the output; removing the space
   fixed both and left the rest of the output identical. All runs use Baidu's prompt
   format.

## 5. Results [planned]

No results yet.

## 6. Discussion and limitations [draft]

- Training-based improvements are out of reach on this hardware.
- The paper's long-document test set is not public, so long-document comparisons are by
  trend only.
- The MLX port has not been independently checked against the official CUDA model;
  any gap we measure may come from the port rather than the model.

## 7. Conclusions [planned]
