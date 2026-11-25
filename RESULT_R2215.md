# 早期打新雷达 R2215 RESULT

工作目录 /tmp/r2215/。本路完成 X 雷达（UF1–UF5 + MUST_WIN）、站点/链上核验、apply 写盘并推送面板。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek）。本轮无新收录。2hour.fun 官帖 07:07:21 CST 确认第一场窗口已结束，并确认第二窗为明天 21:00 UTC（2026-11-27 05:00 CST）；关窗已在 R2214 按官网 payload 汇报，发币费改免费已在 R2213 通知，其余均为进度刷新，故 notify=false。dsFallback=false。

开跑约 2026-11-26 07:31 CST。写盘 lastScout=2026-11-26 07:41:40 CST。这是 08:00 CST 前最后一轮，不是全量补扫，lastFullAfterReset 保持 R2170。时区 Asia/Shanghai (CST)。关键站点/API 核验约 07:33–07:40 CST。

## 额度与模式

- 开火前 live remainingBefore=28（R2214 末次脚注 remainingAfter）。首搜 UF1 之后今日剩余 27，按搜索后剩余 +1 计，与预期一致。
- mode=near-exhausted（remaining <50），softCap=8，minSpend=6，silentCap=0。未 override-full。关键词、官号 mentions、MUST_OFF、静号、薄栏 24h 全部延期，留给 08:00 CST 后首轮全量补扫。本轮是重置前末轮，按 minSpend=6 跑满（UF 连续 5 个分片 + MUST_WIN），不再把额度预留给后续 08:00 前轮次。
- 计划 6 次（UF1–UF5 + MUST_WIN），实际 6 次。同一 handle 未做额外确认重读。MUST_WIN 24h 用正确窗口，触顶有 next_token，未翻页。
- xReads=6（main=6，silent=0），remainingBefore=28，remainingAfter=22。
- 今日硬顶重置约 08:00 CST（脚注 todayReset=2026-11-26T00:00:00.000Z）。本轮未把额度打到 0。
- 写盘 meta.xBudgetMode=near-exhausted。

各次脚注（result_count / remainingToday）：
UF1 0/27，UF2 0/26，UF3 0/25，UF4 0/24，UF5 0/23，MUST_WIN 25/22（触顶有 next_token，未翻页）。全部 error=None。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- 十栏未跑全：near-exhausted，十栏关键词本轮延期。coverage.tenLanes=false，kwDeferred=true。
- UF 已刷（本轮 5 个分片，wrap=false）：cursor 147 @Oxbitgen 起，刷到 @nuovora_fun（共 120 个）。预跳已知 NF 23 个（含用户点名但长期 NF 的 @starx_xlayer，未做额外 getUsers 重读），故 from: 实际 97 个（UF1–UF5）。UF1–UF5 均为 0 帖，无新官号开窗。写盘后 ufCursor=267 @auven_ai，uf_total=2434（本轮无新挂号）。
- mentions：本轮未跑，延期。下轮 mentionsNext 仍为：DogeEVM / BTC / Starknet / squeek / STARX（未推进指针）。
- 静号：本轮未跑（silentCap=0）。下轮静号仍为 Starknet（未推进指针；08:00 CST 后首轮全量补扫时应纳入）。
- 未做薄栏 24h。与关键词一并延期。禁止把肥栏改成 24h。08:00 CST 后第一轮必须全量补扫（须含瘦栏 24 小时关键词和 Discord 积压清理）。

## 新收录

无。UF 0 帖；MUST_WIN 25 条均为已在库官号。newThisRound=[]，dsFallback=false。

## 看见但未收

无新号候选。MUST_WIN 作者分布：2hourfun 11、fueltenderagent 10、GunsOfTheHood 3、ShieldedWizBTC 1。@uglypuggies @deMinersNft @agentcardshq @TheJacket_NVDA @F0B90Bclub @antopia_xyz @TriForgeAgent @VALORIXBNB @Agx_bsc 未出现在这 25 条里，相应状态以官网 / OpenSea / RPC 为准，未做额外 X 重读。

Explore /api/window 另见 Robinhood 链币 0x5f8d1a0df77bcb16ab46d4db5d3df66bcdb2cfb1，peak 约 $2.7k，本轮 API volume/traders 为 0，名称/官推未解析到，未单独建卡。

## 关键刷新 — 2hour.fun 关窗官帖已核到（不重推）

- 2hour.fun @2hourfun：第一场官方窗口已按原时间表于 07:00 CST 关闭。官网 RSC payload 仍为 `"open":false`。首页 SSR 仍可能显示 Window open + 00:00:00 倒计时占位，不以该标签为准。
- 官帖 07:07:21 CST（https://x.com/2hourfun/status/2125728073392033795）确认 Window one: done，并写明 Window two: tomorrow, 21:00 UTC（2026-11-27 05:00 CST）。R2214 MUST 约在 07:07 前后，当时还未见此帖，只按官网关窗。
- 官帖自称 233 traders、$44K traded、$2HOURFUN 曾 11x 至 $29.7K。这是官方口径；官网 /api/window traderCount 仍为 37，peak 约 $28.0k。两者一并记录，不以 API 否认官帖，也不把官帖数字当成 API 读数。
- 另称 tomorrow devs get more、Big updates landing before window two，未见具体规则或改期，是预告不是新窗口。
- 发币费仍为免费（R2213 已通知 06:05:02 CST 官帖 https://x.com/2hourfun/status/2125712391253930030），不是 NFT 免费 mint。
- 平台币 $2HOURFUN 仍在曲线、未毕业，CA 54PSWdiJbeF9H9Eumi3fLc8wfiLE3igN3GAuxb5zUeHi，pool AWPh3HYuc2e9d7ooAuEZhL75SoMRTggLCLWAh7bHjyDY，进度约 14.6%（R2214 约 14.3%），官网约 $5.2k mcap（上轮约 $5.1k），已筹约 16.31 SOL / 约 $1146（上轮 15.96 SOL / 约 $1120），门槛 112 SOL。最后成交约 07:25:45 CST。
- 下一窗已由官帖确认：2026-11-27 05:00–07:00 CST（约 21.3 小时），未到 ≤2h。关窗与下一窗时间均按原计划，费率变更已通知，不重推。已清 meta.le2h / meta.le2hIds（R2214 写盘后 meta.le2h 仍残留 `['2hourfun']`，本轮补清；卡片 status 此前已是 window_closed）。

