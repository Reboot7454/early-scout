# RESULT R1724

- round: 1724
- completedAt: 2026-11-13 02:18:21 CST
- docsSynced: true
- notify: true
- notifyReason: 补收 hood-havoc、elythoria（并行 tight R1723 因裁栏未收）；clover-rh 仍在 ≤2h。
- newThisRound: ["hood-havoc", "elythoria"]
- candidates: 4065
- dsFallback: false
- discordPeekDeferred: true
- lastFullAfterReset: R1692
- userOrderedFull: R1715
- panel: https://reboot7454.github.io/early-scout/
- pushSha: PENDING
- pushPending: true
- priorR1723pushSha: ca2b491 (ca2b49103bb4b89437778e2b8c2f32803d4a3180)

## 新收录
- hood-havoc（@HoodHavocNFTS，打新 / Robinhood Chain NFT，score 63，announced，focus=false）：官帖公布 GTD 11/25、Public 11/26，5555 枚，至少一半免费 GTD、合格钱包最多 4；官网 hoodhavoc.com 写明非 Robinhood 官方、概念开发中；暂无 CA。已入 freeMintWatch。
- elythoria（@elythoria，台子/Meme，score 45，announced，focus=false）：bio 挂靠 @Enter_Elysium 发币，建号 11/9、粉 1463、仅 5 帖；无官网/自身官帖/CA/精确时间，第三方倒计时不作为开铸确认。已入 elysiumWatch。
- skip phew（@phew_pro）：建号 2025-12、8.7k 粉，launchpad 已上线并推 Season 1 空投，偏成熟，非极早期。
- meta.newThisRound=["hood-havoc","elythoria"]。candidateCount=4065。
- 说明：以上两张是对已推送 tight R1723（02:11 CST，sha ca2b491，0 新卡）的漏报补收。该轮 softCap=10 裁掉核心 KW 与 mentions；本补扫按 ample 跑全栏后独立捞到。不覆盖 R1723 的 Clover/FarmFilch 结论。

## xQuota
- xReads: 25（主路径 24；静号 1 次，不占 softCap）——为本次补扫另行计数，不含 tight R1723 的 10 次
- remainingBefore / remaining: 不以本扫描 footer 为准（见下）
- footerClaimed: remainingBefore=1000，remaining=975（与 R1722 收工 122、并行 R1723 开跑 105 / 收工 91 冲突，存疑）
- mode: ample-supplement
- softCap: 40
- minSpend: 20
- silentCap: 2
- ufCursor: 342→380（本补扫实际从 R1722 的 290 扫到 380，kept 88, skip 2 already-read, considered 90；已推送 R1723 停在 342，下一轮从 380 续）
- laneReads: LayerZero/Tape/电路/GIWA/DogeEVM/BTC/Starknet 全部 true
- kwCoreRan: 打新, 挖矿, 台子/Meme, GO盘, Elysium
- kwCoreDeferred: 无
- mentionsThin: LayerZero, Tape/电路, GIWA, DogeEVM, BTC, Starknet
- mentionsRest: Enter_Elysium, kinetiq_xyz, AgentKinetiq, squeekchain, NutshellMarkets, starx_xlayer, PulseLaunchpad, flapdotsh, irys_xyz, fulldotfun, arcxtrade
- fatShards: 已推进 — agentPad 276→301（25 个已在本扫描 UF 覆盖，未另开 from:）；freeMint 40→65（11 个已在 UF2，余 14 查询，0 帖）；bnAgent 103→128（0 帖）；elysium 61→86（0 帖）。nAccounts：762 / 372 / 283 / 269。R1723 未推进的 nextStart 由此补上。
- le2hSupplement: false
- lastFullAfterReset: 仍为 R1692（不是 08:00 CST 重置后首轮全量补扫）
- userOrderedFull: 仍为 R1715
- 注：无探索性重试、无翻页。十栏关键词（薄栏 6 + 核心 5）都跑到。userFollow 软刷完成。下一轮开跑必须重核官方 footer remaining。

## silentAccounts
- ran: true
- seen: 0
- sentToReview: 0
- admitted: 0
- skipped: 0
- lane: GIWA
- index: 7
- userQuery: GIWA launch
- search_users_unavailable: true
- mentionQuery: has:mentions (GIWA OR GIWA_by_Upbit) (mint OR launch) -is:retweet
- mentionRan: true
- deferredHandles: []
- 注：silentCap=2。第一槽 search_users 不可用，未伪造。第二槽按计划跑了 GIWA mentions（计入静号，不占 softCap）；主要为已在库 Ammora/deuslaunch 宣传，新静号 admit=0。tight R1723 因 silentCap=1 只计划 search_users、未跑第二槽。

## 本轮结论
R1724 为已推送 tight R1723（02:11 CST，sha ca2b491）之后的补扫：新收 2 张卡（hood-havoc、elythoria），skip phew。Clover / FarmFilch 结论沿用 R1723：clover-rh 官方 01:51 CST 宣布 $CLV 已在 Robinhood Chain 上线，官帖代币 CA 0x500908d166d9adfb76ea226e6c1619ab25a6da07，旧自报 CA 0x1ead1942232dae5a296eea527b7feb871941d960 已保留；DexScreener 对官帖 CA 暂 0 交易对，目前只索引到旧地址的池，不能把任一地址当成唯一确定交易标的；窗口至约 04:00 CST，仍 ≤2h，粉丝 KEEP 3994。farm-filch 窗口已过，仍无官方开铸确认、无 mint CA，le2h=false。lockpad 02:06 CST 再发几乎相同「Lockpad is live.」，官网仍写功能不可用，不改为真正 live，本补扫补刷 lastChecked（R1723 未触及）。Canton/Glaze/TokenWorks lastChecked 已刷。notify=true。discordPeekDeferred=true。

## 粉丝上调（仅升不降）
本补扫新上调：raeto 2079->2082、1k-art-gallery 32->343。shoutoutloudio 已在 R1723 调至 39，保持。R1723 已写入的 lil-giraffies/enter-elysium/globemkts/2hourfun/stillwater-play/vaubanworks 不上调回退。clover-rh KEEP 3994。

## dsNote
deepseek-flash thinking-on：max_tokens=16000，第一次调用即完整可解析 JSON。admits=hood-havoc（overall 63）、elythoria（overall 45，因 Elysium 部署证据不足进台子/Meme 低置信）。skip phew（已过热）。Clover/FarmFilch 文案沿用已推送 R1723（含 DexScreener 差异）。新卡 focus=false。粉丝只上调。search_users 不可用；silentCap=2 的第二槽 GIWA mentions 已跑。未走 dsFallback。

## alertMessage
🔔 R1724 补收：Hood Havoc（Robinhood Chain NFT，GTD 11/25、Public 11/26，至少一半免费 GTD，暂无 CA）与 elythoria（Elysium bio 挂靠发币台，低置信，无官帖/CA）。Clover $CLV 仍在约 04:00 CST 窗口，官帖 CA 0x500908d166d9adfb76ea226e6c1619ab25a6da07 与旧 CA 不一致，DexScreener 暂只索引到旧地址的池，请自行核对、勿把未核验地址当唯一标的。面板：https://reboot7454.github.io/early-scout/
