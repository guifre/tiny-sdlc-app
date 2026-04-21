#!/bin/sh
set -eu

SCRIPT_PATH="$0"
. "$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/common.sh"

OUTPUT_PATH="${OUTPUT_PATH:-${REPO_ROOT}/results.sarif}"

cd "${REPO_ROOT}"
checkov \
  --directory . \
  --framework kubernetes \
  --soft-fail \
  --output cli \
  --output sarif \
  --output-file-path "console,${OUTPUT_PATH}"
