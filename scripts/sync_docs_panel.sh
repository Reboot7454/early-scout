#!/usr/bin/env bash
# Sync root data.json → slim docs/data.json for GitHub Pages (main:/docs).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/docs"
python3 - "$ROOT" <<'PY'
import json, re, sys
from pathlib import Path
root = Path(sys.argv[1])
src = root / "data.json"
dst = root / "docs" / "data.json"
d = json.loads(src.read_text())
cands = d.get("candidates") or []
rounds = sorted({c.get("round") for c in cands if isinstance(c.get("round"), int)})
keep = set(rounds[-120:]) if rounds else set()
focus = set((d.get("meta") or {}).get("focusIds") or [])
slim = []
for c in cands:
    if c.get("round") in keep or c.get("id") in focus or c.get("focus") is True or c.get("newThisRound"):
        slim.append(c)
meta = dict(d.get("meta") or {})
r = meta.get("round") or (rounds[-1] if rounds else 0)

def round_num(k):
    m = re.match(r"round(\d+)Added$", k)
    return int(m.group(1)) if m else None

for k in list(meta):
    n = round_num(k)
    if n is not None and isinstance(r, int) and n < r - 30:
        meta.pop(k, None)
new = [c.get("id") for c in slim if c.get("newThisRound") and c.get("id")]
if new:
    meta["roundNAdded"] = new
    meta["newThisRound"] = new
    meta["round"] = r
docs = {"meta": meta, "candidates": slim}
for k, v in d.items():
    if k in ("meta", "candidates"):
        continue
    docs[k] = v
dst.write_text(json.dumps(docs, ensure_ascii=False, separators=(",", ":")))
print(
    f"synced slim docs/data.json cands={len(slim)} bytes={dst.stat().st_size} "
    f"round={meta.get('round')} added={meta.get('roundNAdded')}"
)
PY
for f in index.html app.js styles.css .nojekyll; do
  if [[ ! -f "$ROOT/docs/$f" && -f "$ROOT/$f" ]]; then
    cp -f "$ROOT/$f" "$ROOT/docs/$f"
  fi
done
