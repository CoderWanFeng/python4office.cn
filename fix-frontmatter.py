#!/usr/bin/env python3
import os
import re
from pathlib import Path

def fix_frontmatter(content):
    """修复 frontmatter 格式问题"""
    # 分离 frontmatter 和内容
    if content.startswith('\ufeff'):
        content = content[1:]  # 移除 BOM
    
    if not content.startswith('---'):
        return content
    
    # 找到 frontmatter 的结束位置
    parts = content.split('---', 2)
    if len(parts) < 3:
        return content
    
    frontmatter = parts[1]
    body = parts[2]
    
    # 修复常见格式问题
    lines = frontmatter.split('\n')
    fixed_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 修复 tags 混合格式问题
        if line.strip().startswith('tags:') and ('[' in line and ']' not in line or ':' in line.split('tags:', 1)[1]):
            # 处理 tags 行后面跟着缩进列表的情况
            tag_line = line.strip()
            if '[' in tag_line and ']' not in tag_line:
                # 数组格式但不完整
                fixed_lines.append(line)
            elif ':' in tag_line.split('tags:', 1)[1].strip():
                # 混合格式，重新整理
                fixed_lines.append('tags:')
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
        
        i += 1
    
    fixed_frontmatter = '\n'.join(fixed_lines)
    return '---' + fixed_frontmatter + '---' + body

def process_directory(source_dir, target_dir):
    """处理整个目录"""
    target_dir.mkdir(parents=True, exist_ok=True)
    
    count = 0
    fixed_count = 0
    
    for md_file in source_dir.rglob('*.md'):
        if '.DS_Store' in str(md_file):
            continue
        
        # 计算相对路径
        rel_path = md_file.relative_to(source_dir)
        target_file = target_dir / rel_path
        
        # 确保目标目录存在
        target_file.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            # 读取文件
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 修复
            fixed_content = fix_frontmatter(content)
            
            # 写入
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            if fixed_content != content:
                fixed_count += 1
            
            count += 1
            
        except Exception as e:
            print(f"⚠️  处理 {rel_path} 时出错: {e}")
            # 直接复制原文件
            import shutil
            shutil.copy2(md_file, target_file)
            count += 1
    
    print(f"✅ 处理完成: {count} 篇文章，修复 {fixed_count} 篇")

if __name__ == "__main__":
    source_dir = Path("hexo/hexo/source/_posts")
    target_dir = Path("astro-site/src/content/blog")
    
    print(f"从 {source_dir} 迁移到 {target_dir}")
    process_directory(source_dir, target_dir)
