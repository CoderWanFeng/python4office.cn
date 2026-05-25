import os
import re

# 匹配front-matter的正则
front_matter_pattern = re.compile(r'^---\s*(.*?)\s*---', re.DOTALL)
title_pattern = re.compile(r'title:\s*(["\']?)(.*?)\1\s*$', re.MULTILINE)

# 遍历所有md文件
for root, dirs, files in os.walk('source/_posts'):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read(5000)  # 只读前5000字符，足够包含front-matter
                    
                    # 查找front-matter
                    fm_match = front_matter_pattern.match(content)
                    if fm_match:
                        fm_content = fm_match.group(1)
                        # 查找title
                        title_match = title_pattern.search(fm_content)
                        if not title_match or not title_match.group(2).strip():
                            print(f"❌ 无标题文章：{file_path}")
                    else:
                        # 没有front-matter
                        print(f"⚠️  无front-matter：{file_path}")
            except Exception as e:
                print(f"❌ 读取失败：{file_path}，错误：{e}")
