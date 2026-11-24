# RESULT R2153

写盘前远程已是 **R2152**（2ffc72c，lastScout 2026-11-24 23:04:10 CST）。本路为额度重置后的常规增量轮（不是 08:00 CST 后首轮全量补扫；全量补扫已在 R2148），升为 **R2153**。lastScout **2026-11-24 23:36:49 CST**。

面板：https://reboot7454.github.io/early-scout/

## 配额
- remainingBefore=851，xReads=26，remainingAfter=825。日额重置 2026-11-25 08:00 CST。
- 模式 ample（softCap 40，minSpend 20 已满足）。searchUsersUnavailable=true（本连接器无 search_users，沉默路径仅 mentions）。
- 未开额外/重复 X 读；同一 handle 本轮只拉一次；MUST_WIN 触顶后用 leftover from-query 补缺号，未另开分页。
- 计划搜索：UF2 + MUST_OFF + MUST_WIN + 十栏/链 KW（含 KW_GAPS）+ 4 条 mentions + SILENT_DOGE + 瘦栏 24h 关键词 3 次 + MUST_WIN leftover 2 次；合计 26 次读。remainingBefore 取上轮 remainingAfter 851。
- 30m 窗口 start 2026-11-24T15:01:00Z；24h 窗口 start 2026-11-23T15:01:00Z。

## 十栏与关键词
- 十栏关键词本轮都跑到（UF → 必盯 Watch → 关键词盲捞）。另同等扫 BTC / Starknet。
- 30m 命中：KW_LZ 1、KW_TAPE 20、KW_GIWA 14、KW_DOGE 10、KW_BTC 4、KW_STARK 1、KW_MINT 25、KW_MINE 2、KW_PAD 24、KW_GO 24、KW_ELY 16、KW_GAPS 15。MUST_OFF 30m 3。
- 同一轮 24h 补搜（因 30m <5）：**LayerZero / BTC / Starknet**（24h 各触顶 25）。挖矿 30m 为 2，属核心栏，未改成 24h。禁止把所有关键词改成 24h：已遵守。
- MUST_WIN 24h 首搜触顶 25，见到 shit_capital / DeadGridNft / FinalDays365 / RGB_Stone / FionaHippoBNB / BaekjeDotFun / TheForgeEN_ / Ignis_bnb / GiwaStepUp。MUST_WIN_LEFT（9 个缺号）再触顶 25，见到 antnestwars / 7launchpad / platounseen / baocatbsc / launchbl / thebeliefnft。MUST_WIN_LEFT2 收回 ShieldedWizBTC / ThinkersClub_ / HoodHavocNFTS（16 条，均有早于首屏的 24h 帖，并非静默）。

## userFollowWatch
- 软刷 2034→2084；shard 50（@makefunai … @play_blastoff），wrap=false。
- 下轮游标 **2084 @HelmSwap**。
- 本片软刷仅见已在库的 @makefunai（2 帖，AI 游戏向，不是铸造窗）；UF2 0 帖。无新开铸。
- 新收 mospho / enigma-sol / baofu-agent 已写入 accounts + candidateIds，并按赛道挂 Watch。

## 官号 mentions / silent
- 本轮 mentions：GIWA 30m（1）、Tape 30m（1）、LayerZero 24h（25 触顶）、Elysium-rest 30m（0）。各指定链都跑到，未只强化 Elysium。额度够时瘦栏 LZ 24h mentions 本轮已跑。
- silent：DogeEVM 24h mentions（0 条）。silentNextAfter：**BTC**。
- mentionsNextAfter：**DogeEVM / BTC / Starknet / squeek / STARX**。

## 新收录（notify=true）
均已 DeepSeek 打分，focus=false，入库同时进 Watch。本轮**没有**新的免费 mint / 免费登记 LIVE。

