from types import SimpleNamespace

import mlx.nn as nn
from mlx_vlm.models.deepseekocr.language import MoEGate

from run_ocr import set_experts_per_token

CONFIG = SimpleNamespace(scoring_func="softmax", num_experts_per_tok=6, n_routed_experts=8, routed_scaling_factor=1.0,
                         topk_method="greedy", n_group=1, topk_group=1, hidden_size=4)


def test_set_experts_per_token_changes_every_gate():
    model = nn.Module()
    model.layers = [MoEGate(CONFIG), nn.Linear(4, 4), MoEGate(CONFIG)]

    assert set_experts_per_token(model, 4) == 2
    assert [g.top_k for g in model.layers if isinstance(g, MoEGate)] == [4, 4]
