#!/usr/bin/env python3
"""Backfill highlights / drawbacks / whatsNew / scores for every candidate."""
from __future__ import annotations

import json
import re
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data.json"
TZ = ZoneInfo("Asia/Shanghai")

# Curated crisp bullets (id -> dict). Overrides auto-derivation when present.
CURATED: dict[str, dict] = {
    "ink-terminal": {
        "highlights": [
            "合约已上 OpenSea，供应 2000 明确",
            "北京时间今晚 18:00 免费公售，日历可排",
            "Ink 链短线注意力窗口，时效明确",
        ],
        "drawbacks": [
            "官推主体分散，假 mint 链接多",
            "务必核对 0x40aca2… 与合集一致后再打",
            "免费公售易被 bot 扫空，gas 战风险",
        ],
        "whatsNew": "",
    },
    "motif": {
        "highlights": [
            "合约生成网格艺术，上限 2048、价 0.03 ETH",
            "10-20 UTC 分阶段 mint，时间表清晰",
            "仍可查 First Chair / Ensemble 资格",
        ],
        "drawbacks": [
            "艺术盘二级流动性偏薄",
            "假 mint 页多，只认 themotif.art",
            "Ensemble 已封，公开窗竞争更烈",
        ],
        "whatsNew": "",
    },
    "computers-rh": {
        "highlights": [
            "今日分阶段免费 mint：GTD→持有者 FCFS→Public",
            "供应 3333 + 游戏内 hashrate/合成叙事",
            "OpenSea 合集已开，可盯成交节奏",
        ],
        "drawbacks": [
            "粉已不小，极早期溢价变薄",
            "公售约 10PM UTC，bot/gas 战难免",
            "Reveal/交易延迟需跟官推确认",
        ],
        "whatsNew": "",
    },
    "afterflow": {
        "highlights": [
            "10-26 免费 mint（+gas），AL/Public 时刻已定",
            "烧 5 换 Afterimage，有二次玩法",
            "供给 1 万、每钱包限 5，规则清楚",
        ],
        "drawbacks": [
            "艺术向二次流动性不确定",
            "只等官宣合约，防假 mint 页",
            "供给偏大，短线炒作空间受限",
        ],
        "whatsNew": "",
    },
    "mutual-fun": {
        "highlights": [
            "RH 链上共同基金叙事，$TMF + Seat",
            "10-22 19:00 UTC mint，日历可排",
            "无 Pass 仍可用 Smart Launch/DEX 入座",
        ],
        "drawbacks": [
            "合规与流动性不确定性高",
            "Pass 二级与假 mint 页需自验",
            "粉过万，信息差不如极早期",
        ],
        "whatsNew": "",
    },
    "glocks-onchain": {
        "highlights": [
            "供应仅 666，合约已上 OpenSea",
            "官推约 8 粉，极早期窗口今晚起",
            "WL 价约 0.00003 ETH，分阶段清晰",
        ],
        "drawbacks": [
            "粉极少、无审计，假合集风险高",
            "务必核对 0x2ecfd6… 再打，小额试水",
            "纯 degen 叙事，默认高归零",
        ],
        "whatsNew": "",
    },
    "hoodpoker": {
        "highlights": [
            "House Pass 7777，今晚起分阶段日历清晰",
            "合约已公布，可链上对表",
            "CCFF00 / WL / HoodFI 多档免费窗",
        ],
        "drawbacks": [
            "赌场叙事监管与跑路风险",
            "假 mint 页多，只认官推+OpenSea",
            "公售 0.001777 ETH，注意 bot",
        ],
        "whatsNew": "",
    },
    "tickertapes": {
        "highlights": [
            "burn-to-earn 像素 ticker，分成叙事清楚",
            "Signal Worlds 4444，免费 WL→公售窗",
            "合约 0xa72d… 已挂，可链上盯",
        ],
        "drawbacks": [
            "代币经济与分成需自验闭环",
            "仿盘/假 mint 多，只认官站合约",
            "RH 新合集流动性可能极薄",
        ],
        "whatsNew": "",
    },
    "swarmpad": {
        "highlights": [
            "今日新建 0 粉号，信息差窗口最大",
            "发币配对 $SWARM + 毕业锁 LP 叙事",
            "费率衰减与国库燃烧差异化可辨",
        ],
        "drawbacks": [
            "站 swarmpad.run 仍 404，无产品可验",
            "当日新号，仿盘/假站风险极高",
            "勿提前授权或打款，只跟官推",
        ],
        "whatsNew": "本轮新收录：当日新建官推、站点尚未上线的 Solana 配对发射预告。",
    },
    "sasa-pad": {
        "highlights": [
            "同币四链 5 分钟赛跑，机制差异化强",
            "官推仅约 101 粉，站已 200 可访问",
            "覆盖 Base/BNB/RH 等多链叙事",
        ],
        "drawbacks": [
            "跨链竞赛规则与锁仓需链上自核",
            "粉极少，执行与仿盘风险高",
            "勿重仓平台币，先小额测交互",
        ],
        "whatsNew": "本轮新收录：多链赛跑发射台，站已 live、粉极少。",
    },
    "torpor": {
        "highlights": [
            "@zenyield 点名，青蛙卡牌 allowlist 已开",
            "申请拿 codes→开 boxes→A 卡保 mint",
            "站 torpor.net/apply 可交互，仍属名单窗",
        ],
        "drawbacks": [
            "链/供应量/价格未全公示",
            "allowlist 钓鱼站多，只走官推域名",
            "正式 mint 日程未锁",
        ],
        "whatsNew": "本轮新收录：@zenyield 点名的卡牌 allowlist，申请流已开。",
    },
    "robocap": {
        "highlights": [
            "robotics / physical AI 向发射台，叙事新鲜",
            "自称刚结束 Colosseum 四周，站已 live",
            "粉约 1.1k，可蹲首批 robotics 币",
        ],
        "drawbacks": [
            "审计与上币规则未充分核验",
            "Colosseum 关联需自证",
            "新叙事台易炒概念，勿 FOMO 平台币",
        ],
        "whatsNew": "本轮新收录：Solana robotics/实体 AI 融资板，站已 live。",
    },
    "units-xreign": {
        "highlights": [
            "5555 LED 机器人免费 mint，名单约今日截止",
            "持有者宣称分 5% $REIGN，时间窗很短",
            "大粉项目但名单窗口仍可操作",
        ],
        "drawbacks": [
            "项目本身不隐形，错过名单=无票",
            "规则以官推为准，防假报名页",
            "正式 mint 时刻未在文案中锁死",
        ],
        "whatsNew": "",
    },
    "ethernal-cubs": {
        "highlights": [
            "10/29 14:00 UTC 免费 mint（仅 gas）日期锁死",
            "3333 Orbs，WL/GTD + Galxe 仍可抢名额",
            "可组装 AI 伙伴+对战，玩法叙事完整",
        ],
        "drawbacks": [
            "WL 已填大半，公共窗变薄",
            "玩法交付不确定，注意钓鱼站",
            "RH 链 NFT 流动性普遍偏弱",
        ],
        "whatsNew": "",
    },
    "donk": {
        "highlights": [
            "自称 11-01 Pump.fun 公平发射，CA 未开",
            "无预售/无团队仓叙事 + CA Verify 工具",
            "倒计时页完整，适合蹲开盘瞬间",
        ],
        "drawbacks": [
            "仿盘/同名币极多，只认官宣 CA",
            "默认土狗高 rug，开盘即博弈",
            "营销页完整≠交付可信",
        ],
        "whatsNew": "",
    },
    "ghosts-among-us": {
        "highlights": [
            "444 供给（含 5 个 1/1），粉约 250",
            "团队点名 Oct 31 mint，大号未覆盖",
            "OpenSea 合集已开，AL 抽奖仍在跑",
        ],
        "drawbacks": [
            "账号极新，无官网/审计",
            "钓鱼回复钱包常见",
            "精确时刻未公告，默认高不确定性",
        ],
        "whatsNew": "",
    },
    "zero-chain": {
        "highlights": [
            "LayerZero 自建 L1，绑定机构级叙事",
            "开链前后常有生态首发/积分窗口",
            "当前主网未开闸，链级事件优先级高",
        ],
        "drawbacks": [
            "大叙事≠立刻有可打新台",
            "假「Zero 测试网」钓鱼极多",
            "只跟 @LayerZero_Core 官宣",
        ],
        "whatsNew": "",
    },
    "omnisea": {
        "highlights": [
            "OFT/ONFT 一键全链发射，Shared OFT 零部署",
            "已支持 Agent 从 X 创建桥接",
            "打新点在「首批用它上链的资产」",
        ],
        "drawbacks": [
            "工具层≠保证赚钱，假桥页多",
            "平台粉量大，赔率在早期用户发射币",
            "核官方 UI 与路由，勿把可跨链当安全",
        ],
        "whatsNew": "",
    },
    "liquid-apes": {
        "highlights": [
            "「流动性内置」叙事差异化",
            "若真 mint 有短线博弈空间",
        ],
        "drawbacks": [
            "⚠️ 高域名风险：假站/撞名/引流 mint 极多",
            "仅官推核对，默认当高危",
            "同名 OpenSea 活动混淆严重",
        ],
        "whatsNew": "",
    },
    "streamoors": {
        "highlights": [
            "AI 虚拟主播发射台今日刚 live",
            "$STREAM CA 已出，可跟创作者币首发",
            "跨 Twitch/Kick/YouTube 实时互动叙事",
        ],
        "drawbacks": [
            "极新产品，合约/审计不明",
            "假主播与抽成难验",
            "平台币已上 pump 后赔率变薄",
        ],
        "whatsNew": "",
    },
    "unbuy-fun": {
        "highlights": [
            "买单可撤销（15m–24h undo），机制少见",
            "站与官推同日上线，极早期",
            "SOL 先托管再进曲线，叙事可辨",
        ],
        "drawbacks": [
            "当日新号、粉丝极少",
            "undo/burn/refund 声明未全核",
            "$UNBUY 本身在 pump，假站风险极高",
        ],
        "whatsNew": "",
    },
    "pumpx": {
        "highlights": [
            "官推约 16h 内新建、仅约 2 粉",
            "社交造梗→铸币叙事，信息差大",
            "仍处预告帖，解封瞬间跟的人少",
        ],
        "drawbacks": [
            "零产品可验，同名仿盘极多",
            "勿提前授权，只认后续 CA/站",
            "默认高不交付风险",
        ],
        "whatsNew": "",
    },
    "orbit-launchpad": {
        "highlights": [
            "RH bonding→Uniswap V4 锁仓毕业，非托管",
            "Fresh launches 仍空，空板早期窗口",
            "factory 合约已公开可对表",
        ],
        "drawbacks": [
            "indexer 追块期板面可能空白",
            "共享 factory，发射币仍高归零",
            "团队社交公开度低",
        ],
        "whatsNew": "",
    },
    "standard-launchpad": {
        "highlights": [
            "股票代币配对发射已 live（SPCX/BABA 等）",
            "RH 独特叙事：美股/A股/韩股链上配对",
            "可盯毕业前扫货与 Charter 空投规则",
        ],
        "drawbacks": [
            "发射洪水期捆绑盘/串发多",
            "毕业率极低，勿盲目跟曲线",
            "核 LP/持仓集中度再动手",
        ],
        "whatsNew": "",
    },
    "hookit": {
        "highlights": [
            "Ink 上 Uniswap v4 hooks 发射，可报价股票/USDG",
            "Master/Classic 双轨 + LP 锁，机制差异化强",
            "工厂合约与文档已公开",
        ],
        "drawbacks": [
            "Ink 流量与 hook 复杂度并存",
            "需核对模块冻结规则",
            "首波自定义 hook 质量参差",
        ],
        "whatsNew": "",
    },
    "litpump": {
        "highlights": [
            "LitVM 上许可less bonding，台子几乎零数据",
            "反狙击 + 85 zkLTC 毕业阈值清晰",
            "创作者分 50% 交易费",
        ],
        "drawbacks": [
            "流动性与用户几乎为空",
            "L2/跨链资产路径需自验",
            "默认高归零概率",
        ],
        "whatsNew": "",
    },
    "bakeru": {
        "highlights": [
            "免费 mint 申请刚开，挂动画工作室叙事",
            "Solana Free Mint / NFT / TGE 路径写明",
            "中文区开始推，合约官宣前可蹲",
        ],
        "drawbacks": [
            "粉约 1.3 万，不算隐形",
            "表单/DC 钓鱼常见，勿提前授权",
            "mint 日仍 TBA",
        ],
        "whatsNew": "",
    },
    "esccap": {
        "highlights": [
            "复古键盘 Genesis 3333，RH 路线图 Q4",
            "referral 榜 + 字谜 GTD WL 进行中",
            "WL 截止时刻可排（约 10-16 07:30 UTC）",
        ],
        "drawbacks": [
            "正式 mint 仍在 Q4，非立刻可打",
            "协作抽奖钓鱼常见",
            "以官推截止规则为准",
        ],
        "whatsNew": "",
    },
    "enter-the-anime": {
        "highlights": [
            "RH 原创新街动漫，供应 3333 免费 mint",
            "官站角色页已上线，日历约 10/15–10/22",
            "可盯开售/售罄节奏",
        ],
        "drawbacks": [
            "外部日历供应口径曾与官站不一致",
            "团队曝光少，假 mint 链接风险",
            "精确开售时刻未锁",
        ],
        "whatsNew": "",
    },
    "vampme-fun": {
        "highlights": [
            "粘贴任意 Solana CA 生成 vamp 结尾孪生",
            "创作者费叙事 70%，站已 live",
            "官推约 21 粉，工具层极早期",
        ],
        "drawbacks": [
            "审计不明，「吸血」易出诈骗仿盘",
            "先核站与 CA 一致",
            "勿重仓平台币",
        ],
        "whatsNew": "",
    },
    "fobo-fun": {
        "highlights": [
            "RH rising-floor 发射台，站已 live",
            "仍写 Launching soon，首批发射可蹲",
            "官推约 412 粉，社区开始推",
        ],
        "drawbacks": [
            "未正式开板，机制未链上核验",
            "RH 新台仿盘多",
            "勿提前打款",
        ],
        "whatsNew": "",
    },
    "robinfinite": {
        "highlights": [
            "RH 永久曲线 meme 台+DEX，站已开",
            "官推仅约 29 粉，板面可早蹲",
            "自推 100% Permanent Curve 差异化",
        ],
        "drawbacks": [
            "粉丝极少，审计/锁仓未公开核验",
            "先小额测交互",
            "勿把平台币当必涨",
        ],
        "whatsNew": "",
    },
    "cracker-fun": {
        "highlights": [
            "自称美国 LLC + Quill 审计、无平台币",
            "站已 live，合规向叙事相对少见",
            "多链定位，社区对标 Monad 式扩张",
        ],
        "drawbacks": [
            "合规/审计需自核报告与实体",
            "粉不算隐形",
            "叙事不降归零概率",
        ],
        "whatsNew": "",
    },
}


