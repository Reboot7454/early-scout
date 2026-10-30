# Panel fix · R912 Squeek Companion invisible

- **rootCause**: R912 admitted `squeek-companion` with `focus:true`. Skill hard-ban: ordinary admits must not set focus — board columns (打新/挖矿/台子/GO/LZ) hide focus cards; only Elysium/Tape/GIWA/DogeEVM/BN Agent re-show them. Card only lived in 重点 strip as a mini, easy to miss / empty when filtering 轮次 912 on 打新.
- **secondary**: Pages build race on `b6afe37` (duration 0 / errored) before `0655e44` finished (~41s); notify could land before CDN had new `data.json`.
- **docs/data.json**: was stale at R601; Pages source is `/` (root `data.json`), but docs snapshot resynced.
- **fix**: `focus:false`, drop focus tags, add whyWatch/oneLiner; sync `docs/data.json`; re-push for clean Pages build.
