# R2090 早期打新雷达

写盘前远程已是 R2089（ecde100，Discord alpha 补收 coinductor / playluckyguard / ideafun_io / smooveoffsol / jesterdotfun / blackwater_z26，lastScout 2026-11-21 14:04 CST）。本路 X 雷达升为 **R2090**，保留这 6 张卡并为它们补挂 Watch（入库时未进任何 Watch，属监控 bug，当场修复）。

## 配额
- 模式 ample；softCap 28；本轮 xReads=30（主查询 + silent BTC + 瘦栏 24h LZ/BTC/Starknet）。
- remainingBefore=638，remainingAfter=608。
- 未开额外/重复 X 读；同一 handle 只拉一次；无分页。
- getUsers: 0。searchUsersUnavailable=true。
- 未跑可选 MEN_TAPE（24h 瘦栏补搜已近/超 softCap）。
- lastFullAfterReset: R2072。

## 十栏与关键词
- 十栏关键词本轮都跑到（核心肥词 30m + 瘦栏 30m + 专名补漏 KW_GAPS）。
- 30m 瘦栏命中：LZ 0、Tape 10、GIWA 5、DogeEVM 21、BTC 0、Starknet 3。
- 同一轮 24h 补搜：LZ / BTC / Starknet（均 capped 25）。GIWA 30m=5、Tape 30m=10、DogeEVM 30m=21，未拉 24h。
- 禁止把所有关键词改成 24h：已遵守。

## userFollowWatch
- 软刷 1734→1784；kept 50，walk 50，skip_already=[]，NF_skip=0，wrap=false。
- firstKept @securityum_xyz，lastKept @BagDropSocial。
- 下轮游标 **1784 @nullclawio**（本地 R2089 草稿曾把 nextStart 留在 1734，本轮已纠正）。
- 本片作者均已在库，无真新官号。
- 库内 @Zero_Kitties 首次核到 WL application 已开（官帖 10:43 CST）。
- 新收 @appcityhood @PaydPad 已写入 accounts + candidateIds。

## 官号 mentions / silent
- 本轮 mentions：MEN_GIWA 24h（has:mentions GIWA/GIWA_by_Upbit 或 @GIWALAUNCHPAD / @GIWA_by_Upbit，25 帖封顶未翻页）。覆盖 GIWA 挂靠。
- mentionsNextAfter：Tape。
- silent：BTC（24h 6 命中，无 0 帖新官号可收）。searchUsersUnavailable=true。
- silentNextAfter：Starknet。

## 新收录（notify=true）
1. **CITYHOOD（@appcityhood / https://cityhood.fun）** id=cityhood
   - 建号 2026-11-03 20:19:04 CST，27 粉 / 10 帖 / 3 关注。资料栏与官网互证（页面写 follow @appcityhood）。
   - 官帖 13:57:06 CST 2124019251207901688，自称 Robinhood Chain（4663）4,333 份街区 NFT，走 OpenSea SeaDrop。
   - 官网本轮 Minted 0/4,333。GTD 500 份免费抽奖（每钱包 1）、WL 1,000 份 $0.50、Public 2,833 份 $1.50 / 约 0.000923 ETH（每钱包 25）。GTD+WL：关注+转发+评论钱包，公开开奖。
   - **公售 2026-11-21 22:00 CST（14:00 UTC）**，本轮核验时约 7.92h，le2h=false，尚未 LIVE。GTD 免费是抽奖，**不是全员免费 mint LIVE**，也不是已开放的免费登记表单。
   - 本轮未见 OpenSea 集合直链，未链上复核。勿与 @CityHood_NFT / cityhood.online 混淆。
   - DS admit=true，overall 70，early 80，actionable 72，risk 55。focus=false。
   - Watch：userFollowWatch + freeMintWatch。
2. **Payd（@PaydPad）** id=paydpad
   - 建号 2026-11-21 11:33:58 CST，0 粉 / 3 帖 / 0 关注。资料栏无 URL，本轮未见独立官网。
   - 官帖 13:55:34 CST 2124018867080991026 自称 Introducing $Payd：可替没有钱包的人在 PumpFun 发射，75% 创作者费用走 Apple Cash。
   - **不是免费 mint**。未见合约，未实测发射或打款。
   - DS admit=true，overall 48，early 88，risk 85。focus=false。
   - Watch：userFollowWatch。

## 写盘前已在 R2089 入库、本路补报并补挂 Watch
- Coinductor（@coinductorai）：Robinhood Chain 交易 Agent 回测/运行，极早期，不是免费 mint。补挂 userFollowWatch + agentPadWatch。
- Lucky Guardians（@playluckyguard）：Solana idle，预售中，不是免费 mint。补挂 userFollowWatch。
- IdeaFun Lab（@ideafun_io）：Experiment #001 The Vault，无入口/合约，不是免费 mint。补挂 userFollowWatch。
- SMOOVE（@smooveoffsol）：Solana meme 已发射，不是免费 mint。补挂 userFollowWatch。
- JESTER（@jesterdotfun）：Solana meme 已发射，不是免费 mint。补挂 userFollowWatch。
- Blackwater（@blackwater_z26）：自称 MINT IS LIVE，未见免费、未见链与供应量核验，**不是已确认免费 mint LIVE**。补挂 userFollowWatch。
- 六卡 links.twitter 已按 links.x 补齐。分数仍沿用 R2089 写入的 1–10 量纲，本轮未重打。

