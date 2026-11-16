# RESULT R1912

- time: **2026-11-16 20:11 CST**
- mode: **pace**（独立例行，非第二次 post-reset-full；remaining>200，十栏仍跑全）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- notify: **true**
- newThisRound: **poolfun**（@PoolFun_app，免费 Early Bird 登记 LIVE，overall 55，按免费登记规则必须提醒）
- le2h: **bombshell-cats**（Art Dealers 白名单免费 mint 11-16 20:00 CST，R1910 已提醒，档期未改，不重推）；**dotbots-ai**（Round 2 销售 11-16 21:00 CST，R1911 已提醒，本窗无改期，不重推）
- 额外提醒：在库 **ozero** 主网 waitlist 首次开放（不是 mint 开窗）
- dsFallback: false
- xReads: **27**（main 26 + silent 1）
- remainingBefore: **492** → remaining: **465**
- softCap 21 / minSpend 18 / silentCap 2

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1911）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常节流；本轮 `x_budget.py` 判 pace（remainingBefore=492，softCap 21），不强制第二次 post-reset-full。因 remaining>200，按用户「额度够时不得砍栏」跑全十栏 KW、mentions 4 组与 THIN official。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent BTC 栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖 / 不替用户预存。

## X 额度与查询

remainingBefore=492（首读后 remaining 491，按 left_after_first+1 还原）。27 次读取后 remaining=465。同一计划 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=25，实际主扫 26：第一读 UF 查询误带 15 个非本分片号（与计划 UF1 前 10 个重叠），已保留这 10 个结果，并对余下 15 个计划号另读 UF1b，未对重叠号重读。打满 minSpend 18，超过 softCap 21：MUST 优先号+窗口号在 2 片装不下，增加 MUST3；THIN official 去重后 108 号需要 5 片；再加 UF1 分拆多出的 1 读。silent 1 次在 softCap 外。13 条被截断的 write_to_file 预览已从 assets 完整副本恢复，未重拉 X。

- UF1–UF2：0-based 1248 elysianpull 起 packed 2 片 kept 50（25+25），wrap=false，walkScanned 50。NF_skip 0。firstKept elysianpull，lastKept makehoodxyz。next 1298 tryspreadly。UF1 实际拆成 UF1a（3 帖，含 10 个计划号）+ UF1b（1 帖，余下 15 个计划号）。
- MUST1：24 个 live/窗口号；MUST2：25 个（含 Fistagent_ 取代已更名的 Bonkagent_）；MUST3：7 个（mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer。
- THIN official：去重后 108 号 5 片全读（26+25+26+27+4）。UF2 / THIN3 / THIN4 / THIN5 / KW_MINE / MEN_MINE 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T10:30:00Z（约 1.5h，与 R1911 09:30Z 重叠）；KW 与 mentions 自 2026-11-16T10:00:00Z（约 2h）；silent 自 2026-11-15T12:00:00Z（约 24h）。
- mentions 4 组轮换：LayerZero 12 / Elysium+kinetiq 25 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 1。
- silent：1912%11=9 BTC，SILENT_MEN 1 次 12 帖，多为 RGB/Ordinals 空投讨论与第三方，送审 0、录取 0。下一轮 lane=Starknet。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖 56；在库作者 29；新作者 176，短名单保留 90，跳过 86，very_new 7。

栏 rc：UF1a 3，UF1b 1，UF2 0，MUST1 16，MUST2 19，MUST3 1，THIN1 9，THIN2 7，THIN3 0，THIN4 0，THIN5 0，KW_LZ 1，KW_TAPE 25，KW_GIWA 25，KW_DOGE 15，KW_BTC 20，KW_SN 11，KW_MINT 25，KW_MINE 0，KW_PAD 24，KW_GO 5，KW_ELY 25，MEN_LZ 12，MEN_ELY 25，MEN_MINE 0，MEN_BN 1，SILENT_MEN 12。parse_errors=[]。

## 收录与在库

新收录 1 张：

- poolfun（@PoolFun_app）：19:56 CST 官帖宣布 POOL Early Bird Tickets 已开。官网 https://poolfun.app/ HTTP 200，与 bio/t.co 一致。连接钱包、关注官号并发帖领票，连续 3 天 check-in 激活；活跃票持有人分享协议费 30%。建号 2026-11-16 16:56 CST，0 粉 1 帖。自称 built with LayerZero，未独立核验，lzVerified=false，归台子/Meme，focus=false。Launch Soon / Token Soon，不是已开铸。DeepSeek overall 55（early 95 / actionable 70 / novelty 45 / risk 80）。按免费登记规则本轮提醒。已写入 userFollowWatch。本号不自动 mint。

