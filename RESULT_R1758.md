# RESULT R1758

- time: 2026-11-13 16:40 CST（Asia/Shanghai）
- mode: pace（R1739 已完成 08:00 CST 后首轮全量补扫，本轮为正常节流，不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: false（本轮无新收录，无新的免费 LIVE/登记卡；GateCerberus / Lil Giraffies / Bagnotary 均尚未进入 ≤2h；The Syndicate ≤2h 已于 14:37 CST 结束，不作为新窗重推；已通知过的 DripEVM / agx-402 窗未变，只刷新进度）
- xReads: 25（main 24；silent 1；admitVerify 0）；remainingBefore 568 → remaining 543 / 1000；softCap 18，minSpend 18，silentCap 2；main 24 略超 softCap（UF×2 + 厚表分片×4 + 薄栏 Watch/MUST×2 + 薄栏 KW×6 + 核心 KW×5 + KW_GAPS×1 + mentionsThin×3 + mentionsRest×1，未砍栏），高于 minSpend
- admitVerifyReads: 0（无新收录，未另做 get_users 核验。金毛矿工卡来自第三方帖 @Annak0ox，官网 goldenminer.surge.sh 与链上均可见免费 LIVE，但页面无官推，未为猎号另耗 X 读。官网 / 链上 / HTTP / OpenSea 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重。部分 KW/mentions 回包被截断，已用清洗后的 raw 回收文本，未为修复解析另耗 X 读）
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet + 核心 KW 打新/挖矿/台子/GO/Elysium + KW_GAPS squeek/Nutshell/仓鼠链/STARX/X Layer/Agent ID/AIDROP/Pulse/computeroll/pipfun/TapeOut/Local Bottom 全跑；API 从词面去掉 `$` 字符，$PULSE 按 PULSE 跑。BN Agent 靠 fat agentPad/bnAgent。不翻页 next_token。MN_DOGE / MN_BTC / MN_STARK 回包为 0 帖；KW_Tape / KW_GIWA / 部分核心 KW / SILENT_BTC 回包被截断，已 salvage，未重拉）
- userFollow: 刷完本片 523→580，kept 50，skip 7（agentpunkai / stockcatsfun / Volitionxyz / tollsfun / whackyrh / bibiainft / AgentBoss_AI，已知 NF），下一轮从 580 续（UF 全表 1615；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 DogeEVM、BTC、Starknet（薄栏 mentionsThin，三条均为 0 帖）；rest 实际查询官号为 @Enter_Elysium / @kinetiq_xyz / @AgentKinetiq / @squeekchain / @NutshellMarkets / @starx_xlayer / @PulseLaunchpad / @flapdotsh / @irys_xyz / @fulldotfun / @arcxtrade / @dotaipad。mentionsThinDeferred=[]。均已跑，不翻页
- fat shards: agentPad 492→523 kept 28 skip 3 NF（AiPullpad / oblaunchpadbase / Morumai_）；freeMint 213→245 kept 28 skip 4 NF（SENSEIAgent_ / Agentspunks / BN_Big_Bang / cryptosympbnb）；bnAgent 234→266 kept 28 skip 4 NF（spiderproject69 / bianjiayou / topaaafun / agenticsocial）；elysium 50→81 kept 28 skip 3 NF（obolworld / Elysium_Rocks / ramencoinmeme）。均未绕回。下一轮 nextStarts：agentPad 523 / freeMint 245 / bnAgent 266 / elysium 81
- thin official watches: 92 unique，与本轮已用 handle 去重 2 个（PlunderPort、ShieldedWizBTC）后 90，再加上 MUST 剩余 GateCerberus / giraffies_nft / bagnotary / AscendLaunch（Elysium_Pepes 已在 elysium 分片去重），2 个 from: 批次（47+47）。已知 NF 未在本批单独出现。THIN1 本窗 7 帖（均已在库，RUNECLAW_AI / packswap_xyz / owlgatecli），THIN2 本窗 2 帖（均已在库，Jumak_app 日常任务，非新开铸）
- silentAccounts: ran=true，lane=BTC，search_users unavailable（不在本轮 X 工具目录，未空转），改跑 mentions（窗从 2026-11-12T08:30:16Z 起，softCap 外，query: has:mentions (Ordinals OR CRC20 OR ShieldedNaka) (mint OR launch) -is:retweet）；回包 result_count=14，正文截断后清洗回收；未见可建卡的新官号。未做第二读。seenApprox=14，sentToReview=0，admitted=0，skipped=0
- discordPeekDeferred: true（DC 不登录）
- DS: deepseek-flash thinking-on，成功；判定 notify=false，且金毛矿工卡 admit=false（无官推）。未走 dsFallback。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: 与薄栏 Watch 合并查询 from:GateCerberus OR giraffies_nft OR bagnotary OR AscendLaunch（Elysium_Pepes 已在本轮 elysium 厚表分片，去重不重读）。本窗这四号均无新官帖。GateCerberus 发售仍为 20:00 CST，尚未进入 ≤2h。lil-giraffies 开铸仍为 23:00 CST，尚未进入 ≤2h。Bagnotary 仍为 2026-11-14 00:00 CST，未进 ≤2h。Elysium Pepes 仍为 Announced，不把预告写成已开盘。AscendLaunch 不是免费铸造。
- watch-bug: 本轮扫描 round≥1740 及近轮 Discord 补收（含 hookdroid / agx-402 / gangstazfun / bagnotary 等），无新的在库却不在任何 Watch 的漏挂。

