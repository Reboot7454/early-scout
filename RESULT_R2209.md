# 早期打新雷达 R2209 RESULT

工作目录 `/tmp/r2209/`。本路只做 X 雷达、站点/链上核验、DeepSeek、dry-run 写盘与 RESULT。未 git commit/push，未改 `/workspace/early-scout/data.json`，未打开 Discord/浏览器。`discordPeekDeferred=true`（占位，待父进程合并）。

开跑约 2026-11-26 04:37 CST。dry-run `lastScout=2026-11-26 04:49:41 CST`。本轮是常规增量，`lastFullAfterReset` 保持 **R2170**。时区 Asia/Shanghai (CST)。`dsFallback=false`。关键站点/API 核验约 **04:43 CST**，当时仍早于三个 05:00 CST 窗口。

## 额度与模式

- 开火前预期 remainingBefore=51（R2208 RESULT 直播脚注 remainingAfter）。首搜 UF1 脚注「今日剩余 50 / 1000」，按搜索后剩余 +1 计，**live remainingBefore=51**，与预期一致，落在 tight ±20 内。
- `mode=tight`，softCap=10，minSpend=10，silentCap=1。未 override-full，未补 MUST_OFF（live 远低于 ≥250 门槛）。
- 已排 12 次全部跑完（main 11 + silent 1），未再加计划外搜索。
- **xReads=12**（main=11，silent=1），**remainingBefore=51**，**remainingAfter=39**（末次 SILENT_BTC 脚注今日剩余 39）。
- 今日硬顶重置约 08:00 CST（脚注 `todayReset=2026-11-26T00:00:00.000Z`）。距重置约 6 轮，本轮未把额度打到 0。
- 写盘 `meta.xBudgetMode=tight`。

各次脚注（result_count / remainingToday）：
UF1 5/50，UF2 0/49，MUST_WIN 25/48（触顶有 next_token，未翻页），KW_LZ 0/47，KW_TAPE 6/46，KW_GIWA 25/45，KW_DOGE 5/44，KW_BTC 2/43，KW_STARK 4/42，KW_CORE 25/41，MEN_LZ_ELY 25/40，SILENT_BTC 13/39。全部 error=None。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- **十栏跑全**：六薄栏独立 30m KW 均跑到；核心栏+GAPS 合并为一次 KW_CORE（30m，25 触顶未改 24h）。MUST_WIN 24h 1 次；MUST_OFF 延期。
- **UF 刷完（本轮 wrap=true）**：分片 cursor 2421 `@tailtradesxyz` 起，先刷到名单末尾 `@launchonvybe`，再从头 `@banipool` 到 `@TapeLaunch`（共 40 个）。LIVE/临近窗口号 `@GunsOfTheHood @Agx_bsc` 已从 UF 30m 挪到 MUST_WIN 24h，另预跳 9 个已知 NF，故 from: 实际 **29** 个（UF1 24 + UF2 5）。UF1 5 帖（`@launchhelium` / `@launchonvybe`）、UF2 0 帖，无新官号开窗。写盘后 **ufCursor=27 `@Naru_giwa`**，uf_total=2434（本轮无新挂号，cursor 指向不变）。
- **mentions**：本轮子集 MEN_LZ_ELY（24h，1 条合并查询覆盖 LayerZero-24h + Elysium-rest 官号/挂靠），25 条触顶未翻页。**下轮 mentionsNext：DogeEVM / BTC / Starknet / squeek / STARX。**
- **静号**：SILENT_BTC（2209 % 11 = 9，BTC），`search_users` 仍不可用，用 mentionQuery 兜底。13 帖。送审 3 个均 skip，无新收录。**下轮静号：Starknet。**
- **未做薄栏 24h。** 独立薄栏 30m：LZ=0、BTC=2、STARK=4 均 <5；TAPE=6、GIWA=25、DOGE=5 已 ≥5。按规则最多再搜 2 条 24h，且前提是主计划后 remainingToday 仍大致 ≥150；本轮 12 次后 remainingToday=39，远低于门槛，故默认不做。禁止把 KW_CORE 改成 24h。

## 新收录

**无。** DeepSeek admit（deepseek-flash，思考开启）送审 3 个均 skip，`dsFallback=false`。

## 看见但未收

