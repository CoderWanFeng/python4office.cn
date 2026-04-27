#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def main():
    hexo_posts_dir = Path("hexo/hexo/source/_posts")
    astro_posts_dir = Path("astro-site/src/content/blog")
    
    astro_posts_dir.mkdir(parents=True, exist_ok=True)
    
    count = 0
    for md_file in hexo_posts_dir.rglob("*.md"):
        if ".DS_Store" in str(md_file):
            continue
            
        # 计算相对路径，保持目录结构
        rel_path = md_file.relative_to(hexo_posts_dir)
        target_path = astro_posts_dir / rel_path
        
        # 确保目标目录存在
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 复制文件
        shutil.copy2(md_file, target_path)
        print(f"✓ 迁移: {rel_path}")
        count += 1
    
    print(f"\n🎉 迁移完成！共迁移 {count} 篇文章")
    print(f"   源目录: {hexo_posts_dir}")
    print(f"   目标目录: {astro_posts_dir}")

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    main()
