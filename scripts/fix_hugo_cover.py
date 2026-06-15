#!/usr/bin/env python3
"""
修复Hugo文章的cover字段格式
- PaperMod主题要求cover字段是对象格式：cover: {image: "url"}
- 而不是字符串：cover: "url"
"""
import re
from pathlib import Path

CONTENT_DIR = Path('/Users/wanfeng/code/opc-website/python4office.cn/hugo/content')

def fix_cover(content):
    """把单行字符串cover改为对象格式cover"""
    # 匹配 cover: "url" 或 cover: 'url' 或 cover: url
    pattern = r'^cover:\s*["\']?(https?://[^"\'\n]+)["\']?\s*$'

    lines = content.split('\n')
    new_lines = []
    for line in lines:
        match = re.match(pattern, line)
        if match:
            url = match.group(1)
            new_lines.append('cover:')
            new_lines.append(f'  image: "{url}"')
            new_lines.append('  alt: "封面"')
            new_lines.append('  caption: ""')
            new_lines.append('  relative: false')
        else:
            new_lines.append(line)
    return '\n'.join(new_lines)

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 解析frontmatter
        match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return False

        old_fm = match.group(1)
        new_fm = fix_cover(old_fm)

        if new_fm == old_fm:
            return False

        new_content = content.replace(f'---\n{old_fm}\n---', f'---\n{new_fm}\n---', 1)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"处理 {file_path} 出错: {e}")
        return False

def main():
    count = 0
    for md_file in CONTENT_DIR.rglob('*.md'):
        if process_file(md_file):
            count += 1
    print(f"✅ 修复了 {count} 篇文章的cover字段格式")

if __name__ == '__main__':
    main()
