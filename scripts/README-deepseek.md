# DeepSeek helpers for early-scout

Uses `DEEPSEEK_API_KEY`. Default model: `deepseek-flash`. **Thinking on** by default (`thinking: {type: enabled}`).

## Chat
```bash
echo '{"messages":[{"role":"user","content":"..."}],"model":"deepseek-flash"}' \
  | python3 scripts/deepseek_chat.py
```

Pass `"thinking": false` only if you explicitly want thinking off.

## Batch score / admit / alert
```bash
echo '{"mode":"score","items":[{"id":"...","name":"...","handle":"@x","chain":"Base","category":"台子/Meme","blurb":"..."}]}' \
  | python3 scripts/ds_batch_score.py
```
Modes: `score` | `admit` | `alert` (alert uses `context`).

Admit 写入 `data.json` 时：`links.x` 必填（`https://x.com/<handle>`，可同时抄一份到 `links.twitter`）。面板认这两个字段；缺 `links.x` 且只有 `links.twitter` 时，旧页面会藏掉卡片和该轮芯片。同时把 `meta.newThisRound` 改成当前 `meta.round` 的新 id（与 `roundNAdded` 一致），先清上一轮。
