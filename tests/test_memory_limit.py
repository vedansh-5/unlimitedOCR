import mlx.core as mx

from run_ocr import set_memory_limit_gb


def test_memory_limit_sets_both_mlx_limits():
    before = mx.set_memory_limit(mx.device_info()["max_recommended_working_set_size"])
    try:
        set_memory_limit_gb(8)
        assert mx.set_memory_limit(before) == 8 * 1024**3
    finally:
        mx.set_cache_limit(mx.device_info()["memory_size"])


def test_chunked_call_matches_one_batch_and_splits_extra_inputs():
    from run_ocr import chunked_call

    seen = []

    def encoder(x, patch_embeds=None):
        seen.append(x.shape[0])
        return x * 2 + (0 if patch_embeds is None else patch_embeds)

    x = mx.arange(10 * 3).reshape(10, 3).astype(mx.float32)
    out = chunked_call(encoder, 4)(x, patch_embeds=x)

    assert seen == [4, 4, 2]
    assert mx.array_equal(out, x * 3)


def test_chunked_method_passes_positional_extras_through_unchunked():
    from run_ocr import chunked_method

    class Encoder:
        def __call__(self, x, extra=None):
            return x if extra is None else x + extra

    Encoder.__call__ = chunked_method(Encoder.__call__, 2)
    x = mx.ones((5, 2))

    assert mx.array_equal(Encoder()(x, x), x * 2)
    assert mx.array_equal(Encoder()(x, extra=x), x * 2)


def test_row_chunked_sam_attention_matches_the_original():
    from mlx_vlm.models.deepseekocr.sam import Attention

    from run_ocr import row_chunked_attention

    mx.random.seed(0)
    attn = Attention(64, num_heads=4, use_rel_pos=True, input_size=(16, 16))
    attn.rel_pos_h = mx.random.normal(attn.rel_pos_h.shape)
    attn.rel_pos_w = mx.random.normal(attn.rel_pos_w.shape)
    x = mx.random.normal((2, 16, 16, 64))

    expected = attn(x)
    got = row_chunked_attention(attn, x, rows=48)

    assert got.shape == expected.shape
    assert mx.allclose(got, expected, atol=1e-5)
