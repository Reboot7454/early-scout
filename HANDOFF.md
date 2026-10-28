# Early Scout 交接简报（换号续跑）

> 生成：2026-10-19（Asia/Shanghai）｜旧号 agent：小七｜当前库内轮次：**R238**｜候选约 **656**  
> 面板：https://reboot7454.github.io/early-scout/  
> 仓库：https://github.com/Reboot7454/early-scout （push `data.json` → `main`；本 box 曾以 **Reboot7454** `gh` 登录）

## 1. 目标与节奏

- 早期打新雷达：尽量早期为第一标准；六栏等量扫描，**禁止 Elysium / 单链偏科**。
- 例行：`@every 35m`（可灵活 ±10m）。用包内 `ROUTINE_PROMPT.txt` **原文**在新号建例行；**不要**恢复全量 X 账号时间线监控。
- 工作目录：`/workspace/early-scout/` 或已 clone 的 `early-scout-git`。开跑前必 `git pull`，避免盖掉另一号已推的更高轮次。
- 推送：只覆盖 `data.json`（及本轮必要 RESULT）到 `main`；Pages 跟 main。

## 2. 面板与栏位

宽屏六列（2026-10-18）：**打新｜挖矿｜台子/Meme｜GO盘｜LayerZero｜Elysium 生态**。

- **硬禁 focus（2026-10-23）**：普通新收录禁止 `focus:true`。台子/打新等栏会排除 focus 卡，误标会导致本轮新看不见。仅 `meta.focusIds` 或仓鼠/实体 PoW toychain（squeekchain 类）可 focus；其它新卡 `focus:false` 或不写。
- **重点条**：搜索/筛选统计下方、六列**上方**横条（`focus:true` / `meta.focusIds`），**不是**左侧第六列；常驻、与轮次无关。当前 focus 含 squeekchain / TapeAI / Ascend / Enter Elysium 等。
- **收藏**：用户本机 `localStorage`，例行**勿改**。
- **zoneOf 互斥优先级**：`Elysium > LayerZero > mining > go > meme > scout`。
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
| TapeOut / 电路板 | `meta.blonskrWatch` / `tapeOutWatch`：`@TapeAIAgent @Blonskr @TapeOutWorld @BEMGoGoGo @tapeupio @FirstoAI`；有独立项目推特且极早期才收；标签 `电路板`/`电路NFT`/`TapeOut`；**勿标 Elysium** |
| X 链 pad | `meta.xChainPadWatch`：`@StarcatOKX`、`@NinetailsTrade` 及同类 → 台子/Meme |
| PaperBird | `meta.paperbirdWatch`：`@paperbird_lol` 及同类极早期鸟/meme → 台子/Meme 或打新 |
| Starknet/史塔克 | `meta.starknetWatch`：用户点名须覆盖；样例 `@Bramble_fi`；扫 `@Starknet` 官推点名与同类极早期隐私/DeFi/打新；**禁止漏史塔克链**（全覆盖不偏科） |
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
- 全覆盖六栏与各链（ETH/Base/Solana/Ink/RH/Injective/**BTC**/Canton/X链 等），含 GPU/PoW、fair-launch、AI 发射、GO/AR 等——**同等努力**。

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

## 2026-10-23 R407
- 用户点名补收 `@agentpunkid`（Agent Punk ID）。R406 曾以「无独立官推」skip，属误判；已写入 `agentPadWatch.accounts` 必盯。

## 2026-10-23 R413
- 用户点名补收 `@pipfun_xyz`（Pipfun）。此前 RESULT 无痕迹=关键词漏捞，非「无官推」误判；已写入 `agentPadWatch.accounts`。
- 用户点名补收 `@pipfun_xyz`（Pipfun）。此前 RESULT 无痕迹=关键词漏捞，非「无官推」误判；已写入 `agentPadWatch.accounts`。
- 用户点名补收 `@StonksPadsh`（StonksPad）。此前 RESULT/库内无痕迹=关键词漏捞；官宣 2026-10-26 live on `@flapdotsh`；已写入 `meta.flapPadWatch.accounts` 必盯；卡 `stonks-pad`（R426）。
- 用户点名补收 `@spritefun_xyz`（Sprite Fun）。Discord Peek 曾标未收；官宣 2026-10-24 12:00 UTC live on Irys；已写入 `meta.irysPadWatch.accounts` 必盯；卡 `sprite-fun`（R436）。

## 2026-10-24 用户点名补盯 @Leeonmort
- 卡 `xuanwu-sigil` 已于 **R425** 收录（BNB Agent ID EX-00 Sigil mint LIVE）；非漏卡。
- 但 `meta.agentPadWatch.accounts` / `candidateIds` 此前未写入 `@Leeonmort` / `xuanwu-sigil` → 例行软刷不会专盯该号。
- 已补写入 `agentPadWatch.accounts` 必盯；软刷粉≈505；`focus:false` 保持。

