2018年1月1日
<|det|>header [126, 28, 325, 75]<|/det|>Baidu百度
<|det|>title [357, 135, 642, 155]<|/det|>Unlimited OCR Works
<|det|>text [287, 162, 711, 180]<|/det|>Welcome the Era of One-shot Long-horizon Parsing
<|det|>text [456, 212, 542, 226]<|/det|>Baidu Inc.
<|det|>title [448, 273, 550, 291]<|/det|>Abstract
<|det|>text [113, 317, 886, 590]<|/det|>Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However, the downside is equally evident: as the output sequence lengthens, the accumulated KV cache drives up memory consumption and progressively slows down generation. This stands in stark contrast to humans, who exhibit no such decline in efficiency during long-horizon copying tasks. In this technical report, we propose Unlimited OCR, a model designed to emulate human parsing working memory. Taking DeepSeek OCR as the baseline, we replace all attention layers in the decoder with our proposed Reference Sliding Window Attention (R-SWA), which reduces attention computation costs while maintaining a constant KV cache throughout the entire decoding process. By combining the high compression rate of DeepSeek OCR's encoder with our constant KV cache design, Unlimited OCR can transcribe dozens of pages of documents in a single forward pass under a standard maximum length of 32K. More importantly, R-SWA is a general-purpose parsing attention mechanism — beyond OCR, it is equally applicable to tasks such as ASR, translation, etc. Codes and model weights are publicly available at http://github.com/baidu/Unlimited-OCR.
<|det|>image [167, 601, 825, 804]<|/det|>
<|det|>image_caption [113, 813, 885, 896]<|/det|>Figure 1 | Illustration of Reference Sliding Window Attention (R-SWA). Each generated token attends to all reference tokens (visual tokens in OCR) and the preceding n output tokens (128 by default). Compared to standard full attention, R-SWA maintains a constant KV cache throughout decoding. Compared to vanilla SWA, it preserves visual token fidelity by excluding them from state transitions, thereby avoiding progressive blurring.
<PAGE><|det|>title [115, 101, 212, 117]<|/det|>Contents
<|det|>title [117, 143, 884, 159]<|/det|>1 Introduction 3
<|det|>title [116, 178, 884, 194]<|/det|>2 Related Works 4
<|det|>text [143, 200, 884, 216]<|/det|>2.1 Pipeline-based Framework 4
<|det|>text [143, 222, 885, 238]<|/det|>2.2 End-to-end Model 4
<|det|>list [143, 200, 885, 238]<|/det|>
<|det|>text [186, 244, 884, 261]<|/det|>2.2.1 High-compression Encoder 4
<|det|>text [186, 267, 885, 283]<|/det|>2.2.2 High-efficiency Decoder 4
<|det|>list [186, 244, 885, 283]<|/det|>
<|det|>title [116, 303, 884, 320]<|/det|>3 Methodology 5
<|det|>text [143, 325, 884, 342]<|/det|>3.1 Long-horizon Parsing 5
<|det|>text [143, 348, 884, 363]<|/det|>3.2 Architecture 5
<|det|>text [143, 370, 884, 386]<|/det|>3.3 DeepEncoder 5
<|det|>text [143, 393, 884, 409]<|/det|>3.4 Reference Sliding Window Attention 6
<|det|>list [143, 325, 884, 409]<|/det|>
<|det|>text [186, 415, 884, 431]<|/det|>3.4.1 Attention computation 6
<|det|>text [186, 438, 884, 454]<|/det|>3.4.2 KV cache management 7
<|det|>text [186, 460, 884, 476]<|/det|>3.4.3 Kernel study 7
<|det|>list [186, 415, 884, 476]<|/det|>
<|det|>title [115, 496, 884, 513]<|/det|>4 Experimental Settings 8
<|det|>text [143, 518, 884, 534]<|/det|>4.1 Data Engine 8
<|det|>text [143, 540, 884, 556]<|/det|>4.2 Implementation Details 8
<|det|>list [143, 518, 884, 556]<|/det|>
<|det|>title [115, 577, 884, 592]<|/det|>5 Evaluation 8
<|det|>text [143, 599, 884, 615]<|/det|>5.1 Benchmark and Metrics 8
<|det|>text [143, 621, 884, 637]<|/det|>5.2 Main Results 9
<|det|>text [143, 643, 884, 660]<|/det|>5.3 Subcategory Study 10
<|det|>text [143, 666, 884, 683]<|/det|>5.4 Long-horizon Parsing 10
<|det|>list [143, 599, 884, 683]<|/det|>
<|det|>title [115, 702, 884, 718]<|/det|>6 Efficiency Analysis 11
<|det|>title [115, 738, 884, 754]<|/det|>7 Limitation and Future Work 11
<|det|>title [115, 773, 884, 789]<|/det|>8 Conclusion 11
<|det|>title [115, 809, 884, 825]<|/det|>9 Author List 12
<|det|>page_number [493, 923, 506, 935]<|/det|>2
<PAGE><|det|>title [115, 100, 274, 116]<|/det|>1. Introduction
<|det|>text [112, 131, 884, 310]<|/det|>Humans are remarkably adept at seemingly straightforward long-horizon tasks: transcribing hundreds of book pages, translating hours-long audio recordings, and the like. Yet these are precisely the tasks where current models fall short. Take OCR as an example—no existing model  \( [10, 30, 33, 34] \)  can even parse ten of pages in a single forward pass. Instead, they resort to page-by-page processing in a for-loop fashion, resetting memory at every step. This divergence is far from superficial, and it cannot be reduced to a mere lack of sufficient context. When humans perform such tasks, they maintain a continuous cognitive state in which distant outputs fade softly from memory, while nearby context is used to track progress. The for-loop paradigm, by contrast, erases memory entirely at each page, fragmenting a coherent long-horizon process into isolated short tasks managed by an external scheduler. It works to some extent, but it remains an engineering workaround, not a step toward AGI-purpose intelligence.
<|det|>text [112, 313, 885, 462]<|/det|>Consider the act of transcribing a document. As we copy each character, we do not scan the entire text already written; we simply glance at the immediately surrounding context to stay oriented. This everyday behavior points to an attention pattern fundamentally different from those in current models. It is not standard full attention—the full history is never fully consulted. Nor does it resemble linear attention, since visual/reference tokens undergo no recurrent state updates; such updates would progressively blur the visual features and degrade recognition accuracy. To align more closely with this natural attention flow, and to explore how multimodal large language models (MLLMs)  \( [8, 14, 22, 28] \)  can handle simple long-horizon parsing tasks, we propose Unlimited OCR. Our main contributions are as follows:
<|det|>text [143, 483, 884, 581]<|/det|>- We introduce Reference Sliding Window Attention (R-SWA), illustrated in Figure 1. For each token, R-SWA attends to all reference tokens—visual tokens and the prompt—while limiting output attention to the preceding n tokens (n defaults to 128). In this way, each token perceives the full image and autonomously tracks OCR progress through state transitions within the causal sliding window. This design keeps the KV cache constant during inference, alleviating memory pressure and reducing the computational cost.
<|det|>text [143, 581, 885, 678]<|/det|>- Building on R-SWA, we propose Unlimited OCR. Using DeepSeek OCR as our baseline, we retain its DeepEncoder with high image compression rate, modifying all the decoder LLM's attention mechanism to R-SWA. This enables Unlimited OCR to parse dozens of paper pages in a single forward pass. R-SWA also yields a modest improvement in general OCR accuracy. Specifically, Unlimited OCR achieves 93% on the OmniDocBench v1.5 benchmark [23], outperforming the DeepSeek OCR baseline by 6%.
<|det|>text [143, 678, 885, 759]<|/det|>- We conduct a preliminary validation of MLLM architectures with linear-complexity attention on OCR tasks, particularly in long-horizon scenarios. Rather than brute-force scaling up the training context, we identify an elegant approach that achieves long-horizon OCR. Looking ahead, we see promise in extending R-SWA to ASR, translation, and other reference-based tasks that demand long-horizon dependency modeling.
<|det|>list [143, 483, 885, 759]<|/det|>
<|det|>text [113, 780, 885, 860]<|/det|>In summary, we present R-SWA, which substantially reduces both the computational cost of attention and the memory footprint in the long-horizon inference. Building on R-SWA, Unlimited OCR not only enables one-shot parsing of an entire book, but also surpasses the DeepSeek OCR baseline by a large margin on popular document parsing benchmarks. Furthermore, we believe R-SWA holds promise well beyond OCR.
<|det|>page_number [493, 924, 506, 935]<|/det|>3
