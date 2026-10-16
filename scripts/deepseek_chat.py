#!/usr/bin/env python3
"""Thin DeepSeek chat helper for early-scout enrichment.

Uses process.env.DEEPSEEK_API_KEY. Prefer deepseek-flash for bulk.
Default: thinking ENABLED. Never prints the API key.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.deepseek.com/chat/completions"
DEFAULT_MODEL = "deepseek-flash"


def chat(
    messages: list[dict],
    *,
    model: str | None = None,
    temperature: float = 0.3,
    max_tokens: int = 2048,
    thinking: bool = True,
) -> str:
    key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not key:
        raise SystemExit("DEEPSEEK_API_KEY is not set")
    body: dict = {
        "model": model or DEFAULT_MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "thinking": {"type": "enabled" if thinking else "disabled"},
    }
    req = urllib.request.Request(
        API,
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")[:500]
        raise SystemExit(f"DeepSeek HTTP {e.code}: {err}") from e
    msg = data["choices"][0]["message"]
    content = (msg.get("content") or "").strip()
    if not content and msg.get("reasoning_content"):
        # fallback if thinking spilled everything
        content = str(msg["reasoning_content"]).strip()
    return content


def main() -> None:
    raw = sys.stdin.read().strip()
    if not raw:
        raise SystemExit("empty stdin")
    if raw.startswith("{"):
        payload = json.loads(raw)
        messages = payload["messages"]
        text = chat(
            messages,
            model=payload.get("model"),
            temperature=float(payload.get("temperature", 0.3)),
            max_tokens=int(payload.get("max_tokens", 2048)),
            thinking=bool(payload.get("thinking", True)),
        )
    else:
        text = chat([{"role": "user", "content": raw}])
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
