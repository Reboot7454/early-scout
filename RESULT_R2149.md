# R2149 早期打新雷达

写盘前远程已是 **R2148**（11b2762，lastScout 2026-11-24 20:49:33 CST）。本路为额度重置后的常规增量轮（不是 08:00 CST 后首轮全量补扫），升为 **R2149**。lastScout **2026-11-24 21:34:50 CST**。

面板：https://reboot7454.github.io/early-scout/

## 配额
- remainingBefore=956，xReads=25，remainingAfter=931。日额重置 2026-11-25 08:00 CST。
- 模式 ample（softCap 30，minSpend 20 已满足）。searchUsersUnavailable=true（本连接器无 search_users，沉默路径仅 mentions）。
- 未开额外/重复 X 读；同一 handle 本轮只拉一次；无分页。getUsersByUsernames 1 次（新候选批量画像），searchPostsAll 24 次。
- 30m 窗口 start 2026-11-24T12:47:00Z（lastScout 12:49:33Z 减 2 分钟）；24h 窗口 start 2026-11-23T13:27:00Z。

## 十栏与关键词
- 十栏关键词本轮都跑到（UF → 必盯 Watch → 关键词盲捞）。另同等扫 BTC / Starknet。
- 30m 命中（约）：KW_LZ 0、KW_TAPE 25、KW_GIWA 20、KW_DOGE 11、KW_BTC 2、KW_STARK 2（多为误伤）、KW_MINT 25、KW_MINE 0、KW_PAD 25、KW_GO 25、KW_ELY 25、KW_GAPS 25。
- 同一轮 24h 补搜（因 30m <5）：**LayerZero / BTC / Starknet**。挖矿 30m 为 0 但属核心栏，未改成 24h。禁止把所有关键词改成 24h：已遵守。
- KW_GAPS 中 `$PULSE` 的 `$` 会被 X 搜索剥掉，噪声偏多。

## userFollowWatch
- 软刷 1834→1884；shard 50，wrap=false。
- 下轮游标 **1884 @grandpumpfun**。
- 本片软刷未见由此片新收的官号（UF2 命中 theoutcomers / UnicornGPrix / 已在库项）。
- 新收 2 卡已写入 accounts + candidateIds，并按赛道挂 Watch。

## 官号 mentions / silent
- 本轮 mentions：GIWA 30m、Tape 30m、LayerZero 24h、Elysium 增量（1 条）。各链都有覆盖，未只强化 Elysium。
- silent：LayerZero 24h mentions。silentNextAfter：**Elysium**。
- mentionsNextAfter：**DogeEVM / BTC / Starknet / squeek / STARX**（额度够时瘦栏 LZ 24h mentions 仍应每轮或隔轮跑）。

## 新收录（notify=true）
均已 DeepSeek 录取打分，focus=false，入库同时进 Watch。**没有一项是已确认免费 mint LIVE / 免费登记 LIVE。**

1. **蚁巢战争 / Ant Nest Wars（@AntNestWars / https://antnestwars.com/）** id=antnestwars
   - 老号复用（资料写 2009-07-28），241 粉 / 53 帖。资料栏与官网互证。
   - 自称像素蚂蚁卡牌，`$蚁巢` 经 @TapeLaunch 在 BNB 发射，S1 42 天。
   - 官网本轮仍显示本季已破茧 0、当前区块 #0，开赛未核到。第三方「一天免费抽蚂蚁」未经本轮官帖复核。**不是免费 mint LIVE。**
   - DS admit=true，overall 54，early 72，actionable 38，risk 68。
   - Watch：userFollowWatch + tapeWatch + tapeOutWatch。

2. **StepUp（@GiwaStepUp / https://stepupcrew.com）** id=giwastepup
   - 建号 2026-09-23 12:43 CST，5586 粉 / 36 帖。资料栏与官网互证。
   - GIWA 跑步记录/克鲁应用，跑完积 SUP 积分，Android 已出、iPhone 准备中。未见 CA，未见打新窗。**不是免费 mint。**
   - DS admit=true，overall 63，early 64，actionable 60。zoneHint 挖矿。
   - Watch：userFollowWatch + giwaWatch + miningWatch。

