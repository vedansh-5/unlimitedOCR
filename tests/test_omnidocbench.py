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
