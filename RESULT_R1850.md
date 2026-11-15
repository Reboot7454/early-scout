# RESULT R1850

- 时间：2026-11-15 11:38 CST（Asia/Shanghai）
- 模式：独立例行 ample（非 08:00 CST 后第二轮全量补扫；lastFullAfterReset 保持 R1843）
- notify=true
- 新收录：usexfee、nearvanapad
- ≤2h 新窗口：无
- xReads 28（main 26 + silent 1 + admitVerify 1），remainingBefore 806 → 778
- mode=ample（softCap 28，minSpend 20，silentCap 2，ufAccountShard 50）
- UF 3 + MUST 3 + THIN 5 + 薄栏 KW×6 + 核心栏 KW×5 + mentions 4 + silent 1 + admitVerify 1
- UF 从 1442 unicornxdotfun 起 kept 50 skip 0，last kept 1491 playaventra，next start 1492 liquidlootgg（R1849 所写 nextStart 1443 与当前表差 1，本轮以 handle unicornxdotfun 为准）
- 十栏关键词均已跑全；mentions 本轮覆盖 Tape / GIWA / BTC / Starknet+DogeEVM
- silent 1850%11=2 → 台子/Meme（search_users 仍不可用，仅 mentions，命中噪音未送审）
- dsFallback=false；discordPeekDeferred=true
- 未自动 mint

## 新收录

- **usexfee**（@useXFee，台子/Meme，status=live，overall 74）：官号 2026-11-15 05:53 CST 建立，约 9 粉、12 帖。官网 https://usexfee.fun/ 与官推互链，官帖 11:23 CST 宣布 We’re live。定位反向 X Money 发射台：把币绑到任意 X 账号，该账号回复/引用/转帖时 creator fees 付给被互动的人；可连钱包在 pump.fun 一签发射。站点 CFG 披露 CA 7DicoaDnuUPJKVCMLg8h2CLPqt4Xjcy6ZNHJYgFApump（未链上核实），无审计。已进 userFollowWatch。非免费 mint、非 ≤2h，因真新收录推送。
- **nearvanapad**（@nearvanapad / Nearvana，台子/Meme，status=watching，overall 56）：官号 2026-09-30 建立，44 粉、92 帖。资料栏无网站字段，bio 给出测试网 https://testnet.nearvana.trade/（站点回链官推，已可 Create/Swap）与 https://vana.nearvana.trade/（VANA 安全检查）。仅测试网，无主网打新/免费 mint 窗口。已进 userFollowWatch。

## DeepSeek 未收录 / 未送审

- 本轮送审 2 个均收录，dsSkipped 为空。
- pilyears：3 万粉、6 万帖的 airdrop-alarm 互动号（资料栏 t.me/airdropalarmm），不是 UNSOLVABLE 谜题 mint 官方，未送审。
- Anonbotcoin：已在库 anoncoin（@anoncoinit）的资讯号，本窗只转「Building on DogeOS」，未送审。
- BTRFLYely：R1849 已 skip 的非官方 mascot，不重审。
- silent 窗 $GREENDILDO / 同类喊单，未送审。

## 在库进度（不重推）

- microfrens：官号 11:30 CST 宣布 Public Mint is LIVE，5 Hour Window（约 11:30–16:30 CST），铸造页 OpenSea ETH。此前记录为付费 0.0015 ETH；持有 ≥3 枚的免费 WL/快照是另一条规则，不是对公免费 LIVE。尚余约 5 小时，未进入 ≤2h，不重推。待约 14:30 CST 进入 ≤2h 再报。已把卡片改为 live。
- polyrob：官号 11:00 CST 再申 0.033 ETH、无名单、每钱包不限，关闭仍为 2026-11-16 01:12 CST，约 13.5 小时后，尚未 ≤2h。已在库 live，不重推。
- usegnomon：官号续写定位，无部署/开窗，已通知不重推。
- echofun：再提醒核验 chain ID 56，已是 live 铸造提醒，非新窗。
- elysiasealed：续报 FOOK/PLANO 成交统计，非新开窗。
- qtronlaptops / hood-turtle / hood-bitz / umbrapad / elyver-xyz / gloopix / coinfin / hokori-quantum / thedawgzrh：MUST 1h 窗无新开窗。qtronlaptops 11-16 01:00 CST、polyrob 关闭 11-16 01:12 CST、BITBOTZ Monday 11-16、hood-turtle 开铸 11-17 22:15 CST 均尚未 ≤2h，已通知过的不重推。

## 关键词 / mentions 摘记

- 薄栏 6 条独立 KW（LayerZero / Tape/电路 / GIWA / DogeEVM / BTC / Starknet）与核心栏 5 条 KW 本轮均已跑全。
- 台子/Meme KW 命中 @useXFee 官宣与 @nearvanapad，因而 admitVerify 一次批量 from:useXFee OR from:pilyears OR from:nearvanapad OR from:Anonbotcoin（未分页）。
- mentions：Tape 多为社区口号、GIWA 见 Squid 测试网周报、BTC 为 ShieldedNaka 成交客诉、Starknet+DogeEVM 基本是噪音；未见新的可操作挂靠官号。

## 推送

- 本地已跑 `scripts/sync_docs_panel.sh`。commit 后推 main：`data.json` + `docs/data.json` + `RESULT_R1850.md`。面板 https://reboot7454.github.io/early-scout/
- notify=true：真新收录 usexfee 与 nearvanapad。

## 未做 / 交接

- 未自动 mint。本轮 2 个候选送 DeepSeek（2 收 / 0 跳），dsFallback=false。
- search_users 仍不可用；silent 已用 mentions 路径跑完台子/Meme 栏。
- lastFullAfterReset=R1843。UF cursor=1491（下一 walk 从 1492 起，startHandle=liquidlootgg）。mentionsNext=LayerZero / Elysium+kinetiq / mining-squeek+Nutshell / BN Agent pads+STARX。freeMint 分片 nextStart 46→66；agentPad / bnAgent / elysium nextStart 未改（730 / 169 / 283）。
- 待临近 ≤2h 再报：microfrens 对公窗约 14:30 CST 进入 ≤2h（关闭约 16:30 CST）、qtronlaptops 2026-11-16 01:00 CST、polyrob 关闭 2026-11-16 01:12 CST、BITBOTZ Monday 11-16、hood-turtle 开铸 2026-11-17 22:15 CST。
