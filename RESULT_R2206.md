# 早期打新雷达 RESULT R2206

- 时间：2026-11-26 约 03:00–03:15 CST（Asia/Shanghai）
- 模式：tight（softCap=10，minSpend=10，silentCap=1）
- lastScout（已写盘）：2026-11-26 03:18:07 CST
- lastFullAfterReset：R2170（本轮是常规增量，不是 08:00 CST 后首轮全量补扫）
- 面板：https://reboot7454.github.io/early-scout/
- 本路径只做 X 雷达 / 站点与链上核验 / DeepSeek / dry-run 写盘；未 git commit/push，未改 `/workspace/early-scout/data.json`

## X 额度与搜索

- 首搜脚注：UF1 结束后 remainingToday=88、remainingMinute=29；remainingBefore = 88+1 = **89**（与开火前预期完全一致，±20 内，保持已排 13 次，未加计划外搜索，也未改 near-exhausted）
- remainingAfter（末次 SILENT_TAPE 脚注）= **76**
- xReads = **13**（main 12 + silent 1）
- meta.xBudgetMode = tight
- MUST_OFF 本轮 tight 跳过（官号 30m 延期）；live remainingBefore=89 未到 ≥250 补跑阈值
- 有 next_token 的查询均未翻页
- 未对 @starx_xlayer 做 from: 重试，未对同一 handle 重复读取

| id | 窗口 | result_count | remToday（该次后） |
|---|---|---:|---:|
| UF1 | 30m | 3 | 88 |
| UF2 | 30m | 5 | 87 |
| MUST_WIN | 24h | 25（触顶未翻页） | 86 |
| KW_LZ | 30m | 0 | 85 |
| KW_TAPE | 30m | 7 | 84 |
| KW_GIWA | 30m | 25（触顶未翻页） | 83 |
| KW_DOGE | 30m | 7 | 82 |
| KW_BTC | 30m | 4 | 81 |
| KW_STARK | 30m | 1 | 80 |
| KW_CORE | 30m | 25（触顶未翻页） | 79 |
| MEN_STARK | 24h | 0 | 78 |
| MEN_SQUEEK | 24h | 0 | 77 |
| SILENT_TAPE | 24h | 1 | 76 |

十栏：独立薄栏 6 条 30m KW 全跑；核心栏+GAPS 合并为一次 KW_CORE。UF 分片刷完。

### 薄栏 24h

未做。TAPE 30m=7、GIWA=25、DOGE=7 已 ≥5，不改 24h；LZ=0、BTC=4、STARK=1 虽 <5，但主计划 13 次后 remainingToday=76，远低于约 150 的补搜门槛。最多 2 次 24h 补搜的额度本轮不用。

## UF

- 本轮分片 cursor 2301 @antebellrh 起，至 @LYNXOPIA（名单 40 个，其中 @ShieldedWizBTC 在 2339，已从 UF 30m 挪到 MUST_WIN 24h，故 from: 实际 39 个：UF1 24 + UF2 15），wrap=false
- UF1 3 帖、UF2 5 帖：@memoriaagent 产品更新；@hagitrade 称 Ghost Addresses are live；@AntNestWars 红包/分解/合成更新；@FionaHippoBNB 称 raise 近 48 BNB / 214 agents。均为已在库号，不是新的免费 mint/登记窗口，不新建卡、不重推
- 写盘后 ufCursor=**2341 @MintuBots**，uf_total=**2432**（新收录 @GunsOfTheHood 追加在名单末尾，cursor 指向不变）

## Mentions / 静号

- 本轮覆盖：Starknet（MEN_STARK 0）、squeek（MEN_SQUEEK 0）
- mentionsNext：STARX（先补完本轮轮转剩余，再回到 pads-rest / GIWA / Tape / LayerZero-24h / Elysium-rest）
- 静号：Tape/电路，mentionQuery 兜底（search_users 仍不可用），SILENT_TAPE 1 条，未见可核验新官号窗口
- silentNext：GIWA

