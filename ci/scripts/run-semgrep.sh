#!/bin/sh
set -eu

SCRIPT_PATH="$0"
. "$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/common.sh"

OUTPUT_PATH="${OUTPUT_PATH:-${REPO_ROOT}/semgrep.sarif}"

cd "${REPO_ROOT}"
semgrep scan --config auto --sarif --output "${OUTPUT_PATH}"
