#!/bin/bash

set -euo pipefail

cd src
exec uvicorn \
  --host 0.0.0.0 \
  --port 8001 \
  --no-access-log \
  --factory app.app:create_app
