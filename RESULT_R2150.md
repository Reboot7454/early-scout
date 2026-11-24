# R2150 早期打新雷达

写盘前远程已是 **R2149**（295df09，lastScout 2026-11-24 21:34:50 CST）。本路为额度重置后的常规增量轮（不是 08:00 CST 后首轮全量补扫；全量补扫已在 R2148），升为 **R2150**。lastScout **2026-11-24 22:11:01 CST**。

面板：https://reboot7454.github.io/early-scout/

## 配额
- remainingBefore=931，xReads=28，remainingAfter=903。日额重置 2026-11-25 08:00 CST。
- 模式 ample（softCap 40，minSpend 20 已满足）。searchUsersUnavailable=true（本连接器无 search_users，沉默路径仅 mentions）。
- 未开额外/重复 X 读；同一 handle 本轮只拉一次；无分页。searchPostsAll 24 次（22 组计划搜索 + MUST_WIN leftover from-query 1 次）+ getUsersByUsernames 1 次（新候选批量画像）+ getUsersPosts 2 次（@RGB_Stone、@Ignis_bnb 官号时间线）。
- 30m 窗口 start 2026-11-24T13:32:00Z（lastScout 13:34:50Z 减 2 分钟）；24h 窗口 start 2026-11-23T13:32:00Z。
- live remaining 以首读 footer 为准；meta.xQuota.remaining 曾为过期的 638，未采用。

## 十栏与关键词
- 十栏关键词本轮都跑到（UF → 必盯 Watch → 关键词盲捞）。另同等扫 BTC / Starknet。
- 30m 命中（约）：KW_LZ 1、KW_TAPE 25、KW_GIWA 19、KW_DOGE 12、KW_BTC 9、KW_STARK 2、KW_MINT 25、KW_MINE 0、KW_PAD 25、KW_GO 25、KW_ELY 14、KW_GAPS 25。UF1 0；UF2 4（均为已知号，含 @JSTK_NFT / @imaginegamelabs）；MUST_OFF 30m 0。
- 同一轮 24h 补搜（因 30m <5）：**LayerZero / Starknet**。BTC 30m=9，未拉 24h。挖矿 30m 为 0 但属核心栏，未改成 24h。禁止把所有关键词改成 24h：已遵守。
- MUST_WIN 24h 首搜被 Baocat / AntNest / GiwaStepUp / Plato 等顶满 25 条，补做 1 次 leftover from-query（shit_capital / ShieldedWizBTC / ThinkersClub_ / ChunkyKongs / FinalDays365 / HoodHavocNFTS / ZerothFi / corelinkbnb / vinductfi / ThebeliefNFT）。Thinkers 仍占页，shit_capital / ChunkyKongs / vinductfi 该 25 条内无新官帖。

## userFollowWatch
- 软刷 1884→1934；shard 50，wrap=false。
- 下轮游标 **1934 @LaunchOnGTA6**。
- 本片软刷未见由此片新收的官号。
- 新收 ignis 及换号 @theforgeen_ 已写入 accounts + candidateIds，并按赛道挂 Watch。

## 官号 mentions / silent
- 本轮 mentions 30m：DogeEVM / BTC / Starknet / squeek / STARX（各链都跑到，命中均为 0）。未只强化 Elysium。
- silent：Elysium 24h mentions。silentNextAfter：**Tape/电路**。
- mentionsNextAfter：**GIWA / Tape / LayerZero-24h / Elysium-rest**（额度够时瘦栏 LZ 24h mentions 隔轮再跑）。

## 新收录（notify=true）
均已 DeepSeek 录取打分，focus=false，入库同时进 Watch。

1. **IGNIS（@Ignis_bnb / https://ignis.ing/）** id=ignis
   - 2017-09-06 老号复用，6,267 粉 / 88 帖。资料栏 URL 为空；官网经搜索找到，站点 markdown 未见回链官推，siteXMutual=partial。
   - 币安 Agent ID 付费创世铸已 LIVE：官网 8,567/12,000 份、2 USDT/份、每份 1000 万枚 IGNIS，每 ID 最多 10 份；905 个 AI 钱包 / 1,025 笔。满 12,000 自称自动开 Pancake 池后曲线加价。官帖 21:39 CST（https://x.com/Ignis_bnb/status/2125222688457457997）报约 70%。
   - **不是免费 mint。** CA 本轮未独立核验（caUnverified=true），未发明合约地址。
   - DS admit=true，overall 48，early 45，actionable 60，risk 72。zoneHint 打新。
   - Watch：userFollowWatch + agentPadWatch + bnAgentWatch。

