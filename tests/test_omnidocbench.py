from collections import Counter

from omnidocbench import image_name, select


def page(kind, i):
    return {"page_info": {"image_path": f"{kind}_{i:03d}.png", "page_attribute": {"data_source": kind}}}


PAGES = [page("book", i) for i in range(30)] + [page("note", i) for i in range(30)] + [page("rare", i) for i in range(3)]


def test_select_takes_per_type_and_all_of_small_types():
    counts = Counter(p["page_info"]["page_attribute"]["data_source"] for p in select(PAGES, 5, 42))

    assert counts == {"book": 5, "note": 5, "rare": 3}


def test_select_is_reproducible_and_seed_dependent():
    names = lambda seed: [image_name(p) for p in select(PAGES, 5, seed)]

    assert names(42) == names(42)
    assert names(42) != names(7)


def test_select_skips_excluded_pages():
    taken = {image_name(p) for p in select(PAGES, 5, 42)}
    rest = select(PAGES, 5, 42, exclude=taken)

    assert not taken & {image_name(p) for p in rest}
    assert len(rest) == 10


def test_select_pages_picks_named_pages():
    from omnidocbench import select_pages

    chosen = select_pages(PAGES, ["book_002.png", "note_005.png"])
    assert [image_name(p) for p in chosen] == ["book_002.png", "note_005.png"]


def test_needs_retry_flags_loops_and_pages_cut_off_at_the_token_cap(tmp_path):
    import json

    from omnidocbench import needs_retry

    def page(name, text, finish):
        md = tmp_path / f"{name}.md"
        md.write_text(text)
        md.with_suffix(".json").write_text(json.dumps({"finish_reason": finish}))
        return md

    loop = "\n".join(f"<|det|>text [1, {i}, 3, 4]<|/det|>same line" for i in range(8))
    assert needs_retry(page("loop", loop, "stop"))
    assert needs_retry(page("capped", "<|det|>text [1, 2, 3, 4]<|/det|>varied text", "length"))
    assert needs_retry(page("whole_page_image", "<|det|>image [0, 0, 999, 999]<|/det|>", "stop"))
    assert not needs_retry(page("fine", "<|det|>text [1, 2, 3, 4]<|/det|>A normal paragraph of page text.", "stop"))


def test_counting_loops_are_cut_only_on_pages_at_the_token_cap(tmp_path):
    import json

    from omnidocbench import write_predictions

    sums = "\n".join(f"<|det|>equation [1, {i}, 3, 4]<|/det|>\\[ {i} \\div 6 = \\]" for i in range(30))
    meta = {"prompt_tokens": 1, "generation_tokens": 1, "elapsed_seconds": 1, "generation_tps": 1, "peak_memory_gb": 1, "complete": True}
    (tmp_path / "raw").mkdir()
    for name, finish in (("stopped", "stop"), ("capped", "length")):
        (tmp_path / "raw" / f"{name}.md").write_text(sums)
        (tmp_path / "raw" / f"{name}.json").write_text(json.dumps({**meta, "finish_reason": finish}))

    write_predictions(tmp_path, 0, cut_counting_loops=True)

    assert "29 \\div" in (tmp_path / "pred" / "stopped.md").read_text()
    assert "29 \\div" not in (tmp_path / "pred" / "capped.md").read_text()


def test_retry_identifies_empty_pages_for_base_mode(tmp_path):
    from ocr_to_md import to_markdown
    from omnidocbench import MIN_TEXT_CHARS

    empty_raw = "<|det|>image [0, 0, 999, 999]<|/det|>\n"
    valid_raw = "<|det|>title [1, 2, 3, 4]<|/det|>Actual slide title with sufficient content\n"

    assert len(to_markdown(empty_raw)) < MIN_TEXT_CHARS
    assert len(to_markdown(valid_raw)) >= MIN_TEXT_CHARS


def test_write_predictions_supports_split_merged_tables_and_cut_repeated_lines(tmp_path):
    import json

    from omnidocbench import write_predictions

    content = (
        "<|det|>table [1, 2, 3, 4]<|/det|>"
        "<table>"
        "<tr><td>H1</td><td>H2</td></tr>"
        "<tr><td>1</td><td>2</td></tr>"
        "<tr><td>H1</td><td>H2</td></tr>"
        "<tr><td>3</td><td>4</td></tr>"
        "</table>\n"
        "<|det|>text [5, 6, 7, 8]<|/det|>"
        + "\n".join(["[Non-Text]"] * 10)
    )
    meta = {"prompt_tokens": 1, "generation_tokens": 1, "elapsed_seconds": 1, "generation_tps": 1, "peak_memory_gb": 1, "finish_reason": "stop", "complete": True}
    (tmp_path / "raw").mkdir()
    (tmp_path / "raw" / "sample.md").write_text(content)
    (tmp_path / "raw" / "sample.json").write_text(json.dumps(meta))

    write_predictions(tmp_path, 0, split_merged_tables=True, cut_repeated_lines=True)
    pred_text = (tmp_path / "pred" / "sample.md").read_text()
    assert pred_text.count("[Non-Text]") == 2
    assert (tmp_path / "pages.csv").exists()

