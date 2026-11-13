# RESULT R1761（Discord 17:29 占轮 + 例行 17:38 合并）

- time: 2026-11-13 17:38 CST（Asia/Shanghai）。Discord alpha 已于 17:29 CST 占用 R1761 并补收 ashling / heir-finance / noct-trading / outliers（当时已 notify=true，不在本合并里重推这四张）。本段是随后合并的例行 pace 扫描：LIVE 进度、X 游标、Watch 漏挂修复，以及对 agx-402 官方池开盘的第二次 notify。
- mode: pace（R1739 已完成 08:00 CST 后首轮全量补扫，本轮例行不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: true（例行侧无新收录、无新的免费 LIVE/登记卡；GateCerberus 仍 20:00 CST、Lil Giraffies 仍 23:00 CST、Bagnotary 仍 11-14 00:00 CST、Ashling 发射仍 22:00 CST，均尚未进入 ≤2h。但 agx-402 官方池刚于 17:25:44 CST 开盘，phase PRE_MIGRATION→POST_MIGRATION，migration units 9800/9800 售罄，属已通知窗口内的实质性新事件，DeepSeek 判定重推。The Syndicate ≤2h 已于 14:37 CST 结束，不作为新窗重推；已通知过的 DripEVM 等只刷新进度。Discord 四张新卡已在 17:29 推过，不重推。）
- xReads: 25（main 24；silent 1；admitVerify 0）；remainingBefore 518 → remaining 493 / 1000；softCap 18，minSpend 18，silentCap 2；main 24 略超 softCap（UF×2 + 厚表分片×4 + 薄栏 Watch/MUST×2 + 薄栏 KW×6 + 核心 KW×5 + KW_GAPS×1 + mentionsThin×3 + mentionsRest×1，未砍栏），高于 minSpend。Discord 段未另耗 X 读。
- admitVerifyReads: 0（例行无新收录，未另做 get_users 核验。金毛矿工卡再次来自第三方帖 @Annak0ox，未为猎号另耗 X 读。官网 / 链上 / HTTP / OpenSea 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重。）
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet 均已跑 + 核心 KW 打新/挖矿/台子/GO/Elysium + KW_GAPS squeek/Nutshell/仓鼠链/STARX/X Layer/Agent ID/AIDROP/Pulse/computeroll/pipfun/TapeOut/Local Bottom 全跑。BN Agent 靠 fat agentPad/bnAgent。不翻页 next_token。）
- laneReads: KW_LayerZero=1，KW_Tape=1，KW_GIWA=1，KW_DogeEVM=1，KW_BTC=1，KW_Starknet=1，核心打新/挖矿/台子/GO/Elysium 各 1，KW_GAPS=1
- userFollow: 刷完本片 644→702，kept 48，skip 10（已知 NF：onbeatfun / lettucegrow_rh / beatdotfamily / nonamespnft / heyribbid / inkwellonbnb / certuna_rh / miuadotfun / origopad / lootbale），下一轮从 702 续（UF 全表现 1620，含本轮补挂的 4 个 Discord 新号；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 DogeEVM、BTC、Starknet（薄栏 mentionsThin；DogeEVM 0 帖、BTC 0 帖、Starknet 3 帖，均为已在库项目评论或词误伤，无新官号可建卡）；rest 实际查询官号为 @Enter_Elysium / @kinetiq_xyz / @AgentKinetiq / @squeekchain / @NutshellMarkets / @starx_xlayer / @PulseLaunchpad / @flapdotsh / @irys_xyz / @fulldotfun / @arcxtrade / @dotaipad（约 25 帖，均为已在库项目或生态评论）。mentionsThinDeferred=[]。均已跑，不翻页
- fat shards: agentPad 561→590 kept 28 skip 1 已知 NF（Panba_EmojiPack）；freeMint 276→304 kept 28 skip 0；bnAgent 0→29 kept 28 skip 1 已知 NF（HashOre_BNB），未绕回；elysium 114→142 kept 28 skip 0。均未绕回。下一轮 nextStarts：agentPad 590 / freeMint 304 / bnAgent 29 / elysium 142
- thin official watches: 去重后 95 unique，kept 92（跳过已知 NF TapeFractal / FoundryTape，以及 GAMA_GIWA 已在本轮 UF 读过去重），再加上 MUST 剩余 GateCerberus / bagnotary / giraffies_nft / AscendLaunch / Elysium_Pepes，2 个 from: 批次（49+48）
- silentAccounts: ran=true，lane=挖矿（按 R1761 轮换 1761%11=1，下一栏台子/Meme），search_users unavailable（不在本轮 X 工具目录，未空转），改跑 mentions（窗从 2026-11-12T09:12:00Z 起，softCap 外，query: has:mentions ("GPU mine" OR "NFT miner" OR "PoW mine") -is:retweet）；回包 result_count=0。未做第二读。seenApprox=0，sentToReview=0，admitted=0，skipped=0
- discordPeekDeferred: true（本例行不登录 DC；Discord 段已由另一通道在 17:29 完成 alpha 补收）。保留 Discord lastSeen / lastSeenByChannel，不回拨。
- DS: deepseek-flash thinking-on，成功；判定 notify=true（agx-402 官方池开盘），且金毛矿工卡 / $ORNG / 第三方名单 TSB/Owlex/BLlPZ admit=false。未走 dsFallback。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: 与薄栏 Watch 合并查询 from:GateCerberus OR bagnotary OR giraffies_nft OR AscendLaunch OR Elysium_Pepes。GateCerberus 本窗无新官帖，发售仍为今日 20:00 CST，尚未进入 ≤2h。lil-giraffies 开铸仍为 23:00 CST，尚未进入 ≤2h。Bagnotary 本窗有产品说明官帖，开盘仍为 2026-11-14 00:00 CST，未进 ≤2h；官网 bagnotary.pro 本轮恢复 200。Elysium Pepes 仍为 Announced，不把预览写成已开盘。AscendLaunch 不是免费铸造。Ashling 官宣今日 22:00 CST 在 Pons 发 $ASHLING，尚未进入 ≤2h（≤2h 自 20:00），已由 Discord 通知过，不重推。
- watch-bug: Discord 四张新卡 ashling / heir-finance / noct-trading / outliers 在库但不在任何 Watch，已补进 userFollowWatch（与 R1754/R1756 同类 bug）。扫描其余 round≥1740 无新的漏挂。四张均不重推。

