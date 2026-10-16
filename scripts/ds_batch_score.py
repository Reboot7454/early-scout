#!/usr/bin/env python3
"""Batch admit/score/copy via DeepSeek — keeps SuperGrok off the heavy lifting.

stdin JSON:
  {
    "mode": "score" | "admit" | "alert",
    "items": [ {id,name,handle,chain,category,blurb,tags?} , ... ],
    "model"?: "deepseek-flash"
  }

stdout: JSON array or object from the model (parsed), or raw with --raw
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from deepseek_chat import chat  # noqa: E402

SYSTEM_SCORE = """你是早期打新雷达打分器。只输出合法 JSON 数组，不要 markdown。
每个元素字段：
id, name, category(打新|挖矿|台子/Meme|GO盘|LayerZero),
scores:{early,actionable,novelty,risk,overall 0-100整数},
highlights:[2-4条短中文], drawbacks:[2-4条短中文], whatsNew:一句中文,
zoneHint:同上五栏之一, admit:true/false, reason:一句。
规则：尽量早期优先；无推特不 admit；仅名字含 OFT/Omnichain 不算 LayerZero，需明确 LZ 生态才进 LayerZero。"""

SYSTEM_ADMIT = """你是早期收录筛选器。只输出 JSON：{"admit":[{id,reason}],"skip":[{id,reason}]}。
无推特 skip；已过热/无早期窗口 skip；极早期 mint/launch/fair-launch/挖矿/GO/LZ 可 admit。"""

SYSTEM_ALERT = """根据给定新增与可操作项，写一句短中文 alert（含面板链接占位 PANEL）。只输出 JSON：{"alertMessage":"..."}。"""


def extract_json(text: str):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"(\[.*\]|\{.*\})", text, re.S)
        if m:
            return json.loads(m.group(1))
        raise


def main() -> None:
    payload = json.load(sys.stdin)
    mode = payload.get("mode", "score")
    items = payload.get("items") or []
    model = payload.get("model") or "deepseek-flash"
    if mode == "score":
        system, user = SYSTEM_SCORE, json.dumps(items, ensure_ascii=False)
    elif mode == "admit":
        system, user = SYSTEM_ADMIT, json.dumps(items, ensure_ascii=False)
    elif mode == "alert":
        system, user = SYSTEM_ALERT, json.dumps(payload.get("context") or items, ensure_ascii=False)
    else:
        raise SystemExit(f"unknown mode {mode}")
    out = chat(
        [{"role": "system", "content": system}, {"role": "user", "content": user}],
        model=model,
        temperature=0.2,
        max_tokens=4096,
        # thinking defaults to enabled in deepseek_chat.chat
    )
    parsed = extract_json(out)
    json.dump(parsed, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