1. **Mospho（@TryMospho / https://mospho.trade/）** id=mospho
   - 今日 21:26 CST 建号，3 粉 / 12 帖。官网与资料栏、页脚互证（siteXMutual=yes，回链 @TryMospho）。
   - 官帖 23:30 CST（https://x.com/TryMospho/status/2125250590443700238）。自称 Robinhood Chain（4663）上按次付费研究终端，Checkout live，每请求 0.00001 ETH；$MOSPHO 自称 Live on Pons，CA 0x3519019b871f9a3f84126c17db146336f9061dd2；另有免费 Stock token desk。
   - **不是免费 mint。** 本轮未实测付款/Pons 盘口。
   - DS admit=true，overall 70，early 88，actionable 72，risk 60。栏位 **台子/Meme**。
   - Watch：userFollowWatch（无独立 Robinhood Watch 可挂）。

2. **Enigma（@_enigmasol / https://www.enigmasol.tech/）** id=enigma-sol
   - 2026-11-23 02:54 CST 建号，49 粉 / 117 帖。资料栏指向官网；本轮网页正文未见回链 @_enigmasol（siteXMutual=partial）。
   - 自称 Solana 私密市场+发射台已 Live on Solana mainnet，CA Enig2EsfQz6ajRXHWK1BGmjyt5n845MazeGamCyCiVR1。官帖 23:30 CST（https://x.com/_enigmasol/status/2125250591643611150）称自家 $ENIGMA 已从该台发出、在 Meteora DBC 交易，近 $80k mcap、费率 2.5%。
   - **不是免费 mint。** 本轮未实测发币/兑换。
   - DS admit=true，overall 64，early 72，actionable 75，risk 55。栏位 **台子/Meme**。
   - Watch：userFollowWatch。

3. **baofu（@baofuagent_ai / https://baofuagent.agency/）** id=baofu-agent
   - 2026-01-15 17:21 CST 建号，仅 2 粉 / 24 帖，老号低粉。官网与资料栏互证（siteXMutual=yes，回链 @baofuagent_ai）。
   - js/config.js 写明 NETWORK='mainnet'，注释称主网已上线 2026-11-23；静态 HTML 默认 TESTNET 标签会被 JS 改成 BSC。主网 sale 0x88E7d1bba25230619C4D1576A21181445a60aC7d，token 0xF4469b309223dC6ea25E45dd7378Fc360d957834。
   - 机制：持 Agent ID 铸造，总份 444,000，基价 0.002 BNB、126 档至 0.00876 BNB，每笔最多 10 份，10,000 份开池、LP 送黑洞；买 2% 全烧、卖 2% 分红。静态页默认显示 0/444,000，本轮 BSC eth_call 被 Auto-review 拦截、BscScan 403，**未独立复核链上 totalMinted**。
   - 官帖 23:05 CST（https://x.com/baofuagent_ai/status/2125244431339295036）只讲机制，未写 already live / 已铸数。
   - **不是免费 mint。**
   - DS admit=true，overall 55，early 70，actionable 55，risk 78。DS 栏位曾写「打新」，已覆盖为 **BN Agent 钱包**。
   - Watch：userFollowWatch + agentPadWatch + bnAgentWatch。

## 库内状态翻转 / 窗口更新
- **Shit Capital（@shit_capital / https://shitcapital.com/）**：官帖 23:02:17 CST（https://x.com/shit_capital/status/2125243614045642823）宣布 Shit Capital is now live，**确认付费白名单售已开**（R2152 到点但未见官帖）。官网本轮仍显示 Loading contract address，未见已筹数字。公开售仍约 2026-11-25 07:00 CST。**不是免费 mint。** 仍 le2h。R2149 已预告，本轮补官帖确认并点名。
- **Hood Havoc（@HoodHavocNFTS）**：本轮 leftover2 所见仍是此前「dates moved」官宣，无新日程。已把卡片里过期的 schedule.gtdAt / publicAt（仍写 11-25 / 11-26）改正为 GTD 2026-12-01 00:00 CST、FCFS 12-02、Public 12-03。R2150 已提醒，不重推。
- **Shielded Wizards（@ShieldedWizBTC）**：WL mint 仍是 2026-11-25 02:00 CST（约 2.4h），公开售 2026-11-26 02:00 CST。发射台/WL Checker 此前已报 live。尚未 ≤2h，不重推。
- **Thinkers Club（@ThinkersClub_）**：仍是 2026-11-25 02:00 CST 开 36 小时付费拍卖（Ink 上 USDC/ETH）。尚未 ≤2h，不重推。
- **Final Days / DeadGrid / Fiona the Hippo**：R2152 已报 LIVE，本轮无实质新确认，不重推。
- **RGBStone**：R2151 已铸完，不重推。
- **IGNIS / THE FORGE / Hongbao Cat / Plato Unseen / 蚁巢战争 / 7 Pad / The Belief NFT / Baekje / Ballast GIWA / GiwaStepUp**：相对上轮无实质新确认，仅戳 lastChecked，不重推。

