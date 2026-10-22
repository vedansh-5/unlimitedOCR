import infer_mlx
import unlimited_ocr_mlx

_guard_call = unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor.__call__


def _guard_call_keeping_shape(self, input_ids, logits):
    # mlx-vlm 0.6.16 passes 1-D token ids with (1, vocab) logits; the port returned (vocab,).
    return _guard_call(self, input_ids, logits).reshape(logits.shape)


unlimited_ocr_mlx.SlidingWindowNoRepeatNgramProcessor.__call__ = _guard_call_keeping_shape

if __name__ == "__main__":
    raise SystemExit(infer_mlx.main())
