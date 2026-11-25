# Early-scout R2191 结果

执行器只在 box 上工作，未改 /workspace/early-scout/data.json，未 commit / push。仓库仍停在 13079fd（R2190）。本轮产物在 /tmp/r2191/，供 parent apply、提交 data.json + docs/data.json + RESULT_R2191.md，并决定推送。

开火约 2026-11-25 18:32 CST（Asia/Shanghai）。lastScout 源数据 2026-11-25 18:16:25 CST。常规增量轮，不是 08:00 CST 后首轮全量补扫（lastFullAfterReset=R2170）。dry-run lastScout=2026-11-25 18:51:45 CST。

## X 额度与预算

- 第一笔 UF1 后 remainingToday=422 / 1000。因此 remainingBefore=423/1000，与预期一致。
- `python3 /workspace/early-scout/scripts/x_budget.py` 建议 mode=pace、softCap=18、minSpend=18、silentCap=2。
- **覆盖**：remaining ≫ 200，且用户禁止额度充足时砍栏，本轮仍按 queries.json 完整增量执行（与 R2185–R2190 相同）。
- 实际：xReads=26（main 25 + silent 1），remainingAfter=397/1000。无重复查询、无探索性加读、无分页。search_users 仍不可用。跳过已知 NF @starx_xlayer，未重试。
- 全部 26 次搜索均成功写入 /tmp/r2191/x_raw/，errors=[]。部分 inline 结果无 Cursor asset，已重建为结构化 x_raw（`_source=inline_reconstruct`），字段足够 flatten。

## 搜索执行

计划顺序已全部跑完一次：UF1/UF2 → MUST_WIN / MUST_WIN2 / MUST_WIN3 → MUST_OFF → KW_LZ/TAPE/GIWA/DOGE/BTC/STARK/MINT/MINE/PAD/GO/ELY/GAPS → MEN_PADS/MEN_GIWA/MEN_TAPE/MEN_LZ/MEN_ELY → SILENT_PAD。

30m 独立 KW 命中：LZ=8、TAPE=25、GIWA=25、DOGE=5、BTC=4、STARK=2、MINT=25、MINE=0、PAD=25、GO=25、ELY=6、GAPS=14。

**瘦栏 24h 回填**（仅 30m 独立 KW <5，每栏最多 +1）：

- 已跑：KW_BTC_24（25）、KW_STARK_24（25）。
- 未跑：KW_LZ_24（8≥5）、KW_TAPE_24（25≥5）、KW_GIWA_24（25≥5）、KW_DOGE_24（5≥5）。
- MINE=0 但是核心栏，未加 24h。

UF 软刷：cursor 1611 @HubrixRH，50 户至 @Orbyt3d，wrap=false，total 源 2402 / dry-run 后 2404（新挂 @deMinersNft、@AnthroposAgents）；下轮 1661 @sonnaagent。本分片无已知 NF。UF1=2、UF2=0。本轮无 UF3。

MUST：MUST_WIN / MUST_WIN2 / MUST_WIN3 均 25 触顶；MUST_OFF=3。MUST_OFF 已跳过已知 NF @starx_xlayer，未重试。本轮 MUST_WIN2 见到 @TheJacket_NVDA 供应削减官帖。

Mentions 本轮：pads-rest（14）/ GIWA（25 触顶）/ Tape（14）/ LayerZero-24h（25 触顶）/ Elysium-rest（24）。下轮应轮换 DogeEVM / BTC / Starknet / squeek / STARX。

静号：台子/Meme（2191 % 11 = 2），SILENT_PAD 24h keyword fallback（search_users 不可用），25 帖触顶，不占 softCap。下轮 silent：GO盘。

## 关键核验

### The Jacket @TheJacket_NVDA — 供应削减 + 公售已核到付费（实质变化，须点名）

官帖 2026-11-25 18:23:13 CST（https://x.com/TheJacket_NVDA/status/2125535772678004922）：Mint is open；The Jacket supply: 4,444 → 777；仍 Free for holders of Rebelkin / Argonauts / Vaultlings / Quotrons404。

公开 OpenSea（https://opensea.io/collection/the-jacket-man/overview 及 api.opensea.io）：

