#!/usr/bin/env python3
"""
Hexo 到 Hugo 文章迁移脚本 V4
正确处理日期格式和所有 front matter
"""

import os
import re
from datetime import datetime

HEXO_POSTS_DIR = '../hexo/hexo/source/_posts'
HUGO_POSTS_DIR = 'content/posts'

def parse_date(date_str):
    """解析各种日期格式，返回 Hugo 标准格式"""
    if not date_str:
        return None

    date_str = date_str.strip().strip('"\'')

    formats = [
        '%Y-%m-%d %H %M %S',
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d %H:%M',
        '%Y-%m-%d',
        '%Y/%m/%d %H %M %S',
        '%Y/%m/%d %H:%M:%S',
        '%Y/%m/%d',
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime('%Y-%m-%dT%H:%M:%S+08:00')
        except:
            continue

    return None

def convert_frontmatter(content):
    """将 Hexo front matter 转换为 Hugo 格式"""
    lines = content.split('\n')
    in_frontmatter = False
    frontmatter_lines = []

    for line in lines:
        stripped = line.strip()

        if stripped == '---':
            if not in_frontmatter:
                in_frontmatter = True
                continue
            else:
                break

        if in_frontmatter:
            frontmatter_lines.append(stripped)

    frontmatter = {}
    current_key = None

    for line in frontmatter_lines:
        if not line:
            continue

        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            if key == 'date':
                parsed_date = parse_date(value)
                if parsed_date:
                    frontmatter[key] = parsed_date
                current_key = None
            elif key == 'tags':
                if value.startswith('['):
                    items = re.findall(r'["\']?([^"\'\[\],]+)["\']?', value)
                    frontmatter[key] = items
                    current_key = 'tags'
                else:
                    current_key = 'tags'
                    frontmatter[key] = []
            elif key == 'categories':
                if value.startswith('['):
                    items = re.findall(r'["\']?([^"\'\[\],]+)["\']?', value)
                    frontmatter[key] = items
                    current_key = 'categories'
                else:
                    current_key = 'categories'
                    frontmatter[key] = []
            else:
                current_key = None
                frontmatter[key] = value
        elif line.startswith('- ') and current_key:
            if current_key in frontmatter:
                if isinstance(frontmatter[current_key], list):
                    frontmatter[current_key].append(line[2:])

    return frontmatter

def process_file(filepath):
    """处理单个文件，转换格式"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '-en.md' in str(filepath):
        return None

    frontmatter = convert_frontmatter(content)

    if not frontmatter or 'title' not in frontmatter:
        return None

    lines = content.split('\n')
    in_frontmatter = False
    content_start = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '---':
            if not in_frontmatter:
                in_frontmatter = True
                continue
            else:
                content_start = i + 1
                break

    body = '\n'.join(lines[content_start:])

    hugo_content = '---\n'
    for key, value in frontmatter.items():
        if isinstance(value, list):
            hugo_content += f'{key}:\n'
            for item in value:
                item = str(item).strip().replace('"', '\\"')
                hugo_content += f'  - "{item}"\n'
        else:
            value = str(value).strip().replace('"', '\\"')
            hugo_content += f'{key}: "{value}"\n'
    hugo_content += '---\n\n'
    hugo_content += body

    return hugo_content

def main():
    print("=" * 50)
    print("Hexo 到 Hugo 文章迁移工具 V4")
    print("=" * 50)

    os.makedirs(HUGO_POSTS_DIR, exist_ok=True)

    total_files = 0
    converted_files = 0
    skipped_files = 0
    errors = []

    for root, dirs, files in os.walk(HEXO_POSTS_DIR):
        for filename in files:
            if not filename.endswith('.md'):
                continue

            if '-en.md' in filename:
                skipped_files += 1
                continue

            total_files += 1
            filepath = os.path.join(root, filename)

            try:
                content = process_file(filepath)

                if content:
                    output_path = os.path.join(HUGO_POSTS_DIR, filename)
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    converted_files += 1

                    if converted_files % 200 == 0:
                        print(f"已转换 {converted_files} 个文件...")

            except Exception as e:
                errors.append(f"{filename}: {str(e)}")

    print("\n" + "=" * 50)
    print("迁移完成！")
    print(f"总文件数: {total_files}")
    print(f"成功转换: {converted_files}")
    print(f"跳过文件: {skipped_files}")
    print(f"错误数量: {len(errors)}")
    print("=" * 50)

    if errors:
        print("\n错误详情:")
        for error in errors[:10]:
            print(f"  - {error}")

if __name__ == '__main__':
    main()