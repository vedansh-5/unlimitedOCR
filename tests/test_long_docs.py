from long_docs import edit_distance, normalize


def test_normalize_drops_markup_and_layout_whitespace():
    assert normalize("## Title\n\n<table><tr><td>a</td></tr></table>  \\(x\\) **bold**") == "Title a x bold"


def test_edit_distance_ignores_formatting_only_differences():
    assert edit_distance("# Zero Trust\n\nArchitecture", "Zero Trust Architecture") == 0.0
    assert edit_distance("abcd", "abcf") == 0.25


def test_flag_pages_finds_missing_looping_cut_off_and_empty_pages():
    from long_docs import flag_pages

    good = "<|det|>text [1, 2, 3, 4]<|/det|>A normal paragraph of text."
    loop = "\n".join(f"<|det|>text [1, {i}, 3, 4]<|/det|>the same line" for i in range(8))
    raw = "<PAGE>".join(["", good, loop, "<|det|>text [1, 2, 3, 4]<|/det|>x", good])

    assert flag_pages(raw, 6, "stop") == {1: "loop", 2: "empty", 4: "missing", 5: "missing"}
    assert flag_pages(raw, 4, "length") == {1: "loop", 2: "empty", 3: "cut off"}


def test_splice_puts_retried_pages_back_in_order():
    from long_docs import splice

    assert splice(["a", "b"], 4, {1: "B", 3: "D"}) == ["a", "B", "", "D"]
