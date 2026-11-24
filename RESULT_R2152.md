# RESULT R2152

写盘前远程已是 **R2151**（8d00aad，lastScout 2026-11-24 22:41:55 CST）。本路为额度重置后的常规增量轮（不是 08:00 CST 后首轮全量补扫；全量补扫已在 R2148），升为 **R2152**。lastScout **2026-11-24 23:04:10 CST**。

面板：https://reboot7454.github.io/early-scout/

## 配额
- remainingBefore=877，xReads=26，remainingAfter=851。日额重置 2026-11-25 08:00 CST。
- 模式 ample（softCap 40，minSpend 20 已满足）。searchUsersUnavailable=true（本连接器无 search_users，沉默路径仅 mentions）。
- 未开额外/重复 X 读；同一 handle 本轮只拉一次；无分页。
- 计划搜索 22 次（UF2 + MUST + 十栏 KW + KW_GAPS + 5 条 mentions + SILENT_GIWA）+ 瘦栏 24h 关键词 3 次 + MUST_WIN leftover 1 次；合计 26 次读。live remaining 以首读 footer 为准（876 left => remainingBefore 877）。
- 30m 窗口 start 2026-11-24T14:39:00Z（lastScout 14:41:55Z 减约 3 分钟）；24h 窗口 start 2026-11-23T14:39:00Z。

## 十栏与关键词
- 十栏关键词本轮都跑到（UF → 必盯 Watch → 关键词盲捞）。另同等扫 BTC / Starknet。
- 30m 命中：KW_LZ 0、KW_TAPE 16、KW_GIWA 8、KW_DOGE 5、KW_BTC 0、KW_STARK 4、KW_MINT 25、KW_MINE 0、KW_PAD 25、KW_GO 25、KW_ELY 14、KW_GAPS 19。MUST_OFF 30m 0。
- 同一轮 24h 补搜（因 30m <5）：**LayerZero / BTC / Starknet**（24h 各触顶 25）。挖矿 30m 为 0 但属核心栏，未改成 24h。禁止把所有关键词改成 24h：已遵守。
- MUST_WIN 24h 首搜触顶 25 条，覆盖 FinalDays365 / RGB_Stone / TheForgeEN_ / Ignis_bnb / GiwaStepUp / AntNestWars / 7launchpad / PlatoUnseen。补做 1 次 leftover from-query（shit_capital / ShieldedWizBTC / ThinkersClub_ / BaocatBSC / ThebeliefNFT / HoodHavocNFTS）。leftover 收回 25 条，见到后五号；**@shit_capital 仍不在 24h 最新 25 条里**，视为本窗无官帖。

## userFollowWatch
- 软刷 1984→2034；shard 50，wrap=false。
- 下轮游标 **2034 @makefunai**。
- 本片软刷仅见已在库的 @Tauro_Agent 23:00 CST 路线图更新（13 live / 1 next），无新开铸。
- 新收 deadgrid / fiona-hippo / baekje / ballast-giwa 已写入 accounts + candidateIds，并按赛道挂 Watch。

## 官号 mentions / silent
- 本轮 mentions：DogeEVM 30m（0）、BTC 30m（1，仅为已在库 @RGBHorse 的第三方推广）、Starknet 30m（0）、squeek 30m（0）、STARX 30m（0）。各指定链都跑到，未只强化 Elysium。
- silent：GIWA 24h mentions（25 触顶）。silentNextAfter：**DogeEVM**。
- mentionsNextAfter：**GIWA / Tape / LayerZero-24h / Elysium-rest**（额度够时瘦栏 LZ 24h mentions 隔轮再跑）。

## 新收录（notify=true）
均已 DeepSeek 打分，focus=false，入库同时进 Watch。Ballast GIWA 为覆盖录取（见下）。

