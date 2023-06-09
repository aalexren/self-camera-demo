#!/bin/sh

set -e

cd db # && alembic upgrade head
cd ..
# Evaluating passed command:
exec "$@"
