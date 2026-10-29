#!/usr/bin/env python3
"""Discord alpha-40: filter cards → DS admit batches → apply → patch lastSeenByChannel."""
from __future__ import annotations
import json, os, re, sys, time, urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Asia/Shanghai")
ROOT = Path("/workspace/early-scout")
GIT = Path("/workspace/early-scout-git")
PANEL = "https://reboot7454.github.io/early-scout/"
TS = datetime.now(TZ).strftime("%Y%m%d_%H%M")
HIGH_FOL = 3000  # pre-reject mature KOL

SYSTEM = """你是 Discord alpha Peek 早期收录筛选器（补漏，宁缺毋滥）。只输出合法 JSON，不要 markdown。
格式：{"decisions":[{所有字段见下}]}
每条卡必须有一条 decision，字段：
admit:true/false, reason:一句中文,
id:小写短横线slug（来自handle）, name, handle:@xxx, category:打新|挖矿|台子/Meme|GO盘|LayerZero|Elysium,
zone:频道名, chain:链名或空, tags:["discord-alpha"], lzVerified:false, focus:false（硬禁：默认 false；仅 squeek/仓鼠/实体PoW toychain 才可 true）, followers:数字,
scores:{early,risk,novelty,actionable,overall 0-10}, highlights:[], drawbacks:[], whatsNew, summary, blurb, links:{x:url}
规则：
- 必须有独立项目推特才 admit；无推特/个人号/KOL/空壳/新闻/喊单/成熟DeFi → admit:false
- 只收极早期且 bio/卡面有实际产品、发射、mint、挖矿、发射台、玩法线索的项目
- LZ 自称未核验 → category=台子/Meme, lzVerified=false
- Elysium：仅明确 On testnet / Announced 具体部署；仅关注 @Enter_Elysium 的猎人个人号一律拒；perpme/branchpoint/outrive 不进 Elysium
- 硬禁 focus：普通新卡 focus 必须 false（勿进重点条）；仅 squeekchain/仓鼠/实体 PoW toychain 才可 focus:true
- 高粉成熟 KOL 拒；follower 噪音大，宁缺毋滥
- overall≈early*0.35+actionable*0.25+novelty*0.2+(10-risk)*0.2（0-10 分制）
"""

def now_cst():
    return datetime.now(TZ).strftime("%Y-%m-%d %H:%M CST")

def slugify(handle: str) -> str:
    h = handle.lstrip("@").lower()
    return re.sub(r"[^a-z0-9]+", "-", h).strip("-") or "unknown"

def extract_json(text: str):
    text = (text or "").strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"(\{[\s\S]*\}|\[[\s\S]*\])", text)
        if m:
            return json.loads(m.group(1))
        raise

def existing_index(data):
    ids, handles = set(), set()
    for c in data.get("candidates") or []:
        ids.add((c.get("id") or "").lower())
        for k in ("handle", "twitter"):
            v = c.get(k)
            if v:
                handles.add(str(v).lstrip("@").lower())
        x = (c.get("links") or {}).get("x") or ""
        m = re.search(r"(?:x|twitter)\.com/([^/?#]+)", x, re.I)
        if m:
            handles.add(m.group(1).lower())
    return ids, handles

