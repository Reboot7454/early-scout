# R2197 X-radar RESULT

- Round: **R2197**（增量轮，非 08:00 CST 首轮全量补扫）
- lastScout 写入：`2026-11-25 22:48:42 CST`（Asia/Shanghai）
- lastFullAfterReset：R2170
- 面板（父进程 push 后）：https://reboot7454.github.io/early-scout/
- 产出：`/tmp/r2197/RESULT_R2197.md`、`/tmp/r2197/notify.json`、`/tmp/r2197/data.json`（dry-run，未改 `/workspace/early-scout/data.json`）
- apply：`/tmp/r2197/apply_r2197.py`（`APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2197/data.json.src APPLY_DRY_OUT=/tmp/r2197/data.json` 已成功）

## X 预算与检索

- **remainingBefore=258/1000**（首搜 UF1 后脚注 257/1000，故开火前为 258，与 R2196 remainingAfter 一致）
- **remainingAfter=229/1000**
- **xReads=29**（main 28 + silent 1）
- `x_budget.py 258` 建议 mode=pace，softCap=18，minSpend=18，silentCap=2
- **Override：** remaining >> 200，按用户额度充裕时不得砍栏的规则，跑满 queries.json 已排好的增量计划（25 主搜 + 1 静号），并在薄栏 30m KW <5 时加 24h 回看。与 R2185–R2196 相同 override。已写入 `meta.xBudgetMode=pace-override-full`
- 全部 10 条泳道 + KW_GAPS 均已跑 30m：是
- 计划内 26 次搜索各跑一次，无重复/探索性补搜；薄栏 24h 仅 LZ/BTC/Starknet 各 +1
- 已知 NF `@starx_xlayer` 未做 from: 重试；mentions 里提到该号是允许的（本轮 mentions 未跑 STARX 栏）
- MUST_WIN / MUST_WIN2 / MUST_WIN3 / MUST_WIN4 均为计划内官号 24h from:（因 qlen 拆批，含 R2196 新号 @VALORIXBNB @flybrainterm @ajourneyboats @fueltenderagent），不是探索读

### 各搜结果

| id | window | result_count | remToday after |
|---|---|---:|---:|
| UF1 | 30m | 0 | 257 |
| UF2 | 30m | 2 | 256 |
| UF3 | 30m | 0 | 255 |
| MUST_WIN | 24h | 25（触顶，有 next_token，未翻页） | 254 |
| MUST_WIN2 | 24h | 25（触顶） | 253 |
| MUST_WIN3 | 24h | 22（有 next_token，未翻页） | 252 |
| MUST_WIN4 | 24h | 9 | 251 |
| MUST_OFF | 30m | 8 | 250 |
| KW_LZ | 30m | 1 | 249 |
| KW_TAPE | 30m | 25 | 248 |
| KW_GIWA | 30m | 25 | 247 |
| KW_DOGE | 30m | 14 | 246 |
| KW_BTC | 30m | 2 | 245 |
| KW_STARK | 30m | 4 | 244 |
| KW_MINT | 30m | 25 | 243 |
| KW_MINE | 30m | 2 | 242 |
| KW_PAD | 30m | 25 | 241 |
| KW_GO | 30m | 25 | 240 |
| KW_ELY | 30m | 23 | 239 |
| KW_GAPS | 30m | 22 | 238 |
| MEN_PADS | 24h | 17 | 237 |
| MEN_GIWA | 24h | 25（触顶） | 236 |
| MEN_TAPE | 24h | 9 | 235 |
| MEN_LZ | 24h | 25（触顶） | 234 |
| MEN_ELY | 24h | 24 | 233 |
| SILENT_DOGE | 24h | 1 | 232 |
| KW_LZ_24 | 24h | 25（触顶） | 231 |
| KW_BTC_24 | 24h | 25（触顶） | 230 |
| KW_STARK_24 | 24h | 25（触顶） | 229 |

无 X 工具错误。部分 24h/热门栏 result_count=25 且有 next_token，按规则不翻页。MUST_WIN3 为 22 但仍带 next_token，同样未翻页。

## UF 分片 / 光标

