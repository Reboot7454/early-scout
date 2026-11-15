# RESULT R1849

- 时间：2026-11-15 11:14 CST（Asia/Shanghai）
- 模式：独立例行 ample（非 08:00 CST 后第二轮全量补扫；lastFullAfterReset 保持 R1843）
- notify=true
- 新收录：gloopix、usegnomon（均已通知一次）
- ≤2h 新窗口：无
- xReads 28（main 26 + silent 1 + admitVerify 1），remainingBefore 834 → 806
- mode=ample（softCap 28，minSpend 20，silentCap 2，ufAccountShard 50）
- UF 3 + MUST 3 + THIN 5 + 薄栏 KW×6 + 核心栏 KW×5 + mentions 4 + silent 1 + admitVerify 1
- UF 从 1393 Agentdeskonsol 起 kept 50 skip 0，last kept 1442 ELYMONS_，next start 1443 unicornxdotfun
- 十栏关键词均已跑全；mentions 本轮覆盖 LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX
- silent 1849%11=1 → 挖矿（search_users 仍不可用，仅 mentions，1 条噪音）
- dsFallback=false；discordPeekDeferred=true
- 未自动 mint

## 新收录

- **gloopix**（@Gloopix_，打新，status=watching，overall 60）：官号 2026-10-15 20:40 CST 建立，仅 1 帖、210 粉，资料栏无官网。唯一官帖 2026-11-14 22:00 CST 宣布 2,222 枚像素头像 FREE MINT on Robinhood App，无 mint 页/时间/白名单规则。OpenSea 同名合约展示为 OFFSIDE ART，未核实为官方 CA。免费 mint 官宣即便 score<70 也必须推送。已进 userFollowWatch + freeMintWatch。
- **usegnomon**（@usegnomon / Gnomon，Elysium生态，status=watching，overall 66）：官网 https://usegnomon.xyz/ 与官推互链。定位 Elysium 自动化执行层（类 Gelato），站点仍为 PREVIEW，合约未部署、未审计。官帖 10:56 CST 宣布定位。已进 userFollowWatch + elysiumWatch + kinetiqWatch。

## DeepSeek 未收录

- memepad-lol（@memepad_lol / memepad.lol）：韩国迷因发射台已运行，$MPAD 毕业约 104 天，非极早期，skip。
- tapeexit（@TapeExit）：资料栏指向个人 GitHub，2 粉/5 帖，公开版只读，证据过薄，skip。
- BTRFLYely 自称 Elysium/Montra unofficial mascot，未送审。

## 在库进度（不重推）

- elysiasealed：官号 10:51 CST 报 PLANO on Pons 近 24h 411 笔；STOA 口径已在 R1848 记下。已通知过的 live 窗口，非 ≤2h。
- echofun：官号 10:32 CST 提醒核验 chain ID 56 再 mint。已是 live 铸造提醒，非新窗。
- polyrob：官号 11:00 CST 再申 0.033 ETH mint，关闭仍为 2026-11-16 01:12 CST，约 14 小时后，尚未 ≤2h。已在库 live。
- microfrens：官号回复提醒 hold 3 进 snapshot / 持有者 free mint WL；关键词窗另见对旧「Reducing Supply + FREE」帖的转发。不是新的对公免费 LIVE 窗口。
- thedawgzrh：2h 窗仍在转发 2026-10-27 的介绍帖（当时写 24 hours to get in），窗口早已过期，维持 watching。
- coinfin / hokori-quantum：本窗无新于 R1848 的实质进度，仅刷新 lastChecked。
- hood-turtle / umbrapad / elyver-xyz / qtronlaptops / hood-bitz：MUST/待窗项目 1h 官方窗无新开窗。qtronlaptops 11-16 01:00 CST、hood-turtle 11-17 22:15 CST、BITBOTZ Monday 11-16 均尚未 ≤2h，已通知过的不重推。

## 关键词 / mentions 摘记

- 薄栏 6 条独立 KW（LayerZero / Tape/电路 / GIWA / DogeEVM / BTC / Starknet）与核心栏 5 条 KW 本轮均已跑全。
- 打新 KW 命中 Gloopix 转发，因而发现并 admitVerify 官帖（1 次额外 from:Gloopix_，未分页）。
- mentions：LayerZero 6、Elysium+kinetiq 18、mining-squeek+Nutshell 0、BN Agent pads+STARX 2，多为在库讨论或噪音；Gnomon 官帖在 Elysium 关键词/官号窗被捕捉。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1849.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：真新收录 gloopix（免费 mint 官宣）与 usegnomon。

## 未做 / 交接

- 未自动 mint。本轮 4 个候选送 DeepSeek（2 收 / 2 跳），dsFallback=false。
- search_users 仍不可用；silent 已用 mentions 路径跑完挖矿栏。
- lastFullAfterReset=R1843。UF cursor=1442（下一 walk 从 1443 起，startHandle=unicornxdotfun）。mentionsNext=Tape / GIWA / BTC / Starknet+DogeEVM。fat 分片起点未变（agentPad 250 / freeMint 277 / bnAgent 114 / elysium 197）。
- 待临近 ≤2h 再报：qtronlaptops 2026-11-16 01:00 CST、polyrob 关闭 2026-11-16 01:12 CST、BITBOTZ Monday 2026-11-16、hood-turtle 开铸 2026-11-17 22:15 CST。
