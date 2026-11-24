# R2148 早期打新雷达

写盘前远程已是 **R2147**（9c184c4，Discord 收录 gkitens / vanda / glint，lastScout 2026-11-23 23:01 CST）。本路为今日 08:00 CST 额度重置后的**首轮 X 雷达**，且上一轮 X 是 R2090（2026-11-21 14:12 CST）——中间 R2091–R2147 为 Discord-only，X 中断约 3 天。虽开跑已是 20:33 CST（不在 x_budget.py 的 08:00–08:25 自动全量窗），仍按**全量补扫**执行，本路升为 **R2148**。

面板：https://reboot7454.github.io/early-scout/

## 配额
- remainingBefore=1000（首探 footer 999/1000 ⇒ 记 1000），xReads=44，remainingAfter=956。日额重置 2026-11-25 08:00 CST。
- 模式记 ample（softCap 40），因全量补扫 + 瘦栏 24h 略超 softCap。lastFullAfterReset=R2148。
- 未开额外/重复 X 读；同一 handle 本轮只拉一次；无分页。
- getUsers: 0。searchUsersUnavailable=true（本连接器无 search_users，沉默路径仅 mentions）。
- 部分官号/mentions 查询返回已冻结号警告（layerzro、akarihood、mr），非致命。

## 十栏与关键词
- 十栏关键词本轮都跑到（核心肥词 30m + 瘦栏 30m + 专名补漏 KW_GAPS）。
- 30m 瘦栏命中：LZ 0、Tape 25、GIWA 25、DogeEVM 11、BTC 4、Starknet 0。
- 同一轮 24h 补搜：LZ / BTC / Starknet（因 30m <5）。Tape/GIWA 已触顶 25、DogeEVM 11，未拉 24h。
- 禁止把所有关键词改成 24h：已遵守。
- 瘦栏官号 24h 也跑了：LZ+Zero、Tape、GIWA、Doge、BTC、Stark、flap/Irys/Full/Arc。

## userFollowWatch
- 软刷 1784→1834；kept 50，walk 50，wrap=false。
- 起点 @nullclawio，下轮游标 **1834 @misthraxyz**。
- 本片为已关注号软刷，无由此片新收的官号。
- 点名 @listendotmoney 已在库（id=listen-money，已在 agentTradingWatch）但未进 UF，本轮补挂 UF。
- 新收 5 卡已写入 accounts + candidateIds，并按赛道挂 Watch。

## 官号 mentions / silent
- 本轮 mentions 全链 24h 补扫：Tape、Elysium+kinetiq、GIWA、squeek+Nutshell、BN Agent pads、LayerZero、BTC 隐私、Starknet、STARX/X Layer、flap+Irys+Full+Arc pads、DogeEVM（DOGE mentions 0 命中）。
- mentionsNextAfter：GIWA / Tape（下轮可恢复轮换，额度够时瘦栏 24h mentions 仍应每轮或隔轮跑）。
- silent：GO盘（2148%11=3）24h。silentNextAfter：LayerZero。

## 新收录（notify=true）
均已 DeepSeek 录取打分（0–100），focus=false，入库同时进 Watch。**没有一项是已确认免费 mint LIVE / 免费登记 LIVE。** BAOCAT 与 BELIEF 有免费份额/FREE MINT 自称，必须点名，但不得写成已经开铸。

1. **Hongbao Cat / BAOCAT（@BaocatBSC / https://baocatbsc.fun/）** id=baocat
   - 建号 2026-11-24 17:43 CST，0 粉 / 8 帖。官网与资料栏互证。
   - 官网自称 BNB Chain、仅限 Agent ID：999 份免费份额（只付 gas，每 Agent ID 1 份，每份 20 万枚）、3000 份付费 0.001 BNB、2222 张 Dividend Card 0.002 BNB。付费 BNB 75% 进池。
   - **Status standing by / Coming soon，Opening date TBA，不是免费 mint LIVE，也不是已开放的免费登记。** 合约未本轮链上复核。本号不自动 mint。
   - DS admit=true，overall 71，early 93，actionable 68，risk 52。
   - Watch：userFollowWatch + agentPadWatch + freeMintWatch。

2. **7 Pad（@7launchpad / https://7pad.fun/）** id=7pad
   - 建号 2026-11-24 11:06 CST，6 粉 / 1 帖。官帖 20:31 CST 称 7 Pad is live。官网 HTTP 200，与官帖文案互证（资料栏本身无 URL）。
   - 多链发射/交易控制台。未见合约，未实测发币。**不是免费 mint。**
   - DS admit=true，overall 60。Watch：userFollowWatch。

3. **Zeroth（@ZerothFi / https://zeroth.fi/）** id=zeroth
   - 建号 2026-11-24 02:13 CST，1 粉 / 2 帖。官网与 testnet.zeroth.fi 均可打开（偏 SPA 薄页）。
   - 官帖称 Zero 上的发射台+交易终端，代币以 LayerZero OFT 发射，**Testnet is live**。LZ 官方未验证。**不是免费 mint**，未见主网开铸窗。
   - DS admit=true，overall 66，early 88。Watch：userFollowWatch + layerZeroWatch + zeroWatch。

4. **Corelink（@corelinkbnb / https://www.corelink.family/）** id=corelink
   - 建号 2026-11-23 23:31 CST，9 粉 / 7 帖。官网可访问。
   - 官帖称 $CORELINK 已在 @flapdotsh 上线，CA `0x3207de602b8c7e46253504a4d76b5c8be2897777`（未链上复核）。自称闲置 NVIDIA GPU 赚 BNB。**已开盘，不是免费 mint。**
   - DS admit=true，overall 55。Watch：userFollowWatch + miningWatch。

