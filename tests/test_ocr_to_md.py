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