- **@theinscriboors**（约 11.47 天，169 粉，http://inscriboors.com）：SILENT_BTC 仅见 `@Larpcheckbot` 点评 `$INSCRIBOOR`（TOTAL 53/100，称 Ordinals draws are real、mining prize not live yet、insiders 9%）。已有代币的 Ordinals 抽签/奖池，不是免费 mint / 免费登记；本轮未直接拉到该号原创帖。DS skip。
- **@zayrotrade**（约 7.47 天，955 粉，https://zayro.trade）：KW_GIWA 仅见被列入 GIWA 生态观察名单。简介是 1000x 杠杆交易，不是打新/免费 mint。DS skip。
- **@famulusai**（约 7.16 天，20 粉，http://famulusai.app）：仅被回复提及，简介只有一个 0x 地址，本轮无发射/mint 证据。DS skip。
- **@WorldsEndFarm**：KW_STARK 命中 “bramble” 的农场日常帖，误伤，不收。
- **Puffins `@PuffinRH`**：已在库（R 更早，watching，自称 Robinhood 免费 mint 555）。本轮只见到推广号 RT「Introducing PuffinsRH / Free mint 555 / Drop your EVM wallet」，未做额外 from: 重读，不是本轮新卡，也未核到已开铸 LIVE，不重推。
- **GAMA / gamatiles**：已在库（`@gamapadcom` / `@gama_giwa`）。本轮见 GIWA 测试网体验转述，不是新卡。
- 其它提及（MMIX Districts、Plunder Port Genesis Captains、Vicehood 登记、JPEGZart、hoojafun、Lamoryant 等）均为已在库项目的转载/登记帖，不重复收录。

## 关键刷新（三个 05:00 CST 窗口，核验约 04:43 CST）

- **2hour.fun `@2hourfun`**：官方第一场窗口仍是 **2026-11-26 05:00 CST（21:00–23:00 UTC）**。MUST 24h 再见 04:01 CST 官帖（https://x.com/2hourfun/status/2125681213071368656）写 “1 hour / The first 2hourfun window opens at 21:00 UTC”，另有 03:23 CST 就绪指南，未见改期/取消。官网 https://www.2hour.fun/ HTTPS 200，文案仍是 New coins launch only in the daily 2-hour window，并写 “No coins on the curve right now. Come back when the window opens”；静态页可见 Window open 00:00:00（未跑客户端计时，不作已开窗证据）。`/api/window` 返回空 `perCoin/traders`。**窗口尚未打开。** R2206 已发首次 ≤2h，时间表相对 R2208 未变，不重推。
- **Shielded Wizards `@ShieldedWizBTC`**：权威 `https://brimhollow.app/launchpad/api/status` 仍 `phase=wl`，minted=**32/3333**（与 R2208 持平），`mintOpen=true`。Public `startsAt` 仍是 `2026-11-25T21:00:00.000Z` = **2026-11-26 05:00:00 CST**，price=0（仍 Free），fee=4000。**尚未开公售。** 本轮 MUST 24h 未见该号新官帖（25 条触顶，最旧约 01:30 CST，`fueltenderagent` 占 13 条，未翻页；以官网 API 为准）。WL 免费铸仍 LIVE（R2165 已提醒），不因仍 LIVE 或 minted 进度重推。R2207 已就改期通知，时间表相对 R2208 未再改，不重推。
- **Guns Of The Hood `@GunsOfTheHood`**：MUST 24h 见 04:00 CST 官帖（https://x.com/GunsOfTheHood/status/2125680927250473179）写 “1 HOUR LEFT”，公售仍按 22:00 CET · 4 PM ET · 1 PM PT（即 **2026-11-26 05:00 CST**），10,000 sealed crates，No whitelist，官帖写 “0,05$ in $ETH + gas”、max 10/钱包（与 0.00003 ETH 同口径，不是改价）。官网 https://www.gunsofthehood.xyz/drop 写 OpenSea mint scheduled for 25 November at 22:00 Amsterdam time (21:00 UTC)，Mint price **0.00003 ETH + gas**，Wallet limit 10，并写 “Wallet sign-in opens when the collection launches.” OpenSea 合集 HTML SeaDrop 仍 **MINTING_SOON**，erc721 **0/10000**，PUBLIC_SALE `startTime=2026-11-25T21:00:00.000Z`，合约仍是 `0x1d3f3b153533bde7912da634b38ab50b3b90456d`。stats API 本轮 401，供应以合集 HTML / collection API 为准。**尚未开铸。** R2206 已发付费公售首次 ≤2h，时间表/价格未变，不重推。

## 库内其它刷新（无实质变化，不重推）