5. **BELIEF（@ThebeliefNFT / OpenSea collection/belief-faith-identity）** id=belief-nft
   - 建号 2026-11-23 05:30 CST，249 粉 / 11 帖。资料栏自称 2222 份、Coming soon to Robinhood Chain，**展示名带 FREE MINT**；URL 指向 OpenSea 合集（HTTP 200）。
   - 本轮未见该号自己的开铸官帖，仅见第三方 30GTD+50 FCFS 免费 mint 抽奖转发。**开铸未核到，不是已确认免费 mint LIVE。**
   - DS admit=true，overall 66。Watch：userFollowWatch + freeMintWatch。

## 库内窗口更新（不按新 LIVE 重推）
- **CITYHOOD（@appcityhood）**：相对 R2090 原定 2026-11-21 22:00 CST 公售，官帖 2026-11-23 20:44 CST LAST CALL 改到 **11-23 14:00 UTC GTD 免费 / 14:30 WL $0.50 / 15:00 Public $1.50**，钱包提交 13:30 UTC 截止。现已过窗。官网仍显示 Minted 0/4333、登记页仍像 Open now（静态页可能未更新）。本轮 Blockscout/OpenSea 遇 Cloudflare，**未能链上复核是否已铸**。因 X 中断约 3 天可能错过窗口，只作事实更新，不按新免费 LIVE 重推。
- **Shielded Wizards（@ShieldedWizBTC）**：官帖 10:36 CST 称发射台已 live（https://brimhollow.app/），可用 WL Checker。**WL mint 2026-11-25 02:00 CST（约 5h，尚未 ≤2h）**，Public 2026-11-26 02:00 CST。资料栏称免费 3333。WL Checker 是查已在名单，不是新的免费登记。≤2h 再报。
- **PlunderPort（@PlunderPort）**：官帖公布日历 **2026-11-29 Genesis Captains 免费 mint**，3333 份，5 条 ONFT-ready 链（含 Robinhood）。官网 hero 亦写 GTD mint · Nov 29。早期登记仍开。不是已开铸 LIVE。
- **GetTroopers（@GetTroopers）**：官帖 13:47 CST「GTD Registrations closed, moving to FCFS」，随后 Collabs OPEN。仍是登记，不是 mint LIVE。
- **kangozro**：WL checker 已开，合作社区 11-28 前提交钱包；另有推特抽奖。不是新的免费登记 LIVE。
- **Layermachines**：Free Mint soon + Like+RT 留钱包，不是已开铸。
- **Ballers（@ballersxyz）**：玩小游戏登榜赢 Series 1 免费 mint pack，日期规则即将公布。不是 LIVE。
- **Emberfall（@EmberfallGiwa）**：称 500 个免费 mint 名额开始通过 Like+RT+评论 EVM 抽选。是推特抽奖，不是免费登记 LIVE。

## 监控 bug 修复
- R2091–R2147 入库但未进任何 Watch 的 **177** 张卡，本轮全部补进 userFollowWatch；能判断赛道的另挂 giwaWatch 8、miningWatch 5、layerZeroWatch/zeroWatch 3、tapeOutWatch/tapeWatch 1。
- 历史 2000+ 张更早无 Watch 卡本轮不批量回填。
- 新卡与 @listendotmoney 均已进 Watch。在库不进 Watch 视为监控 bug，已当场修本轮范围。

## 看见但未收
- **Implied Markets（@impliedmarkets / https://impliedmarkets.xyz/）**：官网可访问，自称在 Elysium 上下期权、成交在 Derive，资料栏仍是 Coming soon @enter_elysium。Elysium 部署未实测，按 Exploring/未核到部署，**不进 Elysium 栏**。DS 亦 admit=false（打分器还按旧「五栏」口径，主要否决原因仍是部署未验证）。
- **@eutoprotocol**：简介自称 Solana AI launchpad，无官网无合约，证据太薄，DS admit=false。
- **@GiwaCat_**（giwa.cat）：官网写官方 @GiwaCat 已暂停、期望恢复；@GiwaCat_ 0 帖，铸造数字为破折号。冒认/替代号风险高，本轮不建卡。
- **@Giwaterminal** 即库内 giwa-terminal（@Giwa_Terminal），不新建卡。
- **AmmoraEco** 对比库内 ammorahq @AmmoraHQ，不新建卡。
- **@LayerzeroEco** 等侦察号此前已跳过，本轮不收。
- 其它 KOI/抽奖号、交易基础设施（如 PerpetualAgents）未收。

## Discord Peek
- **discordPeekDeferred=true**。computerUse 打开 #alpha-3-new-accounts 即遇登录墙：`https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1537897411668746302`。页面 Welcome back / Email or Phone Number / Password / Log In / QR / passkey。立即停止，未输入、未点登录。
- loginOk=false。**lastSeen / lastSeenByChannel 未改**：alpha-3 2026-11-23 22:55、backup 22:29、smart 22:56、alpha-1 22:19 CST。约 21h 积压。
- 同一轮须由父代理在用户于聊天中登录 Discord 后补 Peek（含 notify=false 的安静轮也不许堆到几天后再补）。补扫若出现自称免费 mint/登记须逐个点名通知。

## notify
- notify=true：有 5 张真新卡；告警须点名 BAOCAT 的 999 免费份额（未开售）与 BELIEF 展示名 FREE MINT（开铸未核到），并附面板链接。
- CITYHOOD 过窗、Shielded Wizards 约 5h 窗口作为库内更新写在告警里，不单独按新 LIVE 重推。
