from loops import broken_marker, is_loop, max_repeat

WALKING_LOOP = "\n".join(f"<|det|>text [875, {190 + 50 * i}, 902, {220 + 50 * i}]<|/det|>m = 3/11" for i in range(8))


def test_loop_that_walks_down_the_page_is_caught():
    assert max_repeat(WALKING_LOOP) == 8
    assert is_loop(WALKING_LOOP)


def test_numbered_lines_are_not_a_loop():
    raw = "\n".join(f"<|det|>title [1, {i}, 3, 4]<|/det|>2.{i}.1" for i in range(9))

    assert not is_loop(raw)


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


def test_content_guard_bans_a_repeat_that_only_changes_its_numbers():
    from loops import ContentNoRepeatGuard

    guard = ContentNoRepeatGuard(ngram_size=4, window=64)
    guard.number_tokens = frozenset({22, 23, 24, 14843, 14844})
    # "(2354) x (2355) x (2356" with "235" and "4" as separate tokens, as the tokenizer writes it
    sequence = [10, 14843, 22, 11, 40, 10, 14843, 23, 11, 40, 10, 14843]

    assert guard.banned_tokens(sequence) == guard.number_tokens
    assert guard.banned_tokens(sequence[:-1] + [14844, 24, 11]) == {40}


def test_content_guard_keeps_numbers_exact_inside_table_rows():
    from loops import ROW_CLOSE, ROW_OPEN, ContentNoRepeatGuard

    guard = ContentNoRepeatGuard(ngram_size=4, window=64)
    guard.number_tokens = frozenset({736, 2012, 3661})
    row = lambda a, b: [ROW_OPEN, 128821, a, 16, b, 128822, ROW_CLOSE]

    assert guard.banned_tokens(row(736, 2012) + row(3661, 2012)[:3]) == set()


def test_content_guard_bans_runaway_cells_inside_unclosed_row():
    from loops import CELL_CLOSE, CELL_OPEN, ROW_OPEN, ContentNoRepeatGuard

    guard = ContentNoRepeatGuard(ngram_size=4, window=64)
    guard.number_tokens = frozenset(range(100, 200))
    # An unclosed row with 40 cells where only numbers increment
    seq = [ROW_OPEN]
    for i in range(100, 140):
        seq.extend([CELL_OPEN, i, CELL_CLOSE])

    # After MAX_ROW_CELLS (35 cells), numbers are normalized and repeats are banned
    assert guard.banned_tokens(seq + [CELL_OPEN]) == guard.number_tokens


def test_number_tokens_are_the_all_digit_ones():
    from loops import number_tokens

    assert number_tokens({"0": 18, "235": 14843, "x2": 5, "²": 6, "Ġ12": 7}) == {18, 14843}


def test_content_guard_keeps_logits_shape_and_masks_banned():
    import mlx.core as mx

    from loops import ContentNoRepeatGuard

    out = ContentNoRepeatGuard(ngram_size=2, window=8)(mx.array([5, 6, 5]), mx.zeros((1, 10)))

    assert out.shape == (1, 10)
    assert out[0, 6].item() == float("-inf")
    assert out[0, 7].item() == 0


def test_repeated_bounding_boxes_are_flagged_as_loop():
    raw = "\n".join("<|det|>image [510, 340, 510, 3]<|/det|>" for _ in range(5))
    assert is_loop(raw)

