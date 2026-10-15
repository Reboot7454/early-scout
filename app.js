(() => {
  const state = {
    data: null,
    category: "all",
    chain: "all",
    round: "all",
    layerzero: "all",
    query: "",
    sort: "earlyness",
  };

  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => [...document.querySelectorAll(sel)];

  const RISK_RANK = {
    extreme: 4,
    high: 3,
    "medium-high": 2,
    medium: 1,
    low: 0,
  };

  const RISK_LABEL = {
    extreme: "极高",
    high: "高",
    "medium-high": "中高",
    medium: "中",
    low: "低",
  };

  function xIcon() {
    return `<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.727-8.835L1.254 2.25H8.08l4.253 5.622L18.244 2.25zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>`;
  }
  function siteIcon() {
    return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>`;
  }

  function escapeHtml(s) {
    return String(s ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function isLayerZero(c) {
    const tags = (c.tags || []).map((t) => String(t).toLowerCase());
    if (tags.some((t) => t.includes("layerzero") || t === "lz" || t === "oft" || t === "zro")) {
      return true;
    }
    const chain = String(c.chain || "").toLowerCase();
    if (chain === "layerzero" || chain === "zero") return true;
    const blob = `${c.name} ${c.whyWatch || ""} ${c.background || ""}`.toLowerCase();
    return blob.includes("layerzero") || blob.includes("layer zero");
  }

  function cardHtml(c) {
    const flagClass =
      c.flag === "high_domain_risk"
        ? "flag-domain"
        : c.flag === "borderline"
          ? "flag-borderline"
          : "";
    const riskClass = c.riskLevel === "extreme" ? "risk-extreme" : "";
    const lz = isLayerZero(c);
    const lzClass = lz ? "card-lz" : "";
    const hasFlag = Boolean(flagClass);
    const x = c.links?.x;
    const site = c.links?.site;
    const riskLevelKey = String(c.riskLevel || "medium");
    const extraTags = (c.tags || [])
      .filter((t) => !["LayerZero"].includes(t))
      .slice(0, 3)
      .map((t) => `<span class="tag tag-extra">${escapeHtml(t)}</span>`)
      .join("");

    return `
      <article class="card ${riskClass} ${flagClass} ${lzClass}" data-id="${escapeHtml(c.id)}">
        <div class="card-top ${hasFlag ? "" : "has-no-flag"}">
          <div>
            <div class="name">${escapeHtml(c.name)}${lz ? '<span class="lz-chip" title="LayerZero 相关">LZ</span>' : ""}</div>
            <div class="tags">
              <span class="tag tag-cat-${escapeHtml(c.category)}">${escapeHtml(c.category)}</span>
              <span class="tag tag-chain">${escapeHtml(c.chain)}</span>
              ${lz ? '<span class="tag tag-lz">LayerZero</span>' : ""}
              ${extraTags}
            </div>
          </div>
          <span class="round-badge r${c.round}">轮次 ${c.round}</span>
        </div>
        <div class="field">
          <div class="label">为什么值得蹲</div>
          <div class="value">${escapeHtml(c.whyWatch)}</div>
        </div>
        <div class="field">
          <div class="label">背景</div>
          <div class="value">${escapeHtml(c.background)}</div>
        </div>
        <div class="field risk level-${escapeHtml(riskLevelKey)}">
          <div class="label">风险 · ${escapeHtml(RISK_LABEL[riskLevelKey] || riskLevelKey)}</div>
          <div class="value">${escapeHtml(c.risk)}</div>
        </div>
        <div class="actions">
          <a class="btn ${x ? "" : "disabled"}" href="${x || "#"}" target="_blank" rel="noopener noreferrer">${xIcon()} X</a>
          <a class="btn ${site ? "" : "disabled"}" href="${site || "#"}" target="_blank" rel="noopener noreferrer">${siteIcon()} 官网</a>
        </div>
      </article>
    `;
  }

  function filtered() {
    const q = state.query.trim().toLowerCase();
    let list = state.data.candidates.slice();

    if (state.category !== "all") {
      list = list.filter((c) => c.category === state.category);
    }
    if (state.chain !== "all") {
      list = list.filter((c) => c.chain === state.chain);
    }
    if (state.round !== "all") {
      list = list.filter((c) => String(c.round) === String(state.round));
    }
    if (state.layerzero === "on") {
      list = list.filter(isLayerZero);
    }
    if (q) {
      list = list.filter((c) => {
        const blob = [
          c.name,
          c.category,
          c.chain,
          c.whyWatch,
          c.background,
          c.risk,
          c.flag,
          ...(c.tags || []),
        ]
          .join(" ")
          .toLowerCase();
        return blob.includes(q);
      });
    }

    if (state.sort === "risk") {
      list.sort(
        (a, b) =>
          (b.riskScore ?? RISK_RANK[b.riskLevel] * 20) -
            (a.riskScore ?? RISK_RANK[a.riskLevel] * 20) ||
          b.earlyScore - a.earlyScore
      );
    } else if (state.sort === "name") {
      list.sort((a, b) => a.name.localeCompare(b.name, "zh"));
    } else {
      list.sort(
        (a, b) =>
          (b.earlyScore ?? 0) - (a.earlyScore ?? 0) ||
          (b.riskScore ?? 0) - (a.riskScore ?? 0)
      );
    }
    return list;
  }

  function uniqueChains(candidates) {
    return [...new Set(candidates.map((c) => c.chain))].sort((a, b) => {
      // Pin LayerZero / Zero near front for visibility
      const rank = (ch) =>
        ch === "LayerZero" ? 0 : ch === "Zero" ? 1 : 2;
      return rank(a) - rank(b) || a.localeCompare(b);
    });
  }

  function renderChips() {
    const catHost = $("#cat-chips");
    const chainHost = $("#chain-chips");
    const roundHost = $("#round-chips");
    const lzHost = $("#lz-chips");

    const cats = [
      { id: "all", label: "全部品类", cls: "" },
      { id: "新台", label: "新台", cls: "cat-platform" },
      { id: "Meme", label: "Meme", cls: "cat-meme" },
      { id: "NFT", label: "NFT", cls: "cat-nft" },
    ];
    catHost.innerHTML = cats
      .map(
        (c) =>
          `<button type="button" class="chip ${c.cls} ${state.category === c.id ? "active" : ""}" data-group="category" data-value="${c.id}">${c.label}</button>`
      )
      .join("");

    const chains = [
      { id: "all", label: "全部链" },
      ...uniqueChains(state.data.candidates).map((ch) => ({
        id: ch,
        label: ch,
      })),
    ];
    chainHost.innerHTML = chains
      .map(
        (c) =>
          `<button type="button" class="chip ${c.id === "LayerZero" || c.id === "Zero" ? "chip-lz" : ""} ${state.chain === c.id ? "active" : ""}" data-group="chain" data-value="${escapeHtml(c.id)}">${escapeHtml(c.label)}</button>`
      )
      .join("");

    const maxRound = Math.max(
      1,
      ...state.data.candidates.map((c) => Number(c.round) || 1)
    );
    const rounds = [
      { id: "all", label: "全部轮次" },
      ...Array.from({ length: maxRound }, (_, i) => ({
        id: String(i + 1),
        label: `轮次 ${i + 1}`,
      })),
    ];
    roundHost.innerHTML = rounds
      .map(
        (c) =>
          `<button type="button" class="chip ${state.round === c.id ? "active" : ""}" data-group="round" data-value="${c.id}">${c.label}</button>`
      )
      .join("");

    if (lzHost) {
      const lzCount = state.data.candidates.filter(isLayerZero).length;
      lzHost.innerHTML = `
        <button type="button" class="chip chip-lz ${state.layerzero === "all" ? "active" : ""}" data-group="layerzero" data-value="all">全部（含非 LZ）</button>
        <button type="button" class="chip chip-lz ${state.layerzero === "on" ? "active" : ""}" data-group="layerzero" data-value="on">LayerZero 监控 · ${lzCount}</button>
      `;
    }

    const btn = $("#lz-filter-btn");
    if (btn) {
      btn.classList.toggle("active", state.layerzero === "on");
      btn.textContent =
        state.layerzero === "on" ? "显示全部候选" : "只看 LayerZero";
    }
  }

  function renderLzWatch() {
    const watch = state.data.meta?.layerZeroWatch;
    const desc = $("#lz-watch-desc");
    const pill = $("#lz-pill");
    if (!watch) return;
    const n = state.data.candidates.filter(isLayerZero).length;
    if (desc) {
      const focus = (watch.focus || []).join(" · ");
      desc.textContent = `${watch.label || "LayerZero 监控中"} · ${n} 条相关 · ${focus}`;
    }
    if (pill) {
      pill.textContent = `LayerZero 监控 · ${n}`;
      pill.classList.add("pill-lz");
    }
  }

  function render() {
    const list = filtered();
    const grid = $("#grid");
    if (!list.length) {
      const emptyLz =
        state.layerzero === "on"
          ? `<div class="empty empty-lz"><div class="lz-badge-lg">LZ</div><div><b>LayerZero 监控已开启</b><br/>当前筛选下暂无匹配项。开链/新台信号出现后会自动入库；可点「显示全部候选」或清空筛选。</div></div>`
          : `<div class="empty">没有匹配的候选。试试清空筛选或换个关键词。</div>`;
      grid.innerHTML = emptyLz;
    } else {
      grid.innerHTML = list.map(cardHtml).join("");
    }

    const total = state.data.candidates.length;
    const lzN = state.data.candidates.filter(isLayerZero).length;
    const r1 = state.data.candidates.filter((c) => c.round === 1).length;
    const r2 = state.data.candidates.filter((c) => c.round === 2).length;
    $("#stats").innerHTML = `
      显示 <b>${list.length}</b> / ${total} ·
      LayerZero <b>${lzN}</b> ·
      轮次1 <b>${r1}</b> ·
      轮次2 <b>${r2}</b> ·
      更新日期 <b>${escapeHtml(state.data.meta.updated)}</b> CST
    `;
  }

  function bind() {
    $("#search").addEventListener("input", (e) => {
      state.query = e.target.value;
      render();
    });
    $("#sort").addEventListener("change", (e) => {
      state.sort = e.target.value;
      render();
    });

    document.addEventListener("click", (e) => {
      const chip = e.target.closest(".chip, .lz-filter-btn");
      if (!chip) return;
      const group = chip.dataset.group;
      let value = chip.dataset.value;
      if (!group) return;

      if (group === "layerzero" && chip.id === "lz-filter-btn") {
        state.layerzero = state.layerzero === "on" ? "all" : "on";
      } else {
        state[group] = value;
      }
      renderChips();
      render();
    });
  }

  async function boot() {
    try {
      const res = await fetch("./data.json?t=" + Date.now(), { cache: "no-store" });
      if (!res.ok) throw new Error("data.json load failed");
      state.data = await res.json();
      $("#updated").textContent = state.data.meta.updated;
      $("#count").textContent = String(state.data.candidates.length);
      renderLzWatch();
      renderChips();
      bind();
      render();
    } catch (err) {
      $("#grid").innerHTML = `<div class="empty">无法加载 data.json：${escapeHtml(err.message)}</div>`;
    }
  }

  boot();
})();
