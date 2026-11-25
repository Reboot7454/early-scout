# RESULT R2174

- time: 2026-11-25 10:12:58 CST（Asia/Shanghai）
- mode: ample（常规增量；lastFullAfterReset=R2170，本轮不是 08:00 CST 后首轮全量补扫）
- notify: true
- xReads: 28；remainingBefore: 884；remainingAfter: 856 / 1000（mode=ample，softCap 28，minSpend 20，silentCap 2；主扫 23 + SILENT_GIWA 1 + 瘦栏 24h 4；getUsers=0。主扫含瘦栏 24h 为 27，未超 softCap；silent 可计在 softCap 外。已达 minSpend。首次回包 remaining=883，未跌破 200，未收缩。）
- userFollow: 已刷完。soft-brush 761 @askglyph 起 50 号至 @Leeonmort；next 811 @computeroll，wrap=false，MUST 重叠 0。UF 30m：UF1–UF3 均 0 帖。写盘后 UF 总账户将含新收 @spcxchain（2375→2376）。
- 十栏关键词: 全部跑到（30m）：LZ 0、TAPE 17、GIWA 11、DOGE 4、BTC 0、STARK 1、MINT 25 触顶、MINE 2、PAD 25 触顶、GO 25 触顶、ELY 10、GAPS 24。MUST_WIN 24h 25 触顶、MUST_WIN2 24h 25 触顶、MUST_OFF 30m 0。
- 瘦栏 24h 补搜: 是（仅 30m 独立 KW 命中 <5 的栏各多 1 次）。LZ（30m=0→17）、DogeEVM（30m=4→25 触顶）、BTC（30m=0→25 触顶）、Starknet（30m=1→25 触顶）。Tape 30m=17、GIWA 30m=11 均 ≥5，未补 24h。未把肥栏关键词改成 24h。
- mentions 覆盖: 本轮轮换 24h：DogeEVM 9 / BTC 25 触顶 / Starknet 5 / squeek 0 / STARX 0。未跑 pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest（留给下轮）。
- silent: GIWA（searchUsers 不可用，24h has:mentions 回退；ran=true，hits=25 触顶，seen=9，sentToReview=9，admitted=0）。送审 zauberdotfun / vestedfun / CircusLaunchpad / GitZero_ / z000fun / PilotusTrade / WeathookETH / warpnetp2p / silentkeyeth，均未收。SPCX Chain 来自 KW_PAD，不计入 silent admitted。下轮 silent：DogeEVM。
- 新收录:
  - SPCX Chain（@spcxchain / https://spcxchain.network）→ 栏「台子/Meme」。2026-11-23 03:08:55 CST 建号（约 2.29 天），135 粉 / 17 帖 / following 10，未认证。资料栏指向官网，并写 $SPCXC CA 0x904ccdcee00a4f4596b1e92604c00274b75cb244。本轮 KW_PAD 见到转发的官帖 2026-11-25 08:38:03 CST（https://x.com/spcxchain/status/2125388510941339842 ）：发射台 beta 已上线，可在主网发币、首块即可交易，新币走 bonding curve，4.2 SPCX 毕业；买卖 1% 基础费，70% 给创建者（原文后半被配图截断，未编造剩余分成）。官网 HTTP 200，标题 SPCX Chain — Equity-powered execution，页脚回链 https://x.com/spcxchain（siteXMutual=yes）。自称独立 EVM L3，父链 Robinhood Chain（ID 4663），本网 Chain ID 46630022，页面标 MAINNET LIVE，原生 gas 为 SPCX。发射台页 https://spcxchain.network/launchpad/ 写 No tokens have been launched yet。不是免费 mint。$SPCXC 在 Pons 另有项目代币页，与发射台「尚未有人发币」不矛盾。已进 userFollowWatch；无对应栏专用 Watch，非免费 mint 故不挂 freeMintWatch。focus=false。DS overall=82。
