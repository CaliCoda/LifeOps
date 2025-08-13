#!/usr/bin/env bash
set -euo pipefail
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT/backend"

# Install dependencies if not already installed
if [ ! -d "node_modules" ]; then
  echo "Installing backend dependencies..."
  npm install
fi

echo "Starting LifeOps backend on port ${PORT:-8000}..."
npm start