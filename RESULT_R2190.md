# RESULT R2190


开火约 2026-11-25 18:04 CST（Asia/Shanghai）。lastScout 源数据 2026-11-25 17:51:27 CST。常规增量轮，不是 08:00 CST 后首轮全量补扫（lastFullAfterReset=R2170）。dry-run lastScout=2026-11-25 18:16:25 CST。

## X 额度与预算

- 第一笔 UF1 后 remainingToday=450 / 1000（本分钟 29/30，重置 2026-11-25 10:06:00Z）。因此 remainingBefore=451/1000，与预期一致。
- `python3 /workspace/early-scout/scripts/x_budget.py 450`（及 451）建议 mode=pace、softCap=18、minSpend=18、silentCap=2。
- **覆盖**：remaining ≫ 200，且用户禁止额度充足时砍栏，本轮仍按 queries.json 完整增量执行（与 R2185–R2189 相同）。UF3、MUST_WIN3 属于计划内完整增量（分片 qlen 与 R2189 新官号），不是探索性加读。
- 实际：xReads=28（main 27 + silent 1），remainingAfter=423/1000。无重复查询、无探索性加读、无分页。search_users 仍不可用。
- 全部 28 次搜索均成功写入 /tmp/r2190/x_raw/，errors=[]。

## 搜索执行

计划顺序已全部跑完一次：UF1/UF2/UF3 → MUST_WIN / MUST_WIN2 / MUST_WIN3 → MUST_OFF → 10 栏 + KW_GAPS 30m → MEN_DOGE / MEN_BTC / MEN_STARK / MEN_SQUEEK / MEN_STARX → SILENT_MINE。

30m 独立 KW 命中：LZ=7、TAPE=25、GIWA=25、DOGE=4、BTC=2、STARK=2、MINT=25、MINE=0、PAD=25、GO=24、ELY=3、GAPS=18。

**瘦栏 24h 回填**（仅 30m 独立 KW <5，每栏最多 +1）：

- 已跑：KW_DOGE_24（25）、KW_BTC_24（25）、KW_STARK_24（25）。
- 未跑：KW_LZ_24（7≥5）、KW_TAPE_24（25≥5）、KW_GIWA_24（25≥5）。
- MINE=0 但是核心栏，未加 24h。

UF 软刷：cursor 1561 @ZodiacFortune_N，50 户至 @bagnotary，wrap=false，total 源 2401 / dry-run 后 2402；下轮 1611 @HubrixRH。本分片无已知 NF（uf_skip=[]，mustOverlap=0）。UF1=0、UF2=16、UF3=0。

MUST：MUST_WIN / MUST_WIN2 / MUST_WIN3 均 25 触顶；MUST_OFF=1。MUST_OFF 已跳过已知 NF @starx_xlayer，未重试。@TheJacket_NVDA、@TriForgeAgent、@thecoffeeagents 未出现在本轮 MUST 返回的 25 条中（触顶，未加读）。The Jacket 改用公开 OpenSea 核验。

Mentions 本轮：DogeEVM-24h（9）/ BTC-24h（25 触顶）/ Starknet-24h（5）/ squeek-24h（0）/ STARX-24h（0）。下轮应轮换 pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest。

静号：挖矿（2190 % 11 = 1），SILENT_MINE 24h keyword fallback，1 帖，不占 softCap。命中 @williamapan 是艺术家讨论 GPU 渲染 GIF，与挖矿/mint 无关，未送审未收录。下轮 silent：台子/Meme（2191 % 11 = 2）。

## 关键核验

### The Jacket @TheJacket_NVDA — 已 LIVE（免费 mint）

官方开窗已到 2026-11-25 18:00 CST（10:00 UTC）。R2186 已发首次 ≤2h，不能只因仍在 2h 内重推。本轮 MUST_WIN2 触顶未见该官号新帖。

公开 OpenSea 核验（https://opensea.io/collection/the-jacket-man/overview 及 api.opensea.io）：

- drop.mintStatus=MINTING，disabledReason=null。
- SIGNED_PRESALE：2026-11-25 18:00:56–18:05:56 CST；PUBLIC_SALE：2026-11-25 18:05:56 CST 至 2026-12-02 18:05:56 CST，当前 activeDropStage 为公售。
- totalSupply=156 / 4444，remainingSupply=4288，uniqueItemCount=156，ownerCount 约 118–119。
- 合约 0x655d13c73ce062e95907e68db43cb39c6d11106a（Robinhood Chain），twitterUsername=TheJacket_NVDA。
- OpenSea 标题/地板 1.50 USDG、listedItemCount=13、近 24h volume 约 23.34 USDG，属二级市场，不是已核到的铸造价；overview 载荷未单独给出 stage 铸造单价。既有口径仍为 RebelKin / Argonauts / Vaultlings / Quotrons404 持有人免费 mint（只付 gas）。
- 上轮已铸 0，本轮 156 份已铸且 mintStatus=MINTING，确认免费 mint LIVE，属实质变化，必须 notify 并点名。卡片 status=live，le2h=false（已开铸，不再只是即将窗口），并补挂 freeMintWatch。