- 库内更新:
  - TRIFORGE（@TriForgeAgent / https://triforge.fun）：付费预售已确认打开。公共 BSC RPC（https://bsc-dataseed.binance.org/ ，约 2026-11-25 10:05:05 CST）只读：lpMintOpen=true，lpOpened=false，lpFinalized=false，lpTotalMinted=0，lpTotalPaid=0；lpMintStart=2026-11-25 10:01:25 CST，lpMintDeadline=2026-12-02 10:01:25 CST。Forge Keys 免费 mint 仍 LIVE 未暂停，进度 22/3333→56/3333；claimsOpen=true、totalClaimed=1（R2173 为 0）；挖矿仍开（miningTotalShares=1）；tokenTradingEnabled=false。本轮 MUST_WIN2 仍见到 09:17 CST 那则官帖（Presale — opens 02:01 UTC），未见新的开售官宣，以链上 lpMintOpen 为准。官网静态 HTML 仍有 JS 水合前 “Contracts are not deployed yet” 占位，不以该句判断未部署；siteXMutual 仍为 no。免费 mint 已在 R2173 提醒，本轮因付费预售打开与免费铸进度变化纳入 notify。本号不自动 mint。账号约 415 天、0 粉 / 1 帖，冷号风险仍在。
  - Ugly Puggies：再见到 2026-11-25 09:35:25 CST 官帖（first wl batch has been added），与 R2173 为同一则。镜像开铸仍约 2026-11-25 21:00 CST（13:00 UTC），尚未进入 2 小时窗口，不提前告警，不重推。
  - 2hour.fun：官帖继续称 Launching tomorrow / Tomorrow 21:00 UTC（= 2026-11-26 05:00 CST）。不要把 21:00 误读成今天 21:00 CST，不按 ≤2h，不重推。
  - Thinkers Club：付费公开铸仍 LIVE（07:10 CST 官帖称当时还剩约 31 小时价格发现），不是免费 mint，不重推。
  - Shit Capital：Genesis 仍开放（官帖称约 48 小时关闭），不是免费 mint，不重推。
  - Shielded Wizards：白名单免费铸仍 LIVE；本轮再见到官回称即将支持任意 Bitcoin 钱包铸造，未见关窗或公开售改期（公开售仍约 2026-11-26 05:10 CST = 21:10 UTC，不要误读成今天 21:10 CST）。本轮未核铸页进度，不编造新数字，不重推。
  - Flame-BTC：KW_BTC_24 见到官回称 Public mint is open。付费公开铸仍 LIVE，不是免费 mint，无关窗/改期，不重推。
  - Z3RO Terminal：官帖仍为产品功能介绍，主网未开，不是免费 mint，不重推。
  - DAEMONS：MUST_WIN 再见到 waitlist 官帖（Before Christmas，members 免费 mint），无新的开铸/改期，不重推。
  - ANKOU：MUST_WIN2 24h 未见 @ankou_art 新帖，日期仍 TBA、未见登记已开，不重推。
  - lore：官号发修 bug / 4chan 发币功能帖，仍是网页发币发射台，不是免费 mint，不重推。
  - Amend：官号持续发功能/费分帖，无新的免费 mint 或开铸窗口，不重推。
  - Lamoryant：免费登记已开，开铸仍约 2026-11-26 19:00 CST，不是 LIVE，不重推。
  - QQAI：开铸仍约 2026-11-26 18:00 CST，不是 LIVE。
  - Lynco Punks / PlatoUnseen / oripa-xyz：无新的 2 小时开铸窗口，不重推。