def clamp(n: int, lo: int = 0, hi: int = 100) -> int:
    return max(lo, min(hi, int(round(n))))


def split_clauses(text: str) -> list[str]:
    if not text:
        return []
    # split on Chinese/English separators
    parts = re.split(r"[；;。！!？?\n]+|(?<=[）)])\s*|(?<=,)\s+(?=[A-Z一-龥])", text)
    out = []
    for p in parts:
        p = p.strip(" ，,、·-|")
        p = re.sub(r"\s+", " ", p)
        if len(p) >= 8:
            out.append(p)
    return out


def crisp(s: str, max_len: int = 42) -> str:
    s = s.strip()
    s = re.sub(r"^(适合|可以|能够|需要|注意)", "", s)
    if len(s) > max_len:
        # cut at punctuation if possible
        cut = s[:max_len]
        for sep in ("，", "、", ",", "；", " "):
            i = cut.rfind(sep)
            if i >= 18:
                cut = cut[:i]
                break
        s = cut.rstrip("，,、；; ") + "…"
    return s


BANNED_HI = re.compile(r"^(早期|热门|不错|看好|值得关注|潜力大|很早|极早)$")


def derive_highlights(c: dict) -> list[str]:
    why = c.get("whyWatch") or ""
    bg = c.get("background") or ""
    clauses = split_clauses(why) + split_clauses(bg)
    picks = []
    for cl in clauses:
        # prefer mechanism / supply / time / product specifics
        score = 0
        if re.search(r"\d|合约|供应|免费|mint|发射|曲线|锁|OFT|GTD|WL|UTC|CA|live|Live|差异|首个|配对|undo|hooks|赛跑", cl, re.I):
            score += 2
        if re.search(r"粉|账号|建号", cl):
            score += 1
        if score == 0:
            continue
        item = crisp(cl)
        if BANNED_HI.match(item) or item in picks:
            continue
        picks.append(item)
        if len(picks) >= 4:
            break
    if len(picks) < 2:
        # fallback: take first why clauses anyway
        for cl in split_clauses(why):
            item = crisp(cl)
            if item and item not in picks and not BANNED_HI.match(item):
                picks.append(item)
            if len(picks) >= 2:
                break
    if len(picks) < 2:
        picks.append(crisp(f"{c.get('category','')} · {c.get('chain','')} 早期候选"))
        picks.append(crisp((why or bg or "信息仍偏预热")[:40]))
    return picks[:4]


