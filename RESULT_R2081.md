# 早期打新雷达 RESULT R2081

- 时间：写盘时以 data.json `meta.lastScout` 为准（Asia/Shanghai）
- 模式：常规 ample X 雷达（非 08:00 CST 后首轮全量补扫；`lastFullAfterReset=R2072`）
- 写盘前远程：已是 R2080（commit 87f1567，Discord 增量收录 casebookduel，lastScout 2026-11-21 10:53 CST）。本路升为 R2081。
- 通知：`notify=true`。无新收录。库内 `bons-world`（@bons_world / https://bons.world）**首次核到可操作窗口** + 白名单截止 **≤2h** + 自称即将免费 WL mint（尚未开铸 LIVE）。

## X 额度

- remainingBefore **817**（首条搜索页脚 816 left）
- xReads **30**（主路径 29 + silent 1；主路径因瘦栏 24h 覆盖略超 softCap 28）
- remainingAfter **787**
- 分解：UF 3 + MUST 2 + THIN official 6 + KW_THIN 30m 6 + KW_CORE 5 + KW_GAPS 1 + MEN 2 + KW_THIN24 4 + SILENT 1 = 30
- 无翻页、无 getUsers、无重复确认读
- 十栏关键词：已跑全
- userFollow：已刷完本片

## userFollowWatch

- 起点 1433 @tell_markets → 终点 1483 @NoveElysium；kept 50，walk 50，NF_skip=0，wrap=false；firstKept @tell_markets，lastKept @wickoptdesk
- 本片无真新官号
- 下轮从 1483 @NoveElysium

## 新收录 / 首次窗口

- 新收录：无
- 首次窗口：`bons-world` / @bons_world
  - 官帖：白名单 2026-11-21 13:00 CST 截止（≤2h）；今晚 20:00 CST 免费 WL mint；23:00 CST BONS 上 Pons；23:30 CST 开直播；次日 01:00 CST 公售
  - OpenSea [bons-genesis](https://opensea.io/collection/bons-genesis) 本轮 0 铸 / 0 持有，**不是已开铸 LIVE**
  - 资格自称：在 bons.world 登录后赢 Bons Show
  - 已补挂 `freeMintWatch`，`le2h=true`，`focus=false`
  - 第三方看板另列 TEAM 阶段与 CA，本轮未链上复核，不当官宣

## 库内续更（不重推）

- Hood Drive：官帖称 OpenSea allowlist 已更新；官网仍 WL Closed，开铸仍 2026-11-22 01:00 CST（约 14h），OpenSea 供应 0
- MARIO：免费 mint 仍 LIVE，关窗仍 23:00 CST（约 12h）；官帖代币仍 coming soon（官网另写 SUPER is live，未当新窗）
- Kismo：`/genesis/` 仍 TBA；首页 Live 是栏目徽章，不是开铸确认
- Tribe：白名单申请仍开，铸价未核到
- KRYOSHI：开铸仍 11-27 21:00 CST
- Fragfun：官帖补 CA `5WzTW19zYvb7TejCFdqHcyn5gb6yamsnoxnd8Ujopump`（未链上复核）；R2076 已报台子 LIVE，不重推
- Cipher Saints：称今晚稍晚会更新 mint 日期，未见确认新窗
- Kinetiq Toons / Robin Yield：本轮 MUST 窗口未见新官帖，未再拉 OpenSea 进度，不重推

## Watch 修复

- `bons-world`、`hood-drive` 补进 `freeMintWatch`
- 库内 `betonbons`（@betonbons）此前不在任何 Watch，已补进 `userFollowWatch`

## 看见但未收

- @HOODZNFTs：仅被第三方提及自称 RH 5555 / GTD free，本轮不做额外 X 核验，未收录
- @memepad_lol：约 43 天、教育向 bonding 帖，证据不足

## mentions / 瘦栏 / silent

- mentions：squeek+Nutshell（0）+ BN Agent/pads（25 触顶未翻页）；optional MEN_LZ 未跑。下轮 LayerZero，然后 GIWA+Zero / Tape
- 瘦栏 30m：LayerZero 0、Tape 13、GIWA 3、DogeEVM 7、BTC 0、Starknet 0 → 同一轮 24h 补搜 LZ / GIWA / BTC / Starknet（均 25 触顶未翻页）
- silent：Starknet 4 帖，无新收。下轮 GIWA（勿按模跳步）

## Discord Peek

- `discordPeekDeferred=true`，`loginOk=false`
- computerUse 遇登录墙，未填凭证、未扫消息
- cutoff 仍用 R2080：alpha-3 10:49 / backup 08:29 / smart 10:00 / alpha-1 09:39 CST（backup 最落后）
- **须父代理请用户在盒子 Chrome 登录 Discord 后同轮补 Peek**，禁止堆到下几轮
- 11/15–11/18 积压仍不在增量范围

## 面板

- 只推 `data.json` + 本 RESULT 到 `Reboot7454/early-scout` main
- https://reboot7454.github.io/early-scout/
