# RESULT R2050

- 时间：2026-11-21 01:13:07 CST（Asia/Shanghai）
- 模式：pace 增量轮（非 08:00 CST post-reset-full；lastFullAfterReset 保持 R2004）
- 面板：https://reboot7454.github.io/early-scout/
- 写盘前远程已是 R2049（commit 96d3a82，Discord 增量收录 layerfee-defi / frypigeonn / seolintfun，lastSeen 00:51 CST）；本路升为 R2050，未改 lastSeen
- notify=true（新收录 3 项：Monsie Hood 自称免费 mint OG 登记；Bored Grinch Yacht Club 官网自称免费 mint 且 GTD 已开；Shoji 真新收录，非免费 mint）
- 新收录：monsie-hood, bgyc-rh, shojifun（round2050Added 同步）
- dsFallback=false（admit/score/文案经 DeepSeek；普通新卡 focus=false）
- discordPeekDeferred=false：本路 computerUse 遇登录墙，但远程 R2049 已成功增量 Peek（loginOk=true，四频道 passedCutoff、未封顶），不催登录、不重扫同一窗口
- R2049 的 layerfee-defi / frypigeonn / seolintfun 保持在库，newThisRound 已清，非免费 mint 预告级观察/挖矿，不重推

## X 额度

- remainingBefore=210（与写盘前 R2048/R2049 面板 remainingAfter 一致；R2049 Discord 路未改 X 统计）
- remainingAfter=183
- xReads=27（26 次 searchPostsAll + 1 次 getUsersByUsernames；瘦栏 24h 4 记 xReadsExtra；其中 silent 1）
- mode=pace，softCap=18，minSpend=18，silentCap=2
- 略超 softCap：开跑 remaining 210>200，距 08:00 CST 重置约 6.8h，按规则跑全十栏 + THIN_OFF + 瘦栏 24h + mentions + silent，不得以 pacing 砍栏
- 无同 handle 重复重试；未伪造 search_users（searchUsersUnavailable=true）
- 日额重置：2026-11-21 08:00 CST

### 分解

- UF 2（分片 from: OR，24h）
- MUST 1（24h）
- THIN_OFF 3（本轮旋转 Tape + BTC privacy + DogeEVM + GIWA；THIN_TAPE / THIN_BTC / THIN_DOGE_GIWA，其中 Doge+GIWA 合并 1 次、命中 0）
- 十栏 KW 30m 11（LZ/TAPE/GIWA/DOGE/BTC/SN + 核心 MINT/MINE/PAD/GO/ELY）
- mentions 24h 4（MEN_TAPE / MEN_GIWA / MEN_BTC / MEN_SNDOGE）
- 瘦栏 24h extra 4（LZ/TAPE/BTC/SN）
- silent 1（台子/Meme mentions-only）
- getUsersByUsernames 1

## 覆盖