- 本轮 cursor **1911 @yuange99988852**，50 个账号刷到 **@rack_compute**
- next **1961 @lpstationxyz**，wrap=false，total 开火前 2419、入库后 2422（新挂 3 个官号到表尾，未打乱光标）
- UF1/UF2/UF3 因 qlen 拆成三次 from:；UF3 短尾巴 `@rack_compute`
- 本分片无已知 NF（uf_skip=[]）
- 本轮 UF 帖：@Vice6fun「Work is underway... We're getting close.」（无改期/开铸）；@AcruxHub 感谢 @AcruxComputer 关注，并称几天前已私信对方团队一个安全问题

## Mentions 与静号

- 本轮 mentions（24h）：**pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest**（MEN_PADS 17、MEN_GIWA 25、MEN_TAPE 9、MEN_LZ 25、MEN_ELY 24）
- **下轮 mentions 轮转：** DogeEVM / BTC / Starknet / squeek / STARX（本轮未跑这些）
- 本轮静号：**DogeEVM**（SILENT_DOGE，24h has:mentions (DogeEVM OR DogeOS) (mint OR launch)，1 帖；search_users 仍不可用，走已写入 queries 的 mentionQuery 兜底）
- **下轮静号：** BTC（2198 % 11 = 9）

## 薄栏 24h 回看

30m 独立 KW 命中：LZ **1**、TAPE 25、GIWA 25、DOGE 14、BTC **2**、STARK **4**。MINE=2 但是核心栏，不加 24h。MINT/PAD/GO/ELY/GAPS 均 ≥5 或不属于薄栏。

- **做了：** KW_LZ_24、KW_BTC_24、KW_STARK_24（各 25）
- **没做：** KW_TAPE_24 / KW_GIWA_24 / KW_DOGE_24（30m 已 ≥5）

## 新收录（DeepSeek 打分，dsFallback=false）

1. **Mopao Terminal @mopaoxyz** — id `mopao`，score **64**（early 88 / actionable 45 / novelty 55 / risk 30）。建号 **2026-11-12 06:01:01 CST**，14 粉 / following 3 / 34 帖，xUserId 2120636419156889600。官网 https://mopao.xyz/ HTTPS 200，twitter:site=@mopaoxyz，站点与官号互证。官帖 21:32:17 CST（https://x.com/mopaoxyz/status/2125583351906181594）称 Terminal 已 LIVE，并称 $MOPAO 30 分钟后在 @flapdotsh 发射（约 22:02 CST）。本轮未再读 X、也未独立核到 Flap CA。**不是免费 mint**。focus=false。Watches：userFollowWatch + flapPadWatch。

2. **Acrux @AcruxComputer** — id `acrux-computer`，score **57**。建号 **2026-11-16 17:25:23 CST**，479 粉 / following 4 / 204 帖，xUserId 2122258482347053056。官网 https://acrux.computer/ HTTPS 200，链到 https://x.com/AcruxComputer 与 github.com/AcruxComputer/acrux，站点与官号互证。自称 Solana fork（三 proposer、50ms slot）。本轮无该号原创帖；已在库的 @AcruxHub 于 22:10:49 CST 称向其团队私信了安全问题。**不是免费 mint**，也不是打新窗口。focus=false。Watch：userFollowWatch。

3. **TAIL @tailtradesxyz** — id `tailtrades`，score **61**。建号 **2026-11-19 12:46:22 CST**，10 粉 / following 0 / 7 帖，xUserId 2123276042614050816。官网 https://tailtrades.xyz/ HTTPS 200，twitter:site=@tailtradesxyz，站点与官号互证。自称 Hyperliquid 上公开运行的 AI 交易台，利润回购销毁 $TAIL，并挂靠 @Enter_Elysium。bio 写 CA `0xC6333959D096f151dee397AC56c9259a1127B870`（本轮未链上核验）。官帖 13:07:33 CST。**不是免费 mint**。官方生态页 https://elysium.kinetiq.xyz/ecosystem 本轮未列出 TAIL，属挂靠自称、未核到 On testnet/Announced，**不进 Elysium 栏**（ecosystem 已清空）。focus=false。Watches：userFollowWatch + elysiumWatch（仅作挂靠盯梢）。

## 看见但未收录

