#!/usr/bin/env python3
"""Filter new Discord cards vs existing index, batch DeepSeek admit, write admits JSON."""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from deepseek_chat import chat

ZONE_MAP = {
    "Elysium": "Elysium",
    "LayerZero": "LayerZero",
    "挖矿": "挖矿",
    "GO盘": "GO盘",
    "台子/Meme": "台子/Meme",
    "打新": "打新",
}

SYS = """你是极早期加密打新雷达审核员。对 Discord New-follower 卡候选做 admit/拒收。
规则：必须有独立项目推特；跳过成熟KOL/高粉(>5k)/空壳/个人号/纯噪音；宁缺毋滥，只收极早期且有实际产品/发射/玩法/合约线索的项目。
六栏 category 必须是其一：打新｜挖矿｜台子/Meme｜GO盘｜LayerZero｜Elysium；优先级 Elysium>LayerZero>挖矿>GO盘>台子/Meme>打新。LZ 自称未核验→台子/Meme；lzVerified 仅真核验才 true。
tags 含 discord-alpha。输出严格 JSON 数组，每项字段：admit(bool), reason, id(kebab), name, handle(@x), category, chain, tags, lzVerified, focus, followers, scores{early,risk,novelty,actionable,overall}, highlights[], drawbacks[], whatsNew, summary, blurb, links{x}。
硬禁 focus：focus 默认必须 false。仅仓鼠/实体 PoW toychain（squeekchain 类）才可 focus:true；普通打新/挖矿/台子/Elysium 新卡一律 focus:false（重点条会把卡从栏位拿走）。
admit=false 也要给 id/handle/reason。不要 markdown 围栏。"""

def norm_handle(h):
    if not h: return ""
    h = str(h).strip()
    h = h.lstrip("@")
    h = h.split("/")[-1].split("?")[0]
    return h.lower()

def main():
    cards_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "DISCORD_ALPHA_40_ADMITS_latest.json"
    idx = json.loads((ROOT / "DISCORD_ALPHA_40_EXISTING_INDEX.json").read_text())
    ids = set(idx.get("ids") or [])
    handles = set(idx.get("handles") or [])
    cards = json.loads(cards_path.read_text())
    new_cards = cards.get("newCards") or []
    # dedupe by handle within batch; drop existing
    seen = set()
    cands = []
    pre_reject = []
    for c in new_cards:
        h = norm_handle(c.get("handle") or "")
        if not h:
            # try links
            for L in (c.get("links") or []):
                if "x.com/" in L or "twitter.com/" in L:
                    h = norm_handle(L)
                    break
        if not h:
            pre_reject.append({"handle": None, "reason": "no_handle"})
            continue
        if h in seen:
            continue
        seen.add(h)
        if h in handles or h.replace("_", "-") in ids or h.replace("_", "") in ids:
            pre_reject.append({"handle": "@"+h, "reason": "already_in_data"})
            continue
        # crude high-follower prefilter if present
        fol = c.get("followers")
        try:
            fol_n = int(fol) if fol is not None else None
        except Exception:
            fol_n = None
        if fol_n is not None and fol_n > 5000:
            pre_reject.append({"handle": "@"+h, "reason": f"high_followers_{fol_n}"})
            continue
        cands.append({**c, "handle": "@"+h})
    print(json.dumps({"raw": len(new_cards), "unique_new": len(cands), "pre_reject": len(pre_reject)}, ensure_ascii=False))
    if not cands:
        out_path.write_text("[]\n")
        (ROOT / "DISCORD_ALPHA_40_PRE_REJECT_latest.json").write_text(json.dumps(pre_reject, ensure_ascii=False, indent=2))
        return
    def parse_json_array(raw: str, batch_i: int):
        t = raw.strip()
        if t.startswith("```"):
            t = re.sub(r"^```(?:json)?\s*", "", t)
            t = re.sub(r"\s*```$", "", t)
        try:
            return json.loads(t)
        except Exception:
            pass
        m = re.search(r"\[.*\]", t, re.S)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                t = m.group(0)
        # salvage truncated array: keep complete objects
        if "[" in t:
            body = t[t.find("[") + 1 :]
            objs = []
            depth = 0
            start = None
            in_str = False
            esc = False
            for j, ch in enumerate(body):
                if in_str:
                    if esc:
                        esc = False
                    elif ch == "\\":
                        esc = True
                    elif ch == '"':
                        in_str = False
                    continue
                if ch == '"':
                    in_str = True
                    continue
                if ch == "{":
                    if depth == 0:
                        start = j
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0 and start is not None:
                        chunk = body[start : j + 1]
                        try:
                            objs.append(json.loads(chunk))
                        except Exception:
                            pass
                        start = None
            if objs:
                print(json.dumps({"batch": batch_i, "salvaged": len(objs)}, ensure_ascii=False), flush=True)
                return objs
        raise SystemExit(f"DS parse fail batch {batch_i}: {raw[:500]}")

    admits = []
    # batch ~10 to avoid truncated JSON with thinking+long fields
    B = 10
    for i in range(0, len(cands), B):
        batch = cands[i:i+B]
        # slim payload for DS
        slim = []
        for c in batch:
            slim.append({
                "handle": c.get("handle"),
                "name": c.get("name") or c.get("displayName") or "",
                "followers": c.get("followers"),
                "bio": (c.get("bio") or c.get("description") or "")[:280],
                "channel": c.get("channel"),
                "time": c.get("time") or c.get("cardTime"),
                "links": c.get("links") or [],
                "text": (c.get("text") or c.get("snippet") or "")[:400],
            })
        user = "审核下列候选，返回 JSON 数组（每项尽量精简字段，highlights/drawbacks 各最多2条，summary/blurb/whatsNew 各≤80字）：\n" + json.dumps(slim, ensure_ascii=False)
        text = chat(
            [{"role": "system", "content": SYS}, {"role": "user", "content": user}],
            model="deepseek-flash",
            temperature=0.2,
            max_tokens=8192,
            thinking=True,
        )
        part = parse_json_array(text, i)
        if isinstance(part, dict):
            part = part.get("admits") or part.get("items") or [part]
        admits.extend(part)
        print(json.dumps({"batch": i, "got": len(part), "admit_yes_so_far": sum(1 for a in admits if a.get("admit"))}, ensure_ascii=False), flush=True)
    out_path.write_text(json.dumps(admits, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "DISCORD_ALPHA_40_PRE_REJECT_latest.json").write_text(json.dumps(pre_reject, ensure_ascii=False, indent=2))
    n_yes = sum(1 for a in admits if a.get("admit"))
    print(json.dumps({"admits_file": str(out_path), "ds_total": len(admits), "admit_yes": n_yes, "pre_reject": len(pre_reject)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
