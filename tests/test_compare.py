from compare import FULL_SET, interval, paired, reweighted


def test_full_set_counts_add_up_to_the_benchmark():
    assert sum(FULL_SET.values()) == 1651


def test_reweighted_uses_full_set_share_of_types_present():
    by_type = {"book": [0.1, 0.3], "historical_document": [0.9]}

    assert reweighted(by_type) == (276 * 0.2 + 5 * 0.9) / 281


def test_interval_brackets_the_estimate_and_is_repeatable():
    by_type = {"book": [0.0, 0.1, 0.2, 0.3], "note": [0.5, 0.6]}
    lo, hi = interval(reweighted, by_type)

    assert lo <= reweighted(by_type) <= hi
    assert (lo, hi) == interval(reweighted, by_type)


def test_paired_keeps_only_shared_pages():
    assert paired({"a": 0.5, "b": 0.2}, {"a": 0.25, "c": 0.9}) == {"a": -0.25}


def test_page_means_average_tables_within_a_page_first():
    from compare import page_means

    tables = {"a.png_[0]": 1.0, "a.png_[1]": 0.0, "a.png_[2]": 0.5, "b.png_[0]": 0.25}

    assert page_means(tables) == {"a.png": 0.5, "b.png": 0.25}
