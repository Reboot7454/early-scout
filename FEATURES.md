# Early Scout 面板功能说明（给父 agent）

静态站：`/workspace/early-scout/` → 发布镜像 `/workspace/early-scout-pages/`  
永久 URL：https://reboot7454.github.io/early-scout/  
风险声明：高风险 · 非投资建议 · DYOR

## 1) 开售日程（schedule）

- 候选可选字段 `schedule`：`status`（confirmed|tentative|tba|live|ended）、`startsAt`（ISO8601）、`phases[]`、`source`、`note`（中文）。
- **只在有证据时写入**；模糊文案用 `tentative` + note，不编造精确时刻。
- 面板：卡片日程 chip（今晚/倒计时/进行中/TBA）、顶栏「日程」最近约 8 条、筛选「即将开售（24h）/有日程」、排序「开售时间（近→远）」。
- 倒计时按 Asia/Shanghai 展示；每 30s 刷新标签。

## 2) 链上 mint 盯盘（onchain）

- 可选字段 `onchain`：`chainId`、`contract`、`standard`、`mintStatus`、`minted`/`totalSupply`/`maxSupply`、`explorer`、`lastCheckedAt`。
- 有合约或 OpenSea 时卡片显示状态行（未开 / 进行中 / x/y / 合约链接）。
- 脚本：`python3 scripts/check_onchain.py`  
  - 读 `data.json`，对 EVM（ethereum/base/ink/robinhood）用公共 RPC `eth_getCode` + `totalSupply()`。  
  - 无 API key；失败软跳过；打印 JSON 变更摘要。  
  - **Solana / 无稳定 RPC 的链会 skip**；Robinhood 公共 RPC 常不可用。

## 3) 亮点 / 缺点 / 本轮新 / 评分

- `highlights[]`、`drawbacks[]`：各 2–4 条短中文要点（具体机制/窗口/风险，避免空话）。
- `whatsNew`：本轮 `roundNAdded`（当前 round14）候选有「本轮新」徽章 + 一句说明。
- `scores`：`early` / `risk`（镜像 earlyScore/riskScore）、`novelty`、`actionable`、`overall`  
  - `overall = early*0.35 + actionable*0.25 + novelty*0.2 + (100-risk)*0.2`
- 面板：综合分大号 + 四条迷你条；亮点/缺点双列；排序「综合评分」。

## 维护脚本

| 脚本 | 用途 |
|------|------|
| `scripts/extract_schedules.py` | 日程/链上证据回填（幂等覆盖 schedule/onchain map） |
| `scripts/enrich_cards.py` | 全量亮点/缺点/whatsNew/scores |
| `scripts/check_onchain.py` | 公共 RPC 探测并写回 mint 状态 |

改完后：校验 JSON → 同步到 `early-scout-pages/` → 父 agent push `Reboot7454/early-scout` main。

## 4) 挖矿品类（GPU PoW / NFT 变异盘）

- 新品类 `category: "挖矿"`：GPU/PoW 币（PRL / QTC / NOID 风格）与 NFT 挖矿/变异盘。
- 可选字段 `miningType`：`gpu-pow` | `nft-mutation` | `nft-miner` | `other`；`tags` 含 `挖矿`/`PoW`/`变异盘`。
- 面板：品类 chip「挖矿」+ 顶栏「挖矿监控」筛选（同 LayerZero 监控逻辑）；卡片打「挖矿」徽章。
- 例行搜刮需同时扫：新 GPU 矿币、AI-PoW、NFT 变异盘 / Miner NFT 早期信号。