## 2026-10-24 用户点名补收 @saulpink + @fulldotfun
- 库内此前 **无** `saulpink` / `fulldotfun` / `full.fun` / PinkSale 相关卡 → 关键词漏捞（非「无官推」）。
- 新收卡：`full-fun`（@fulldotfun，多链 meme launchpad live，full.fun）+ `saul-pink`（@saulpink，PinkSale 创始人，官宣周一 $FULL）。
- 已写入 `meta.fullFunWatch.accounts` 必盯：`@fulldotfun` `@saulpink`；`candidateIds`：`full-fun` `saul-pink`。
- `focus:false` 硬禁遵守；归台子/Meme。
- $FULL Monday（约 2026-10-26）非 ≤2h；平台本身已 live。

## 2026-10-25 用户点名补盯 @bitcointapes
- 卡 `bitcointapes`（BTape）已于 **R486** Discord alpha Peek 收录（Bitcoin TapeOut 电路 FREE MINT）；非漏卡。
- 但 `meta.tapeWatch.accounts` / `tapeOutWatch.accounts` / `candidateIds` 此前未写入 `@bitcointapes` / `bitcointapes` → 例行软刷不会专盯该号。
- 已补写入 `tapeWatch` + `tapeOutWatch` 必盯；软刷粉≈118；近帖：主网免费公平铸造即将开放（UCO/Ordinals）；`focus:false` 保持；ecosystem→Tape（chain 仍 Bitcoin）。
- 建议例行关键词：`@bitcointapes` / `BTape` / `Bitcoin Tapes` / `UCO` / `Ordinals 电路`。

## 2026-10-28 用户点名补收 @UBIdotFUN
- 库内此前 **无** `ubidotfun` / `UBIdotFUN` / `ubi.fun` → 关键词漏捞（雷达主盯 BN Agent/Flap/Tape/Elysium/RH，Arc+UBI launchpad 不在固定必盯）。
- 新收卡：`ubidotfun`（@UBIdotFUN，Arc 社区优先 token launchpad，官网 https://ubi.fun LIVE；Agents {v2} 官宣 2026-10-28 12:00 UTC / 20:00 CST）。
- 已写入 `meta.arcPadWatch.accounts` 必盯：`@UBIdotFUN`；`candidateIds`：`ubidotfun`；keywords：`UBIdotFUN` / `ubi.fun` / `Arc launchpad`。
- `focus:false` 硬禁遵守；归台子/Meme；`$UBI` CA 未独立核实。
- 建议例行关键词：`@UBIdotFUN` / `ubi.fun` / `UBI.fun` / `Arc launchpad`。

## 2026-10-28 用户自关注清单加强监控
- 用户发两张自关注清单，点名加强监控（尤其 `@mobster_meme`）。
- **已在库**：mobster / tape-fractal / gang-fun / motes / notuspad / ok-meme / ka-agents / tape-launch / naru-giwa / elysian-fields / ascendants-games / rebate-launch / boxa-elysium / peakfun·launch-on-peak / satcap / tapeup / pick-rush / playmooland / null-xmr / elytra·elyra / elysium-outlaws / foundry-tape / computeroll / oripa / reapoxyz / xmrroots；flap 系 flapPadWatch 已盯。
- **漏项补收（R775）**：`sunrig`(@sunrigfun) · `over-computer`(@overdotcomputer) · `peerxyz`(@peerxyz) · `joinbread`(@joinbread) · `crowdedfun`(@Crowdedfun) · `umia-finance`(@umia_finance)。`focus:false`。
- **noxstack**：`@noxstack` 为 `@nullonxmr` 协议核心开发同团队 → 写入 `null-xmr` links，**不单独建卡**。
- **必盯**：新建 `meta.userFollowWatch`（active，含清单官推 + candidateIds）；`meta.agentPadWatch` 加入 `@mobster_meme` / `mobster`。
- 例行每轮软刷 `userFollowWatch.accounts` 近帖；可操作窗 ≤2h notify。

## 用户打新零漏捕标准（2026-10-28）

Jafar 是打新玩家：目标尽量不漏可操作机会，不是固定赛道覆盖率好看。

每轮 X/精力硬顺序：① `meta.userFollowWatch` → ② 各必盯 Watch → ③ 关键词盲捞 → ④ Discord 仓内线索。额度紧时砍 ③④，**禁止砍 ①**。

硬规则：
- **在库但不在任何 Watch = 监控 bug**，本轮必须补进对应 Watch 或 `userFollowWatch`。
- 用户点名 / 丢关注表 → 立刻建卡 + 进 Watch，禁止只建卡不盯。
- 漏报当机制故障：补卡 + 进 Watch + 关键词，RESULT 写明漏因。

`userFollowWatch` 与 `agentPadWatch`（含 `@mobster_meme` / `mobster`）以 `data.json` 为准。

