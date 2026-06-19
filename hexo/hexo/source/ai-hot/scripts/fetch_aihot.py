#!/usr/bin/env python3
"""
fetch_aihot.py — AIHOT API 命令行调用脚本

零依赖（只用 Python 3.8+ 标准库），用于：
1. 手动测试 AIHOT API 是否可用
2. 在 Agent 里被 SKILL.md 引用，让 LLM 生成调用参数
3. 快速拉取今日日报 / 精选条目做内容素材

用法：
    python3 fetch_aihot.py daily
    python3 fetch_aihot.py daily --date 2026-06-17
    python3 fetch_aihot.py items --since 24h
    python3 fetch_aihot.py items --category ai-models --since 7d
    python3 fetch_aihot.py items --q "Python 自动化"
    python3 fetch_aihot.py dailies --take 30
    python3 fetch_aihot.py items --cursor <token>   # 翻页
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

BASE_URL = "https://aihot.virxact.com"

# 必须用浏览器 UA，否则 nginx 会直接 403
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

# 实际 API 用的英文分类枚举
CATEGORIES_EN = ["ai-models", "ai-products", "industry", "paper", "tip"]
CATEGORIES_ZH = {
    "ai-models": "模型",
    "ai-products": "产品",
    "industry": "行业",
    "paper": "论文",
    "tip": "技巧",
}

USE_COLOR = sys.stdout.isatty()


def c(code: str, text: str) -> str:
    if not USE_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"


def http_get(path: str, params: Optional[Dict[str, Any]] = None, timeout: int = 20) -> Dict[str, Any]:
    if params:
        qs = urllib.parse.urlencode(params, quote_via=urllib.parse.quote_plus)
        url = f"{BASE_URL}{path}?{qs}"
    else:
        url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url, headers=DEFAULT_HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def parse_since(since: str) -> str:
    """自然语言时长 → ISO-8601（UTC）"""
    now = datetime.now(timezone.utc)
    if since.endswith("h"):
        delta = timedelta(hours=int(since[:-1]))
    elif since.endswith("d"):
        delta = timedelta(days=int(since[:-1]))
    elif since.endswith("w"):
        delta = timedelta(weeks=int(since[:-1]))
    else:
        return since
    return (now - delta).strftime("%Y-%m-%dT%H:%M:%SZ")


def fmt_time(iso: str) -> str:
    """UTC → Asia/Shanghai 友好显示"""
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        sh = dt.astimezone(timezone(timedelta(hours=8)))
        return sh.strftime("%m-%d %H:%M")
    except Exception:
        return iso


def render_item(item: Dict[str, Any], idx: int) -> str:
    """渲染单条热点（适配实际字段，daily 端点可能缺部分字段）"""
    title = item.get("title") or "（无标题）"
    summary = item.get("summary") or ""
    url = item.get("url", "")
    cat_en = item.get("category", "")
    cat_zh = CATEGORIES_ZH.get(cat_en, cat_en) if cat_en else ""
    source = item.get("source", "")
    published_at = item.get("publishedAt") or item.get("generatedAt")
    published = fmt_time(published_at) if published_at else ""
    score = item.get("score")
    score_str = f"  💯{score}" if score is not None else ""

    lines = [
        f"{c('1;36', f'[{idx}]')} {c('1;33', title)}{score_str}",
    ]

    # 第二行：元信息（只显示有的字段）
    meta_parts = []
    if cat_zh:
        meta_parts.append(f"🏷️  {c('35', cat_zh)}")
    if published:
        meta_parts.append(f"🕐 {published}")
    if source:
        meta_parts.append(f"📡 {source}")
    if meta_parts:
        lines.append("    " + "  ".join(meta_parts))

    if summary:
        sm = summary[:200] + ("..." if len(summary) > 200 else "")
        lines.append(f"    {sm}")
    if url:
        lines.append(f"    🔗 {c('4', url)}")
    return "\n".join(lines)


def cmd_daily(args):
    """拉日报"""
    if args.date:
        path = f"/api/public/daily/{args.date}"
    else:
        path = "/api/public/daily"
    data = http_get(path)

    date = data.get("date", args.date or "今日")
    print(c("1;32", f"📰 AI 日报 — {date}"))
    print("=" * 60)
    print(f"  生成时间：{fmt_time(data.get('generatedAt', ''))}  "
          f"窗口：{fmt_time(data.get('windowStart', ''))} ~ {fmt_time(data.get('windowEnd', ''))}")
    print()

    # 真实结构: sections: [{label, items: [...]}]
    sections = data.get("sections") or []
    idx = 0
    for sec in sections:
        label = sec.get("label", "")
        items = sec.get("items", [])
        if items:
            print(c("1;35", f"### {label}（{len(items)} 条）"))
            for item in items:
                idx += 1
                print(render_item(item, idx))
                print()

    if not sections:
        print(c("33", "（今天还没有日报，可以试试 items 端点）"))


def cmd_items(args):
    """拉条目（精选/全量）"""
    params = {}
    if args.mode:
        params["mode"] = args.mode
    if args.category:
        params["category"] = args.category
    if args.since:
        params["since"] = parse_since(args.since)
    if args.q:
        params["q"] = args.q
    if args.cursor:
        params["cursor"] = args.cursor

    data = http_get("/api/public/items", params)
    items = data.get("items") or []
    has_next = data.get("hasNext", False)
    next_cursor = data.get("nextCursor")

    print(c("1;32", f"🔥 AIHOT 条目（{len(items)} 条，本页；总池：{data.get('count', '?')}）"))
    print("=" * 60)
    for i, item in enumerate(items[: args.limit], 1):
        print(render_item(item, i))
        print()

    if has_next and next_cursor and not args.no_next_hint:
        print(c("36", f"👉 还有更多，翻页命令："))
        print(f"   python3 fetch_aihot.py items --cursor {next_cursor}")


def cmd_dailies(args):
    """列出最近 N 天日报"""
    data = http_get("/api/public/dailies", {"take": args.take})
    items = data.get("items") or data
    print(c("1;32", f"📅 可用日报列表（最近 {len(items)} 天）"))
    print("=" * 60)
    for d in items:
        if isinstance(d, dict):
            date = d.get("date", "")
            lead = d.get("leadTitle", "")
            print(f"  • {c('33', date)}  {lead}")
        else:
            print(f"  • {d}")


def main():
    ap = argparse.ArgumentParser(
        description="AIHOT API 命令行调用（python4office.cn 定制 Skill 配套）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    # daily
    p_daily = sub.add_parser("daily", help="拉日报（默认今日）")
    p_daily.add_argument("--date", help="指定日期 YYYY-MM-DD")
    p_daily.set_defaults(func=cmd_daily)

    # items
    p_items = sub.add_parser("items", help="拉精选/全量条目")
    p_items.add_argument("--mode", choices=["selected", "all"], default="selected")
    p_items.add_argument("--category", choices=CATEGORIES_EN,
                        help="分类：ai-models / ai-products / industry / paper / tip")
    p_items.add_argument("--since", help="时间窗：24h / 7d / 2w，或 ISO-8601")
    p_items.add_argument("--q", help="关键词搜索")
    p_items.add_argument("--cursor", help="分页 cursor（接上次 nextCursor）")
    p_items.add_argument("--limit", type=int, default=20)
    p_items.add_argument("--no-next-hint", action="store_true")
    p_items.set_defaults(func=cmd_items)

    # dailies
    p_dailies = sub.add_parser("dailies", help="列出可用日报日期")
    p_dailies.add_argument("--take", type=int, default=30)
    p_dailies.set_defaults(func=cmd_dailies)

    args = ap.parse_args()
    try:
        args.func(args)
    except urllib.error.HTTPError as e:
        print(c("1;31", f"❌ HTTP {e.code}: {e.reason}"), file=sys.stderr)
        if e.code == 403:
            print(c("33", "   （403 通常是 User-Agent 被拒，检查 DEFAULT_HEADERS）"), file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(c("1;31", f"❌ 网络错误: {e.reason}"), file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(c("1;31", f"❌ 返回非 JSON: {e}"), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()