## 新收录

### Guns Of The Hood（@GunsOfTheHood / https://gunsofthehood.xyz/）

- 来源：KW_CORE 30m 官帖 2026-11-26 03:02 CST（https://x.com/GunsOfTheHood/status/2125666328728231990）
- 建号 2026-11-17 17:39:13 CST（约 8.39 天），13 粉 / 9 帖，资料栏仅 Discord；库内原先无此卡
- 官帖自称 10,000 sealed weapon crates，Robinhood Chain，OpenSea 公售，无 GTD/白名单；Nov 25 22:00 CET（= 21:00 UTC = 2026-11-26 05:00 CST）；约 $0.05 + gas，单钱包 10 份
- 官网 HTTPS 200（跳转 www.gunsofthehood.xyz）。/drop 页写明：OpenSea mint scheduled for 25 November at 22:00 Amsterdam time (21:00 UTC)；Mint price 0.00003 ETH + gas；Wallet limit 10 lifetime；supply 10,000；Robinhood Chain；开交易前转让与转售锁定；并链到同一 OpenSea 合集。页上仍写 Wallet sign-in opens when the collection launches
- OpenSea 合集 guns-of-the-hood：twitterUsername=GunsOfTheHood，externalUrl=https://gunsofthehood.xyz，chain=robinhood，合约 0x1d3f3b153533bde7912da634b38ab50b3b90456d（合集 createdAt=2026-11-26 00:29:59 CST）
- SeaDrop（合集 HTML 转义 JSON）：mintStatus=**MINTING_SOON**，0/10000，activeDropStage=null；仅一段 PUBLIC_SALE 2026-11-25T21:00:00.000Z（2026-11-26 05:00:00 CST）至 2027-11-25T20:00:00.000Z
- 公开 stats：持有 0，成交 0，无地板
- **不是免费 mint，不是已开铸 LIVE**。付费公售本轮首次进入 ≤2h
- DeepSeek admit=true，overall=62（early 88 / actionable 76 / novelty 52 / risk 80），focus=false
- 已挂 userFollowWatch + freeMintWatch（名单末尾）。dsFallback=false

## 看见但未收

- @asdascasdauf：0 粉新号，只是跟 @LawoftheAbyss（已在库）free mint 口令，不是新项目官号
- @CadaCasoxLayer：7.8 天、2 粉，向 TapeOut 团队询问示例仓库/测试网，不是 mint/launch 窗口
- @2hourfunEco：2hour.fun 生态号，官网指向已在库项目，不新建卡
- GIWAPUNK @giwapunk：R2204 已筛过 admit=false（overall=44），本轮未见主网上线或开铸证据，不重收
- KW_CORE / KW_GIWA 大量抽奖转发与旧号讨论（Vicehood / Ugly Puggies GTD、Law of the Abyss 等），对应项目已在库或没有可核验的新官号窗口
- ONE LaunchPad @one_launchpad：用户点名已在 R2205 面板合并，不是本轮新卡，不重推

## 必须核验的库内刷新

### 2hour.fun @2hourfun — 首窗仍是 05:00 CST，本轮首次 ≤2h，必须通知

- 官方第一场窗口仍是 **2026-11-26 05:00 CST（21:00–23:00 UTC）**。MUST 24h 最新实质官帖仍是 01:09:03 CST（https://x.com/2hourfun/status/2125637903741063614）：倒计时 4 hours，Opening Night 21:00–23:00 UTC 交易、Premiere 窗口内发射。01:13 / 01:31 CST 短回复不是改期或取消
- 官网 https://www.2hour.fun/ HTTPS 200，文案仍是每日 2 小时窗口；可见 “No coins on the curve right now. Come back when the window opens”；`/api/window` 返回空 `perCoin` / `traders`，窗口尚未打开。未见改期/取消证据
- R2205 lastScout 02:48:50 CST 距窗约 2.2 小时，当时未告警。本轮开跑已约 03:00 CST，属**付费发射窗首次 ≤2h**（不是新的免费 mint LIVE）