## 库内状态翻转 / 窗口更新
- **RGBStone（@RGB_Stone / https://rgbstone.com）** id=rgb-stone：**免费 mint 已 LIVE（状态翻转，必须点名）**。SatSea https://www.satsea.xyz/ 显示 Mint price Free，已铸 8,652/9,000（另 16 locked），Allowlist 还剩约 2 天 3 小时，整场还剩约 5 天 3 小时。官帖 20:54 CST（https://x.com/RGB_Stone/status/2125211382828413412）称进入最后阶段、当时还剩 2,000。先前只记了“将在 SatSea 做免费 mint”，且此前未进 freeMintWatch。本轮已挂 freeMintWatch + btcPrivacyWatch。属库内卡状态翻转，不是真新卡。
- **THE FORGE（@theforgeen_ / https://theforgeen.pages.dev/）** 不是新卡：即库内 the-forge-en（R651），同站换号（原记 THEFORGEEN_NFT / 别号 @THEFORGENFT_EN）。官网写「免费铸造已结束……之后每把 0.0027 BNB」，并称赛季开始前铸造关闭；21:38 CST 官帖仍称每个 Agent ID 首把铁钥匙免费（另收 0.000162 BNB 防机器人费）。本轮未独立核到链上已铸/是否关窗（check_onchain.py 不支持 BSC totalMinted）。**不按已确认免费 mint LIVE 重推。** 已把 @theforgeen_ 补进 UF / agentPadWatch / bnAgentWatch。
- **Thinkers Club（@ThinkersClub_）**：官帖给出精确钟点——2026-11-24 18:00 UTC（**2026-11-25 02:00 CST**）开 36 小时付费拍卖，底价 $100，2483 份可拍，走 NFTX / Ink。不是免费 mint，本轮距开窗仍 >2h，不按 ≤2h 或 LIVE 单独提醒（随本轮告警顺带）。
- **Hood Havoc（@HoodHavocNFTS）**：官帖改期，GTD **2026-12-01 00:00 CST**（Dec 1 16:00 UTC）、FCFS 12-02、Public 12-03，仍 OpenSea / Robinhood。原 GTD 11-25、Public 11-26。属近窗推迟，随本轮告警顺带，不单独当新开铸。
- **Plato Unseen（@PlatoUnseen）**：免费公铸延期至 2026-12-02 18:00 UTC（2026-12-03 02:00 CST）或满 520，仍 0 ETH+Base gas、1/钱包。已提醒过的同一窗延期，不重推。
- **Shit Capital（@shit_capital）**：付费白名单售仍是 **2026-11-24 23:00 CST**，仍在 ≤2h；本轮 leftover 未见新官帖。**不是免费 mint。** R2149 已提醒，不重推。公开售仍约 2026-11-25 07:00 CST。
- **Shielded Wizards（@ShieldedWizBTC）**：WL mint 仍是 2026-11-25 02:00 CST（约 3.8h），公开售 2026-11-26 02:00 CST。尚未 ≤2h，不重推。
- **Hongbao Cat / BAOCAT（@BaocatBSC）**：官网本轮仍 Sale opens in -- / Opening date TBA / Status standing by。不按已确认免费 mint LIVE，不重推。
- **蚁巢战争（@AntNestWars）**：官帖称集市升级已上线；$蚁巢 11/22 经 TapeLaunch 在 Fourmeme 发射。开赛/免费铸仍未新确认，不重推。
- **StepUp（@GiwaStepUp）**：事前登记已结束，可用邀请码下 Android；称 live stepup in gasok。不是免费 mint，不重推。
- **Final Days（@FinalDays365）**：Wallet Checker 已 LIVE（约 90% 已处理），开铸未确认，不重推。
- **7 Pad（@7launchpad）**：再发 “7 Pad is live”。R2148 已收录，不重推。
- **The Belief NFT（@ThebeliefNFT）**：仍是预告，不重推。

## 看见但未收
- **INSSAFUN（@Inssafun / https://inssa.fun/）**：建号 2026-11-13，4 粉 / 8 帖，官网与官推互证。自称即将上线的 GIWA 创作者发射台，本轮未见已部署入口或 CA。DS admit=false（overall 34，early 87，actionable 12，risk 82）。不覆盖录取、不建卡。
- **thenottiesworld / the-notties（R1922 已在库）**：资料栏仍写 Free Mint … Not Live Yet；nottiesraid.fun 为预铸游戏。官方 mint 未 LIVE，最多静默更新，不通知。
- **vinductfi**：第三方称今晚发射，leftover 官帖集未确认。不按 ≤2h。
- **giwadoteco / giwaeco.com 目录站**：上轮已跳过。ZeroTrade 2014 死号。CallPut 上轮已跳过。HALEXApp 仅评论。
- 完全 0 帖、资料栏没网址、也没人 @ 过的号，两边都可能看不见，不能承诺零漏。

## Discord Peek
- **discordPeekDeferred=true**。本轮 computerUse 仍遇登录墙（Welcome back / 邮箱密码 / QR / passkey），loginOk=false，未填写凭证，未改变 lastSeen。
- landedUrl：https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1537897411668746302
- lastSeen 仍是 2026-11-23 22:19–22:56 CST，积压约 24h。
- 须父代理在同一轮请用户在 box 上登录 Discord，然后补 Peek 四频道（#alpha-3-new-accounts、#alpha-1-backup、#smart-accounts-tracker、#alpha-1）。补扫若出现自称免费 mint/登记，须逐个点名并挂 Watch。禁止再堆到几天后。

## 监控修补
- 入库同时进 Watch：ignis → UF + agentPadWatch + bnAgentWatch。
- rgb-stone 补挂 freeMintWatch + btcPrivacyWatch（原在 UF，未进 freeMintWatch）。
- the-forge-en 补挂 @theforgeen_ 至 UF + agentPadWatch + bnAgentWatch。
- 软债 lastChecked 已戳：含 flapPadWatch / arcPadWatch / fullFunWatch / irysPadWatch / agentTradingWatch（此前停在 11-19 / 11-20）及其它标准 Watch。
- 新卡 focus=false（非 squeek/toychain 类）。links.x 与 links.twitter 均已写。

## notify
- **notify=true**：真新 IGNIS（付费 LIVE，须标明不是免费 mint）+ 库内 RGBStone 免费 mint 已 LIVE（必须点名）。THE FORGE 不当免费 LIVE。Hood 改期与 Thinkers 精确钟点顺带。Shit Capital ≤2h 不重推。
- 告警文案经 DeepSeek 生成后去掉一句指令腔（「不要当新卡」改成对用户的事实陈述）。
