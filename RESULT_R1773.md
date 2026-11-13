# RESULT R1773（例行独立 pace 扫描）

- time: 2026-11-13 23:19:00 CST（Asia/Shanghai）。开跑前 `git pull`，origin/main 与本地同在 R1772（5966ae7），扫描期间远程未抢占，本轮独立记为 R1773。notify=true。未自动 mint。
- mode: pace（R1739 已完成 08:00 CST 后首轮全量补扫，本轮不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: true。须推：已在库 oathbots（@Oathbots）本轮首次确认 $OATH 付费预售开窗 LIVE。官帖 22:51 CST 宣布 Presale is live now（https://x.com/Oathbots/status/2121254742491857339）；页面 https://oathbots.online/oath ；窗口 11-13 22:00 CST → 11-18 22:00 CST；任意钱包，每笔最少 0.005 BNB、每钱包最多 0.1 BNB；硬顶 1.8 BNB、软顶 0.3 BNB（已达）。链上预售合约 0xea0f02BF67ab10A540B29E979d9b49a17b62414d status=OPEN，已存入 0.725 BNB / 22 钱包，5000 万枚 OATH 已注入；代币合约 0x1e311022fEe30A395291eA21e5f339D3016a0Ed4（页面 JS，BSC hasCode true）。非免费。持有者空投合约 0xFEaa982E8cE7B386bcD4d4cEa86fddE54BDbbd4c 勿与预售合约混淆。禁止重推：bagnotary 仍 11-14 00:00 CST（R1770 已推 ≤2h，未改期）；lil-giraffies / boolish-rh 预约 23:00 CST 已过但本窗无官帖、官网无开铸证据、公开 RPC 失败，未能核验是否已开铸，不作为已开铸通知（R1768 已推 ≤2h）；hooded-ape-club 公铸进度 1276→1342/1500；polyrob 21→22；Ashling / clankbots / diglode 及 R1772 Discord 卡已通知；其它已推 LIVE 仅进度；halfdotfamily 仅 WL bidding 结束刷新。
- xReads: 25（main 24；silent 1；admitVerify 0）；remainingBefore 242 → remaining 217 / 1000；softCap 18，minSpend 18，silentCap 2；main 24 略超 softCap（UF×2 + 厚表分片×4 + 薄栏 Watch/MUST×2 + 薄栏 KW×6 + 核心 KW×5 + KW_GAPS×1 + mentionsThin×3 + mentionsRest×1，未砍栏），高于 minSpend。官网 / 链上 / HTTP / OpenSea 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重。from: 官号窗 start_time=2026-11-13T14:50:00Z；关键词 / mentions start_time=2026-11-13T14:55:00Z。
- admitVerifyReads: 0。未为候选另耗 X 读。oathbots 预售来自本轮 THIN/FAT 官帖（@Oathbots 在 agentPad 分片）+ 官网 + BSC RPC（totalDeposited / depositors / status / token balanceOf）。lil-giraffies / boolish-rh 未另开 X 复核。Voxel Kings / @0xTheHS 为第三方 RT，本轮未另开 X 核验官号，故不收录。
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet 均已跑 + 核心 KW 打新/挖矿/台子/GO/Elysium + KW_GAPS 全跑。BN Agent 靠 fat agentPad/bnAgent。不翻页 next_token。帖量 meta.result_count：LayerZero 1、Tape 6、GIWA 9、DogeEVM 12（JSON 截断）、BTC 9、Starknet 4、打新 25（截断）、挖矿 3、台子 18（截断）、GO 25（截断）、Elysium 25（截断）、GAPS 25（截断）。部分 write_to_file 回包在约 6.3–6.4KB 截断，已用正则抽取完整帖，未为完整 JSON 重拉。）
- laneReads: KW_LayerZero=1，KW_Tape=1，KW_GIWA=1，KW_DogeEVM=1，KW_BTC=1，KW_Starknet=1，核心打新/挖矿/台子/GO/Elysium 各 1，KW_GAPS=1
- userFollow: 刷完本片 1182→1230，kept 48，skip 0，2 from: batches，本片 7 帖（UF1=7，UF2=0）。下一轮从 1230 续（UF 全表 accounts=1660；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 LayerZero、Tape、GIWA（薄栏 mentionsThin）；rest 实际查询官号为 @Enter_Elysium / @kinetiq_xyz / @AgentKinetiq / @squeekchain / @NutshellMarkets / @starx_xlayer / @PulseLaunchpad / @flapdotsh / @irys_xyz / @fulldotfun / @arcxtrade / @dotaipad。均已跑，不翻页。帖量 MENT_LayerZero 24（截断）、MENT_Tape 8、MENT_GIWA 10（截断）、MENT_REST 25（截断）。
- fat shards: agentPad 98→126 kept 27 skip 1（cabaldotfun known_nf）；freeMint 186→214 kept 20 skip 8（known_nf）；bnAgent 15→43 kept 17 skip 11（known_nf）；elysium 112→140 kept 28 skip 0。下一轮 nextStarts：agentPad 126 / freeMint 214 / bnAgent 43 / elysium 140
- thin official watches: 去重后 unique 93，MUST_TODAY 已并入（含 ClankBots / diglodeHQ / trycrownmark / homma_agent / nofomopaper / agent_raise / perpsiumXYZ），2 个 from: 批次。本窗 THIN1=15 帖 / THIN2=1 帖。
- silentAccounts: ran=true，lane=台子/Meme（round 1773 % 11 = 2；search_users unavailable，改跑 mentions `has:mentions (launchpad OR "bonding curve") -is:retweet`，softCap 外 1 读，max_results=20）；回包 20 帖（JSON 截断，已抽取）。filter sentToReview=0、admitted=0。未做第二读。
- discordPeekDeferred: true（本例行默认不登录 DC；本轮远程未抢占）。
- DS: 本轮无新收录候选送审。曾用 deepseek-flash thinking-on 请写 alert / oathbots / halfdot 文案，回包仅为思考过程、无断开的可解析 JSON，未改用高成本模型、非 dsFallback；通知与卡片文案按官帖+官网+BSC RPC 事实手写。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: oathbots $OATH 预售已开，须推。lil-giraffies / boolish-rh 预约 23:00 CST 已过但未能核验开铸，不作为已开铸通知。bagnotary 仍 11-14 00:00 CST，R1770 已推，不重推。HonestBull 已售仍 23/10000。boxcars 驾照 138→145/1000。ponke-agent 仍 47/11055、免费 47/555。agx-402 unitsMinted 仍 10325，distributedAgx 仍 4.1300 亿，mintUnitPriceU 0.2739→0.2704，genesisClaims 仍 OPEN，voting 仍 NOT_OPEN。GateCerberus / myco / Freememe 已通知未改期（myco 链上 NFT 仍 0；Freememe 本窗官帖称 Launch didn’t go as planned，只刷新）。hooded-ape-club 公铸仍 LIVE，OS 1276→1342，不重推。polyrob OS 21→22，不重推。
- watch-bug: 本轮无新收录，无需新挂 Watch。历史漏挂约 1686 张；本轮未做整表回填。
- new cards: 无。newThisRound 已清空（独立 R1773，不沿用 R1772 Discord/pace 新卡标记）。新卡规则仍 focus=false（本轮无新卡）。candidateCount 4188 不变。candidate.round 元数据为 1773。

