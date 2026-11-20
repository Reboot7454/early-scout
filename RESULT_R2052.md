# RESULT R2052

- 时间：2026-11-21 01:42:49 CST（Asia/Shanghai）
- 模式：tight 增量轮（非 08:00 CST post-reset-full；lastFullAfterReset 保持 R2004）
- 面板：https://reboot7454.github.io/early-scout/
- 写盘前远程已是 R2051（commit cbffbb5，Discord 增量收录 novemberrain-rh / pingxdepin / gatedapp-xyz，lastSeen 01:21 CST）；本路升为 R2052，未改 lastSeen
- notify=false（本路无新收录；R2051 三项非免费 mint/登记/LIVE，不重推）
- 新收录：无
- dsFallback=false（本轮无新项目候选送审，未调用 DeepSeek admit）
- discordPeekDeferred=false：本路 computerUse 遇登录墙，但远程 R2051 已成功增量 Peek（loginOk 路径已完成，四频道有新 lastSeen），不催登录、不重扫同一窗口
- 监控 bug 已修：R2051 三张卡入库时未挂任何 Watch，本轮补进 userFollowWatch + 对应栏 Watch

## X 额度

- remainingBefore=183（与 R2050 remainingAfter 一致；R2051 Discord 路未改 X 统计）
- remainingAfter=166
- xReads=17（16 次 searchPostsAll + 1 次 getUsersByUsernames；瘦栏 24h 3 记 xReadsExtra；其中 silent 1）
- mode=tight，softCap=10，minSpend=10，silentCap=1
- 略超 softCap：开跑 remaining 183<200，按 tight 仍保留 6 条瘦栏独立 KW、核心栏专名合并查询、2 组 mentions 与瘦栏 24h，不得以 pacing 整栏跳过
- 无同 handle 重复重试；未伪造 search_users（searchUsersUnavailable=true）
- 日额重置：2026-11-21 08:00 CST

### 分解

- UF 2（分片 from: OR，1.5h；512 字符上限拆批）
- MUST 1（1.5h，含优先号 + @KToonsNFT @Hooddrivee @RobinYieldRH @PredictAgent @PnutChain001 @Monsie_Hood @BGYC_RH）
- 十栏 KW：瘦栏 30m 6 + 核心专名合并 1
- mentions 24h 2（MEN_LZ / MEN_ELY）
- 瘦栏 24h extra 3（LZ / BTC / SN，其中 SN 去掉光杆 Bramble）
- silent 1（GO盘 mentions-only）
- getUsersByUsernames 1（@moto_the_shadow）
- THIN_OFF 0（tight 未单开薄栏官号 from:）

## 覆盖

- 十栏关键词：是（瘦栏独立 30m：LZ/TAPE/GIWA/DOGE/BTC/SN；核心栏打新/挖矿/台子/GO/Elysium 及 AIDROP / PulseLaunchpad / STARX / Nutshell / Local Bottom / pipfun / beetleai / computeroll / hostile.xyz / stock launchpad / Oracle DAO / prediction market 合并进 KW_CORE）
- userFollow：是。cursor 565 @Tidewell_BSC → 620 @orenfinance_，next 621 @agentharvest_ai；walk 56，kept 40，NF_skip=16，wrap=false。UF1=17（多为已在库 @marketmugs 与 @anoncoinit）/ UF2=1（@orenfinance_，已在库，股票交易相关，非铸造窗）
- MUST ≤2h/官号：@KToonsNFT 本窗口无新帖；@RobinYieldRH 01:33 CST 官帖报 348/500；@Hooddrivee 01:03 CST 官帖更新 allowlist；@PredictAgent / @PnutChain001 无新开铸/改期（仍分别 22:30 / 18:30 CST）
- 瘦栏 24h 补搜：是。30m 命中 <5：LZ 0→25，BTC 2→25，SN 30m=4 几乎全是 Bramble 猫头鹰噪声，同一轮去掉光杆 Bramble 再搜 24h（2 条）。TAPE 6 / GIWA 11 / DOGE 5 未拉长。核心栏未改成 24h
- mentions 覆盖：LayerZero 25 / Elysium+kinetiq 25。下轮 mentionsNext=mining-squeek+Nutshell / BN Agent pads+STARX
- silentAccounts：ran=true，lane=GO盘，method=mentions，hits=25，无新收录（GTA 6 游戏发售噪声为主）。search_users 不可用未伪造。nextLane=LayerZero
- Discord：deferred=false。远程 R2051 已成功增量 Peek，lastSeen 保持 2026-11-21 01:21 CST（alpha-3 01:21、backup 00:14、smart-accounts 01:18、alpha-1 01:17）。本路 computerUse 遇登录墙，未改 lastSeen。11/15–11/18 积压仍未清，增量范围外

