# 早期打新雷达 RESULT R2207

- 时间：2026-11-26 约 03:30–03:42 CST（Asia/Shanghai）
- 模式：tight（softCap=10，minSpend=10，silentCap=1）
- lastScout（dry-run）：2026-11-26 03:41:52 CST
- lastFullAfterReset：R2170（本轮是常规增量，不是 08:00 CST 后首轮全量补扫）
- 面板：https://reboot7454.github.io/early-scout/
- 本路径只做 X 雷达 / 站点与链上核验 / DeepSeek / dry-run 写盘；未 git commit/push，未改 `/workspace/early-scout/data.json`
- discordPeekDeferred=true（本轮未再开 computerUse，理由见 Discord Peek）

## X 额度与搜索

- 首搜脚注：UF1 结束后 remainingToday=75、remainingMinute=29；remainingBefore = 75+1 = **76**（与开火前预期完全一致，±20 内，保持已排 13 次，未加计划外搜索，也未改 near-exhausted / override-full）
- remainingAfter（末次 SILENT_GIWA 脚注）= **63**
- xReads = **13**（main 12 + silent 1）
- meta.xBudgetMode = tight
- MUST_OFF 本轮 tight 跳过（官号 30m 延期）；live remainingBefore=76 未到 ≥250 补跑阈值
- 有 next_token 的查询均未翻页
- 未对 @starx_xlayer 做 from: 重试，未对同一 handle 重复读取

| id | 窗口 | result_count | remToday（该次后） |
|---|---|---:|---:|
| UF1 | 30m | 6 | 75 |
| UF2 | 30m | 2 | 74 |
| MUST_WIN | 24h | 25（触顶未翻页） | 73 |
| KW_LZ | 30m | 0 | 72 |
| KW_TAPE | 30m | 7 | 71 |
| KW_GIWA | 30m | 25（触顶未翻页） | 70 |
| KW_DOGE | 30m | 6 | 69 |
| KW_BTC | 30m | 3 | 68 |
| KW_STARK | 30m | 2 | 67 |
| KW_CORE | 30m | 25（触顶未翻页） | 66 |
| MEN_STARX | 24h | 0 | 65 |
| MEN_PADS | 24h | 5 | 64 |
| SILENT_GIWA | 24h | 25（触顶未翻页） | 63 |

十栏：独立薄栏 6 条 30m KW 全跑；核心栏+GAPS 合并为一次 KW_CORE。UF 分片刷完。

### 薄栏 24h

未做。TAPE 30m=7、GIWA=25、DOGE=6 已 ≥5，不改 24h；LZ=0、BTC=3、STARK=2 虽 <5，但主计划 13 次后 remainingToday=63，远低于约 150 的补搜门槛。最多 2 次 24h 补搜的额度本轮不用。

## UF

- 本轮分片 cursor 2341 @MintuBots 起，至 @TheJacket_NVDA（名单原 40 个），但本轮把 @uglypuggies / @TheJacket_NVDA / @TriForgeAgent 从 UF 30m 挪到 MUST_WIN 24h，故 from: 实际 37 个：UF1 25 + UF2 12，wrap=false
- UF1 6 帖、UF2 2 帖：主要包括已在库的 @flamebtc_art 图片回复等，未见新的免费 mint/登记窗口，不因 UF 新建卡
- 写盘后 ufCursor=**2381 @NoPvPfun**，uf_total=**2433**（新收录 @AbyssLabsNFTCol / Bonebloom 追加在名单末尾，cursor 指向不变）

## Mentions / 静号

- 本轮覆盖：STARX（MEN_STARX 0）、pads-rest（MEN_PADS 5）
- mentionsNext：GIWA / Tape / LayerZero-24h / Elysium-rest
- 静号：GIWA，mentionQuery 兜底（search_users 仍不可用），SILENT_GIWA 25 条触顶未翻页。看见 @giwapunk、@GamaDotWin，未新建卡（见下）
- silentNext：DogeEVM

## 新收录

### Bonebloom（@AbyssLabsNFTCol / https://opensea.io/collection/bonebloom）

- 来源：KW_CORE 30m includes（本轮未直接拉到该号原创帖；相关转载提到 Bonebloom Genesis / @DeTopiq 免费 mint 抽奖）
- 建号 2026-08-30 22:17:23 CST（约 87.22 天），596 粉 / 3071 帖，资料栏即为该 OpenSea 合集；库内原先无此卡
- 简介自称：555 份以太坊 64x64 像素 PFP，111 Free / 444 Public（0.011 ETH），By Abyss Labs，Minting Nov 27
- OpenSea 合集 bonebloom：twitter_username=AbyssLabsNFTCol（与官号互证），externalUrl / project_url 为空，链 ethereum，合约 0x337354ebc02ba40ee01c46fa510ea19fdb20067d，total_supply=0，持有 0，成交 0，无地板；合集 created_date=2026-11-23
- SeaDrop（合集 HTML 转义 JSON）：mintStatus=**MINTING_SOON**，0/555，activeDropStage 空；SIGNED_PRESALE 2026-11-27 20:30:00 CST 至 2026-11-28 02:30:00 CST；PUBLIC_SALE 2026-11-28 02:30:00 CST 至 2026-12-08 02:30:00 CST。SeaDrop 片段未给出单价，111 免费 / 0.011 ETH 仅见简介自称
- **不是已开铸 LIVE**，距首窗约 41 小时，未到首次 ≤2h。自称含免费额度，须点名
- DeepSeek admit=true，overall=56（early 78 / actionable 38 / novelty 35 / risk 42），focus=false
- 已挂 userFollowWatch + freeMintWatch。dsFallback=false