## 可操作 / 通知

notify=true（第二次，仅 agx-402 开池；四张 Discord 新卡不重推）。agx-402 官方池已于 17:25:44 CST 开盘（POST_MIGRATION，migration units 9800/9800 售罄）；genesisClaims 预约今日 20:25:44 CST（≤2h 自 18:25，尚未进入）。仍需 .ai Agent ID + Binance Agentic Wallet，不是免费铸造，本号不自动 mint。面板 https://reboot7454.github.io/early-scout/

## Discord 已推过、本合并不重推

- ashling（@Ashlingfun，打新，Robinhood Chain，score 由 Discord 段写入）：官网 https://ashling.fun ，官宣今日 22:00 CST 在 Pons 发 $ASHLING；喂 0.0005 ETH 点亮火焰 72 小时。尚未进入 ≤2h。已进 userFollowWatch。
- heir-finance（@heir_finance，打新，Ethereum）：官网 https://heir.finance/en/ ，非托管继承 Dapp，无代币与发射公告。已进 userFollowWatch。
- noct-trading（@NoctTrading，台子/Meme）：官网 https://noct.trading ，多市场交易终端；bio 称 $NOCT on Elysium，生态页本轮无条目、未见官方 CA。已进 userFollowWatch。
- outliers（@OutlierNFT，打新，Robinhood Chain）：供应 2222、定价 $2、OpenSea、11 月 20 日铸造日，白名单已开；无官网、无已验证合约。已进 userFollowWatch。

## 仍在跟（非 ≤2h）

