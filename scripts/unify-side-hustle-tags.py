#!/usr/bin/env python3
"""统一专栏目录的 tags 体系（默认作用于 course/side-hustle）。

用法：
    python3 scripts/unify-side-hustle-tags.py [目标目录]
    # 不传参默认 hexo/hexo/source/_posts/course/side-hustle

规则：
  - 所有文章固定包含：副业、副业信息差
  - 删除泛化标签：项目、副业项目
  - 归一化：AI、AI制作课程 -> ai（与 _config.yml 的 tag_map 保持一致）
  - 其余有信息量的主题标签原样保留
仅替换 frontmatter 中的 tags 行，不改动正文与其它字段。脚本幂等，可重复执行。

注意：本脚本只改 frontmatter，不碰文件名。改文件名会改变线上 URL
（permalink 的 :title 取 slug = 文件路径），可能导致已分发链接 404。
"""
import re
import sys
from pathlib import Path

DEFAULT_ROOT = (
    Path(__file__).resolve().parents[1]
    / "hexo/hexo/source/_posts/course/side-hustle"
)

BASE = ["副业", "副业信息差"]
DROP = {"项目", "副业项目"}
NORMALIZE = {"AI": "ai", "AI制作课程": "ai"}
ORDER = BASE + ["ai", "程序员", "变现", "赚钱", "自媒体", "公众号", "公众号文章", "流量主", "法律", "合规"]

PATTERN = re.compile(r"^tags:\s*\[(.*?)\]\s*$", re.MULTILINE)


def order_key(tag: str) -> tuple:
    return (ORDER.index(tag), "") if tag in ORDER else (len(ORDER), tag)


def build(raw: str) -> list:
    tags = []
    for item in raw.split(","):
        t = item.strip().strip('"').strip("'")
        if not t:
            continue
        t = NORMALIZE.get(t, t)
        if t in DROP or t in BASE:
            continue
        if t not in tags:
            tags.append(t)
    merged = BASE + tags
    return sorted(merged, key=order_key)


def main() -> int:
    if len(sys.argv) > 1:
        root = Path(sys.argv[1]).expanduser().resolve()
    else:
        root = DEFAULT_ROOT
    if not root.is_dir():
        print(f"目录不存在: {root}")
        return 1
    print(f"目标目录: {root}\n")

    changed = 0
    files = 0
    for path in sorted(root.rglob("*.md")):
        files += 1
        text = path.read_text(encoding="utf-8")
        m = PATTERN.search(text)
        if not m:
            print(f"  跳过（无 tags 行）: {path.relative_to(root)}")
            continue
        new_tags = build(m.group(1))
        new_line = f"tags: [{', '.join(new_tags)}]"
        if m.group(0) == new_line:
            continue
        path.write_text(text[: m.start()] + new_line + text[m.end():], encoding="utf-8")
        changed += 1
        print(f"  ✓ {path.relative_to(root)}")
        print(f"      {m.group(0).strip()}  ->  {new_line}")
    print(f"\n扫描 {files} 个文件，修改 {changed} 个")
    return 0


if __name__ == "__main__":
    sys.exit(main())
