# 早期打新雷达 R2208 RESULT

工作目录 `/tmp/r2208/`。本路只做 X 雷达、站点/链上核验、DeepSeek、dry-run 写盘与 RESULT。未 git commit/push，未改 `/workspace/early-scout/data.json`，未打开 Discord/浏览器。`discordPeekDeferred=true`（占位，待父进程合并）。

开跑约 2026-11-26 04:09 CST。dry-run `lastScout=2026-11-26 04:22:37 CST`。本轮是常规增量，`lastFullAfterReset` 保持 **R2170**。时区 Asia/Shanghai (CST)。`dsFallback=false`。

## 额度与模式

- 开火前预期 remainingBefore=63（R2207 RESULT 直播脚注）。首搜 UF1 脚注「今日剩余 62 / 1000」，按搜索后剩余 +1 计，**live remainingBefore=63**，落在 tight 预期 ±20 内。
- `mode=tight`，softCap=10，minSpend=10，silentCap=1。未 override-full，未补 MUST_OFF（live 远低于 ≥250 门槛）。
- 已排 12 次全部跑完（main 11 + silent 1），未再加计划外搜索。
- **xReads=12**（main=11，silent=1），**remainingBefore=63**，**remainingAfter=51**（末次 SILENT_DOGE 脚注今日剩余 51）。
- 今日硬顶重置约 08:00 CST（脚注 `todayReset=2026-11-26T00:00:00.000Z`）。距重置约 7 轮，本轮未把额度打到 0。
- 写盘 `meta.xBudgetMode=tight`。

各次脚注（result_count / remainingToday）：
UF1 3/62，UF2 1/61，MUST_WIN 25/60（触顶有 next_token，未翻页），KW_LZ 0/59，KW_TAPE 3/58，KW_GIWA 25/57，KW_DOGE 14/56，KW_BTC 1/55，KW_STARK 3/54，KW_CORE 25/53，MEN_GIWA_TAPE 25/52，SILENT_DOGE 1/51。全部 error=None。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- **十栏跑全**：六薄栏独立 30m KW 均跑到；核心栏+GAPS 合并为一次 KW_CORE（30m，25 触顶未改 24h）。MUST_WIN 24h 1 次；MUST_OFF 延期。
- **UF 刷完**：分片 cursor 2381 `@NoPvPfun` 起 40 个到 `@AcruxComputer`，LIVE/临近窗口号 `@deMinersNft @F0B90Bclub @VALORIXBNB @antopia_xyz @fueltenderagent` 已从 UF 30m 挪到 MUST_WIN 24h，故 from: 实际 **35** 个（UF1 + UF2）。wrap=false。UF1 3 帖、UF2 1 帖，无新官号开窗。写盘后 **ufCursor=2421 `@tailtradesxyz`**，uf_total=2434（新收录 `@launchonvybe` 追加在名单末尾，cursor 指向不变）。
- **mentions**：本轮子集 MEN_GIWA_TAPE（24h，1 条合并查询覆盖 GIWA + Tape 官号/挂靠，含 MUST_OFF 未跑到的 `@GIWA_by_Upbit @TapeAIAgent @Blonskr`），25 条触顶未翻页。**下轮 mentionsNext：LayerZero-24h / Elysium-rest。**
- **静号**：SILENT_DOGE（2208 % 11 = 8，DogeEVM），`search_users` 仍不可用，用 mentionQuery 兜底。1 帖：`@fizalasdair` 提及 `@DogeOS` 测试网任务，不是新免费 mint，未送审。**下轮静号：BTC。**
- **未做薄栏 24h。** 独立薄栏 30m：LZ=0、TAPE=3、BTC=1、STARK=3 均 <5，GIWA=25、DOGE=14 已 ≥5。按规则最多再搜 2 条 24h，且前提是主计划后 remainingToday 仍大致 ≥150；本轮 12 次后 remainingToday=51，远低于门槛，故默认不做。禁止把 KW_CORE 改成 24h。

## 新收录

**VYBE（`@launchonvybe` / https://launchonvybe.fun）** — 1 张。DeepSeek admit+score，overall=59，focus=false。已挂 `userFollowWatch + agentPadWatch`，写了 `links.x` 与 `links.twitter`。

- 本轮 KW_CORE 30m 命中官帖 2026-11-26 04:09:15 CST（https://x.com/launchonvybe/status/2125683251641745706）。
- 显示名 Vybe，建号 2026-11-08 00:21:45 CST（约 18.16 天），3 粉 / 2 帖，xUserId `2119102733198274560`。资料栏无网址，简介含平台币 CA `ks3h9hxbqSjz2ymvMGCPC4uJ991LxXaQBZEivv2vybe`。
- 官网 HTTPS 200，标题 “VYBE — Good vybes. Great potential.”，页内多次链到 https://x.com/launchonvybe（与官号互证，`siteXMutual=true`）。
- Solana 自定义 bonding curve 发射台：可配开盘/毕业 FDV，交易对支持 SOL / 其他加密资产 / 代币化股票，经 Raydium。站点费口径：VYBE-managed profiles 净收益 85% 创作者、15% VYBE。
- **不是免费 mint / 免费登记。** 发射/费用/曲线未实测。平台币 CA 已公开。本号不自动 mint。

