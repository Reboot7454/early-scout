# RESULT — 用户点名补收 @saulpink + @fulldotfun

- **time**: 2026-10-24 18:07 CST
- **type**: user-named补收（两号均未在库 → 新 admit）
- **round**: 464
- **notify**: false（父代理自行回用户；本子代理不发消息）
- **newIds**: ["full-fun", "saul-pink"]
- **alreadyInRadar**: false（两号均漏）
- **le2h**: []（$FULL 约周一 10/26，非≤2h）
- **xReads**: 3（get_users_by_usernames + 2× get_users_posts）
- **dsFallback**: false（本补收未跑 DS，按用户点名+X核验直收）
- **discordPeekDeferred**: true
- **blocker**: none

## 核验

### @saulpink
- 存在：显示名 **Saul Pink**，≈12171粉，bio `@PinkEcosystem cat, founder`，站外 pinksale.finance。
- 近帖：2026-10-24「We will launch our FULL official token on Monday. Get your funds ready.」（引用 @fulldotfun）。

### @fulldotfun
- 存在：显示名 **Full.fun**，≈11836粉，2026-09-14 建号，站外 full.fun / t.me/fulldotfun。
- 近帖：2026-10-21 Introducing full.fun（跨链 create/launch/trade memecoins，≈1120万曝光）；已上 Arc；提 RH Chain。

## 为何漏
- `data.json` / HANDOFF / 各 `*Watch` 均无 saulpink、fulldotfun、full.fun、PinkSale 痕迹 → 例行关键词未覆盖 PinkSale/Full.fun 线。

## 动作
- 新 admit：`full-fun` + `saul-pink`（`focus:false`）
- 新建 `meta.fullFunWatch`（accounts + candidateIds）
- HANDOFF 追加补收说明
- 推 main（pull --rebase，无 force）

## 建议例行关键词（父代理 UpdateRoutine）
- `@saulpink` / `Saul Pink` / `PinkSale` / `PinkEcosystem`
- `@fulldotfun` / `Full.fun` / `full.fun` / `$FULL` / `FULL token`
