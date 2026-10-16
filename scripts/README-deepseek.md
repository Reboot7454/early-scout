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
