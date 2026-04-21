#!/bin/sh
set -eu

SCRIPT_PATH="$0"
. "$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/common.sh"

pip install -r "${EXAMPLE_DIR}/requirements.txt"
python -m py_compile "${EXAMPLE_DIR}/app.py"
