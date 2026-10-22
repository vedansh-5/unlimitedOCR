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

## 5. Results

### 5.1 Reproduction on OmniDocBench v1.6 [verified]

140 pages (15 per document type, all 5 historical documents; seed 42), official
evaluator at commit `f133a71`, formula CDM not computed. Because the subset
over-samples historical documents, per-type means are reweighted to the full
benchmark's type mix; intervals are 95% stratified bootstrap (2,000 resamples).

| Metric | This work (MLX, M5, 16 GB) | Paper (GPU) | Official leaderboard |
|---|---|---|---|
| Text Edit (lower is better) | 0.036 [0.024, 0.051] | 0.042 | 0.039 |
| Table TEDS | 92.4 [88.7, 95.7] | 90.2 | 90.2 |
| Table TEDS-S | 94.9 [91.9, 97.5] | 93.3 | 93.4 |
| Reading-order Edit (lower is better) | 0.107 [0.078, 0.143] | 0.129 | 0.128 |

All reference values fall inside the intervals: the MLX implementation, with the two
corrections in section 4.1, reproduces the published accuracy within sampling error.
Inference took 18.1 s per page on average at 75 output tokens/s, with peak memory of
10.0 GB.

Two of 140 pages (both historical documents) ended in repetition loops. In both, each
repeated line is a separate layout block with new box coordinates, so no 35-token
sequence repeats exactly and the decode-time n-gram guard never triggers.

### 5.2 Loop repair, I-1 [verified]

**Problem.** Some pages end in repetition loops (2 of 140 test pages, 1 of 45 dev
pages). In every case the model starts a new layout block for each repeat, with new
box coordinates. Because the decode-time guard bans only exact 35-token repeats, the
changing coordinates hide the loop from it.

**Method.** (1) A detector flags a page when one block's text, with the
`<|det|> type [box] <|/det|>` prefix removed, repeats 6 or more times, or when a marker
is left unclosed. The threshold was fixed before looking at test pages. (2) Flagged
pages are re-decoded with the same 35-token rule applied to the text with marker spans
removed, so a repeat that only changes coordinates is blocked. All other pages are left
untouched.

**Results.**

| Subset | Pages re-run | Text Edit before, after | Read-order Edit before, after | Time on re-run pages |
|---|---|---|---|---|
| Dev (45) | 1 | 0.0526, 0.0422 | 0.1343, 0.1306 | 377 s, 19 s |
| Test (140) | 2 | 0.0589, 0.0587 | 0.1271, 0.1286 | 45 s, 23 s |

On the dev page (a newspaper puzzles page) the loop was the failure: the page ran into
the 32,768-token limit repeating one sentence 555 times. Repair recovered the content
(page text edit 0.829 to 0.371) and cut its decoding time by 95%. The two test pages are
warped scans of vertical classical Chinese that the model cannot read; there the loop is
a symptom, and repair reduces repetition without making the text correct. Loop repair
therefore helps when decoding runs away on a readable page, and is neutral otherwise.

## 6. Discussion and limitations [draft]

- Training-based improvements are out of reach on this hardware.
- The paper's long-document test set is not public, so long-document comparisons are by
  trend only.
- The MLX port has not been independently checked against the official CUDA model;
  any gap we measure may come from the port rather than the model.

## 7. Conclusions [planned]
