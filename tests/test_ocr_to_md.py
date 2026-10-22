from ocr_to_md import remove_det, split_pages, to_markdown

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
