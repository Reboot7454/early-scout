# R2196 X-radar RESULT

- Round: **R2196**（增量轮，非 08:00 CST 首轮全量补扫）
- lastScout 写入：`2026-11-25 22:20:01 CST`（Asia/Shanghai）
- lastFullAfterReset：R2170
- 面板（父进程 push 后）：https://reboot7454.github.io/early-scout/
- 产出：`/tmp/r2196/RESULT_R2196.md`、`/tmp/r2196/notify.json`、`/tmp/r2196/data.json`（dry-run，未改 `/workspace/early-scout/data.json`）
- apply：`/tmp/r2196/apply_r2196.py`（`APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2196/data.json.src APPLY_DRY_OUT=/tmp/r2196/data.json` 已成功）

## X 预算与检索

- **remainingBefore=286/1000**（首搜 UF1 后脚注 285/1000，故开火前为 286，与 R2195 remainingAfter 一致）
- **remainingAfter=258/1000**
- **xReads=28**（main 27 + silent 1）
- `x_budget.py 286` 建议 mode=pace，softCap=18，minSpend=18，silentCap=2
- **Override：** remaining >> 200，按用户额度充裕时不得砍栏的规则，跑满 queries.json 已排好的增量计划（24 主搜 + 1 静号），并在薄栏 30m KW <5 时加 24h 回看。与 R2185–R2195 相同 override。已写入 `meta.xBudgetMode=pace-override-full`
- 全部 10 条泳道 + KW_GAPS 均已跑 30m：是
- 计划内 25 次搜索各跑一次，无重复/探索性补搜；薄栏 24h 仅 LZ/BTC/Starknet 各 +1
- 已知 NF `@starx_xlayer` 未做 from: 重试；MEN_STARX 提及该号是允许的（本轮 0 帖）
- MUST_WIN / MUST_WIN2 / MUST_WIN3 均为计划内官号 24h from:（因 qlen 拆批，含 R2195 官号 @freakapesnft @CityHood_NFT @OUTLAWSxNFT），不是探索读

### 各搜结果

| id | window | result_count | remToday after |
|---|---|---:|---:|
| UF1 | 30m | 2 | 285 |
| UF2 | 30m | 1 | 284 |
| UF3 | 30m | 1 | 283 |
| MUST_WIN | 24h | 25（触顶，有 next_token，未翻页） | 282 |
| MUST_WIN2 | 24h | 25（触顶） | 281 |
| MUST_WIN3 | 24h | 25（触顶） | 280 |
| MUST_OFF | 30m | 0 | 279 |
| KW_LZ | 30m | 1 | 278 |
| KW_TAPE | 30m | 25 | 277 |
| KW_GIWA | 30m | 25 | 276 |
| KW_DOGE | 30m | 11 | 275 |
| KW_BTC | 30m | 2 | 274 |
| KW_STARK | 30m | 1 | 273 |
| KW_MINT | 30m | 25 | 272 |
| KW_MINE | 30m | 2 | 271 |
| KW_PAD | 30m | 25 | 270 |
| KW_GO | 30m | 25 | 269 |
| KW_ELY | 30m | 18 | 268 |
| KW_GAPS | 30m | 24 | 267 |
| MEN_DOGE | 24h | 9 | 266 |
| MEN_BTC | 24h | 25 | 265 |
| MEN_STARK | 24h | 4 | 264 |
| MEN_SQUEEK | 24h | 0 | 263 |
| MEN_STARX | 24h | 0 | 262 |
| SILENT_GIWA | 24h | 25 | 261 |
| KW_LZ_24 | 24h | 25 | 260 |
| KW_BTC_24 | 24h | 25 | 259 |
| KW_STARK_24 | 24h | 25 | 258 |

无 X 工具错误。部分 24h/热门栏 result_count=25 且有 next_token，按规则不翻页。

## UF 分片 / 光标