## 看见但未收

- @giwapunk / GIWAPUNK：官网 https://giwapunk.xyz/ 200，与 https://x.com/giwapunk 互证。站点自称 5,000 份 GIWA Chain 1-bit punks，Free mint 4,450（89%，list + collabs，2/钱包），Public 500（Price TBA），Team 50；写明 The list is final、Nothing is minted yet、Community project. Not affiliated with GIWA or Dunamu。不是已开铸 LIVE，主名单自称已截止，未见合约与开铸时钟。DeepSeek admit=false（无开放早期登记窗、价格/时间 TBA）。R2204 也曾筛过未收，本轮不重收
- @GamaDotWin（gama.win，「premier token launchpad on GIWA」）及 launch.gamatiles.com：与已在库的 GAMA @GAMA_GIWA 同项目线索，不另建重复卡
- @2hourfunEco：2hour.fun 生态号，官网指向已在库项目，不新建卡
- @g4ngst3rcrypto / 其它 0 粉新号：只是跟 @LawoftheAbyss（已在库）free mint 口令，不是新项目官号
- KW_CORE 大量已在库项目转发（PlunderPort、Spike、Slime、Owltopia、Unicorn Grand Prix、Law of the Abyss 等），不重收
- @neetardio：11 粉，随机回复自称 $cashcat 持有人免费名单，证据不足，不收
- ONE LaunchPad @one_launchpad：用户点名已在 R2205 面板合并，不是本轮新卡，不重推

## 必须核验的库内刷新

### 2hour.fun @2hourfun

- 官方第一场窗口仍是 **2026-11-26 05:00 CST（21:00–23:00 UTC）**
- MUST 24h 见 03:23 CST 官帖（https://x.com/2hourfun/status/2125671754467049856）How to be ready for 21:00 UTC，以及 03:24 / 03:29 CST 短帖，确认仍按 21:00 UTC，不是改期/取消
- 官网 https://www.2hour.fun/ HTTPS 200；文案仍是 Trading never stops / New coins launch only in the daily 2-hour window；可见 “No coins on the curve right now. Come back when the window opens” 与 Window open 00:00:00
- `/api/window` 仍返回 `{"perCoin":{},"traders":[]}`，窗口尚未打开
- R2206 已发首次 ≤2h。时间表未改且尚未开窗 → **不重推**

### Shielded Wizards @ShieldedWizBTC

- 权威数据来自 `https://brimhollow.app/launchpad/api/status`（本轮 200），不要用静态 launch-schedule.js
- 本轮：phase=wl（仍未开公售），minted=32/3333（与 R2206 持平），reserved=0，mintOpen=true，price=0（Free），fee=4000
- **改期**：Public startsAt 由 R2206 的 `2026-11-25T21:10:26.113Z`（2026-11-26 05:10:26 CST）改为 `2026-11-25T21:00:00.000Z`（**2026-11-26 05:00:00 CST**），提前约 10 分钟。WL startsAt 未变
- MUST 24h 未见 @ShieldedWizBTC 新官帖（MUST_WIN 25 条触顶未翻页，以官网 API 为准）
- WL 免费铸仍 LIVE（R2165 已提醒），不因仍 LIVE 或 minted 进度重推
- R2206 已就原 05:10:26 CST 发过公售首次 ≤2h。本轮因**改期**须通知，不是重复的首次 ≤2h 告警。公售尚未打开

### Guns Of The Hood @GunsOfTheHood

- 官网 /drop 仍写 25 November 22:00 Amsterdam time（21:00 UTC = **2026-11-26 05:00 CST**），价格仍 0.00003 ETH + gas，单钱包终身 10，10,000 份，Robinhood Chain，开交易前转让锁定
- OpenSea 合集 guns-of-the-hood：twitterUsername=GunsOfTheHood，合约 0x1d3f3b153533bde7912da634b38ab50b3b90456d；SeaDrop mintStatus=**MINTING_SOON**，0/10000，activeDropStage 空；PUBLIC_SALE 仍 2026-11-26 05:00 CST 起。持有 0，无地板
- 时间表未改，仍未开铸。R2206 已发付费公售首次 ≤2h → **不重推**。不是免费 mint

### 其它库内（无实质变化，不重推）

