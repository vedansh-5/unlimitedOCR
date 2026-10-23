from select_runs import choose


def test_choose_keeps_the_more_confident_run_per_page():
    confidence = {"A": {"p1": -0.1, "p2": -0.5}, "B": {"p1": -0.3, "p2": -0.2}}

    assert choose(confidence, ["A", "B"]) == {"p1": "A", "p2": "B"}


def test_choose_falls_back_to_the_first_run_when_confidence_is_missing():
    assert choose({"A": {"p1": -0.1}, "B": {}}, ["A", "B"]) == {"p1": "A"}
