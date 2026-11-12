# RESULT R1706

- round: 1706
- completedAt: 2026-11-12 16:18:03 CST
- docsSynced: true
- notify: false
- notifyReason: 本轮无合格新收录，且在库卡均未进入 ≤2h 窗（最近为 elysiumpunks 21:30 CST，窗 19:30 才开）
- newThisRound: []
- candidates: 4060
- dsFallback: false
- discordPeekDeferred: true
- lastFullAfterReset: R1692
- panel: https://reboot7454.github.io/early-scout/
- pushSha: PENDING
- pushPending: true

## xQuota
- xReads: 18
- remainingBefore: 516
- remaining: 497
- mode: pace
- softCap: 18
- minSpend: 18
- silentCap: 2
- ufCursor: 947→999 (kept 48, skip 4 NF/suspended, considered 52)
- laneReads: LayerZero/Tape/电路/GIWA/DogeEVM/BTC/Starknet 全部 true
- kwCoreRan: 挖矿
- kwCoreDeferred: 打新, Elysium, 台子/Meme, GO盘
- mentionsThin: []（因 pace softCap=18 裁掉；原计划翻到 @ZeroVaultxyz/@TapeOutWorld, @YeonPad/@LaikaSuperApp, @banknotes_btc/@Starknet）
- mentionsRest: []（因 softCap 裁掉；原计划偶数轮 @flapdotsh/@irys_xyz）
- fatShards: agentPad 721→746 kept=25 drop=0, freeMint 93→118 kept=19 drop=6, bnAgent 70→95 kept=10 drop=15, elysium 14→39 kept=24 drop=1
- lastFullAfterReset: 仍为 R1692（本轮不是重置后全量补扫）

## silentAccounts
- ran: true
- seen: 4
- sentToReview: 0
- admitted: 0
- skipped: 4
- lane: 挖矿
- index: 1
- userQuery: GPU mine
- search_users_unavailable: true
- deferredHandles: []
- skipReasons: {"too_many_posts": 4}

## 本轮结论
R1706 非全量补扫（lastFullAfterReset 仍 R1692）：6 个送审新号全部保守 skip（无独立官号+CA 或精确开盘时刻）；在库续更以刷 lastChecked 为主，实质变化：agentlifebnb 官方 sold 1,000→2,016（20%，LP 5 BNB，勿采信第三方 2330）、粉 179→695；mori-elysium 仍 free mint 收地址但无精确时刻，粉修正 61→1906；elyscan 恢复实时同步，粉 406→487；blob-on-elysium 粉 1934→2092；laika-doge 补粉 34425；unseen-ordo 补粉 5301。粉丝高于本轮 includes 的（enter-elysium 47316、elysiumpunks 5827、tapeai 3010、tapeup 2979、pairmine 978、elysdex 118、slymzcrew 5044、dogeos 179760）一律不降。今晚档期不变：clover-rh 揭示 20:00（代币+平台重启 11-13 02:00）、zerva 21:00 上 Pons、elysiumpunks $EPUNK 21:30 上 AscendLaunch（快照 21:00）、bloodstockrh open() 与 mythosbsc FCFS 22:00、boolish-rh Possession night 11-13 23:00；均未进 ≤2h 窗，le2h=false。静号路径 jirobots/cryptocom/Csilla_cro/Rotikaintel filter 全部 too_many_posts，sentToReview=0，未建卡；search_users 不可用。@Blonskr 称将确认 Behemoth 二期时间但仍无时刻，未建卡。notify=false。

## dsNote
deepseek-flash thinking-on：第一次调用（max_tokens=8000，系统要求只输出完整 JSON）即完整可解析，admits=[]，notify=false。未重试，未改用高成本模型，dsFallback=false。送审 6 个 handle 全部 skip。pace 公式在 remaining=516（预活 538 为 R1705 余量；第一脚 footer 515 故 remainingBefore=516）、距 08:00 约 15.7h 时给出 softCap=18 / minSpend=18 / silentCap=2（不是额度见底）。为卡在 softCap，UF 48 个号打成 2 条 from:；薄栏 Watch 碎段互相合并。四张厚表合计 78 个 kept handle，25 上限下需 4 条 from:，把 bnAgent 最短 3 个号（devpnl/BSCQUQU/Clawlers_）并进 must_rest 同查（未与薄栏混合），其余 75 个号重打成 3 条 fat_pack，查询数压到 18。kwCore 计划恢复 挖矿/台子/Meme/GO盘（均推迟 R1704+R1705；挖矿还曾推迟 R1700），推迟刚跑过的 打新 与只推迟一轮的 Elysium；因 softCap 又裁掉 台子/Meme 与 GO盘，本轮只跑挖矿。mentionsThin 翻到 R1702/R1703 那组（ZeroVaultxyz/TapeOutWorld、YeonPad/LaikaSuperApp、banknotes_btc/Starknet），mentionsRest 偶数轮 flapdotsh/irys_xyz，四条 mentions 全部因 softCap 裁掉，不是漏栏。六条薄栏独立 KW 均已跑。主路径 xReads=18，等于 softCap 也等于 minSpend。静号轮到 挖矿（index 1，userQuery “GPU mine”）。search_users 仍不可用，未伪造、未计入 xReads/静号已读。上轮 deferredHandles（jirobots/cryptocom/Csilla_cro/Rotikaintel）用 silentCap 第二次调用 get_users_by_usernames 一次批量解析（不占 softCap）。filter 见 4 个号全部 too_many_posts（19/23215/32026/32），deferredHandles 清空，sentToReview=0，无静号收录。18 条主查询成功后 remaining=498，再加 1 次静号档案 remaining=497（该次计入 remaining、不计入 xReads）。无翻页、无探索性重读。UF 947→999（kept 48，跳过 4 个已知 NF/suspended，considered 52）。apply_patch 未改今晚未读号（clover/zerva/bloodstock/mythos/kurogane）的档期或 lastChecked；boolish-rh 与 elysiumpunks 本轮有读同一条已记录官帖，只刷 lastChecked/粉丝（不降粉、不改档期）；未降低 enter-elysium/elysiumpunks/tapeai/tapeup/pairmine/elysdex/slymzcrew/dogeos 粉丝；未重开任何 ≤2h 窗；未给 @Blonskr Behemoth 二期编造时刻或新卡；未把 DS 编造的 UnseenOrdo 状态 ID 写入；未采信 agentlifebnb 转推 2330；未动 foome/hood-junkies/oak-agent-kit/elyfish/dotbots（本轮未读）。

## alertMessage
R1706：本轮无新收录、无 ≤2h 窗。今晚档期：elysiumpunks $EPUNK 21:30、zerva 21:00、bloodstockrh/mythosbsc 22:00、clover-rh 揭示 20:00，boolish-rh 11-13 23:00。agentlifebnb 已售 2,016 包。面板 https://reboot7454.github.io/early-scout/
