# Early Scout 面板功能说明（给父 agent）

静态站：`/workspace/early-scout/` → 发布镜像 `/workspace/early-scout-pages/`  
永久 URL：https://reboot7454.github.io/early-scout/  
风险声明：高风险 · 非投资建议 · DYOR

## 1) 开售日程（schedule）

- 候选可选字段 `schedule`：`status`（confirmed|tentative|tba|live|ended）、`startsAt`（ISO8601）、`phases[]`、`source`、`note`（中文）。
- **只在有证据时写入**；模糊文案用 `tentative` + note，不编造精确时刻。
- 面板：卡片日程 chip（今晚/倒计时/进行中/TBA）、顶栏「日程」最多 12 条（主窗口 now−6h～now+72h；**台子/Meme/Launchpad 的 upcoming/confirmed/tentative ≤72h 保底入栏**；live 台子可回看至 24h 作余量）、筛选「即将开售（24h）/有日程」、排序「开售时间（近→远）」；点击开推特。
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
- `whatsNew`：续更说明文案；**仅** `newThisRound: true`（= 当前 `roundNAdded`）显示「本轮新」徽章，其余有文案时显示「续更」。
- `round`：首次收录轮次（discovery），例行续更**不得**改写成当前 round；轮次筛选靠此字段。
- 例行交接：新收录写 `newThisRound:true` + `flag:"本轮新"` + `meta.roundNAdded`；上一轮新收录清 `newThisRound`/`本轮新`，可留 whatsNew 续更句。
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
- 面板：宽屏（≥1280px）六列 `.board`，顺序 **重点 | 打新 | 挖矿 | 台子/Meme | GO盘 | LayerZero**；1280–1679 可横向滚动（列 min≈200px），≥1680 六列均分。窄屏纵向堆叠，顺序相同。
- 互斥归类（一条只进一列）：**重点最优先**（`focus: true` / `meta.focusIds` / tags 含 `重点`）→ LayerZero（显式 lz/layerzero tag 或 chain/文案）→ 挖矿 → GO盘 → 台子/Meme → 其余打新。重点项**只出现在重点栏**，不重复。
- 默认排序「最新信号」：有 `firstSeen` 或 `addedAt` 则新的在前，否则 `round` 降序；同轮 `whatsNew` 非空优先，再按 `scores.overall` / `earlyScore`。六列共用；下拉仍可改早期程度 / 综合 / 日程 / 风险 / 名称。
- 挖矿列保持紧凑 `.mining-row` + GPU PoW / NFT 变异 / Miner NFT / 其他。打新、台子/Meme、GO盘、LayerZero 用完整卡片。点品类「挖矿」或顶栏药丸跳到对应列；LayerZero 监控顶栏/芯片可跳 LayerZero 栏。
- 例行搜刮需同时扫：新 GPU 矿币、AI-PoW、NFT 变异盘 / Miner NFT 早期信号。

## 5) 重点栏（focus）

- 新列 **重点**（zone id `focus`），视觉强调（玫粉/琥珀描边 + 「重点」chip），**左起第一列**。
- 归入条件（任一即可，且优先于 LZ/挖矿等）：`focus: true` · `id ∈ meta.focusIds` · `tags` 含 `重点`。
- 种子：`squeekchain`（首位）· `hamster-hour`。例行可把清晰早期 peer 以 `focus: true` 收入，或至少打 `重点` tag 并记入 `meta.focusWatch`。
- `meta.focusWatch`：accounts + categoryScan + admitRule；**每轮例行扫描本类**（非整账号时间线监控）。

## 6) 例行扩展关注（非全量 X 监控）

- **TokenWorks Playground**：盯 `@Rhynotic`（兼 `@token_works`）与站 https://playground.token.works/ ——策展小组发射/分账台（ETH+Robinhood）；关注 `launchesEnabled`、首批想法（FWA 配对）、工厂公开部署。归台子/Meme，勿因跨链字样进 LayerZero。
- **实验玩具链 / 实体+链上（重点栏 standing watch）**：每轮扫同类信号——仓鼠/动物 PoW toychain、硬件矿机 novelty 链、实体物理装置上链验证、公平分配实验 L1/L2 且仍预发币/测试网。种子账号 `@squeekchain` `@squeektoshi` `@pillheadddd` `@hamsterhourgame`；同类有推特的清晰早期 peer → 重点栏（`squeekchain` 保持首位）。
- 此类为品类扩展监视，**不是**恢复全量 X 账号时间线监控。


## DeepSeek 省用量
- 例行打分/筛选/亮点缺点/whatsNew/alert → `deepseek-flash`（thinking 开启，勿强制关闭）。
- 脚本：`scripts/deepseek_chat.py`、`scripts/ds_batch_score.py`。
- 执行端只拉信号+推送，避免用 SuperGrok 做长推理。
