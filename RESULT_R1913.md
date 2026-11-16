# RESULT R1913

- time: **2026-11-16 21:13 CST**
- mode: **pace**（独立例行，非第二次 post-reset-full；remaining>200，十栏仍跑全）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- notify: **true**
- newThisRound: **squoze**（@squozedotfun，Solana 股票代币配对 memecoin 发射台，站点可进但 Trading halted，overall 54，按真新收录提醒；不是免费 mint LIVE）
- le2h: **escapehub**（Launchpad 11-16 23:00 CST，首次进入 ≤2h，本轮提醒）；**ephemeral-eth**（Early Access 11-16 23:00 CST，首次进入 ≤2h，本轮提醒）；**bombshell-cats**（Art Dealers 白名单 11-16 20:00 CST，R1910 已提醒，不重推）；**dotbots-ai**（Round 2 销售 11-16 21:00 CST，R1911 已提醒，不重推）
- dsFallback: false
- xReads: **26**（main 25 + silent 1）
- remainingBefore: **465** → remaining: **439**
- softCap 22 / minSpend 18 / silentCap 2

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1912）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常节流；本轮 `x_budget.py` 判 pace（remainingBefore=465，softCap 22），不强制第二次 post-reset-full。因 remaining>200，按用户「额度够时不得砍栏」跑全十栏 KW、mentions 4 组与 THIN official。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent Starknet 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖 / 不替用户预存。

## X 额度与查询

remainingBefore=465（首读后 remaining 464，按 left_after_first+1 还原）。26 次读取后 remaining=439。同一计划 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=25，实际主扫 25，无额外补读。打满 minSpend 18，超过 softCap 22：MUST 优先号+窗口号+PoolFun_app 在 2 片装不下，增加 MUST3；THIN official 去重后 108 号需要 5 片。silent 1 次在 softCap 外。被截断的 write_to_file 预览已从 assets 完整副本按 newest_id 恢复，未重拉 X。

- UF1–UF2：0-based 1298 tryspreadly 起 packed 2 片 kept 50（25+25），wrap=false，walkScanned 50。NF_skip 0。firstKept tryspreadly，lastKept wilmacartemv2f。next 1348 payolaads。
- MUST1：24 个 live/窗口号；MUST2：25 个（含 Fistagent_）；MUST3：8 个（PoolFun_app / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 108 号 5 片全读（26+25+26+27+4）。THIN5 / MEN_BTC / MEN_SN_DOGE 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T11:30:00Z（约 1.5h，与 R1912 10:30Z 重叠）；KW 与 mentions 自 2026-11-16T11:00:00Z（约 2h）；silent 自 2026-11-15T13:00:00Z（约 24h）。
- mentions 4 组轮换：Tape 9 / GIWA 1 / BTC 0 / Starknet+DogeEVM 0。
- silent：1913%11=10 Starknet，SILENT_MEN 1 次 2 帖，为已在库 HOKORI_QUANTUM 带 @starknet launchpad 字样，送审 0、录取 0。下一轮 lane=打新。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 60；在库作者 31；新作者 140，短名单保留 73，跳过 67，very_new 2。

栏 rc：UF1 1，UF2 1，MUST1 13，MUST2 24，MUST3 1，THIN1 2，THIN2 7，THIN3 1，THIN4 2，THIN5 0，KW_LZ 1，KW_TAPE 25，KW_GIWA 25，KW_DOGE 25，KW_BTC 16，KW_SN 11，KW_MINT 25，KW_MINE 1，KW_PAD 24，KW_GO 5，KW_ELY 25，MEN_TAPE 9，MEN_GIWA 1，MEN_BTC 0，MEN_SN_DOGE 0，SILENT_MEN 2。parse_errors 仅截断预览伪栏（已用完整副本，不计入正式 rc）。

## 收录与在库

新收录 1 张：

- squoze（@squozedotfun）：20:59 CST 官帖宣布玩法。官网 https://squoze.fun/ HTTP 200，与 bio/t.co 一致。选 NVDAx/TSLAx/AAPLx 等股票代币，发射配对 memecoin，在 Meteora bonding curve 交易，毕业后进 damm v2 pool。建号 2026-11-13 14:18 CST，1 粉 2 帖。站点有 Launch a token / Connect 入口，但页面显示 Trading halted，不是免费 mint LIVE。归台子/Meme，lzVerified=false，focus=false。DeepSeek overall 54（early 93 / actionable 48 / novelty 72 / risk 85）。按真新收录本轮提醒。已写入 userFollowWatch。本号不自动 mint。

