#!/usr/bin/env python3
"""
Hexo文章迁移到Hugo脚本
功能：转换Front-matter格式，把Hexo的tags/categories/cover等字段，转为Hugo的标准格式
"""
import os
import re
from pathlib import Path
from datetime import datetime

HEXO_POSTS_DIR = Path('/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts')
HUGO_CONTENT_DIR = Path('/Users/wanfeng/code/opc-website/python4office.cn/hugo-site/content/posts')

def parse_hexo_frontmatter(content):
    """解析Hexo文章的frontmatter部分"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return None, content
    return match.group(1), match.group(2)

def convert_to_hugo(hexo_fm, body):
    """将Hexo frontmatter转换为Hugo格式"""
    lines = hexo_fm.split('\n')
    hugo_data = {
        'title': '',
        'date': '',
        'tags': [],
        'categories': [],
        'cover': '',
        'draft': False,
    }

    current_key = None
    for line in lines:
        line = line.rstrip()
        if not line:
            continue
        # 尝试匹配 key: value
        kv_match = re.match(r'^(\w+):\s*(.*)$', line)
        if kv_match:
            key = kv_match.group(1)
            value = kv_match.group(2).strip()
            current_key = key
            if key in ('tags', 'categories'):
                if value:
                    hugo_data[key] = [value]
                else:
                    hugo_data[key] = []
            elif key == 'cover':
                hugo_data['cover'] = value
            elif key in hugo_data:
                hugo_data[key] = value
            else:
                hugo_data[key] = value
        # 列表项 - xxx
        elif line.startswith('  - ') or line.startswith('- '):
            value = re.sub(r'^\s*-\s*', '', line).strip()
            if current_key in ('tags', 'categories'):
                hugo_data[current_key].append(value)

    # 构建Hugo frontmatter
    fm_parts = ['---']
    fm_parts.append(f'title: "{hugo_data["title"].strip()}"')
    if hugo_data['date']:
        fm_parts.append(f'date: {hugo_data["date"]}')
    if hugo_data['tags']:
        tags_str = ', '.join(f'"{t}"' for t in hugo_data['tags'])
        fm_parts.append(f'tags: [{tags_str}]')
    if hugo_data['categories']:
        cats_str = ', '.join(f'"{c}"' for c in hugo_data['categories'])
        fm_parts.append(f'categories: [{cats_str}]')
    if hugo_data['cover']:
        fm_parts.append(f'cover:\n  image: "{hugo_data["cover"]}"\n  alt: "封面"')
    fm_parts.append('draft: false')
    fm_parts.append('---')

    return '\n'.join(fm_parts) + '\n\n' + body

def migrate_post(src_file, dst_file):
    """迁移单篇文章"""
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()
    fm, body = parse_hexo_frontmatter(content)
    if fm is None:
        return False, "无frontmatter"
    new_content = convert_to_hugo(fm, body)
    dst_file.parent.mkdir(parents=True, exist_ok=True)
    with open(dst_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True, "迁移成功"

def main():
    # 先获取所有最新的md文件，按修改时间排序
    all_posts = []
    for md_file in HEXO_POSTS_DIR.rglob('*.md'):
        if '-en.md' in md_file.name:
            continue
        # 跳过.workbuddy等特殊目录
        if '.workbuddy' in str(md_file) or '/memory/' in str(md_file):
            continue
        all_posts.append((md_file, os.path.getmtime(md_file)))
    all_posts.sort(key=lambda x: x[1], reverse=True)

    # 验证版本：先迁移最近的10篇
    test_count = 10
    migrated = 0
    print(f"=== 验证版迁移：迁移最新 {test_count} 篇文章 ===\n")

    for src_file, _ in all_posts[:test_count]:
        # 保持原始相对路径结构
        rel_path = src_file.relative_to(HEXO_POSTS_DIR)
        dst_file = HUGO_CONTENT_DIR / rel_path
        ok, msg = migrate_post(src_file, dst_file)
        status = "✅" if ok else "❌"
        print(f"{status} {rel_path}: {msg}")
        if ok:
            migrated += 1

    print(f"\n✅ 迁移完成：{migrated}/{test_count} 篇文章")

if __name__ == '__main__':
    main()
