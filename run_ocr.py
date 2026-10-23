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