def derive_drawbacks(c: dict) -> list[str]:
    risk = c.get("risk") or ""
    clauses = split_clauses(risk)
    picks = []
    for cl in clauses:
        item = crisp(cl)
        if item and item not in picks:
            picks.append(item)
        if len(picks) >= 4:
            break
    if len(picks) < 2:
        lvl = c.get("riskLevel") or "high"
        picks.append(f"风险档 {lvl}，默认可归零")
        if "钓鱼" not in "".join(picks):
            picks.append("只认官推入口，防假站/假 mint")
    # ensure actionable tone
    return picks[:4]


def novelty_score(c: dict) -> int:
    blob = f"{c.get('whyWatch','')} {c.get('background','')} {c.get('name','')}"
    n = 45
    if re.search(r"首个|差异化|全新|刚|今日|当日|新建|密封|极早|信息差", blob):
        n += 18
    if re.search(r"hooks|OFT|undo|赛跑|permanent curve|rising-floor|吸血|robotics|physical AI|共同基金|burn-to-earn|agent", blob, re.I):
        n += 16
    if re.search(r"仿盘|同名|营销|已 live.*粉", blob):
        n -= 5
    # newer rounds slightly higher novelty baseline
    n += min(12, (int(c.get("round") or 1) - 1) * 1.2)
    return clamp(n)