- 十栏关键词：是（打新/挖矿/台子/GO/LZ/Elysium/Tape/GIWA/DogeEVM/BN 相关词均在 KW 合并查询中跑到；另同等扫 BTC、Starknet）
- userFollow：是。cursor 517 @drift_room → 564 @playthecrypt，next 565 @Tidewell_BSC；walk 48，NF_skip=0，wrap=false。UF1=1（@orimgame）/ UF2=25（@buckme_sol、@klll_floor 等，均已在库）。远程 R2049 仍停在 517，本路推进
- MUST ≤2h/官号：@KToonsNFT @Hooddrivee @RobinYieldRH @PredictAgent @PnutChain001 已核验。Hood 00:08 CST 帖仍是「mints tomorrow Nov 21 / Free mint on OpenSea」（R2046 已见，id 2123810739421131193），不是改期
- THIN_OFF 24h：Tape + BTC privacy + DogeEVM + GIWA。THIN_TAPE=25（含 TapeAI prestake 已于 11-20 18:00 CST 关闭、TAI PoB 11-21 时刻 TBA，此前已提醒）；THIN_BTC=10（banknotes「THE LOST COIN」已在库）；THIN_DOGE_GIWA=0
- 瘦栏 24h 补搜：是。30m 命中 <5 或实质无效：LZ 1→25，TAPE 3→25，BTC 1→25，SN 30m=3 几乎全是 Bramble the Barred Owl 噪声，同一轮去掉光杆 Bramble 再搜 24h（2 条）。GIWA 19 / DOGE 6 未拉长。核心 MINE 30m=1（含 Nutshell/squeek 词）不把肥/核心栏改成 24h。PAD/GO 30m 各 25，ELY 24
- mentions 覆盖：Tape 25 / GIWA 25 / BTC 25 / Starknet+DogeEVM 25。下轮 mentionsNext=LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX
- silentAccounts：ran=true，lane=台子/Meme，method=mentions，hits=25，新收录 @shojifun。开跑时面板仍是 R2048，按当时 nextLane（2048%11=2）跑台子/Meme。search_users 不可用未伪造。nextLane=GO盘（不因 Discord 路占用 R2049 而跳过 GO盘）
- Discord：deferred=false。远程 R2049 已成功增量 Peek，lastSeen 保持 2026-11-21 00:51 CST（alpha-3 00:51、backup 00:14、smart-accounts 00:47、alpha-1 00:44；四频道 passedCutoff、未封顶）。本路 computerUse 再次遇登录墙，未改 lastSeen。11/15–11/18 积压仍未清，增量范围外

## 新收录

### Monsie Hood（@Monsie_Hood）— 必须 notify（自称免费 mint / OG 登记）

- 建号 2026-11-20 05:12 CST（created_at 2026-11-19T21:12:09.000Z），22 粉、2 帖，xUserId 2123524463056580608，未认证
- bio：「Monsie Hood 555 free mint on Robinhood Chain。」资料栏无官网
- 本轮见到被转载的官帖文本：50 OG spots for early joiners，Supply 555，Mint: Free Mint，Date: TBA，Follow @Monsie_Hood Like & Repost Drop your address。未额外重拉该号时间线（避免重复 X 读），转载来源 KW_MINT
- 无官网、无合约、日期 TBA，不是已开铸 LIVE，高风险
- DeepSeek overall 58；zone=scout（打新）；focus=false
- 入库同时挂 userFollowWatch + freeMintWatch
- 本号不自动 mint

### Bored Grinch Yacht Club（@BGYC_RH）— 必须 notify（官网自称免费 mint，GTD 已开）

- 建号 2026-11-17 03:34 CST（created_at 2026-11-16T19:34:40.000Z），1259 粉、14 帖，xUserId 2122412736143572992
- 官网 https://www.boredgrinchyc.xyz/ 可打开：10,000 Supply，FREE Mint，Robinhood Chain，GTD Spots open。资料栏 t.co 跳转即该站
- 本轮未见直接官帖（只见第三方 GTD 抽奖转载），开铸是否 LIVE 未在 OpenSea/官帖核到，只按官网 GTD 已开收录
- DeepSeek overall 64；zone=scout（打新）；focus=false；siteXMutual=partial-x-to-site
- 入库同时挂 userFollowWatch + freeMintWatch
- 本号不自动 mint

### Shoji（@shojifun）— 必须 notify（真新收录，非免费 mint）

- 建号 2026-11-16 17:15 CST（created_at 2026-11-16T09:15:11.000Z），9 粉、4 帖，xUserId 2122256792441016320
- 官网 https://shoji.fun/ 可打开：Solana 隐私账户 + 发射台，基于 @Helius Privacy Rings 与 @MeteoraAG
- 官帖 2026-11-21 00:53:54 CST https://x.com/shojifun/status/2123822153967759670 「Shoji is live」
- 官网费率：Shield/Unshield 0.25%，私钥发送免费，发射无 launch fee（约 0.021 SOL 网络租金），创建者得 60% 交易费
- DeepSeek overall 72；zone=pad（台子/Meme）；focus=false
- 入库同时挂 userFollowWatch + agentPadWatch
- 非免费 mint。本号不自动 mint