1. **DeadGrid（@DeadGridNft / https://deadgridprotocol.fun/）** id=deadgrid
   - 2026-11-15 00:30 CST 建号，18 粉 / 7 帖。官网与官推互证（mint.json 回链 x.com/DeadGridNft，siteXMutual=yes）。
   - 官帖 22:59 CST（https://x.com/DeadGridNft/status/2125243006781693952）称 PUBLIC MINT IS OPEN、已铸 734/3,000。
   - 官网 mintOpen=true：Agent ID 首份免费（只付 gas），之后 0.001 BNB；无 ID 走 mintPublic()，每份 0.001 BNB。NFT CA 0x3dB83C288A0C7c91B31D855dF079ACa5763aC3eF（BSC）。本轮未独立复核链上已铸数。
   - **Agent ID 首份免费 mint 已 LIVE。** 不是全员免费 mint。
   - DS admit=true，overall 76，early 78，actionable 88，risk 58。栏位 **打新**。
   - Watch：userFollowWatch + agentPadWatch + bnAgentWatch + freeMintWatch。

2. **Fiona the Hippo（@FionaHippoBNB）** id=fiona-hippo
   - 今日 18:30 CST 建号，4 粉 / 1 帖，资料栏无独立官网。
   - 官帖 22:54 CST（https://x.com/FionaHippoBNB/status/2125241581343293792）称 $FIONA 在 CheesePad 预售已 LIVE，仅限 Binance Agent Wallet，每钱包最多 0.5 BNB，税 2/2 自称全部捐动物园，售卖可随时结束。
   - 销售页 https://www.cheesepad.ai/sale/bsc/0xFe6aDae958E341A1CDa89cac9285F014be64B0Ef ，CA 0xFe6aDae958E341A1CDa89cac9285F014be64B0Ef。CheesePad 首页列出 Fiona · Fairlaunch · Agent ID only，Raised 1.8 / 1 BNB。
   - **不是免费 mint。** CheesePad 本轮未找到官推，不单独建台子卡。
   - DS admit=true，overall 68，early 88，actionable 78，risk 82。DS 栏位曾写「打新」，已覆盖为 **BN Agent 钱包**。
   - Watch：userFollowWatch + agentPadWatch + bnAgentWatch。

3. **Baekje（@BaekjeDotFun / https://baekje.fun/）** id=baekje
   - 2026-11-06 15:31 CST 建号，7 粉 / 2 帖。官网与资料栏互证。
   - 官帖 22:44 CST（https://x.com/BaekjeDotFun/status/2125239226686222613）称 The Baekje waitlist is live。官网写 Baekje opens soon / Take your number，可连钱包或 Continue with X。
   - **免费候补登记已开，尚未开盘，不是已开铸免费 mint LIVE。**
   - DS admit=true，overall 60，early 84，actionable 45，risk 62。DS 栏位曾写「台子/Meme」，已覆盖为 **GIWA**。
   - Watch：userFollowWatch + giwaWatch。

4. **Ballast (GIWA)（@LaunchBL / https://ballast.exchange）** id=ballast-giwa
   - 与库内 Elysium 上的 Ballast（@ballastedapp，id=ballast）不是同一张卡。2026-09-30 建号，74 粉 / 41 帖。资料栏指向官网。
   - 官帖 18:08 CST（https://x.com/LaunchBL/status/2125169610995724374）称站点换了新外观。官网已显示 Tokens launched 5、Volume $1.52，流动性自称永久锁定。
   - **不是免费 mint。** siteXMutual=partial。
   - DS admit=false（成交极低、不像打新窗），**按 GIWA 台子覆盖规则覆盖录取**（dsOverride）。overall 45，early 62，actionable 40，risk 78。栏位 **GIWA**。
   - Watch：userFollowWatch + giwaWatch。