- 本轮 cursor **1861 @pumptoksocial**，50 个账号刷到 **@WantedLaunch**
- next **1911 @yuange99988852**，wrap=false，total 开火前 2415、入库后 2419（新挂 4 个官号到表尾，未打乱光标）
- UF1/UF2/UF3 因 qlen 拆成三次 from:；UF3 短尾巴 `@Codedotkitty @WantedLaunch`
- 本分片无已知 NF（uf_skip=[]）；mustOverlap=0（`@ThinkersClub_` 在本分片内，已从 MUST_WIN 24h 去掉，只读 30m UF）
- 本轮 UF 帖：@UnicornGPrix 两条社区回复（无改期/开铸）；@beavzclub「First 150 / Free mint / Drop EVM wallet」；@Codedotkitty 20 人 GTD 免费 mint 抽奖

## Mentions 与静号

- 本轮 mentions（24h）：**DogeEVM / BTC / Starknet / squeek / STARX**（MEN_DOGE 9、MEN_BTC 25、MEN_STARK 4、MEN_SQUEEK 0、MEN_STARX 0）
- **下轮 mentions 轮转：** pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest（本轮未跑这些）
- 本轮静号：**GIWA**（SILENT_GIWA，24h has:mentions has:links，25 帖，多为已在库的 @GAMA_GIWA 测试网发射讨论/转发，未把已在库打新转发花掉静号配额去探索）
- **下轮静号：** DogeEVM（2197 % 11 = 8）
- search_users 仍不可用，静号走已写入 queries 的 SILENT_GIWA 兜底

## 薄栏 24h 回看

30m 独立 KW 命中：LZ **1**、TAPE 25、GIWA 25、DOGE 11、BTC **2**、STARK **1**。MINE=2 但是核心栏，不加 24h。MINT/PAD/GO/ELY/GAPS 均 ≥5 或不属于薄栏。

- **做了：** KW_LZ_24、KW_BTC_24、KW_STARK_24（各 25）
- **没做：** KW_TAPE_24 / KW_GIWA_24 / KW_DOGE_24（30m 已 ≥5）

## 新收录（DeepSeek 打分，dsFallback=false）

1. **VALORIX @VALORIXBNB** — id `valorix`，score **55**（early 88 / actionable 55 / novelty 52 / risk 25）。建号 **2026-11-25 21:44:18 CST**，0 粉 / following 0 / 1 帖，xUserId 2125585958641037312。官网 https://valorixofficiall.web.app/ 与官号互证。官帖 21:52:50 CST（https://x.com/VALORIXBNB/status/2125588526247072232）称 LIVE：用 Binance Agent ID 铸 FREE card，再买 VALX shares。官网：Hero Card 需邀请码、1 卡/Agent ID、只付 gas；份额 **0.002 BNB/份**，首轮 5,500，窗口 2026-11-25 21:00 CST 至 2026-11-28 21:00 CST 或售罄。本轮 BSC RPC：Cards `0xf0eD746BEd0f513811485d811DBd30c13d79728c` name=Valorix Hero Cards，**totalMinted=11**；Mint `0xE56993B5655e6208069fb1e08Ded325F5DdADcD1` **fillSold=0/5500**；VALX `0x84Aa2285a2b2FcB475D0FC098e3b2E696201a20c` totalSupply=41,250,000；Agent ID 走既有 SPACE ID 注册表 `0x60B9262456dE011F7d15a54CdD8c48bAaa8B022F`。免费卡路径已链上确认；**份额不是免费**。Firebase 域名 officiall 双写 l，0 粉极新号，风险高。focus=false。Watches：userFollowWatch + freeMintWatch + bnAgentWatch + agentPadWatch。

2. **Flybrain @flybrainterm** — id `flybrain`，score **38**。建号 **2026-11-25 03:16:35 CST**，0 粉 / 2 帖，xUserId 2125306907082563584。站点 https://flybrainterminal.fun（资料栏 HTTP，实际 HTTPS 200）。自称果蝇脑 Solana 发射台，Create coin 至少 0.01 SOL dev buy，本轮 0 币。站点未回链官号（siteXMutual=false）。不是免费 mint。Watch：userFollowWatch。

3. **A Journey Boats @ajourneyboats** — id `ajourney-boats`，score **40**。建号 **2026-11-25 20:37:13 CST**，4 粉 / 18 帖，xUserId 2125569256154873856。官网 https://ajourney.boats/，twitter:site=@AJourneyBoats 与官号互证。自称 Robinhood Chain 上 AI 船长交易股票代币，产品页几乎只有一幅画，无 CA / 铸造窗。不是免费 mint。Watch：userFollowWatch。

