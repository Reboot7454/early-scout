# 早期打新雷达 R2213 RESULT

工作目录 /tmp/r2213/。本路完成 X 雷达（仅 UF + MUST_WIN）、站点/链上核验、apply 写盘并推送面板。未打开 Discord/浏览器。discordPeekDeferred=true（占位，须父进程同一轮补 Peek）。本轮无新收录，但 2hour.fun 官帖宣布发币费从 $100 改为免费且第一场窗口仍开，故 notify=true。dsFallback=false，告警文案由 DeepSeek 生成。

开跑约 2026-11-26 06:31 CST。写盘 lastScout=2026-11-26 06:40:51 CST。不是 08:00 CST 后全量补扫，lastFullAfterReset 保持 R2170。时区 Asia/Shanghai (CST)。关键站点/API 核验约 06:34–06:37 CST。

## 额度与模式

- 开火前 live remainingBefore=32（R2212 末次脚注 remainingAfter）。首搜 UF1 之后今日剩余 31，按搜索后剩余 +1 计，与预期一致。
- mode=near-exhausted（remaining <50），softCap=8，minSpend=6，silentCap=0。未 override-full。关键词、官号 mentions、MUST_OFF、静号、薄栏 24h 全部延期，把剩余额度留给 08:00 CST 前的后续 MUST/UF 轮，以及 08:00 CST 后首轮全量补扫。minSpend=6 未凑满，不是漏跑。
- 计划 2 次（UF1 + MUST_WIN），实际 2 次。同一 handle 未做额外确认重读。MUST_WIN 24h 用正确窗口，未再误开短窗。
- xReads=2（main=2，silent=0），remainingBefore=32，remainingAfter=30。
- 今日硬顶重置约 08:00 CST（脚注 todayReset=2026-11-26T00:00:00.000Z）。距重置约 2 轮，本轮未把额度打到 0。
- 写盘 meta.xBudgetMode=near-exhausted。

各次脚注（result_count / remainingToday）：
UF1 0/31，MUST_WIN 25/30（触顶有 next_token，未翻页）。全部 error=None。

## 十栏 / UF / mentions / 静号 / 薄栏 24h

- 十栏未跑全：near-exhausted，十栏关键词本轮延期。coverage.tenLanes=false，kwDeferred=true。
- UF 已刷（本轮分片，wrap=false）：cursor 99 @paycashtag 起，刷到 @squeekchain（共 24 个）。预跳已知 NF 3 个（@battle_pad @cabaldotfun @project_hoodmon），故 from: 实际 21 个（UF1 1 次）。UF1 0 帖，无新官号开窗。写盘后 ufCursor=123 @pipfun_xyz，uf_total=2434（本轮无新挂号）。
- mentions：本轮未跑，延期。下轮 mentionsNext 仍为：DogeEVM / BTC / Starknet / squeek / STARX（未推进指针）。
- 静号：本轮未跑（silentCap=0）。下轮静号仍为 Starknet（未推进指针；若额度仍紧则延至 08:00 CST 后首轮全量补扫）。
- 未做薄栏 24h。与关键词一并延期。禁止把肥栏改成 24h。

## 新收录

无。UF 0 帖；MUST_WIN 25 条均为已在库官号。newThisRound=[]，dsFallback=false。

## 看见但未收

无新号候选。MUST_WIN 作者分布：fueltenderagent 11、2hourfun 10、GunsOfTheHood 3、ShieldedWizBTC 1。@uglypuggies @deMinersNft @agentcardshq @TheJacket_NVDA @F0B90Bclub @antopia_xyz @TriForgeAgent @VALORIXBNB @Agx_bsc 未出现在这 25 条里，相应状态以官网 / OpenSea / RPC 为准，未做额外 X 重读。

Explore /api/window 另见 Robinhood 链币 0x5f8d1a0df77bcb16ab46d4db5d3df66bcdb2cfb1，peak 约 $2.7k，本轮 API volume/traders 为 0，名称/官推未解析到，未单独建卡。

## 关键刷新 — 2hour.fun 发币费改为免费（本轮通知）

- 2hour.fun @2hourfun：官网仍显示 Window open，窗口开至 07:00 CST，故本轮仍标 le2h=true。
- 官帖 2026-11-26 06:05:02 CST（https://x.com/2hourfun/status/2125712391253930030）宣布：此前 $100 发币费被指为门槛，即刻起在 2hour.fun 发币免费（Solana 与 Robinhood Chain）。其余安排不变（每日一窗 21:00–23:00 UTC、Season 1 airdrop、Refund Bot、最多 $2M dev incentives、首窗 Premiere/Diamond 徽章）。这是费率/规则变更，不是 NFT 免费 mint。
- R2210 已首次确认并通知窗口开启（当时仍是 $100 发币费）。本轮因改为免费再通知，不是单纯进度重推。
- 平台币 $2HOURFUN 仍在曲线、未毕业，CA 54PSWdiJbeF9H9Eumi3fLc8wfiLE3igN3GAuxb5zUeHi，pool AWPh3HYuc2e9d7ooAuEZhL75SoMRTggLCLWAh7bHjyDY，进度约 27.0%（R2212 约 33.0%），官网约 $8.1k mcap（上轮约 $9.7k），已筹约 30.29 SOL / 约 $2132，门槛 112 SOL / 约 $7884。最后成交约 06:32:53 CST。/api/window traderCount=37。

