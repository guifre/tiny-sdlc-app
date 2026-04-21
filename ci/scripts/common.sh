#!/bin/sh
set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "${SCRIPT_PATH:-$0}")" && pwd)"
REPO_ROOT="$(CDPATH= cd -- "${SCRIPT_DIR}/../.." && pwd)"
EXAMPLE_DIR="${EXAMPLE_DIR:-${REPO_ROOT}/examples/python-flask}"

case "${EXAMPLE_DIR}" in
  /*) ;;
  *) EXAMPLE_DIR="${REPO_ROOT}/${EXAMPLE_DIR}" ;;
esac
