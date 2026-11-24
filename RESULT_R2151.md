# RESULT R2151

写盘前远程已是 **R2150**（a6628b1，lastScout 2026-11-24 22:11:01 CST）。本路为额度重置后的常规增量轮（不是 08:00 CST 后首轮全量补扫；全量补扫已在 R2148），升为 **R2151**。lastScout **2026-11-24 22:41:55 CST**。

面板：https://reboot7454.github.io/early-scout/

## 配额
- remainingBefore=903，xReads=26，remainingAfter=877。日额重置 2026-11-25 08:00 CST。
- 模式 ample（softCap 40，minSpend 20 已满足）。searchUsersUnavailable=true（本连接器无 search_users，沉默路径仅 mentions）。
- 未开额外/重复 X 读；同一 handle 本轮只拉一次；无分页。
- searchPostsAll 计划搜索 + MUST_WIN leftover from-query 1 次 + 瘦栏 24h 关键词 3 次 + 新候选官号/画像查询；合计 26 次读。live remaining 以首读 footer 为准。
- 30m 窗口 start 2026-11-24T14:09:00Z（lastScout 14:11:01Z 减 2 分钟）；24h 窗口 start 2026-11-23T14:09:00Z。

## 十栏与关键词
- 十栏关键词本轮都跑到（UF → 必盯 Watch → 关键词盲捞）。另同等扫 BTC / Starknet。
- 30m 命中：KW_LZ 1、KW_TAPE 25、KW_GIWA 15、KW_DOGE 7、KW_BTC 3、KW_STARK 1、KW_MINT 25、KW_MINE 0、KW_PAD 25、KW_GO 25、KW_ELY 24、KW_GAPS 25。MUST_OFF 30m 2。
- 同一轮 24h 补搜（因 30m <5）：**LayerZero / BTC / Starknet**（24h 各触顶 25）。挖矿 30m 为 0 但属核心栏，未改成 24h。禁止把所有关键词改成 24h：已遵守。
- MUST_WIN 24h 首搜触顶 25 条，补做 1 次 leftover from-query（shit_capital / ShieldedWizBTC / ThinkersClub_ / ThebeliefNFT / FinalDays365 / HoodHavocNFTS 等）。leftover 收回 23 条，覆盖了这些必盯号。

## userFollowWatch
- 软刷 1934→1984；shard 50，wrap=false。
- 下轮游标 **1984 @ZeroPunksNFT**。
- 本片软刷见到 @Vice6fun 直播帖、@heph_ai 测试合作、@GetTroopers 短帖，均已在库、无新开铸。未见由此片新收的官号。
- 新收 blackoutfi / originonzero / show-of-hands 已写入 accounts + candidateIds，并按赛道挂 Watch。

## 官号 mentions / silent
- 本轮 mentions：GIWA 30m（1）、Tape 30m（0）、LayerZero 24h（25 触顶）、Elysium-rest 30m（1）。各指定链都跑到，未只强化 Elysium。
- silent：Tape/电路 24h mentions（2）。silentNextAfter：**GIWA**。
- mentionsNextAfter：**DogeEVM / BTC / Starknet / squeek / STARX**（额度够时瘦栏 LZ 24h mentions 隔轮再跑）。

## 新收录（notify=true）
均已 DeepSeek 录取打分，focus=false，入库同时进 Watch。三卡都不是已确认免费 mint / 免费登记 LIVE。

1. **Blackout（@blackoutfi / https://blackoutfi.app/）** id=blackoutfi
   - 今日 22:04 CST 建号，1 粉 / 1 帖。资料栏指向官网，站点可打开（Connect wallet、0.20%、自称 GIWA 约 4 秒 sealed intent 路由，跨 GIWA / ETH / Base / Arb / OP）。$BLKT 写明 GIWA 主网之后才部署，未见 CA。官帖 22:13 CST（https://x.com/blackoutfi/status/2125231362848518147）。站点 markdown 未见回链官推，siteXMutual=partial。
   - **不是免费 mint。** 转账未实测。
   - DS admit=true，overall 60，early 95，actionable 30，risk 88。DS 栏位曾写「打新」，已覆盖为 **GIWA**（隐私/路由基础设施，不是铸造窗）。
   - Watch：userFollowWatch + giwaWatch。

2. **Origin（@Originonzero）** id=originonzero
   - 2026-11-24 03:09 CST 建号，0 粉 / 1 帖，无官网无 CA。22:33 CST 首帖（https://x.com/Originonzero/status/2125236481463886312）称 Origin is coming to Zero：无预售、bonding curve、毕业后锁流动性，并 @LayerZero_Core。
   - **不是免费 mint，也不是已开盘。** 与库内 Zeroth 并列观察（lzVerified=false，zoneHint LayerZero，ecosystem LayerZero / Zero），因本号明确挂靠 @LayerZero_Core / Zero。
   - DS admit=true，overall 43，early 92，actionable 12，risk 92。
   - Watch：userFollowWatch + layerZeroWatch + zeroWatch。

