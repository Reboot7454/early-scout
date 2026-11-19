# 用户点名补挂（R1983b，2026-11-19 22:07 CST）

用户确认后补挂 Watch，并补关键词。未改 `meta.round` / `notify` / `lastScout` / 大 alert 旗。本号不自动 mint。

## 建卡

- `beetleai`（打新，focus=false，status=announced）：宣传号 @CherylB83488，官网 https://beetleai.fun/。宣传帖称 2026-11-19 21:00 CST 开售（8000 份、0.003 BNB/份、仅限 Agent ID，48 小时，售罄自动开池）。站点 Cloudflare 403，开闸与 CA 未独立核验。已入 userFollowWatch + bnAgentWatch + agentPadWatch。付费，不进 freeMintWatch。与 @hostilexyz、库内 DungBeetleAgent 都不是同一项目。
- `hostilexyz`（台子/Meme，focus=false，status=live）：官号 @hostilexyz，官网 https://hostile.xyz/ HTTP 200。meme 配对微型股发射台，资料写 no token，账号 0 帖。已入 userFollowWatch accounts + candidateIds。
- `telemarket`（台子/Meme，focus=false，status=watching）：官网 https://telemarket.org/ 与 Oracle DAO https://telemarket.org/oracle/dao。TON 预测市场，JURY 投票争议结果。站点无官推；X 上 @telemarket 是 2009 年超市号，只把 telemarket 写入 candidateIds，不写 UF accounts。

## 关键词（meta.keywordGaps.r1983b + scripts/x_budget.py）

- 打新栏：beetleai.fun / beetleai
- 台子/Meme 栏与静号 mentions：hostile.xyz / hostilexyz / "microcap stocks" / "stock launchpad" / "stock token" / telemarket.org / Telemarket / "Oracle DAO" / "prediction market"
- 不加光杆 beetle / hostile / stock / oracle / dao / prediction / jury / telegram

## 建卡门槛（用户已确认）

铸造/开售窗若有可指认的官网（含用户点名 URL），即使发帖号不像典型官号、或因 Cloudflare / 页内无回链导致 siteXMutual 不完整，也不要只因此丢弃；应建 watching/live 卡并挂 Watch，付费只报不自动打。仍禁止张冠李戴无关账号当官推。
