# 早期打新雷达 R2220 RESULT

工作目录 /tmp/r2220/。本路完成 X 常规增量（UF1–UF2 + MUST_WIN 24h + MUST_OFF 30m + 十栏关键词 30m + 条件瘦栏 24h + mentions 轮换 24h + SILENT_GIWA）、站点/链上核验、DeepSeek admit/score、写盘并推送面板。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek）。dsFallback=false。

开跑约 2026-11-26 10:01 CST。写盘 lastScout=2026-11-26 10:16:41 CST。这是重置后的第五轮常规增量，不是 post-reset-full，lastFullAfterReset 保持 R2216。时区 Asia/Shanghai (CST)。关键站点/API/链上核验约 10:05–10:13 CST。

## 额度与模式

- 开火前 remainingBefore=892。首搜 UF1 之后今日剩余 891（脚注 remainingMinute=29 / remainingToday=891，todayReset=2026-11-27T00:00:00.000Z），确认 ample，继续主计划 21 次 + 条件瘦栏 24h 3 次。
- mode=ample，softCap=28，minSpend=20，silentCap=2。主扫 23 + silent 1 = 24，低于 softCap，已达 minSpend。未翻页（多组触顶有 next_token，均未跟）。未做探索性额外 X 读，未为「再确认」重读同一 handle。未把额度打到 0。未对 @starx_xlayer 做 getUsers 重读（MEN_PADS 查询里包含该 handle，仅作为 mentions 检索）。
- xReads=24（main=23，silent=1），remainingBefore=892，remainingAfter=868。
- 写盘 meta.xBudgetMode=ample。

各次脚注（result_count / remainingToday；全部 error=None）：
UF1 0/891，UF2 0/890，MUST_WIN 25/889（触顶有 next_token，未翻页），MUST_OFF 0/888，
KW_LZ 1/887，KW_TAPE 9/886，KW_GIWA 12/885，KW_DOGE 9/884，KW_BTC 2/883，KW_STARK 4/882，
KW_MINT 25/881（触顶），KW_MINE 2/880，KW_PAD 25/879（触顶），KW_GO 25/878（触顶），KW_ELY 12/877，KW_GAPS 7/876，
MEN_DOGE 3/875，MEN_BTC 25/874（触顶），MEN_STARK 3/873，MEN_PADS 25/872（触顶），
SILENT_GIWA 25/871（触顶），
KW_LZ_24 23/870，KW_BTC_24 25/869（触顶），KW_STARK_24 25/868（触顶）。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- 十栏已跑全（30m）：LZ 1、TAPE 9、GIWA 12、DOGE 9、BTC 2、STARK 4、MINT 25 触顶、MINE 2、PAD 25 触顶、GO 25 触顶、ELY 12、GAPS 7。MUST_WIN 24h 25 触顶、MUST_OFF 30m 0。coverage.tenLanes=true，kwDeferred=false。
- UF 已刷完。cursor 497 @rheacatnear 起 50 号至 @hoodskullsfun；写盘后 cursor 547 @yeetr_fun，wrap=false。预跳已知 NF 8 个（含起始号 @rheacatnear 以及 @99901dotfun @magnitudeagent @bububullfun @lanternfield @streamlitmaker @trycortano @hook404rh），故 from: 实际 42 个（UF1 25 + UF2 17）。UF1 result_count=0，UF2 result_count=0。用户点名但长期 NF 的 @starx_xlayer 禁止 getUsers 重读。写盘后 UF 总账户 2440（本轮新挂 @edictink）。
- 瘦栏 24h：仅对 30m 命中 <5 的栏各补 1 次。已补 LZ（30m=1→23）、BTC（30m=2→25 触顶）、Starknet（30m=4→25 触顶）。跳过 Tape（30m=9）、GIWA（30m=12）、DogeEVM（30m=9），原因 30m>=5。未把肥栏改成 24h。thin24hDeferred=false。
- mentions 覆盖: DogeEVM 3 / BTC 25 触顶 / Starknet 3 / pads+squeek+STARX 25 触顶（均为 24h 轮换）。下轮：GIWA / Tape / LayerZero / Elysium。mentionsDeferred=false。
- silent: GIWA（search_users 不可用，24h has:mentions 回退；result_count=25 触顶，seen=25，sentToReview=0，admitted=0，ran=true）。未知作者多为 @GAMA_GIWA / Gamatiles 测试网体验帖（GAMA 已在库），无新项目，未送审。下轮：DogeEVM。silentDeferred=false。

## 新收录

- Edict（@edictink / https://edict.ink/），id=edictink，台子/Meme，Solana。建号 2026-11-23 09:31:54 CST（约 3.02 天），46 粉 / 5 帖，未认证，xUserId 2124676769416433664。官帖 2026-11-26 10:00:26 CST（https://x.com/edictink/status/2125771630617980930）宣布 Edict is open：可在 pump.fun / Meteora / Raydium 发射，持有人奖励在发射时锁定，$EDICT is up next。官网 HTTPS 200，页面回链 @edictink（siteXMutual=yes）；Launch 页 https://edict.ink/launch HTTPS 200。$EDICT Launching soon；Seals 250 NFT 菜单标 SOON，未见已开铸。GitHub https://github.com/edictink。不是免费 mint，也不是免费登记。DS score overall=64（early=94 / actionable=55 / novelty=58 / risk=86），admit=true。已挂 userFollowWatch + agentPadWatch。focus=false。links.x 与 links.twitter 双写。本号不自动 mint。