def actionable_score(c: dict) -> int:
    s = c.get("schedule") or {}
    o = c.get("onchain") or {}
    why = c.get("whyWatch") or ""
    a = 30
    status = s.get("status")
    if status == "live":
        a += 40
    elif status == "confirmed":
        a += 32
    elif status == "tentative":
        a += 18
    elif status == "tba":
        a += 8
    if s.get("startsAt"):
        a += 10
    if o.get("contract") or o.get("explorer"):
        a += 12
    if o.get("mintStatus") == "open":
        a += 10
    if re.search(r"WL|白名单|申请|allowlist|表单|GTD|live|已开|可交互", why, re.I):
        a += 8
    if re.search(r"TBA|Coming soon|未开|CA 未|无产品", why, re.I):
        a -= 6
    return clamp(a)


def compute_scores(c: dict) -> dict:
    early = clamp(c.get("earlyScore") or 50)
    risk = clamp(c.get("riskScore") or 70)
    novelty = novelty_score(c)
    actionable = actionable_score(c)
    overall = clamp(early * 0.35 + actionable * 0.25 + novelty * 0.2 + (100 - risk) * 0.2)
    return {
        "early": early,
        "risk": risk,
        "novelty": novelty,
        "actionable": actionable,
        "overall": overall,
    }