- 看见但未收:
  - zauberdotfun：约 0.46 天、19 粉、0 帖，bio 自称 Solana 隐私发射台；https://zauber.fun 仍为 Offline。本轮仍无自有官帖，仅猎人名单，保持不收。
  - vestedfun：约 1.06 天、419 粉、0 帖、已认证，bio 称 Launch tokens on public terms；vested.fun / vested.app 无实质官网，保持不收。
  - CircusLaunchpad：约 1.47 天、75 粉、0 帖，无可用官网，仅猎人名单，不收。
  - GitZero_：约 28.5 天、140 粉，自称 GitHub token launchpad；gitzero.fun / gitzero.io 本轮不可达，gitzero.xyz 为占位跳转，不收。
  - z000fun：资料栏 https://z000.fun/ 本轮 TLS 失败，仅猎人名单提及，保持不收。
  - WeathookETH / silentkeyeth / PilotusTrade：交易/工具向，本轮无可用官方铸造窗（pilotus.trade 存在但是 Telegram 交易代理，非 mint），不收。
  - warpnetp2p：http://warpnet.site 本轮 HTTP 500，去中心化社交网络，无 mint/发射窗口，保持不收。
  - Glowing Futures（@GlowingFutures / https://glowingfutures.xyz）：约 7.19 天、50 粉，官网回链官推（siteXMutual=yes），Built on GlazeCorp 的基金代币，$CAPS CA 已在资料栏；官网仍写 Pre-launch · figures go live at launch，无明确时间。本轮仅互动帖并 @Enter_Elysium，不因此标成 Elysium。DS admit=false。不收。
  - HANDLE（@get_handle / https://gethandle.fun）：约 12.76 天，已有 8242 粉 / 仅 5 帖。官网可打开并写 Claim your allocation / Sign in with X，但 HTML 未见回链官推（siteXMutual=no），本轮未见自有官帖。不是免费 mint。不收。
  - RGBMonsters（@RGBMonsters）：约 20 天、1 粉，自称 333 monsters 在 SatSea 免费 mint，官帖写 Soon™，无官网、无日期，不收。
  - TheFenceFun（@TheFenceFun / https://thefence.fun/）：GTA 奖杯兑 USDC 产品，官网回链官推，不是铸造窗，不收。
  - ArtemisArt / Forgotten（@artemisart_art / https://forgotten.artemisart.art）：约 3 年艺术家号、1842 粉，官网回链官推，计划 2026-11-28 20:00 GMT+1 在 Robinhood / OpenSea 发 1000 份 1/1，尚未进入 2 小时窗口，非早期号，不建卡。
  - UseIpoPad：本轮新建号、0 粉 1 帖、无官网，不收。
- Discord Peek: attempted，loginOk=false，discordPeekDeferred=true。登录墙 https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1537897411668746302 。lastSeen 未改（2026-11-23 22:19–22:56 CST，积压约 36h+）。R2158 已请用户重登，本轮 nag=false，未重发登录表。
- 失败 / dsFallback: 无完整 dsFallback。X 搜索 28/28 成功，无重试。DeepSeek flash 对 SPCX Chain 评分成功（overall=82，admit=true）；同批 glowing-futures 在 summary 处输出截断，但 admit=false / overall=38 已完整。get-handle 补评思考溢出未产出完整 JSON，结论明确为不收录，未用高成本模型。alert 调用成功（alertMessageDsRaw 已存）。write_to_file 预览曾截断长行，已改用完整资产文件解析，数据齐全。
- 写盘说明: 执行端未改 /workspace/early-scout/data.json，也未 git commit / push。自检可用：
  `cp /workspace/early-scout/data.json /tmp/r2174/data.json.src && EARLY_SCOUT_DATA=/tmp/r2174/data.json.src APPLY_DRY_RUN=1 APPLY_DRY_OUT=/tmp/r2174/data.json python3 /tmp/r2174/apply_r2174.py`
  父代理正式写盘：先备份，再 `APPLY_ALLOW_WORKSPACE=1 EARLY_SCOUT_DATA=/workspace/early-scout/data.json python3 /tmp/r2174/apply_r2174.py`（不要用执行端来 commit/push）。自检 dry-run 已成功（WATCH_LEAK_RECENT 0，added spcx-chain，uf_next 811 @computeroll，uf_total 2376；workspace 仍为 R2173 / lastScout 2026-11-25 09:49:48 CST）。

## notify / alert

- notify: true
- reason: 真新收录 SPCX Chain（发射台 beta 已上线，非免费 mint）；库内 TRIFORGE 付费预售已确认打开（lpMintOpen=true），Forge Keys 进度 22/3333→56/3333。
- alert:

值班提醒 R2174：新收录 SPCX Chain（@spcxchain / https://spcxchain.network）——Robinhood Chain 上的独立 EVM L3，主网已标 MAINNET LIVE；发射台 beta 已上线，官网写尚未有代币发射，不是免费 mint。库内 TRIFORGE（@TriForgeAgent / https://triforge.fun）付费预售已确认打开（lpMintOpen=true，2026-11-25 10:01:25 CST 至 2026-12-02 10:01:25 CST，0.003 BNB/份、共 6666 份，本轮 lpTotalMinted=0）；Forge Keys 免费铸仍 LIVE 未暂停，进度 22/3333→56/3333。本号不自动 mint。面板：https://reboot7454.github.io/early-scout/
