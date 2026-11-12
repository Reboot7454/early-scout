# RESULT R1705

- round: 1705
- completedAt: 2026-11-12 15:49:29 CST
- docsSynced: true
- notify: false
- notifyReason: 本轮无合格新收录；在库卡中无仍开 ≤2h 窗（clover-rh 揭示 20:00 CST，最早 18:00 才进窗）。
- newThisRound: []
- candidates: 4060
- dsFallback: false
- discordPeekDeferred: true
- lastFullAfterReset: R1692
- panel: https://reboot7454.github.io/early-scout/
- pushSha: aaa66af8576d2c8bae41f391b84989b5e0aaa7c9
- pushPending: false

## xQuota
- xReads: 18
- remainingBefore: 557
- remaining: 538
- mode: pace
- softCap: 18
- minSpend: 18
- silentCap: 2
- ufCursor: 892→947 (kept 48, skip 7 NF/suspended, considered 55)
- laneReads: LayerZero/Tape/电路/GIWA/DogeEVM/BTC/Starknet 全部 true
- kwCoreRan: 打新
- kwCoreDeferred: GO盘, Elysium, 挖矿, 台子/Meme
- mentionsThin: []（因 pace softCap=18 裁掉；原计划保持 @PlunderPort/@TapeAIAgent, @GIWA_by_Upbit/@DogeOS, @ShieldedNaka/@Bramble_fi）
- mentionsRest: []（因 softCap 裁掉；原计划奇数轮 @fulldotfun/@PulseLaunchpad）
- fatShards: agentPad 696→721 kept=24 drop=1, freeMint 68→93 kept=19 drop=6, bnAgent 45→70 kept=7 drop=18, elysium 257→14 kept=25 drop=0
- lastFullAfterReset: 仍为 R1692（本轮不是重置后全量补扫）

## silentAccounts
- ran: true
- seen: 35
- sentToReview: 0
- admitted: 0
- skipped: 35
- lane: 打新
- index: 0
- userQuery: fair mint
- search_users_unavailable: true
- deferredHandles: ["jirobots", "cryptocom", "Csilla_cro", "Rotikaintel"]
- skipReasons: {"too_many_posts": 28, "already_in_library": 3, "profile_unresolved": 4}

## 本轮结论
R1705 无合格新收录，admit 为空。12 个送审号中 5 个为 Ammora 等待名单喊单、2 个仅转推 PlunderPort 等待名单，另有多轮重复 skip 的 PostageVault、非加密的 Copper12Studios、仅转 CoinDesk DogeOS 新闻的 uwantuget1/DecileFlow、只回复 GIWA @ 串的 gooner7788、以及评论半导体新闻的 OpalMistfkc，均无独立官号+CA 或精确开盘时刻，全部 skip。在库续更：tapeai、tapeup 为 X Layer×TapeOut 黑客松拉票/榜单（不设窗、非 Elysium）；kleos-elysium 再销毁 800 万 $Kleos（粉更正 2533）；qhooks 图表/launch 视觉/资料页命名等产品更新（粉 56→309）；kestrixspace Creator check live 与 Pons 钱包数据披露（粉 0→92）；hoodrai 与 Ape Hood 合作（粉 1333）；akadotfun 三阶段算法策略（粉 23646）；floorfeeders 本币金额读数；elyspay/artasmonkey/toshi-pad/kurvfun/pairmine 仅刷 lastChecked 与粉丝；enter-elysium 5 帖均为短回复/转推无新开盘（includes 47305）。另有 @Blonskr 仅称会去确认 Behemoth 二期开放时间、未给时刻，无法对应到确切在库卡故仅在此提及，不新建卡、不设窗。hamster-hour/squeekchain/AscendLaunch 合并查询 0 帖，alpha-pad/open-ember/quoted-xyz 及 packswap/digigolds/giwapad-xyz/giwahook/joayo-fun/silicon-dreamers/void-giwa 均只刷 lastChecked，档期与 CA 不变。今晚档期保持：clover-rh 20:00 CST 揭示、zerva 21:00 CST 上 Pons、$EPUNK 21:30 CST 上 AscendLaunch（快照 21:00）、bloodstockrh 与 mythosbsc 22:00 CST、boolish-rh 11-13 23:00 CST；现在约 15:48，全部 le2h=false，kurogane-fun 的 GTD/WL 已于 11-10 截止不上榜。本轮 notify=false。

## dsNote
deepseek-flash thinking-on：第一次调用（max_tokens=8000，系统要求只输出完整 JSON）即完整可解析，admits=[]，notify=false。未重试，未改用高成本模型，dsFallback=false。送审 12 个 handle 全部 skip。pace 公式在 remaining=557、距 08:00 约 16.3h、预估 32 轮时给出 softCap=18 / minSpend=18（不是额度见底）。为卡在 softCap，UF 48 个号打成 2 条 from:；薄栏 Watch 碎段互相合并、厚表碎段互相合并（从未薄+厚、从未把薄栏 KW 并进 Elysium/BNB/RH）。因 fat_freeMint(19)+fat_bnAgent(7) 合并后会超 25 柄/512 字，把 Silicon_Dreamer 打进 fat_agentPad，其余 25 个号并成 fat_rest，查询数压到 18。kwCore 计划恢复打新/挖矿/台子/Meme（打新为 R1704 推迟后的最长待恢复），推迟 GO盘 与刚跑过的 Elysium；因 softCap 又裁掉挖矿与台子/Meme，本轮只跑打新。mentionsThin 保持 R1704 那组（周期第 2 轮：PlunderPort/TapeAIAgent、GIWA_by_Upbit/DogeOS、ShieldedNaka/Bramble_fi），mentionsRest 奇数轮 fulldotfun/PulseLaunchpad，四条 mentions 全部因 softCap 裁掉，不是漏栏。六条薄栏独立 KW 均已跑。主路径 xReads=18，等于 softCap 也等于 minSpend。静号轮到 打新（index 0，userQuery “fair mint”）。search_users 仍不可用，未伪造、未计入 xReads/静号已读。上轮 deferredHandles 已空，silentCap 第二次调用改为第三方 has:mentions 搜索（不占 softCap）。filter 见 35 个号：28 个 too_many_posts、3 个已在库、4 个 profile_unresolved（jirobots/cryptocom/Csilla_cro/Rotikaintel）留给下轮静号档解析。sentToReview=0，无静号收录。18 条主查询成功后 remaining=539，再加 1 次静号 mentions remaining=538（该次计入 remaining、不计入 xReads）。无翻页、无探索性重读。UF 892→947（kept 48，跳过 7 个已知 NF/suspended，considered 55）。apply_patch 未改今晚档期/未给未读的今晚号写 lastChecked；未降低 enter-elysium/aka-fun/tapeup/pairmine 粉丝；未重开任何 ≤2h 窗；未给 @Blonskr Behemoth 二期编造时刻或新卡；未动 foome/hood-junkies/oak-agent-kit/elyfish/dotbots（本轮未读）。

## alertMessage
R1705：无新收录；12 个送审号均为转推/喊单/非官号或无 CA 与精确时刻，保守 skip。今晚档期（不改）：clover-rh 20:00、zerva 21:00、$EPUNK 21:30、bloodstockrh/mythosbsc 22:00 CST；当前无 ≤2h 窗。面板 https://reboot7454.github.io/early-scout/