- agx-402：付费 fair launch 仍 OPEN，phase PRE_MIGRATION→POST_MIGRATION；manifest unitsMinted 4579→9800/9800，distributedAgx 1.8316亿→3.92亿，mintUnitPriceU 现读 0.6429。官方池 17:25:44 CST 已开。genesisClaims 预约 20:25:44 CST。CA 仍为 0xF334039c3B0aBDe100887D17a476952D3E992Eb0。本号不自动 mint。本合并因此开池事件通知。
- dripevm：白名单免费仍开，Elysium RPC 已铸仍为 157/888。本轮 OpenSea drip-nft 401，owners/sales/floor 沿用 54 / 149 / 0.03 HYPE。公开铸造仍为 11-16 06:00 CST。官网仍 200。已通知过，不重推。
- the-syndicate-rh：≤2h 已于 14:37 CST 结束。OpenSea 已铸 904→909/1000，owners 361→362，sales 817→822，floor 仍约 0.15 USDG。官网仍 200。公开 Robinhood RPC 仍失败。不作为新窗通知。
- jpeg-monkes：OpenSea 已铸 1428→1432，owners 877→878，sales 1712→1715，floor 约 0.00108 ETH。公开 Robinhood RPC 仍失败。
- hood-terminals：OpenSea total_supply 仍 527/777，owners 350，sales 647，floor 约 0.00098 ETH。不是免费窗。公开 Robinhood RPC 仍失败。
- boatn-fish：api/stats 已铸仍为 1279/2222，wallets 仍 100，priceSol≈0.02702，priceUsd≈2.15。不是免费窗。
- arctic-bear：链上已铸仍为 78/5555。官网仍 200。
- clause-protocol：链上已铸仍为 8/7777。官网仍 200。
- momo-mochi：链上已铸 295→296/2222。官网仍 200。已通知过的免费窗不重推。
- zodiac-fortune：本轮 totalSupply() 回退，沿用 335/3333 remainingFree=0。官网仍 200。
- riftera-rifters：本轮 totalSupply() 回退，沿用 447/1111。官网 riftera.net 仍 200。
- sharkverse：本轮 totalSupply() 回退，沿用 21/4444。官网仍 200。
- firsttake-xyz：本轮 BSC RPC totalSupply() 回退，沿用 194/7620。官网 rifera.xyz 仍 200。
- lil-giraffies：MUST_TODAY 本窗无改期官帖，开铸仍为今日 23:00 CST，尚未进入 ≤2h。官网仍 200。公开 Robinhood RPC 仍失败。
- GateCerberus：份额发售仍为今日 20:00 CST（500 免费 / 1,000 付费 0.01 HYPE），≤2h 自 18:00 CST 起，尚未进入。本窗无新官帖，未改期。公开 Elysium RPC 仍只能读到代币量级 totalSupply，不能当作 NFT 已铸数。
- Bagnotary：开盘仍为 2026-11-14 00:00 CST，未进 ≤2h。本窗有产品说明官帖，未改期。官网 bagnotary.pro 本轮恢复 200。
- Elysium Pepes：MUST_TODAY 本窗无新官帖，仍为 Announced，不把预告写成已开盘。
- AscendLaunch：MUST_TODAY 本窗无新官帖。不是免费铸造。

## 跳过 / 不建卡（例行 X 扫描）

- 金毛矿工卡 Golden Miner Cards：本轮 KW_挖矿 再次见到第三方帖（@Annak0ox）指向 https://goldenminer.surge.sh/。硬规则新收录必须有推特，DeepSeek 判定 admit=false，本轮不建卡，也未为猎号另耗 X 读。
- @_O_R_N_G_ / $ORNG：自称首个水果主题 BTC L1 CRC-20 meme，经 @BONSonBTC 已上线并有游戏；官号 2026-09-29 开、约 29 粉。已是上线 meme，非未开盘打新，不建卡。
- @TSBdotfun / @Owlexart / @BLlPZ_NFT：仅出现在第三方免费 mint 名单（@Ava__Luna 与已在库的 Ape_CityRH / hoodgremlinrh / Mopes / Gangstazfun 并列），本窗无这些号自己的官帖或官网证据，证据不足，不建卡。
- Agent Life / Mintropolis / Baum / Grokie / Companions / RuninAI / VoltaFamily / madang 抽奖 / TapeOut-BEM 社区帖 / Squid×GIWA 测试网 / DogeOS 打赏任务等：均已在库或测试网/评论噪音，不作为新收录。
- 其它新作者噪音（Starknet 词误伤 Bramble 猫/啤酒、IOTA Pulse 仪表盘误伤、泵盘 bonding curve 信号）：已在库、空投号或无关内容，跳过。