def whats_new_for(c: dict, latest_ids: set[str], latest_round: int) -> str:
    if c["id"] in CURATED and CURATED[c["id"]].get("whatsNew"):
        return CURATED[c["id"]]["whatsNew"]
    if c["id"] in latest_ids or int(c.get("round") or 0) == latest_round:
        name = c.get("name") or c["id"]
        cat = c.get("category") or ""
        chain = c.get("chain") or ""
        # one crisp line from whyWatch
        first = split_clauses(c.get("whyWatch") or "")
        tip = crisp(first[0], 36) if first else "新候选入库"
        return f"本轮新收录：{cat}/{chain} · {tip}"
    return ""


def enrich(data: dict) -> dict:
    data = deepcopy(data)
    meta = data.setdefault("meta", {})
    now = datetime.now(TZ)
    meta["updated"] = now.strftime("%Y-%m-%d %H:%M CST")
    feats = list(meta.get("features") or [])
    for f in ("schedule", "onchain", "scores", "highlights"):
        if f not in feats:
            feats.append(f)
    meta["features"] = feats

    # latest roundNAdded
    latest_round = 0
    latest_ids: set[str] = set()
    for k, v in meta.items():
        m = re.match(r"round(\d+)Added$", k)
        if m and isinstance(v, list):
            r = int(m.group(1))
            if r > latest_round:
                latest_round = r
                latest_ids = set(v)

    for c in data.get("candidates", []):
        cur = CURATED.get(c["id"], {})
        c["highlights"] = cur.get("highlights") or derive_highlights(c)
        c["drawbacks"] = cur.get("drawbacks") or derive_drawbacks(c)
        # ensure 2–4
        c["highlights"] = c["highlights"][:4]
        c["drawbacks"] = c["drawbacks"][:4]
        while len(c["highlights"]) < 2:
            c["highlights"].append("机制/窗口仍需对照官推更新")
        while len(c["drawbacks"]) < 2:
            c["drawbacks"].append("高风险，仅作信息整理")

        c["whatsNew"] = whats_new_for(c, latest_ids, latest_round)
        c["scores"] = compute_scores(c)
        # keep mirrors
        c["earlyScore"] = c["scores"]["early"]
        c["riskScore"] = c["scores"]["risk"]

    return data, latest_round, len(latest_ids)


def main() -> None:
    raw = json.loads(DATA.read_text(encoding="utf-8"))
    data, latest_round, n_latest = enrich(raw)
    DATA.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    n = len(data["candidates"])
    with_new = sum(1 for c in data["candidates"] if c.get("whatsNew"))
    avg_o = sum(c["scores"]["overall"] for c in data["candidates"]) / n
    print(json.dumps({
        "ok": True,
        "candidates": n,
        "latestRound": latest_round,
        "whatsNewCount": with_new,
        "avgOverall": round(avg_o, 1),
        "updated": data["meta"]["updated"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