### ORIPA @oripaxyz — 首次 ≤2h，仍按点开窗

官帖仍是 16:43:16 CST https://x.com/oripaxyz/status/2125510621185839205：Allowlist emails are out；Rips open tonight, 8 PM GMT+8。无改期。未中签可从 11-26 铸造 Early Bird badge。Mint here：https://oripa.xyz/#early 。

官网 HTTPS 200，标题 oripa.xyz — Onchain Gacha for Real Graded Pokémon Cards，twitter:site=@oripaxyz，互证成立。不是免费 mint。开火/收尾均已过 18:00 CST，这是首次 ≤2h 窗口，必须 notify 并点名。卡片 le2h=true。

不要把 12:00 UTC / 任何 UTC 字段误读成 12:00 CST。

### ZeroGate @ZeroGate0G — 已确认 LIVE（非免费 mint）

R2189 已收录并提醒，但当时官帖 18:00 CST vs 官网 zeroLaunch=2026-11-30 口径冲突，未当 LIVE。本轮官帖 18:03:23 CST（https://x.com/ZeroGate0G/status/2125530779773997123）称 zero-gravity:native is live，并公布 CA 0xca2E57985A339E130775597332fc55ea0f917777。

官网 HTTPS 200，last-modified 约 2026-11-25 18:09 CST；twitter:site=@ZeroGate0G，window.__LZ.brand 已写入同一 CA，creationFee 仍 0.001 BNB；brand.zeroLaunch 仍写 2026-11-30，视为残留字段，不据此否定 LIVE。

DexScreener：BSC / flapsh 对 0xfB100E7167322D3eA6b3E06d92CbE2124ca52165，baseToken=ZeroGate / OG，报价 WBNB，pairCreatedAt=2026-11-25 18:03:44 CST；本轮见 marketCap≈$8330、liquidity≈$11071、h1 volume≈$17750.67、h1 buys=211 / sells=141。

已确认 LIVE，属实质变化，必须点名。不是免费 mint。

### TRIFORGE @TriForgeAgent

公共 BSC RPC（约 2026-11-25 18:07:10 CST，https://bsc-dataseed.binance.org/）：Forge Keys 免费铸仍 LIVE 未暂停，354/3333→356/3333，小幅增加，只更新卡片不重推。付费预售仍开，lpTotalMinted=0，lpTotalPaid=0；claimsOpen=true、totalClaimed=3；miningShares=6；tokenTradingEnabled=false。本轮 MUST 返回中未见该官号新帖。

## 新收录

DeepSeek（deepseek-flash，thinking on）打分并 admit：

- **Helipaid（@usehelipaid / https://helipaid.fun/）**：台子/Meme，score=56，focus=false。建号 2026-11-25 16:49:05 CST，15 粉 / 16 帖，xUserId 2125511782781341696。Solana 隐私创作者费发射台（Helius Privacy Rings），自称可为任意 X 账户发币。官网已公布平台币 CA F9uXudpDQVvQDUSqieuD79oxYVQMQzHbgCbYkrorpump；Dex 见 pump.fun 交易对（创建于 2026-11-25 17:41:38 CST，报价 hSOL，h1 buys=1067 / sells=619），但本轮 DexScreener 未返回美元市值/流动性/成交额，不编造。官网 window.PD.x 为空，页内 X 链接未回链官号，互证不完整（仅资料栏指向官网），仍按规则先建卡。不是免费 mint / 免费登记。已同时挂 userFollowWatch + agentPadWatch。

看见但未收录：@axtapi（当天新号，AI API「$5 FREE credit」，不是打新/发射台）；KW/mentions 里大量已入库项目转发、RGBHorse 拉新、GIWA 测试网 GAMA、以及年龄更大的无关站点。静号 @williamapan 已跳过。

## 库内其它更新（不重推）