### Shielded Wizards @ShieldedWizBTC — 公售 05:10:26 CST，本轮首次 ≤2h，必须通知

- 官网 https://brimhollow.app/mint 可访问（SPA）。权威数据来自 `https://brimhollow.app/launchpad/api/status`（本轮 200）：
  - phase 仍为 **wl**，minted=**32**/3333（此前有记录的核验为 8/3333），reserved=0，mintOpen=true
  - Public startsAt=**2026-11-25T21:10:26.113Z** = **2026-11-26 05:10:26 CST**
  - 公售 price=0（仍 Free），fee=4000；另有 1,000 sats ticket 口径
- 静态 `launch-schedule.js` 里有一份更早的 19:00 UTC 默认表，**不以它为准**，以 live API 为准
- MUST 24h 合查 25 条触顶，未见 @ShieldedWizBTC 新官帖；未再做 from: 重读。未见改期或取消
- WL 免费铸仍 LIVE（R2165 已提醒），不因仍 LIVE 或 minted 8→32 重推
- R2205 约 02:48 CST 距 05:10 仍大于 2 小时，当时未告警。本轮开跑后距 05:10:26 CST **首次进入公售 ≤2h**（不是新的免费 mint LIVE）

### 只刷新、不重推

- **Ugly Puggies**：仍 MINTING 263/777（R2205 为 260；公开 API 亦 263），持有 194（R2205 为 195），地板 0.000169 ETH。activeDropStage 仍 stageIndex=2 SIGNED_PRESALE，至 2026-11-26 13:30 CST；stageIndex 3 仍是 SIGNED_PRESALE 至 2026-11-27 13:30 CST；PUBLIC_SALE 仍要到 2026-11-27 13:30 CST。阶段未变，只是小幅进度
- **deMiners**：付费公售仍按 2026-11-26 00:30:04 CST 开出，至 2026-11-28 00:30:04 CST。SeaDrop 仍 MINTING 572/3333（与 R2205 持平），持有 153（R2205 为 152），二级地板 0.0001 ETH。铸造价沿用已核验 0.0002 ETH，本轮 SeaDrop JSON 仍无价格字段，未见改价/改期/取消。MUST 仅见已记过的 01:14 CST 短回复
- **Agent Cards**：`/api/mint/status` phase=open，opened=true，ended=false，fillSold=5000/5000，curveSold=427，sold=5427/1,007,493（与 R2205 持平），现价仍约 0.00198 BNB（约 $1.09）。池内约 4.023 BNB（R2205 约 3.773）。MUST 见 00:07 / 00:38 / 02:55 CST 回购销毁续帖，属已通知开铸后的纠偏，不是新的铸造规则/价格窗口。不是免费 mint
- **The Jacket**：仍 MINTING 213/777（与 R2205 持平），持有 135，地板 0.61 USDG，active 仍 PUBLIC_SALE。MUST 未见新官帖
- **Slime**：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍 2026-11-29 00:00 CST 起，PUBLIC_SALE 仍 2026-11-30 01:00 CST 起，不是已开铸 LIVE
- **YORI**：官网 200，标题仍是 YORI | More Than Colors，未见开铸，日期仍 TBA。R2205 已通知，不重推
- **BAD APE / Helium**：Helium 官网 200，仍是 Solana private payout launchpad 文案，不是免费 mint/登记。二者此前已收录通知，无实质变化
- **ONE LaunchPad**：用户点名已在 R2205 合并，不是本轮新卡
- **Vicehood @Vicehood_RH**：官方合集仍是 vchood（勿与已在铸的 vicehood / PlayVicehood 混淆）。SeaDrop 仍 MINTING_SOON 0/3333；SIGNED_PRESALE 2026-11-27 01:00–04:00 CST，PUBLIC_SALE 2026-11-27 05:00 CST 起。距首窗约 22 小时，未到首次 ≤2h，不提前告警
- **Wildlife Universe / Tiger Universe**：SeaDrop 仍 MINTING_SOON 0/5555；SIGNED_PRESALE 自 2026-11-26 21:30 CST 起，PUBLIC_SALE 2026-11-27 02:29 CST 起。距首窗约 18 小时，未到首次 ≤2h，不提前告警
- **Fueltender**：官网 fueltender.agency 仍可访问，MUST 未见新官帖
- **F0B90B**：链上 mintOpen=True，419/10000（R2205 为 418），小幅进度
- **Antopia**：saleOpen=True，6253/8888 与 R2205 持平，freeRemaining=0
- **VALORIX**：Hero Cards totalMinted=15（R2205 面板记 12），fillSold 仍 0/5500，MUST 未见新官帖，小幅进度不重推
- **TRIFORGE**：Forge Keys 754/3333（R2205 为 750），未暂停；付费预售仍开（lpTotalMinted=1）；claims 31（R2205 亦为 31）；挖矿 shares=6。01:32 CST 官帖已在 R2205 记过
- **AGX**：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」；三份地址仍有 bytecode，未确认开铸

