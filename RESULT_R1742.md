# RESULT R1742

- time: 2026-11-13 09:46 CST（Asia/Shanghai）
- mode: ample（R1739 已完成 08:00 CST 后首轮全量补扫，本轮为正常节流，不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: true
- xReads: 26（main 25 = 计划 24 + LE2H2 1；silent 1；admitVerify 0）；remainingBefore 919 → remaining 893 / 1000；softCap 28，minSpend 20，silentCap 2；未超 softCap，高于 minSpend
- admitVerifyReads: 0（新卡 @clause_protocol 已在 KW_CORE_mint / KW_GAPS_MINE 作为作者返回档案；@ZeroGuysNFT 档案来自 mentions。官网 / 链上 / MCP 只读无 X 成本，未重读官帖时间线）
- tenLanes: true（薄栏 6 条独立 KW + 核心 KW 打新/台子/GO/Elysium + KW_GAPS_MINE squeek/Nutshell/仓鼠链/STARX/Agent ID/AIDROP/Pulse/computeroll + 挖矿词全跑；BN Agent 靠 fat agentPad/bnAgent。LayerZero/GIWA/BTC/Starknet 薄栏 KW 本窗 0 帖，但仍已跑）
- userFollow: 刷完本片 1313→1363，kept 50，skip 0，下一轮从 1363 续（UF 全表现 1575，扫后因新卡增至 1577；本轮不是整表一次扫完）
- mentions: 本轮轮换已覆盖 Tape、GIWA、LayerZero、BTC、Starknet、DogeEVM，以及 rest Elysium/kinetiq、flap/Irys/Full.fun/Arc、squeek/Nutshell、STARX、PulseLaunchpad、dotaipad；mentionsThinDeferred=[]
- fat shards: agentPad 27→55 kept 28 skip 0；freeMint 144→179 kept 28 skip 7；bnAgent 44→83 kept 28 skip 11；elysium 220→248 kept 28 skip 0
- thin official watches: 93 unique，2 个 from: 批次，skip 0；含 starknet/LZ/btcPrivacy/btcCrc20/dogeEvm/tape/tapeOut/giwa/zeroWatch
- silentAccounts: ran=true，lane=LayerZero，search_users unavailable，改跑 mentions（窗从 2026-11-12T01:34:00Z 起，softCap 外）；seen=24，sentToReview=1（zero-guys，同时命中 MEN_GIWA_LZ），admitted=1，skipped=23
- discordPeekDeferred: true（DC 不登录）
- DS: deepseek-flash thinking-on，成功；未走 dsFallback。新卡 focus 为 false。未编造 CA/官号/官网。
- LE2H2: LE2H1 近乎全是 @useCashme 发币确认帖，另开一次排除 CashMe 的 must 查询（非同号重读）。仅 @hoodicorns 有帖（教学/spotlight，非新窗口）。

## 可操作 / 通知

