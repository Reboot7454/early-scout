# RESULT R2286

- 时间：2026-11-27 17:20 CST（Asia/Shanghai）
- 仓库：Reboot7454/early-scout，面板 https://reboot7454.github.io/early-scout/
- 模式：Discord alpha 每小时补漏（本号只做 DC，不跑全量网页雷达）
- notify=true（真新 4 项：Pivotra、Alastor、HALFKEY 在台子/Meme；Astromine Miners 在挖矿。官称 Astromine 首铸免费但未实测，未标 freeMintLIVE。无 ≤2h 新开铸。）
- DeepSeek：HTTP 401 invalid api key（request_id f955cdc6-9024-42da-b12c-74677e156cd7），判断/文案/打分为本地兜底（dsFallback），未改用高成本模型
- 登录：loginOk=true，spideyPosting=true，本轮增量 Peek 四频道均越过各自增量 cutoff，无封顶，gapIncomplete 仅指更早积压未补
- 扫卡：合并 38 张（unique handles 30，已在库 0）。newestByChannel：alpha-3 17:03、backup 16:39、smart 16:18、alpha-1 17:03。增量 cutoff：alpha-3 15:59、backup 15:54、smart 14:37、alpha-1 15:55。
- lastSeenByChannel：alpha-3 17:03、backup 16:39、smart 16:18、alpha-1 17:03。本轮未补扫更早积压。积压缺口仍在：alpha-3 11-23 22:55→11-27 05:20；smart 11-23 22:56→11-25 00:25；alpha-1 11-23 22:19→11-25 20:50。backup 已追上。更早 11/15–20 缺口本轮仍不在范围内。
- 清上一轮 newThisRound：无（候选 flag 已空）
- 新收录 4（focus=false，dsFallback）：
  1. pivotra / @pivotratech / 台子/Meme / Robinhood / https://pivotra.tech/ — 昨日建号（8粉），站点 pivotra.tech 自称一只 OpenAI 兼容 API 按成本/延迟/质量路由模型；$PIVOT 官宣在 Robinhood Chain 上线，CA 已核到 Pivotra/PIVOT 10 亿 18 位，DexScreener 暂无交易对，产品未实测。
  2. alastor / @Alastor_rbh / 台子/Meme / Robinhood / https://alastor.tech/ — 昨日建号（0粉），站点 alastor.tech 自称在 Robinhood Chain 上用 HUNTER/JUDGE 代理核验 AI 或代币经济断言并出具错误证明，官称创世无代币、SIWE 免费提交，产品未实测。
  3. astromine-miners / @AstromineMiners / 挖矿 / BNB / https://astromine-miners.pages.dev/ — 今日建号（0粉），站点 astromine-miners.pages.dev 自称 BNB 上 1 万个矿工 NFT，持有 Binance Agent ID 可免首铸并按档挖 $ASTRO；NFT/$ASTRO/挖矿合约已在 BSC 核到代码，铸造与挖矿未实测，勿与无关的 astromine.io 混淆。
  4. halfkey / @Halfkeyxyz / 台子/Meme / Solana / https://halfkey.xyz/ — 今日建号（33粉），站点 halfkey.xyz 自称 Solana 与门罗的原子互换已在主网 capped beta；$HALFKEY CA 已核到约 9.50 亿/6 位，pumpswap 市值约 $12.2k、流动性约 $6.6k，交易对今日 16:53 CST 创建，互换未实测。
- 拒收（核验后）：@AsgardHashworks 为 2021 年挖矿软件小站；@maroo_io 为 1 月起的韩国 L1、2935 粉，非极早期；@Fusesocialapp 官推已被冻结；@HTXLive_bot 为火币播报机器人；@gyjujiweb、@THEDEXDEVLOL 为空壳/噪声；@SrLontroso 为个人号。其余新 handle 按预过滤拒收（个人号、空简介、互粉号）。未给已冻结的 Fuse Social 造卡。
- 未改 focus，未把普通补漏卡送进重点条，未进 Elysium/LayerZero 栏。Astromine 勿与无关的 astromine.io（AstroMine.ai 2022 航天站）混淆。Pivotra DexScreener 本轮无交易对，仍以 Robinhood RPC 核验为准。

- 推送：origin/main 0de456d（0de456d8f6c3e58273ff7af65d7feb53c576556f），remoteVerified=true