- Rugg Kidz @RUGGKIDZ：官网 https://ruggkidz.com 自称 Mint is live，0.086 SOL / 份，7,777 供给，50/钱包；官帖自称已铸 27 份。付费 mint 已 LIVE，非免费，只更新卡片。
- Ugly Puggies：公开仍 2026-11-25 21:00 CST，约 19:00 CST 才进入 2h；本轮仅见中奖公布，不提前告警。
- Agent Cards：窗口仍 2026-11-25 23:00 CST，约 21:00 CST 才进入 2h。
- 2hour.fun：首窗仍 2026-11-26 05:00 CST（21:00 UTC，勿误读成今天 21:00 CST）。
- Shielded Wizards：公开仍 2026-11-26 05:10 CST（21:10 UTC）；本轮回复称 allowlist mint is open now，不是新的免费公铸窗口，不重推。
- Plato / The Unseen：publicEndsAt 2026-11-25 18:00 CST 是结束不是开窗；免费公铸延期至 12-03 的既有窗口不重推。
- Coffee Agents：MUST 未见新官帖，上次官方进度仍 188/1500，无实质变化。
- 4pump：18:04 CST 产品说明帖，CA 未变，R2188 已提醒不重推。
- SleighPad / OPCOM / Sov Money / gonk.fun / MEME FACTORY：无新的免费铸或需重推的实质变化。

## Discord Peek

discordPeekDeferred=true（占位已写入 dry-run，parent 可再合并 /tmp/r2190/discord_peek.json）。执行时已见到该文件：loginOk=false，loginWall=true，attemptedAt=2026-11-25 18:04:55 CST，停在 Discord 登录墙，四频道均未翻，lastSeen 保持不变。本路未自行做 Discord。

## notify

- notify=true
- reason：The Jacket 持有人免费 mint 已 LIVE（156/4444），须点名；ORIPA 首次 ≤2h、仍 20:00 CST 无改期，须点名（非免费 mint）；ZeroGate 已确认 LIVE，须点名（非免费 mint）；新收录 Helipaid，须点名（非免费 mint）。TRIFORGE 仅小幅进度不重推。
- alertMessage：【R2190】The Jacket @TheJacket_NVDA 持有人免费 mint 已 LIVE（156/4444）；ORIPA @oripaxyz 首包进入首次 ≤2h，定于 2026-11-25 20:00 CST，并非免费 mint；ZeroGate @ZeroGate0G 已确认 LIVE，并非免费 mint；新收录 Helipaid @usehelipaid 为 Solana 隐私发射台，并非免费 mint；面板：https://reboot7454.github.io/early-scout/
- namedFreeMintOrRegistration：The Jacket @TheJacket_NVDA
- dsFallback=false（deepseek-flash，thinking on；告警文案由 DeepSeek 起草，仅把 PANEL 换成面板链接）

## 失败 / 限制

- 28 次 X 搜索全部成功，无额度耗尽、无重试。
- search_users 不可用，静号走 mentions 关键词回退。
- MUST_WIN / MUST_WIN2 / MUST_WIN3 均 25 触顶；@TheJacket_NVDA、@TriForgeAgent、@thecoffeeagents 未出现在返回的 25 条中，未加读。The Jacket 用 OpenSea 公开页/API 核验。
- Helipaid DexScreener 未返回 volume / liquidity / marketCap / fdv，不编造美元数字。
- The Jacket OpenSea overview 未给出 stage 铸造单价；1.50 USDG 按二级地板记录。
- 官网静态页可能有 hydration 前占位，ZeroGate / ORIPA / Helipaid 以抓到的 HTML 与公开 API 为准。
- ingest_direct.py 预备稿有 `""round"` 笔误，已在 /tmp/r2190/ingest_direct.py 修好后跑通，未改仓库。
- Discord 登录墙，peek deferred。
- 本号不自动 mint。

## 产出路径

- /tmp/r2190/RESULT_R2190.md
- /tmp/r2190/notify.json
- /tmp/r2190/new_cards.json
- /tmp/r2190/ds_payload.json、/tmp/r2190/ds_score.json、/tmp/r2190/ds_alert.json、/tmp/r2190/ds_alert_payload.json
- /tmp/r2190/apply_r2190.py（默认 dry-run：APPLY_DRY_RUN=1 EARLY_SCOUT_DATA=/tmp/r2190/data.json.src APPLY_DRY_OUT=/tmp/r2190/data.json）
- /tmp/r2190/data.json（dry-run 结果，lastScout=2026-11-25 18:16:25 CST）
- /tmp/r2190/x_usage.json、/tmp/r2190/x_all.json、/tmp/r2190/x_raw/
- /tmp/r2190/triforge_rpc.json
- /tmp/r2190/discord_peek.json（parent 并行产物，loginOk=false）