4. **Fueltender @fueltenderagent** — id `fueltender`，score **48**。建号 **2026-11-25 15:13:11 CST**，14 粉 / 8 帖，xUserId 2125487238498922496。官网 https://fueltender.agency 与官号互证。Robinhood Chain gas 油箱（EIP-7702 + ERC-4337），演示罐已有少量 refuel。CA / $TENDER 仍写 at launch，本轮未见。不是免费 mint。Watch：userFollowWatch。

## 看见但未收录

- **Clash of Cats @ClashOfCatss** / https://coconsol.fun：建号约 2 天、7 粉，官帖只说还在等上线，官网可见文本几乎只有标题，无 CA / 规则 / 链。DeepSeek admit=false（overall 20）。
- **Agent Pass「54/10,000 免费灵魂绑定 NFT」**：仅见 @ZainMuttaqin21 等猎人转帖，t.co 展开为 `https://unrivaled-tulumba-61bd9b.netlify.app/`，未见已核验官号，不收录。
- **@astituponi** 等静号帖在讲已在库的 @GAMA_GIWA（GIWA 测试网发射台），不是新官号。
- **@shaolinsaga**：旧项目，出现在 @Owltopia_sol 付费 raffle（0.03 SOL），不新收。
- **@BlockpayGenesis**：本轮未再出现；仍不因旧的自称免费 LIVE、缺独立站点/CA 而强收。
- 大量 mint 关键词噪帖 / 已在库项目转发（RGBHorse、hoojafun、playblocq、LawoftheAbyss、Spike__wtf 等）不重复收录。

## 库内刷新（不重推，除非另行说明）

- **Ugly Puggies @uglypuggies**：21:35:39 CST 官帖「1 hrs and 30 mins before mint」，与官窗 **2026-11-25 23:00 CST** 一致。OpenSea collection API 仍 **0/777**、持有 0；drop 页 mintStatus=**MINTING_SOON**，activeDropStage=null，首阶段仍 23:00–23:30 CST。R2195 已发首次 ≤2h，**不重推**。le2h 保持 true。
- **Agent Cards @agentcardshq**：MUST 24h 未见新官帖，翻印窗仍 23:00 CST。R2195 已发首次 ≤2h，**不重推**。le2h 保持 true。
- **deMiners @deMinersNft**：OpenSea collection **512/3333**（R2195 505；drop 页 512，R2195 为 508），持有 **135**（R2195 134），地板仍 0.00059 ETH。drop 时间表未变：OG 至 **2026-11-26 00:30:04 CST**，付费公售同时点起、仍 0.0002 ETH。MUST 只见表情回复。OG 免费仍 LIVE。公售首次 ≤2h 从 **22:30 CST** 才开始，本轮开火约 22:03–22:20，**不提前发**。le2h=false。
- **ORIPA @oripaxyz**：继续 ripping（50 pools / 10K packs 等），并提到 Early Bird 明日 20:00 CST。约 22:00 CST 的 2h 窗已结束，无改期，**不重推**。le2h 改为 false。
- **The Jacket @TheJacket_NVDA**：OpenSea **207/777**（R2195 205），持有 131（R2195 129），地板 1.0 USDG。无新官帖，小幅进度，**不重推**。
- **TRIFORGE @TriForgeAgent**：链上 Forge Keys **550/3333**（R2195 409；官帖 20:15 CST 自称 364，落后于链），claims 19（R2195 8），预售 lpTotalMinted 仍 0，挖矿 shares 仍 6。免费 Key 仍 LIVE，规则未变，进度更新，**不重推**。
- **F0B90B @F0B90Bclub**：链上 **292/10000**（R2195 215），mintOpen=true，规则未变，无新官帖，**不重推**。
- **Antopia @antopia_xyz**：链上 **6249/8888**（R2195 6244），免费额度仍 4000/4000 满。官帖宣布 Clash of Antopia **2026-11-26 21:00 CST**（13:00 UTC），不是铸造规则变化，**不重推**。
- **WishList @TheWishListSol**：官帖称 “$WISH is live”，同时有 “WishList. Soon.”。官网 /config.json / 前端 JS 仍写 **CA: coming at launch**，链接展开为官网或官帖视频，未见已公布 CA。**不重推**。
- **ZeroGate @ZeroGate0G**：MUST 再见到已在 R2195 入库的 18:03 CST 官帖与既有 CA，无新变化，**不重推**（仅修正过时 summary 里「平台代币 CA 尚未公布」）。
- **Beavz Club @beavzclub**：官帖改口 **First 150** 免费 mint，继续 Drop EVM wallet，仍无官网/CA。更新卡片，**不重推**（丢钱包风险，不要回复地址）。
- **Code Kitty @Codedotkitty**：20 人 GTD 免费 mint 抽奖，仍未开铸，**不重推**。
- **DAEMONS @daemons_art**：官帖 “FREE MINTS. Before Christmas. For the waitlist only.”，与既有 12 月 waitlist 口径一致，**不重推**。
- **2hourfun @2hourfun**：官帖确认 Telegram 已开，第一场 **21:00 UTC tonight = 2026-11-26 05:00 CST**。不要把 extract 的 teaserAtUTC 23:00 CST 当成今天开窗。**不提前告警**。
- **Shielded Wizards @ShieldedWizBTC**：本轮 MUST 未见新官帖。公售仍是 **2026-11-26 05:00 CST**，WL 免费仍 LIVE（R2165 已提醒），**不提前告警、不因仍 LIVE 重推**。

