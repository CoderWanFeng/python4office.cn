#!/usr/bin/env python3
"""
自动给Hexo文章添加封面图片脚本
匹配规则：根据文章文件名关键词自动匹配对应的免费商用图片（来自unsplash/pexels）
运行方式：python3 scripts/add_article_covers.py
"""
import os
import re
from pathlib import Path
from datetime import datetime

# 文章主题和对应的图片链接（全部来自unsplash免费商用图库）
COVER_MAPPING = {
    # 开发/编程相关
    'github': 'https://images.unsplash.com/photo-1618401479379-e8fd5e49a025?q=80&w=1200&auto=format&fit=crop',
    'git': 'https://images.unsplash.com/photo-1618401479379-e8fd5e49a025?q=80&w=1200&auto=format&fit=crop',
    'code': 'https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop',
    'python': 'https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop',
    'pycharm': 'https://images.unsplash.com/photo-1626968301924-901294f75607?q=80&w=1200&auto=format&fit=crop',
    'plugin': 'https://images.unsplash.com/photo-1626968301924-901294f75607?q=80&w=1200&auto=format&fit=crop',
    'hexo': 'https://images.unsplash.com/photo-1547658719-da2b51169186?q=80&w=1200&auto=format&fit=crop',
    'mongodb': 'https://images.unsplash.com/photo-1554080353-a576cf803bda?q=80&w=1200&auto=format&fit=crop',
    'spark': 'https://images.unsplash.com/photo-1655636044795-5cc862885966?q=80&w=1200&auto=format&fit=crop',
    'datav': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop',
    'data': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop',
    
    # AI相关
    'ai': 'https://images.unsplash.com/photo-1677442136019-235d647109c6?q=80&w=1200&auto=format&fit=crop',
    'chatgpt': 'https://images.unsplash.com/photo-1677442136019-235d647109c6?q=80&w=1200&auto=format&fit=crop',
    'robot': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1200&auto=format&fit=crop',
    'cup': 'https://images.unsplash.com/photo-1677442136019-235d647109c6?q=80&w=1200&auto=format&fit=crop',
    
    # 地点相关
    'chongqing': 'https://images.unsplash.com/photo-1579208578152-875549830880?q=80&w=1200&auto=format&fit=crop',
    
    # 内容类型
    'course': 'https://images.unsplash.com/photo-1501504905252-473c47e087f8?q=80&w=1200&auto=format&fit=crop',
    '1w-hours': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1200&auto=format&fit=crop',
    'book': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd?q=80&w=1200&auto=format&fit=crop',
    'nav': 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=1200&auto=format&fit=crop',
    'baiss': 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=1200&auto=format&fit=crop',
    'wemedia': 'https://images.unsplash.com/photo-1611162617474-528ee0916c11?q=80&w=1200&auto=format&fit=crop',
    'wechat': 'https://images.unsplash.com/photo-1511707171731-15ed56c6f5a5?q=80&w=1200&auto=format&fit=crop',
    'download': 'https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop',
    
    # 默认图片
    'default': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop'
}

def process_post(file_path):
    """处理单篇文章，添加封面"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找frontmatter部分
        match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return False, "无frontmatter"
        
        frontmatter = match.group(1)
        
        # 检查是否已有cover字段
        if 'cover:' in frontmatter:
            return False, "已有封面"
        
        # 匹配最相关的图片
        filename = os.path.basename(file_path).lower()
        cover_url = COVER_MAPPING['default']
        matched_key = 'default'
        
        for key in COVER_MAPPING:
            if key in filename:
                cover_url = COVER_MAPPING[key]
                matched_key = key
                break
        
        # 在frontmatter添加cover字段
        new_frontmatter = frontmatter + f"\ncover: {cover_url}"
        new_content = content.replace(match.group(0), f'---\n{new_frontmatter}\n---')
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True, f"匹配关键词: {matched_key}"
        return False, "无修改"
    except Exception as e:
        return False, f"出错: {str(e)}"

def main():
    posts_dir = Path('/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts')
    
    # 获取所有md文件
    all_posts = list(posts_dir.rglob('*.md'))
    # 按修改时间排序，最新的在前
    all_posts.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    
    success_count = 0
    skip_count = 0
    log_entries = []
    run_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"=== 开始处理文章封面，共找到 {len(all_posts)} 篇文章 ===")
    
    for post_path in all_posts:
        relative_path = str(post_path.relative_to(posts_dir))
        print(f"处理: {relative_path}")
        success, msg = process_post(post_path)
        
        if success:
            success_count += 1
            log_entries.append(f"✅ 成功 | {relative_path} | {msg}")
        else:
            skip_count += 1
            log_entries.append(f"❌ 跳过 | {relative_path} | {msg}")
    
    # 生成日志
    log_file = Path('/Users/wanfeng/code/opc-website/python4office.cn/scripts/cover_logs.txt')
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n=== 执行时间: {run_time} ===\n")
        f.write(f"处理总数: {len(all_posts)} 篇 | 成功添加: {success_count} 篇 | 跳过: {skip_count} 篇\n")
        for entry in log_entries:
            f.write(f"{entry}\n")
    
    print(f"\n✅ 处理完成！")
    print(f"总文章数: {len(all_posts)}")
    print(f"成功添加封面: {success_count} 篇")
    print(f"跳过: {skip_count} 篇（已有封面或无frontmatter）")
    print(f"详细日志已保存到: scripts/cover_logs.txt")
    print("\n下次运行直接执行: python3 scripts/add_article_covers.py")

if __name__ == '__main__':
    main()
