from ocr_to_md import cut_counting_loops, remove_det, split_pages, to_markdown

RAW = """<|det|>title [115, 101, 212, 117]<|/det|>Contents
<|det|>text [112, 215, 886, 378]<|/det|>First line
second line of the same block
<|det|>image [167, 601, 825, 804]<|/det|>
<|det|>page_number [489, 923, 511, 936]<|/det|>10"""


def test_remove_det_groups_blocks_and_drops_images():
    assert remove_det(RAW) == "Contents\n\nFirst line\nsecond line of the same block\n\n10"


def test_text_before_first_marker_is_kept():
    assert remove_det("5.3. Study\n<|det|>text [1, 2, 3, 4]<|/det|>Body") == "5.3. Study\n\nBody"


def test_page_separator_does_not_leak_markers():
    raw = "<|det|>text [1, 2, 3, 4]<|/det|>Page one\n<PAGE><|det|>title [1, 2, 3, 4]<|/det|>Page two"

    assert to_markdown(raw) == "Page one\n\nPage two"


def test_leading_page_separator_does_not_create_an_empty_page():
    assert split_pages("<PAGE>one\n<PAGE>two") == ["one\n", "two"]


BROKEN = "<|det|>text [1, 2, 3, 4]<|/det|>fine\n<|det|>text [768, 189,</td><td></td>\nmore <|det|>title [5, 6"


def test_unclosed_markers_leak_without_repair():
    assert "<|det|>" in to_markdown(BROKEN)


def test_repair_cuts_unclosed_markers():
    assert to_markdown(BROKEN, repair=True) == "fine\nmore"


def test_remove_det_can_drop_page_furniture():
    from ocr_to_md import PAGE_FURNITURE, remove_det

    raw = "<|det|>header [1, 2, 3, 4]<|/det|>Journal 12\n<|det|>text [1, 9, 3, 12]<|/det|>Body.\n<|det|>page_number [5, 6, 7, 8]<|/det|>10"

    assert remove_det(raw) == "Journal 12\n\nBody.\n\n10"
    assert remove_det(raw, skip=PAGE_FURNITURE) == "Body."


COUNTING_LOOP = "<|det|>text [1, 2, 3, 4]<|/det|>" + " ".join(f"( {i} ) item" for i in range(20))


def test_counting_loops_leak_without_cut():
    assert "( 19 ) item" in to_markdown(COUNTING_LOOP)


def test_cut_counting_loops_keeps_first_repeats():
    md = to_markdown(COUNTING_LOOP, cut_loops=True)
    assert "( 0 ) item" in md
    assert "( 19 ) item" not in md


RUNAWAY_TABLE = "<|det|>table [1, 2, 3, 4]<|/det|><table>" + "".join("<tr><td></td><td></td></tr>" for _ in range(50))


def test_runaway_empty_tables_leak_without_cut():
    assert "<tr><td></td><td></td></tr>" * 10 in to_markdown(RUNAWAY_TABLE)


def test_cut_empty_tables_removes_runaway():
    md = to_markdown(RUNAWAY_TABLE, cut_tables=True)
    assert "<tr><td></td><td></td></tr>" * 10 not in md


def test_cut_counting_loops_keeps_whole_copies_only():
    cell = "; ".join(f"{i // 10 + 1}.{i % 10 + 1}" for i in range(30)) + "</td>"

    assert cut_counting_loops(cell) == "1.1; 1.2; 1.3; </td>"


def test_cut_counting_loops_leaves_table_rows():
    rows = "".join(f"<tr><td>{i}</td><td>{2 * i}</td></tr>" for i in range(30))

    assert cut_counting_loops(rows) == rows


def test_cut_counting_loops_needs_many_copies_of_a_line_with_no_number():
    lines = "\n\n".join(["Provincial Government"] * 12)

    assert cut_counting_loops(lines) == lines
    assert cut_counting_loops("\n\n".join(["Provincial Government"] * 60)).count("Government") < 5


