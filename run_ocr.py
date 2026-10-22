import sys

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


unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor.__call__ = _guard_call_keeping_shape

if __name__ == "__main__":
    argv = sys.argv[1:]
    if "--keep-prompt-space" in argv:
        argv.remove("--keep-prompt-space")
    else:
        # Baidu's infer() strips the formatted prompt; the mlx-vlm template leaves a trailing space.
        prompt_utils.apply_chat_template = strip_trailing_space(prompt_utils.apply_chat_template)
    raise SystemExit(infer_mlx.main(argv))
