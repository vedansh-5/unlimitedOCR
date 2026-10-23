import math

import mlx.core as mx

from run_ocr import confidence_summary, with_confidence_log


class Guard:
    def __call__(self, input_ids, logits):
        return logits


def test_confidence_records_log_probability_of_the_greedy_token():
    guard = with_confidence_log(Guard)()
    logits = mx.array([[0.0, math.log(3.0)]])
    guard(None, logits)
    guard(None, mx.array([[0.0, 0.0]]))

    summary = confidence_summary(guard)
    assert summary["confidence_tokens"] == 2
    assert abs(summary["mean_logprob"] - (math.log(0.75) + math.log(0.5)) / 2) < 1e-4


def test_confidence_summary_is_empty_without_tokens():
    assert confidence_summary(with_confidence_log(Guard)()) == {}
