# RESULT R1911

- time: **2026-11-16 19:11 CST**
- mode: **pace**（独立例行，非第二次 post-reset-full；remaining>200，十栏仍跑全）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- notify: **true**
- newThisRound: 无
- le2h: **dotbots-ai**（Round 2 销售 11-16 21:00 CST，首次进入 ≤2h）；**bombshell-cats**（Art Dealers 白名单免费 mint 11-16 20:00 CST，R1910 已提醒，档期未改，不重推）
- dsFallback: false
- xReads: **26**（main 25 + silent 1）
- remainingBefore: **518** → remaining: **492**
- softCap 18 / minSpend 18 / silentCap 2

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1910）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常节流；本轮 `x_budget.py` 判 pace（remainingBefore=518），不强制第二次 post-reset-full。因 remaining>200，按用户「额度够时不得砍栏」跑全十栏 KW、mentions 4 组与 THIN official。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent DogeEVM 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖 / 不替用户预存。

## X 额度与查询

remainingBefore=518（首读 UF1 后 remaining 517，按 left_after_first+1 还原）。26 次读取后 remaining=492。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=25，打满 minSpend 18，超过 softCap 18（+7）：MUST 优先号+窗口号在 2 片装不下，增加 MUST3；THIN official 去重后 107 号需要 5 片。silent 1 次在 softCap 外。9 条被截断的 write_to_file 预览已从 assets 完整副本恢复，未重拉 X。

- UF1–UF2：0-based 1200 Elytrafi_ 起 packed 2 片 kept 48（24+24），wrap=false，walkScanned 48。NF_skip 0。firstKept Elytrafi_，lastKept trenchingdotfun。next 1248 elysianpull。
- MUST1：24 个 live/窗口号；MUST2：25 个（含 bitmaxdog、Bonkagent_ 与优先号 mobster_meme）；MUST3：6 个（machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer）。mustSkip=[Agentlifebnb]（本 UF 分片已覆盖，未重复读）。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 107 号 5 片全读（26+25+26+26+4）。KW_LZ / KW_MINE / THIN3 / MEN_BTC / MEN_SN_DOGE 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T09:30:00Z（约 1.5h，与 R1910 08:30Z 重叠）；KW 与 mentions 自 2026-11-16T09:00:00Z（约 2h）；silent 自 2026-11-15T11:00:00Z（约 24h）。
- mentions 4 组轮换：Tape 11 / GIWA 6 / BTC 0 / Starknet+DogeEVM 0。
- silent：1911%11=8 DogeEVM，SILENT_MEN 1 次 5 帖，主要为已在库 Dogstarter/wowpadlol，送审 0、录取 0。下一轮 lane=BTC。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 45；在库作者 23；新作者 154，短名单保留 85，跳过 69，very_new 8。

栏 rc：UF1 5，UF2 1，MUST1 5，MUST2 22，MUST3 1，THIN1 1，THIN2 3，THIN3 0，THIN4 4，THIN5 1，KW_LZ 0，KW_TAPE 25，KW_GIWA 25，KW_DOGE 15，KW_BTC 14，KW_SN 8，KW_MINT 25，KW_MINE 0，KW_PAD 25，KW_GO 5，KW_ELY 25，MEN_TAPE 11，MEN_GIWA 6，MEN_BTC 0，MEN_SN_DOGE 0，SILENT_MEN 5。parse_errors=[]。

## 收录与在库

新收录 0 张。

在库刷新：

