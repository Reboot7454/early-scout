# RESULT R1760

- time: 2026-11-13 17:12 CST（Asia/Shanghai）
- mode: pace（R1739 已完成 08:00 CST 后首轮全量补扫，本轮为正常节流，不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: false（本轮无新收录，无新的免费 LIVE/登记卡；GateCerberus / Lil Giraffies / Bagnotary 均尚未进入 ≤2h；The Syndicate ≤2h 已于 14:37 CST 结束，不作为新窗重推；已通知过的 DripEVM / agx-402 窗未变，只刷新进度；vibecool2026 仅补 Watch，不重推）
- xReads: 25（main 24；silent 1；admitVerify 0）；remainingBefore 543 → remaining 518 / 1000；softCap 18，minSpend 18，silentCap 2；main 24 略超 softCap（UF×2 + 厚表分片×4 + 薄栏 Watch/MUST×2 + 薄栏 KW×6 + 核心 KW×5 + KW_GAPS×1 + mentionsThin×3 + mentionsRest×1，未砍栏），高于 minSpend
- admitVerifyReads: 0（无新收录，未另做 get_users 核验。金毛矿工卡再次来自第三方帖 @Annak0ox，官网与链上仍可见免费 LIVE，但页面无官推，未为猎号另耗 X 读。官网 / 链上 / HTTP / OpenSea 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重。）
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet 均已跑 + 核心 KW 打新/挖矿/台子/GO/Elysium + KW_GAPS squeek/Nutshell/仓鼠链/STARX/X Layer/Agent ID/AIDROP/Pulse/computeroll/pipfun/TapeOut/Local Bottom 全跑；API 从词面去掉 `$` 字符，$PULSE 按 PULSE 跑。BN Agent 靠 fat agentPad/bnAgent。不翻页 next_token。）
- laneReads: KW_LayerZero=1，KW_Tape=1，KW_GIWA=1，KW_DogeEVM=1，KW_BTC=1，KW_Starknet=1，核心打新/挖矿/台子/GO/Elysium 各 1，KW_GAPS=1
- userFollow: 刷完本片 580→644，kept 48，skip 16（已知 NF：Trysmolpadfun / FISTAgent / Villagers_RH / Ainubsc / agentcityuk / UseHyperLiquid / MonsterRH_ / Derpagent_ / Proxisfun / ramencoinmeme / letswinhood / agentharvest_ai / seatworkcells / frogsagent / Honestcoin60 / DropMinters），下一轮从 644 续（UF 全表 1615，本轮补入 @vibecool2026 后略增；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 LayerZero、Tape/电路、GIWA（薄栏 mentionsThin；LayerZero 约 24 帖、Tape 约 25 帖、GIWA 约 25 帖，均为已在库项目或测试网/候补名单转帖，无新官号可建卡）；rest 实际查询官号为 @Enter_Elysium / @kinetiq_xyz / @AgentKinetiq / @squeekchain / @NutshellMarkets / @starx_xlayer / @PulseLaunchpad / @flapdotsh / @irys_xyz / @fulldotfun / @arcxtrade / @dotaipad。mentionsThinDeferred=[]。均已跑，不翻页
- fat shards: agentPad 523→561 kept 28 skip 10 NF（KDAgentAI / Gweiwbbb / PlayTycoonCity / baoracletrade / agentplacewall / LastCall4vx / SENSEIAgent_ / Agentspunks / BN_Big_Bang / cryptosympbnb）；freeMint 245→276 kept 28 skip 3 NF（LumenGenesisNFT / pixelboyzai / spiderproject69）；bnAgent 266→291 kept 24 skip 1 去重（TheUnwrittenBNB 已在本轮 freeMint 读过），触表尾（291/291），下一轮 nextStarts=0；elysium 81→114 kept 28 skip 5 NF（CyclopesElysium / elyword_xyz / vytraqfun / HordeOnElysium / Estock_）。除 bnAgent 触尾外均未绕回。下一轮 nextStarts：agentPad 561 / freeMint 276 / bnAgent 0 / elysium 114
- thin official watches: 去重后 93 unique（跳过已在本轮 UF 读过的 anoncoinit、已知 NF TapeFractal / FoundryTape，以及 tapeOut 与 tape 重复号），再加上 MUST 剩余 GateCerberus / bagnotary / AscendLaunch / Elysium_Pepes（giraffies_nft 已在 freeMint 分片去重），2 个 from: 批次（49+44）
- silentAccounts: ran=true，lane=打新（按 R1760 轮换，Starknet 下一栏 index 0），search_users unavailable（不在本轮 X 工具目录，未空转），改跑 mentions（窗从 2026-11-12T09:09:44Z 起，softCap 外，query: has:mentions has:links ("fair mint" OR "free mint" OR whitelist) -is:retweet）；回包 result_count=20，均为已在库或第三方登记/白名单转帖。未做第二读。seenApprox=20，sentToReview=0，admitted=0，skipped=0
- discordPeekDeferred: true（DC 不登录；R1759 已于 16:46 CST peek，本轮不另开浏览器/Discord，不占用 Discord 轮号）
- DS: deepseek-flash thinking-on，成功；判定 notify=false，且金毛矿工卡 admit=false（无官推）。未走 dsFallback。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: 与薄栏 Watch 合并查询 from:GateCerberus OR bagnotary OR AscendLaunch OR Elysium_Pepes（giraffies_nft 已在本轮 freeMint 厚表分片，去重不重读）。GateCerberus 本窗仅见 11-12 20:00 CST 旧帖（HOUND 持有者空投说明），发售仍为今日 20:00 CST，尚未进入 ≤2h。lil-giraffies 开铸仍为 23:00 CST，尚未进入 ≤2h。Bagnotary 本窗有产品说明官帖，开盘仍为 2026-11-14 00:00 CST，未进 ≤2h。Elysium Pepes 仍为 Announced，不把预览写成已开盘。AscendLaunch 不是免费铸造。
- watch-bug: 扫描 round≥1740 共 39 张卡，仅 vibecool2026（R1759 已通知）在库却不在任何 Watch；已把 @vibecool2026 写入 userFollowWatch.accounts、把 vibecool2026 写入 candidateIds，不重推。