## 库内其它刷新（无开铸确认级变化，不重推）

- Shielded Wizards @ShieldedWizBTC：免费公售仍 LIVE。API phase=public，minted=91/3333（R2214 为 83），reserved=3（上轮 1），mintOpen=true，price=0，perWallet=1，fee=4000。开售官帖仍是 05:00:06 CST。公售页 https://brimhollow.app/mint 。R2210 已首次确认并通知，本轮只是进度，不重推。
- Guns Of The Hood @GunsOfTheHood：付费公售仍 LIVE。OpenSea SeaDrop 仍 mintStatus=MINTING，erc721 90/10000（与 R2214 持平），持有 13，地板 0。合约仍是 0x1d3f3b153533bde7912da634b38ab50b3b90456d（Robinhood Chain）。官网 https://www.gunsofthehood.xyz/drop 定价仍是 0.00003 ETH + gas，Wallet limit 10。R2210 已首次确认并通知，本轮只是进度，不重推。不是免费 mint。
- Ugly Puggies：仍 MINTING，310/777（与 R2214 持平），持有 237，地板 0.000169 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST。只是进度。
- deMiners：仍 MINTING，SeaDrop / OpenSea 1364/3333（与 R2214 持平），持有 180（上轮 181），地板约 0.000107 ETH。PUBLIC_SALE 仍至 2026-11-28 00:30:04 CST。已 LIVE 的进度，不因供应量/持有变化重推。
- The Jacket：仍 MINTING，214/777，持有 136，地板 0.61 USDG，active 仍 PUBLIC_SALE。与上轮持平。
- Agent Cards：官网 /api/mint/status 仍 phase=open，fillSold=5000/5000，curveSold=533，sold=5533/1,007,493（R2214 为 527 / 5527），现价约 0.00216 BNB。只是进度。
- TRIFORGE：链上 Forge Keys 777/3333，claims 32，与 R2214 持平。预售仍开至 2026-12-02，挖矿仍开。
- F0B90B：链上仍 433/10000（与 R2214 持平），mintOpen=True。
- Antopia：链上仍 6253/8888，saleOpen=True，免费额度仍满。
- VALORIX：链上 Hero Cards 仍 15，fillSold=0/5500。
- Fueltender：MUST 见多条技术/安全向官帖（本轮 10 条），无新铸造窗口。
- AGX：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」，本轮 MUST 25 条未见 @Agx_bsc，未做额外 X 重读。
- Helium / VYBE：本轮 UF 分片未覆盖这两号。不是免费 mint。R2202 / R2208 已通知，不重推。
- Bonebloom：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，PUBLIC_SALE 仍 2026-11-28 02:30 CST。距首窗约 37 小时，未到首次 ≤2h。
- Slime Agents：SeaDrop 仍 MINTING_SOON 0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- BAD APE：OpenSea 供应仍为 0，未见开铸 LIVE。
- Vicehood @Vicehood_RH（官集合集 vchood）：SeaDrop 仍 MINTING_SOON 0/3333，SIGNED_PRESALE 仍 2026-11-27 01:00 CST 起，距首窗约 17.3 小时，未到首次 ≤2h。同名合集 vicehood（非该官号，已在铸，本轮仍约 209/3333）未与官号混淆。
- Wildlife Universe / Tiger Universe：SeaDrop 仍 MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起。距首窗约 13.8 小时，未到首次 ≤2h，不提前告警。
- Canton/Glaze/TokenWorks：本轮无新 admit，仅刷 lastChecked。

## notify 判定

notify=false。

- 原因：无新收录；2hour.fun 关窗官帖只是确认 R2214 已按官网汇报的计划关窗，并重申原定第二窗时间；发币费改免费已在 R2213 通知；「big updates before window two」只是预告。Wizards/Guns 及其它 LIVE 项本轮只是进度、不重推。无首次 ≤2h 窗口。
- namedFreeMintOrRegistration=[]，namedMintConfirm=[]，namedPaidLe2h=[]，namedScheduleChange=[]，newCards=[]，le2h=[]。
- dsFallback=false。
- discordPeekDeferred=true：X 路径遇既有登录墙未做 Discord Peek，父进程须同一轮补 Peek；登录墙与此前轮次相同（上次尝试约 2026-11-26 03:02 CST 落在 discord.com/login），不要重发登录表单，除非已有新会话。补扫若出现免费 mint/登记再追加通知。

## 交付

- 面板 https://reboot7454.github.io/early-scout/
- 写盘并推送 data.json + docs/data.json + RESULT_R2215.md 到 Reboot7454/early-scout main。
- 下轮：UF 从 cursor 267 @auven_ai 继续；mentionsNext 仍 DogeEVM / BTC / Starknet / squeek / STARX；静号仍 Starknet。08:00 CST 后第一轮必须全量补扫（UF+十栏关键词+全链 mentions+瘦栏 24 小时关键词+Discord 积压清理）。本轮剩余 22 次将随 08:00 CST 重置作废。
