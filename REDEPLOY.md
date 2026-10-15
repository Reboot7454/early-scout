# Public URL & redeploy notes

Primary public URL (GitHub Pages, permanent):
https://reboot7454.github.io/early-scout/

Repo: https://github.com/Reboot7454/early-scout (branch `main`, root)

## Schema extras（data.json）

- `schedule` — 开售日程（confirmed/tentative/tba/live/ended + startsAt/phases/note）
- `onchain` — 链上合约盯盘（contract/mintStatus/supply/explorer）
- `highlights` / `drawbacks` / `whatsNew` / `scores` — 卡片亮点缺点与评分
- `meta.features` 含 `schedule`, `onchain`, `scores`, `highlights`

## On-chain probe

```bash
cd /workspace/early-scout
python3 scripts/check_onchain.py
```

无 API key；EVM 公共 RPC；失败软跳过。写回 `data.json` 并打印 JSON 摘要。

可选回填：

```bash
python3 scripts/extract_schedules.py
python3 scripts/enrich_cards.py
```

## ~10 min data.json updates (GitHub Pages)

After refreshing `/workspace/early-scout/data.json`（及静态文件若改过），同步到 `/workspace/early-scout-pages/`，再 push `data.json` + 静态文件到 `main` on `Reboot7454/early-scout`。Confirm:

- https://reboot7454.github.io/early-scout/ → 200
- https://reboot7454.github.io/early-scout/data.json → 200

Keep `URL.txt` as the github.io URL above.

## Fallback only (ZeroDeploy)

Use ZeroDeploy only if Pages push fails. Do not treat temporary ZeroDeploy drops as the primary panel.
