# 早期打新雷达 R2211 RESULT

工作目录 `/tmp/r2211/`。本路完成 X 雷达（仅 UF + MUST_WIN）、站点/链上核验、apply 写盘并推送面板。未打开 Discord/浏览器。`discordPeekDeferred=true`（占位，须父进程同一轮补 Peek）。本轮无新收录，无首次开窗/开铸确认，故 **notify=false**，无需 DeepSeek 告警文案。`dsFallback=false`。

开跑约 2026-11-26 05:33 CST。写盘 `lastScout=2026-11-26 05:44:46 CST`。不是 08:00 CST 后全量补扫，`lastFullAfterReset` 保持 **R2170**。时区 Asia/Shanghai (CST)。关键站点/API 核验约 **05:36–05:37 CST**。

## 额度与模式

- 开火前 live remainingBefore=**37**（R2210 末次脚注 remainingAfter）。首搜 UF1 之后今日剩余 36，按搜索后剩余 +1 计，与预期一致。
- `mode=near-exhausted`（remaining <50），softCap=8，minSpend=6，silentCap=0。未 override-full。关键词、官号 mentions、MUST_OFF、静号、薄栏 24h **全部延期**，把剩余额度留给 08:00 CST 前的后续 MUST/UF 轮，以及 08:00 CST 后首轮全量补扫。minSpend=6 未凑满，不是漏跑。
- 已排 **2** 次全部跑完（UF1 + MUST_WIN），未再加计划外搜索，同一 handle 未重读。
- **xReads=2**（main=2，silent=0），**remainingBefore=37**，**remainingAfter=35**。
- 今日硬顶重置约 08:00 CST（脚注 `todayReset=2026-11-26T00:00:00.000Z`）。距重置约 4 轮，本轮未把额度打到 0。
- 写盘 `meta.xBudgetMode=near-exhausted`。

各次脚注（result_count / remainingToday）：
UF1 0/36，MUST_WIN 25/35（触顶有 next_token，未翻页）。全部 error=None。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- **十栏未跑全**：near-exhausted，十栏关键词本轮延期。`coverage.tenLanes=false`，`kwDeferred=true`。
- **UF 已刷（本轮分片，wrap=false）**：cursor 51 `@reapoxyz` 起，刷到 `@reynarlabs`（共 24 个）。预跳已知 NF 6 个（`@deadpacksol @blindfloor @blobsdotmeme @trytoprint @PlayFarmFi @reynarlabs`），故 from: 实际 **18** 个（UF1 1 次）。UF1 **0 帖**，无新官号开窗。写盘后 **ufCursor=75 `@world_ygg`**，uf_total=2434（本轮无新挂号）。
- **mentions**：本轮未跑，延期。**下轮 mentionsNext 仍为：DogeEVM / BTC / Starknet / squeek / STARX**（未推进指针）。
- **静号**：本轮未跑（silentCap=0）。**下轮静号仍为 Starknet**（未推进指针；若额度仍紧则延至 08:00 CST 后首轮全量补扫）。
- **未做薄栏 24h。** 与关键词一并延期。禁止把肥栏改成 24h。

## 新收录

**无。** UF 0 帖；MUST_WIN 25 条均为已在库官号。`newThisRound=[]`，`dsFallback=false`。

## 看见但未收

无新号候选。MUST_WIN 作者分布：`fueltenderagent` 10、`2hourfun` 8、`GunsOfTheHood` 6、`ShieldedWizBTC` 1。`@uglypuggies @deMinersNft @agentcardshq @TheJacket_NVDA @F0B90Bclub @antopia_xyz @TriForgeAgent @Agx_bsc` 未出现在这 25 条里，相应状态以官网 / OpenSea / RPC 为准，未做额外 X 重读。

2hour.fun MUST 新见开窗官帖：05:02:04 CST https://x.com/2hourfun/status/2125696546645651566 “We're open”（窗口至 23:00 UTC / 07:00 CST），以及 05:21:50 CST https://x.com/2hourfun/status/2125701519001764170（窗口还剩约 1h40m）。这是 R2210 已确认 LIVE 之后的官宣补齐，不是新的首次开窗。

## 关键刷新（三个 05:00 CST 窗口，核验约 05:36 CST）— 只刷进度，不重推

