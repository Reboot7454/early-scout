# Early scout R457
Fired ~2026-10-24 14:55 CST. meta.round was 456 → this round 457.
Prior R456: admitted stonkemon/stray-society/peryn; soft-refreshed sprite-fun(~5.3h)/stonks-pad(10/26)/anthrobit/pipfun/TapeSurge+AMA/Elysium11/09; notify=true; discordPeekDeferred; xReads=20; push d287cad.
Watch: sprite-fun live was 20:00 CST today — check if live (~6h past); stonks-pad 10/26; Elysium mainnet 11/09; Zero/lzATLAS 11/30; TapeSurge AMA tonight 22:00 CST.

## Goal
Run one early-alpha scout round; refresh https://reboot7454.github.io/early-scout/ (Reboot7454/early-scout). Earliest operable first. Workdir `/workspace/early-scout/`. `git pull` first. Push with gh only `data.json` + ROUND457_RESULT.json (+ this DISPATCH) to main.

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
flap: @StonksPadsh @flapdotsh → 台子 Launchpad/flap; flapPadWatch; ≤2h notify.
Irys: @spritefun_xyz @irys_xyz → 台子 Launchpad/Irys; irysPadWatch.
BN Agent: @dotaipad @yinghubnb @Ptahtrade @gangfunmeme @agentpunkid @pipfun_xyz + peers; tags Binance Agent钱包+AI Agent+Launchpad; agentPadWatch.
Agentic trading: @listendotmoney; AI Agent/Agentic Trading; agentTradingWatch.
Agent mining: @TracNetwork @fitzyOG; agentMiningWatch; old projects with NEW plays still admit.
GIWA/Zero/DogeEVM watches; Zero 11/30. BTC privacy @ShieldedNaka @banknotes_btc. Starknet meta.starknetWatch. X pads @StarcatOKX @NinetailsTrade. PaperBird @paperbird_lol. Soft refresh Canton/Glaze/TokenWorks lastChecked.
New admits need Twitter. LZ unverified → 台子. discordPeekDeferred=true (no browser).

## X ~20 reads
CallDynamicTool namespace x: search_posts_all (start_time last 30-40m UTC, recency), get_users_by_username(s), get_users_posts sparingly.
Keywords: agent mining, AI mining, PoW mining, free mint, testnet live, fair launch, launchpad, agent launchpad, agent CLI launchpad, agent-native, Agent ID, agentic wallet, Binance agent wallet, agent钱包, bn agent, 内盘, agentic trading, vibe trading, pipfun, stonkspad, flap.sh, flapdotsh, spritefun, irys launchpad, 挖矿, 打新, GIWA, DogeOS, Zero, Elysium, Kinetiq, Starknet, Ordinals, Monad, Ink, Robinhood, BNB, Irys, TapeOut.
Count xReads.

## Data
candidate.round = first admit only. Clear prior newThisRound; meta.newThisRound == newThisRound == roundNAdded for 457 ids. links.x AND links.twitter. meta.round=457; updated/lastScout CST. Soft-refresh watches. Peek gaps only.

## Push
git add data.json ROUND457_RESULT.json R457_DISPATCH.md; commit; git push origin main. Push fail → notify=true.

## notify
true if new admits OR ≤2h schedule OR push fail → Chinese alert + panel URL. Else false.

## RESULT shape
See ROUND456_RESULT.json. Write ROUND457_RESULT.json similarly.

## Report
Final message = exact ROUND457_RESULT.json + push status. If notify=true include full Chinese alert for parent WakeParent.