## 可操作 / 通知

本轮无需要推送给用户的新收录或新进/仍有效 ≤2h 窗口。notify=false。

## 仍在跟（非 ≤2h）

- agx-402：付费 fair launch 仍 OPEN / PRE_MIGRATION，manifest 约 17:08 CST 已铸 630→4579/9800 单位，单价 1.0→1.1 U，distributedAgx 2,520 万→1.8316 亿。需 .ai Agent ID + Binance Agentic Wallet。不是免费铸造。CA 仍为 0xF334039c3B0aBDe100887D17a476952D3E992Eb0。本号不自动 mint。已在 R1757 通知过，不重推。
- dripevm：白名单免费仍开，OpenSea drip-nft / Elysium RPC 已铸仍为 157/888，owners 仍 54，sales 149，floor 仍 0.03 HYPE。公开铸造仍为 11-16 06:00 CST。官网 dripevm.com 仍 200。已通知过，不重推。
- the-syndicate-rh：≤2h 已于 14:37 CST 结束。OpenSea thesyndicate- 已铸 891→904/1000，owners 仍 361，sales 仍 817，floor 仍约 0.15 USDG。官网仍 200。公开 Robinhood RPC 仍失败。不作为新窗通知。
- jpeg-monkes：OpenSea 已铸 1424→1428，owners 877，sales 1712，floor 约 0.00090 ETH。公开 Robinhood RPC 仍失败。
- hood-terminals：OpenSea total_supply 仍 527/777，owners 350，sales 647，floor 约 0.00098 ETH。不是免费窗。公开 Robinhood RPC 仍失败。
- boatn-fish：api/stats 已铸 1269→1279/2222，wallets 96→100，priceSol≈0.02701，priceUsd≈2.15。不是免费窗。
- arctic-bear：链上已铸 76→78/5555。官网仍 200。
- clause-protocol：链上已铸仍为 8/7777。官网仍 200。
- momo-mochi：链上已铸仍为 295/2222。官网仍 200。
- zodiac-fortune：本轮 totalSupply() 回退，沿用 335/3333 remainingFree=0。官网仍 200。
- riftera-rifters：本轮 totalSupply() 回退，沿用 447/1111。官网 riftera.net 仍 200。
- sharkverse：本轮 totalSupply() 回退，沿用 21/4444。官网仍 200。
- firsttake-xyz：本轮 BSC RPC totalSupply() 超时，沿用 194/7620。官网 rifera.xyz 仍 200。
- lil-giraffies：MUST_TODAY 本窗无改期官帖，开铸仍为今日 23:00 CST，尚未进入 ≤2h。官网仍 200。公开 Robinhood RPC 仍失败。
- GateCerberus：份额发售仍为今日 20:00 CST（500 免费 / 1,000 付费 0.01 HYPE），≤2h 自 18:00 CST 起，尚未进入。本窗仅见 11-12 20:00 CST 旧帖（HOUND 持有者空投说明），未改期。公开 Elysium RPC 仍只能读到代币量级 totalSupply，不能当作 NFT 已铸数。
- Bagnotary：开盘仍为 2026-11-14 00:00 CST，未进 ≤2h。本窗有产品说明官帖，未改期。本轮访问 bagnotary.pro 再次 SSL 失败，未改写其它字段。
- Elysium Pepes：MUST_TODAY 本窗无新官帖，仍为 Announced，不把预告写成已开盘。
- AscendLaunch：MUST_TODAY 本窗无新官帖。不是免费铸造。

## 跳过 / 不建卡

- 金毛矿工卡 Golden Miner Cards：本轮 KW_挖矿 再次见到第三方帖（@Annak0ox）称 Golden Miner Cards are live，指向 https://goldenminer.surge.sh/。站点与 BSC CA 0x088708f79A71b82C14e1864FB0c63E53Cbf94243 仍可见免费 LIVE。页面与 config.js 仍无官推。库内无此卡。硬规则新收录必须有推特，DeepSeek 判定 admit=false，本轮不建卡，也未为猎号另耗 X 读。
- PlunderPort waitlist、ZeroGuysNFT 11-30 免费铸造、PlayPixelora / Companions / HyperHaul / Jpegsaredead 等第三方登记或白名单转帖：均已在库，不作为新收录。
- RuninAI / ORYN / OSK / giwapad_xyz / TapeMine 等本轮官号或生态帖：均已在库，只作软刷，不新建卡。
- 其它新作者噪音（LayerZero / GIWA 测试网与 Ammora 候补、TapeOut 社区热点、Starknet 词误伤 Bramble 猫/赛马等、泵盘 bonding curve 信号）：已在库、空投号或无关内容，跳过。