newThisRound=["edictink"]。

## 看见但未收

- LumixPad（@lumixpad / https://lumixpad.fun/）：资料栏账号建于 2023-09-05（约 1177 天），仅 18 粉 / 3 帖。本轮该号无原创帖（未额外重读），只在 KW_PAD 见到 10 粉账号 @coachchesterlee 回复声称官网已 live、0 币发射、0% 平台费。官网 HTTPS 200，标题 LumixPad — 0% Fee Launchpad and DEX，页面写 No coins launched yet。不是免费 mint。因旧号、无本轮官帖、早期证据不足，DS admit=false。
- antwork（@antworkdotfun / https://antwork.fun/）：建号 2026-11-25 23:00:54 CST（约 0.46 天），170 粉 / 101 帖。本轮无原创帖进入搜索（仅 MEN_PADS includes，未额外重读）。官网 HTTPS 200，正文仅 “setting up the Hill”，未见 mint/登记入口。DS admit=false。
- @HamsteCombatHQ：本轮未见。R2219 已因无官网/合约、score=38 拒绝，无需反复送审。
- @WorldsEndFarm：Starknet「Bramble」关键词误伤（农场清杂草），跳过。
- @Arabiaxjan 等新号：仅转发已在库 @MMIX_io / @Spike__wtf / @StinkyPenguinL0 等，不是项目方。
- 其余 KW/mentions 多为已在库项目转载、KOL 互动或无站点无官帖的噪声。MUST_WIN 25 条均为已在库官号（fueltenderagent、2hourfun、ShieldedWizBTC、GunsOfTheHood、antopia_xyz、agentcardshq、uglypuggies），只做状态刷新。MUST_OFF 0 帖。UF 本轮 0 帖。

## 关键刷新 — 库内无改期、无首次 ≤2h（不因进度重推）

