#!/usr/bin/env bash
#
# Usage:
#   bash scripts/start_py.sh
#   visit http://localhost:8000/healthz -> {"status":"ok"}

set -euo pipefail

# Change to the backend directory
cd "$(dirname "$0")/../backend"

# Activate Python virtual environment, if present.
if [ -f ../venv/bin/activate ]; then
  source ../venv/bin/activate
elif [ -f ../venv/Scripts/activate ]; then
  source ../venv/Scripts/activate
fi

# Start the Uvicorn server
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