## 看见但未收

- **Hamster CombatHQ `@HamsteCombatHQ`**：KW_CORE 仅见推广号 `@CryptoXHQ` 抽奖帖（04:08:33 CST）提到该号，自称 1,111 份 Robinhood 100% FREE MINT、Coming to Robinhood，资料栏只有 Telegram，无官网无合约。本轮未直接拉到该号原创帖（禁止为再确认加 X 读）。建号约 6.07 天、7 粉 / 3 帖。DeepSeek skip：未确认 LIVE，早期执行信息不足、风险过高。
- **`@pairedcoin`**：约 0.71 天，简介已给 pump CA，KW_CORE 仅为他人回复，已是上线代币而非新 mint 窗，未送审。
- **`$HAPPY @FINGERSAREHAPPY`**：Canton 社区代币，KW_CORE 为他人「如何购买」帖，不是新免费 mint 窗，未送审。
- **`@launchonvybe` 已收**；其余 unknowns 以老号/无关提及为主，未再扩搜。

## 关键刷新（尤其三个 ≤2h 窗口）

开跑约 04:09 CST，核验时三个窗口都还没到 05:00 CST。

### 2hour.fun `@2hourfun` — 仍 05:00 CST，尚未开窗，不重推

- MUST 24h 04:01:09 CST 官帖（https://x.com/2hourfun/status/2125681213071368656）：“1 hour”，**The first 2hourfun window opens at 21:00 UTC**（即 2026-11-26 05:00 CST），并称 `$2HOURFUN` 随窗口上线、合约只从该号公布。
- 03:23 CST 官帖仍是 “How to be ready for 21:00 UTC”；03:24 / 03:29 CST 短帖无改期。
- 官网 https://www.2hour.fun/ HTTPS 200：文案 “No coins on the curve right now. Come back when the window opens.” 静态页可见 “Window open 00:00:00”（未跑客户端计时，**不作已开窗证据**）。
- `/api/window` 返回 `{"perCoin":{},"traders":[]}`，窗口尚未打开。`/api/v1/window` 404。
- 时间表相对 R2207 未改。R2206 已发首次 ≤2h，**不重推**。

### Shielded Wizards `@ShieldedWizBTC` — 仍 05:00:00 CST，尚未开公售，不重推

- 权威接口 `https://brimhollow.app/launchpad/api/status`（未用静态 launch-schedule.js）：**phase=wl**，**minted=32/3333**（与 R2207 持平），reserved=0，mintOpen=true，mintUnavailable=false。
- 公售 `startsAt=2026-11-25T21:00:00.000Z` = **2026-11-26 05:00:00 CST**，与 R2207 改期后时刻一致，本轮未见再次改期。price=0（仍 Free），fee=4000。
- MUST 24h 25 条触顶未翻页，最旧一条仅到 01:14:52 CST（`fueltenderagent` 占 12 条），其中**未见 `@ShieldedWizBTC` 新官帖**，以官网 API 为准。
- WL 免费铸仍 LIVE（R2165 已提醒），不因仍 LIVE 或 minted 进度重推。R2207 已就改期通知，R2206 已发原时刻公售首次 ≤2h。**不重推**。

### Guns Of The Hood `@GunsOfTheHood` — 仍 05:00 CST，尚未开铸，不重推

- 04:00:00 CST 官帖（https://x.com/GunsOfTheHood/status/2125680927250473179）：“**1 HOUR LEFT**”，公售仍按 22:00 CET · 4 PM ET · 1 PM PT（**2026-11-26 05:00 CST**），10,000 sealed weapon crates，No whitelist，约 $0.05 in $ETH + gas，max 10 per wallet。03:02 CST 线程重申同一时刻。
- 官网 https://www.gunsofthehood.xyz/drop HTTPS 200：仍写 “The OpenSea mint is scheduled for 25 November at 22:00 Amsterdam time (21:00 UTC)”；Mint price **0.00003 ETH + gas**，Wallet limit 10，supply 10,000，Robinhood Chain；“Wallet sign-in opens when the collection launches”。
- OpenSea 合集 `guns-of-the-hood`：twitterUsername=GunsOfTheHood，合约 `0x1d3f3b153533bde7912da634b38ab50b3b90456d`（chain=robinhood），API total_supply=0。合集 HTML SeaDrop：**MINTING_SOON，0/10000**，PUBLIC_SALE 2026-11-26 05:00:00 CST 起（至 2027-11-26 04:00:00 CST），无地板。stats API 本轮 401，持有按 0 供计。
- 时间表相对 R2207 未改，未见改价/取消，仍未开铸。R2206 已发付费公售首次 ≤2h。**不是免费 mint。不重推。**

### 其他库内刷新（均无实质变化，不重推）