- **Loxleyswap @loxleyswap** / https://loxleyswap.com/：建号 2026-09-23（约 63 天），27 粉，官网与官号互证，自称 Elysium 兑换、24h 约 $3.75M 成交。DeepSeek admit=false（overall 50；窗口已过、粉丝与成交数据不匹配）。
- **Autonomo @useautonomo** / https://autonomo.fun/：建号 2026-10-28（约 28 天），603 粉，x402 API 发射台，已有 $AUTONOMO CA。DeepSeek admit=false（已发币、不再是早期打新窗）。
- **@supersmoney**：1 天新号、0 粉，只是在转述已在库的 @AscendLaunch「Free (planned) / TBA」，不是新官号。
- **@astituponi**：0 天新号，在讲已在库的 GAMA / @gamapadcom（GIWA 测试网发射台），不是新官号。
- **@HumanCoinOnRH**：约 2 天、资料栏是新闻站，本轮无原创项目帖，不收。
- 大量 mint 关键词噪帖 / 已在库项目转发（Vicehood、Spike__wtf、PandalZero、MMIX、Niblekins、Owltopia 等）不重复收录。

## 必须通知的 ≤2h / 库内刷新

- **deMiners @deMinersNft**：**付费公售首次进入 ≤2h**（从今晚 22:30 CST 起算，本轮开火已过 22:30）。时间表未改：公售仍是 **2026-11-26 00:30:04 CST** 起、**0.0002 ETH（不是免费公售）**。OpenSea collection **515/3333**（R2196 512），持有 **137**（R2196 135），地板 0.000511 ETH；drop 页 mintStatus=**MINTING**，activeDropStage 仍是 SIGNED_PRESALE（stageIndex 2）至 00:30:04 CST，随后 PUBLIC_SALE。OG 免费 mint 仍 LIVE 至同一时刻，R2191 已提醒，不因仍 LIVE 单独重推，已在同一条告警里带进度。le2h=true。
- **Ugly Puggies @uglypuggies**：官窗仍 **2026-11-25 23:00 CST**。OpenSea 仍 **0/777**、持有 0；drop 页 mintStatus=**MINTING_SOON**，activeDropStage=null，首阶段仍 23:00–23:30 CST。MUST 再见到 21:35 CST「1 hrs and 30 mins before mint」倒计时官帖，未见开铸。R2195 已发首次 ≤2h，**不重推**。
- **Agent Cards @agentcardshq**：MUST 24h 未见新官帖，翻印窗仍 23:00 CST。R2195 已发首次 ≤2h，不得写成免费 mint，**不重推**。
- **ORIPA @oripaxyz**：MUST 再见到今日 ripping 进度帖（与 R2196 已记录的同一组）。Early Bird 仍 2026-11-26 20:00 CST。≤2h 窗已结束，无改期，**不重推**。
- **The Jacket @TheJacket_NVDA**：OpenSea 仍 **207/777**（与 R2196 相同），持有 131，地板 1.0 USDG。无新官帖，**不重推**。
- **TRIFORGE @TriForgeAgent**：链上 Forge Keys **610/3333**（R2196 550），claims 21（R2196 19），预售 lpTotalMinted 仍 0，挖矿 shares 仍 6。官帖 20:15 CST 自称 364（落后于链）。免费 Key 仍 LIVE，规则未变，**不重推**。
- **F0B90B @F0B90Bclub**：链上 **308/10000**（R2196 292）。MUST 见 22:31:37 CST 进度官帖自称 304。mintOpen=true，规则未变，**不重推**。
- **Antopia @antopia_xyz**：链上 **6253/8888**（R2196 6249），免费额度仍满。无新的铸造规则变化，**不重推**。
- **VALORIX @VALORIXBNB**：BSC RPC Hero Cards 仍 **11**，fillSold 仍 **0/5500**，无实质变化，**不重推**。
- **Fueltender @fueltenderagent**：22:30 CST 官帖称 TENDER 即将上线、CA 只会发在本官号和官网；罐体已可试 0 ETH refuel。CA 仍未公布，不是免费 mint，**不重推**。
- **DAEMONS @daemons_art**：官帖 “FREE MINTS. Before Christmas. For the waitlist only.”，与既有 12 月 waitlist 口径一致，**不重推**。
- **2hourfun @2hourfun**：官帖确认 Telegram 已开，第一场 **21:00 UTC tonight = 2026-11-26 05:00 CST**。不要把 extract 的 teaserAtUTC 23:00 CST 当成今天开窗。**不提前告警**。
- **Shielded Wizards @ShieldedWizBTC**：本轮 MUST 未见新官帖。公售仍是 **2026-11-26 05:00 CST**，**不提前告警、不因仍 LIVE 重推**。

