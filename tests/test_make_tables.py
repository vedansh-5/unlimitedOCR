from make_tables import by_bucket, interval_cell


def test_interval_cell_formats_value_and_bounds():
    assert interval_cell({"value": 0.03621, "ci95": [0.0243, 0.051]}, 3) == "0.036 [0.024, 0.051]"


def test_by_bucket_averages_documents_with_the_same_page_count():
    rows = [
        {"pages": "2", "edit_distance": "0.1", "distinct_20": "1.0", "distinct_35": "1.0", "gen_tokens": "400", "model_s": "10", "peak_mlx_gb": "8", "complete": "True"},
        {"pages": "2", "edit_distance": "0.3", "distinct_20": "0.9", "distinct_35": "0.95", "gen_tokens": "600", "model_s": "14", "peak_mlx_gb": "9", "complete": "False"},
    ]

    assert by_bucket(rows) == [{"pages": 2, "docs": 2, "edit_distance": 0.2, "distinct_20": 0.95, "distinct_35": 0.975,
                                "gen_tokens": 500, "model_s": 12.0, "peak_mlx_gb": 9.0, "incomplete": 1}]
