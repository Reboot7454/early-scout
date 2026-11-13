# RESULT R1762（Discord 18:10 占轮 + 例行 18:18 合并）

- time: 2026-11-13 18:18 CST（Asia/Shanghai）。Discord alpha 已于 18:10 CST 占用 R1762 并补收 dusktape（当时已 notify=true，不在本合并里重推）。本段是随后合并的例行 pace 扫描：LIVE 进度、X 游标、Watch 漏挂修复，以及对 GateCerberus / Freememe 首次进入 ≤2h 的第二次 notify。
- mode: pace（R1739 已完成 08:00 CST 后首轮全量补扫，本轮例行不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: true（例行侧无新收录、无新的免费 LIVE/登记卡。Discord 的 dusktape 已在 18:10 推过，不重推。但 GateCerberus 今日 20:00 CST 开售、Freememe 今日 20:00 CST 应用上线，均于 18:00 CST 起首次进入 ≤2h，且 Discord 通知未覆盖这两个窗口，故本合并 notify=true。agx-402 genesisClaims 仍 20:25:44 CST，尚未进入 ≤2h（≤2h 自 18:25）。Lil Giraffies 仍 23:00 CST、Bagnotary 仍 11-14 00:00 CST、Ashling 仍 22:00 CST、polyrob 开铸约 22:02 CST、boolish-rh 仍 23:00 CST，均尚未进入。The Syndicate ≤2h 已于 14:37 CST 结束，不作为新窗重推；已通知过的 DripEVM 等只刷新进度。）
- xReads: 26（main 24；silent 1；admitVerify 1）；remainingBefore 493 → remaining 467 / 1000；softCap 18，minSpend 18，silentCap 2；main 24 略超 softCap（UF×2 + 厚表分片×4 + 薄栏 Watch/MUST×2 + 薄栏 KW×6 + 核心 KW×5 + KW_GAPS×1 + mentionsThin×3 + mentionsRest×1，未砍栏），高于 minSpend。Discord 段未另耗 X 读。admitVerify 为对 @Badyfra_ink 的一次 get_users（本轮判定不建卡）。
- admitVerifyReads: 1（@Badyfra_ink）。金毛矿工卡再次来自第三方帖，未为猎号另耗 X 读。官网 / 链上 / HTTP / OpenSea 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重。
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet 均已跑 + 核心 KW 打新/挖矿/台子/GO/Elysium + KW_GAPS squeek/Nutshell/仓鼠链/STARX/X Layer/Agent ID/AIDROP/Pulse/computeroll/pipfun/TapeOut/Local Bottom 全跑。BN Agent 靠 fat agentPad/bnAgent。不翻页 next_token。）
- laneReads: KW_LayerZero=1，KW_Tape=1，KW_GIWA=1，KW_DogeEVM=1，KW_BTC=1，KW_Starknet=1，核心打新/挖矿/台子/GO/Elysium 各 1，KW_GAPS=1
- userFollow: 刷完本片 702→750，kept 48，skip 0，下一轮从 750 续（UF 全表现 1621，含本轮补挂的 @dusktape；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 LayerZero、Tape、GIWA（薄栏 mentionsThin）；rest 实际查询官号为 @Enter_Elysium / @kinetiq_xyz / @AgentKinetiq / @squeekchain / @NutshellMarkets / @starx_xlayer / @PulseLaunchpad / @flapdotsh / @irys_xyz / @fulldotfun / @arcxtrade / @dotaipad。mentionsThinDeferred=[]（DogeEVM/BTC/Starknet 已在 R1761 轮到，本轮不重复）。均已跑，不翻页。未见可建新卡的官号挂靠。
- fat shards: agentPad 590→618 kept 28 skip 0；freeMint 304→332 kept 28 skip 0；bnAgent 29→57 kept 28 skip 0；elysium 142→171 kept 28 skip 1（GLOAMMAIL dedup_used）。均未绕回。下一轮 nextStarts：agentPad 618 / freeMint 332 / bnAgent 57 / elysium 171
- thin official watches: 去重后 unique 92，kept 88，skip 4（已知 NF TapeFractal / FoundryTape / GAMA_GIWA，以及 DogeOSExchange 已在本轮 fat 读过去重），再加上 MUST 剩余 GateCerberus / bagnotary / giraffies_nft / AscendLaunch / Elysium_Pepes / Ashlingfun，2 个 from: 批次
- silentAccounts: ran=true，lane=台子/Meme（1762%11=2，下一栏 GO盘），search_users unavailable（不在本轮 X 工具目录，未空转），改跑 mentions（softCap 外）；回包约 result_count=20，多为已在库 @Grokiefun 评论或泛 launchpad 讨论。未做第二读。admitted=0
- discordPeekDeferred: true（本例行不登录 DC；Discord 段已由另一通道在 18:10 完成 alpha 补收）。保留 Discord lastSeen / lastSeenByChannel，不回拨。
- DS: deepseek-flash thinking-on 连续两次只吐出思考过程、未给出可解析 JSON，本轮走 dsFallback。判定 notify=true（GateCerberus / Freememe 窗口首次进入 ≤2h）；Badyfra 与金毛矿工卡 admit=false。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: 与薄栏 Watch 合并查询 from:GateCerberus OR bagnotary OR giraffies_nft OR AscendLaunch OR Elysium_Pepes OR Ashlingfun。GateCerberus 本窗无新官帖，发售仍为今日 20:00 CST，已于 18:00 CST 进入 ≤2h（第一次），本合并通知。lil-giraffies 开铸仍为 23:00 CST，尚未进入 ≤2h。Bagnotary 开盘仍为 2026-11-14 00:00 CST，未进 ≤2h；官网 bagnotary.pro 本轮 200。Elysium Pepes 仍为 Announced，不把预览写成已开盘。AscendLaunch 不是免费铸造。Ashling 官宣今日 22:00 CST 在 Pons 发 $ASHLING，尚未进入 ≤2h（≤2h 自 20:00）；本窗官帖谈 game-contract / pyre 经济，未改期；官网本轮 SSL EOF；已由 Discord 通知过，不重推。
- watch-bug: Discord 新卡 dusktape 在库但不在任何 Watch，已补进 userFollowWatch（与 R1754/R1756/R1761 同类 bug）。扫描其余 round≥1740 无新的漏挂。dusktape 不重推。

