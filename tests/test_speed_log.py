from run_ocr import with_speed_log


class Guard:
    def __call__(self, input_ids, logits):
        return logits


def test_speed_log_records_first_and_every_500th_token(tmp_path):
    log = tmp_path / "speed.tsv"
    timed = with_speed_log(Guard, log, every=500)
    guard = timed()
    for _ in range(1001):
        assert guard(None, "logits") == "logits"

    steps = [int(line.split("\t")[0]) for line in log.read_text().splitlines()]
    assert steps == [1, 500, 1000]
