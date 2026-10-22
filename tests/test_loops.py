from loops import broken_marker, is_loop, max_repeat

WALKING_LOOP = "\n".join(f"<|det|>text [875, {190 + 50 * i}, 902, {220 + 50 * i}]<|/det|>m = 3/11" for i in range(8))


def test_loop_that_walks_down_the_page_is_caught():
    assert max_repeat(WALKING_LOOP) == 8
    assert is_loop(WALKING_LOOP)


def test_normal_page_is_not_a_loop():
    raw = "<|det|>title [1, 2, 3, 4]<|/det|>Intro\n<|det|>text [1, 9, 3, 12]<|/det|>Some body text.\n<|det|>page_number [5, 6, 7, 8]<|/det|>10"

    assert not is_loop(raw)


def test_short_repeats_like_page_numbers_are_ignored():
    raw = "\n".join("<|det|>text [1, 2, 3, 4]<|/det|>10" for _ in range(9))

    assert not is_loop(raw)


def test_unclosed_marker_is_flagged():
    raw = "<|det|>text [1, 2, 3, 4]<|/det|>fine\n<|det|>text [768, 189,</td><td></td>"

    assert broken_marker(raw)
    assert is_loop(raw)


def test_content_tokens_drop_marker_spans():
    from loops import DET_CLOSE, DET_OPEN, content_tokens

    assert content_tokens([DET_OPEN, 7, 8, DET_CLOSE, 1, 2, DET_OPEN, 9]) == ([1, 2], True)


def test_content_guard_bans_a_repeat_that_only_changes_coordinates():
    from loops import DET_CLOSE, DET_OPEN, ContentNoRepeatGuard

    block = lambda y: [DET_OPEN, 5, y, DET_CLOSE, 40, 41, 42]
    sequence = block(190) + block(240) + [DET_OPEN, 5, 290, DET_CLOSE, 40, 41]
    guard = ContentNoRepeatGuard(ngram_size=3, window=64)

    assert guard.banned_tokens(sequence) == {42}
    assert guard.banned_tokens(block(190) + [DET_OPEN, 5, 240, DET_CLOSE]) == set()


def test_content_guard_keeps_logits_shape_and_masks_banned():
    import mlx.core as mx

    from loops import ContentNoRepeatGuard

    out = ContentNoRepeatGuard(ngram_size=2, window=8)(mx.array([5, 6, 5]), mx.zeros((1, 10)))

    assert out.shape == (1, 10)
    assert out[0, 6].item() == float("-inf")
    assert out[0, 7].item() == 0