## 须推

- OathBots $OATH 预售（@Oathbots）已开：官帖 22:51 CST 宣布 Presale is live now。窗口 2026-11-13 22:00 CST → 2026-11-18 22:00 CST。任意钱包可参与，每笔最少 0.005 BNB、每钱包最多 0.1 BNB；硬顶 1.8 BNB、软顶 0.3 BNB（已达）。链上预售合约 0xea0f02BF67ab10A540B29E979d9b49a17b62414d（BSC）status=OPEN，已存入 0.725 BNB / 22 钱包，5000 万枚 OATH 已在合约内；代币合约 0x1e311022fEe30A395291eA21e5f339D3016a0Ed4。页面 https://oathbots.online/oath 。按存入占比分配；不足软顶可全额退款；上线 11-19 22:00 CST。非免费。本号不自动 mint。
- 顺带（已通知或不核验为开铸，不重推）：bagnotary 仍 11-14 00:00 CST；lil-giraffies / boolish-rh 到点未能核验开铸；hooded-ape-club 公铸仍 LIVE（OpenSea 1276→1342/1500）；polyrob 已铸 21→22；Ashling / clankbots / diglode 及既有 Discord 新卡不重推。

## 仍在跟（刷新，不重推）

- hooded-ape-club：公开铸造仍 LIVE。本窗官帖称 Only 158 left! 1,342 / 1,500。OpenSea 1276→1342，sales 1280→1358，owners 523→535，floor 约 0.14 USDG。付费公铸。公开 Robinhood RPC 仍失败。
- polyrob：白名单铸造仍 LIVE。本窗官帖 22 of 6,551 minted，Allowlist 仍余约 23h，0.033 ETH。OpenSea 已铸 21→22，owners 7，sales 0。仍需 WL，非免费公铸。
- lil-giraffies / boolish-rh：预约 23:00 CST 已过。本窗无官帖；giraffies 官网仍白名单文案，boolish.fun 无铸造 CTA；公开 RPC 失败，OpenSea 集合未找到。未能核验是否已开铸。
- bagnotary：仍定 2026-11-14 00:00 CST 于 Pons。本窗无改期官帖。官网仍 SSL EOF。
- honestbull：Issue #1 付费公平份额铸造仍 LIVE。链上已售仍 23/10000，saleEnd 2026-11-18 02:29:53 CST。R1767 已通知，不重推。非免费。
- boxcars：免费驾照仍开放，链上已领 138→145/1000。预售 11-17 21:00 CST。R1766 已通知，不重推。
- ponke-agent：免费公平铸造仍 LIVE。链上仍 47/11055，免费 47/555。R1769 已通知，不重推。
- myco：官网 200。BSC 链上 NFT 0x86229C12DB0F8F5816750Eb2A4ac6076FDb912d3 totalSupply 仍为 0。R1764 已通知，不单独重推。
- GateCerberus：本窗无新官帖更新已售数。上一轮官帖 Paid 0/1000 @0.01 HYPE，Free 0/500。R1762 已通知，不单独重推。
- Freememe（@FreeMemeApp）：应用已 LIVE。本窗官帖称 Launch didn’t go as planned，并在办竞赛。R1762 已通知，不作为新 mint 窗重推。
- agx-402：付费 fair launch 仍 OPEN。unitsMinted 仍 10325，distributedAgx 仍 4.1300 亿，mintUnitPriceU 0.2739→0.2704。genesisClaims 仍 OPEN，voting 仍 NOT_OPEN。仍需 .ai Agent ID + Binance Agentic Wallet。本号不自动 mint。
- dripevm：白名单免费仍开，Elysium RPC 与 OpenSea drip-nft 本轮均为 165/888。公开铸造仍为 11-16 06:00 CST。已通知过，不重推。
- the-syndicate-rh：OpenSea 已铸仍 925/1000；owners 366，sales 838，floor 约 0.15 USDG。公开 Robinhood RPC 仍失败。
- jpeg-monkes：OpenSea 已铸 1481→1484，owners 876→874，sales 1832→1824，floor 约 0.00081 ETH。公开 Robinhood RPC 仍失败。
- hood-terminals：OpenSea 仍 528/777，owners 349，sales 653，floor 约 0.00072 ETH。不是免费窗。公开 Robinhood RPC 仍失败。
- boatn-fish：api/stats 已铸 1720→1737/2222，wallets 135→138，priceUsd≈2.56。不是免费窗。
- arctic-bear：链上已铸仍为 82/5555。
- clause-protocol：链上已铸仍为 9/7777。
- momo-mochi：链上已铸仍为 299/2222。
- tsbdotfun：OpenSea the-shadow-born 仍 0。Discord 已通知，不重推。
- halfdotfamily：官帖 23:08 CST 宣布 WL bidding closed，90 bids、总出价 52.39 ETH。本轮未核到铸造合约。仅刷新，不重推。
- ashling：本轮未再补拉官帖。官网仍 SSL EOF。R1772 已通知 Pons 池与 CA，不重推。

## 例行侧 skips

- Voxel Kings / @0xTheHS：关键词窗出现第三方 RT「Mint tomorrow! Only 555 NFTs | FREE Mint」。本轮未见官号原文，未另开 X 核验 handle（硬禁误判无官推），不收录。
- AntHood / @KingAnt：第三方 RT 称 Space 即将开始、免费 mint 仍有名额。官号已在库（anthood），精确开售仍 TBA，不另建卡、不重推。
- Gangstaz（@gangstazfun）：第三方提到 Free mint starts November 13。已在库 watching，本片未拉到官号帖，不以第三方声称开铸。

## 面板与推送

- docsSynced=true（Pages 源为 main:/docs；根目录与 docs/data.json 一并推到 R1773）
- panel: https://reboot7454.github.io/early-scout/
- 未自动 mint。
