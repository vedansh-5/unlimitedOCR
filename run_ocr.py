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
        from loops import ContentNoRepeatGuard

        unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor = ContentNoRepeatGuard
    if "--log-speed" in argv:
        i = argv.index("--log-speed")
        path = argv[i + 1]
        del argv[i : i + 2]
        unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor = with_speed_log(
            unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor, path
        )
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
