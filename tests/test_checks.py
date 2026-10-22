from checks import compression_ratio, distinct_n, empty_pages, max_repeated_line, ragged_tables, strip_tags, table_row_widths


def test_max_repeated_line_ignores_short_lines():
    text = "a looping sentence here\n" * 5 + "ok\n" * 9 + "something else entirely"

    assert max_repeated_line(text) == 5


def test_loop_compresses_better_than_prose():
    loop = "the same line again and again " * 40
    prose = " ".join(f"word{i}" for i in range(240))

    assert compression_ratio(loop) > 3 * compression_ratio(prose)


def test_distinct_n():
    assert distinct_n("a b c d", 2) == 1.0
    assert distinct_n("a b a b a b", 2) == 2 / 5
    assert distinct_n("short", 20) == 1.0


def test_row_widths_count_rowspan_and_colspan():
    table = (
        '<tr><td rowspan="2">M</td><td>x</td><td>y</td></tr>'
        "<tr><td>x</td><td>y</td></tr>"
        '<tr><td colspan="3">all</td></tr>'
    )

    assert table_row_widths(table) == [3, 3, 3]


def test_ragged_table_is_flagged():
    good = "<table><tr><td>a</td><td>b</td></tr><tr><td>c</td><td>d</td></tr></table>"
    bad = "<table><tr><td>a</td><td>b</td></tr><tr><td>c</td></tr></table>"

    assert ragged_tables(good + bad) == 1


def test_empty_pages():
    assert empty_pages(["a real page of text here", "", " 10 "]) == 2


def test_sparse_table_is_not_mistaken_for_a_loop_once_tags_are_stripped():
    rows = "".join(f"<tr><td>{i}</td>" + "<td></td>" * 12 + "</tr>" for i in range(60))
    table = f"<table>{rows}</table>"

    assert compression_ratio(table) > 6
    assert compression_ratio(strip_tags(table)) < 4
