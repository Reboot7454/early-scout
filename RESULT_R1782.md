# RESULT R1782（例行 pace 合并进 Discord 已占轮）

- time: 2026-11-14 03:39:46 CST（Asia/Shanghai）。开跑前 `git pull`，随后 Discord 于 03:34:44 CST 推送 R1782（commit 523ff36，补收 fluxadotfun / silvexmining / zdripsol / yieldyfun / orrerynode，已通知，不重推）。例行再次 `git pull --ff-only` 后把 pace 扫描合并进同一轮，不另起 R1783。notify=false。未自动 mint。
- mode: tight merge（R1739 已完成 08:00 CST 后首轮全量补扫，本轮不是又一次重置后全量补扫）
- lastFullAfterReset: R1739
- notify: false。pace 本轮无新收录、无新确认免费 LIVE / 首次 ≤2h。polyrob 公开销售仍 11-14 22:00 CST（约 18h）；agent-cat 开铸仍 11-14 21:00 CST（约 17h）；burybud / ape-city 仍 11-14 23:00 CST（约 19h）；agx-402 migrationDeadline 仍 11-14 16:00:58 CST（约 12h）。均非 ≤2h。Discord 五张新卡已推，不重推；oathbots / bagnotary / ponke-agent / boxcars / 免费 LIVE 已推项目仅进度刷新。
- xReads: 13（main 12；silent 1；admitVerify 0）；remainingBefore 110 → remaining 97 / 1000；softCap 10，minSpend 10，silentCap 1；main 12 超 softCap 2（UF×1 + 薄栏 Watch/MUST×3 + 薄栏 KW×6 + mentionsThin×2，未砍栏）。THIN 因 MUST+薄栏+zeroWatch 去重后 108 个 handle 无法在 1024 字符内装进 2 批，故多 1 次 THIN3，高于 minSpend。官网 / 链上 / HTTP / OpenSea / GeckoTerminal 只读无 X 成本。MUST_TODAY 已并进薄栏 Watch 批次并与 used-handle 去重（本轮 MUST 18 个，其中 AgentCatRh / DripEVM 已在本片 UF，故 THIN 实装 16 个 MUST；另增 Ape_CityRH）。from: 官号窗 start_time=2026-11-13T18:55:00Z；关键词 / mentions / silent start_time=2026-11-13T19:00:00Z。不翻页 next_token。
- admitVerifyReads: 0。未为候选另耗 X 读。硬禁无官推核验：本窗 pace 无新收录候选。
- tenLanes: true（薄栏 6 条独立 KW LayerZero/Tape/GIWA/DogeEVM/BTC/Starknet 均已跑。核心栏因 tight / alloc.kwCore=0 本轮延后。BN Agent 靠已有卡 + 官网/RPC 刷新，不另烧 fat shard。不翻页。帖量：LayerZero 2、Tape 4、GIWA 2、DogeEVM 8、BTC 8、Starknet 3。）
- laneReads: KW_LayerZero=1，KW_Tape=1，KW_GIWA=1，KW_DogeEVM=1，KW_BTC=1，KW_Starknet=1；核心栏本轮未跑（kwCore=0）
- userFollow: 刷完本片 1558→1598，kept 40，skip 0，1 from: batch，本片 3 帖（@AIAgent_OSK 03:03:07 CST 再确认免费席已尽、现 0.008 BNB/席、开池仍 11-15 18:00 CST；@aurbitdotfun 12/1 权重重置预告；@spindottrading 发布已在卡内的 Robinhood CA）。下一轮从 1598 续（UF accounts=1687，含 Discord 本轮补挂 5 个官号；本轮不是整表一次扫完，未绕回）
- mentions: 本轮轮换已覆盖 GIWA、DogeEVM（薄栏 mentionsThin；R1781 已覆盖 LayerZero+Tape，R1780 已覆盖 BTC+Starknet）。kwCore=0、mentionsRest=0，本轮不跑核心栏 KW、不跑 rest mentions。均已跑，不翻页。帖量 MENT_GIWA 2、MENT_DogeEVM 2（均为已在库号的回复/社区提及）。
- fat shards: 本轮 tight 跳过厚表分片，光标不变：agentPad 154 / freeMint 242 / bnAgent 71 / elysium 168。未改 meta.fatNextStarts。
- thin official watches: 3 个 from: 批次（MUST 优先装进第一批）。去重后薄栏+zeroWatch 独立 handle 92，加 MUST 后扣除本轮 UF 重叠（ZeroGuysNFT / ZROfun 以及 MUST 中已在 UF 的 AgentCatRh / DripEVM）及已知 NF TapeFractal / FoundryTape 不连刷后查询 108。本窗 THIN1=3 帖 / THIN2=1 / THIN3=0（含 @burybud 03:00:01 CST 再确认 15:00 UTC 上 Pons、@banknotes_btc “THE LOST COIN FINAL HOURS OF BETA” 直播、@giwapad_xyz 回复）。无 @bagnotary / @boolish_rh / @giraffies_nft / @PonkeAgent / @Oathbots / @HoodedApeClubRH / @Ape_CityRH / @agentai_lotto / @AgentCatRh 本窗官帖（后两个在 UF 批次，同样无帖）。公开销售/预约均非 ≤2h。
- silentAccounts: ran=true，lane=打新（round 1782 % 11 = 0；search_users unavailable，改跑 mentions `has:mentions has:links ("fair mint" OR "free mint" OR whitelist) -is:retweet`，softCap 外 1 读）；回包多为 @CompanionsWfit 任务拉人（库内已有 companions-wfit）及一条 @jirobots Lands 白名单拉人（无官号本窗发帖，未另耗 admitVerify 核验）。filter 未把新号送审，admitted=0。未做第二读。
- discordPeekDeferred: false（本例行默认不登录 DC；开跑前 Discord 已占用本轮并补收 5 卡，例行合并进 R1782。未尝试登录）。
- DS: 例行 pace 无新收录候选送审，未另开 DeepSeek 批次。未编造 CA/官号/官网。未自动 mint。
- MUST_TODAY: hooded-ape 仍售罄 1500/1500，本窗无新官帖，不重推；OS sales 1598→1618，owners 537→542，floor 约 0.00015 ETH（本轮单位为 ETH，此前约 0.13 USDG）。lil-giraffies 本窗无新官帖，OS 仍 6666，sales 9185→9250、owners 3978→3959、floor 约 3.07 USDG，不重推。polyrob 公开销售仍 11-14 22:00 CST，OS 集合+stats 本轮均 401，上次已铸 32。oathbots 预售仍 OPEN，0.825 BNB / 28 钱包不变。HonestBull 已售仍 23/10000。boxcars 驾照仍 174/1000。ponke-agent 仍 63/11055、免费 63/555。agx-402 unitsMinted 仍 10339，distributedAgx 仍 4.1356 亿，接口再变为 PRICE_UNAVAILABLE、phase=POST_MIGRATION，genesisClaims 仍 OPEN，voting 仍 SERVICE_DISABLED，migrationDeadline 仍 2026-11-14 16:00:58 CST。bagnotary 池储备约 3249 USD（此前约 3237），成交约 2377 USD，R1775 已推开盘，不重推。agent-lotto 链上仍 0/300，R1781 已推，不重推。
- watch-bug: Discord 五张新卡开跑时已在 userFollowWatch（orrerynode 兼挂 miningWatch）。本轮把 silvexmining 补进 miningWatch（60 秒网格抽块玩法）。fluxadotfun / zdripsol / yieldyfun 只挂 userFollowWatch，未兼挂 pad 表。本轮未做整表回填。
- new cards: pace 无新卡。保留 Discord 本轮 newThisRound（fluxadotfun, silvexmining, zdripsol, yieldyfun, orrerynode）。meta.newThisRound == 顶层 newThisRound == round1782Added。candidateCount=4215（顶层与 meta 对齐）。UF accounts=1687。

