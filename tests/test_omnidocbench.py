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
