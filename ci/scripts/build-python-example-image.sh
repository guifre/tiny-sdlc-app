#!/bin/sh
set -eu

SCRIPT_PATH="$0"
. "$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)/common.sh"

IMAGE_TAG="${IMAGE_TAG:-tiny-sdlc-app:ci}"
docker build -t "${IMAGE_TAG}" "${EXAMPLE_DIR}"
