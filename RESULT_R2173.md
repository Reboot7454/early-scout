# RESULT R2173

- time: 2026-11-25 09:48:20 CST（Asia/Shanghai）
- mode: ample（08:00 CST 重置后常规增量；lastFullAfterReset=R2170，本轮不是全量补扫）
- notify: true
- xReads: 26；remainingBefore: 910；remainingAfter: 884 / 1000（mode=ample，softCap 28，minSpend 20，silentCap 2；主扫 22 + SILENT_TAPE 1 + 瘦栏 24h 3；getUsers=0。不含 silent 的主扫为 25，未超 softCap；silent 可计在 softCap 外。已达 minSpend）
- userFollow: 已刷完。soft-brush 711 @elyword_xyz 起 50 号至 @oblaunchpadAll；next 761 @askglyph，wrap=false，MUST 重叠 0。UF 30m：UF1–UF3 均 0 帖。写盘后 UF 总账户将含新收 @TriForgeAgent（2374→2375）。
- 十栏关键词: 全部跑到（30m）：LZ 0、TAPE 25 触顶、GIWA 7、DOGE 8、BTC 0、STARK 1、MINT 25 触顶、MINE 3、PAD 25 触顶、GO 25 触顶、ELY 2、GAPS 25 触顶。MUST_WIN 24h 25 触顶、MUST_WIN2 24h 25 触顶、MUST_OFF 30m 0。
- 瘦栏 24h 补搜: 是（仅 30m 独立 KW 命中 <5 的栏各多 1 次）。LZ（30m=0→17）、BTC（30m=0→25 触顶）、Starknet（30m=1→25 触顶）。Tape 30m=25、GIWA 30m=7、DogeEVM 30m=8 均 ≥5，未补 24h。未把肥栏关键词改成 24h。
- mentions 覆盖: 本轮轮换 24h：GIWA 25 触顶 / Tape 25 触顶 / LayerZero-24h 21 / Elysium-rest 24。未跑 DogeEVM / BTC / Starknet / squeek / STARX / pads-rest（留给下轮）。
- silent: Tape/电路（searchUsers 不可用，24h has:mentions 回退；ran=true，seen=3，sentToReview=0，admitted=0；3 帖均为已有 TapeOut 讨论/汇总，未见可建卡新官号）。下轮 silent：GIWA。
- 新收录:
  - TRIFORGE（@TriForgeAgent / https://triforge.fun）→ 栏「BN Agent 钱包」。2025-10-06 14:23:15 CST 建号（约 414.8 天），0 粉 / 1 帖 / following 19，未认证；账号较老且几乎无互动，存在改号/冷号启用风险。资料栏与官帖均指向官网。官网 HTTP 200（Vercel），标题 Forge Keys · Triforge；静态 HTML 仍有 “Contracts are not deployed yet” 的 JS 水合前占位，不以此判断未部署。config.js 写明 contracts DEPLOYED 2026-11-25 ~01:01 UTC，deploy block 135563285。官网与 JS 未见回链 https://x.com/TriForgeAgent（siteXMutual=no），但 token CA 与官帖一致：0xC73ddcd3A25fD576F1e10B6e755f04C9fBDF51dd。官帖 2026-11-25 09:17:23 CST（https://x.com/TriForgeAgent/status/2125398411570774087 ）称 LIVE：Forge Keys free mint live now，Mining live now，Presale opens 02:01 UTC，Agent ID gated。本轮用公共 BSC RPC 只读核到 token/nft/launchpad/mining 均已有代码；Forge Keys 22/3333、未暂停；claimsOpen=true、totalClaimed=0；miningTotalShares=1、未暂停；launchpad lpMintOpen=false、lpTotalMinted=0；lpMintStart=2026-11-25 10:01:25 CST（02:01:25 UTC），lpMintDeadline=2026-12-02 10:01:25 CST；tokenTradingEnabled=false；总供应 1T。免费 mint 仅 gas，每钱包基础 1 份、推荐 +1，每把 key 可领 25,000,000 TRIFORGE，领取后 7 天才可交易。付费预售 6,666 份、0.003 BNB/份，本轮核验时窗口未开。须持 Agent ID。已进 UF+freeMintWatch+agentPadWatch+bnAgentWatch+miningWatch。focus=false。DS overall=80。本号不自动 mint。