## 新收录

无。

## 关键核验（均已在库，非本路新收录，不重推）

### Kinetiq Toons（@KToonsNFT）

- 公售仍 LIVE。本轮 OpenSea API 583/5555、持有 454、地板 0.009 HYPE（R2050 为 582/5555、持有 458、地板 0.008 HYPE）
- 官帖称约两小时窗口（约 00:00–02:00 CST），本轮写盘时仍 le2h
- 铸造页 https://opensea.io/collection/kinetiqtoons
- R2046 已提醒公售 LIVE，本轮仅进度，不重推
- 自称 Elysium，仍不进 Elysium 栏

### Hood Drive（@Hooddrivee）

- 官网仍 WL Closed、Mint Nov 21, 17:00 UTC = 2026-11-22 01:00 CST，5555 份
- 01:03 CST 官帖 https://x.com/Hooddrivee/status/2123824662971117661 ：allowlist 已更新，请在 OpenSea 再查资格，还有部分获奖名单待写入
- 不是改期，不是已开铸 LIVE，配额窗口已过，不重推
- R2043 已提醒全员 GTD 与配额窗口

### Robin Yield（@RobinYieldRH）

- 公售仍 LIVE。本轮官帖 01:33 CST 报 348/500；OpenSea API 353、持有 148、地板约 0.00006 ETH（R2050 为 300/500、持有 140、地板 0.00006 ETH）
- 铸造页 https://opensea.io/collection/robin-yield- ；合约仍是 0xa6eb329f5d8090b839cab7be3e47ee74204b3eea
- R2045 已提醒公售 LIVE 与总量 1500→500，本轮仅进度，不重推

### R2051 Discord 三项（非本路新收录，不重推）

- November Rain（@novemberrain_rh / https://novrain.fun/）RH meme，CA 已核验，站点有 mint your own raindrop 文案但 mint 未实测，不是已确认免费 mint LIVE
- Ping-X DePIN（@PingXDepin / https://pingx.click/）站点描述签名 ping 验证后铸 1 PINGX，客户端/挖矿未实测，不是免费 NFT mint LIVE
- Gated App（@gatedapp_xyz / https://gatedapp.xyz）RH SocialFi，$GATED 已上主网，非免费 mint
- 以上三项 R2051 入库时未挂任何 Watch，本轮已补进 userFollowWatch，并分别挂 agentPadWatch / miningWatch / agentPadWatch

## 看见但未新收

库内已有：Kismo @Kismonft、PandalZero、LineZero @LineZero_NFT、Cars As Cards @CarsAsCards、MaruTales @MaruTalesStudio、Syndicate @SyndicateRHC、PlunderPort、Spike @spike__wtf、Zero Guys @ZeroGuysNFT、Shielded Wizards @ShieldedWizBTC、make.fun @makefunai、Elysdex、BTC_CRC30、TapeAI 预告（TAI PoB 时刻 TBA，此前已提醒）等，只刷新/跳过。
未收：@moto_the_shadow（MOTO / motobase.xyz，2025-09 建号，1036 粉、773 帖，已有 Base 社区代币，转载声称 2000 份手绘 NFT 免费 mint；非极早期新号，未建卡）。大量 LZ/打新转载号与 GTA 6 游戏噪声未建卡。

## Watch / 漏挂

R2051 三张新卡入库时不在任何 Watch，已当场补挂。UF 分片 40 个已刷账号软更新 lastChecked。Canton/Glaze/TokenWorks 软债 lastChecked 已刷新。

## Discord Peek

- 写盘前远程 R2051 已成功增量 Peek 并入库 3 项，lastSeen 已推进到 01:21 CST，本路不改 lastSeen，不记 deferred
- 本路 computerUse 遇到登录墙（https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1537897411668746302 ），未填写凭据，也未用这次失败覆盖远程成功结果
- 不必再请用户登录补同一窗口；11/15–11/18 积压仍未清，不在本轮增量范围

## 面板 / git

- lastScout / completedAt：2026-11-21 01:42:49 CST
- ufCursor：621 @agentharvest_ai
- 推送：data.json + docs/data.json（sync_docs_panel.sh）+ RESULT_R2052.md
