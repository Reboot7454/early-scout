#!/usr/bin/env bash
# Copy root data.json → docs/data.json and ensure panel static files exist.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/docs"
cp -f "$ROOT/data.json" "$ROOT/docs/data.json"
for f in index.html app.js styles.css .nojekyll; do
  if [[ ! -f "$ROOT/docs/$f" && -f "$ROOT/$f" ]]; then
    cp -f "$ROOT/$f" "$ROOT/docs/$f"
  fi
done
echo "synced docs/data.json ($(wc -c < "$ROOT/docs/data.json") bytes)"