## 可操作 / 通知

notify=true（第二次，仅 GateCerberus 与 Freememe 首次进入 ≤2h；dusktape 不重推）。GateCerberus 今日 20:00 CST 在 Elysium 开售（500 免费 / 1,000 付费 0.01 HYPE）。Freememe 应用也定在今日 20:00 CST 上线（官网写 7AM EST，不是 mint）。agx-402 genesisClaims 仍预约 20:25:44 CST，尚未进入 ≤2h。本号不自动 mint。面板 https://reboot7454.github.io/early-scout/

## Discord 已推过、本合并不重推

- dusktape（@dusktape，打新，Robinhood Chain）：官网 https://dusktape.live ，$LULL 定档 2026-11-15 00:00 CST 在 Pons 发射；LullLedger 0x5eeAF93840D7fED94A9f2e5322Aeed3965Bd6F12 是账本合约不是代币 CA。已进 userFollowWatch。

## 仍在跟

- GateCerberus：份额发售仍为今日 20:00 CST（500 免费 / 1,000 付费 0.01 HYPE），已于 18:00 CST 进入 ≤2h。本窗无新官帖，未改期。公开 Elysium RPC 仍只能读到代币量级 totalSupply，不能当作 NFT 已铸数。本合并因此窗口首次进入而通知。
- Freememe（@freememeapp）：应用上线仍为今日 20:00 CST（官网 7AM EST 已核，站点 200），已于 18:00 CST 进入 ≤2h。这是产品/应用上线，不是 NFT mint。本合并因此窗口首次进入而通知。
- agx-402：付费 fair launch 仍 OPEN / POST_MIGRATION；官方池 17:25:44 CST 已开（R1761 已通知开池，不因进度再推）。manifest unitsMinted 9800→10173，distributedAgx 3.92亿→4.0692亿，mintUnitPriceU 0.6429→0.3717。genesisClaims 仍 SCHEDULED，预约 20:25:44 CST，尚未进入 ≤2h（≤2h 自 18:25）。仍需 .ai Agent ID + Binance Agentic Wallet。CA 仍为 0xF334039c3B0aBDe100887D17a476952D3E992Eb0。本号不自动 mint。
- dripevm：白名单免费仍开，Elysium RPC 已铸 157→158/888。本轮 OpenSea drip-nft 200，owners 54→55、sales 149→150、floor 仍 0.03 HYPE。公开铸造仍为 11-16 06:00 CST。官网仍 200。已通知过，不重推。
- the-syndicate-rh：≤2h 已于 14:37 CST 结束。OpenSea 已铸 909→910/1000，owners 362→363，sales 822→823，floor 仍约 0.15 USDG。官网仍 200。公开 Robinhood RPC 仍失败。不作为新窗通知。
- jpeg-monkes：OpenSea 已铸 1432→1442，owners 仍 878，sales 1715→1726，floor 约 0.00108 ETH。公开 Robinhood RPC 仍失败。
- hood-terminals：OpenSea total_supply 仍 527/777，owners 350，sales 647，floor 约 0.000999 ETH。不是免费窗。公开 Robinhood RPC 仍失败。
- boatn-fish：api/stats 已铸 1279→1302/2222，wallets 100→103，priceSol≈0.02709，priceUsd≈2.17。不是免费窗。
- arctic-bear：链上已铸 78→81/5555。官网仍 200。
- clause-protocol：链上已铸仍为 8/7777。官网仍 200。
- momo-mochi：链上已铸仍为 296/2222。官网仍 200。已通知过的免费窗不重推。
- zodiac-fortune：本轮 totalSupply() 回退，沿用 335/3333 remainingFree=0。官网仍 200。
- riftera-rifters：本轮 totalSupply() 回退，沿用 447。官网 riftera.net 仍 200。
- sharkverse：本轮 totalSupply() 回退，沿用 21/4444。官网仍 200。
- firsttake-xyz：本轮 BSC/1rpc totalSupply() 失败（限额或回退），沿用 194/7620。官网 rifera.xyz 仍 200。
- lil-giraffies：MUST_TODAY 本窗无改期官帖，开铸仍为今日 23:00 CST，尚未进入 ≤2h。官网仍 200。公开 Robinhood RPC 仍失败。
- Bagnotary：开盘仍为 2026-11-14 00:00 CST，未进 ≤2h。本窗无改期官帖。官网 bagnotary.pro 本轮 200。
- Ashling：发射仍为今日 22:00 CST，尚未进入 ≤2h。本窗官帖未改期。官网本轮 SSL EOF。Discord 已通知，不重推。
- polyrob：白名单约 20:00 CST 锁定、开铸约 22:00/22:02 CST，距开铸仍 >2h。
- boolish-rh：Possession night 仍为 11-13 23:00 CST，未进 ≤2h。
- Elysium Pepes：MUST_TODAY 本窗无新官帖，仍为 Announced，不把预告写成已开盘。
- AscendLaunch：MUST_TODAY 本窗无新官帖。不是免费铸造。