- **deMiners**：SeaDrop 仍 MINTING，active PUBLIC_SALE（自 2026-11-26 00:30:04 CST 至 2026-11-28 00:30:04 CST）。**575/3333**（R2207 为 572），持有 153（持平），地板 0.0000999 ETH（约 0.0001）。只是进度。MUST 见 01:14 CST 回复帖，无改价/改期。
- **Ugly Puggies**：仍 MINTING，active SIGNED_PRESALE stageIndex=2 至 **2026-11-26 13:30 CST**；stageIndex 3 仍是 SIGNED_PRESALE 至 2026-11-27 13:30 CST；PUBLIC_SALE 仍 2026-11-27 13:30 CST 起。**273/777**（R2207 为 263），持有 203（R2207 为 193），地板 0.000169 ETH（持平）。阶段未切，不重推。本轮 MUST 25 条窗口内未见该号新帖。
- **The Jacket**：仍 MINTING，active PUBLIC_SALE。OpenSea API / SeaDrop **213/777**（与 R2207 持平），持有 135，地板 0.61 USDG。MUST 窗口内未见新官帖。
- **Agent Cards**：官网 `/api/mint/status` 仍 phase=open，fillSold=5000/5000，curveSold=427，**sold=5427**/1,007,493，现价约 0.00198 BNB（与 R2207 完全一致）。不是免费 mint。MUST 窗口内未见新官帖。
- **TriForge**：RPC nft **757/3333**（R2207 为 756；01:32 CST 官帖当时报 721/3333），paused=false；预售仍 open（deadline 2026-12-02 10:01:25 CST），lpTotalMinted=1，claimsOpen、totalClaimed=31，tradingEnabled=false。只是钥匙进度 +1，已提醒过，不重推。
- **F0B90B**：RPC mintOpen=true，**426/10000**（与 R2207 持平）。
- **Antopia**：RPC saleOpen=true，**6253/8888**，freeClaimed=4000/4000，freeRemaining=0（与 R2207 持平）。
- **VALORIX**：cards.totalMinted=15，mint.fillSold=0（与 R2207 持平）。MUST 见 02:58 CST moltbook 验证帖，无新窗口。
- **Fueltender / AGX**：MUST 见 Fueltender 多条产品说明（无新免费窗）；AGX 三合约仍有代码。已提醒，不重推。
- **Slime**：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍自 **2026-11-29 00:00 CST** 起。不是已开铸 LIVE。
- **Bonebloom**：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍自 **2026-11-27 20:30 CST** 起，PUBLIC_SALE 自 2026-11-28 02:30 CST。距首窗约 40 小时，未到首次 ≤2h。R2207 已收录并通知。
- **YORI / BAD APE / Helium / ONE LaunchPad**：无实质变化，不重推。BAD APE OpenSea API total_supply=0，持有 0；Helium 官网仍 200。
- **Vicehood `@Vicehood_RH`（官集合集 vchood）**：SeaDrop MINTING_SOON 0/3333，SIGNED_PRESALE 仍 2026-11-27 01:00–04:00 CST，另有 stageIndex 2 至 05:00 CST，PUBLIC_SALE 自 2026-11-27 05:00 CST。距首窗约 21 小时，未到首次 ≤2h，不提前告警。同名合集 `vicehood`（非该官号，已在铸 209/3333）未与官号混淆。
- **Wildlife Universe / Tiger Universe**：SeaDrop MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 **2026-11-26 21:30 CST** 起。距首窗约 17 小时，未到首次 ≤2h，不提前告警。
- Canton/Glaze/TokenWorks：本轮无新 admit，仅刷 lastChecked。

MUST_WIN 限制：24h 查询 25 条触顶未翻页，最旧 01:14:52 CST；`@uglypuggies @agentcardshq @ShieldedWizBTC @TheJacket_NVDA @F0B90Bclub @antopia_xyz @Agx_bsc` 未出现在这 25 条里，相应状态以官网 / OpenSea / RPC 为准，未做额外 X 重读。

## notify 判定

**notify=true。**

- 原因：新收录 VYBE（须点名）。它不是免费 mint / 免费登记，但属于真新卡片。
- 三个 ≤2h 项目相对 R2207 时间表未变且尚未开窗/开铸，**不因仍在 ≤2h 窗口内重推**。
- `namedFreeMintOrRegistration=[]`，`namedPaidLe2h=[]`，`namedMintConfirm=[]`，`namedScheduleChange=[]`。
- alert 由 DeepSeek 撰写（略加 R2208 前缀与三个窗口不重推一句），含面板 https://reboot7454.github.io/early-scout/ 。本号不自动 mint。
- `dsFallback=false`。

## 交付

- `/tmp/r2208/RESULT_R2208.md`（本文件）
- `/tmp/r2208/notify.json`
- `/tmp/r2208/data.json`（APPLY_DRY_RUN=1，源 `/tmp/r2208/data.json.src`）
- `/tmp/r2208/apply_r2208.py`
- `/tmp/r2208/x_usage.json`

写盘核对：`meta.newThisRound == 顶层 newThisRound == round2208Added == ["launchonvybe"]`；上一轮 newThisRound 已清；ufCursor=2421 @tailtradesxyz；xBudgetMode=tight；discordPeekDeferred 占位已留。`/workspace/early-scout/data.json` 未被本路修改。

生成时间 2026-11-26 04:24:01 CST。
