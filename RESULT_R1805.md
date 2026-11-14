# RESULT R1805（Discord alpha 补漏）

- time: 应用时远程已是 R1804（ff1c7fd，ample X scan，无新收录，2026-11-14 14:05 CST）。本轮 DC 不覆盖既有轮次，记为 R1805。timezone Asia/Shanghai。
- mode: discord-alpha-40。未跑全量六栏网页雷达。
- notify: true（本轮真新 2 张：raidfolk、hwan）。
- 扫卡：lastSeen 之后 51 张 / 48 个独立号（alpha-3-new-accounts 40、alpha-1-backup 1、smart-accounts-tracker 6、alpha-1 4；窗口约 12:42–14:02 CST）。Spidey 仍在 #alpha-1 发卡。cutoffs 来自 R1803 peek（alpha-3 12:40、backup 12:34、smart 12:35、alpha-1 12:23）。alpha3OlderGap 本轮仍不补。
- lastSeenByChannel：alpha-3-new-accounts 14:02、alpha-1-backup 13:34、smart-accounts-tracker 13:44、alpha-1 13:55；lastSeen→2026-11-14 14:02；lastChecked 见 data.json。
- 预过滤：已在库跳过 @0zero_fun、@010101fun；高粉跳过 @pirroh、@jasonmdesimone、@donaldtdaily。其余明显个人号未送审。短名单 6 个走 X 核验 + DeepSeek admit。
- 新收：
  - 打新 @playraidfolk Raidfolk（Robinhood Chain，官网 raidfolk.io，等待名单已开）
  - 台子/Meme @hwandotio hwan（Solana 汇率价差市场，官网 hwan.io，bio 挂 CA）
- 拒收：@scoutymeme（无产品研报号）、@plumbercabal（已开盘普通 pump）、@peacefrogggggg（已放量，约 1545 持仓，非极早期）、@vensa_si（开源芯片 nonprofit，非加密）。
- DS 栏位覆盖：Raidfolk 被标 GO盘，已改为打新（RH GameFi 等待名单，非 GO/AR）。focus 均为 false。dsFallback=false。
- X：get_users_by_usernames×1 + get_users_posts×5（核验短名单），本轮未跑网页雷达/ample 扫描。
- 上一轮 NTR 已在 R1804 X scan 清空，本轮无需再清徽章。
