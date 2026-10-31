# RESULT R1004

```json
{
  "round": 1004,
  "mode": "tight-quota-full-scan",
  "completedAt": "2026-10-31 20:38 CST",
  "timezone": "Asia/Shanghai",
  "xReads": 26,
  "remainingBefore": "41/1000",
  "remaining": "11/1000",
  "notify": true,
  "notifyReason": "≤2h可操作窗：SAFU 21:00(~0.4h)、MEH 21:00(~0.4h)、Frogs 21:30(~0.9h前2000免费)；无真新收录",
  "alertMessage": "【early-scout R1004｜notify=true】≤2h：SAFU 21:00(~0.4h Tier1 1U 付费只报)、MEH 21:00($1 付费只报)、Frogs 21:30(前2000免费)；免费LIVE续：GLYPHMIND/SnakeId/SIEGE；付费只报：FISTAGENT/BOTAI；本轮无真新收录。面板：https://reboot7454.github.io/early-scout/",
  "alert": "【early-scout R1004｜notify=true】≤2h：SAFU 21:00(~0.4h Tier1 1U 付费只报)、MEH 21:00($1 付费只报)、Frogs 21:30(前2000免费)；免费LIVE续：GLYPHMIND/SnakeId/SIEGE；付费只报：FISTAGENT/BOTAI；本轮无真新收录。面板：https://reboot7454.github.io/early-scout/",
  "newAdmits": [],
  "newIds": [],
  "newCount": 0,
  "skipped": [
    {
      "id": "mobster_meme",
      "why": "handle Not Found this round"
    },
    {
      "id": "starx_xlayer",
      "why": "handle Not Found；改用@lumora_agent mentions"
    },
    {
      "id": "fortune-sigil",
      "why": "关键词见分享帖但无独立官推可核，跳过admit"
    },
    {
      "id": "dantapixelnft",
      "why": "库内已有danta，付费相LIVE软刷不重复新收"
    },
    {
      "id": "gang-mentions-noise",
      "why": "gang mentions多为抱怨/互动无新挂靠mint"
    },
    {
      "id": "squeek-mentions-noise",
      "why": "squeek mentions社区互动无新官号"
    },
    {
      "id": "tape-mentions-empty",
      "why": "Tape mentions窗内无新挂靠"
    },
    {
      "id": "lumora-mentions-empty",
      "why": "lumora/STARX mentions窗内0"
    },
    {
      "id": "flap-dns-hijack-noise",
      "why": "flap mentions含第三方安全警报噪音，无新挂靠mint"
    }
  ],
  "coverage": {
    "tenLanes": true,
    "userFollowSoft": true,
    "keywords": true,
    "keywordsTenCols": true,
    "mentionsChains": [
      "BN/gangdotfun",
      "Tape(TapeAIAgent)",
      "squeek/Nutshell",
      "STARX/XLayer(lumora)",
      "BTC/ShieldedNaka",
      "GIWA",
      "DogeEVM",
      "Starknet",
      "Zero/Arc/flap",
      "Elysium(抽1 Enter_Elysium)"
    ],
    "notes": "额度紧(41→11)：UF soft优先点名+≤2h(SAFU/MEH/Frogs/Glyph/FIST)→关键词合并EN+CN十栏→mentions轮换子集等力；Discord deferred=false(R1003刚补跳过)；软债canton/glaze/tokenWorks lastChecked已刷；无真新admit"
  },
  "watchBugs": [
    "bitcoin-frogs-agent→UF+agentPadWatch+freeMintWatch+bnAgentWatch",
    "dropminters→UF+agentPad+agentMining+freeMint+bnAgent+mining(re-ensure)",
    "botai-meme→UF+agentPad+agentMining+freeMint+bnAgent+mining(re-ensure)",
    "snakeidbnb→agentPad+freeMint+bnAgent"
  ],
  "discordPeekDeferred": false,
  "discordPeekNote": "R1003刚补，本轮跳过",
  "dsFallback": false,
  "dsModel": "deepseek-flash",
  "thinking": false,
  "push": {
    "ok": null,
    "sha": null
  },
  "panel": "https://reboot7454.github.io/early-scout/",
  "le2h": [
    {
      "id": "safu-fund-bnb",
      "note": "SAFU mint 21:00CST ≤2h (~0.4h); Tier1 1U paid report-only; safufund.live"
    },
    {
      "id": "mehcat-bnb",
      "note": "MEH mint 21:00CST ≤2h (~0.4h); $1; CA 0x2149…c106 live 0/10k"
    },
    {
      "id": "bitcoin-frogs-agent",
      "note": "Frogs mint 21:30CST ≤2h (~0.9h); free first 2000; CA 0xd9e0…0131"
    }
  ],
  "softUpdates": [
    "glyphmind free LIVE ~7000/10k fol62",
    "fistagent paid 1U LIVE ~3209/10k",
    "dropminters still coming soon",
    "botai-meme fair mint LIVE",
    "snakeidbnb free-first LIVE ~7440/10k",
    "siege free LIVE",
    "pixelblobsnft Elysium free-mint road mainnet",
    "elysiumant Market live testnet"
  ],
  "summary": "SAFU、Frogs、MEH 将在21:00-21:30开铸，均为2小时内窗口；GLYPHMIND、FISTAGENT、BOTAI、SnakeId、SIEGE 免费或公平铸造进行中；DropMinters 未上线；无真正新收录。",
  "remoteVerified": false
}
```