## 看见但未收
- **HODL AGENT（@HODL_LP / https://www.hodlpads.club/）**：2026-11-10 建号，94 粉 / 2 帖，官网与资料栏互证。官帖称 Base 发射台 is live 并给 EVM CA，官网却写 Solana / Pump.fun，Tokens launched 0、launches open soon。链互相矛盾且零发射。DS admit=false，不收录。
- **Socivexa（@SocivexaFi / https://socivexa.fun/）**：今日 23:04 CST 建号，2 粉。官网互证，自称 SocialFi 推荐分成路由，却挂 $4.8M USDC 已结算等大数字，与新号严重不符，更像演示数据。无发币、无免费 mint。DS admit=false，不收录。
- LycheeUni：仅预测市场教学向，不收。
- LawoftheAbyss / Vicehood_RH / numencash / playblocq / MMIX_io / Ammora / PlunderPort / T0dotfun / buzzchain_io / medusa_io：仅第三方或已在库，不重收。
- CheesePad 仍未找到官推，不单独建台子卡。
- MUST_OFF 见到 flapdotsh 闲聊、Blonskr 回复提到 AntNestWars/TapeLaunch，均已在库。
- 11-25 日期检索除优先项外只见已在库的 chunky-kongs（日程过期），不重收。
- Bramble 儿童绘本噪声已忽略。
- 完全 0 帖、资料栏没网址、也没人 @ 过的号，两边都可能看不见，不能承诺零漏。

## Discord Peek
- **discordPeekDeferred=true**。写盘时仍按与 R2148–R2152 相同的登录墙处理；本轮将在推送后再尝试 computerUse，若仍是 Welcome back / 邮箱密码 / QR / passkey 墙，则 loginOk=false，未填写凭证，不改变 lastSeen。
- lastSeen 仍是 2026-11-23 22:19–22:56 CST，积压约 25h。
- 须父代理在同一轮请用户在 box 上登录 Discord，然后补 Peek 四频道（#alpha-3-new-accounts、#alpha-1-backup、#smart-accounts-tracker、#alpha-1）。补扫若出现自称免费 mint/登记，须逐个点名并挂 Watch。禁止再堆到几天后。

## 监控修补
- 入库同时进 Watch：mospho → UF；enigma-sol → UF；baofu-agent → UF + agentPadWatch + bnAgentWatch。shit-capital 官帖确认后保持/补挂 UF。
- 新卡 focus=false（非 squeek/toychain 类）。links.x 与 links.twitter 均已写。
- Hood Havoc 过期 schedule.gtdAt/publicAt 已改正。
- 软债 lastChecked 已戳标准 Watch。
- 在库必盯号本轮均能从 MUST_WIN / leftover 覆盖到，无「在库不在 Watch」新 bug。

## notify
- **notify=true**：真新 Mospho / Enigma / baofu（三项都不是免费 mint，须在告警里标明）+ 库内 Shit Capital 官帖确认付费白名单售已 LIVE（点名，不是免费 mint）。本轮无新的免费 mint / 免费登记。Shielded Wizards / Thinkers Club 距 02:00 CST 开窗仍约 2.4h，尚未 ≤2h，不按 le2h 推送。
- discordPeekDeferred=true，即便推送后仍须父代理补 Discord Peek。
