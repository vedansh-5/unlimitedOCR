"""Run the OmniDocBench evaluator with each page's match kept on disk.

Matching is the slow part of scoring (minutes on some formula pages) and the evaluator keeps
no progress, so a stopped run starts over. Each page's match is stored under a hash of its
answer key, its prediction, the match settings and the evaluator's code; a re-run reuses it,
and a rescore only matches the pages whose Markdown changed.

Runs under the evaluator's Python, from the eval folder:
    python match_cache.py EVALUATOR CACHE_DIR --config config.yaml
"""
import hashlib
import json
import os
import pickle
import sys
from pathlib import Path

evaluator, cache = Path(sys.argv[1]), Path(sys.argv[2])
sys.path[0] = str(evaluator)

from src.cli import main  # noqa: E402
from src.core.preprocess import text_postprocess  # noqa: E402
from src.dataset.end2end_dataset import End2EndDataset  # noqa: E402

CODE = hashlib.sha256(b"".join(p.read_bytes() for p in sorted((evaluator / "src").rglob("*.py")))).hexdigest()
# Settings that change how a page is matched; the worker count only changes speed.
SETTINGS = ("match_method", "enable_timeout_match_fallback", "match_timeout_sec", "quick_match_truncated_timeout_sec")
match_page = End2EndDataset._match_single_page


def cached_match_page(self, index, sample, pred_folder):
    img_name = os.path.basename(sample["page_info"]["image_path"])
    pred_path = self._resolve_prediction_path(pred_folder, img_name)
    settings = {k: v for k, v in vars(self).items() if k in SETTINGS or k.startswith("timeout_fallback_")}
    key = hashlib.sha256()
    for part in (CODE, json.dumps(settings, sort_keys=True), json.dumps(sample, sort_keys=True)):
        key.update(part.encode() + b"\0")
    key.update(Path(pred_path).read_bytes() if pred_path else b"")
    path = cache / f"{key.hexdigest()}.pkl"
    if path.exists():
        saved = pickle.loads(path.read_bytes())
        for reason in saved["fallbacks"]:
            self._record_match_fallback(img_name, reason)
        return {"index": index, "img_name": img_name, "pred_path": pred_path, "result": saved["result"]}
    page = match_page(self, index, sample, pred_folder)
    with self._match_debug_lock:
        fallbacks = [r for r, pages in self.match_debug_info["text_match_fallback_pages"].items() if img_name in pages]
    tmp = path.with_suffix(f".{os.getpid()}.{index}.tmp")
    tmp.write_bytes(pickle.dumps({"img_name": img_name, "fallbacks": fallbacks, "result": page["result"]}))
    tmp.replace(path)
    return page


End2EndDataset._match_single_page = cached_match_page

# Each LaTeX-to-text conversion runs in a fresh process so a stuck one can be cut off. On macOS
# a fresh process costs about 2 s, and a page where the model repeated itself converts the same
# formulas thousands of times. Keep every result, and convert short formulas in place: they
# finish in milliseconds, so the cut-off never applies to them.
SHORT_LATEX = 200
latex_to_text = text_postprocess._latex_to_text_with_timeout
converted = {}


def cached_latex_to_text(latex, timeout=None):
    if (latex, timeout) in converted:
        return converted[latex, timeout]
    short = len(latex) <= SHORT_LATEX
    text = latex_to_text(latex, timeout=0 if short else timeout)
    # A long formula that failed may have hit the time limit, so it is tried again next time.
    if text is not None or short:
        converted[latex, timeout] = text
    return text


text_postprocess._latex_to_text_with_timeout = cached_latex_to_text

if __name__ == "__main__":
    cache.mkdir(parents=True, exist_ok=True)
    main(sys.argv[3:])
