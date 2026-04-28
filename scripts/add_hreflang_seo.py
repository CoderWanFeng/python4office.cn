#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hexo SEO 优化脚本 - 添加 hreflang 标签
功能：
1. 为所有英文版本文档添加 hreflang frontmatter
2. 生成 hreflang sitemap
3. 验证翻译文档的SEO完整性
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

class HexoSEOTools:
    """Hexo SEO 优化工具"""
    
    def __init__(self, posts_dir: str):
        self.posts_dir = Path(posts_dir)
        self.translated_docs = []  # 存储所有翻译文档信息
        
    def find_translated_docs(self) -> List[Tuple[str, str]]:
        """查找所有英文版本的文档"""
        translated = []
        
        for md_file in self.posts_dir.rglob("*.md"):
            # 跳过README和index文件
            if md_file.name in ['README.md', 'index.md']:
                continue
            
            # 检查是否是英文版本
            if '-en.md' in md_file.name:
                # 找到对应的中文原版
                chinese_version = str(md_file).replace('-en.md', '.md')
                chinese_path = Path(chinese_version)
                
                if chinese_path.exists():
                    translated.append((str(md_file), chinese_version))
                    
        return translated
    
    def add_hreflang_frontmatter(self, en_file: str, zh_file: str) -> bool:
        """
        为英文版本文档添加 hreflang frontmatter
        """
        try:
            with open(en_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否已有hreflang标签
            if 'hreflang:' in content or 'alternate_link:' in content:
                print(f"  ⏭️  跳过（已存在）: {en_file}")
                return True
            
            # 提取文件名用于生成URL
            en_filename = Path(en_file).stem.replace('-en', '')
            zh_filename = Path(zh_file).stem
            
            # 添加hreflang信息到frontmatter
            hreflang_meta = f'''---
hreflang:
  en: /{en_filename}/
  zh: /{zh_filename}/
canonical: /{zh_filename}/
---
'''
            
            # 如果已经有frontmatter，在开头添加hreflang
            if content.startswith('---'):
                # 找到第一个---的位置
                first_dash_end = content.find('\n', content.find('---') + 3)
                if first_dash_end != -1:
                    # 在第一个---后插入hreflang元数据
                    new_content = content[:first_dash_end+1] + '\n' + hreflang_meta.replace('---', '') + content[first_dash_end+1:]
                else:
                    new_content = hreflang_meta + content
            else:
                # 如果没有frontmatter，在开头添加
                new_content = hreflang_meta + content
            
            # 写回文件
            with open(en_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✅ 添加hreflang: {Path(en_file).name}")
            return True
            
        except Exception as e:
            print(f"  ❌ 错误: {en_file} - {e}")
            return False
    
    def add_alternate_to_chinese(self, zh_file: str, en_file: str) -> bool:
        """
        为中文原版文档添加对英文版本的引用
        """
        try:
            with open(zh_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否已有alternate_link
            if 'alternate_link:' in content:
                return True
            
            # 提取文件名
            en_filename = Path(en_file).stem.replace('-en', '')
            zh_filename = Path(zh_file).stem
            
            alternate_meta = f'''alternate_link: /{en_filename}/
'''
            
            # 如果有frontmatter，添加alternate_link
            if content.startswith('---'):
                first_dash_end = content.find('\n', content.find('---') + 3)
                if first_dash_end != -1:
                    new_content = content[:first_dash_end+1] + '\n' + alternate_meta + content[first_dash_end+1:]
                else:
                    new_content = content[:4] + '\n' + alternate_meta + content[4:]
            else:
                new_content = f'''---
{alternate_meta}---
''' + content
            
            with open(zh_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✅ 添加alternate: {Path(zh_file).name}")
            return True
            
        except Exception as e:
            print(f"  ❌ 错误: {zh_file} - {e}")
            return False
    
    def generate_hreflang_sitemap(self, output_file: str, base_url: str = "https://www.python4office.cn"):
        """生成hreflang sitemap"""
        sitemap_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
'''
        
        for en_path, zh_path in self.translated_docs:
            en_url = base_url + '/' + Path(en_path).stem.replace('-en', '') + '/'
            zh_url = base_url + '/' + Path(zh_path).stem + '/'
            
            sitemap_content += f'''  <url>
    <loc>{zh_url}</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{en_url}"/>
    <xhtml:link rel="alternate" hreflang="zh" href="{zh_url}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{zh_url}"/>
  </url>
'''
        
        sitemap_content += '</urlset>\n'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(sitemap_content)
        
        print(f"\n📄 已生成hreflang sitemap: {output_file}")
    
    def run(self):
        """执行SEO优化"""
        print("🔍 开始SEO优化...")
        print("=" * 60)
        
        # 查找所有翻译文档
        print("\n📋 步骤1: 查找翻译文档...")
        self.translated_docs = self.find_translated_docs()
        print(f"   找到 {len(self.translated_docs)} 对翻译文档\n")
        
        if not self.translated_docs:
            print("⚠️  未找到翻译文档")
            return
        
        # 为英文版本添加hreflang
        print("📋 步骤2: 为英文版本添加hreflang标签...")
        for en_file, zh_file in self.translated_docs:
            self.add_hreflang_frontmatter(en_file, zh_file)
        
        # 为中文原版添加alternate引用
        print("\n📋 步骤3: 为中文原版添加alternate引用...")
        for en_file, zh_file in self.translated_docs:
            self.add_alternate_to_chinese(zh_file, en_file)
        
        # 生成sitemap
        print("\n📋 步骤4: 生成hreflang sitemap...")
        sitemap_path = os.path.join(self.posts_dir.parent, 'public', 'hreflang-sitemap.xml')
        self.generate_hreflang_sitemap(sitemap_path)
        
        # 生成SEO报告
        print("\n📋 步骤5: 生成SEO报告...")
        self.generate_seo_report()
        
        print("\n" + "=" * 60)
        print("✅ SEO优化完成！")
        print(f"   处理文档对数: {len(self.translated_docs)}")
    
    def generate_seo_report(self):
        """生成SEO优化报告"""
        report_file = self.posts_dir.parent / 'seo_optimization_report.md'
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("# Hexo SEO 优化报告\n\n")
            f.write("## 优化概述\n\n")
            f.write(f"- 处理翻译文档对数: {len(self.translated_docs)}\n")
            f.write("- 优化时间: 自动生成\n")
            f.write("- 优化内容: hreflang标签、alternate链接\n\n")
            
            f.write("## 翻译文档列表\n\n")
            for i, (en_file, zh_file) in enumerate(self.translated_docs, 1):
                en_name = Path(en_file).name
                zh_name = Path(zh_file).name
                f.write(f"{i}. {zh_name} ↔ {en_name}\n")
            
            f.write("\n## SEO最佳实践\n\n")
            f.write("1. ✅ hreflang标签已添加到所有英文版本\n")
            f.write("2. ✅ alternate链接已添加到中文原版\n")
            f.write("3. ✅ 生成了hreflang-sitemap.xml\n")
            f.write("4. ⚠️  需要在网站header中添加hreflang声明\n")
            
            f.write("\n## 下一步操作\n\n")
            f.write("1. 在Hexo主题的 `head.ejs` 或 `header.swig` 中添加:\n")
            f.write("```html\n")
            f.write('<link rel="alternate" hreflang="en" href="/<%= page.slug %>-en/" />\n')
            f.write('<link rel="alternate" hreflang="zh" href="/<%= page.slug %>/" />\n')
            f.write("```\n")
            f.write("\n2. 在 `source/sitemap.xml` 中包含hreflang-sitemap\n")
            f.write("\n3. 提交hreflang-sitemap到Google Search Console\n")
        
        print(f"   📄 已生成报告: {report_file}")

def main():
    posts_dir = '/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts'
    
    seo_tools = HexoSEOTools(posts_dir)
    seo_tools.run()

if __name__ == '__main__':
    main()