## 关键核验（均已在库，非新收录，不重推）

### Kinetiq Toons（@KToonsNFT）

- 公售仍 LIVE。本轮 OpenSea 582/5555、持有 458、地板 0.008 HYPE（与 R2048 相同）
- 官帖称约两小时窗口（约 00:00–02:00 CST），本轮核验时约 01:13 CST，仍 le2h
- 铸造页 https://opensea.io/collection/kinetiqtoons
- R2046 已提醒公售 LIVE，本轮仅进度，不重推
- 自称 Elysium，仍不进 Elysium 栏

### Hood Drive（@Hooddrivee）

- 官网仍 WL Closed、Mint Nov 21, 17:00 UTC = 2026-11-22 01:00 CST，5555 份
- 配额 2026-11-21 01:00 CST 已过，不再 ≤2h；开铸仍约 24h 后
- 00:08 CST 帖仍是原「mints tomorrow」提醒，不是改期，不重推
- R2043 已提醒全员 GTD 与配额窗口

### Robin Yield（@RobinYieldRH）

- 公售仍 LIVE。本轮 OpenSea 300/500、持有 140、地板 0.00006 ETH（R2048 为 280/500、持有 139、地板 0.00006 ETH）
- 铸造页 https://opensea.io/collection/robin-yield- ；合约仍 0xa6eb329f5d8090b839cab7be3e47ee74204b3eea
- R2045 已提醒公售 LIVE 与总量 1500→500，本轮仅进度，不重推

### 其他

- Predict Agent 已推迟至 2026-11-21 22:30 CST；Pnut 18:30 CST 尚未 ≤2h。未见 LIVE/改期，不重推
- Elysdex（@Elysdex）本轮再见「live now」类帖，官网解析为 https://elysdex.com/ ；R1696 已按产品向评论处理，不是首次确认开盘/铸造窗，仅补官网链接并刷新 lastChecked，不改 status、不重推

## 看见但未新收

库内已有：Spike @spike__wtf、Writ_Fi、sight_hood、Elysdex、StarkLaunchy、Haven_Hn_、BTC_CRC30、floradotmeme、fobodotfun、soomdotfun、avadaq_AVAX、HelmSwap、Rezofun、Kismonft、MMIX_io、JustheadzHQ、ChaoticorderNFT、onlystreetsfun、PandalZero、Icarus_Elysium、GIWAUP 等，只刷新/跳过。
未收：@TheSuitedApes（2024-07 建号，4891 粉、1888 帖，非极早期）；@chartixofficial（1 粉，Coming soon，无官网）；@Yntbet（17465 粉，预测市场+赌场，非早期）；@Itzfoden92（评论者）；@memecoinsoul（$MEMES 等待 DogeOS 主网，非本轮可打窗口）；@CyberSeaNFT（2021 艺术家评论）。BTC_CRC30「Live in a few hours」转账功能帖相对现已过时（原 mint 窗 11-07 已关闭），不重推。

## Watch / 漏挂

新卡入库同时挂 Watch，无「只建卡不盯」。无发现「在库但不在任何 Watch」需另补挂。UF 分片 48 个已刷账号软更新 lastChecked。

## Discord Peek

- 写盘前远程 R2049 已成功增量 Peek 并入库 3 项，lastSeen 已推进到 00:51 CST，本路不改 lastSeen，不记 deferred
- 本路随后 computerUse 再次遇到登录墙（https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1537897411668746302 ），未填写凭据，也未用这次失败覆盖远程成功结果
- 不必再请用户登录补同一窗口；11/15–11/18 积压仍未清，不在本轮增量范围

## 面板 / git

- lastScout / completedAt：2026-11-21 01:13:07 CST
- ufCursor：565 @Tidewell_BSC
- 推送：data.json + docs/data.json（sync_docs_panel.sh）+ RESULT_R2050.md
