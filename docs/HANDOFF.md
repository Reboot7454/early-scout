# Early Scout 交接简报（换号续跑）

> 生成：2026-10-19（Asia/Shanghai）｜旧号 agent：小七｜当前库内轮次：**R238**｜候选约 **656**  
> 面板：https://reboot7454.github.io/early-scout/  
> 仓库：https://github.com/Reboot7454/early-scout （push `data.json` → `main`；本 box 曾以 **Reboot7454** `gh` 登录）

## 1. 目标与节奏

- 早期打新雷达：尽量早期为第一标准；七栏等量扫描（含 Tape/电路与 BTC），**禁止 Elysium / Tape / 单链偏科**。
- 例行：`@every 35m`（可灵活 ±10m）。用包内 `ROUTINE_PROMPT.txt` **原文**在新号建例行；**不要**恢复全量 X 账号时间线监控。
- 工作目录：`/workspace/early-scout/` 或已 clone 的 `early-scout-git`。开跑前必 `git pull`，避免盖掉另一号已推的更高轮次。
- 推送：只覆盖 `data.json`（及本轮必要 RESULT）到 `main`；Pages 跟 main。

## 2. 面板与栏位

宽屏七列：**打新｜挖矿｜台子/Meme｜GO盘｜LayerZero｜Elysium 生态｜Tape/电路**。

- **重点条**：搜索/筛选统计下方、七列**上方**横条（`focus:true` / `meta.focusIds`），**不是**看板列；常驻、与轮次无关。当前 focus 含 squeekchain / TapeAI / Ascend / Enter Elysium 等。Tape 与 Elysium 栏可重复展示各自 focus 卡。
- **收藏**：用户本机 `localStorage`，例行**勿改**。
- **zoneOf 互斥优先级**：`Elysium > tape > LayerZero > mining > go > meme > scout`。
- 轮次筛选芯片：只列库内实际有候选的轮次，勿造空轮芯片。

## 3. DeepSeek 优先（省用量）

- `DEEPSEEK_API_KEY`；模型 **`deepseek-flash`**；**思考模式保持开启**。
- 脚本：`scripts/deepseek_chat.py`、`ds_batch_score.py`。
- DS 覆盖：admit / score / 栏位归类草稿 / 亮点·缺点 / whatsNew / alertMessage / 一轮 summary / 候选去重。
- **Executor 只做**：拉信号（web / Trencher / OpenSea 等）、跑脚本、改 `data.json`、`gh` 推送、写 RESULT、notify 真假判定。
- 严禁高成本模型批量 admit/score；DS 失败才极短本地兜底并注明 `dsFallback`。

## 4. 监视清单（每轮同等努力）

