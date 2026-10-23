#!/bin/sh
# Usage: ./quantize.sh 8   (or 4). Writes unlimitedOCRvenv/models/unlimited-ocr-<bits>bit.
# The vision encoders stay in bf16; mlx-vlm's default rule quantizes the decoder and projector.
set -eu
cd "$(dirname "$0")"
. ./env.sh
BITS="$1"
OUT="$VENV_HOME/models/unlimited-ocr-${BITS}bit"
[ -d "$OUT" ] && { echo "$OUT exists"; exit 0; }
uv run mlx_vlm.convert --hf-path baidu/Unlimited-OCR --revision 07dea832e22aefee32ad281d4b80551282e1c168 \
  --mlx-path "$OUT" -q --q-bits "$BITS" --q-group-size 64