def test_cut_consecutive_repeats_truncates_non_text_placeholders():
    from ocr_to_md import cut_consecutive_repeats

    text = "\n".join(["[Non-Text]"] * 10)
    res = cut_consecutive_repeats(text)
    assert res.count("[Non-Text]") == 2


def test_cut_consecutive_repeats_truncates_single_char_spams():
    from ocr_to_md import cut_consecutive_repeats

    text = "\n".join(["B"] * 40)
    res = cut_consecutive_repeats(text)
    assert res.count("B") == 1


def test_cut_consecutive_repeats_preserves_normal_lines():
    from ocr_to_md import cut_consecutive_repeats

    text = "First paragraph\n\nSecond paragraph\n\nThird paragraph"
    assert cut_consecutive_repeats(text) == text


def test_split_merged_tables_splits_stacked_tables():
    from ocr_to_md import split_merged_tables

    tbl = (
        "<table>"
        "<tr><td>Year</td><td>Revenue</td><td>Profit</td></tr>"
        "<tr><td>2021</td><td>100</td><td>10</td></tr>"
        "<tr><td>2022</td><td>120</td><td>15</td></tr>"
        "<tr><td>2023</td><td>150</td><td>20</td></tr>"
        "<tr><td colspan=\"3\">Cash Flow</td></tr>"
        "<tr><td>Year</td><td>Operating</td><td>Investing</td></tr>"
        "<tr><td>2021</td><td>50</td><td>-20</td></tr>"
        "<tr><td>2022</td><td>60</td><td>-25</td></tr>"
        "<tr><td>2023</td><td>70</td><td>-30</td></tr>"
        "</table>"
    )
    res = split_merged_tables(tbl)
    assert res.count("<table>") == 2
    assert "Cash Flow" in res


def test_split_merged_tables_leaves_normal_table():
    from ocr_to_md import split_merged_tables

    tbl = (
        "<table>"
        "<tr><td>Year</td><td>Revenue</td><td>Profit</td></tr>"
        "<tr><td>2021</td><td>100</td><td>10</td></tr>"
        "<tr><td>2022</td><td>120</td><td>15</td></tr>"
        "<tr><td>2023</td><td>150</td><td>20</td></tr>"
        "</table>"
    )
    assert split_merged_tables(tbl) == tbl


def test_unwrap_single_row_tables_removes_false_table():
    """1-row table with a short code cell and a long prose cell is unwrapped."""
    from ocr_to_md import unwrap_single_row_tables

    prose = "Anti-HIV-1 Activity of Pyrryl Aryl Sulfone (PAS) Derivatives: Synthesis and SAR Studies of Novel Esters and Amides at the Position 2 of the Pyrrole Nucleus."
    tbl = f"<table><tr><td>R 0120</td><td>{prose}</td></tr></table>"
    result = unwrap_single_row_tables(tbl)
    assert "<table>" not in result
    assert prose in result
    assert "R 0120" in result


def test_unwrap_single_row_tables_leaves_short_cell_table():
    """1-row table whose every cell is short (real key-value table) is NOT unwrapped."""
    from ocr_to_md import unwrap_single_row_tables

    tbl = "<table><tr><td>Name</td><td>Value</td></tr></table>"
    assert unwrap_single_row_tables(tbl) == tbl


def test_unwrap_single_row_tables_leaves_multirow_table():
    """Multi-row table with a prose-like cell is NOT unwrapped."""
    from ocr_to_md import unwrap_single_row_tables

    prose = "Anti-HIV-1 Activity of Pyrryl Aryl Sulfone derivatives with long description text here."
    tbl = (
        "<table>"
        f"<tr><td>R 0120</td><td>{prose}</td></tr>"
        "<tr><td>R 0121</td><td>Another entry with enough characters to be considered prose content here.</td></tr>"
        "<tr><td>R 0122</td><td>Yet another bibliographic entry about some chemical compounds studied.</td></tr>"
        "</table>"
    )
    assert unwrap_single_row_tables(tbl) == tbl