- drop.mintStatus=MINTING。SIGNED_PRESALE / Allowlist（label: official-rebelkin, argonauts, vaultlings, quotrons404）：2026-11-25 18:00:56–18:05:56 CST，每钱包 1，价格 0 ETH。PUBLIC_SALE / Public stage：2026-11-25 18:05:56 CST 至 2026-12-02 18:05:56 CST，每钱包 20，价格 0.0003 ETH（约 $0.49），当前 activeDropStage 为公售。
- 合约仍是 0x655d13c73ce062e95907e68db43cb39c6d11106a（Robinhood Chain），twitterUsername=TheJacket_NVDA。
- 本轮多次核验：collection API 最新 totalSupply/uniqueItemCount=170；overview/页面较早快照 164/777（remainingSupply=613）；更早一次 API 为 160。owners 约 120，地板仍 1.50 USDG，sales 约 175。1.50 USDG 是地板不是铸造价。
- 相对 R2190 的 156/4444：供应官宣削减、公售单价已核到（不能再把公售写成免费）、已铸约 170/777。这是必须点名的实质变化，不是“仍在 LIVE”的重复提醒。持有人名单价仍为 0 ETH。本号不自动 mint。已保持 freeMintWatch。

### deMiners @deMinersNft — 新收录，OG list 免费 mint 已 LIVE（须点名）

官号建号 2026-11-23 23:25:43 CST，18 粉 / following 12 / 11 帖，资料栏 https://deminers.xyz/ 。本轮该官号自己没有出现在雷达返回的帖子里，是被 KW_MINT 第三方 @Pkasiou 18:34:32 CST 点到（称 let’s mint this miners for free）；不把第三方“免费”当作官方口径。

官网 HTTPS 200，Phase 1 PFP、Robinhood Chain、3,333 miners，正文未写出铸造单价。公开 OpenSea collection/deminers：twitterUsername=deMinersNft，合约 0xfd474027f475506b24d9f7cf36fa519c93fff80f，drop.mintStatus=MINTING。

SeaDrop 三阶段（CST）：

1. Team reserve：2026-11-25 04:00:04–04:15:04 CST，每钱包 100，本阶段上限 100，0 ETH。
2. OG list（当前 activeDropStage）：2026-11-25 04:15:04 CST 至 2026-11-25 22:30:04 CST，每钱包 3，本阶段上限 2000，0 ETH（免费）。
3. Public sale：2026-11-25 22:30:04 CST 至 2026-11-27 22:30:04 CST，每钱包 5，0.0002 ETH（约 $0.33），不是免费。

本轮 overview 快照约 468/3333（collection API 稍早见 465），持有约 121–122，地板 0.0005 ETH。OG 名单免费 mint 已 LIVE，必须点名；公售尚未开始，未到公售首次 ≤2h（20:30 CST 才进入），不要提前把公售说成免费。DeepSeek score=78，focus=false。已挂 userFollowWatch + freeMintWatch。本号不自动 mint。

### Anthropos @AnthroposAgents — 新收录，不是免费 mint

官号建号 2026-11-24 19:01:44 CST，23 粉 / 7 帖，资料栏 https://anthropos.lol。官帖 2026-11-25 12:43:28 CST（https://x.com/AnthroposAgents/status/2125450270331289806）称可在 Flap 上 swap/bridge/send/launch，风险操作需人工批准。官网 HTTPS 200，是面向 Claude 代理的 BNB Chain MCP 工具，不是铸造窗。资料栏指向官网；本轮未核到官网页内回链官推。DeepSeek score=55，focus=false。已挂 userFollowWatch + flapPadWatch。不是免费 mint / 免费登记。

### ORIPA @oripaxyz — 不重推

MUST 再见到同一则 16:43:16 CST 官帖：Rips open tonight, 8 PM GMT+8，窗口仍 2026-11-25 20:00 CST，无改期。首次 ≤2h 已在 R2190 发出。不是免费 mint。卡片 le2h 保持 true，不重推。

### ZeroGate @ZeroGate0G / Helipaid @usehelipaid — 不重推

ZeroGate 本轮仍称已 live，CA 不变。18:32:54 CST 回复 @aaaliuyan112233「Launch is failed because of snipers」是对用户发币失败的回复，不能据此认定平台下线。Helipaid 本轮续发产品说明，无改链/改价/新的免费窗。二者 R2190 已提醒，本轮不重推。都不是免费 mint。

### Ugly Puggies @uglypuggies — 尚未进入 2h，不提前告警

官方开闸仍约 2026-11-25 21:00 CST（13:00 UTC）。2 小时窗口 19:00 CST 才开始。dry-run 收尾 2026-11-25 18:51:45 CST，尚未到 19:00 CST，不提前告警。17:54:26 CST 官帖只是抽奖获奖名单，不是开铸确认。自称免费 mint（777，Robinhood），不是已确认 LIVE。卡片 le2h 仍为 false。