## 库内其它刷新（无开铸确认级变化，不重推）

- Shielded Wizards @ShieldedWizBTC：免费公售仍 LIVE。API phase=public，minted=78/3333（R2212 为 63），reserved=3（上轮 13），mintOpen=true，price=0，perWallet=1，fee=4000。开售官帖仍是 05:00:06 CST。公售页 https://brimhollow.app/mint 。R2210 已首次确认并通知，本轮只是进度，不重推。
- Guns Of The Hood @GunsOfTheHood：付费公售仍 LIVE。OpenSea SeaDrop 仍 mintStatus=MINTING，erc721 90/10000（R2212 为 68），持有 13（上轮 10），地板 0。合约仍是 0x1d3f3b153533bde7912da634b38ab50b3b90456d（Robinhood Chain）。官网 https://www.gunsofthehood.xyz/drop 定价仍是 0.00003 ETH + gas，Wallet limit 10。R2210 已首次确认并通知，本轮只是进度，不重推。不是免费 mint。
- Ugly Puggies：仍 MINTING，310/777（R2212 为 309），持有 237，地板 0.000169 ETH。active 仍 SIGNED_PRESALE stageIndex=2 至 2026-11-26 13:30 CST。只是进度。
- deMiners：仍 MINTING，SeaDrop / OpenSea 1364/3333（R2212 为 1363/3333），持有 181，地板约 0.000107 ETH。PUBLIC_SALE 仍至 2026-11-28 00:30:04 CST。已 LIVE 的进度跳升，不因供应量变化重推。
- The Jacket：仍 MINTING，214/777，持有 136，地板 0.61 USDG，active 仍 PUBLIC_SALE。与上轮持平。
- Agent Cards：官网 /api/mint/status 仍 phase=open，fillSold=5000/5000，curveSold=527，sold=5527/1,007,493，现价约 0.00216 BNB。与 R2212 持平。
- TRIFORGE：链上 Forge Keys 775/3333（R2212 为 773），claims 31，预售仍开至 2026-12-02，挖矿仍开。小幅进度。
- F0B90B：链上 433/10000（R2212 为 430），mintOpen=True。
- Antopia：链上仍 6253/8888，saleOpen=True，免费额度仍满。
- VALORIX：链上 Hero Cards 仍 15，fillSold=0/5500。
- Fueltender：MUST 见多条技术/安全/flight-log 向官帖（本轮 11 条），无新铸造窗口。
- AGX：官网仍是「官网维护中，即将回来 / Under maintenance. Back soon.」，本轮 MUST 25 条未见 @Agx_bsc，未做额外 X 重读。
- Helium / VYBE：本轮 UF 分片未覆盖这两号。不是免费 mint。R2202 / R2208 已通知，不重推。
- Bonebloom：SeaDrop 仍 MINTING_SOON 0/555，SIGNED_PRESALE 仍 2026-11-27 20:30 CST，PUBLIC_SALE 仍 2026-11-28 02:30 CST。距首窗约 38 小时，未到首次 ≤2h。
- Slime Agents：SeaDrop 仍 MINTING_SOON 0/555，预售仍 2026-11-29 00:00 CST，不是已开铸 LIVE。
- BAD APE：OpenSea 供应仍为 0，未见开铸 LIVE。
- Vicehood @Vicehood_RH（官集合集 vchood）：SeaDrop 仍 MINTING_SOON 0/3333，SIGNED_PRESALE 仍 2026-11-27 01:00 CST 起，未到首次 ≤2h。同名合集 vicehood（非该官号，已在铸，本轮 209/3333）未与官号混淆。
- Wildlife Universe / Tiger Universe：SeaDrop 仍 MINTING_SOON 0/5555，SIGNED_PRESALE 仍自 2026-11-26 21:30 CST 起。距首窗约 15 小时，未到首次 ≤2h，不提前告警。
- Canton/Glaze/TokenWorks：本轮无新 admit，仅刷 lastChecked。

## notify 判定

notify=true。

- 原因：无新收录；三个 05:00 CST 窗口已在 R2210 首次确认并通知，Wizards/Guns 本轮只是进度、不重推。但 2hour.fun 在窗口仍开期间（至 07:00 CST）官宣发币费从 $100 改为免费，属可操作规则变更，需要提醒。不是 NFT 免费 mint。
- namedFreeMintOrRegistration=[]，namedMintConfirm=[]，namedPaidLe2h=[]，namedScheduleChange=["2hourfun launch fee $100 -> free"]，newCards=[]，le2h=["2hourfun"]。
- dsFallback=false。
- discordPeekDeferred=true：X 路径遇既有登录墙未做 Discord Peek，父进程须同一轮补 Peek；登录墙与此前轮次相同（上次尝试约 2026-11-26 03:02 CST 落在 discord.com/login），不要重发登录表单，除非已有新会话。补扫若出现免费 mint/登记再追加通知。

## 交付

- 面板 https://reboot7454.github.io/early-scout/
- 写盘并推送 data.json + docs/data.json + RESULT_R2213.md 到 Reboot7454/early-scout main。
- 下轮：UF 从 cursor 123 @pipfun_xyz 继续；mentionsNext 仍 DogeEVM / BTC / Starknet / squeek / STARX；静号仍 Starknet。若 remaining 仍 <50，继续只保 UF + MUST_WIN；08:00 CST 后第一轮必须全量补扫（含瘦栏 24 小时关键词和 Discord 积压清理）。
