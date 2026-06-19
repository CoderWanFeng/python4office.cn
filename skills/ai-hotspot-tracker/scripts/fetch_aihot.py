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
    python3 fetch_aihot.py items --mode selected --since 24h
    python3 fetch_aihot.py items --category 模型 --since 7d
    python3 fetch_aihot.py items --q "Python 自动化"
    python3 fetch_aihot.py dailies --take 30
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from typing import Any

BASE_URL = "https://aihot.virxact.com"

# 输出美化（关掉就传 --no-color）
USE_COLOR = sys.stdout.isatty()


def c(code: str, text: str) -> str:
    """简单 ANSI 颜色"""
    if not USE_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"


def http_get(path: str, params: dict | None = None, timeout: int = 15) -> dict:
    """发起 GET 请求并返回 JSON"""
    if params:
        # 关键词里的空格用 +（API 文档明确说明）
        qs = urllib.parse.urlencode(params, quote_via=urllib.parse.quote_plus)
        url = f"{BASE_URL}{path}?{qs}"
    else:
        url = f"{BASE_URL}{path}"

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "ai-hotspot-tracker/1.0 (+python4office.cn)"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def parse_since(since: str) -> str:
    """把自然语言时长转 ISO-8601 时间戳（默认 UTC）"""
    now = datetime.now(timezone.utc)
    if since.endswith("h"):
        delta = timedelta(hours=int(since[:-1]))
    elif since.endswith("d"):
        delta = timedelta(days=int(since[:-1]))
    elif since.endswith("w"):
        delta = timedelta(weeks=int(since[:-1]))
    else:
        # 当成 ISO-8601 原样返回
        return since
    return (now - delta).strftime("%Y-%m-%dT%H:%M:%SZ")


def fmt_time(iso: str) -> str:
    """UTC → Asia/Shanghai (UTC+8) 友好显示"""
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        sh = dt.astimezone(timezone(timedelta(hours=8)))
        return sh.strftime("%m-%d %H:%M")
    except Exception:
        return iso


def render_item(item: dict, idx: int) -> str:
    """单条热点的卡片化输出"""
    title = item.get("title", "（无标题）")
    summary = item.get("summary") or item.get("description", "")
    url = item.get("url", "")
    category = item.get("category", "")
    published = fmt_time(item.get("published_at", ""))

    lines = [
        f"{c('1;36', f'[{idx}]')} {c('1;33', title)}",
    ]
    if category:
        lines.append(f"    🏷️  {c('35', category)}  🕐 {published}")
    if summary:
        # 截断过长摘要
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
    print(c("1;32", f"📰 AI 日报 — {data.get('date', args.date or '今日')}"))
    print("=" * 60)
    # 假设返回结构: {"date":..., "sections": [...]} 或扁平 items
    items = data.get("items") or data.get("sections") or []
    for i, item in enumerate(items, 1):
        print(render_item(item, i))
        print()
    if not items:
        print(c("33", "（今天还没有日报，可以试试 selected 端点）"))


def cmd_items(args):
    """拉精选/全量条目"""
    params = {}
    if args.mode:
        params["mode"] = args.mode
    if args.category:
        params["category"] = args.category
    if args.since:
        params["since"] = parse_since(args.since)
    if args.q:
        params["q"] = args.q

    data = http_get("/api/public/items", params)
    items = data.get("items") or data
    print(c("1;32", f"🔥 AIHOT 条目（{len(items)} 条）"))
    print("=" * 60)
    for i, item in enumerate(items[: args.limit], 1):
        print(render_item(item, i))
        print()


def cmd_dailies(args):
    """列出最近 N 天日报（用于发现哪些日期有日报）"""
    data = http_get("/api/public/dailies", {"take": args.take})
    items = data.get("items") or data
    print(c("1;32", f"📅 可用日报列表（最近 {len(items)} 天）"))
    print("=" * 60)
    for d in items:
        if isinstance(d, dict):
            print(f"  • {d.get('date', d)}")
        else:
            print(f"  • {d}")


def main():
    ap = argparse.ArgumentParser(
        description="AIHOT API 命令行调用（python4office.cn 定制 Skill 配套脚本）",
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
    p_items.add_argument("--category", choices=["模型", "产品", "行业", "论文", "技巧"])
    p_items.add_argument("--since", help="时间窗：24h / 7d / 2w，或 ISO-8601")
    p_items.add_argument("--q", help="关键词搜索")
    p_items.add_argument("--limit", type=int, default=20, help="最多展示多少条（默认 20）")
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
        sys.exit(1)
    except urllib.error.URLError as e:
        print(c("1;31", f"❌ 网络错误: {e.reason}"), file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(c("1;31", f"❌ 返回非 JSON: {e}"), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()