在库刷新：

- ozero：@ozero_fun 20:01 CST 官帖（https://x.com/ozero_fun/status/2122298950728491482）首次宣布主网 waitlist 已开，https://ozero.fun/waitlist HTTP 200。连接 X、做任务、邀请好友争取主网早鸟。此前只确认 Base Sepolia 测试网。这是首次可操作的主网免费登记，不是 mint 开窗。本轮提醒。本号不自动 mint。
- bombshell-cats：@1KArtGallery Art Dealers 白名单免费 mint 已到 11-16 20:00 CST。R1910 已按首次 ≤2h 提醒，档期未改，本窗无新官帖，不重推。公售仍为 11-17 20:00 CST 起 0.0003 ETH、3/钱包。不是公开无门槛免费 mint。
- dotbots-ai：@dotBots_ai Round 2 销售仍为 11-16 21:00 CST。R1911 已按首次 ≤2h 提醒，本窗无改期官帖，不重推。这是销售窗，不是主网免费 mint。
- plunderport：20:02 CST 称 Genesis Captains 将以 LayerZero ONFT 推出，Zero 主网与 ATLAS 于 11-30 上线。未宣布免费 mint LIVE，不重推。
- hoodfrenz：20:01 CST 再预告 mint tomorrow，时刻仍为 11-17 23:00 CST，未改期，尚未 ≤2h，不重推。
- spiritsrh：19:11 CST 再见白名单帖，时刻未改（11-20 00:00 CST），R1909 已提醒，不重推。
- spoxyfun：19:05 CST 再预告 Marketplace 11-17 上线，付费 0.001 BNB 已 LIVE，非新窗口，不重推。
- inklegions：19:51 CST 回复 free mint for Ink OGs，时刻仍为 11-17 03:00 CST，未见改期，尚未 ≤2h，不重推。
- ephemeral-eth / escapehub：本窗无新官帖，窗口仍为 11-16 23:00 CST，尚未 ≤2h，不重推。
- bonkagent / Fistagent_：本窗无新官帖，铸造仍为 11-17 15:00 CST，尚未 ≤2h，不重推。
- microfrens / wrapped-eth / zyro / pingpay / bitmaxdog / unicorn-grand-prix：互动、产品续更或旧口径，无新开窗，不重推。

尚未 ≤2h、无改期、不重推：escapehub / ephemeral-eth 11-16 23:00 CST；Cipher Syndicate 11-17 00:00 CST；MicroFrens reveal 11-17 01:00 CST（mint 已完成）；hood-bitz 11-17 02:00 / 06:00 CST；Ink Legions 免费 mint 11-17 03:00 CST；FIST / Fistagent_ 11-17 15:00 CST；Bombshell Cats 公售 11-17 20:00 CST；boxcars 预售 11-17 21:00 CST；HoodTurtleRH mint 11-17 22:15 CST；hoodfrenz 11-17 23:00 CST；SpiritsRH 免费 mint 11-20 00:00 CST。

## 跳过（要点）

- DeepSeek 录取 @PoolFun_app（dsFallback=false）。其余短名单未建卡。
- TwinForge（https://twinforge.surge.sh/ ，CA 0x96d560b1e2b2061c417d8f14D111A4dE7e9680fF）：本轮仍未见官方 Twitter，按「新收录必须有推特」继续不建卡，只作线索。
- @Troyaagent：$TROYA 已有 CA，本窗为 F10 界面更新，R1911 已 skip。
- @deeptracexyz：研究工具接入 @AscendLaunch 追踪面板，不是发射台官号。
- @Sujon1009 / @Ankit_Avyentra / @Alxi39304 / @ssshaluucz：Ammora/GIWA 任务或回复号。
- @Metroishim / @VolNavyCaptain7：转发他人免费 mint/launchpad 文案。
- @npsail2026 / @AnFeng0858 / @FanRHwe / @NHPX_：资讯号或社区互动。
- @JelsenChirstino：盘点已在库/已在 Watch 的 Zero 链发射台。
- 其余短名单多为 Tape/GIWA/Elysium/BTC 互动，或已在库项目转发。

## 覆盖与债

- 十栏关键词：跑全。laneReads 十一条均为 true。
- userFollowWatch：本分片刷完，wrap=false，next 1298 tryspreadly。新卡 @PoolFun_app 已追加进 Watch。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

true。新收录 poolfun（免费 Early Bird 登记，即便 overall 55 也必须提醒）；ozero 主网 waitlist 首次开放。Bombshell Cats 与 dotBots 仍 ≤2h，但此前已提醒、档期未改，不重推。推送成功。详见 https://reboot7454.github.io/early-scout/ 。本号不自动打、不替用户存。