- **Ugly Puggies @uglypuggies**：仍 MINTING 263/777，持有 193（R2206 为 194），地板 0.000169 ETH；active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST；stageIndex 3 仍 SIGNED_PRESALE 至 2026-11-27 13:30 CST；PUBLIC_SALE 仍 2026-11-27 13:30 CST。R2198 已通知免费 mint LIVE
- **deMiners @deMinersNft**：仍 PUBLIC_SALE MINTING 572/3333，持有 153，地板 0.0001 ETH；价仍按已核验 0.0002 ETH，至 2026-11-28 00:30:04 CST。R2197/R2201 已提醒
- **The Jacket @TheJacket_NVDA**：仍 MINTING 213/777，持有 135，地板 0.61 USDG，active 仍 PUBLIC_SALE
- **Agent Cards @agentcardshq**：官网 /api/mint/status 仍 phase=open，fillSold=5000/5000，curveSold=427，sold=5427/1,007,493，现价约 0.00198 BNB；池内约 3.781 BNB（R2206 约 4.023，属回购后续波动）。MUST 见 02:55 CST 回购续帖。不是免费 mint。R2200 已通知开铸
- **Slime @Slime_agents**：SeaDrop 仍 MINTING_SOON、0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE
- **Vicehood @Vicehood_RH**（官方合集 vchood，勿与 vicehood / PlayVicehood 混淆）：仍 MINTING_SOON 0/3333；SIGNED_PRESALE 2026-11-27 01:00–04:00 CST，另有一段 04:00–05:00 CST SIGNED_PRESALE，PUBLIC_SALE 自 2026-11-27 05:00 CST。距首窗约 21.5 小时，未到首次 ≤2h，不提前告警
- **Wildlife Universe / Tiger Universe @Wildlifeuni_55**：仍 MINTING_SOON 0/5555；SIGNED_PRESALE 自 2026-11-26 21:30 CST。距首窗约 18 小时，未到首次 ≤2h，不提前告警
- **YORI @yoricolors / BAD APE @artnesh / Helium @launchhelium**：本轮站点/合集无实质变化，不是已确认免费 mint LIVE，不重推
- **TRIFORGE**：链上 NFT 756/3333（R2206 为 754），claims 31，预售/挖矿规则未变；MUST 再见已记过的 01:32 CST 官帖，不重推
- **F0B90B**：链上 mintOpen=True，426/10000（R2206 为 419），小幅进度，不重推
- **Antopia**：saleOpen=True，仍 6253/8888，免费额度已满，不重推
- **VALORIX**：Hero Cards 仍 15，fillSold 仍 0/5500，不重推
- **Fueltender / AGX**：官网仍可访问 / 维护页口径与上轮一致，未见新开铸，不重推

## notify 判定

- **notify=true**
- 原因：新收录 Bonebloom（自称 111 免费额度，不是已开铸 LIVE，须点名）；Shielded Wizards 公售改期 05:10:26 CST → 05:00:00 CST（须通知）。2hour.fun / Guns Of The Hood 时间表未改且尚未开窗/开铸，R2206 已发首次 ≤2h，不重推
- alert：`R2207｜新收录 Bonebloom：自称 555 份 ETH PFP，其中 111 免费、444 公售 0.011 ETH，目前状态为 MINTING_SOON，0/555，尚未开铸，并非 LIVE；Shielded Wizards 公售改期提前约 10 分钟，至 2026-11-26 05:00 CST，当前仍为 WL 阶段；详情见 https://reboot7454.github.io/early-scout/ 。本号不自动 mint。`
- namedFreeMintOrRegistration：Bonebloom @AbyssLabsNFTCol（自称 111 免费额度，不是已开铸 LIVE）
- namedPaidLe2h：无（三个原 ≤2h 项目中，仅 Wizards 因改期通知，不是新的首次 ≤2h）
- namedMintConfirm：无
- dsFallback=false（admit / score / alert 均走 DeepSeek flash，思考开启）
- 本号不自动 mint


## Discord Peek

- discordPeekDeferred=true
- 本轮未再开 computerUse。R2206 已于 2026-11-26 03:02:24 CST 停在 Discord 登录墙（Welcome back / Email or Phone Number / Password / Log In / Register / QR / passkey），loginOk=false，channelsPeeked=false，cardsRead=0。四频道 cutoff 仍为：#alpha-1 after 2026-11-23 22:19 CST；#alpha-1-backup after 22:29 CST；#smart-accounts-tracker after 22:56 CST；#alpha-3-new-accounts after 22:55 CST。积压仍未清。
- 用户已在 R2206 被告知用已有表单在盒子 Chrome 再登。同一未登录会话无法翻过登录墙，本轮不重复开浏览器、不向用户重发登录表单。

## 交付

- `/tmp/r2207/RESULT_R2207.md`
- `/tmp/r2207/notify.json`
- `/tmp/r2207/data.json`（APPLY_DRY_RUN=1 生成）
- `/tmp/r2207/apply_r2207.py`
- `/tmp/r2207/x_usage.json`（remainingBefore=76，remainingAfter=63，xReads=13=12+1，mode=tight）