- 2hour.fun @2hourfun：第一场窗口仍关闭。RSC payload `open=false`；首页 SSR 仍可能显示 Window open 占位，不以该标签为准。下一窗仍为 2026-11-27 05:00–07:00 CST（约 18.7h，未到 ≤2h）。平台币 $2HOURFUN 仍在曲线、未毕业，CA 54PSWdiJbeF9H9Eumi3fLc8wfiLE3igN3GAuxb5zUeHi，pool AWPh3HYuc2e9d7ooAuEZhL75SoMRTggLCLWAh7bHjyDY，进度约 14.3%，约 $5.2k mcap，已筹约 16.03 SOL / 约 $1138（R2219 约 14.3% / $5.1k / 15.98 SOL），最后成交约 2026-11-26 09:48:48 CST。关窗、第二窗时间与发币费改免费此前已通知，本轮 MUST 无新官帖（最新仍是 07:07 CST），只是进度，不重推。
- Shielded Wizards @ShieldedWizBTC：免费公售仍 LIVE。API phase=public，minted=118/3333（R2219 为 114），reserved=6，mintOpen=true，price=0。公售页 https://brimhollow.app/mint 。R2210 已通知，只是进度。
- Guns Of The Hood @GunsOfTheHood：付费公售仍 LIVE。OpenSea SeaDrop mintStatus=MINTING，100/10000（R2219 为 90），持有 14，地板 0。合约仍是 0x1d3f3b153533bde7912da634b38ab50b3b90456d。R2210 已通知，只是进度。不是免费 mint。
- Ugly Puggies：仍 MINTING，312/777（与 R2219 持平），持有 239，地板 0.000167 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST（写盘时约 3.2h，未到首次 ≤2h；该阶段结束后仍是 SIGNED_PRESALE #3，公售 2026-11-27 13:30 CST）。本轮新官帖 2026-11-26 10:02:13 CST（https://x.com/uglypuggies/status/2125772081011040521）承认 mint 不及预期、WL 未正确添加、信息不透明，并称仍在建设（引用此前开铸帖）；API 未返回 note 全文，t.co 指向被引用的开铸帖。OpenSea 阶段表未改，不是已确认改期/关窗，不按改期重推，也未到首次 ≤2h。
- deMiners：仍 MINTING，1368/3333（R2219 为 1364），持有 181，地板约 0.000107 ETH。PUBLIC_SALE 仍至 2026-11-28 00:30:04 CST。
- The Jacket：仍 MINTING，214/777，持有 136，地板 0.61 USDG，active 仍 PUBLIC_SALE。与上轮持平。
- Agent Cards：官网 /api/mint/status 仍 phase=open，fillSold=5000/5000，curveSold=533，sold=5533/1,007,493（与 R2219 持平），现价约 0.00216 BNB。本轮 MUST 官帖（08:06 CST）提出三种 AGENTMINT 补偿方案，不是改期或新开铸。
- TRIFORGE：链上 Forge Keys 817/3333（R2219 为 812），claims 38（持平）。预售仍开至 2026-12-02，挖矿仍开。
- F0B90B：链上 458/10000（R2219 为 457），mintOpen=True。只是进度。
- Antopia：链上 6305/8888（R2219 为 6264），saleOpen=True，免费额度仍满。本轮 MUST 官帖（08:19 CST）仍称付费窗至 2026-11-27 12:45 UTC（20:45 CST）关闭，Clash of Antopia 2026-11-26 13:00 UTC（21:00 CST）上线（gameAtCST 此前已记）。距关停约 34.5h，未到 ≤2h，不是改期，不重推。
- VALORIX：链上 Hero Cards 16（与 R2219 持平），fillSold=0/5500。只是进度。
- AGX：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」。本轮 MUST 未见 @Agx_bsc，未做额外 X 重读。
- Bonebloom：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，PUBLIC_SALE 仍 2026-11-28 02:30 CST。距首窗约 34.2h，未到首次 ≤2h。
- Slime Agents：SeaDrop 仍 MINTING_SOON 0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- Vicehood @Vicehood_RH（官集合集 vchood）：官网仍 Early List。SeaDrop 仍 MINTING_SOON 0/3333，SIGNED_PRESALE 仍自 2026-11-27 01:00 CST 起，距首窗约 14.7h，未到首次 ≤2h。同名合集 vicehood（非该官号，本轮仍 209/3333 已在铸）未与官号混淆。
- Wildlife Universe / Tiger Universe：SeaDrop 仍 MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起。距首窗约 11.2h，未到首次 ≤2h，不提前告警。
- Bons Genesis @bons_world：官网仍存活。OpenSea bons-genesis 仍 119/1111，SeaDrop 仍 MINTING，active PUBLIC_SALE 至 2026-12-22 01:00 CST。原免费 WL 窗已过，公售仍开；旧 le2h 文案已过期。不是免费 mint LIVE，不重推。本轮 osstats 再遇 401，持有/地板未刷新；集合 API total_supply=119，与上轮一致。
- CITYHOOD @appcityhood / cityhood.fun：官网仍 Minted 0/4,333，并残留已过期「Public mint opens today」。原 2026-11-23 窗口已过，无改期、无新开铸确认。勿与 @CityHood_NFT 合并。
- CITYHOOD @CityHood_NFT / cityhood.online：前端 /api/config 本轮仍返回 SPA HTML；后端 https://cityhoodbackend-production.up.railway.app/api/config 仍 chainId=46630 Robinhood Chain Testnet，合约地址与此前相同。市民登记仍开，主网铸造未确认，不是免费 mint LIVE。勿沿用过期「今晚 22:00」文案。勿与 cityhood.fun 合并。
- ClankTube：https://clanktube.fun 仍 HTTP 200，免费早期登记仍开（关注+互动+EVM 地址），未见开铸，不重推。
- OTC Rings / Famulus：R2216 新卡，本轮站点仍 HTTP 200，状态未变，不重推。
- FOMO4NFT：R2217 新卡，官网 https://fomo4nft.com 与发射台 https://launch.fomo4nft.com 仍 HTTP 200，非免费 mint，状态未变，不重推。
- Heliring：R2218 新卡。本轮访问 https://heliring.app/ 遇到 TLS 错误（TLSV1_ALERT_INTERNAL_ERROR），未能重新打开页面。未见新官帖或改期/开铸证据（MUST 未覆盖该号，未额外重读）。非免费 mint，不按状态变化重推。
- Canton/Glaze/TokenWorks：本轮无新该类 admit，仅刷 lastChecked。

## notify 判定

- notify=true。
- alertMessage：新增 Edict（@edictink）：Solana 发射台已开站，非免费 mint，$EDICT 即将发射；本轮无免费 mint/登记。面板：https://reboot7454.github.io/early-scout/ 。本号不自动 mint。
- 原因：真新收录 Edict。库内 2hour / Wizards / Guns / Vicehood / Wildlife / Ugly Puggies / Bonebloom / Bons / CityHood / FOMO4NFT / Heliring / ClankTube 等无改期、无首次 ≤2h，不按进度重推。Ugly Puggies 写盘时距 13:30 CST 约 3.2h，未到首次 ≤2h。R2216 / R2217 / R2218 新卡无状态变化，不重推。Edict 不是免费 mint/登记，告警已点名项目，未写成「入库 N 项见面板」。
- namedFreeMintOrRegistration=[]，namedMintConfirm=[]，namedPaidLe2h=[]，namedScheduleChange=[]，newCards=["edictink"]，le2h=[]。

discordPeekDeferred=true（X 路径占位，未假装已 Peek）。dsFallback=false。

面板：https://reboot7454.github.io/early-scout/

## 交付

- 推送文件：data.json、docs/data.json、RESULT_R2220.md（仅这三项进 main）。
- notify.json 已写 /tmp/r2220/notify.json（通常不提交）。
