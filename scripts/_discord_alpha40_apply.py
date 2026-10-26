#!/usr/bin/env python3
"""Apply Discord alpha-40 peek: clear prev NTR, optional admits, update meta, write RESULT."""
from __future__ import annotations
import json, sys, copy
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Asia/Shanghai")
ROOT = Path(__file__).resolve().parents[1]
PANEL = "https://reboot7454.github.io/early-scout/"

def now_cst() -> str:
    return datetime.now(TZ).strftime("%Y-%m-%d %H:%M CST")

def load(p):
    return json.loads(Path(p).read_text())

def main():
    cards_path = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "DISCORD_ALPHA_40_CARDS_20261026_2325.json")
    admits_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None  # optional DS admits JSON list
    data_path = ROOT / "data.json"
    d = load(data_path)
    cards = load(cards_path)
    meta = d.setdefault("meta", {})
    prev_round = int(meta.get("round") or 0)
    new_round = prev_round + 1
    checked = now_cst()

    # clear previous newThisRound
    prev_ntr = list(d.get("newThisRound") or meta.get("newThisRound") or [])
    flagged = [c.get("id") for c in d.get("candidates", []) if c.get("newThisRound")]
    for x in flagged:
        if x not in prev_ntr:
            prev_ntr.append(x)
    cleared = []
    for c in d.get("candidates", []):
        if c.get("newThisRound"):
            c["newThisRound"] = False
            cleared.append(c.get("id"))
    d["newThisRound"] = []
    meta["newThisRound"] = []

    new_cards = cards.get("newCards") or []
    admits = []
    if admits_path and admits_path.exists():
        admits = load(admits_path)
        if isinstance(admits, dict):
            admits = admits.get("admits") or admits.get("items") or []

    new_ids = []
    skipped = []
    # index existing
    existing_ids = {(c.get("id") or "").lower() for c in d.get("candidates", [])}
    existing_handles = set()
    for c in d.get("candidates", []):
        for k in ("handle", "twitter"):
            v = c.get(k)
            if v:
                existing_handles.add(str(v).lstrip("@").lower())
        x = (c.get("links") or {}).get("x") or ""
        if "x.com/" in x or "twitter.com/" in x:
            existing_handles.add(x.rstrip("/").split("/")[-1].split("?")[0].lower())

    for a in admits:
        if not a.get("admit", True):
            skipped.append({"id": a.get("id"), "reason": a.get("reason") or "ds_reject"})
            continue
        hid = (a.get("handle") or "").lstrip("@").lower()
        cid = (a.get("id") or hid.replace("_", "-")).lower()
        if not hid and not (a.get("links") or {}).get("x"):
            skipped.append({"id": cid, "reason": "no_twitter"})
            continue
        if cid in existing_ids or hid in existing_handles:
            skipped.append({"id": cid, "reason": "dup"})
            continue
        cand = {
            "id": cid,
            "name": a.get("name") or cid,
            "handle": "@" + hid if hid else a.get("handle"),
            "twitter": "@" + hid if hid else a.get("twitter"),
            "chain": a.get("chain") or "",
            "category": a.get("category") or "台子/Meme",
            "ecosystem": a.get("ecosystem") or "",
            "tags": list(dict.fromkeys((a.get("tags") or []) + ["discord-alpha"])),
            "links": a.get("links") or ({"x": f"https://x.com/{hid}"} if hid else {}),
            "scores": a.get("scores") or {},
            "highlights": a.get("highlights") or [],
            "drawbacks": a.get("drawbacks") or [],
            "whatsNew": a.get("whatsNew") or f"Discord alpha 补漏收录 @{hid}",
            "summary": a.get("summary") or a.get("blurb") or "",
            "blurb": a.get("blurb") or a.get("summary") or "",
            "round": new_round,
            "focus": bool(a.get("focus", False)),
            "lzVerified": bool(a.get("lzVerified", False)),
            "status": a.get("status") or "watching",
            "followers": a.get("followers"),
            "xFollowers": a.get("followers") or a.get("xFollowers"),
            "firstSeen": checked,
            "addedAt": checked,
            "lastChecked": checked,
            "zoneHint": a.get("zoneHint") or a.get("category") or "",
            "newThisRound": True,
        }
        if a.get("schedule"):
            cand["schedule"] = a["schedule"]
        d["candidates"].insert(0, cand)
        existing_ids.add(cid)
        if hid:
            existing_handles.add(hid)
        new_ids.append(cid)

    d["newThisRound"] = list(new_ids)
    meta["newThisRound"] = list(new_ids)
    meta["round"] = new_round
    meta["updated"] = checked
    d["updated"] = checked
    d["updatedAt"] = checked
    d["candidateCount"] = len(d["candidates"])
    key = f"round{new_round}Added"
    d[key] = list(new_ids)
    meta[key] = list(new_ids)

    newest = cards.get("newestVisibleTime") or meta.get("discordAlphaPeek", {}).get("lastSeen")
    last_seen = meta.get("discordAlphaPeek", {}).get("lastSeen") or "2026-10-26 13:03 CST"
    # advance lastSeen only if we saw newer cards (even if not admitted)
    if new_cards:
        times = [c.get("cardTimeCST") for c in new_cards if c.get("cardTimeCST")]
        if times:
            last_seen = max(times)
        elif newest:
            last_seen = newest
    # if no new cards, keep last_seen

    n_after = len(new_cards)
    note = (
        f"R{new_round}：Discord alpha 补漏"
        + (f"补收 {','.join(new_ids)}" if new_ids else "无新卡")
        + f"（#alpha-1 最新仍 {newest or last_seen}）"
        + (f"；清 {','.join(cleared)}" if cleared and not new_ids else (f"；清 {','.join(cleared)}" if cleared else ""))
        + f"；lastSeen {'→' if new_cards else '保持'} {last_seen}，lastChecked→{checked}"
    )
    if new_ids:
        note = (
            f"R{new_round}：Discord alpha 补收 {','.join(new_ids)}；"
            + (f"跳过 {skipped}；" if skipped else "")
            + (f"清 {','.join(cleared)}；" if cleared else "")
            + f"lastSeen→{last_seen}；lastChecked→{checked}"
        )
    elif cleared:
        note = (
            f"R{new_round}：Discord alpha 补漏无新卡（#alpha-1 最新仍 {newest or last_seen}）；"
            f"清 {','.join(cleared)}；lastSeen 保持 {last_seen}，lastChecked→{checked}"
        )
    else:
        note = (
            f"R{new_round}：Discord alpha 补漏无新卡（#alpha-1 最新仍 {newest or last_seen}）；"
            f"lastSeen 保持 {last_seen}，lastChecked→{checked}"
        )

    meta["discordAlphaPeek"] = {
        "deferred": False,
        "lastSeen": last_seen,
        "lastChecked": checked,
        "newestCardTime": newest or last_seen,
        "cardsAfterCutoff": n_after,
        "note": note,
        "lastRound": new_round,
    }
    d["alertMessage"] = ""
    d["lastScout"] = checked
    meta["lastScout"] = checked

    data_path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    result = {
        "round": new_round,
        "mode": "discord-alpha-40",
        "completedAt": checked,
        "timezone": "Asia/Shanghai",
        "notify": bool(new_ids),
        "notifyReason": "new_admits" if new_ids else "no_new_admits",
        "alertMessage": "",
        "newAdmits": new_ids,
        "newCount": len(new_ids),
        "newIds": new_ids,
        "skipped": skipped,
        "cardsAfterLastSeen": n_after,
        "clearedPrevNewThisRound": True,
        "prevNewThisRoundCleared": cleared,
        "candidateFlagsCleared": len(cleared),
        "topNewThisRoundCleared": cleared,
        "discordPeekDeferred": False,
        "dsFallback": False,
        "dsUsage": "none (0 newCards after cutoff; no admit/score)" if not admits else f"deepseek-flash admits={len(admits)}",
        "coverage": "discord-alpha #alpha-1 only",
        "discordAlphaPeek": meta["discordAlphaPeek"],
        "push": {"attempted": False, "ok": False},
        "panel": PANEL,
        "summary": note,
        "remoteVerified": False,
        "cardsFile": cards_path.name,
        "priorRoundNote": f"R{prev_round} meta NTR {prev_ntr}; cardsAfterCutoff={n_after}",
    }
    out = ROOT / f"ROUND{new_round}_RESULT.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    # also mirror timestamped
    ts = datetime.now(TZ).strftime("%Y%m%d_%H%M")
    (ROOT / f"DISCORD_ALPHA_40_RESULT_{ts}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"round": new_round, "newIds": new_ids, "cleared": cleared, "result": str(out), "summary": note}, ensure_ascii=False))

if __name__ == "__main__":
    main()