- dotbots-ai：@dotBots_ai Round 2 销售 11-16 21:00 CST（Mon Nov 16 20:00 GMT+7）首次进入 ≤2h。这是销售窗，不是主网免费 mint；Arena Pioneer Cup 测试网杯赛不要当成开铸。本轮未见改期官帖。本轮提醒。本号不自动 mint。
- bombshell-cats：@1KArtGallery Art Dealers 白名单免费 mint 仍为 11-16 20:00 CST，R1910 已按首次 ≤2h 提醒，档期未改，本窗无新官帖，不重推。公售仍为 11-17 20:00 CST 起 0.0003 ETH、3/钱包。不是公开无门槛免费 mint。
- bonkagent：官号已从 @Bonkagent_ 更名为 @Fistagent_（同一账号 user id 4406828415，同一条 18:02 CST 官帖现址 https://x.com/Fistagent_/status/2122268978592596122）。铸造时刻未改：11-17 15:00 CST 在 https://fistagent.fun/（本轮 HTTP 200），前 1,000 份免费；铸造合约与代币仍写「待配置」，尚未 ≤2h。按更名提醒，不当新开铸。本号不自动 mint。同系列旧卡 fistagent 的官号 @FISTAgent 仍为 suspended，入口以 @Fistagent_ / fistagent.fun 为准。
- inklegions：18:26 CST Last call，招募 18:00 CET（11-17 01:00 CST）截止；免费 mint 仍为 20:00 CET / 11-17 03:00 CST，未改期，尚未 ≤2h，不重推。
- ephemeral-eth：18:07 CST 讲 Kaito Lab，上线仍是 11-16 23:00 CST，R1897/R1910 已提醒，尚未 ≤2h，不重推。
- bitmaxdog：18:58 CST 预告邻地合并，属已开铸玩法功能，不重推。
- microfrens / wrapped-eth / zyro / pingpay / agentlifebnb：互动、产品续更、销毁或退款回复，无新开窗，不重推。

尚未 ≤2h、无改期、不重推：escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；MicroFrens reveal 11-17 01:00 CST（mint 已完成）；hood-bitz 11-17 02:00 / 06:00 CST；Ink Legions 免费 mint 11-17 03:00 CST；FIST / Fistagent_ 11-17 15:00 CST；Bombshell Cats 公售 11-17 20:00 CST；boxcars 预售 11-17 21:00 CST；HoodTurtleRH mint 11-17 22:15 CST；hoodfrenz 11-17 23:00 CST；SpiritsRH 免费 mint 11-20 00:00 CST。

## 跳过（要点）

- 无新官号可建卡。DeepSeek 评审后未录取（admits=[]）。dsFallback=false。
- TwinForge（https://twinforge.surge.sh/ ，CA 0x96d560b1e2b2061c417d8f14D111A4dE7e9680fF）：站点+链上核实为免费 LIVE（销售窗 11-16 13:40–11-23 13:40 CST，须持币安 Agent ID，每 ID 前 5 张免费，免费池剩余 1976/2000，已铸 24/5555，付费档已开 0.001 BNB）。站点与短名单均未见官方 Twitter，按「新收录必须有推特」未建卡，只在本轮提醒里作线索。
- @Fistagent_：与已在库 @Bonkagent_ 为同一账号更名，不新建卡。
- @proofofstock：Base/Robinhood 代币化股票核验/MCP 工具，不是打新官号。
- @Troyaagent：$TROYA 已有 CA，本窗为产品界面更新。
- @highbar_capital：Meteora DBC launchpad 已 live。
- @BantayGiwaDog：0 粉新号、无官网，证据过薄。
- @NelaJahanscfz / @DolaJahansh64 / @AriYaN3450 / @princevn36 / @samsumhoca / @jeentekali：Ammora/GIWA 测试网任务或复制文案号。
- @Annak0ox：仅第三方转发 TwinForge。
- 其余短名单多为 DogeOS/Tape/GIWA 互动，或已在库项目转发。

## 覆盖与债

- 十栏关键词：跑全。laneReads 十一条均为 true。
- userFollowWatch：本分片刷完，wrap=false，next 1248 elysianpull。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

true。无新收录卡。dotBots Round 2 销售首次进入 ≤2h；TwinForge 免费 LIVE 线索（无官推未建卡）；@Bonkagent_ 更名为 @Fistagent_（铸造时刻未改）。Bombshell Cats 仍 ≤2h 但 R1910 已提醒、档期未改，不重推。推送成功。详见 https://reboot7454.github.io/early-scout/ 。本号不自动打、不替用户存。