- **Shielded Wizards `@ShieldedWizBTC`**：免费公售仍 LIVE。API `phase=public`，minted=**58/3333**（R2210 为 32），reserved=**9**（上轮 6），`mintOpen=true`，price=0，perWallet=1，fee=4000。开售官帖仍是 05:00:06 CST。公售页 https://brimhollow.app/mint 。**R2210 已首次确认并通知，本轮只是进度，不重推。**
- **Guns Of The Hood `@GunsOfTheHood`**：付费公售仍 LIVE。OpenSea SeaDrop 仍 `mintStatus=MINTING`，erc721 **46/10000**（R2210 为 0），持有 7，地板空。合约仍是 `0x1d3f3b153533bde7912da634b38ab50b3b90456d`（Robinhood Chain）。官网 https://www.gunsofthehood.xyz/drop 定价仍是 **0.00003 ETH + gas**，Wallet limit 10；drop 页主文案可能仍写 scheduled / “Wallet sign-in opens when the collection launches”，以官帖与 OpenSea 为准。**R2210 已首次确认并通知，本轮只是进度，不重推。** 不是免费 mint。
- **2hour.fun `@2hourfun`**：官网仍显示 **Window open**，窗口开至 **07:00 CST**，故本轮仍标 `le2h=true`。平台币 **\$2HOURFUN** 仍在曲线、未毕业，CA `54PSWdiJbeF9H9Eumi3fLc8wfiLE3igN3GAuxb5zUeHi`，pool `AWPh3HYuc2e9d7ooAuEZhL75SoMRTggLCLWAh7bHjyDY`，进度约 **22.4%**（R2210 约 52.7%），官网 ExploreView 约 **\$7.0k mcap**（上轮约 \$16.1k），已筹约 **25.04 SOL / 约 \$1771**，门槛 112 SOL / 约 \$7921。最后成交约 05:35:42 CST。**R2210 已首次确认并通知，本轮只是进度/行情，不重推。** 不是免费 mint。

## 库内其它刷新（无开铸确认级变化，不重推）

- **Ugly Puggies**：仍 MINTING，**274/777**，持有 203，地板 0.000169 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST。与上轮持平。
- **deMiners**：仍 MINTING，合集 HTML SeaDrop **1278/3333**（R2210 为 668/3333），持有 188，地板约 0.000108 ETH。已 LIVE 的进度跳升，不因供应量变化重推。
- **The Jacket**：仍 MINTING，**214/777**，持有 136，地板 0.61 USDG，active 仍 PUBLIC_SALE。
- **Agent Cards**：官网 `/api/mint/status` 仍 phase=open，fillSold=5000/5000，curveSold=427，sold=**5427**/1,007,493，现价约 0.00198 BNB。与上轮持平。
- **TRIFORGE**：链上 Forge Keys **770/3333**（R2210 为 761），claims 31，预售仍开至 2026-12-02，挖矿仍开。小幅进度。
- **F0B90B**：链上 **429/10000**（R2210 为 427），mintOpen=True。
- **Antopia**：链上仍 **6253/8888**，saleOpen=True，免费额度仍满。
- **Fueltender**：MUST 见多条技术/安全向官帖（本轮 10 条），无新铸造窗口。
- **AGX**：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」，本轮 MUST 25 条未见 `@Agx_bsc`，未做额外 X 重读。
- **Helium / VYBE**：本轮 UF 分片未覆盖这两号。官网仍可访问。不是免费 mint。R2202 / R2208 已通知，不重推。
- **Bonebloom**：SeaDrop 仍 MINTING_SOON **0/555**，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，PUBLIC_SALE 仍 2026-11-28 02:30 CST。距首窗约 39 小时，未到首次 ≤2h。
- **Slime Agents**：SeaDrop 仍 MINTING_SOON 0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- **BAD APE**：OpenSea 供应仍为 0，未见开铸 LIVE。
- **Vicehood `@Vicehood_RH`（官集合集 vchood）**：SeaDrop 仍 MINTING_SOON 0/3333，SIGNED_PRESALE 仍 2026-11-27 01:00 CST 起，未到首次 ≤2h。同名合集 `vicehood`（非该官号，已在铸，本轮 209/3333、持有 13、地板 0.0035 ETH）未与官号混淆。
- **Wildlife Universe / Tiger Universe**：SeaDrop 仍 MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 **2026-11-26 21:30 CST** 起。距首窗约 16 小时，未到首次 ≤2h，不提前告警。
- Canton/Glaze/TokenWorks：本轮无新 admit，仅刷 lastChecked。

## notify 判定

**notify=false。**

- 原因：无新收录；三个 05:00 CST 窗口已在 R2210 首次确认并通知，本轮只是进度/行情刷新；2hour.fun 虽仍 ≤2h（至 07:00 CST），不重复提醒。
- `namedFreeMintOrRegistration=[]`，`namedMintConfirm=[]`，`namedPaidLe2h=[]`，`namedScheduleChange=[]`，`newCards=[]`。
- `dsFallback=false`。
- `discordPeekDeferred=true`：X 路径遇既有登录墙未做 Discord Peek，父进程须同一轮补 Peek；登录墙与此前轮次相同（上次尝试约 2026-11-26 03:02 CST 落在 discord.com/login），**不要重发登录表单**，除非已有新会话。补扫若出现免费 mint/登记再追加通知。

## 交付

- 面板 https://reboot7454.github.io/early-scout/
- 写盘并推送 `data.json` + `docs/data.json` + `RESULT_R2211.md` 到 `Reboot7454/early-scout` main。
- 下轮：UF 从 cursor 75 `@world_ygg` 继续；mentionsNext 仍 DogeEVM / BTC / Starknet / squeek / STARX；静号仍 Starknet。若 remaining 仍 <50，继续只保 UF + MUST_WIN；08:00 CST 后第一轮必须全量补扫（含瘦栏 24 小时关键词和 Discord 积压清理）。

