# RESULT R1792（合并：08:00 CST 后首轮全量补扫并入 Discord 已占轮）

- time: 2026-11-14 08:39:58 CST（Asia/Shanghai）。开跑前 `git pull` 已与 origin/main 对齐在 R1792 / ab0d025；Discord 已于 08:09 CST 落地补收 gpu-hubs（watching / 挖矿，非免费 LIVE，已通知，不重推）。本轮为例行 08:00 CST 后首轮 X 全量补扫合并进同一轮，不另起 R1793。notify=true（真新收录 FeeTag）。未自动 mint。
- mode: post-reset-full（forced）。X 日额约 08:00 CST 重置；首探 `search_posts_all` 页脚 remaining 999/1000，倒推 remainingBefore=1000。`python3 scripts/x_budget.py` 默认仍读到重置前残留 remaining=26（near-exhausted），不可用。脚本自动判定窗口是 local.hour==8 且 minute<25，本例行 08:28 才触发，故强制按 post-reset-full 跑全量：softCap=50，minSpend=24，silentCap=2，ufAccountShard=80。R1787–R1791 因 remaining<50 延后 KW / mentions / silent，本轮一次补齐。不是连续两轮重置后全量（R1739 为上一轮重置后全量；R1791 为重置前 near-exhausted；R1792 Discord 未做 X）。
- lastFullAfterReset: R1792（本轮）
- notify: true。例行新收录 FeeTag（@useFeeTag）Solana 发射台已 live：2026-11-14 08:24 CST 官宣，官推已用 get_users_by_usernames 核验，官网 https://feetag.fun 200 与 bio 一致，DeepSeek 综合 86，按真新必须提醒。gpu-hubs 已于本轮 Discord 通知，不重推。无新确认免费 NFT mint LIVE / 免费登记 / 首次 ≤2h。polyrob 公开销售仍 11-14 21:52 CST，约 13h；burybud 仍 11-14 23:00 CST，约 14h。第三方对 PlayPixelora / Tinylegends 的免费 mint 喊单未见官推确认，不改 LIVE、不预推。
- xReads: 33（main 31；silent 1；admitVerify 1）；remainingBefore 1000 → remaining 967 / 1000；softCap 50，minSpend 24，silentCap 2；main 31 未超 softCap，已达 minSpend（UF×4 + MUST×3 + THIN×2 + FAT×4 + 薄栏 KW×6 + 核心 KW×5 + KW_GAPS×1 + mentions×6 + silent×1；另 admitVerify×1）。官网 / HTTP / OpenSea 只读无 X 成本。from: 官号窗 start_time=2026-11-13T23:45:00Z；关键词 / mentions / silent start_time=2026-11-13T21:30:00Z（加长以覆盖 R1787 起延后的盲捞窗）。不翻页 next_token。search_posts_all 的 max_results 实际硬顶 25。
- admitVerifyReads: 1。核验 @useFeeTag（官号，10 粉 / 21 帖，2026-11-13 21:07 UTC 建号，bio 官网 feetag.fun，blue verified）与 @Halal_Dao（3960 粉，无官网，社区/alpha 号，本窗只出现在第三方 GTD 抽奖，跳过不收录）。
- tenLanes: true。薄栏 6 条独立 KW（LayerZero / Tape/电路 / GIWA / DogeEVM / BTC / Starknet）+ 核心栏 5 条（mint / mine / pad / GO / Elysium）+ KW_GAPS 均已跑。FAT 分片四表各刷 28 个有效官号。
- laneReads: 薄栏 KW 与核心栏、KW_GAPS、全链 mentions 均各 1 次查询（见下 mentions）。silent 1（Starknet 提法，0 帖）。
- userFollow: 刷本片 160→257，kept 80，skip 17（已知 NF，不连刷），另优先软刷 machinedotfun / bscaidrop / PulseLaunchpad / localbottomcom / NutshellMarkets；priority 已知 NF 跳过 mobster_meme、starx_xlayer。4 个 from: 批次，未绕回。UF accounts 1696→1699（本轮补挂 @useFeeTag / @Tinylegends_io / @AGNTX_HQ）。下一轮从 257 续。
- mentions: 本轮全覆盖，未延后。分 6 批：Tape；GIWA+Zero；LayerZero；BTC+Starknet+DogeEVM（含 @squeekchain）；Elysium+Kinetiq；pads（Irys / Full.fun / Arc / flap / NutshellMarkets / PulseLaunchpad / dotaipad / starx_xlayer）。
- fat shards: agentPad 154→250 kept 28 skip 68 未绕回；freeMint 242→277 kept 28 skip 7 未绕回；bnAgent 71→114 kept 28 skip 15 未绕回；elysium 168→197 kept 28 skip 1 未绕回。meta.fatNextStarts 已更新。
- thin official watches: 完整薄栏约 85 个有效官号，2 批（starknet / layerZero / btcPrivacy / btcCrc20 / dogeEvm / tape / tapeOut / giwa / zero）。另 MUST/≤2h/LIVE 官号 3 批共 25 号（含 UseCPay / squeez7z / gpu_hubs）。
- silentAccounts: ran=true，lane=Starknet（1792%11=10），silentCap=2 本轮用 1（search_users 仍不可用，仅 mention 路径），结果 0 帖。
- discordPeekDeferred: true（本例行默认不登录 DC；开跑前 git pull 已见 Discord 占轮 ab0d025）。
- DS: FeeTag 送审 deepseek-flash（思考开启）。admit=true，scores early 95 / actionable 82 / novelty 78 / risk 58 / overall 86。alert 已生成。Halal_Dao 未送审（非项目官号）。未编造 CA/官号/官网。未自动 mint。
- watch-bug: 发现 tinylegends-io、agntx-hq 在库但不在任何 Watch，当场补进 userFollowWatch + freeMintWatch。gpu-hubs 兼挂 miningWatch。feetag 进 userFollowWatch。未做整表回填（残留未挂计数 2081→2079）。
- new cards: 例行新收录 1 张 feetag（另保留本轮 Discord 的 gpu-hubs）。meta.newThisRound == 顶层 newThisRound == round1792Added == ["gpu-hubs","feetag"]。candidateCount=4223→4224。UF accounts=1699。新卡 focus=false。

