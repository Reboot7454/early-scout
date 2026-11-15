# RESULT R1852

- 时间：2026-11-15 12:41 CST（Asia/Shanghai）
- 模式：独立例行 ample（非 08:00 CST 后第二轮全量补扫；lastFullAfterReset 保持 R1843）
- notify=false
- 新收录：无
- ≤2h 新窗口：无
- xReads 26（main 24 + silent 1 + admitVerify 1），remainingBefore 751 → 725
- mode=ample（softCap 28，minSpend 20，silentCap 2，ufAccountShard 50）
- UF 3 + MUST 2 + THIN 4 + 薄栏 KW×6 + 核心栏 KW×5 + mentions 4 + silent 1 + admitVerify 1
- UF 从 1542 Elypx402 起 kept 50 skip 0，last kept 1591 spindottrading，next start 1592 Hypepe_official（0-based 游标，与 R1851 一致；以 handle 为准）
- 十栏关键词均已跑全；mentions 本轮覆盖 Tape / GIWA / BTC / Starknet+DogeEVM（R1851 交接的轮换子集）
- silent 1852%11=4 → LayerZero（search_users 仍不可用，仅 mentions，25 条多为德语 oft 口语误伤，未送审）
- dsFallback=false；discordPeekDeferred=true
- 未自动 mint

## 新收录

- 无。DeepSeek 审 1 个（tapeexit）后 skip，未写入新卡。

## DeepSeek 未收录 / 未送审

- **tapeexit**（@TapeExit，overall 35，admit=false）：官网/资料栏互链 GitHub https://github.com/wangyangmingsss/tapeexit ，Demo 与主网只读入口已开，自称 TapeOut 协议上的 X Layer DeFi 应急退出工具（V3 仓位与 Spark USDC 金库预览）。公开版只读、生产签名关闭、未独立审计；2 粉、不是 mint/打新窗口。DS 判定暂不收录。admitVerify：get_users_by_usernames TapeExit 1 次。
- Glyphoras：第三方 @0xhe4ler 再称 1,111 花朵 mint、社区阶段免费；仍无官方 handle，未送审（与 R1851 相同缺口）。
- Payphone：同一第三方称 checker 已开、1,111 个钱包免费 mint。在库项目 @PayphoneNFT，非官方帖，未当新开窗，不重推；已把官号补进 freeMintWatch。
- audacitycorp：第三方赠票贴，铸造日仍 TBA。项目已在库（R1542），本轮只补 Watch，不重推。
- Kuriare7Rz 观察名单：@PlayPixelora、@BitMinersonRH、@scintillamine、@LayerZero_Core 均为在库或母链新闻；BitMinersonRH「11-16 15:00 UTC / 0.003 ETH」仅为第三方口径，未做额外官号重读，不预推。
- Sapling / @saplingdotcash：在库发射台 Lore 帖，不重推；补 handle 与 userFollowWatch。
- OSK / @AIAgent_OSK：在库 failed，官号再确认今日 18:00 CST 开池，未进入 ≤2h，不重推。
- ElysiaSealed MRDN 毕业、useXFee 产品说明、ZeroGuysNFT 预告、tapemineworld 公式说明：均在库进度，不重推。
- RGBHorse 邀请刷、Monko/MyDoge 测试网打赏、Squid Korea 周报、德语 oft 噪音、随机 pump/$EGGU 喊单：未送审。

## 在库进度（不重推）

- microfrens：官号 12:17 CST 回复 additional Free Mint Phase「not yet, working out new phase and giving people more time」。对公窗仍为今日 11:30–16:30 CST。尚余约 4 小时，未进入 ≤2h，不重推。待约 14:30 CST 进入 ≤2h 再报。
- deadhood：仍在 mint day 帖下发 GTD 回复，无新的公开铸造页。已按 R1851 提醒，不重推。
- osk-agent：官号再确认 18:00 CST 开池、0.008 BNB/席。status 保持 failed，未进入 ≤2h，不重推。
- qtronlaptops / DualForgeBSC / pillowbookRH / HoodTurtleRH / tmachinroBot：MUST 1h 窗无新帖。DualForgeBSC 今日 19:00 CST、qtronlaptops 2026-11-16 01:00 CST、pillowbookRH 2026-11-16 01:00 CST、polyrob 关闭 2026-11-16 01:12 CST、BITBOTZ Monday 11-16、hood-turtle 开铸 2026-11-17 22:15 CST 均尚未 ≤2h，已通知过的不重推。

## 关键词 / mentions 摘记

- 薄栏 6 条独立 KW（LayerZero / Tape/电路 / GIWA / DogeEVM / BTC / Starknet）与核心栏 5 条 KW 本轮均已跑全。KW_LZ 本窗 result_count=0。
- UF/MUST/THIN start_time=2026-11-15T03:34:00Z（约 1h）。薄栏 KW、核心栏 KW 与 mentions start=2026-11-15T02:34:00Z（约 2h）。silent start=2026-11-14T04:34:00Z（约 24h）。search_posts_all 的 max_results 实际硬顶 25。search_users 仍不在 X 工具目录。无 next_token 翻页。
- mentions：Tape 命中 @TapeExit（送审后 skip）与生态应援；GIWA 多为 Ammora/Upbit 讨论与 Squid 测试网周报；BTC 为 ShieldedNaka 二级市场与 RGBHorse 邀请；Starknet+DogeEVM 为 DogeOS 测试网打赏，无新的可操作挂靠官号。
- 优先号 7 个（mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets / starx_xlayer）不在本 UF 分片，并入 MUST2，本窗 0 帖、非 NF。

## Watch 漏挂修复

- audacitycorp：在库但无 Watch → userFollowWatch + freeMintWatch
- BitMinersonRH：在库但无 Watch → userFollowWatch + miningWatch
- sapling / @saplingdotcash：卡片缺 handle 且无 Watch → 补 handle，进 userFollowWatch
- PayphoneNFT：已在 userFollowWatch，补进 freeMintWatch

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1852.md`。面板 https://reboot7454.github.io/early-scout/
- notify=false：无真新收录、无 ≤2h 新窗口、推送若成功则保持安静。

## 未做 / 交接

- 未自动 mint。本轮 1 个候选送 DeepSeek（0 收 / 1 跳），dsFallback=false。
- search_users 仍不可用；silent 已用 mentions 路径跑完 LayerZero 栏。
- lastFullAfterReset=R1843。UF cursor=1591（下一 walk 从 1592 起，startHandle=Hypepe_official）。mentionsNext=LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。fatNextStarts 未改（meta 仍为 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。已同时回写 meta.xQuota 与 meta.xBudget。
- 待临近 ≤2h 再报：microfrens 对公窗约 14:30 CST 进入 ≤2h（关闭约 16:30 CST）、DualForgeBSC 今日 19:00 CST、osk-agent 开池 18:00 CST（status=failed，是否提醒交下轮按窗口规则判断）、qtronlaptops 2026-11-16 01:00 CST、pillowbookRH 2026-11-16 01:00 CST、polyrob 关闭 2026-11-16 01:12 CST、BITBOTZ Monday 11-16、hood-turtle 开铸 2026-11-17 22:15 CST。