3. **Show of Hands（@0x_ShowofHands / https://showofhands.io）** id=show-of-hands
   - 2026-11-21 02:24 CST 建号，5 粉 / 154 帖。官网自称用币安 Agent ID 做一人一票免费投票、公平募资和链上预测；本轮页面显示 2 票 / 2 个投票、匹配池 0.100 BNB。Funding Round 1 写 Applications open，backing 窗口 2026-11-30 19:00 → 2026-12-04 13:00（未标明时区）。本轮未见独立开盘官帖，近帖多为回复。
   - **不是免费 mint，也不是用户 mint 的免费登记。** CA 本轮未独立核验（caUnverified=true）。
   - DS admit=true，overall 65，early 72，actionable 62，risk 58。DS 栏位曾写「打新」，已覆盖为 **BN Agent 钱包**（投票/募资工具，不是铸造窗）。
   - Watch：userFollowWatch + agentPadWatch + bnAgentWatch。

## 库内状态翻转 / 窗口更新
- **RGBStone（@RGB_Stone / https://rgbstone.com）** id=rgb-stone：**免费 mint 已结束（状态翻转，必须点名）**。官帖 22:30 CST（https://x.com/RGB_Stone/status/2125235736534303213）称 fully minted in less than 24 hours。R2150（22:11 CST）时 SatSea 仍显示 Mint price Free、已铸 8,652/9,000。本轮按官宣记为铸完/售罄（status=sold-out），未再打开 SatSea 二次计数。已保持 freeMintWatch + btcPrivacyWatch + UF。
- **Shit Capital（@shit_capital）**：付费白名单售仍是 **2026-11-24 23:00 CST**，写盘时仍在 ≤2h。leftover 未见新官帖（仅见 11-23 旧帖）。**不是免费 mint。** R2149/R2150 已提醒，不重推。公开售仍约 2026-11-25 07:00 CST。
- **Shielded Wizards（@ShieldedWizBTC）**：WL mint 仍是 2026-11-25 02:00 CST，公开售 2026-11-26 02:00 CST。尚未 ≤2h，不重推。
- **Thinkers Club（@ThinkersClub_）**：仍是 2026-11-25 02:00 CST 开 36 小时付费拍卖。尚未 ≤2h，不重推。
- **IGNIS（@Ignis_bnb）**：付费创世铸仍约 70% LIVE，无实质变化，不重推。
- **THE FORGE（@theforgeen_）**：官网仍写免费铸造已结束；此前官帖称首把铁钥匙免费。本轮无新确认，**不按已确认免费 mint LIVE 重推。**
- **Hood Havoc / Plato Unseen / Hongbao Cat（@BaocatBSC） / 蚁巢战争 / StepUp / Final Days / 7 Pad / The Belief NFT**：相对 R2150 无实质新确认，仅戳 lastChecked，不重推。
- **Stinky Penguin（@StinkyPenguinL0）**：官帖 21:39 CST 称 launchpad token 今日在 Ethereum Uniswap V2 上线，合约自称 LayerZero OFT；资料栏改为 https://rookery.stinkypenguin.xyz/ 。仍是自标 parody 的观察位，CA 未独立核验，未放入 LayerZero 核验栏。**不是免费 mint，不按新开铸单独提醒。**

## 看见但未收
- **uglypuggies（@uglypuggies）**：bio 自称 free mint 777 Robinhood … coming soon，无官网，本窗未见官发铸造帖。不覆盖录取、不建卡。
- **INSSAFUN（@Inssafun）**：R2150 已 DS admit=false，本轮不再重收。
- LineZero_NFT / LawoftheAbyss / trippiart / T0dotfun / spike__wtf / supernovers 已在库，仅软戳。
- HALEXApp 仅评论。Stinky 24h 关键词里的体育/Bramble 噪声已忽略。
- 完全 0 帖、资料栏没网址、也没人 @ 过的号，两边都可能看不见，不能承诺零漏。

## Discord Peek
- **discordPeekDeferred=true**。写盘时仍按与 R2148–R2150 相同的登录墙处理；本轮将在推送后面再尝试 computerUse，若仍是 Welcome back / 邮箱密码 / QR / passkey 墙，则 loginOk=false，未填写凭证，不改变 lastSeen。
- lastSeen 仍是 2026-11-23 22:19–22:56 CST，积压约 24h。
- 须父代理在同一轮请用户在 box 上登录 Discord，然后补 Peek 四频道（#alpha-3-new-accounts、#alpha-1-backup、#smart-accounts-tracker、#alpha-1）。补扫若出现自称免费 mint/登记，须逐个点名并挂 Watch。禁止再堆到几天后。

## 监控修补
- 入库同时进 Watch：blackoutfi → UF + giwaWatch；originonzero → UF + layerZeroWatch + zeroWatch；show-of-hands → UF + agentPadWatch + bnAgentWatch。
- 新卡 focus=false（非 squeek/toychain 类）。links.x 与 links.twitter 均已写。
- 软债 lastChecked 已戳标准 Watch。

## notify
- **notify=true**：真新 Blackout / Origin / Show of Hands（均须标明不是已确认免费 mint/登记 LIVE）+ 库内 RGBStone 免费 mint 已结束（必须点名）。Shit Capital ≤2h 不重推。Stinky 代币自称上线不单独提醒。
