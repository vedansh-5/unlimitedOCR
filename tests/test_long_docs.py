from long_docs import edit_distance, normalize


def test_normalize_drops_markup_and_layout_whitespace():
    assert normalize("## Title\n\n<table><tr><td>a</td></tr></table>  \\(x\\) **bold**") == "Title a x bold"


def test_edit_distance_ignores_formatting_only_differences():
    assert edit_distance("# Zero Trust\n\nArchitecture", "Zero Trust Architecture") == 0.0
    assert edit_distance("abcd", "abcf") == 0.25
