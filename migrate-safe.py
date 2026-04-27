#!/usr/bin/env python3
import os
import re
import yaml
from pathlib import Path
import shutil

def is_valid_frontmatter(content):
    """检查 frontmatter 是否有效"""
    if content.startswith('\ufeff'):
        content = content[1:]
    
    if not content.startswith('---'):
        return True
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return True
    
    frontmatter = parts[1]
    
    try:
        yaml.safe_load(frontmatter)
        return True
    except:
        return False

def process_directory(source_dir, target_dir):
    """安全地处理整个目录"""
    target_dir.mkdir(parents=True, exist_ok=True)
    problematic_dir = target_dir.parent / 'problematic-files'
    problematic_dir.mkdir(exist_ok=True)
    
    count = 0
    skipped = 0
    
    for md_file in source_dir.rglob('*.md'):
        if '.DS_Store' in str(md_file):
            continue
        
        # 计算相对路径
        rel_path = md_file.relative_to(source_dir)
        target_file = target_dir / rel_path
        
        try:
            # 读取文件
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查
            if is_valid_frontmatter(content):
                # 确保目标目录存在
                target_file.parent.mkdir(parents=True, exist_ok=True)
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
            else:
                # 移到有问题的目录
                problem_file = problematic_dir / rel_path.name
                problem_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(md_file, problem_file)
                skipped += 1
                print(f"⚠️  跳过: {rel_path}")
                
        except Exception as e:
            print(f"❌ 错误 {rel_path}: {e}")
            skipped += 1
    
    print(f"\n✅ 完成: {count} 篇成功迁移, {skipped} 篇跳过")
    print(f"📂 有问题的文件在: {problematic_dir}")

if __name__ == "__main__":
    source_dir = Path("hexo/hexo/source/_posts")
    target_dir = Path("astro-site/src/content/blog")
    
    # 清空目标目录
    if target_dir.exists():
        shutil.rmtree(target_dir)
    
    print(f"从 {source_dir} 安全迁移到 {target_dir}")
    process_directory(source_dir, target_dir)
