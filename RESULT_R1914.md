# RESULT R1914

- time: **2026-11-16 22:12 CST**
- mode: **pace**（独立例行，非第二次 post-reset-full；remaining>200，十栏仍跑全）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- notify: **true**
- newThisRound: **forg3r**（@Forg3rApp，BNB+Solana 社区出资发射台，主网已开、当前可见 $PETTY/$BOSS Open 发射，overall 79，按真新收录提醒，不是免费 mint）；**oinkhash**（@oinkhash，BNB 算力挖矿游戏，主网合约已部署，付费 Piglet 0.0015 BNB，overall 73，按真新收录提醒；新用户免费 mint 未核验，不是已确认的免费 mint LIVE）
- le2h: **cipher-syndicate**（AL/公售 11-17 00:00 CST，首次进入 ≤2h，本轮提醒）；**escapehub**（Launchpad 11-16 23:00 CST，R1913 已提醒，不重推）；**ephemeral-eth**（Early Access 11-16 23:00 CST，R1913 已提醒，不重推）
- dsFallback: false
- xReads: **26**（main 25 + silent 1）
- remainingBefore: **439** → remaining: **413**
- softCap 23 / minSpend 18 / silentCap 2

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点为 R1913）。R1892 为 08:00 CST 后首轮全量补扫，之后已恢复正常节流；本轮 `x_budget.py` 判 pace（remainingBefore=439，softCap 23），不强制第二次 post-reset-full。因 remaining>200，按用户「额度够时不得砍栏」跑全十栏 KW、mentions 4 组与 THIN official。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent 打新栏（仅 mentions；search_users 仍不在目录）。DC 不登录，discordPeekDeferred=true。本号不自动 mint / 不自动买卖 / 不替用户预存。

## X 额度与查询

remainingBefore=439（首读 UF1 后 remaining 438，按 left_after_first+1 还原）。26 次读取后 remaining=413。同一计划 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=25，实际主扫 25，无额外补读。打满 minSpend 18，超过 softCap 23：MUST 优先号+窗口号在 2 片装不下，增加 MUST3；THIN official 去重后 108 号需要 5 片。silent 1 次在 softCap 外。被截断的 write_to_file 预览已从 assets 完整副本按 newest_id 恢复，未重拉 X。

- UF1–UF2：0-based 1348 payolaads 起 packed 2 片 kept 49（25+24），wrap=false，walkScanned 49。NF_skip 0。firstKept payolaads，lastKept soar_ag。next 1397 Conquerors_Dao。
- MUST1：24 个 live/窗口号；MUST2：25 个（含 Fistagent_）；MUST3：8 个（PoolFun_app / mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer）。mustSkip=[]。prio_in_shard=[]；prio_folded=mobster_meme/machinedotfun/bscaidrop/PulseLaunchpad/localbottomcom/NutshellMarkets/starx_xlayer。
- THIN official：去重后 108 号 5 片全读（26+25+26+27+4）。THIN5 / MEN_MINE / MEN_BN 本窗 0 帖，不是漏跑。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-16T12:30:00Z（约 1.5h，与 R1913 11:30Z 重叠）；KW 与 mentions 自 2026-11-16T12:00:00Z（约 2h）；silent 自 2026-11-15T14:00:00Z（约 24h）。
- mentions 4 组轮换：LayerZero 19 / Elysium+kinetiq 25 / mining-squeek+Nutshell 0 / BN Agent pads+STARX 0。
- silent：1914%11=0 打新，SILENT_MEN 1 次 25 帖，送审 1（@oinkhash）并录取。下一轮 lane=挖矿。search_users 仍不在目录。不要把下一轮 silentCap 花在 bitcoincoreorg / StreetHoodMedia / ZeroHoppersNFT。
- 官号去重帖与新作者见 parse：栏 rc 如下。

栏 rc：UF1 2，UF2 5，MUST1 5，MUST2 25，MUST3 0，THIN1 3，THIN2 11，THIN3 2，THIN4 9，THIN5 0，KW_LZ 1，KW_TAPE 25，KW_GIWA 25，KW_DOGE 25，KW_BTC 11，KW_SN 7，KW_MINT 25，KW_MINE 1，KW_PAD 25，KW_GO 4，KW_ELY 25，MEN_LZ 19，MEN_ELY 25，MEN_MINE 0，MEN_BN 0，SILENT_MEN 25。parse_errors 无；截断预览已用完整副本，不计入正式 rc。

## 收录与在库

新收录 2 张：