## 库内状态翻转 / 窗口更新
- **Final Days（@FinalDays365）** id=final-days：**免费 Early Access mint 已 LIVE（状态翻转，必须点名）**。官帖 23:00:01 CST（https://x.com/FinalDays365/status/2125243044559831127）宣布 EARLY ACCESS MINT IS NOW LIVE，入口 OpenSea https://opensea.io/collection/finaldays。OpenSea 铸页：Early Access 为 Free、Allowlist、1/钱包；另有 Team 免费（100/钱包）；随后 WL/Public 各 0.0004 ETH（约 $0.69）。本轮页面已铸 186/10,000（第一次拉取 174，随后 186），持有 67，地板 0.005 ETH。此前仅记录 11-24 将开、尚未 LIVE。已保持 UF + freeMintWatch，le2h=true。
- **Shit Capital（@shit_capital）**：付费白名单售到点（约 23:00 CST），但 24h 内未见官号新帖，官网本轮未读到明确已筹/开卖数字。公开售仍约 2026-11-25 07:00 CST。**不是免费 mint。** R2149/R2150 已提醒，不按已确认开卖重推。仍 le2h。
- **Shielded Wizards（@ShieldedWizBTC）**：WL mint 仍是 2026-11-25 02:00 CST，公开售 2026-11-26 02:00 CST。尚未 ≤2h，不重推。
- **Thinkers Club（@ThinkersClub_）**：仍是 2026-11-25 02:00 CST 开 36 小时付费拍卖。尚未 ≤2h，不重推。
- **IGNIS（@Ignis_bnb）**：付费创世铸仍约 70% LIVE，无实质变化，不重推。
- **THE FORGE（@theforgeen_）**：本轮 22:39 CST 仍称每个 Agent ID 首把铁钥匙免费；官网此前写免费铸造已结束。口径同 R2150，**不按已确认免费 mint LIVE 重推。**
- **Hongbao Cat（@BaocatBSC）**：leftover 仍是回复里自称 999 免费份额 claimable now，未再打开官网。不按已确认免费 mint LIVE 重推。
- **Tauro Agent（@Tauro_Agent）**：23:00 CST 路线图续更（13 live / 1 next），不是免费 mint，不重推。
- **RGBStone / Hood Havoc / Plato Unseen / 蚁巢战争 / StepUp / Final Days 之外的 7 Pad / The Belief NFT / Stinky Penguin**：相对 R2151 无实质新确认，仅戳 lastChecked，不重推。

## 看见但未收
- CheesePad（https://www.cheesepad.ai/）是 Fiona 的发射台，首页已有多笔 sale/microsale，但本轮未找到官推，按「新收录必须有推特」不单独建台子卡。
- Unicorn Grand Prix / Law of the Abyss / Agent Cards 仅见第三方转发或旧卡，本轮无官号新确认，不改期、不重收。
- Kaldravyx 自称即将上 Pump.fun，Solana 噪声，不收。
- theworldof_mai / Nuztech 等是 Bramble 关键词误伤（儿童绘本/音乐），已忽略。
- SamiTrades_ 推广已在库的 RGBHorse，非新官号。
- 完全 0 帖、资料栏没网址、也没人 @ 过的号，两边都可能看不见，不能承诺零漏。

## Discord Peek
- **discordPeekDeferred=true**。写盘时仍按与 R2148–R2151 相同的登录墙处理；本轮将在推送后面再尝试 computerUse，若仍是 Welcome back / 邮箱密码 / QR / passkey 墙，则 loginOk=false，未填写凭证，不改变 lastSeen。
- lastSeen 仍是 2026-11-23 22:19–22:56 CST，积压约 25h。
- 须父代理在同一轮请用户在 box 上登录 Discord，然后补 Peek 四频道（#alpha-3-new-accounts、#alpha-1-backup、#smart-accounts-tracker、#alpha-1）。补扫若出现自称免费 mint/登记，须逐个点名并挂 Watch。禁止再堆到几天后。

## 监控修补
- 入库同时进 Watch：deadgrid → UF + agentPadWatch + bnAgentWatch + freeMintWatch；fiona-hippo → UF + agentPadWatch + bnAgentWatch；baekje → UF + giwaWatch；ballast-giwa → UF + giwaWatch。final-days 状态翻转后保持 UF + freeMintWatch。
- 新卡 focus=false（非 squeek/toychain 类）。links.x 与 links.twitter 均已写。
- 软债 lastChecked 已戳标准 Watch。

## notify
- **notify=true**：真新 DeadGrid（须点名 Agent ID 首份免费 mint LIVE）/ Baekje（须点名免费候补登记）/ Fiona the Hippo（付费 Fairlaunch LIVE，须标明不是免费 mint）/ Ballast GIWA（不是免费 mint）+ 库内 Final Days 免费 Early Access mint 已 LIVE（必须点名）。Shit Capital ≤2h 到点但未见官帖确认，不重推。
