(async () => {
  const CHANNELS = {
    '1537897411668746302': { channel: 'alpha-3-new-accounts', cutoff: '2026-11-21 14:57' },
    '1549303534263214160': { channel: 'alpha-1-backup', cutoff: '2026-11-21 14:14' },
    '1527900129300840551': { channel: 'smart-accounts-tracker', cutoff: '2026-11-21 14:13' },
    '1527862926885785710': { channel: 'alpha-1', cutoff: '2026-11-21 14:51' },
  };
  const id = (location.pathname.split('/').filter(Boolean).pop() || '');
  const meta = CHANNELS[id];
  if (!meta) {
    console.error('unknown channel', location.href);
    document.title = 'SCRAPE_ERR unknown channel';
    return { error: 'unknown channel', url: location.href };
  }
  const CHANNEL = meta.channel;
  const CUTOFF = meta.cutoff;
  const HARDCAP = 250;
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const pad = n => String(n).padStart(2, '0');
  const toCST = (d) => {
    const t = new Date(d.getTime() + 8 * 3600e3);
    return `${t.getUTCFullYear()}-${pad(t.getUTCMonth() + 1)}-${pad(t.getUTCDate())} ${pad(t.getUTCHours())}:${pad(t.getUTCMinutes())}`;
  };
  const cstNow = toCST(new Date());
  const todayDate = cstNow.slice(0, 10);
  const y = new Date(Date.now() + 8 * 3600e3);
  y.setUTCDate(y.getUTCDate() - 1);
  const yestDate = `${y.getUTCFullYear()}-${pad(y.getUTCMonth() + 1)}-${pad(y.getUTCDate())}`;
  const cstToIso = (cst) => {
    const m = cst.match(/(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})/);
    if (!m) return null;
    return new Date(Date.UTC(+m[1], +m[2] - 1, +m[3], +m[4] - 8, +m[5])).toISOString();
  };
  const num = (t, l) => {
    const m = t.match(new RegExp(l + '\\s*([\\d,]+)', 'i'));
    return m ? parseInt(m[1].replace(/,/g, ''), 10) : null;
  };
  // Prefer exact 跳转至当前; do NOT click 以来有 (stale unread cursor).
  const jumpHits = [...document.querySelectorAll('div,button,span,a')].filter(e => {
    const t = (e.innerText || '').trim();
    return t === '跳转至当前' || t === 'Jump to Present' || t === 'Jump to present';
  });
  jumpHits.forEach(e => { e.click(); e.dispatchEvent(new MouseEvent('click', { bubbles: true })); });
  if (jumpHits.length) await sleep(2000);
  const findScroller = () => {
    const cands = [...document.querySelectorAll('div')].filter(d => {
      const cs = getComputedStyle(d);
      return (cs.overflowY === 'scroll' || cs.overflowY === 'auto') && d.scrollHeight > d.clientHeight + 200;
    });
    const withMsg = cands.find(d => d.querySelector('li[id^="chat-messages-"]'));
    if (withMsg) return withMsg;
    return cands.sort((a, b) => (b.scrollHeight - b.clientHeight) - (a.scrollHeight - a.clientHeight))[0] || null;
  };
  const sc0 = findScroller();
  if (sc0) { sc0.scrollTop = sc0.scrollHeight; await sleep(800); }

  const seen = new Set(), cards = [];
  let oldest = null, newest = null, capped = false, passed = false, spidey = false, nv = null, read = 0;
  let stagnant = 0, lastOldest = null, lastLen = 0;

  for (let i = 0; i < 280 && !passed && !capped; i++) {
    const nodes = [...document.querySelectorAll('li[id^="chat-messages-"]')];
    read = Math.max(read, nodes.length);
    for (const el of nodes) {
      const text = el.innerText || '';
      const te = el.querySelector('time');
      let iso = te && te.getAttribute('datetime');
      let cst = iso ? toCST(new Date(iso)) : null;
      if (!cst) {
        const fmtHM = (dateStr, hh, mm, ap) => {
          let h = +hh;
          if (ap) { const a = ap.toUpperCase(); if (a === 'PM' && h < 12) h += 12; if (a === 'AM' && h === 12) h = 0; }
          return `${dateStr} ${pad(h)}:${mm}`;
        };
        let m = text.match(/(?:Today|今天)\s*(?:at\s*)?(\d{1,2}):(\d{2})\s*(AM|PM)?/i);
        if (m) cst = fmtHM(todayDate, m[1], m[2], m[3]);
        m = text.match(/(?:Yesterday|昨天)\s*(?:at\s*)?(\d{1,2}):(\d{2})\s*(AM|PM)?/i);
        if (!cst && m) cst = fmtHM(yestDate, m[1], m[2], m[3]);
        if (!cst) {
          m = text.match(/(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|星期一|星期二|星期三|星期四|星期五|星期六|星期日|周一|周二|周三|周四|周五|周六|周日)\s*(?:at\s*)?(\d{1,2}):(\d{2})\s*(AM|PM)?/i);
          if (m) {
            const map = {monday:1,tuesday:2,wednesday:3,thursday:4,friday:5,saturday:6,sunday:0,
              '星期一':1,'星期二':2,'星期三':3,'星期四':4,'星期五':5,'星期六':6,'星期日':0,
              '周一':1,'周二':2,'周三':3,'周四':4,'周五':5,'周六':6,'周日':0};
            const want = map[m[1].toLowerCase()];
            const now = new Date(Date.now() + 8 * 3600e3);
            for (let back = 1; back <= 6; back++) {
              const d = new Date(now); d.setUTCDate(d.getUTCDate() - back);
              if (d.getUTCDay() === want) {
                cst = fmtHM(`${d.getUTCFullYear()}-${pad(d.getUTCMonth()+1)}-${pad(d.getUTCDate())}`, m[2], m[3], m[4]);
                break;
              }
            }
          }
        }
        m = text.match(/(\d{1,2})\/(\d{2})\/(\d{4}),?\s*(\d{1,2}):(\d{2})(?::(\d{2}))?\s*(AM|PM)?/i);
        if (!cst && m) {
          let hh = +m[4];
          if (m[7]) { const ap = m[7].toUpperCase(); if (ap === 'PM' && hh < 12) hh += 12; if (ap === 'AM' && hh === 12) hh = 0; }
          const utc = Date.UTC(+m[3], +m[2] - 1, +m[1], hh, +m[5], +(m[6] || 0));
          cst = toCST(new Date(utc)); iso = new Date(utc).toISOString();
        }
      }
      if (!cst) continue;
      if (!nv || cst > nv) nv = cst;
      if (/Spidey Bot|Twitter Follow Monitor|X Follow Monitor/i.test(text)) spidey = true;
      if (!/New follower|Twitter Follow Monitor|X Follow Monitor|follower of|\sfollowed\s/i.test(text)) continue;
      let handle = null, followerOf = null, snippet = 'New follower';
      const fo = text.match(/New follower of\s*(@[A-Za-z0-9_]+)/i);
      const fol = text.match(/(@[A-Za-z0-9_]+)\s+followed\s+(@[A-Za-z0-9_]+)/i);
      if (fo) { followerOf = fo[1]; snippet = `New follower of ${fo[1]}`; }
      else if (fol) { followerOf = fol[1]; handle = fol[2]; snippet = `${fol[1]} followed ${fol[2]}`; }
      const als = [...el.querySelectorAll('a[href*="x.com/"],a[href*="twitter.com/"]')];
      if (!handle) {
        for (const a of als) {
          const hm = a.href.match(/https?:\/\/(?:x|twitter)\.com\/([A-Za-z0-9_]+)/i);
          if (hm && !/^(i|intent|home|share|search)$/i.test(hm[1])) {
            const h = '@' + hm[1];
            if (followerOf && h.toLowerCase() === followerOf.toLowerCase()) continue;
            handle = h; break;
          }
        }
      }
      if (!handle) {
        const lines0 = text.split(/\n/).map(s => s.trim()).filter(Boolean);
        for (const line of lines0) {
          const hm = line.match(/^@([A-Za-z0-9_]{1,40})$/);
          if (hm) {
            const h = '@' + hm[1];
            if (followerOf && h.toLowerCase() === followerOf.toLowerCase()) continue;
            handle = h; break;
          }
        }
      }
      if (!handle) { const hm = text.match(/@([A-Za-z0-9_]{1,40})/); if (hm) handle = '@' + hm[1]; }
      if (!handle) continue;
      const key = CHANNEL + '|' + handle.toLowerCase() + '|' + cst;
      if (seen.has(key)) continue;
      seen.add(key);
      if (cst <= CUTOFF) { passed = true; if (!oldest || cst < oldest) oldest = cst; continue; }
      const nameM = text.match(/Name\s*\n?\s*([^\n]+)/i);
      const links = ['https://x.com/' + handle.replace(/^@/, '')];
      const lines = text.split(/\n/).map(s => s.trim()).filter(Boolean);
      let bio = '';
      const hi = lines.findIndex(l => l === handle || l.startsWith(handle + ' '));
      if (hi >= 0) {
        const chunk = [];
        for (let k = hi + 1; k < lines.length; k++) {
          if (/^(Name|Followers|Following|New follower)/i.test(lines[k])) break;
          if (/^(Captain Hook|APP|Spidey|Twitter Follow|Webhook|X Follow)/i.test(lines[k])) continue;
          if (/^(今天|Today|昨天|Yesterday|\d{1,2}:\d{2})/.test(lines[k])) continue;
          chunk.push(lines[k]);
        }
        bio = chunk.join(' ').slice(0, 280);
      }
      let bot = null;
      if (/Captain Hook/i.test(text)) bot = 'Captain Hook';
      else if (/Spidey/i.test(text)) bot = 'Spidey Bot';
      else if (/X Follow Monitor/i.test(text)) bot = 'X Follow Monitor';
      else if (/Twitter Follow Monitor/i.test(text)) bot = 'Twitter Follow Monitor';
      if (!fo && !fol && bio) snippet = bio;
      cards.push({
        channel: CHANNEL, handle,
        name: nameM ? nameM[1].trim() : handle.slice(1),
        followers: num(text, 'Followers'),
        following: num(text, 'Following'),
        followerOf, links,
        cardTimeCST: cst,
        cardTime: iso || cstToIso(cst),
        time: cst, snippet, bio, description: bio, bot
      });
      if (!newest || cst > newest) newest = cst;
      if (!oldest || cst < oldest) oldest = cst;
      if (cards.length >= HARDCAP) { capped = true; break; }
    }
    if (passed || capped) break;
    const sc = findScroller();
    const beforeTop = sc ? sc.scrollTop : null;
    if (sc) {
      sc.scrollTop = Math.max(0, sc.scrollTop - Math.max(1200, Math.floor(sc.clientHeight * 1.2)));
      sc.dispatchEvent(new WheelEvent('wheel', { deltaY: -1800, bubbles: true }));
    }
    await sleep(700);
    if (sc && sc.scrollTop === 0) {
      sc.dispatchEvent(new WheelEvent('wheel', { deltaY: -2400, bubbles: true }));
      await sleep(250);
    }
    const curOldest = oldest;
    if (cards.length === lastLen && curOldest === lastOldest && beforeTop === 0) stagnant++;
    else stagnant = 0;
    lastLen = cards.length; lastOldest = curOldest;
    if (stagnant >= 8) break;
  }
  cards.sort((a, b) => a.cardTimeCST < b.cardTimeCST ? 1 : a.cardTimeCST > b.cardTimeCST ? -1 : 0);
  const body = (document.body && document.body.innerText || '').slice(0, 2500);
  const loginOk = !(/QR code|Scan this|Log in with|Welcome back/i.test(body) && !/Reboot\.Btc|#alpha/i.test(body));
  const result = {
    channel: CHANNEL, cutoff: CUTOFF, loginOk, cards,
    newest: newest || nv, oldestReached: oldest || nv, newestVisible: nv,
    capped, spidey, cardsReadApprox: Math.max(read, seen.size),
    passedCutoff: passed, n: cards.length
  };
  document.title = `SCRAPE_OK ${CHANNEL} n=${cards.length} nv=${nv} old=${result.oldestReached} passed=${passed} cap=${capped} spidey=${spidey}`;
  try { copy(JSON.stringify(result)); } catch (e) {}
  try {
    const blob = new Blob([JSON.stringify(result, null, 2)], { type: 'application/json' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'dc40_r2092_' + CHANNEL + '.json';
    document.body.appendChild(a);
    a.click();
    a.remove();
  } catch (e) { console.error('download fail', e); }
  console.log('SCRAPE_DONE', result.channel, 'n=', result.n, 'newest=', result.newestVisible, 'oldest=', result.oldestReached, 'passed=', result.passedCutoff, 'capped=', result.capped, 'spidey=', result.spidey);
  return result;
})();
