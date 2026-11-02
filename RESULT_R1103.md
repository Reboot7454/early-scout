# RESULT R1103 — 2026-11-02 ~09:38 CST

- mode: ample
- softCap: 28
- xReads: ≈13
- remainingBefore: 941
- remaining: ≈928
- resetAt: 2026-11-03 08:00 CST
- xQuota: softCap=28 用≈13余≈15；footer remainingBefore≈941→≈928；本轮非 08:00 后首轮（R1100 已是 post-reset-full）；ample pacing UF→必盯/≤2h→十栏KW全量→mentions轮换子集

- newIds: （无）
- admits: 无新收录
- skip:
  - Servobun / MintRadar factory 0x0a1E…（RPC totalSupply≈281 freeLIVE 样）但仅 XiaoMei_laika 报道、无官网/无官推 → 同 NFOX 规则不收
  - UF 新 NF/死号：blindfloor / trytoprint / PlayFarmFi / reynarlabs / world_ygg / deadpacksol(suspended) → 记 NF_skip 不连刷
  - Ptahtrade mentions 全为既有 #ProofOfAgent 互动，无新挂靠项目
  - theidmfun 已在库(R831)；zakehowell/Squeek Pulse 为工具号非打新卡
- updates:
  - agent-harvest(**关键** pause→09:17:55CST 已过；RPC freeOpen=1 phase=6 LIVE；tm≈3328 free≈2963 paid≈360 phaseMinted≈466；较 R1102 pause 期猛增 → le2h=true)
  - nullsector(ts≈1600/4321 freeLIVE；较≈1418 续增)
  - onimaru(tm≈1000 freeMinted≈993/1000 近罄未变)
  - baoracle(tm≈6744；较≈6394 续增)
  - rootlinks(tm≈371 free≈369；较≈346 续增)
  - pixcade(tm≈1548 free罄1500 → paidLIVE)
  - jiepanfun(tm≈167)
  - shalinggou(watching；RPC stats全0；距今晚19:00CST≈9.3h 非≤2h)
  - agent-yyds(watching；链上开售戳=2026-11-02 20:30 CST 已确认；非≤2h)
  - agent2(upcoming；sold≈0；今晚20:00CST；非≤2h)

- le2h: true（agent-harvest phase6 freeOpen LIVE）
- notify: true
- alert: early-scout R1103告警：Harvest phase6免费窗已开(freeOpen=true) tm≈3328 free≈2963；nullsector≈1600；onimaru free≈993近罄；baoracle≈6744；rootlinks≈371；shalinggou仍等19:00CST；面板 https://reboot7454.github.io/early-scout/

- ufCursor: 42→70
- userFollowShardDone: true（42→70；点名 @mobster_meme @machinedotfun @bscaidrop @PulseLaunchpad @localbottomcom @NutshellMarkets @starx_xlayer 仍 NF_skip 不连刷仅记）
- tenLanesKeywords: true（合并十栏近30min：Agent mining/free mint/fair launch/launchpad/Agent ID/Binance agent/AIDROP/bscaidrop/PulseLaunchpad/$PULSE/Local Bottom/Nutshell/squeek/STARX/X Layer/TapeOut/GIWA/DogeEVM/Starknet/Elysium/挖矿/打新/GO盘 等；无强新录取）
- mentionsChains: Elysium/kinetiq · Tape/TapeAIAgent · GIWA · squeek/X Layer · BN pads(Ptah)；无强新挂靠录取（Elysium/Tape/GIWA/squeek 无新 affiliate；Ptah 既有互动）
- watchBugsFixed: 无（跟进卡均已在 Watch；本轮无新 admit 需接入）
- Discord: discordPeekDeferred=true（无登录，未尝试登录）
- push commit: （待写）
- NF_skip: TapeFractal; Leeonmort; computeroll; PulseLaunchpad; machinedotfun; mobster_meme; starx_xlayer; +deadpacksol; blindfloor; trytoprint; PlayFarmFi; reynarlabs; world_ygg
- softDebt: 已刷新各 Watch lastChecked（userFollowWatch/freeMintWatch/bnAgentWatch/agentPadWatch 及十栏相关 Watch）
- deferredFullScan: false（本轮 ample 常规轮，非重置后首轮）
- notes:
  ample 硬序：UF软刷(42→70) → 必盯/≤2h HTTP+RPC（Harvest 核验优先） → 十栏KW全量 → mentions 轮换子集（补 Elysium/Tape/GIWA/X Layer·squeek/BN pads） → Discord deferred。
  Harvest freeOpen 恢复 LIVE → notify=true（无新 admit 亦告警）。
  Servobun 因无官推/官网硬门槛跳过。
  建议下轮：续盯 Harvest 是否再 pause；onimaru free 是否罄；shalinggou→19:00 / YYDS→20:30 / AGENT2→20:00 临近≤2h 升档；nullsector/baoracle/rootlinks 进度。