## discordPeekDeferred

已合并 `/tmp/r2197/discord_peek.json` 进 `meta.discordAlphaPeek`：`loginOk=false`，`loginWall=true`，attemptedAt **2026-11-25 22:34:06 CST**，四频道均未翻到（登录墙），lastSeen 不变。`meta.discordPeekDeferred=true`。本执行器未打开 Discord/浏览器。

## 失败 / 限制

- X 检索全部成功，无重试、无 0 remaining 中断
- MUST_WIN/2、若干热门 KW/mentions 以及三组薄栏 24h result_count=25 且有 next_token，按规则不翻页
- OpenSea drops API 仍不可用，改用 collection+stats API + 合集 HTML 里的 SeaDrop JSON（与 R2195/R2196 相同路径）
- `search_users` 仍不可用
- extract.py 的假 LE2H（2hourfun teaserAtUTC 23:00 CST）已忽略，未按这个告警
- DeepSeek 打分与 alert 草稿成功，**dsFallback=false**（alert 已补上面板链接、轮次前缀与官网 URL，并点名 handle）
- 未修改、未 commit、未 push `/workspace/early-scout/data.json`

## notify

- **notify=true**
- 理由：deMiners @deMinersNft 付费公售首次进入 ≤2h（0.0002 ETH，不是免费公售）；同时新收录 Mopao Terminal @mopaoxyz、Acrux @AcruxComputer、TAIL @tailtradesxyz（均不是免费 mint，须在告警里点名）。不重推 R2195 已发的 Ugly Puggies / Agent Cards 首次 ≤2h。不提前告警 2hourfun / Shielded Wizards。
- namedFreeMintOrRegistration：无（本轮新卡均不是免费 mint/登记；deMiners 本轮通知的是付费公售）
- namedPaidLe2h：`deMinersNft`
- dsFallback：false
- alertMessage：

```
R2197：deMiners @deMinersNft 付费公售首次进入 ≤2h，2026-11-26 00:30:04 CST 起、0.0002 ETH（不是免费公售）。OG 免费 mint 仍 LIVE 至同一时刻，OpenSea 515/3333、持有 137、地板 0.000511 ETH。新收录 Mopao Terminal @mopaoxyz（https://mopao.xyz/）自称终端已 LIVE，并称 $MOPAO 约 22:02 CST 在 @flapdotsh 发射，本轮未核到 CA，不是免费 mint。新收录 Acrux @AcruxComputer（https://acrux.computer/）自称 50ms Solana fork，不是免费 mint。新收录 TAIL @tailtradesxyz（https://tailtrades.xyz/）自称 Hyperliquid/Elysium AI 交易台，bio 有 CA 未链上核验，不是免费 mint。Ugly Puggies @uglypuggies / Agent Cards @agentcardshq 官窗仍是 2026-11-25 23:00 CST，R2195 已发首次 ≤2h，本轮未见开铸，不重推。2hourfun / Shielded Wizards 公售均为 2026-11-26 05:00 CST，不提前告警。本号不自动 mint。面板：https://reboot7454.github.io/early-scout/
```

## 写盘摘要（供父进程）

- dry-run：`/tmp/r2197/data.json`
- `meta.round2197Added` = 顶层 `newThisRound` = `['mopao', 'acrux-computer', 'tailtrades']`
- ufCursor **1961 @lpstationxyz**，uf_total 2422，wrap=false
- mentionsCoverage / mentionsNext、silentLane=DogeEVM、silentNext=BTC 已写
- Canton / Glaze / TokenWorks lastChecked 软债刷到本轮
- 已合并 discord_peek.json，`discordPeekDeferred=true`
- 工作区 `/workspace/early-scout/data.json` 未改（mtime 仍为 2026-11-25 22:23:19 CST）
