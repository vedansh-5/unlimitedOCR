import json
import sys
import time

import infer_mlx
import unlimited_ocr_mlx
from mlx_vlm import prompt_utils

_guard_call = unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor.__call__


def _guard_call_keeping_shape(self, input_ids, logits):
    # mlx-vlm 0.6.16 passes 1-D token ids with (1, vocab) logits; the port returned (vocab,).
    return _guard_call(self, input_ids, logits).reshape(logits.shape)


def strip_trailing_space(apply_chat_template):
    def apply(*args, **kwargs):
        return apply_chat_template(*args, **kwargs).rstrip(" ")

    return apply


def set_experts_per_token(model, k):
    from mlx_vlm.models.deepseekocr.language import MoEGate

    gates = [m for _, m in model.named_modules() if isinstance(m, MoEGate)]
    for gate in gates:
        gate.top_k = k
    return len(gates)


def with_number_tokens(load_model, guard):
    def load(*args, **kwargs):
        model, processor = load_model(*args, **kwargs)
        guard.number_tokens = number_tokens(getattr(processor, "tokenizer", processor).get_vocab())
        if not guard.number_tokens:
            raise RuntimeError("content guard: no number tokens found in the vocabulary")
        print(f"content guard: {len(guard.number_tokens)} number tokens", file=sys.stderr)
        return model, processor

    return load


def with_experts_per_token(load_model, k):
    def load(*args, **kwargs):
        model, processor = load_model(*args, **kwargs)
        print(f"experts per token: {k} in {set_experts_per_token(model, k)} MoE layers", file=sys.stderr)
        return model, processor

    return load


# The guard runs once per generated token, so it doubles as a clock for decode speed.
def with_speed_log(guard_class, path, every=500):
    class Timed(guard_class):
        steps = 0

        def __call__(self, input_ids, logits):
            self.steps += 1
            if self.steps == 1 or self.steps % every == 0:
                with open(path, "a") as f:
                    f.write(f"{self.steps}\t{time.perf_counter():.4f}\n")
            return super().__call__(input_ids, logits)

    return Timed


def set_memory_limit_gb(gb):
    import mlx.core as mx

    limit = int(gb * 1024**3)
    mx.set_memory_limit(limit)
    # Freed buffers are kept for reuse up to the cache limit; a small cache keeps the total near the limit.
    mx.set_cache_limit(256 * 1024**2)


# Runs an encoder over the batch a few images at a time, evaluating each group before the next,
# so only one group's activations are alive at once.
def chunked_call(call, size):
    def run(x, **kwargs):
        import mlx.core as mx

        if x.shape[0] <= size:
            return call(x, **kwargs)
        parts = []
        for i in range(0, x.shape[0], size):
            part = call(x[i : i + size], **{k: v[i : i + size] if v is not None else None for k, v in kwargs.items()})
            mx.eval(part)
            parts.append(part)
        return mx.concatenate(parts, axis=0)

    return run


def chunked_method(method, size):
    def call(self, x, *args, **kwargs):
        if args:
            return method(self, x, *args, **kwargs)
        return chunked_call(lambda y, **k: method(self, y, **k), size)(x, **kwargs)

    return call


# SAM's global-attention layers build a (heads, HW, HW) position bias; for the 1024 px
# global view that is 12 x 4096 x 4096. Same computation, a block of query rows at a time.
def row_chunked_attention(self, x, rows=1024):
    import mlx.core as mx
    from mlx_vlm.models.deepseekocr.sam import add_decomposed_rel_pos

    B, H, W, _ = x.shape
    qkv = self.qkv(x).reshape(B, H * W, 3, self.num_heads, -1).transpose(2, 0, 3, 1, 4)
    q, k, v = qkv.reshape(3, B * self.num_heads, H * W, -1)
    rel_h, rel_w = add_decomposed_rel_pos(q, self.rel_pos_h, self.rel_pos_w, (H, W), (H, W))
    q, k, v = (t.reshape(B, self.num_heads, H * W, -1) for t in (q, k, v))
    rel_h = rel_h.reshape(B, self.num_heads, H * W, H, 1)
    rel_w = rel_w.reshape(B, self.num_heads, H * W, 1, W)
    parts = []
    for i in range(0, H * W, rows):
        bias = (rel_h[:, :, i : i + rows] + rel_w[:, :, i : i + rows]).reshape(B, self.num_heads, -1, H * W)
        part = mx.fast.scaled_dot_product_attention(q[:, :, i : i + rows], k, v, scale=self.scale, mask=bias)
        mx.eval(part)
        parts.append(part)
    x = mx.concatenate(parts, axis=2)
    x = x.reshape(B, self.num_heads, H, W, -1).transpose(0, 2, 3, 1, 4).reshape(B, H, W, -1)
    return self.proj(x)


