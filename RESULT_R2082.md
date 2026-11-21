# 早期打新雷达 RESULT R2082

- 时间：写盘时以 data.json meta.lastScout 为准（Asia/Shanghai）：2026-11-21 11:40:05 CST
- 模式：常规 ample X 雷达（非 08:00 CST 后首轮全量补扫；lastFullAfterReset=R2072）
- 写盘前远程：已是 R2081（commit ebf0119，lastScout 2026-11-21 11:12:19 CST）。本路升为 R2082。
- 通知：notify=true。新收录 plastic-only（@plasticonlyclub）。不是已确认免费 mint LIVE / 已确认免费登记开放。

## X 额度

- remainingBefore **787**
- xReads **30**（主路径 29 + silent 1；因瘦栏 24h 覆盖略超 softCap 28，与 R2081 相同处理）
- remainingAfter **757**
- 分解：UF 3 + MUST 2 + THIN official 6 + KW_THIN 30m 6 + KW_CORE 5 + KW_GAPS 1 + MEN 2 + KW_THIN24 4 + SILENT 1 = 30
- 无翻页、无 getUsers、无重复确认读
- 十栏关键词：已跑全
- userFollow：已刷完本片

## userFollowWatch

- 起点 1483 @NoveElysium → 终点 1533 @Elyzor_nft；kept 50，walk 50，NF_skip=0，wrap=false；firstKept @NoveElysium，lastKept @ChainPadApp
- 片内命中多为已在库 @GIWALAUNCHPAD，无真新官号
- 下轮从 1533 @Elyzor_nft

## 新收录 / 首次窗口

- 新收录：plastic-only / @plasticonlyclub / https://plasticonly.netlify.app/
  - 2026-11-02 20:28 CST 建号，118 粉、593 帖，verified blue；官网与官推互指
  - 自称以太坊 10,000 份生成 PFP，Mint date/price TBA，OpenSea soon
  - 官网有 JOIN WL（页面写 WL opens soon）和 FREE RACK 预登记表单（自称免费阶段、只需钱包、日期 TBA）。本轮未实测表单是否已开放
  - 本轮官帖 https://x.com/plasticonlyclub/status/2123981472943993101 是为朋友项目 @fomofuzz_lol 宣传允许名单，不是自身开铸官宣
  - 不是已开铸免费 mint LIVE，也不是已确认免费登记开放
  - DeepSeek admit，overall 55，focus=false，已进 userFollowWatch + freeMintWatch
- 首次窗口：无（bons-world 白名单 <=2h 仍有效，但 R2081 已提醒且截止未改，不重推）

## 库内续更（不重推）

- TapeAI：官帖 11:29 CST（https://x.com/TapeAIAgent/status/2123982140719374517）确认「今晚发射」，并说明 TapeUP 加速码可提前释放预存购买额度。仍无精确开盘钟点，尚未 <=2h。11-21 经 TapeUP PoB 发射窗此前已在 R2028/R2022 记录，不重推
- bons-world：白名单仍 13:00 CST 截止（约 1.33h，仍 <=2h），今晚 20:00 CST 免费 WL mint 计划不变。本轮 MUST 仍是旧帖 2123959584767324392。R2081 已提醒，不重推
- MARIO：免费 mint 仍 LIVE，关窗仍 23:00 CST（约 11.33h）；官称仍 847 minted。R2076 已提醒，不重推
- Hood Drive：本轮无新官帖（仍是 allowlist-updated 2123971270081757597）。开铸仍 2026-11-22 01:00 CST（约 13.33h）。未再拉官网/OpenSea，不重推

## Watch 修复

- 库内 casebookduel（@casebookduel，R2080 新收）此前不在任何 Watch，已补进 userFollowWatch
- 新卡 plastic-only 入库同时进入 userFollowWatch + freeMintWatch

## 看见但未收

- @sotanoxyz：2026-11-20 建号，7 粉 9 帖，无官网，仅一条关于 Base 上股票代币的回复，证据不足，本轮不收
- @fomofuzz_lol：仅在 @plasticonlyclub 官帖中被宣传（自称 11-30 19:00 CET 公售、免费仅 gas）。本轮不是发帖作者，未做额外 X 核验，硬禁误判无官推，未收录

## mentions / 瘦栏 / silent

- mentions：LayerZero + GIWA（均 25 触顶未翻页）。optional MEN_TAPE / squeek 未跑，以免继续超过 softCap。下轮 Tape，然后 squeek+Nutshell / BN Agent pads
- 瘦栏 30m：LayerZero 0、Tape 13、GIWA 3、DogeEVM 6、BTC 1、Starknet 1 → 同一轮 24h 补搜 LZ / GIWA / BTC / Starknet（均 25 触顶未翻页）
- silent：GIWA 25 触顶未翻页，无新收。下轮 DogeEVM（勿按模跳步）

## Discord Peek

- discordPeekDeferred=true，loginOk=false
- computerUse 遇登录墙，未填凭证、未扫消息
- landed：https://discord.com/login?redirect_to=%2Fchannels%2F1502958818865188956%2F1549303534263214160 （#alpha-1-backup）
- cutoff 仍用 R2080：alpha-3 10:49 / backup 08:29 / smart 10:00 / alpha-1 09:39 CST（backup 最落后）
- 须父代理请用户在盒子 Chrome 登录 Discord 后同轮补 Peek，禁止堆到下几轮
- 11/15-11/18 积压仍不在增量范围

## 面板

- 只推 data.json + 本 RESULT 到 Reboot7454/early-scout main
- https://reboot7454.github.io/early-scout/