def ds_chat(messages, max_tokens=8192):
    key = os.environ["DEEPSEEK_API_KEY"]
    body = {
        "model": "deepseek-flash",
        "messages": messages,
        "temperature": 0.2,
        "max_tokens": max_tokens,
        "thinking": {"type": "enabled"},
    }
    req = urllib.request.Request(
        "https://api.deepseek.com/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read().decode())
    msg = data["choices"][0]["message"]
    content = (msg.get("content") or "").strip()
    reasoning = msg.get("reasoning_content") or ""
    if not content and reasoning:
        m = re.search(r"(\{\s*\"decisions\"[\s\S]*\})", reasoning)
        if m:
            content = m.group(1)
    return content, data.get("usage") or {}

def main():
    cards_path = Path(sys.argv[1])
    cards = json.loads(cards_path.read_text())
    if not cards.get("loginOk"):
        print(json.dumps({"ok": False, "reason": "loginOk false", "cards": str(cards_path)}))
        sys.exit(2)

    # Prefer git data.json (pulled)
    data_path = GIT / "data.json"
    if not data_path.exists():
        data_path = ROOT / "data.json"
    data = json.loads(data_path.read_text())
    # work on ROOT/data.json copy
    work = ROOT / "data.json"
    work.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

    ids, handles = existing_index(data)
    new_cards = cards.get("newCards") or []
    # dedupe by handle keep newest
    by_h = {}
    for c in new_cards:
        h = (c.get("handle") or "").lstrip("@").strip()
        if not h:
            continue
        by_h[h.lower()] = {**c, "handle": "@" + h.lstrip("@")}

    keep, pre_reject, already = [], [], []
    for h, c in by_h.items():
        if h in handles or slugify(h) in ids:
            already.append({"handle": c["handle"], "reason": "already_have"})
            continue
        fol = c.get("followers")
        if isinstance(fol, int) and fol >= HIGH_FOL:
            pre_reject.append({"handle": c["handle"], "reason": f"高粉({fol})个人/KOL"})
            continue
        # ensure links
        if not c.get("links"):
            c["links"] = [f"https://x.com/{h}"]
        keep.append(c)

    (ROOT / f"DISCORD_ALPHA_40_CANDS_{TS}.json").write_text(json.dumps(list(by_h.values()), ensure_ascii=False, indent=2) + "\n")
    (ROOT / f"DISCORD_ALPHA_40_CANDS_KEEP_{TS}.json").write_text(json.dumps(keep, ensure_ascii=False, indent=2) + "\n")
    (ROOT / f"DISCORD_ALPHA_40_PRE_REJECT_{TS}.json").write_text(json.dumps(pre_reject, ensure_ascii=False, indent=2) + "\n")
    print(f"cards={len(new_cards)} unique={len(by_h)} keep={len(keep)} pre_reject={len(pre_reject)} already={len(already)}", flush=True)

    decisions = []
    ds_usage = {"calls": 0, "prompt_tokens": 0, "completion_tokens": 0}
    BATCH = 9
    if keep:
        for i in range(0, len(keep), BATCH):
            batch = keep[i : i + BATCH]
            bi = i // BATCH
            (ROOT / f"DISCORD_ALPHA_40_BATCH_{bi}_{TS}.json").write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n")
            user = "对下列 New-follower 卡逐条判定（每条一条 decision）：\n" + json.dumps(batch, ensure_ascii=False)
            print(f"DS batch {bi} n={len(batch)}", flush=True)
            t0 = time.time()
            try:
                content, usage = ds_chat([
                    {"role": "system", "content": SYSTEM},
                    {"role": "user", "content": user},
                ])
            except Exception as e:
                print(f"DS ERROR batch {bi}: {e}", flush=True)
                (ROOT / f"DISCORD_ALPHA_40_DS_RAW_B{bi}_{TS}.txt").write_text(f"ERROR: {e}")
                continue
            (ROOT / f"DISCORD_ALPHA_40_DS_RAW_B{bi}_{TS}.txt").write_text(content or "")
            ds_usage["calls"] += 1
            ds_usage["prompt_tokens"] += usage.get("prompt_tokens") or 0
            ds_usage["completion_tokens"] += usage.get("completion_tokens") or 0
            if not content:
                print(f"EMPTY batch {bi} after {time.time()-t0:.1f}s", flush=True)
                continue
            try:
                parsed = extract_json(content)
            except Exception as e:
                print(f"PARSE FAIL batch {bi}: {e}", flush=True)
                continue
            decs = parsed.get("decisions") if isinstance(parsed, dict) else parsed
            if not isinstance(decs, list):
                print(f"BAD shape batch {bi}", flush=True)
                continue
            print(f"  got {len(decs)} decisions in {time.time()-t0:.1f}s", flush=True)
            decisions.extend(decs)

    (ROOT / f"DISCORD_ALPHA_40_DS_ADMIT_{TS}.json").write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + "\n")
    admits = [d for d in decisions if d.get("admit")]
    rejects = [{"handle": d.get("handle"), "reason": d.get("reason")} for d in decisions if not d.get("admit")]
    rejects.extend(pre_reject)
    (ROOT / f"DISCORD_ALPHA_40_ADMITS_ONLY_{TS}.json").write_text(json.dumps(admits, ensure_ascii=False, indent=2) + "\n")
    print(f"admits={len(admits)} ds_rejects={len(decisions)-len(admits)} pre_rejects={len(pre_reject)}", flush=True)

    # apply via existing script
    import subprocess
    cmd = ["python3", str(ROOT / "scripts/_discord_alpha40_apply.py"), str(cards_path)]
    if admits:
        cmd.append(str(ROOT / f"DISCORD_ALPHA_40_ADMITS_ONLY_{TS}.json"))
    out = subprocess.check_output(cmd, text=True)
    print("APPLY", out.strip(), flush=True)
    apply_info = json.loads(out)

    # patch lastSeenByChannel into data.json + RESULT
    d = json.loads(work.read_text())
    meta = d.setdefault("meta", {})
    peek = meta.setdefault("discordAlphaPeek", {})
    cutoffs = cards.get("lastSeenByChannelCutoff") or {}
    newest_by = cards.get("newestByChannel") or {}
    prev_by = (peek.get("lastSeenByChannel") or {}).copy()
    # start from previous or cutoffs
    by_ch = dict(prev_by) if prev_by else dict(cutoffs)
    for ch, t in newest_by.items():
        if not t:
            continue
        # advance only if newer than current
        cur = by_ch.get(ch) or ""
        # normalize compare as strings YYYY-MM-DD HH:MM
        t_norm = t.replace(" CST", "").strip()
        cur_norm = str(cur).replace(" CST", "").strip()
        if (not cur_norm) or (t_norm > cur_norm):
            # only advance if there were new cards in that channel OR newest > cutoff
            ch_cards = [c for c in new_cards if c.get("channel") == ch]
            if ch_cards:
                mx = max(c.get("cardTimeCST", "") for c in ch_cards)
                by_ch[ch] = mx
            elif t_norm > cur_norm:
                # no new after cutoff — keep prior lastSeen for channel
                pass
    # ensure all 4 keys
    for ch in ("alpha-3-new-accounts", "alpha-1-backup", "smart-accounts-tracker", "alpha-1"):
        by_ch.setdefault(ch, cutoffs.get(ch) or prev_by.get(ch) or peek.get("lastSeen") or "")
    peek["lastSeenByChannel"] = by_ch
    # global lastSeen = max of channel lastSeens / peek lastSeen
    times = [str(v).replace(" CST", "").strip() for v in by_ch.values() if v]
    if times:
        peek["lastSeen"] = max(times)
    meta["discordAlphaPeek"] = peek
    work.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    new_round = apply_info["round"]
    result_path = ROOT / f"ROUND{new_round}_RESULT.json"
    result = json.loads(result_path.read_text())
    result["lastSeenByChannel"] = by_ch
    result["discordAlphaPeek"]["lastSeenByChannel"] = by_ch
    result["discordAlphaPeek"]["lastSeen"] = peek["lastSeen"]
    result["cardsRead"] = len(new_cards)
    result["rejected"] = rejects
    result["rejectedCount"] = len(rejects)
    result["dsRejects"] = len(decisions) - len(admits)
    result["dsUsage"] = f"deepseek-flash admits={len(admits)}" if decisions else result.get("dsUsage")
    result["coverage"] = "discord-alpha multi-channel"
    result["admissions"] = [
        {"id": a.get("id"), "handle": a.get("handle"), "category": a.get("category"), "name": a.get("name")}
        for a in admits
    ]

    # alert if admits
    if admits:
        # build short alert via DS
        lines = []
        for a in admits:
            lines.append(f"{a.get('name') or a.get('id')}({a.get('handle')} {(a.get('blurb') or a.get('summary') or a.get('reason') or '')[:40]})")
        ctx = {
            "round": new_round,
            "admits": [{"name": a.get("name"), "handle": a.get("handle"), "category": a.get("category"), "blurb": a.get("blurb") or a.get("summary") or a.get("reason")} for a in admits],
            "panel": PANEL,
        }
        try:
            content, usage = ds_chat([
                {"role": "system", "content": '写一句短中文 alert。只输出 JSON：{"alertMessage":"DC补漏R{N}新收…；面板 URL"}。含面板完整链接。'},
                {"role": "user", "content": json.dumps(ctx, ensure_ascii=False)},
            ], max_tokens=512)
            ds_usage["calls"] += 1
            alert_obj = extract_json(content) if content else {}
            alert = (alert_obj.get("alertMessage") if isinstance(alert_obj, dict) else None) or (
                f"DC补漏R{new_round}新收{len(admits)}：" + "、".join(lines) + f"；面板 {PANEL}"
            )
        except Exception:
            alert = f"DC补漏R{new_round}新收{len(admits)}：" + "、".join(lines) + f"；面板 {PANEL}"
        result["notify"] = True
        result["notifyReason"] = "new_admits"
        result["alertMessage"] = alert
        result["alert"] = alert
        d["alertMessage"] = alert
        work.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    else:
        result["notify"] = False
        result["notifyReason"] = "no_new_admits"
        result["alertMessage"] = ""
        result["alert"] = ""

    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    (ROOT / f"DISCORD_ALPHA_40_RESULT_{TS}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "ok": True,
        "round": new_round,
        "notify": result["notify"],
        "newIds": result.get("newIds"),
        "alert": result.get("alertMessage"),
        "lastSeenByChannel": by_ch,
        "ds_usage": ds_usage,
        "result": str(result_path),
        "ts": TS,
    }, ensure_ascii=False), flush=True)

if __name__ == "__main__":
    main()