def chunk_sam_attention():
    from mlx_vlm.models.deepseekocr.sam import Attention

    original = Attention.__call__

    def call(self, x):
        if not self.use_rel_pos or x.shape[1] * x.shape[2] <= 1024:
            return original(self, x)
        return row_chunked_attention(self, x)

    Attention.__call__ = call


def with_chunked_vision(load_model, size):
    def load(*args, **kwargs):
        model, processor = load_model(*args, **kwargs)
        for encoder in (model.sam_model, model.vision_model):
            cls = type(encoder)
            cls.__call__ = chunked_method(cls.__call__, size)
        return model, processor

    return load


_confidence = {}


# Decoding is greedy, so the chosen token is the arg-max of the guarded logits.
def with_confidence_log(guard_class):
    class Confident(guard_class):
        def __call__(self, input_ids, logits):
            import mlx.core as mx

            out = super().__call__(input_ids, logits)
            chosen = mx.max(out, axis=-1) - mx.logsumexp(out, axis=-1)
            mx.async_eval(chosen)
            self.__dict__.setdefault("logprobs", []).append(chosen)
            _confidence["last"] = self
            return out

    return Confident


def confidence_summary(guard):
    values = sorted(float(v.reshape(-1)[0].item()) for v in getattr(guard, "logprobs", []))
    if not values:
        return {}
    return {
        "confidence_tokens": len(values),
        "mean_logprob": sum(values) / len(values),
        "p10_logprob": values[len(values) // 10],
    }


def with_confidence_in_metrics(write_result):
    def write(result, output):
        markdown_path, metadata_path = write_result(result, output)
        guard = _confidence.pop("last", None)
        if guard is not None:
            metrics = json.loads(metadata_path.read_text())
            metrics.update(confidence_summary(guard))
            metadata_path.write_text(json.dumps(metrics, indent=2) + "\n")
        return markdown_path, metadata_path

    return write


unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor.__call__ = _guard_call_keeping_shape

if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--content-guard" in argv:
        argv.remove("--content-guard")
        from loops import ContentNoRepeatGuard, number_tokens

        unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor = ContentNoRepeatGuard
        infer_mlx.load_model = with_number_tokens(infer_mlx.load_model, ContentNoRepeatGuard)
    if "--log-speed" in argv:
        i = argv.index("--log-speed")
        path = argv[i + 1]
        del argv[i : i + 2]
        unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor = with_speed_log(
            unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor, path
        )
    if "--memory-limit-gb" in argv:
        i = argv.index("--memory-limit-gb")
        set_memory_limit_gb(float(argv[i + 1]))
        del argv[i : i + 2]
        infer_mlx.load_model = with_chunked_vision(infer_mlx.load_model, 4)
        chunk_sam_attention()
    if "--log-confidence" in argv:
        argv.remove("--log-confidence")
        unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor = with_confidence_log(
            unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor
        )
        infer_mlx.write_result = with_confidence_in_metrics(infer_mlx.write_result)
    if "--experts-per-token" in argv:
        i = argv.index("--experts-per-token")
        k = int(argv[i + 1])
        del argv[i : i + 2]
        infer_mlx.load_model = with_experts_per_token(infer_mlx.load_model, k)
    if "--keep-prompt-space" in argv:
        argv.remove("--keep-prompt-space")
    else:
        # Baidu's infer() strips the formatted prompt; the mlx-vlm template leaves a trailing space.
        prompt_utils.apply_chat_template = strip_trailing_space(prompt_utils.apply_chat_template)
    raise SystemExit(infer_mlx.main(argv))