在库刷新：

- escapehub：Launchpad 窗口首次进入 ≤2h，仍为 11-16 23:00 CST（15:00 UTC）。本窗无新官帖、档期未改。本轮提醒。本号不自动 mint。
- ephemeral-eth：Early Access 窗口首次进入 ≤2h，仍为 11-16 23:00 CST。20:21 CST 官帖仍称时刻先在 Telegram 公布，档期未改。本轮提醒。本号不自动 mint。
- bombshell-cats：Art Dealers 白名单免费 mint 已过 11-16 20:00 CST 开窗。R1910 已按首次 ≤2h 提醒，档期未改，不重推。公售仍为 11-17 20:00 CST。
- dotbots-ai：Round 2 销售仍为 11-16 21:00 CST，本窗已到点。R1911 已按首次 ≤2h 提醒，无改期，不重推。这是销售窗，不是主网免费 mint。
- bonkagent / Fistagent_：21:05 CST 官帖称 community project is now live，落地为 https://fistagent.fun/ HTTP 200。站点仍写 11-17 15:00 CST 开铸，前 1,000 份免费；铸造合约与代币待配置。官网已开不是铸造已 LIVE，尚未 ≤2h，不重推。
- hoodfrenz：20:01 CST 再预告 mint tomorrow，时刻仍为 11-17 23:00 CST，未改期，尚未 ≤2h，不重推。
- plunderport：本窗再见 20:02 CST 官帖，口径未改（Zero 主网与 ATLAS 11-30），R1912 已记，不重推。
- ozero / poolfun：本窗再见 waitlist / Early Bird 官帖，口径未改，R1912 已提醒，不重推。
- inklegions：19:51 CST 再见 Ink OGs 免费 mint 回复，时刻仍为 11-17 03:00 CST，尚未 ≤2h，不重推。
- agentmarketbnb：20:01 CST 更新 Stall 进度（2,326 / 131 店主），presale 仍至 11-24 19:30 CST，不重推。
- hokori-quantum / TapeAIAgent / GIWALAUNCHPAD：建设、开盘本周公布或 GAME DAY 预告，无新开窗，不重推。

尚未 ≤2h、无改期、不重推：Cipher Syndicate 11-17 00:00 CST；MicroFrens reveal 11-17 01:00 CST（mint 已完成）；hood-bitz 11-17 02:00 / 06:00 CST；Ink Legions 免费 mint 11-17 03:00 CST；FIST / Fistagent_ 11-17 15:00 CST；Bombshell Cats 公售 11-17 20:00 CST；boxcars 预售 11-17 21:00 CST；HoodTurtleRH mint 11-17 22:15 CST；hoodfrenz 11-17 23:00 CST；SpiritsRH 免费 mint 11-20 00:00 CST。

## 跳过（要点）

- DeepSeek 录取 @squozedotfun（dsFallback=false）。
- @AIDROP_fun（aidrop.fun，「AI 天降轮盘」即将开始、0.003 BNB、合约待部署）：与在库官方 AIDROP 平台 @bscaidrop / bsc-aidrop 重名且极易混淆，独立证据不足，按撞名/仿盘风险 skip。
- @FLOORXFOBO：已在库发射台 fobo-fun 上的 $FLOORX 宣传号。
- TwinForge（https://twinforge.surge.sh/ ，CA 0x96d560b1e2b2061c417d8f14D111A4dE7e9680fF）：本轮仍未见官方 Twitter，按「新收录必须有推特」继续不建卡，只作线索。
- 其余短名单多为 GIWA/Ammora Season 2 任务号、Tape/资讯转发或已在库项目互动。

## 覆盖与债

- 十栏关键词：跑全。laneReads 十一条均为 true。
- userFollowWatch：本分片刷完，wrap=false，next 1348 payolaads。新卡 @squozedotfun 已追加进 Watch。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

true。新收录 squoze（真新，站点 Trading halted，不是免费 mint LIVE）；escapehub 与 ephemeral-eth 窗口首次进入 ≤2h。Bombshell Cats 与 dotBots 仍 ≤2h，但此前已提醒、档期未改，不重推。推送成功。详见 https://reboot7454.github.io/early-scout/ 。本号不自动打、不替用户存。