- 库内更新:
  - Ugly Puggies：本轮官帖 2026-11-25 09:35:25 CST（https://x.com/uglypuggies/status/2125402947144356156 ）再次称 first wl batch has been added，并给 OpenSea collection 链接，next wl batch soon。镜像开铸仍约 2026-11-25 21:00 CST，尚未进入 2 小时窗口，不提前告警，不重推。
  - 2hour.fun：官帖重申 $2HOURFUN 首窗 Tomorrow 21:00 UTC（= 2026-11-26 05:00 CST）。不要把 21:00 误读成今天 21:00 CST，不按 ≤2h，不重推。
  - Thinkers Club：付费公开铸仍 LIVE（官帖 07:10 CST 称当时还剩约 31 小时价格发现），不是免费 mint，不重推。
  - Shit Capital：Genesis 仍开放（官帖称约 48 小时关闭），不是免费 mint，不重推。
  - Shielded Wizards：白名单免费铸仍 LIVE；本轮官回仅称即将支持任意 Bitcoin 钱包铸造，未见关窗或公开售改期（公开售仍约 2026-11-26 05:10 CST）。本轮未核铸页进度，不编造新数字，不重推。
  - Flame-BTC：付费公开铸已 LIVE（R2171），本轮 MUST_WIN 25 触顶未见其新官帖，无关窗/改期，不重推。
  - Z3RO Terminal：本轮官帖为产品功能介绍，主网未开，不是免费 mint，不重推。
  - DAEMONS：MUST_WIN 再次见到 2026-11-25 09:00:01 CST 的 waitlist 官帖，无新的开铸/改期，不重推。
  - ANKOU：本轮 MUST_WIN2 未见其新帖，日期仍 TBA、未见登记已开，不重推。
  - lore：官帖 2026-11-25 08:39:31 CST 称 $lore is now live，CA ESzQdyodjDp6XoXcizp1LrGpJ9hTP2pwHJX5MNbUpump。仍是网页发币发射台，不是免费 mint，不重推。
  - Amend：官号持续发功能/费分帖，无新的免费 mint 或开铸窗口，不重推。
  - Lamoryant：免费登记已开，开铸仍约 2026-11-26 19:00 CST，不是 LIVE，不重推。
  - QQAI：开铸仍约 2026-11-26 18:00 CST，不是 LIVE。
  - Lynco Punks / PlatoUnseen / oripa-xyz：无新的 2 小时开铸窗口，不重推。
- 看见但未收:
  - DANDI（@dandi_fun / https://dandi.fun）：官网与官推互证（siteXMutual=yes），标题 DANDI — coming to Zero，自称 Live day one of Zero mainnet；本轮仅他人转述、未见自有官帖，主网未开，非可操作窗口，暂不收。
  - zauberdotfun：约 0.45 天新号，bio 自称 Solana 隐私发射台；zauber.fun 打开为 Offline。本轮仍无自有官帖，仅猎人名单，保持不收。
  - z000fun：资料栏 https://z000.fun/ 本轮 TLS 失败、http 500，仅猎人名单提及，保持不收。
  - WeathookETH / PilotusTrade：无官网、本轮无原创官帖，仅猎人名单，不收。
  - warpnetp2p：https://warpnet.site 可开，去中心化社交网络，无 mint/发射窗口，保持不收。
  - OrdDropz：已运行较久的 Ordinals 发射/市场基础设施（约 388 天、1804 粉），非本轮新早期铸造窗，不建卡。
  - motiontradingx：社交账号永续纸交易，非 mint 窗口，不收。
  - lithiumlend：LitVM 借贷，官网回链官推，无 mint 窗口，不收。
  - ShieldSuite_：称 TapeOut 加密通讯产品明天上线，不是免费 mint/铸造窗，不收。
  - Nostalgicgareth 自称重建 btcpad（btctalk 风格 runes 发射台）：个人开发者号，未见独立官号/官站互证，不收。
- Discord Peek: attempted，loginOk=false，discordPeekDeferred=true。登录墙 https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1537897411668746302 。lastSeen 未改（2026-11-23 22:19–22:56 CST，积压约 35h+）。R2158 已请用户重登，本轮 nag=false，未重发登录表。
- 失败 / dsFallback: 无。DeepSeek flash 评分与 alert 均成功（评分 overall=80，admit=true）。X 搜索 26/26 成功，无重试。write_to_file 预览曾截断长行，已改用完整资产文件解析，数据齐全。
- 写盘说明: 执行端未改 /workspace/early-scout/data.json，也未 git commit / push。自检可用：
  `cp /workspace/early-scout/data.json /tmp/r2173/data.json.src && EARLY_SCOUT_DATA=/tmp/r2173/data.json.src APPLY_DRY_RUN=1 APPLY_DRY_OUT=/tmp/r2173/data.json python3 /tmp/r2173/apply_r2173.py`
  父代理正式写盘：先备份，再 `APPLY_ALLOW_WORKSPACE=1 EARLY_SCOUT_DATA=/workspace/early-scout/data.json python3 /tmp/r2173/apply_r2173.py`（不要用执行端来 commit/push）。自检 dry-run 已成功（WATCH_LEAK_RECENT 0，added triforge，uf_next 761 @askglyph）。

## notify / alert

- notify: true
- reason: 真新收录 TRIFORGE：Forge Keys 免费 mint 已链上 LIVE（22/3333）；付费预售窗口 2026-11-25 10:01:25 CST 起（本轮核验时未开）。
- alert:

值班提醒 R2173：新收录 TRIFORGE（@TriForgeAgent / https://triforge.fun）——BNB Chain、Agent ID 门槛，Forge Keys 免费 mint（仅 gas）已链上 LIVE（本轮只读核到 22/3333、未暂停），挖矿已开；付费预售 0.003 BNB/份窗口 2026-11-25 10:01 CST 起，本轮核验时尚未打开（lpMintOpen=false）。账号约 415 天、0 粉 / 1 帖，有冷号启用风险，官网未回链官推。面板：https://reboot7454.github.io/early-scout/ 本号不自动 mint。