- **Ugly Puggies**：仍 MINTING，**274/777**（R2208 为 273），持有 204，地板 0.000169 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST；stageIndex 3 仍至 2026-11-27 13:30 CST；PUBLIC_SALE 仍 2026-11-27 13:30 CST 起。
- **deMiners**：仍 MINTING **575/3333**（与 R2208 持平），持有 153，地板约 0.0001 ETH。PUBLIC_SALE 仍至 2026-11-28 00:30:04 CST。只是进度/持平，未见改价/改期。
- **The Jacket**：仍 MINTING **214/777**（R2208 为 213），持有 136，地板 0.61 USDG，active 仍 PUBLIC_SALE。
- **Agent Cards**：官网 `/api/mint/status` 仍 phase=open，fillSold=5000/5000，curveSold=427，sold=**5427**/1,007,493，现价约 0.00198 BNB。与 R2208 持平。
- **TRIFORGE**：链上 Forge Keys **760/3333**（R2208 为 757），claims 31，预售仍开至 2026-12-02，挖矿仍开。MUST 再见已记过的 01:32 CST 官帖，规则未变。
- **F0B90B**：链上 **427/10000**（R2208 为 426），mintOpen=True。小幅进度。
- **Antopia**：链上仍 **6253/8888**，saleOpen=True，免费额度仍满。无新官帖。
- **VALORIX**：链上 Hero Cards 仍 15，fillSold=0/5500。MUST 见 02:58 CST 在 @moltbook 领取 AI agent 的帖，与铸造规则无关。
- **Fueltender**：MUST 见 13 条安全头/bundler 技术帖，官网仍可访问，无新铸造窗口。
- **Helium**：UF 见 04:12 CST「we will be pushing this all day」及回复，官网 heliumpad.com 仍可访问，不是免费 mint。
- **VYBE**：UF 再见产品向官帖（04:09 / 04:15 / 04:23 CST），CA 仍是 `ks3h9hxbqSjz2ymvMGCPC4uJ991LxXaQBZEivv2vybe`，不是免费 mint。R2208 已通知，不重推。
- **Bonebloom**：SeaDrop 仍 MINTING_SOON **0/555**，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，PUBLIC_SALE 仍 2026-11-28 02:30 CST。未到首次 ≤2h。
- **Slime**：SeaDrop 仍 MINTING_SOON 0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- **BAD APE**：OpenSea 供应仍为 0，未见开铸 LIVE。
- **Vicehood `@Vicehood_RH`（官集合集 vchood）**：SeaDrop MINTING_SOON 0/3333，SIGNED_PRESALE 仍 2026-11-27 01:00–04:00 CST，另有 stageIndex 2 至 05:00 CST，PUBLIC_SALE 自 2026-11-27 05:00 CST。距首窗约 21 小时，未到首次 ≤2h，不提前告警。同名合集 `vicehood`（非该官号，已在铸 209/3333）未与官号混淆。
- **Wildlife Universe / Tiger Universe**：SeaDrop MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 **2026-11-26 21:30 CST** 起。距首窗约 17 小时，未到首次 ≤2h，不提前告警。
- **AGX**：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」，合约仍未确认开铸。
- Canton/Glaze/TokenWorks：本轮无新 admit，仅刷 lastChecked。

MUST_WIN 限制：24h 查询 25 条触顶未翻页，最旧约 01:30 CST；作者分布 `fueltenderagent` 13、`2hourfun` 5、`GunsOfTheHood` 5、`TriForgeAgent` 1、`VALORIXBNB` 1。`@uglypuggies @deMinersNft @agentcardshq @ShieldedWizBTC @TheJacket_NVDA @F0B90Bclub @antopia_xyz @Agx_bsc` 未出现在这 25 条里，相应状态以官网 / OpenSea / RPC 为准，未做额外 X 重读。

## notify 判定

**notify=false。**

- 原因：本轮无新收录。2hour.fun / Shielded Wizards / Guns Of The Hood 相对 R2208 时间表未变，约 04:43 CST 核验时仍早于 05:00 CST，且均尚未开窗/开铸。R2206 已发首次 ≤2h，R2207 已就 Shielded Wizards 改期再通知，不因仍在 ≤2h 窗口内重推。库内其它 LIVE/进度项无改期、改价、取消或新的开铸确认。
- `namedFreeMintOrRegistration=[]`，`namedPaidLe2h=[]`，`namedMintConfirm=[]`，`namedScheduleChange=[]`，`newCards=[]`。
- 无需 alert。本号不自动 mint。
- `dsFallback=false`。

## 交付

- `/tmp/r2209/RESULT_R2209.md`（本文件）
- `/tmp/r2209/notify.json`
- `/tmp/r2209/data.json`（APPLY_DRY_RUN=1，源 `/tmp/r2209/data.json.src`）
- `/tmp/r2209/apply_r2209.py`
- `/tmp/r2209/x_usage.json`

写盘核对：`meta.newThisRound == 顶层 newThisRound == round2209Added == []`；上一轮 newThisRound 已清；ufCursor=27 @Naru_giwa（wrap=true）；xBudgetMode=tight；discordPeekDeferred 占位已留。`/workspace/early-scout/data.json` 未被本路修改。

生成时间 2026-11-26 04:50:20 CST。
