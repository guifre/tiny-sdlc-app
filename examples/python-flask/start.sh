#!/bin/sh
set -eu

python -c "from app import init_db; init_db()"
exec gunicorn --bind 0.0.0.0:${PORT:-5000} app:app
