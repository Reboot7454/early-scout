# Early scout R459
Fired ~2026-10-24 16:00 CST. meta.round was 458 → this round 459.
Prior R458: admitted velum-swaps/flap-nidie; soft-refreshed sprite-fun(~4.5h)/stonks-pad(10/26)/pipfun/Tape/Elysium11/09; notify=true; discordPeekDeferred; xReads=20; push 23366d9.

## Timing windows (Asia/Shanghai)
- Sprite Fun (@spritefun_xyz) live **today 20:00 CST** — now ~16:00 → ~4h left; ≤2h window starts ~18:00. Soft-refresh; if you see live already or ≤2h, notify.
- StonksPad (@StonksPadsh) live **2026-10-26** on flap.
- TapeSurge / Blonskr AMA tonight **22:00 CST** (~6h) — soft note, not ≤2h yet.
- Elysium mainnet **2026-11-09**; Zero/lzATLAS **2026-11-30**.

## Goal
Run one early-alpha scout round; refresh https://reboot7454.github.io/early-scout/ (Reboot7454/early-scout). Earliest operable first. Workdir `/workspace/early-scout/`. `git pull` first. Push with logged-in gh only `data.json` + ROUND459_RESULT.json (+ this DISPATCH) to main.

## Cost
All admit/score/zone/highlights/whatsNew/alertMessage/summary/dedup → DeepSeek (`DEEPSEEK_API_KEY`, deepseek-flash, thinking ON). Scripts: `scripts/deepseek_chat.py`, `scripts/ds_batch_score.py`. You: pull signals, run scripts, edit data.json, push, RESULT, notify. DS fail → dsFallback.

## Columns
打新｜挖矿｜台子/Meme｜GO盘｜LayerZero｜Elysium｜Tape/电路｜GIWA｜DogeEVM｜BN Agent钱包
Tape tags 电路板/电路NFT/TapeOut ecosystem Tape (NOT Elysium). GIWA/DogeEVM ecosystem/tags. BN Agent tags must include `Binance Agent钱包`. Also BTC+Starknet. zoneOf per app.js. No empty chips. No favorites.

## Hard bans
1. New admits NO focus:true (unless meta.focusIds or squeekchain-class). Else focus:false/omit.
2. Before skip「无独立官推」, verify handle with X get_users_by_username.
3. Equal coverage all columns+chains.

## Must-watch
Kinetiq/Elysium: @kinetiq_xyz @AgentKinetiq @Enter_Elysium → meta.kinetiqWatch. Only On testnet or Announced+deploy. Exclude perpme/branchpoint/outrive. Mainnet 11/09.
Tape: @TapeAIAgent @Blonskr @TapeOutWorld @BEMGoGoGo @tapeupio @FirstoAI @Tape_Pool.
flap: @StonksPadsh @flapdotsh → 台子 Launchpad/flap; flapPadWatch; ≤2h notify. StonksPad live 10/26.
Irys: @spritefun_xyz @irys_xyz → 台子 Launchpad/Irys; irysPadWatch. Sprite Fun live 2026-10-24 12:00 UTC = 20:00 CST today.
BN Agent: @dotaipad @yinghubnb @Ptahtrade @gangfunmeme @agentpunkid @pipfun_xyz @Leeonmort + peers; tags Binance Agent钱包+AI Agent+Launchpad; agentPadWatch (accounts incl @Leeonmort, candidateIds incl xuanwu-sigil).
Agentic trading: @listendotmoney; AI Agent/Agentic Trading; agentTradingWatch.
Agent mining: @TracNetwork @fitzyOG; agentMiningWatch; old projects with NEW plays still admit.
GIWA/Zero/DogeEVM watches; Zero 11/30. BTC privacy @ShieldedNaka @banknotes_btc. Starknet meta.starknetWatch. X pads @StarcatOKX @NinetailsTrade. PaperBird @paperbird_lol. Soft refresh Canton/Glaze/TokenWorks lastChecked.
New admits need Twitter. LZ unverified → 台子. discordPeekDeferred=true (no browser in this executor).

## X ~20 reads
CallDynamicTool namespace x: search_posts_all (start_time last 30-40m UTC, recency), get_users_by_username(s), get_users_posts sparingly.
Keywords: agent mining, AI mining, PoW mining, free mint, testnet live, fair launch, launchpad, agent launchpad, agent CLI launchpad, agent-native, Agent ID, agentic wallet, Binance agent wallet, agent钱包, bn agent, 内盘, agentic trading, vibe trading, pipfun, stonkspad, flap.sh, flapdotsh, spritefun, irys launchpad, Leeonmort, Xuanwu, EX-00, mchain.art, 挖矿, 打新, GIWA, DogeOS, Zero, Elysium, Kinetiq, Starknet, Ordinals, Monad, Ink, Robinhood, BNB, Irys, TapeOut.
Count xReads. Prefer must-watch accounts + keyword search; less pagination.

## Data
candidate.round = first admit only. Clear prior newThisRound (velum-swaps, flap-nidie); meta.newThisRound == newThisRound == roundNAdded for 459 ids. links.x AND links.twitter. meta.round=459; updated/lastScout CST. Soft-refresh watches. Peek gaps only. Empty round chips: don't invent.

## Push
git add data.json ROUND459_RESULT.json R459_DISPATCH.md; commit; git push origin main. Push fail → notify=true.

## notify
true if new admits OR ≤2h schedule OR push fail → Chinese alert + panel URL. Else false.

## RESULT shape
See ROUND458_RESULT.json. Write ROUND459_RESULT.json similarly.

## Report
Final message = exact ROUND459_RESULT.json contents + push status. If notify=true include full Chinese alert for parent WakeParent.
