from collections import Counter

from ocr_to_md import DET_RE

MAX_REPEAT = 6
MIN_CHARS = 3


def contents(raw):
    for line in raw.splitlines():
        m = DET_RE.match(line.strip())
        text = (m.group(2) if m else line).strip()
        if len(text) >= MIN_CHARS:
            yield text


def max_repeat(raw):
    return max(Counter(contents(raw)).values(), default=0)


def broken_marker(raw):
    return raw.count("<|det|>") != raw.count("<|/det|>")


def box_repeats(raw):
    import re

    boxes = [
        m.group(1)
        for line in raw.splitlines()
        if (m := re.search(r"<\|det\|>image\s*(\[[^\]]+\])<\|/det\|>", line.strip()))
    ]
    return max(Counter(boxes).values(), default=0) if boxes else 0


def is_loop(raw, limit=MAX_REPEAT):
    return max_repeat(raw) >= limit or broken_marker(raw) or box_repeats(raw) >= 4


DET_OPEN, DET_CLOSE = 128818, 128819
CELL_OPEN, CELL_CLOSE = 128821, 128822
ROW_OPEN, ROW_CLOSE = 128823, 128824
MAX_ROW_CELLS = 35
NUMBER = -1


def content_tokens(sequence):
    kept, inside = [], False
    for token in sequence:
        if token == DET_OPEN:
            inside = True
        elif token == DET_CLOSE:
            inside = False
        elif not inside:
            kept.append(token)
    return kept, inside


class ContentNoRepeatGuard:
    # Baidu's n-gram rule applied to the text with <|det|> type [box] <|/det|> spans removed,
    # so a repeat with new box coordinates still counts as a repeat. Outside table rows every
    # number token counts as the same token, so a block that repeats with a count going up is a
    # repeat too; inside a row numbers stay exact, since rows of figures share one shape.
    number_tokens = frozenset()

    def __init__(self, ngram_size=35, window=128):
        self.ngram_size = ngram_size
        self.window = window

    def banned_tokens(self, sequence):
        from unlimited_ocr_mlx import _banned_tokens

        kept, inside = content_tokens(sequence)
        if inside:
            return set()
        shape, in_row, cells = [], False, 0
        for token in kept:
            if token in (ROW_OPEN, ROW_CLOSE, DET_OPEN):
                in_row = token == ROW_OPEN
                cells = 0
            elif in_row and token == CELL_OPEN:
                cells += 1
                if cells > MAX_ROW_CELLS:
                    in_row = False
            shape.append(NUMBER if token in self.number_tokens and not in_row else token)
        banned = _banned_tokens(shape, self.ngram_size, self.window, set())
        if NUMBER in banned:
            banned = (banned - {NUMBER}) | self.number_tokens
        return banned

    def __call__(self, input_ids, logits):
        import mlx.core as mx

        rows = input_ids.tolist()
        rows = [rows] if input_ids.ndim == 1 else rows
        flat = logits.reshape(len(rows), -1)
        out = []
        for sequence, row in zip(rows, flat):
            banned = sorted(self.banned_tokens(sequence))
            if banned:
                mask = mx.zeros(row.shape, dtype=mx.bool_)
                mask[mx.array(banned)] = True
                row = mx.where(mask, mx.array(float("-inf"), dtype=row.dtype), row)
            out.append(row)
        return mx.stack(out).reshape(logits.shape)


def number_tokens(vocab):
    return frozenset(i for text, i in vocab.items() if text.isascii() and text.isdigit())