### TRIFORGE @TriForgeAgent

公共 BSC RPC（约 2026-11-25 18:37:49 CST，https://bsc-dataseed.binance.org/）：Forge Keys 免费铸仍 LIVE 未暂停，356/3333→359/3333，小幅增加，只更新卡片不重推。付费预售仍开，lpTotalMinted=0，lpTotalPaid=0；claimsOpen=true、totalClaimed=3；miningShares=6；tokenTradingEnabled=false。本轮 MUST 返回中未见该官号新帖。

### 其它库内（不重推）

Lamoryant 18:07:58 CST 官帖称 OG Freemint spot 将被加入官方平台 mint list（涉及 reveal），不是新确认的已开铸 LIVE。Owltopia 称在做合作网站、将登陆 Robinhood，无新开铸窗。

## 看见但未收录

DeepSeek（deepseek-flash，thinking on）打分后 skip：

- **IndexIt（@indexitcash / https://indexit.cash/）**：Flap 上的指数币发射台，官网与简介一致并给出 CA 0x7ebd34bd7479f2e5b38dac8593b038fd70137777。建号约 28 天、913 粉，早期窗口偏晚，本轮未核 CA 流动性。score=52，admit=false。不是免费 mint。
- **OUTLAWSxNFT（@OUTLAWSxNFT）**：简介自称 2026-11-27 21:30 CST（Nov 27 1:30 PM UTC）在 OpenSea 免费 mint 6,666 份。OpenSea slug outlawsxnft 合约 0xf5be4d8c1ae8f281297dedf337e93940e8a59b81，本轮 supply=0，twitterUsername 为空，无独立官网，账户为 2022 年老号。与库内 OutlawHood / Elysium Outlaws 不是同一项目。互证弱，admit=false。

未送审或直接跳过：@axtapi（当天新号，AI API「$3 FREE credit」，不是打新/发射台）；@axemoraxyz（当天新号、0 粉、无官网，Solana 发射演练工具，过瘦）；@kajiDarmin 转推的 Agent Seal 已在库（@Handln）；@GIWABYUPBIT 指向已入库的 giwa.markets / @GIWALAUNCHPAD；@officialbunnyos（Bunny Open Studio，Sep 2025 老号，「this week」登陆 Base，日期含糊）。静号未见需单列的新官号。

## 库内其它更新（不重推）

- The Jacket / deMiners / Anthropos / TRIFORGE / ORIPA / ZeroGate / Helipaid / Ugly Puggies / Lamoryant 卡片已按上文更新或补记。
- UF 软刷游标前进至 1661 @sonnaagent，wrap=false。
- discordPeekDeferred=true：本轮 parent 已同一轮补 Peek。box Chrome 打开 #alpha-1 后立刻遇到 Discord 登录墙（Welcome back / Email or Phone / Password / Log In / QR / passkey），attemptedAt=2026-11-25 18:33:06 CST，loginOk=false，loginWall=true，四频道均未翻。lastSeen 保持 2026-11-23 22:56（alpha-1 22:19 / alpha-1-backup 22:29 / smart-accounts-tracker 22:56 / alpha-3 22:55）。未填写凭证、未点登录。积压仍待登录后续翻。

## Notify

notify=true。

alertMessage：

【R2191】The Jacket @TheJacket_NVDA 库内供应 4444→777 已核到公售付费 0.0003 ETH，非免费、持有人名单仍免费；新收录 deMiners @deMinersNft 的 OG list 免费 mint 已 LIVE（Robinhood Chain，约 468/3333，限 3/钱包），Anthropos @AnthroposAgents 不是免费 mint；面板：https://reboot7454.github.io/early-scout/

DeepSeek 原文使用 PANEL 占位，已替换为面板 URL，并补上 @handles 与 deMiners 约 468/3333，未改判断口径。dsFallback=false。

## 产物

- /tmp/r2191/data.json（dry-run，APPLY_DRY_RUN=1，源 /tmp/r2191/data.json.src）
- /tmp/r2191/apply_r2191.py、apply_flags.json、notify.json、new_cards.json
- /tmp/r2191/x_raw/（26 个搜索）、x_usage.json、x_flat.json、x_all.json
- /tmp/r2191/unknowns_raw.json、must_posts.json、ds_payload.json、ds_score.json、ds_alert.json
- /tmp/r2191/triforge_rpc.json、sites/（The Jacket / deMiners OpenSea 与官网快照）

执行器未修改 git 仓库，也未写入 /workspace/early-scout/data.json。
