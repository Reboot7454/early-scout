# RESULT R2280

- 时间：2026-11-27 15:17 CST（Asia/Shanghai）
- 轮次：原计划 R2279，但 origin 在本轮 enrichment 期间已推送 R2279 X 雷达（a3e77d6，SNOWBALLz/Mined/Nerby/No Mercy Zoo）。按规则 bump 为 R2280，未覆盖更高远程轮次。
- 仓库：Reboot7454/early-scout，面板 https://reboot7454.github.io/early-scout/
- 模式：Discord alpha 每小时补漏（本号只做 DC，不跑全量网页雷达，未开浏览器）
- notify=true（真新 4 项，全部台子/Meme。不是免费 mint。无 ≤2h。Outrider 自称 $OUTR 发射为今日 15:00 UTC / 23:00 CST，距开窗约数小时，未到 ≤2h，不按开盘重推以外的提前告警单独处理）
- DeepSeek：HTTP 401 invalid api key（request_id 108be5b8-2e17-4a9f-9450-294761bd1311），判断/文案/打分为本地兜底（dsFallback），未改用高成本模型
- 登录：loginOk=true，spideyPosting=true，本轮增量 Peek 四频道均越过各自增量 cutoff，无封顶，gapIncomplete 仅指更早积压未补
- 扫卡：合并 30 张（unique new handles 24，另高粉跳过 @pexelexchange 21811）。newestByChannel：alpha-3 15:02、backup 14:39、smart 14:37、alpha-1 14:49。增量 cutoff：alpha-3 14:12、backup 14:09、smart 14:07、alpha-1 13:42。
- lastSeenByChannel：alpha-3 15:02、backup 14:39、smart 14:37、alpha-1 14:49。本轮未补扫更早积压。积压缺口仍在：alpha-3 11-23 22:55→11-27 05:20；smart 11-23 22:56→11-25 00:25；alpha-1 11-23 22:19→11-25 20:50。backup 已追上。更早 11/15–20 缺口本轮仍不在范围内。
- 清上一轮 newThisRound：snowballz, usemined, nerbyprotocol, nomercyio
- 新收录 4（focus=false，全部 dsFallback）：
  1. nofeeapp / @nofeeapp / 台子/Meme / Robinhood / https://nofeeapp.xyz/ — 昨日建号 5 粉，自称 Robinhood 上零平台费交易 Pons/Uniswap，官网已开；$NFA 未发行、无 CA，产品未实测。
  2. offrouter / @OffRouter / 台子/Meme / Robinhood / https://offrouter.org/ — Robinhood 隐私层，官网与文档已开；自称 CA 本轮 RPC 未核通。DexScreener 市值约 $236k，产品未实测。
  3. sourcebound / @sourceboundHQ / 台子/Meme / Solana / https://sourcebound-ten.vercel.app/ — 今日建号，自称 Solana 新币核查台，官网已开并回链官推；写 12 月 3 日 pump.fun 公平发射，无 CA，产品未实测。
  4. outrider / @outrider_fi / 台子/Meme / Robinhood / https://outrider.business/ — 昨日建号，自称 Robinhood 上 Uniswap v4 区间 callout，官网已开并回链官推；官帖称 $OUTR 今日 15:00 UTC 发射，无 CA，产品未实测。
- 拒收（likely-enrich）：@Woopy_Dog — Solana RPC 核到 CA 2va3NUJtEcPemDYg2N1RgA79rPKGTGGJKo3gTY5zpump（6 位小数，供给约 9.989 亿）；DexScreener pumpswap 市值约 $193k，但交易对创建于 2025-05-18，早于 11-25 官号约 18 个月，已毕业，近 6h 成交很淡，按中后期/旧 meme 新号拒收。
- 其余 19 个新 handle 按预过滤拒收（18+ 垃圾粉、个人/空壳、KOL @cubbieog、空壳 @originalfat22、CoinNow 宣传号 @raskl07）。未给 @coinnowcash 造卡。
- 未改 focus，未把普通补漏卡送进重点条，未进 Elysium 栏。
- push：1b96b5e（1b96b5ebdbc9326ea4e6d7a9dee5a73b316245a8）origin/main，remoteVerified=true。
