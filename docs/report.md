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

## 3. Proposed modifications [draft]

Training is out of scope (section 6), so every change works at inference time on the
released weights. Each is tested alone against a baseline (section 4).

| ID | Change | Technical reason | Status |
|---|---|---|---|
| I-1 | Re-decode pages flagged as loops with a no-repeat guard that ignores `<\|det\|>` box coordinates | Baidu's 35-gram guard compares raw tokens; a loop that opens a new layout block per repeat changes the box tokens each time, so no 35-token sequence repeats exactly | Kept (5.2) |
| I-6 | Cut unclosed `<\|det\|>` markers in post-processing | A loop cut off by the token cap can leave a marker open, which leaks into the Markdown | Kept as an output option; no score effect |
| I-1L | Re-run flagged pages of a long document alone and splice them back in place | Targets the paper's stated long-document failure | Dropped: the model adds or drops pages (5.3), so position no longer identifies a page |
| I-8 | Decode long documents one page per request and join the outputs | Removes page bookkeeping and the output-token cap from the model's job; each token attends to one page's prefix | Kept (5.3) |
| I-2 | 8-bit and 4-bit weights for the decoder (vision encoders kept in bf16) | Decoding is memory-bandwidth bound; fewer bytes per weight should raise tokens/s and lower peak memory on a 16 GB machine | Code ready |
| I-3 | 4 or 5 routed experts per token instead of 6 | Routed experts are most of the work per token; experts are picked by softmax score, so the dropped ones carry the least weight | Code ready |
| I-7 | Route pages with small text to Gundam mode before decoding | Targets the paper's stated cause of long-document errors before it happens, instead of repairing after | Planned |

## 4. Experimental setup [verified]

- Hardware: MacBook Air, Apple M5, 10 cores, 16 GB unified memory, macOS 27.0.1.
- Software: MLX port `shubhxho/Unlimited-OCR-MLX` at commit `e4c39cd`, `mlx-vlm==0.6.16`,
  `mlx==0.32.1`, Python 3.12 via uv, all versions pinned to the port's lock file. Model
  `baidu/Unlimited-OCR` at revision `07dea83`, bf16, greedy decoding.
- OmniDocBench v1.6: dataset revision `aa1ee96`, official evaluator at commit `f133a71`
  in its own Python 3.11 environment. Formula CDM is not computed (it needs a Linux TeX
  toolchain), so the Overall score is not reported.
- Subsets: a test subset of 140 pages (15 per document type, all 5 historical
  documents, seed 42) and a disjoint dev subset of 45 pages (5 per type, seed 42, test
  pages excluded; it has no historical documents, since all 5 are in the test subset).
  Changes are tried on dev and confirmed on test.
- Statistics: per-type means are reweighted to the full benchmark's type mix (1,651
  pages); 95% intervals come from 2,000 stratified bootstrap resamples (pages
  resampled within type, seed 0). A change is compared with its baseline page by page
  (paired), and counts as an improvement only if the interval of the difference
  excludes zero. `compare.py` computes all of these.
- Long documents: the paper's long-document set is not public. We use page prefixes
  (2, 5, 10, 20, 40 pages) of three public NIST publications, each sent as one
  request, scored by normalized edit distance against the PDF text layer and by the
  paper's distinct-n repetition measure.
- Logged per document: wall time, model time, prompt and output tokens, tokens/s,
  peak memory, finish reason, and repetition flags.

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
over-samples historical documents, per-type means of the edit metrics are reweighted
to the full benchmark's type mix; table scores are page averages over the 37 pages with
tables, as in the evaluator's headline. Intervals are 95% bootstrap (2,000 resamples).
All values are produced by `compare.py score --exp E-002`.

| Metric | This work (MLX, M5, 16 GB) | Paper (GPU) | Official leaderboard |
|---|---|---|---|
| Text Edit (lower is better) | 0.036 [0.024, 0.051] | 0.042 | 0.039 |
| Table TEDS | 92.4 [88.1, 95.9] | 90.2 | 90.2 |
| Table TEDS-S | 94.9 [91.7, 97.6] | 93.3 | 93.4 |
| Reading-order Edit (lower is better) | 0.107 [0.078, 0.142] | 0.129 | 0.128 |

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

### 5.3 Long documents: one request against page by page [verified]

Setup in section 4: page prefixes (2 to 40 pages) of three NIST reports, scored against
the PDF text layer. The text layer misses text inside images, so absolute values are
higher than the paper's and not comparable with its Table 3; the runs below are
compared on the same documents.

| Pages | One request, Base (E-003): edit / recall / s | Page by page, Base (E-010) | Page by page, Gundam (E-009) |
|---|---|---|---|
| 2 | 0.138 / 0.934 / 9 | 0.136 / 0.938 / 7 | 0.137 / 0.934 / 10 |
| 5 | 0.104 / 0.973 / 31 | 0.039 / 0.973 / 25 | 0.038 / 0.977 / 33 |
| 10 | 0.200 / 0.959 / 86 | 0.101 / 0.958 / 64 | 0.096 / 0.960 / 80 |
| 20 | 0.110 / 0.953 / 194 | 0.104 / 0.961 / 141 | 0.091 / 0.961 / 166 |
| 40 | 0.228 / 0.917 / 502 | 0.077 / 0.968 / 283 | 0.062 / 0.967 / 337 |

In one request the model added or dropped a page in 10 of 15 documents (from 5 pages
up), and two of the three 40-page documents ran into the 32,768-token output limit
(NIST pages need about 800 tokens each). Splitting into one request per page removes
both failures, raises recall at 40 pages from 0.917 to 0.968, and cuts model time by
44%, because each output token then attends to one page's prefix instead of all pages'.
Gundam resolution adds a small further gain in edit distance at about 19% more time.

R-SWA does what the paper claims for memory: peak memory stayed between 8 and 11.4 GB
up to 40 pages in one request. On this machine and these documents, though, the
limits of one long request (output budget, page bookkeeping) cost more than its
benefit. Cross-page structure, which the text-layer reference cannot score, is the
case where one request may still be the better choice.

## 6. Discussion and limitations [draft]

- Training-based improvements are out of reach on this hardware.
- The paper's long-document test set is not public, so long-document comparisons are by
  trend only.
- The MLX port has not been independently checked against the official CUDA model;
  any gap we measure may come from the port rather than the model.

## 7. Conclusions [planned]
