# RESULT R1703

- round: 1703
- completedAt: 2026-11-12 14:40:37 CST
- docsSynced: true
- notify: false
- notifyReason: 无新收录且无仍开 2h 窗
- newThisRound: []
- candidates: 4060
- dsFallback: false
- discordPeekDeferred: true
- lastFullAfterReset: R1692
- panel: https://reboot7454.github.io/early-scout/

## xQuota
- xReads: 28
- remainingBefore: 605
- remaining: 576
- mode: ample
- softCap: 28
- minSpend: 20
- silentCap: 2
- ufCursor: 759→831 (kept 50, skip 22 NF/suspended, considered 72)
- laneReads: LayerZero/Tape/电路/GIWA/DogeEVM/BTC/Starknet 全部 true
- kwCoreRan: 打新, 挖矿, 台子/Meme, GO盘
- kwCoreDeferred: Elysium
- mentionsThin: @ZeroVaultxyz/@TapeOutWorld, @YeonPad/@LaikaSuperApp, @banknotes_btc/@Starknet
- mentionsRest: @fulldotfun/@PulseLaunchpad
- fatShards: agentPad 646→671 kept=20 drop=5, freeMint 18→43 kept=15 drop=10, bnAgent 277→20 kept=17 drop=8, elysium 207→232 kept=25 drop=0
- lastFullAfterReset: 仍为 R1692（本轮不是重置后全量补扫）

## silentAccounts
- ran: true
- seen: 24
- sentToReview: 0
- admitted: 0
- skipped: 24
- lane: BTC
- index: 9
- userQuery: Ordinals mint
- search_users_unavailable: true
- deferredHandles: ["PPRGBthereal", "Stacks", "MrEdogtagnft", "frogpoleon", "Shahiniram", "housebets", "awenwenfeng", "juga_btc", "ShieldedNakaCN", "_genk__"]
- skipReasons: {"too_many_posts": 8, "already_in_library": 5, "profile_unresolved": 10, "deferred_overflow": 1}

## 本轮结论
本轮无合格新收录，admits 为空。送审新号全部 skip：deployanchor / MuseAICoin / BubbleonTg / XomoPay / VamCat_fun 均无 CA 或精确开盘时刻；PostageVault 连续多轮无 CA/时刻；Wisnux97 与 sultonnel 仅为已在库 Grokiefun 喊单；bmw123v / Joysaha2020 为 Ammora 等待名单喊单；itzkachides 为火箭互动诱饵；BaceHitom 为空喊。静号 BTC 栏未见送审。在库续更：elysiumpunks 官帖确认 $EPUNK 今日 21:30 CST 上 AscendLaunch（最终快照 21:00 CST，未见 CA，未进 ≤2h）；dualforge-bsc 官宣 Mint 开闸 2026-11-15 19:00 CST（Binance Agent ID 专属）；danta 补价格 0.0013525 BNB、每钱包上限 5；joayo-fun 称 Giwa Sepolia 已列入 Chainlink Data Streams 支持网；agenticrobotrbh 称仍在开发且代币已锁。enter-elysium 无新 mint。今晚 clover-rh 20:00、zerva 21:00、bloodstockrh / mythosbsc 22:00 均未进窗；kurogane-fun 仍不在今晚名单。完成时无仍开 2h 窗。

## dsNote
deepseek-flash thinking-on：第一次调用（max_tokens=8000，系统要求只输出完整 JSON）即完整可解析，admits=[]，notify=false。未重试，未改用高成本模型，dsFallback=false。送审 12 个 handle 全部 skip。must 仍拆成 Enter_Elysium 与 hamster/Ascend/squeek 两条；AscendLaunch 已在本轮 UF 分片中读取故 must_rest 仅 hamster/squeek，后两条 0 帖，无需补查。UF 50 个号因句长拆成 3 次查询，主路径 xReads=28，恰好软顶 softCap 28，不低于 minSpend 20。静号 BTC 栏 search_users 不可用未伪造，提及搜索 seen=24 sentToReview=0 admitted=0，deferredHandles 留下 10 个第三方提及待下轮静号档案批次，未另占 softCap。apply_patch 未把 DS 的 status=tracking 或把 typo id=gwahook 写回已有卡；elysiumpunks 因本轮核到官帖原文而写入 21:30 CST 档期，未编造 CA；dualforge-bsc 按官帖写入 11-15 19:00 CST。

## alertMessage
R1703：无新收录、无 ≤2h 窗。今晚 20:00 CST clover-rh 揭示、21:00 zerva 上 Pons、21:30 elysiumpunks $EPUNK 上 AscendLaunch、22:00 bloodstockrh / mythosbsc，均在库且未进窗。看板：https://reboot7454.github.io/early-scout/
