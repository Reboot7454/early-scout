# RESULT R976

```json
{
  "round": 976,
  "mode": "full-scan",
  "completedAt": "2026-10-31 12:02 CST",
  "xReads": 32,
  "remaining": "658/1000",
  "remainingBefore": "687/1000",
  "notify": true,
  "alertMessage": "🔔2小时内新增：0粉新号 HyperliqPad 今日LIVE——Hyperliquid 杠杆 HYPE meme 发射台，已放 pump CA；Monster Society RH 今日 mint（Robinhood 链1111 NFT，已上 OpenSea）；另 Discord α 补漏 day-zero-drop / 3f3rwefwf——面板：https://reboot7454.github.io/early-scout/",
  "newAdmits": [
    {
      "id": "hyperliqpad",
      "name": "HyperliqPad",
      "handle": "@UseHyperLiquid",
      "why": "0粉新号今日LIVE：Hyperliquid杠杆HYPE meme发射台（跨Solana/HyperEVM、最高10x），已放pump CA；官推+站 hyperliqpad.fun；DS overall74 admit",
      "score": 74,
      "focus": false,
      "le2h": true
    },
    {
      "id": "monster-rh",
      "name": "Monster Society RH",
      "handle": "@MonsterRH_",
      "why": "Robinhood链1111 NFT今日mint day；OpenSea已上；官推~4k粉；DS overall68 admit",
      "score": 68,
      "focus": false,
      "le2h": true
    },
    {
      "id": "day-zero-drop",
      "name": "day-zero-drop",
      "why": "remote Discord α 补漏（同轮 770f142 已入库）；本轮合并保留",
      "source": "discord-alpha-remote",
      "focus": false
    },
    {
      "id": "3f3rwefwf",
      "name": "3f3rwefwf",
      "why": "remote Discord α 补漏（同轮 770f142 已入库）；本轮合并保留",
      "source": "discord-alpha-remote",
      "focus": false
    }
  ],
  "skipped": [
    {"id": "miua-fun", "why": "DS admit:false overall55；薄信息/早期过噪"},
    {"id": "magmarra", "why": "Agent ID系但无官推/X handle NF；缺硬门槛"},
    {"id": "pixel-zodiac", "why": "无官推"},
    {"id": "sloth-aiuki", "why": "telegram-only Agent ID；无官推跳过"},
    {"id": "known-NF", "why": "mobster_meme/starx_xlayer/TapeFractal 本轮跳过（R975已NF）；Leeonmort 本轮NF"}
  ],
  "coverage": {
    "userFollowSoftBrush": ["machinedotfun","bscaidrop","PulseLaunchpad","localbottomcom","NutshellMarkets","squeekchain","gangdotfun","pipfun_xyz","Ptahtrade","ComputeRollLabs","flapdotsh","dotaipad","yinghubnb","Enter_Elysium","kinetiq_xyz","AgentKinetiq","GIWA_by_Upbit","DogeOS","ShieldedNaka","listendotmoney"],
    "userFollowSkippedNF": ["mobster_meme","starx_xlayer","TapeFractal","Leeonmort"],
    "requiredWatches": ["userFollowWatch","agentPadWatch","kinetiqWatch","miningWatch","tapeWatch","giwaWatch","btcPrivacyWatch","starknetWatch","flapPadWatch"],
    "keywordsTenCols": true,
    "mentionsCoverage": ["Elysium/kinetiq","Tape","GIWA","Zero/DogeEVM","Starknet","BTC privacy","flap/Irys/Full.fun/Arc","BN Agent pads","squeek/Nutshell","STARX/X Layer"],
    "bnAgentWeb": ["suan.bid","bnagent.onrender.com","agentcity.uk","nftcalendar free-mint lists"]
  },
  "keywordsTenCols": true,
  "userFollowDone": true,
  "mentionsCoverage": ["Elysium/kinetiq","Tape","GIWA","Zero/DogeEVM","Starknet","BTC privacy","flap/Irys/Full.fun/Arc","BN Agent pads","squeekchain/NutshellMarkets","starx_xlayer/X Layer"],
  "discordPeekDeferred": true,
  "dsUsage": {
    "model": "deepseek-flash",
    "batchScore": 3,
    "admitted": 2,
    "alert": 1,
    "fallback": false,
    "note": "day-zero-drop/3f3rwefwf came from remote DC-alpha commit 770f142; merged not re-scored"
  },
  "watchBugsFixed": ["anemospad→UF", "anemospad→agentPad", "agentcityuk→UF.accounts", "cappybara_fun→UF.accounts", "agentic-pixels→agentPad.candidateIds"],
  "notes": [
    "full-scan remaining≫200 (started ~687)",
    "paid Agent ID mint report-only; no auto-mint",
    "no re-alert R971–R975 items (agentcity-uk/cappybara/anemospad/agentic-pixels/…)",
    "merged with concurrent remote R976 DC-alpha (770f142): day-zero-drop + 3f3rwefwf",
    "soft signals in-lib already: GANG Flywheel V2, Pulse MM, squeek Sepolia, ComputeRoll CRL, bitcointapes indexer, ShieldedNaka secondary, torpor Elysium, deuslaunch/Ammora GIWA",
    "hard ban focus:true on new admits; dual-write links.x+links.twitter",
    "discordPeekDeferred=true (no browser this round; remote DC alpha already landed separately)"
  ],
  "commit": "4a9c819",
  "pushOk": true
}
```