## 可操作 / 通知

本轮无需要推送给用户的新收录或新进/仍有效 ≤2h 窗口。notify=false。

## 仍在跟（非 ≤2h）

- agx-402：付费 fair launch 仍 OPEN / PRE_MIGRATION，manifest 约 16:32 CST 已铸 19→630/9800 单位，单价仍 1.0 U，distributedAgx 76 万→2,520 万。需 .ai Agent ID + Binance Agentic Wallet。不是免费铸造。CA 仍为 0xF334039c3B0aBDe100887D17a476952D3E992Eb0。本号不自动 mint。已在 R1757 通知过，不重推。
- dripevm：白名单免费仍开，OpenSea drip-nft / Elysium RPC 已铸 156→157/888，owners 47→54，sales 149，floor 仍 0.03 HYPE。公开铸造仍为 11-16 06:00 CST。官网 dripevm.com 仍 200。已通知过，不重推。
- the-syndicate-rh：≤2h 已于 14:37 CST 结束。OpenSea thesyndicate- 已铸 859→891/1000，owners 仍 361，sales 798→817，floor 仍约 0.15 USDG。官网仍 200。公开 Robinhood RPC 仍失败。不作为新窗通知。
- jpeg-monkes：OpenSea 已铸 1419→1424，owners 仍 880，sales 1684→1693，floor 约 0.00094 ETH。免费窗已过。公开 Robinhood RPC 仍失败。
- hood-terminals：OpenSea total_supply 仍 527/777，owners 350，sales 647，floor 约 0.00098 ETH。不是免费窗。公开 Robinhood RPC 仍失败。
- boatn-fish：api/stats 已铸 1245→1269/2222，wallets 94→96，priceSol≈0.02686，priceUsd≈2.14。不是免费窗。
- arctic-bear：链上已铸 75→76/5555。官网仍 200。
- clause-protocol：链上已铸仍为 8/7777。官网仍 200。
- momo-mochi：链上已铸仍为 295/2222。官网仍 200。
- zodiac-fortune：本轮 totalSupply() 回退，沿用 335/3333 remainingFree=0。官网仍 200。
- riftera-rifters：本轮 totalSupply() 回退，沿用 447/1111。官网 riftera.net 仍 200。
- sharkverse：本轮 totalSupply() 回退，沿用 21/4444。官网仍 200。
- firsttake-xyz：本轮 totalSupply() 回退，沿用 194/7620。官网 rifera.xyz 仍 200。
- lil-giraffies：本窗 MUST_TODAY 无新官帖，开铸仍为今日 23:00 CST，尚未进入 ≤2h。官网仍 200。公开 Robinhood RPC 仍失败。
- GateCerberus：份额发售仍为今日 20:00 CST（500 免费 / 1,000 付费 0.01 HYPE），≤2h 自 18:00 CST 起，尚未进入。本窗无新官帖。公开 Elysium RPC 仍只能读到代币量级 totalSupply，不能当作 NFT 已铸数。
- Bagnotary：开盘仍为 2026-11-14 00:00 CST，未进 ≤2h。本窗无新官帖。本轮访问 bagnotary.pro 再次 SSL 失败，未改写其它字段。
- Elysium Pepes：MUST_TODAY 本窗无新官帖，仍为 Announced，不把预告写成已开盘。
- AscendLaunch：MUST_TODAY 本窗无新官帖。不是免费铸造。

## 跳过 / 不建卡

- 金毛矿工卡 Golden Miner Cards：本轮 KW_挖矿 见到第三方帖（@Annak0ox，49 粉，简介为 BTC 爱好者）称 Golden Miner Cards are live。t.co 指向 https://goldenminer.surge.sh/（200）。站点与 config.js 确认 BSC CA 0x088708f79A71b82C14e1864FB0c63E53Cbf94243，name=金毛矿工卡，symbol=GMC；链上 saleActive=true，totalMinted=6，freeMinted=6，paidMinted=0，freeRemaining=1994，免费池 2,000，每 Agent ID 前 5 张免费，mintStart=2026-11-13 16:04:08 CST，mintEnd=2026-11-20 16:04:08 CST。页面与 config.js 均无官推 / x.com / twitter 链接。库内无此卡。硬规则新收录必须有推特，DeepSeek 判定 admit=false，本轮不建卡，也未为猎号另耗 X 读。
- DumpMonkeyCrew / StormFrens 今日免费名单（@Tinylegends_io、@Jpegsaredead 等）：均已在库或只是第三方转帖，未为补全作者另耗 X 读，不作为新收录。第三方所称今日开铸时刻未做官号复核，不据此提前进入 ≤2h。
- PlunderPort waitlist、FLAP Agent ID 支持 BAB、Zero/lzATLAS 11-30、CrossEyed 白名单、ShieldedNaka / UnseenOrdo / Filepack 等：已在库或不是今日新 LIVE 官号，跳过。
- 其它新作者噪音（@ArifMaroya 推 ZeroGuysNFT、@META_STARx 推 DogeOS Chapter 5、@BrambleRamble4 / @horsevault / @MyF_Studio 等 Starknet 词误伤、@superstakefun 等）：已在库、空投号或无关内容，跳过。