## 新收录

- feetag（@useFeeTag，台子/Meme，Solana，status=live，overall 86）：08:24 CST 官宣 “FeeTag is live”。在 X / Instagram / TikTok 标记账号后于 pump.fun 发射，creator fees 自动给被标记账号。X 回复 `@useFeeTag @handle $TICKER` 可由平台 launch fund 免费发射；官网站内发射需自付一笔 SOL。交易在 pump.fun，X cashtag 走 fomo。IG/TikTok 收益先进入平台代管 payout 账户（平台持有密钥）。官网 https://feetag.fun，与官推 bio 一致。feetag.com 为无关站点，不用。账号约 10 粉，极早期。按真新 notify。

## 窗口刷新（均非新的免费 LIVE / 非首次 ≤2h，不重推）

- gpu-hubs：R1792 Discord 已收录并通知。本窗官号续发机制帖，仍无 CA/前端，粉丝仍约 1。已兼挂 miningWatch。不重推。
- polyrob：官号 08:30 CST 发 “Mint is live”。铸造页仍 200，仍标 Mint not live yet / not open；公开销售仍 11-14 21:52 CST，约 13h，非 ≤2h。polyrob.xyz 仍 SSL EOF。R1772 已推，不重推。
- burybud：官号 08:30 CST 再确认 11-14 23:00 CST（15:00 UTC）上 Pons。官网 burybud.xyz 本轮 200（上轮 ssl_eof）。CA 仍未公布。约 14h，非 ≤2h，不预推。
- jpeg-monkes：官号本窗仍推 mint 入口。OpenSea sales 1930→1956，owners 873→869，floor 约 0.00040 ETH。免费窗已过，不重推。
- jager：官号宣布 $JAGENT pool burn is live。官网仍 200，付费 mint 仍开放、当前档 1U，不是新的免费窗，不重推。
- play-pixelora：已补 handle=@PlayPixelora。第三方喊 ALPHA FREE MINT，官网仍是白名单页（2,222 Free Land Plots），未见官推确认开铸，不改 LIVE、不预推。
- tinylegends-io：第三方称今日 12:00 UTC 免费 mint，官推未亲自确认，不写入正式开窗。已补 Watch。不预推。
- agntx-hq：本窗无官推确认窗口。已补 Watch。不预推。
- agent-raise：本窗官号仍在推 $AR 募资，已在库，不重推。

## 例行侧 skips

- Halal_Dao：仅出现在第三方 GTD 抽奖，无项目官网，不收录。
- DIPURIOLIVE / kitthecalico 抽奖：已在库或非新项目，不另收。
- 大量关键词噪音（含无关 GO launch、政府/宠物等）未建卡。

## 面板与推送

- docsSynced=true（Pages 源为 main:/docs；根目录与 docs/data.json 一并推到 R1792 merge）
- panel: https://reboot7454.github.io/early-scout/
- 未自动 mint。
- alert: 新收录｜FeeTag（@useFeeTag）Solana 发射台已 live：标记 X/IG/TikTok 账号即可在 pump.fun 发射，creator fees 自动归被标记账号，综合 86 分。详情 https://reboot7454.github.io/early-scout/
