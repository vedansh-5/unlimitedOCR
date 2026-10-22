import mlx.core as mx

import run_ocr
from unlimited_ocr_mlx import SlidingWindowNoRepeatNgramProcessor


def test_guard_keeps_batch_dim_of_logits():
    guard = SlidingWindowNoRepeatNgramProcessor(ngram_size=2, window=8)
    history = mx.array([5, 6, 5])
    logits = mx.zeros((1, 10))

    out = guard(history, logits)

    assert out.shape == (1, 10)
    assert out[0, 6].item() == float("-inf")
    assert out[0, 7].item() == 0