- forg3r（@Forg3rApp）：22:00 CST 官帖宣布玩法。官网 https://forg3r.com/ HTTP 200，与 bio/t.co 一致。社区出资发射台，对比 pump.fun bonding curve。建号 2026-11-14 04:06 CST，29 粉 7 帖。BNB factory 0x811F6a1d876448fF4423A5403503D3e275923B61，Solana program F8yTj3mGEdFHe4exU26Vf2tFTfYnbuBNcwF8VdkM9uiw。当前各 1 个 Open 发射：BNB $PETTY（0xDA7a43f6ff4473333C2B65366BaDc4E43ECF56c7，12:17 CST 开）、Solana $BOSS（HqC5ucppcVDcApyuGoZGDU4h2LS7xEy7yehqA8sr5h2R，10:32 CST 开）。不是免费 mint。归台子/Meme，lzVerified=false，focus=false。DeepSeek overall 79（early 92 / actionable 84 / novelty 70 / risk 68）。按真新收录本轮提醒。已写入 userFollowWatch。本号不自动 mint。
- oinkhash（@oinkhash）：22:04 CST 官号回复说明 Practice mode 与付费档。官网 https://oinkhash.fun/ HTTP 200，与 bio/t.co 一致。建号 2026-11-07 22:57 CST，13 粉 25 帖。.ai Agent ID 持有者 mint 猪按算力挖 $TRUF，51 天减半。BSC 主网合约已部署（TRUF/pigs/mine/vault/market）。Practice 可无钱包试玩；付费 Piglet 0.0015 BNB/1 hashpower；免费再发仅针对 11-08 迁约后的旧猪持有者，新用户免费 mint 未链上核验。bio 仍写 Testnet demo live，与主网付费档不完全一致。归挖矿，lzVerified=false，focus=false。DeepSeek overall 73（early 88 / actionable 76 / novelty 75 / risk 72）。按真新收录本轮提醒。已写入 userFollowWatch 与 agentMiningWatch。本号不自动 mint。

在库刷新：

- cipher-syndicate：AL/公售窗口首次进入 ≤2h，仍为 11-17 00:00 CST。本窗无新官帖、档期未改。Stage 1 AL 免费 mint（444 cap）。本轮提醒。本号不自动 mint。
- escapehub：Launchpad 窗口仍为 11-16 23:00 CST，仍 ≤2h。R1913 已提醒，档期未改，不重推。
- ephemeral-eth：Early Access 窗口仍为 11-16 23:00 CST，仍 ≤2h。R1913 已提醒，档期未改，不重推。
- bombshell-cats：Art Dealers 白名单已过 11-16 20:00 CST。R1910 已提醒，退出本轮 ≤2h 列表。公售仍为 11-17 20:00 CST，尚未 ≤2h，不重推。
- dotbots-ai：21:14 CST 官帖宣布 Round 2 销售已 LIVE（$10/BNB、每 Agent ID 一个、FCFS）。R1911 已按首次 ≤2h 提醒，不重推。退出本轮 ≤2h 列表。这是付费销售窗，不是主网免费 mint。
- bonkagent / Fistagent_：21:33 / 21:56 CST 官帖再确认 11-17 15:00 CST 开铸，并公布规则（总量 163,000,000 FIST，前 1,000 份免费 1/钱包，其后 9,000 份 0.005 BNB、最多 10/钱包，仅 Agent 钱包）。时刻未改，尚未 ≤2h，不重推。
- vorda：21:12 CST 宣布 3,333 FREE VORDA PASS 社交预热（关注/开通知/发帖标签），未见独立登记页或已开铸，不是免费 mint LIVE，不重推。
- TapeAIAgent：补充邀请积分/额度加速与 TAI 用途，开盘仍称本周公布，不重推。
- pocketperps：PL01 is OPEN，属已上线产品续更，不重推。

尚未 ≤2h、无改期、不重推：Ink Legions 免费 mint 11-17 03:00 CST；hood-bitz 11-17 02:00 / 06:00 CST；FIST / Fistagent_ 11-17 15:00 CST；Bombshell Cats 公售 11-17 20:00 CST；boxcars 预售 11-17 21:00 CST；HoodTurtleRH mint 11-17 22:15 CST；hoodfrenz 11-17 23:00 CST；SpiritsRH 免费 mint 11-20 00:00 CST。

## 跳过（要点）

- DeepSeek 录取 @Forg3rApp、@oinkhash（dsFallback=false）。
- TwinForge（https://twinforge.surge.sh/ ，CA 0x96d560b1e2b2061c417d8f14D111A4dE7e9680fF）：本轮仍仅见第三方提及，未见官方 Twitter，按「新收录必须有推特」继续不建卡，只作线索。
- 其余短名单多为 GIWA/Ammora Season 2 任务号、已在库 PlunderPort / PunchInBNB / Mendlings / Hypaww 互动，或 Tape/资讯转发。

## 覆盖与债

- 十栏关键词：跑全。laneReads 十一条均为 true。
- userFollowWatch：本分片刷完，wrap=false，next 1397 Conquerors_Dao。新卡 @Forg3rApp、@oinkhash 已追加进 Watch。
- mentions：本轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX；下一轮 Tape / GIWA / BTC / Starknet+DogeEVM。
- watchLeaks：无。
- fat cursors 未推进（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- soft-debt lastChecked 已刷：cantonPadWatch / cantonWatch / glazeWatch / tokenWorksWatch / tokenWorksPlaygroundWatch / flaunchWatch / flapPadWatch / xChainPadWatch。
- discordPeekDeferred=true（DC 不登录）。
- lastFullAfterReset 保持 R1892。

## notify

true。新收录 forg3r、oinkhash（均为真新；oinkhash 新用户免费 mint 未核验，不是已确认的免费 mint LIVE）；cipher-syndicate 窗口首次进入 ≤2h。escapehub 与 ephemeral-eth 仍 ≤2h，但此前已提醒、档期未改，不重推。推送成功。详见 https://reboot7454.github.io/early-scout/ 。本号不自动打、不替用户存。
