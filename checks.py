import re
import zlib
from collections import Counter

TABLE_RE = re.compile(r"<table>(.*?)</table>", re.DOTALL | re.IGNORECASE)
ROW_RE = re.compile(r"<tr[^>]*>(.*?)</tr>", re.DOTALL | re.IGNORECASE)
CELL_RE = re.compile(r"<t[dh]([^>]*)>", re.IGNORECASE)
SPAN_RE = re.compile(r'(colspan|rowspan)\s*=\s*"?(\d+)', re.IGNORECASE)


def max_repeated_line(text, min_len=10):
    lines = [line.strip() for line in text.splitlines() if len(line.strip()) >= min_len]
    return max(Counter(lines).values(), default=0)


def compression_ratio(text):
    data = text.encode("utf-8")
    return len(data) / len(zlib.compress(data)) if data else 0.0


# Paper section 5.1: unique n-grams / total n-grams. Tokens here are whitespace-separated words.
def distinct_n(text, n):
    words = text.split()
    grams = [tuple(words[i : i + n]) for i in range(len(words) - n + 1)]
    return len(set(grams)) / len(grams) if grams else 1.0


def table_row_widths(table_html):
    widths = []
    carried = Counter()
    for i, row in enumerate(ROW_RE.findall(table_html)):
        width = carried.pop(i, 0)
        for attrs in CELL_RE.findall(row):
            spans = {k.lower(): int(v) for k, v in SPAN_RE.findall(attrs)}
            colspan, rowspan = spans.get("colspan", 1), spans.get("rowspan", 1)
            width += colspan
            for later in range(i + 1, i + rowspan):
                carried[later] += colspan
        widths.append(width)
    return widths


def ragged_tables(text):
    return sum(len(set(table_row_widths(t))) > 1 for t in TABLE_RE.findall(text))


def empty_pages(pages, min_chars=20):
    return sum(len(page.strip()) < min_chars for page in pages)