## 仍在跟（刷新，不重推）

- hooded-ape-club：仍售罄 1500/1500。本窗无新官帖。效用约 08:26 CST 预告不是新开铸窗，不重推。OpenSea 仍 1500，sales 1598→1618，owners 537→542，floor 约 0.00015 ETH。公开 Robinhood RPC 仍 hasCode false。
- lil-giraffies：本窗无新官帖。OpenSea 仍 6666，sales 9185→9250，owners 3978→3959，floor 约 3.07 USDG。合约 0x440c0d01…。铸造窗已过，不重推。
- polyrob：本窗无官号新帖。公开销售仍 11-14 22:00 CST，距窗约 18h，非 ≤2h。铸造页仍 200；polyrob.xyz 仍 SSL EOF。OpenSea 本轮集合+stats 均 401，上次已铸 32。仍需 WL。R1772 已推，不重推。
- oathbots：$OATH 付费预售仍 OPEN。链上已存入仍为 0.825 BNB / 28 钱包，finalized=False，50000000 枚 OATH 仍在预售合约内。窗口至 11-18 22:00 CST。非免费。R1773 已推。
- bagnotary：$BAGNOT 已开盘（R1775 已推）。Pons V2 池储备约 3249 USD，FDV 约 3215 USD，成交约 2377 USD（近 1h 无成交）。官网仍 SSL 失败。官 CA 仍为 0x977441dc…。
- boolish-rh：Possession night 预约已过。本窗无官帖；boolish.fun 仍 200。OpenSea boolish 本轮 401。未能核验是否已开铸。不重推。
- honestbull：Issue #1 付费公平份额铸造仍 LIVE。链上已售仍 23/10000，remaining=9977，saleEnd 2026-11-18 02:29:53 CST。R1767 已通知，不重推。
- boxcars：免费驾照仍开放，链上已领仍 174/1000。预售 11-17 21:00 CST。R1766 已通知，不重推。
- ponke-agent：免费公平铸造仍 LIVE。链上仍 63/11055，免费仍 63/555，paid=0，gift=0。R1769 已通知，不重推。
- myco：官网 200。BSC 链上 NFT 0x86229C12… totalSupply 仍为 0。R1764 已通知，不单独重推。
- agx-402：接口本轮再变为 PRICE_UNAVAILABLE，phase=POST_MIGRATION。unitsMinted 仍 10339，distributedAgx 仍 4.1356 亿，liquidityU 约 8552。poolOpenedAt 仍 11-13 17:25:44 CST；genesisClaims 仍 OPEN；voting 仍 SERVICE_DISABLED。migrationDeadline 仍 11-14 16:00:58 CST，距截止约 12h，非 ≤2h。价格再次不可用不是新的免费窗，不重推。本号不自动 mint。
- dripevm：白名单免费仍开。供应仍 166/888；OpenSea stats 本轮 401。公开铸造仍为 11-16 06:00 CST。已通知过，不重推。
- the-syndicate-rh：OpenSea 已铸仍 925/1000；owners 366，sales 838，floor 约 0.15 USDG。公开 Robinhood RPC 仍失败。
- jpeg-monkes：OpenSea 已铸仍 1508，sales 1877→1884，owners 871→870，floor 约 0.00056 ETH。不重推。
- hood-terminals：OpenSea 仍 528/777，sales 仍 666，owners 仍 342，floor 约 0.00090 ETH。不是免费窗。
- boatn-fish：api/stats 已铸 1798→1803/2222，wallets 148→149，priceUsd≈2.62。不是新的免费开铸窗，不重推。
- arctic-bear：链上已铸仍为 82/5555。官网仍 200。
- clause-protocol：链上已铸仍为 9/7777。ClauseMint 本轮 eth_call 仍 revert。官网仍 200。
- momo-mochi：链上已铸仍为 300/2222。官网仍 200。
- tsbdotfun：OpenSea the-shadow-born 供应仍空；stats sales/owners 为 0。不重推。
- ashling：官网仍 SSL EOF。R1772 已通知，不重推。
- clankbots：Ink 免费白名单登记仍 LIVE，whitelist.html 仍 200。R1772 已通知，不重推。
- burybud：官号 03:00:01 CST 再确认 $BURY 于 11-14 23:00 CST 上 Pons，CA 仍未公布。距窗约 19h，非 ≤2h。官网 burybud.xyz 本轮恢复 200（R1781 为 SSL EOF）。不预推。
- agent-cat：仍未开铸。官网 200。OpenSea 供应仍 0，stats 401。开铸仍 11-14 21:00 CST，距窗约 17h，非 ≤2h。本窗无官帖。
- ape-city：本窗无新官帖。开窗仍 11-14 23:00 CST，距窗约 19h，非 ≤2h。价格仍待核验，不改成 LIVE，不预推。
- agent-lotto：本窗无新官帖。链上 totalSupply 仍为 0/300；官网 200。付费彩票，R1781 已通知，不重推。未自动 mint。
- osk-agent：官号 03:03:07 CST 再确认免费席已尽，现 0.008 BNB/席，开池仍 11-15 18:00 CST。保持 status=failed，不重推。未自动 mint。