## 已提醒、不重推
- Zero Kitties：UF 见到 10:43:46 CST 官帖 2123970597583810883，WL application 已开（https://zerokitties.xyz），自称 2,222 份 on-chain。是白名单申请，不是已开铸免费 mint LIVE，未见开铸钟点。R1803 已收录，已补官网并刷新卡片，不按新卡重推。
- bons-world：MUST 2h 未见新帖，仍是 13:30 CST 白名单关闭帖；今晚 20:00 CST 免费 WL mint 等日程未见改期（约 6h，le2h=false）。R2081 已提醒，不重推。
- Hood Drive：MUST 仍见 13:00 CST「12 hours / Free mint on OpenSea」官帖，开铸仍 2026-11-22 01:00 CST（约 11h），不是改期，尚未 LIVE。R2087 已覆盖，不重推。
- MARIO：免费 mint 仍 LIVE，关窗口径此前记为今晚 23:00 CST；本轮 MUST 未见改期官宣。不重推。
- PredictAgent：MUST 2h 无新官帖，仍今日 22:30 CST Stage 1 付费 mint，未到 ≤2h。R2040/R2045 已提醒。
- TapeAI：MUST 未见新的精确开盘钟点，「今晚发射」口径未变，尚未 ≤2h。不重推。
- FomoFuZZ / Robin Yield / tribe3tech / LightDAO / QBIT / Chimi / StockBox / FEEgent：本轮 MUST 无新窗，不重推。
- CITYHOOD 公售本轮核验时尚未 ≤2h，只作为新收录提醒一次，不另报倒计时。

## 看见但未收
- NORI Launchpad（@NORIGIWA）：2026-11-19 建号、1 粉 / 1 帖，简介自称 GIWA 发币台；唯一帖是 X Article（抓取 403），公开搜索无官网、无合约、无互证。DS admit=false。勿与库内 noritafarm 当成同一项目。
- @FlickerrNft：仅见转述与 Garasu 合作赠票，资料栏写 Full time Community Manager，不是项目官号，未收录。
- @CityHood_NFT / cityhood.online：搜索中出现的另一套 16x16 浮岛游戏/自称免费 mint，与本轮新收的 @appcityhood / cityhood.fun 不是同一项目；本轮未对其官号做独立 X 核验（避免额外读），未收录。
- PandalZero / Garasu / Trippi 等库内项目的第三方赠票转发，不重收。
- Discord 增量里 woodlandz_xyz / gettroopers / rezofun / baggieshood / joinseedborn 等已在库并已在 Watch，不重收。

## Watch / 漏挂
- 新卡入库同时进 Watch：@appcityhood → userFollowWatch + freeMintWatch；@PaydPad → userFollowWatch。
- R2089 六张 Discord 卡当场补挂 Watch（见上）。
- 库内 zero-kitties 已在 userFollowWatch + freeMintWatch，本轮只补官网/状态，未重复挂入。
- 本轮未做历史库「在库不在任何 Watch」大表回填（避免一次把数百旧卡塞进 UF）。
- 软债 lastChecked 已刷新：cantonPadWatch / glazeWatch / tokenWorksPlaygroundWatch（及同族 cantonWatch / tokenWorksWatch 若存在），以及 freeMintWatch / agentPadWatch / elysiumWatch / tapeWatch / kinetiqWatch / layerZeroWatch / dogeEvmWatch / btcPrivacyWatch / starknetWatch / giwaWatch / tapeOutWatch / miningWatch / bnAgentWatch。

## Discord
- discordPeekDeferred=**false**。写盘前远程 R2089 已完成增量 Peek：loginOk=true，读卡约 59（alpha-3 34 / backup 8 / smart 3 / alpha-1 14），spideyPosting=true。
- lastSeenByChannel（未再改）：alpha-3-new-accounts 2026-11-21 13:58 CST，alpha-1-backup 14:00，smart-accounts-tracker 13:44，alpha-1 14:00。
- 四频道 passedCutoff=true 且 capped=false，本窗口增量已追上。11/15–11/18 更早积压仍不在增量范围。
- 本路未再派 computerUse（避免抢同一桌面；Peek 已完成）。

## notify
- notify=true。必须点名新收录 CITYHOOD（公售今晚 22:00 CST，GTD 免费是抽奖，不是全员免费 mint LIVE）和 Payd（不是免费 mint）；并补报 R2089 Discord 六卡（均不是已确认免费 mint LIVE）。
- 文案见 meta.alertMessage。
