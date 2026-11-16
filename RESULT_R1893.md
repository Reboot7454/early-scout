# RESULT R1893

- time: 2026-11-16 09:03 CST (Asia/Shanghai)
- mode: ample（R1892 已是 08:00 CST 后首轮全量补扫，本轮恢复正常节流）
- lastFullAfterReset: **R1892**（不得连续再跑第二次 post-reset-full）
- xReads: 26（main 24 + silent 2）
- remaining: 970 → 944 / 1000
- softCap: 28，minSpend: 20，silentCap: 2
- notify: false
- newIds: （无）
- dsFallback: false（本轮无新卡送审）

## 本轮做什么

独立例行。开跑 `git pull` 已与 origin/main 同步（起点 commit b59bd18 R1892）。R1892 为 08:36 CST 的 08:00 后首轮全量补扫（收录 cipher-syndicate 已通知），本轮按 `x_budget.py` 判 ample，不强制第二次 post-reset-full。

硬顺序：UF 分片软刷 → MUST live/窗口/优先号 → THIN official 全读 → 十栏关键词（薄栏+核心栏）全跑 → mentions 轮换 4 组 → silent 挖矿栏（mentions + 上轮 deferred 档案）。DC 不登录，discordPeekDeferred=true。本号不自动 mint。

## X 额度与查询

remainingBefore=970（UF1 后页脚 969/1000）。26 次读取后 remaining=944。同一 handle 本轮只读一次；无探索/重复确认/NF 连刷。plannedMainReads=24，打满 minSpend 20，未超 softCap 28。

- UF1–UF2：0-based 118 BibblesHQ 起 packed 2 片 kept 50（25+25；hint 50），wrap=false，walkScanned 59。NF_skip 9（elysiumpepecoin / GatorEyesSolada / _pointzz / keyhasp / Arcdepthoock / vaultdock / cloakcapitalai / kuranto_rh / arka_fun）。lastKept jachtpack。next 177 hoodclub_rh。
- MUST1：24 个 live/窗口号（含 @ciphersyndi / @Hood_Bitz）；MUST2：7 个（@inklegions / @hoojafun + 折入优先号）。mustSkip=[]。prio_in_shard=NutshellMarkets / starx_xlayer；prio_folded=mobster_meme / machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom。
- THIN official：5 片全读。
- 薄栏六条 KW（LZ / Tape / GIWA / DogeEVM / BTC / Starknet）与核心栏五条 KW（打新 / 挖矿 / 台子 / GO / Elysium）全部跑完。窗口：official 自 2026-11-15T23:30:00Z（约 1.5h）；KW 与 mentions 自 22:55Z（约 2h）；silent 自 00:55Z（约 24h）。
- mentions 4 组轮换：Tape / GIWA / BTC 0 / Starknet+DogeEVM 0。
- silent：1893%11=1 挖矿。search_users 仍不在 X 目录；SILENT_MEN 1 次（1 帖）+ get_users_by_usernames 解析上轮 deferred。sentToReview 0。hyperhaul / p2eabs 已 NF 写入 NF_skip；ZeroHoppersNFT 仍 0 帖、无资料栏网站、178 粉，按规则 defer 不送审，并列入 doNotSpendSilentOn。下一轮 lane=台子/Meme。
- 部分 KW/MUST/mentions 的 write_to_file 结果在约 6.3KB 处被插入省略标记（MUST1 官方窗申报 15 帖，从截稿前最新 5 帖+includes 尾部提取信号），未因此重拉同一查询。

## 信号与结论

新录取 0。无 ≤2h 新窗口。watchLeaks=0。

- **hood-bitz**（在库）：08:52–08:58 CST 官号提醒 OpenSea 本集合被隐藏、出现仿盘（已向 OpenSea 提工单 36h 未果），并讨论若把免费份额收到 2222、快照前买家可能无法全部拿到免费 mint。未见明确 “BITBOTZ mint is live / 开窗时刻” 官宣。Monday 窗口此前已预告，非本轮首次可操作窗口，不重推；真正开窗或公布时刻再提醒。
- **cipher-syndicate**：MUST1 截稿可见的最新帖中未见其新官帖；开铸仍为 2026-11-17 00:00 CST，非 ≤2h。已在 R1892 按真新提醒，同一时间表不重推。
- **inklegions / hoojafun**：MUST2 本窗 0 帖。Ink Legions 开铸仍 2026-11-17 03:00 CST，非 ≤2h。
- **zerolotl**：08:09 CST 韩语介绍，Zero 主网在即，与 R1892 同一 announced 口径，非 LIVE，不重推。
- **shielded-wizards**：07:52 CST 同一份 Ledgermaw raid 上线（非公开 mint），不重推。
- **banknotes_btc**：08:12 CST 回复 “this week”，无新窗口，不重推。
- **Jumak_app**：社交回复，不重推。
- Tape 社区晨报：Behemoth 二期接近 500 NAND、BEM 预存/协议费讨论，属既有生态进度，不重推。
- Ammora / RebateLaunch / onlystreetsfun：已在库项目的等待名单或 coming soon 转述，不重推。
- 预拒：Launchora（GIWA Sepolia 测试网 demo）、@bataclanayvw「Introducing Migrated」低曝光非官号转述、sindicatgame / TSBdotfun SHADOWBORN / Frenzz_1515 抽奖或已在库互动。未把已在库项目再送 DeepSeek。

## 覆盖与延后

- 十栏关键词：跑全（薄栏 6 + 核心栏 5）。
- userFollowWatch：本轮分片刷完，complete=true，next 177 hoodclub_rh。
- mentions：本轮 Tape / GIWA / BTC / Starknet+DogeEVM；下一轮 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。
- silent：已跑挖矿；下一轮台子/Meme。
- Discord Peek：deferred。
- fatNextStarts 保持 agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197。本轮未推进四表 FAT 分片。
- 软债 lastChecked 已刷：canton / glaze / tokenWorks / flap。

## 不重推（沿用并补充）

- hood-bitz 同一份 OpenSea 隐藏/仿盘预警与 2222 免费份额讨论不重推，除非公布 BITBOTZ 开窗时刻或确认 LIVE。
- Cipher Syndicate 同一份 11-17 00:00 CST AL/公售时间表不重推；临近 ≤2h 或开窗 LIVE 再提醒。
- Ink Legions 同一份「开铸 2026-11-17 03:00 CST、免费 mint」不重推，除非改期或开窗。
- 沿用 R1892：deadhood 售罄确认、hooja-fun “Not yet, soon”、shielded-wizards Ledgermaw raid、zerolotl 主网将至介绍、Hokori 燃烧已落地但官网无用户入口、wrapped-eth 会计示例且 /claim 仍 404、sunfall-world Season 1 结束预告。
- 其余已提醒窗口沿用 R1891/R1890：pillowbook 同一未开盘窗口、jacketagent 付费阶段无新变化、ozero 同一份 Base Sepolia 测试网宣传、TapeMine/Behemoth 二期进度、raccoonslimestd 仍在选择发射台、Elysium Portals 免费登记未见合约、boxcars 进度/箱子奖励刷新（除非预售开盘/改期、驾照售罄、改入口/改 CA）。
- 判断/文案仍走 DeepSeek；失败才 dsFallback。本号不自动 mint。
