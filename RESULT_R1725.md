# RESULT R1725

- round: 1725
- completedAt: 2026-11-13 02:46:29 CST
- docsSynced: true
- notify: true
- notifyReason: clover-rh 仍在约 04:00 CST 前的 ≤2h 窗口，按规则必须 notify=true；本轮无新收录、无新官帖。
- newThisRound: []
- candidates: 4065
- dsFallback: false
- discordPeekDeferred: true
- lastFullAfterReset: R1692
- userOrderedFull: R1715
- panel: https://reboot7454.github.io/early-scout/
- pushSha: a464e8e (a464e8e220cd85091bc590909629b6cfd8451796)
- pushPending: false

## 新收录
- 无。meta.newThisRound=[]。candidateCount=4065。

## xQuota
- xReads: 10（主路径 10；静号 0 次，不占 softCap）
- remainingBefore: 91
- remaining: 81
- mode: tight
- softCap: 10
- minSpend: 10
- silentCap: 1
- ufCursor: 380→420（considered 40，kept 29，skip 11 为 NF_skip 未重打：wedowtf、bsc_bito、cachetdotfun、turbokartbnb、seppidev、manekinecoinft、tikitotemsbnb、nonce_cto、stonkaxyz、claudesprotocol、babelagent）。下一轮从 420 续。
- laneReads: LayerZero/Tape/电路/GIWA/DogeEVM/BTC/Starknet 全部 true
- kwCoreRan: 无
- kwCoreDeferred: 打新, 挖矿, 台子/Meme, GO盘, Elysium
- mentionsThin: 延后（softCap=10 优先薄栏 Watch 2 次全名单，与 R1723 tight 相同）
- mentionsRest: 延后
- fatShards: 未推进，nextStart 仍为 agentPad 301 / freeMint 65 / bnAgent 128 / elysium 86
- lastFullAfterReset: 仍为 R1692
- userOrderedFull: 仍为 R1715
- 注：开跑重核官方 footer remainingBefore=91（与 R1723 收工 91 一致；R1724 曾声称 1000/975 不予采用）。无探索性重试、无翻页。thin2 查询里 SealonGIWA 曾误写为 SealonGIwa，用户名大小写通常不敏感，未另开读。

## silentAccounts
- ran: true
- seen: 0
- sentToReview: 0
- admitted: 0
- skipped: 0
- lane: BTC
- index: 9
- userQuery: Ordinals mint
- search_users_unavailable: true
- mentionQuery: has:mentions (Ordinals OR CRC20 OR ShieldedNaka) (mint OR launch) -is:retweet
- mentionRan: false
- deferredHandles: []
- 注：silentCap=1，计划仅第一槽 search_users；当前 X 客户端无该工具，未伪造结果，也未把第二槽 mentions 改打进静号（silentCap<2）。

## 本轮结论
R1725 tight：无新收录。clover-rh 本轮无新于 01:51 CST 的官帖，窗口仍至约 04:00 CST，status=live、le2h=true；官帖 CA 0x500908d166d9adfb76ea226e6c1619ab25a6da07 在 DexScreener 仍 0 个交易对，旧 CA 0x1ead1942232dae5a296eea527b7feb871941d960 仍有 Robinhood Uniswap 池（其一流动性约 3948.29 USD），勿把任一地址当成已核验唯一标的；粉丝读数 3749，保持 3994。farm-filch 本轮未再打官号，沿用已关闭窗口且未确认开铸。globemkts 官方复述同一 Nov 30 / Founding trader 日程。giwahook peg 模式属 R1716 已记录能力。Canton/Glaze/TokenWorks 仅刷 lastChecked。notify=true。discordPeekDeferred=true。

## 粉丝上调（仅升不降）
globemkts 765→775、solz-money 4→106、tokentunes 2985→3069、madang-fun 519→520；gasokfun 原无字段，写入 189。clover-rh KEEP 3994；giwahook KEEP 37；lumora-agent KEEP 953。未把 alt @BIBIAI_MEME 的 3392 粉写入主号 bibi-ai/@bibiainft。

## dsNote
deepseek-flash thinking-on：max_tokens=16000，第一次调用即完整可解析 JSON。admits=[]。模型误把 notify 写成 false；按硬规则（mint/open≤2h）改回 notify=true，未走 dsFallback。search_users 不可用。

## alertMessage
🔔 R1725：无新收录。Clover $CLV 窗口仍至约 04:00 CST；官帖 CA 0x500908d166d9adfb76ea226e6c1619ab25a6da07 与旧 CA 0x1ead1942232dae5a296eea527b7feb871941d960 不一致，DexScreener 仍只索引到旧地址的池，请自行核对、勿把未核验地址当唯一标的。面板：https://reboot7454.github.io/early-scout/