## 例行侧 skips

- @AIAgent_OSK 付费席再确认：已在库 osk-agent，免费席早已结束，不另建卡、不重推。
- @aurbitdotfun 12/1 重置预告：已在库，不是新打新窗。
- @spindottrading 公布已在卡内的 Robinhood CA：已在库，不另建卡。
- @burybud 再确认 15:00 UTC：已在库，档期未改，非 ≤2h。
- @banknotes_btc “THE LOST COIN FINAL HOURS OF BETA” 直播：已在库，不是新打新。
- @giwapad_xyz 回复 @GIWA_by_Upbit：已在库 giwapad-xyz，不是新开铸。
- @niubainan 提到 Griftords 仍在铸：第三方资讯，未见官号；合集铭文可追溯至 2025，非极早期，未收录、未另耗 X 核验。
- Tape 窗为社区回复 / @tapexo_app 创始人整理帖，无新官号开铸，不收录 TapeXO。
- LayerZero 关键词窗 2 帖均为 Flare DVN / OFT 流量转推，无新打新。
- MENT_GIWA / KW_GIWA 为感谢与已在库号回复，不另建卡。
- DogeEVM / MENT_DogeEVM 窗为 DogeOS 主网临近讨论、打赏机器人与社区帖，无新的主网官铸，不收录。
- BTC 窗其余帖为 Shielded Naka 二次销售与社区转推，已在库项目，不另建卡。
- Starknet 关键词窗 3 帖均为猫/游戏同名 Bramble 误伤，无 Starknet 打新信号。
- silent 打新 mentions：@CompanionsWfit 任务拉人已在库；@jirobots Lands 白名单仅第三方拉人，未见官号本窗发帖，不收录。

## 面板与推送

- docsSynced=true（Pages 源为 main:/docs；根目录与 docs/data.json 一并推到 R1782 merge）
- panel: https://reboot7454.github.io/early-scout/
- 未自动 mint。
