# RESULT R1906

- time: 2026-11-16 15:42 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮继续正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 25（main 24 + silent 1）
- remaining: 645 → 620 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: true
- newIds: （无）
- le2hIds: tapeai
- dsFallback: false

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1905）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常 ample；本轮按 `x_budget.py` 判 ample（remainingBefore=645），不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent GO盘栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖。

## X 额度与查询

remainingBefore=645（首读后 remaining 644，按 left_after_first+1 还原）。25 次读取后 remaining=620。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。silent 1 次在 softCap 外。

- UF1–UF2：0-based 940 Standssocial 起 packed 2 片 kept 49（24+25），wrap=false，walkScanned 54。NF_skip 5，全部已在列（bianjiayou / kpin_ai / LostGodsOnRH / topaaafun / ripstackfun），无新发现；其中 kpin_ai / LostGodsOnRH / ripstackfun 已在 uf.NF_skip，本轮同步写入 meta.NF_skip。firstKept Standssocial，lastKept hookium。next 994 velom33。
- MUST1：24 个 live/窗口号；MUST2：24 个。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。theoutcomers 为等待名单卡、无定时窗口，未自动加入 MUST。
- THIN official：去重后 105 号 5 片全读（26+25+27+26+1）。THIN1 / THIN3 / THIN5 / MEN_MINE 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T06:00:00Z（约 1.5h，与 R1905 05:30Z 重叠）；KW 与 mentions 自 2026-11-16T05:30:00Z（约 2h）；silent 自 2026-11-15T07:30:00Z（约 24h）。
- mentions 4 组轮换：LayerZero 6 / Elysium+kinetiq 25 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 2。
- silent：1906%11=3 GO盘，SILENT_MEN 1 次 10 帖，未从该栏录取。下一轮 lane=LayerZero。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 33；在库作者 20；新作者 169，短名单保留 95，跳过 74。9 条被截断的 write_to_file 预览已从 assets 完整副本恢复，未重拉 X。

## 收录与在库

新收录 0 张。

在库首次确认开铸（重推）：

- brawler-rebels：@BrawlerRebels 14:00 CST 官帖（https://x.com/BrawlerRebels/status/2122208046931746818）称 day 2、约 35% minted，art reveal 已完成并号召去 mint。官网 https://brawlerrebels.xyz/ HTTP 200，写 PUBLIC MINT IS LIVE，但 509/2222 是页面里的 OpenSea 截图快照，非实时。本轮抓取 OpenSea 合集 https://opensea.io/collection/brawler-rebels ：Robinhood Chain SeaDrop，合约 0xe035e407a2a8836c094088b4ac31d5d041f1c2cc，页面写 Minting now，708/2222（余 1514）。TINYBUDS HOLDER CLAIM 免费签名预售仅 2026-11-14 21:00–22:00 CST（已结束，1/钱包）；公售 0.0005 ETH，自 2026-11-14 22:00 CST 至 2026-11-24 22:00 CST，仍在窗内。库内自 R1230 起仍写 mint soon，本轮 UF 才刷到该官号，属首次确认已开铸。非新收录，公售不是免费，也不是新的 ≤2h 窗口。因首次确认可操作开铸，notify=true。本号不自动 mint。

在库刷新（均不重推）：

- tapeai：同一份已提醒的 BEM 预存窗口仍有效（2026-11-16 16:00 CST），现距窗口仍 ≤2h，预存尚未开始。@tapeupio 14:01 CST 仍是同一条已记录官帖，时刻未改、也未见已开始确认，不重推。le2h 保持 true。
- unicorn-grand-prix：复查官网 HTTP 200，Date 仍 to be announced；白名单页本轮 HTTP 200，正文仍写 “The whitelist opens soon” / “not reachable right now”，不是首次可提交开放。14:02 CST 仍是同一条门槛重申。
- gloopix：15:02 CST 官帖称正在审核评论区地址，获 likes 可拿 GTD 名额。仍无开铸时刻、无官网、无已核验 CA；此前已在征集 EVM / Collab DM，不是新的可提交表单或 mint 开窗，不重推。
- wrapped-eth：15:17 CST 新帖提醒创建 wrapper 前要先确定费用分成与受益人（创建时锁定）。14:50 CST 费率图更正已在 R1905 记录。属已上线产品说明，不重推。

产品续更、同一已开闸入口不重推：Creedo / PingPay / PaidTok / Zyro / Bitsigil（游戏上线日 coming soon，无日期）/ ozero（同一条 Base Sepolia 测试网宣传）/ Vorda（GIWA Sepolia Missions）/ VoidCash（已上线隐私产品说明）/ Tapemonkey（本地原型技术更新）/ tapeupio TapeOut Builder Camp。inklegions 14:49 CST 回复不写成 mint 已开始，库内免费 mint 仍是 11-17 03:00 CST，尚未 ≤2h。

尚未 ≤2h、无改期、不重推：Bombshell Cats AL 11-16 20:00 CST；escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；hood-bitz 11-17 02:00 / 06:00 CST；Pantheon AGI 11-17 02:47 CST；Ink Legions 免费 mint 11-17 03:00 CST；hooja-fun UNVAULT 仅有日期无时刻；MicroFrens reveal 11-17 01:00 CST（mint 已完成）；dotBots Round 2 销售 21:00 CST；HoodTurtleRH mint 11-17 22:15 CST；hoodfrenz 11-17 23:00 CST；boxcars presale 11-17 21:00 CST。

## 跳过（要点）

- 无新官号可建卡。本轮 very_new 号（Imax__8 / Danger_089 / Evermoreglowi / andriussulcas99）均为评论、转帖或 Ammora/GIWA 宣传号。
- KairoCollective / Web3Connects 等宣传 Elysium Rigs mine-to-mint：已在库 elysium-rigs，属第三方转发，不新建卡。
- SamiTrades_ 转述 RGBHorse / DarkHorse 210M $RGB 免费铸造：RGBHorse 已在库，本窗官号 0 帖，不按官方 LIVE 通知。
- Mopesnft / CompanionsWfit / Audacity Corp / SyndicateRHC / PlayPixelora / VitrumFalcons 等免费 mint / GTD 均为已在库项目或第三方转帖模板，不是本轮官方确认开窗。
- 多个 Ammora/GIWA 评论搬运号，以及 DogeOS / TapeOut / Elysium / Pad 评论向 KOL：不是新官号。

## 覆盖与债

- 十栏关键词：跑全。
- userFollowWatch：本分片刷完，wrap=false，next 994 velom33。brawler-rebels 已在该 Watch 与 freeMintWatch，无需补列入。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

true。Brawler Rebels（@BrawlerRebels）确认已开铸：公开销售并非免费，价格为 0.0005 ETH，本轮 OpenSea 显示 708/2222，已进行约两天。官网也标注 PUBLIC MINT IS LIVE，公开销售窗口持续至 2026-11-24 22:00 CST。详情和进度请看 https://reboot7454.github.io/early-scout/ ，库内卡片已从 mint soon 更新为已开铸。

TapeAI 同一份已提醒的 ≤2h 预存窗口不重推。Unicorn 白名单仍不可提交；Gloopix 评论区 GTD 不是新表单入口；其余无首次可操作变化。