## 库内窗口更新
- **Shit Capital（@shit_capital）**：付费白名单售 **2026-11-24 23:00 CST** 本轮进入 ≤2h（资料上限 $2K、8 小时），公开售仍约 2026-11-25 07:00 CST。**不是免费 mint。** R2075 当时报名截止仍 >2h，此前未做过 ≤2h 提醒，本轮纳入 notify。
- **Hongbao Cat / BAOCAT（@BaocatBSC）**：官帖自称 `$BAOCAT is LIVE`、999 免费份额 claimable now、售至 2026-11-27 10:55 UTC（帖 2125194361975284048 / 2125193990995411411 / 2125193522401570865），但官网 https://baocatbsc.fun/ 本轮仍是 Sale opens in -- / Opening date to be announced / Status standing by，计数器空白。**不按已确认免费 mint LIVE。** 不重推为新开铸。
- **Thinkers Club（@ThinkersClub_）**：2026-11-23 21:59 UTC 官帖称 mint 将在 NFTX 进行（t.co/Hsd8xDuVV6）；打开后页写 THINKERS_ LAUNCHING NOV 24TH，本轮仍 Loading。**不是已确认开铸 LIVE。**
- **Shielded Wizards（@ShieldedWizBTC）**：WL mint 仍是 2026-11-25 02:00 CST（约 4.5h），公开售 2026-11-26 02:00 CST。尚未 ≤2h，未见改期，不按 ≤2h 重推。
- Vicehood / Gloopix / Final Days / Code Kitty 等库内项本轮未见官方新开铸确认，不重推。

## 看见但未收
- **封神榜 · Agent ID 抽卡（@FengshenGacha / https://www.fengshengacha.dynv6.net/）**：0 粉，dynv6 动态域名。官网写开季 2026-11-23 20:00（已过该点），每日免费 2 包 / 付费 0.002 BNB。公示主合约 `0x26EDA90e551E2Fc0564F6Cc746031a0F26D71968`，本轮 BSC RPC 已探测到字节码，但未连钱包、未核验免费包是否已可领。DS admit=false（0 粉 + 动态域名 + 领取未验证，risk 82）。不按免费 LIVE 收录或通知。
- **Pump Classic（@PumpClassicIO / https://pumpclassic.io/）**：4 天前建号，2 粉。官网写尚未有经由该流程发射的币，与官帖 `$CLASSIC` 已上线表述不一致。DS admit=false。
- **CallPut（@CallPutApp / https://callput.app）**：约一年前建号，合成期权产品自称已 LIVE，无打新窗。DS admit=false。
- **Ryodan（@Ryodan_mave / https://www.ryodan.io）**：2024-09 建号、6056 粉，非极早期。第三方称 Pioneer GTD mint live，本轮未在官网核到明确开铸页。看见但未收。
- **Iceberg（@Icebergdotcash）**：Hyperliquid prop firm，资料称 `$ICE Coming soon to @Enter_Elysium`，属 Exploring，不进 Elysium 栏。
- **giwa.eco / giwaeco.com 目录站**：跳过（后者非官方）。
- **Spike 1 万份 LZ 免费 mint TBA**：本轮未找到可核验官号，不发明手柄。库内 spike-finance / spike-wtf 可能不是同一项。
- **@eutoprotocol**：R2148 已跳过，本轮不再收。

## Discord Peek
- **discordPeekDeferred=true**。computerUse 仍遇登录墙（https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1537897411668746302），Welcome back / 邮箱密码 / QR / passkey。未填写凭证，未改变 lastSeen。
- lastSeen 仍约：#alpha-3-new-accounts 2026-11-23 22:55 CST，#alpha-1-backup 22:29 CST，#smart-accounts-tracker 22:56 CST，#alpha-1 22:19 CST。积压约 23h。
- 须父代理在本聊天请用户登录 Discord 后，同一轮补 Peek 四频道；若补扫出现自称免费 mint/登记须逐个点名通知。未到 cutoff / 触顶的频道下轮续翻。

## 其它
- Canton / Glaze / TokenWorks（含 tokenWorksWatch）及标准 Watch 本轮补盖 lastChecked 软债。
- 新卡无 focus。判断/打分 DeepSeek flash，思考开启。
- notify=true：真新收录 2 项 + Shit Capital 付费 WL 进入 ≤2h；新收录均非免费 LIVE，告警已逐项写明。
