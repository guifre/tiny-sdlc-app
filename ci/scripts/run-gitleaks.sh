#!/bin/sh
set -eu

SCRIPT_PATH="$0"
. "$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/common.sh"

OUTPUT_PATH="${OUTPUT_PATH:-${REPO_ROOT}/gitleaks.sarif}"

cd "${REPO_ROOT}"
gitleaks detect --source . --report-format sarif --report-path "${OUTPUT_PATH}" --exit-code 0
