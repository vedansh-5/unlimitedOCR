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


def is_loop(raw, limit=MAX_REPEAT):
    return max_repeat(raw) >= limit or broken_marker(raw)


DET_OPEN, DET_CLOSE = 128818, 128819


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
    # so a repeat with new box coordinates still counts as a repeat.
    def __init__(self, ngram_size=35, window=128):
        self.ngram_size = ngram_size
        self.window = window

    def banned_tokens(self, sequence):
        from unlimited_ocr_mlx import _banned_tokens

        kept, inside = content_tokens(sequence)
        return set() if inside else _banned_tokens(kept, self.ngram_size, self.window, set())

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