Canton / Glaze / TokenWorks watch 仅 soft-touch lastChecked，本轮无新 admit。

## notify 判定

- **notify=true**
- 原因：新收录 Guns Of The Hood（付费公售首次 ≤2h，不是免费 mint LIVE）；2hour.fun 与 Shielded Wizards 时间表未改期/取消，本轮开跑后首次进入首窗/公售 ≤2h，须逐个点名
- namedFreeMintOrRegistration：[]
- namedPaidLe2h：2hour.fun @2hourfun、Shielded Wizards @ShieldedWizBTC、Guns Of The Hood @GunsOfTheHood
- namedMintConfirm：[]
- 告警由 DeepSeek 撰写，已点名上述三项，并含面板链接与「本号不自动 mint」
- dsFallback=false
- 本号不自动 mint

## Discord Peek

- discordPeekDeferred=true（已合并 /tmp/r2206/discord_peek.json）
- 父进程 computerUse 于 2026-11-26 03:02:24 CST 打开盒子 Chrome，从 #alpha-1（https://discord.com/channels/1502958818865188956/1527862926885785710）起步，随即停在 Discord 登录墙。
- landed/current URL：https://discord.com/login?redirect_to=%2Flogin%3Fredirect_to%3D%252Fchannels%252F1502958818865188956%252F1537897411668746302 （redirect_to 指向 #alpha-3-new-accounts，可能是旧会话残留）
- pageTitle：Discord。visibleText：Welcome back! / Email or Phone Number / Password / Log In / Register / QR Code / passkey。
- loginOk=false，loginWall=true，channelsPeeked=false，cardsRead=0，items=[]，lastSeen/cutoffs 未推进。未填凭据、未点 Log In、未扫码、未用 passkey、未点 Register、未进服、未发消息。
- 四频道 cutoff 仍为：#alpha-1 after 2026-11-23 22:19 CST；#alpha-1-backup after 22:29 CST；#smart-accounts-tracker after 22:56 CST；#alpha-3-new-accounts after 22:55 CST。积压仍未清。
- 同一登录墙已连续多轮出现，需用户在盒子 Chrome 登录 Discord 后才能补 Peek，父代理单独再开未登录会话无法翻过登录墙。

## 交付

- `/tmp/r2206/RESULT_R2206.md`
- `/tmp/r2206/notify.json`
- `/tmp/r2206/data.json`（APPLY_DRY_RUN=1，源为 data.json.src）
- `/tmp/r2206/apply_r2206.py`
- `/tmp/r2206/x_usage.json`
- `/tmp/r2206/new_cards.json`