## 跳过 / 不建卡（例行 X 扫描）

- @Badyfra_ink / Badyfra Garden：get_users 核验官号属实，官网 https://badyfra.xyz/ 本轮 200；bio 称 1111 free mint on @inkonchain，站点是「种花浇三次赢白名单位」。账号 2026-08-18 创建、137 粉、21 帖；未见官方 CA，未见明确开铸时刻。dsFallback 判定不算本轮可操作极早期，admit=false，未建卡。若后续出现开铸时刻可再核。
- 金毛矿工卡 Golden Miner Cards：本轮再次见到第三方帖指向 https://goldenminer.surge.sh/。硬规则新收录必须有推特，admit=false，也未为猎号另耗 X 读。
- UnseenOrdo / willstudiolab：已是库内 unseen-ordo 的 WL 活动（约 300 免费名额），不新建卡。
- AmmoraHQ：已在 giwaWatch。
- PlayPixelora WL：已在 play-pixelora 卡上。
- HATCHIEggy / Grokiefun / RebateLaunch / Hypesium / TeseraLab / VoidCash：已在库。
- $PHEW / @0xZairo：付费预售喊单，证据不足，不建卡。
- Starknet「Bramble」等多为词误伤；DogeEVM 多为打赏噪音；GO 栏 Elon/rocket 误伤；KW_GAPS 见 Nutshell/JEOLEE/Agent ID 等噪音，无新官号可建卡。
