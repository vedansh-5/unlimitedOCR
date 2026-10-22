# Usage: source env.sh
# Keeps uv, Python, packages, caches and model weights inside ./unlimitedOCRvenv.
# Remove everything with: rm -rf unlimitedOCRvenv

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]:-${(%):-%x}}")" && pwd)"
VENV_HOME="$ROOT/unlimitedOCRvenv"

export UV_PROJECT_ENVIRONMENT="$VENV_HOME/env"
export UV_PYTHON_INSTALL_DIR="$VENV_HOME/python"
export UV_CACHE_DIR="$VENV_HOME/cache/uv"
export UV_PYTHON_PREFERENCE=only-managed
export UV_NO_MODIFY_PATH=1
export HF_HOME="$VENV_HOME/hf"
export XDG_CACHE_HOME="$VENV_HOME/cache"
export PATH="$VENV_HOME/uv/bin:$PATH"
