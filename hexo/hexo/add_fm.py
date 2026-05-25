import os
import re

# 匹配文件名的正则：20260406-14-ppt.md
filename_pattern = re.compile(r'(\d{8})-(\d+)-(.+?)(-en)?\.md')

# 默认封面图
default_cover = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop"

# 获取无front-matter的文件
def get_no_fm_files(limit=10, only_zh=True):
    files = []
    for root, _, filenames in os.walk('source/_posts/ai-skills/course-beginner-to-pro'):
        for filename in filenames:
            if filename.endswith('.md'):
                if only_zh and filename.endswith('-en.md'):
                    continue
                    
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    if not first_line.startswith('---'):
                        files.append(file_path)
                        if len(files) >= limit:
                            return files
    return files

# 处理单个文件
def process_file(file_path):
    filename = os.path.basename(file_path)
    match = filename_pattern.match(filename)
    if not match:
        print(f"跳过不匹配的文件名：{filename}")
        return False
    
    date_str, lesson_num, title_part, en_suffix = match.groups()
    # 格式化日期
    year = date_str[:4]
    month = date_str[4:6]
    day = date_str[6:8]
    formatted_date = f"{year}-{month}-{day} 00:00:00"
    
    # 生成标题
    # 把文件名的短标题转为友好标题
    title_mapping = {
        'ppt': 'PPT 智能生成 Skill 开发',
        'word': 'Word 文档智能处理 Skill 开发',
        'excel': 'Excel 批量自动化 Skill 开发',
        'pdf': 'PDF 全功能处理 Skill 开发',
        'email': '邮件自动处理 Skill 开发',
        'ocr': 'OCR 文字识别 Skill 开发',
        'web-crawler': '网页数据爬取 Skill 开发',
        'data-analysis': '数据分析可视化 Skill 开发',
        'core-concepts': 'AI Skill 核心概念',
        'hello-world': '第一个 Skill 开发实战',
        'interaction-design': 'Skill 交互设计原则',
        'coze-deep-dive': 'Coze 平台深入解析',
        'coze-practice': 'Coze 平台实战开发',
        'openclaw-deep-dive': 'OpenClaw 平台深入解析',
        'openclaw-practice': 'OpenClaw 平台实战开发',
        'feishu-deep-dive': '飞书开放平台深入解析',
        'feishu-practice': '飞书 Skill 实战开发',
        'security': 'Skill 安全开发最佳实践',
        'data': 'Skill 数据处理与存储',
        'multi-platform': '多平台适配与发布',
        'performance': 'Skill 性能优化',
        'hr-req': 'HR 招聘 Skill 需求分析',
        'hr-dev': 'HR 招聘 Skill 开发实战',
        'finance-req': '财务自动化 Skill 需求分析',
        'finance-dev': '财务自动化 Skill 开发实战',
        'review': '项目实战总结与复盘',
        'testing': 'Skill 测试与调试',
        'deployment': 'Skill 部署与发布',
        'analytics': 'Skill 数据分析与迭代',
        'branding': '个人品牌与 Skill 推广',
        'business': '商业模式与商业化',
        'pricing': 'Skill 定价策略',
        'customer-service': '客户服务与售后',
    }
    
    title = title_mapping.get(title_part.lower(), title_part.replace('-', ' ').title())
    full_title = f"第 {int(lesson_num)} 讲：{title}"
    
    # 读取原内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成front-matter
    fm = f"""---
title: "{full_title}"
date: {formatted_date}
tags: ["AI Skill", "课程", "实战"]
categories: ["AI Skills 课程"]
cover: {default_cover}
---

"""
    
    # 写入新内容
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fm + content)
    
    print(f"✅ 已处理：{filename} -> {full_title}")
    return True

if __name__ == "__main__":
    files = get_no_fm_files(limit=10)
    print(f"找到 {len(files)} 个待处理文件\n")
    
    for file in files:
        process_file(file)
    
    print("\n处理完成！")