| 主题 | meta / 要点 |
|------|-------------|
| 重点 / squeekchain | `@squeekchain` 及仓鼠/实体 PoW toychain、硬件矿机玩梗、未发币或测试网公平分配 → 有推特极早期可 `focus:true` |
| LayerZero | 自称 LZ/OFT/桥未核验 → `lzVerified=false` 进台子/Meme；明确 tags/chain 或 `lzVerified===true` 才进 LZ；armoreum、oftpad 保持台子/Meme |
| Elysium | 盯 `@Enter_Elysium`、AscendLaunch / Eloscape / Speculate / Montra / Aegis / kalos 等；对照 https://elysium.kinetiq.xyz/ecosystem ；仅 **On testnet** 或 **Announced 且写明 Elysium 部署** → `ecosystem:"Elysium"` + tag `Elysium生态`。Exploring/仅露名/只靠近 HL → 不进该栏。**硬排除勿回滚**：`perpme` / `branchpoint` / `outrive`（`meta.watches.elysiumKeepOut`） |
| TapeOut / 电路板 | 第七栏 Tape/电路。`meta.blonskrWatch` / `tapeOutWatch`：`@TapeAIAgent @Blonskr @TapeOutWorld @BEMGoGoGo @tapeupio @FirstoAI` 及同类电路/TapeOut 项目号；有独立项目推特且极早期才收；标签 `电路板`/`电路NFT`/`TapeOut`；**勿标 Elysium**。行情 tape 撞名不收。加栏不收缩其它栏 |
| X 链 pad | `meta.xChainPadWatch`：`@StarcatOKX`、`@NinetailsTrade` 及同类 → 台子/Meme |
| PaperBird | `meta.paperbirdWatch`：`@paperbird_lol` 及同类极早期鸟/meme → 台子/Meme 或打新 |
| BTC 隐私 | `meta.btcPrivacyWatch` / `watches.btcOrdinals`：`@ShieldedNaka`、`@banknotes_btc` 及同类隐私 Ordinals/CRC20；多进打新，挖矿玩法进挖矿；**禁止漏扫大饼链** |
| Discord alpha Peek | `meta.discordAlphaPeek`（commit `28b2a0e` 挂入例行）。Guild `1502958818865188956`；主频道 **#alpha-1** `1527862926885785710`（Spidey Bot / Twitter Follow Monitor，页脚常不标源）。辅助：`#alpha-1-backup`、`#smart-accounts-tracker`、`#alpha-3-new-accounts`。**只 Peek 补漏**（别人已扫到、我们漏了、仍极早期可操作）；有推特才收；tags 可 `discord-alpha`；更新 `lastSeen`。无桌面/浏览器 → RESULT `discordPeekDeferred=true`，父代理立刻 computerUse 补扫。**不是**全量 X 监控，也不是整频道入库 |

**软债**：每轮刷新 Canton / Glaze / TokenWorks 的 `lastChecked`（`cantonPadWatch` / `glazeWatch` / `tokenWorksPlaygroundWatch`），勿停在旧轮。

## 5. Peek / 潜力榜学习规则

- 只对照 NFT·新台·AI·极早期 DeFi/GameFi **找盲区**。
- **禁止**照搬热度榜；仍非全量 X 账号监控。

## 6. 数据规则

- `candidate.round` = **首次收录轮**（不变）。
- 「本轮新」只认 `newThisRound` / `roundNAdded`；先清上一轮 `newThisRound`，再写本轮。**`meta.newThisRound` 必须改成当前 `meta.round` 的 id 列表**（与 `meta.roundNAdded` 相同），不要留下上一轮 id。
- 新收录**必须有推特**。admit 时写 `links.x`（`https://x.com/<handle>` 或 `twitter.com`）。面板也认 `links.twitter` 里同样的主页 URL；只写 `links.twitter`、不写 `links.x` 时，旧面板会把卡片和该轮芯片一起滤掉。排期卡用同一条链接。
- 全覆盖七栏与各链（ETH/Base/Solana/Ink/RH/Injective/**BTC**/Canton/X链 等），含 GPU/PoW、fair-launch、AI 发射、GO/AR、Tape/电路等——**同等努力**。

## 7. 通知

- `notify=true`：真新收录，或 mint/open ≤2h（Asia/Shanghai），或推送失败 → DeepSeek 短中文 `alertMessage`（含面板链接）。
- 否则 `notify=false`，保持安静。
- RESULT 含 `discordPeekDeferred=true` → 父代理立刻补 Discord Peek，视情况再推/再通知。

## 8. 近期状态（交接时点）

- **R238**：Discord Peek 补漏 admit（inkfun / nicrofinance / raisedmoney / needles-on-ink / evmdotchat 等）；commit 线含 `1749b1b`（R238 admits）与 **`28b2a0e`**（`meta.discordAlphaPeek` 挂入例行）。
- `meta.updated` ≈ `2026-10-19 01:05 CST`；`lastScout` ≈ `2026-10-19 00:08 CST`。
- 下一轮：新号 `git pull` 后从 **R239** 起跑（以 pull 后 `meta.round` 为准）。

## 9. 新号落地

见同目录 `CHECKLIST.md`。例行 prompt 以 `ROUTINE_PROMPT.txt` 为准；本包另含交接时 `data.json` 快照与 `FEATURES.md`。

**换号注意**：旧号停 routine 后再让新号开跑，避免双写 main。