1. **Clause Protocol（@clause_protocol）** — **新收录**，免费 LIVE，le2h=true（官帖 09:19:15 CST，窗至约 11:19 CST），score 74。官号 2026-11-01T20:38:28Z 创建，0 粉、3 帖。官帖宣布 Clause Genesis is LIVE：7777 枚只付 gas，锁定 $PRVS 空投权，每钱包最多 2，12 月 12 日关闭；需 Binance Agent ID，经 MCP 做 EIP-712 签名铸造（不是无门槛公开 mint）。官网 https://clauseprotocol.fun/ 与官号互核通过。链上约 09:43 CST：ClauseGenesis `0xf3F81bEe33DA02324F63385F64f79C1711511181` name=Clause Genesis / CGEN，totalMinted=1、remainingSupply=7776、MAX_SUPPLY=7777、MAX_PER_WALLET=2；ClauseMint `0xEAC70a9AD66B357855bc7d896364BE9a53fB9fcb` isMintLive=true、paused=false、closed=false，mintStart=2026-11-13 01:38:52 CST、mintEnd=2026-12-13 01:38:52 CST，maxMintsPerHour=400。合约在 01:38 CST 已打开但仅铸 1 枚，按官宣计 ≤2h。合约均为站点/MCP 提供，未独立审计。进 userFollowWatch + freeMintWatch + bnAgentWatch + agentPadWatch。本号不自动 mint。
2. **Zero Guys（@ZeroGuysNFT）** — **新收录**，免费 WL 登记，le2h=false，score 51。官网 https://www.zeroguys.fun/ twitter:site=@ZeroGuysNFT，与官号互核。官号 2026-11-10T11:35:07Z 创建，5089 粉、仅 7 帖，刷粉风险高。站点：供 3444，铸造 2026-11-30 时间 TBA，价格 TBD；WL 需关注转评并标记好友、提交 EVM 钱包。官宣帖（站点给出，未另开 X 重读）https://x.com/ZeroGuysNFT/status/2120845780219232332。自称 LayerZero / Zero Chain 首套 NFT，与官方 LZ 关系未独立核实。本轮经 MEN_GIWA_LZ 与静默 LZ mentions 收入（官宣不在近 30 分钟窗内）。无 CA。进 userFollowWatch + freeMintWatch + layerZeroWatch。免费登记即使 score<70 也必须提醒。
3. **Zodiac Fortune（@ZodiacFortune_N）** — 已有卡，仍免费 LIVE，le2h=true（约至 10:04 CST）。链上 09:35 CST：mintOpen=true，remainingFree 124→56，totalMinted 209→277/3333，paidPrice=0.0005 BNB。官网 https://zodiac-fortune-dp8.pages.dev/ ，NFT `0x3293b29372Cdf7F073E544Ce4b0f44777c317000`（站点提供，未独立审计）。
4. **SharkVerse（@sharkverse_）** — 已有卡，仍免费 LIVE，le2h=true（约至 10:36 CST）。链上 09:35 CST：totalMinted 仍为 20/4444，paused=false。官网 https://sharkverse-zeta.vercel.app/ ，NFT `0x7f68011aFF2766dCA686A741dcE68418446ddF99`（未独立审计）。同模板风险仍在。
5. **Arctic Bear（@arcticbear_nft）** — 已有卡，仍免费 LIVE，le2h=true（约至 10:02 CST）。链上已铸 48→54/5555，freeMinted=54，forgeLive=true。paused() 仍 revert，因铸数继续增加按未暂停处理。官网 https://arcticbear.fun/ 。同模板风险仍在。
6. **JPEG Monkes（@jpegmonkes）** — 已有卡，免费窗口仍至约 10:30 CST（≤2h）。OpenSea supply 992→1034、owners 744→758、sales 1079→1148、floor 约 0.0019 ETH。CA `0x7ef4b5f6384e0f2030c2768e60338f4c2cf68f96`（robinhood，未独立审计）。
7. **CashMe（@useCashme）** — 已有卡，发射台仍 LIVE。按首条官宣 08:30 CST 起算，≤2h 至约 10:30 CST。粉丝 19→21。不是免费铸造。官网 https://usecashme.fun/ 。

## 仍在跟（非 ≤2h）

- Agent Cat：仍为预告，官网 Connect 仍写 COMING SOON，OpenSea supply=0，开铸仍为 11-14 21:00 CST。
- hood-terminals：付费公售仍 LIVE，OS 527/777，floor 约 0.001 ETH，sales 641，owners 354。本窗为教学/spotlight 帖，非新窗口。
- boatn-fish：付费 Genesis 仍 LIVE，583/2222，wallets 44，现价约 0.01874 SOL。
- polyrob：LE2H2 未见新官帖；仍按 08:03 CST 官帖，20:00 CST 白名单锁定、22:00 CST 开铸，距开铸约 12.2h。
- clover-rh：付费已 LIVE，OS supply 888、owners 505、floor 约 0.00243 ETH，非新窗口。
- batterydotfun / raeto / Ape_CityRH：本窗未见新官帖，维持原记录。
- play-pixelora：官网 twitter:site 仍为 @PlayPixelora（已在库）。本轮出现的 @pixelorafun（2 粉/4 帖、2019 年号）发类似 2222 WL 内容，视为小号/仿号，不另建卡。
- QUBITFOX（https://qubitfox.pages.dev/）：链上 09:35 CST 读站点 NFT `0x7a2381308B2425D773713A6205732EE8310a9B83`：mintOpen=true、totalSupply 131→138/3333。仍搜不到官推，**未建卡**。同模板克隆风险高。

## 本轮 skip（不够早期 / 非新机会 / 缺官推）

- QUBITFOX / VINECACHE（vinecache.pages.dev，仅推广号 @MaHaDi71Dm，无官推，模板同 QUBITFOX）：无官推，不建卡。
- AGENT CORE / ACORE：同 R1741，站点无官推，未建卡。
- @HOSTPAY_SOL：2026-09-30 创建、59 粉、123 帖，R1741 已判不够早期，本轮不再建卡。
- ignition-rh、hypercell、trippi、memepithq、plunderport：已在库。
- 关键词/mentions 路人、CashMe 发币确认帖未另建卡。

## 其它

- 本号不自动 mint（打新仍交 BAW 打新号）。
- 面板：https://reboot7454.github.io/early-scout/
- docsSynced=true
- 新卡 2、candidates 4110；UF accounts 1577（+@clause_protocol +@ZeroGuysNFT）
- watch-bug：R1741 新卡 agent-cat 已在 UF/freeMint accounts，但未写入 candidateIds，本轮补进。
