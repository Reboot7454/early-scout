# RESULT R2046

- 时间：2026-11-21 00:14:13 CST（Asia/Shanghai）
- 模式：pace 增量轮（非 08:00 CST post-reset-full；lastFullAfterReset 保持 R2004）
- 面板：https://reboot7454.github.io/early-scout/
- notify=true（已在库 Kinetiq Toons 官帖首次确认公售 LIVE；不是新收录）
- 新收录：无（round2046Added=[]）
- dsFallback=false（alert/whatsNew 经 DeepSeek；文案里 Hood Drive 开铸时间按官网更正为 2026-11-22 01:00 CST，避免 DS 把「01:00 CST」写成开铸）

## X 额度

- remainingBefore=260（与 R2045 remainingAfter 一致）
- remainingAfter=237
- xReads=23（主扫 22 + silent 1；瘦栏 24h 3 记 xReadsExtra）
- mode=pace，softCap=18，minSpend=18，silentCap=2
- 略超 softCap：额度未紧（距 08:00 CST 重置约 7.9h），按规则跑全十栏 + THIN_OFF + 瘦栏 24h + mentions + silent，不得以 pacing 砍栏
- 无同 handle 重复重试；未伪造 search_users（searchUsersUnavailable=true）
- 日额重置：2026-11-21 08:00 CST

### 分解

- UF 2（分片 from: OR）
- MUST 1
- THIN_OFF 4（本轮旋转 Tape + BTC 隐私 + DogeEVM + GIWA；因 R2045 已跑 LZ+Starknet）
- 十栏 KW 30m 11（6 薄栏 + 5 核心：MINT/MINE/PAD/GO/ELY）
- mentions 24h 4
- 瘦栏 24h extra 3（LZ/BTC/SN）
- silent 1（Starknet mentions-only）

## 覆盖

- 十栏关键词：是（打新/挖矿/台子/GO/LZ/Elysium/Tape/GIWA/DogeEVM/BN 相关词均在 KW 合并查询中跑到；另同等扫 BTC、Starknet）
- userFollow：是。cursor 421 @wuseagent → 468 @egg_noggy，next 469 @kairoslaunch；kept 48，walk 48，NF_skip=0，skip_already=0，wrap=false；UF1=0 / UF2=0
- MUST ≤2h/官号：@KToonsNFT @Hooddrivee @RobinYieldRH @clariontrade @PnutChain001 @PredictAgent（约 40m 窗，13 帖）
- THIN_OFF 24h：from:GIWA_by_Upbit / ShieldedNaka / banknotes_btc / DogeOS / TapeAIAgent / Blonskr / bitcointapes / TapeOutWorld（25 帖，无新开铸翻转）。TapeAI 重申 TAI PoB 11-21，时刻仍 TBA；预存已关（此前已提醒），不重推
- 瘦栏 24h 补搜：是。30m 命中 <5：LZ 0→25，BTC 0→25，SN 0→2（24h 去掉光杆 Bramble）。TAPE/GIWA/DOGE 30m≥5 未拉长。核心 MINE 30m=0 含 Nutshell/squeek 词，按规则不把肥/核心栏改成 24h
- mentions 覆盖：Tape（9）、GIWA（25）、BTC 隐私（1）、BN Agent pads+STARX+squeek/Nutshell（13）。本轮未重跑 MEN_LZ / MEN_ELY（关键词或上轮 mentions 已覆盖）
- silentAccounts：ran=true，lane=Starknet，method=mentions，hits=1，无新收录。开跑时按 meta.round=2045 旋转（index 10）。search_users 不可用未伪造。nextLane=打新
- Discord：deferred=true（登录墙）。未改 lastSeen（R2044：alpha-3 23:12、backup 22:45、smart-accounts 22:51、alpha-1 23:08 CST；上次成功 lastChecked 23:26 CST）。11/15–11/18 积压仍未清，增量范围外

## 关键核验（均已在库，非新收录）

### Kinetiq Toons（@KToonsNFT）— 必须 notify

- 官帖 2026-11-21 00:00:00 CST https://x.com/KToonsNFT/status/2123808589223727331 ：PUBLIC MINT IS NOW LIVE。无需白名单，0.01 HYPE，5/钱包；官帖写 You have two hour to get your Toon（约两小时窗口，约 00:00–02:00 CST），仍 le2h
- 铸造页 https://opensea.io/collection/kinetiqtoons
- 本轮 OpenSea：已铸 581/5555、持有 457、地板 0.008 HYPE（R2045 约 23:47 CST 为 573/5555、453、0.0085 HYPE）
- R2041 已提醒免费窗开铸与公售≤2h，本轮才是首次确认公售 LIVE
- 本轮官帖只宣布公售，不断言此前免费窗仍开或已关
- 自称 Elysium，仍不进 Elysium 栏
- 粉约 1065

### Hood Drive（@Hooddrivee）— 不重推

- 新帖 2026-11-21 00:08:33 CST https://x.com/Hooddrivee/status/2123810739421131193 ：The wait is over. Hood Drive mints tomorrow, Nov 21. Free mint on @opensea
- 官网 https://www.hooddrive.fun/ 仍 WL Closed、Mint Nov 21, 17:00 UTC = 2026-11-22 01:00 CST，5555 份
- 配额仍 2026-11-21 01:00 CST，≤2h
- 在 11-21 00:08 CST 说 tomorrow Nov 21，与官网时钟对比偏含糊，不以改期论、不重推
- R2043 已提醒全员 GTD 与配额≤2h
- 粉约 1208

### Robin Yield（@RobinYieldRH）— 不重推

- 公售仍 LIVE。本轮 OpenSea 280/500、持有 139、地板 0.0001 ETH
- R2045 已提醒公售 LIVE 与总量 1500→500，本轮仅进度

### 其他 MUST

- Clarion / Pnut（18:30 CST 尚未 ≤2h）/ Predict Agent（已推迟 22:30 CST）：MUST 窗内无新官帖，不重推

## 看见但未新收

Monsie_Hood（555 免费、日期 TBA giveaway）、StrateFai_HQ（genesis free mint，官站/是否 LIVE 不清）、Thenoonesnft（GTD giveaway）、EnclaviumFNF（第三方 early watching）、Stockereum（第三方股票发射台喊单）。kucing_bagong「introducing GiwaPad」不是新项目（giwapad-xyz 已在库 LIVE）。成人向 @Sluts_ord 跳过。ShieldedWizBTC 日期仍为第三方，不编造时刻。

## Watch / 漏挂

本轮无新卡。无「在库但不在任何 Watch」补挂。Canton/TokenWorks 仅软刷 lastChecked（barryoncanton、tokenworks-playground），无状态发明。

## Discord Peek

- computerUse 子代理遇登录墙，loginOk=false，blocker=needs_sign_in
- 未填写凭据（本跑无法 Secure Form 填密）
- 用户电脑离线，box 浏览器无法继承用户本机 Discord 会话，且 box 无已保存会话
- 须父代理请用户在 box 浏览器登录后，同一轮从 R2044 lastSeen 增量 Peek
- 频道 overlay：https://discord.com/channels/1502958818865188956/1537897411668746302
- 既有登录页：https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1527862926885785710
- 16:49 CST Secure Form 或仍待处理，勿盲目重发
- 这是近期连续成功（R2036/38/40/42/44）后的首次登录失败，不暂停整条雷达例程

## 推送

只提交 data.json + RESULT_R2046.md 到 main（不提交 discord_peek_R2046.json / 其它未跟踪 RESULT）。
