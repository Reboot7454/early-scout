# RESULT R1910

- time: **2026-11-16 18:12 CST**
- mode: **pace**（独立例行，非第二次 post-reset-full；remaining>200，十栏仍跑全）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- notify: **true**
- newThisRound: 无
- le2h: **bombshell-cats**（Art Dealers 白名单免费 mint 11-16 20:00 CST，首次进入 ≤2h）
- dsFallback: false
- xReads: **26**（main 25 + silent 1）
- remainingBefore: **544** → remaining: **518**
- softCap 18 / minSpend 18 / silentCap 2

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1909）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常节流；本轮 `x_budget.py` 判 pace（remainingBefore=544），不强制第二次 post-reset-full。因 remaining>200，按用户「额度够时不得砍栏」跑全十栏 KW、mentions 4 组与 THIN official。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent GIWA 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖 / 不替用户预存。

## X 额度与查询

remainingBefore=544（首读 UF1 后 remaining 543，按 left_after_first+1 还原）。26 次读取后 remaining=518。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=25，打满 minSpend 18，超过 softCap 18（+7）：MUST 优先号+窗口号在 2 片装不下，增加 MUST3；THIN official 去重后 108 号需要 5 片。silent 1 次在 softCap 外。10 条被截断的 write_to_file 预览已从 assets 完整副本恢复，未重拉 X。

- UF1–UF2：0-based 1150 MendlingsNFT 起 packed 2 片 kept 50（25+25），wrap=false，walkScanned 50。NF_skip 0。firstKept MendlingsNFT，lastKept Fountainbnb。next 1200 Elytrafi_。
- MUST1：24 个 live/窗口号；MUST2：25 个（含 bitmaxdog 与优先号前段）；MUST3：5 个（bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer）。mustSkip=[escape_hub]（本 UF 分片已覆盖，未重复读）。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 108 号 5 片全读（26+25+26+27+4）。UF1 / MUST3 / THIN1 / KW_MINE / MEN_MINE / MEN_BN 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T08:30:00Z（约 1.5h，与 R1909 07:30Z 重叠）；KW 与 mentions 自 2026-11-16T08:00:00Z（约 2h）；silent 自 2026-11-15T10:00:00Z（约 24h）。
- mentions 4 组轮换：LayerZero 6 / Elysium+kinetiq 25 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 0。
- silent：1910%11=7 GIWA，SILENT_MEN 1 次 25 帖，短名单 20 个均为 Ammora/GIWA 测试网任务号，送审 0、录取 0。下一轮 lane=DogeEVM。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 43；在库作者 22；新作者 175，短名单保留 96，跳过 79，very_new 4。

栏 rc：UF1 0，UF2 6，MUST1 2，MUST2 22，MUST3 0，THIN1 0，THIN2 6，THIN3 1，THIN4 3，THIN5 1，KW_LZ 1，KW_TAPE 25，KW_GIWA 25，KW_DOGE 17，KW_BTC 17，KW_SN 5，KW_MINT 25，KW_MINE 0，KW_PAD 25，KW_GO 5，KW_ELY 25，MEN_LZ 6，MEN_ELY 25，MEN_MINE 0，MEN_BN 0，SILENT_MEN 25。parse_errors=[]。

## 收录与在库

新收录 0 张。

在库刷新：

- bombshell-cats：@1KArtGallery Art Dealers 白名单免费 mint 11-16 20:00 CST 首次进入 ≤2h（限已登记 112 钱包、最多 3/钱包）。公售仍为 11-17 20:00 CST 起 0.0003 ETH、3/钱包。不是公开无门槛免费 mint。本轮提醒。本号不自动 mint。
- bonkagent：@Bonkagent_ 18:02 CST 官帖（https://x.com/Bonkagent_/status/2122268978592596122）首次公布新一轮 $FIST 铸造：11-17 15:00 CST 在 https://fistagent.fun/（本轮 HTTP 200）开启。前 1,000 份免费（每地址 1 份），全部铸完后剩余 9,000 份付费 0.005 BNB/份（每地址 10 份），总量 10,000 份；用币安 App 扫码连接 Agent 钱包。站点写铸造合约与 FIST 代币「待配置」，CA 尚未公布。尚未 ≤2h。本轮按补公布具体时刻提醒。本号不自动 mint。同系列旧卡 fistagent 的官号 @FISTAgent 仍为 suspended，入口以 @Bonkagent_ / fistagent.fun 为准。
- ephemeral-eth：17:25 CST 称 Early Access 时刻先在 TG 公布，上线仍是 11-16 23:00 CST，R1897 已提醒，尚未 ≤2h，不重推。
- spiritsrh / bitmaxdog：本窗再见 R1909 已提醒的官帖，不重推。
- inklegions：17:08 CST 回复空投入口，免费 mint 仍为 11-17 03:00 CST，R1908 已记，尚未 ≤2h，不重推。
- microfrens / wrapped-eth / zyro / owlgatecli / packswap / pingpay：互动、产品续更或销毁说明，无新开窗，不重推。

尚未 ≤2h、无改期、不重推：dotBots Round 2 销售 11-16 21:00 CST；escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；MicroFrens reveal 11-17 01:00 CST（mint 已完成）；hood-bitz 11-17 02:00 / 06:00 CST；Pantheon AGI 11-17 02:47 CST；Ink Legions 免费 mint 11-17 03:00 CST；FIST / Bonkagent 11-17 15:00 CST；Bombshell Cats 公售 11-17 20:00 CST；boxcars 预售 11-17 21:00 CST；HoodTurtleRH mint 11-17 22:15 CST；hoodfrenz 11-17 23:00 CST；SpiritsRH 免费 mint 11-20 00:00 CST。

## 跳过（要点）

- 无新官号可建卡。DeepSeek 评审后未录取（admits=[]）。dsFallback=false。
- @FibDipFun：0.09 天、14 粉，站点 fibdip.fun 是 bonding-curve 回测/交易工具，本窗只回复 @Helius，不是打新官号。
- @NHPX_：已上线的 Elysium DeFi/swap 网关（nhpxswap.site），本窗只是回复，无新 mint 官宣。
- @ebunoluwaabz：只转发 @Hoodfrenz GTD 赠票。
- @memecoinsoul / @furbi59360：与 R1909 相同原因跳过（已上线代币 / 市场推广）。
- 其余短名单多为 Ammora/GIWA 测试网任务、DogeOS 互动，或已在库项目转发。

## 覆盖与债

- 十栏关键词：跑全。laneReads 十一条均为 true。
- userFollowWatch：本分片刷完，wrap=false，next 1200 Elytrafi_。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

true。无新收录卡。Bombshell Cats Art Dealers 白名单免费 mint 首次进入 ≤2h；@Bonkagent_ 首次公布 $FIST 新一轮 11-17 15:00 CST 铸造（前 1,000 份免费，合约待配置）。推送成功。详见 https://reboot7454.github.io/early-scout/ 。本号不自动打、不替用户存。