## discordPeekDeferred

占位已写入 data.json（`meta.discordPeekDeferred=true`）。父进程平行 computerUse 的 `/tmp/r2196/discord_peek.json` 已在开火时存在：`loginOk=false`，`loginWall=true`，attemptedAt **2026-11-25 22:02:12 CST**，当前 URL 为 Discord 登录墙。请父进程按需合并真实 peek，本执行器未自行翻 Discord。

## 失败 / 限制

- X 检索全部成功，无重试、无 0 remaining 中断
- MUST_WIN/2/3、若干热门 KW/mentions/静号 result_count=25 触顶，未翻页（按规则）
- OpenSea drops API 仍 401/不可用，改用 collection+stats API + 合集 HTML 里的 SeaDrop JSON（与 R2195 相同路径）
- `search_users` 仍不可用
- extract.py 的假 LE2H（2hourfun teaserAtUTC 23:00 CST、deMiners 旧 public 22:30 CST）已忽略，未按这些告警
- DeepSeek 打分成功，**dsFallback=false**
- 未修改、未 commit、未 push `/workspace/early-scout/data.json`

## notify

- **notify=true**
- 理由：新收录 VALORIX @VALORIXBNB（免费 Hero Card 已链上 LIVE，需邀请码、只付 gas；VALX 份额仍是付费 0.002 BNB）；同时新收录 Flybrain @flybrainterm、A Journey Boats @ajourneyboats、Fueltender @fueltenderagent（均不是免费 mint，需在告警里点名）。不重推 R2195 已发的 Ugly Puggies / Agent Cards 首次 ≤2h。不提前发 deMiners 付费公售首次 ≤2h。不提前告警 2hourfun / Shielded Wizards。
- namedFreeMintOrRegistration：`VALORIX @VALORIXBNB`
- dsFallback：false
- alertMessage 见 `/tmp/r2196/notify.json`（已点名 @handles）

## 父进程落盘前补丁

- 已重写 `meta.xBudgetPlan` 为 R2196（remainingBefore 286 → remainingAfter 258，xReads 28，mode pace-override-full，ufCursor 1911 @yuange99988852）。
- 已更新 `mentionsCoverage` / `mentionsNext`（下轮 pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest）与 `silentLane=GIWA`、`silentNext=DogeEVM`。
- 已合并 `/tmp/r2196/discord_peek.json`：attemptedAt 2026-11-25 22:02:12 CST，loginOk=false，loginWall=true，channelsPeeked=false，lastSeen 仍停在 2026-11-23 22:56 CST，`discordPeekDeferred=true`。
- 已写 `meta.round2196Added`；Canton / Glaze / TokenWorks lastChecked 软债刷到本轮。
- Flybrain 另挂 `agentPadWatch`（发射台，匹配栏）。VALORIX 原挂不变。
- 工作区原仍为 R2195（4d2397d）；本补丁后复制到仓库 `data.json` + `docs/data.json` 再推送。
