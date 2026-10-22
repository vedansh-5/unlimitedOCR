from run_ocr import strip_trailing_space


def test_strips_only_trailing_spaces():
    apply = strip_trailing_space(lambda *a, **k: "<image>document parsing. ")

    assert apply() == "<image>document parsing."


def test_leaves_prompt_without_trailing_space_alone():
    apply = strip_trailing_space(lambda *a, **k: "<image>Multi page parsing.")

    assert apply() == "<image>Multi page parsing."
