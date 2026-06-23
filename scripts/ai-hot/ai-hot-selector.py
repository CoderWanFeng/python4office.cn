#!/usr/bin/env python3
"""
AI热点选题脚本 - 根据《选题.md》指南自动执行创作流程
从AIHOT获取今日热点，筛选符合条件的选题，创建工作目录
"""

import urllib.request
import urllib.parse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path("/Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn")
HEXO_SOURCE = PROJECT_ROOT / "hexo" / "hexo" / "source"
WORKFLOW_DIR = HEXO_SOURCE / "_posts" / "workflow"

# AIHOT API配置
BASE_URL = 'https://aihot.virxact.com'
HEADERS = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}

def fetch_aihot_data():
    """从AIHOT获取数据"""
    since = (datetime.now(timezone.utc) - timedelta(hours=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
    params = {'mode': 'all', 'since': since}
    
    url = BASE_URL + '/api/public/items'
    if params:
        url += '?' + urllib.parse.urlencode(params)
    
    print(f"正在从AIHOT获取数据: {url}")
    
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as response:
            data = json.loads(response.read())
            items = data.get('items', [])
            print(f"获取到 {len(items)} 条数据")
            return items
    except Exception as e:
        print(f"获取AIHOT数据失败: {e}")
        return []

def filter_today_items(items):
    """过滤出今天的条目（北京时间）"""
    def to_cst(iso):
        dt = datetime.fromisoformat(iso.replace('Z', '+00:00'))
        return dt.astimezone(timezone(timedelta(hours=8)))
    
    today = datetime.now(timezone(timedelta(hours=8))).date().isoformat()
    today_items = []
    
    for item in items:
        pub = item.get('publishedAt', '')
        if not pub:
            continue
        
        try:
            cst = to_cst(pub)
            if cst.date().isoformat() == today:
                item['cst_time'] = cst.strftime('%H:%M')
                today_items.append(item)
        except Exception as e:
            print(f"解析时间失败 {pub}: {e}")
    
    print(f"今天有 {len(today_items)} 条热点")
    return today_items

def evaluate_item(item):
    """评估条目是否符合选题标准"""
    # 核心2问评估
    title = item.get('title', '')
    description = item.get('description', '')
    content = f"{title} {description}"
    
    # 问题1: 大众能听懂吗？
    # 简单评估：检查是否包含过于专业的术语
    technical_terms = ['transformer', 'attention', 'backpropagation', 'gradient', 'neural network']
    is_understandable = True
    for term in technical_terms:
        if term.lower() in content.lower():
            is_understandable = False
            break
    
    # 问题2: 能解释一个热门AI知识/原理吗？
    # 检查是否涉及热门AI概念
    ai_concepts = ['token', 'llm', 'rag', 'agent', 'context', 'prompt', 'fine-tuning', 'embedding']
    can_explain = any(concept in content.lower() for concept in ai_concepts)
    
    # 加分项评估
    has_code = 'code' in content.lower() or 'github' in content.lower() or 'script' in content.lower()
    is_free = 'free' in content.lower() or '开源' in content or '免费' in content
    has_big_company = any(company in content.lower() for company in ['openai', 'google', 'meta', 'microsoft', '字节', '美团', '阿里', '腾讯', '百度'])
    
    score = item.get('score', 0)
    
    return {
        'item': item,
        'is_understandable': is_understandable,
        'can_explain': can_explain,
        'has_code': has_code,
        'is_free': is_free,
        'has_big_company': has_big_company,
        'score': score,
        'meets_core': is_understandable and can_explain
    }

def select_best_item(evaluations):
    """选择最佳条目"""
    # 优先选择符合核心2问的条目
    core_items = [e for e in evaluations if e['meets_core']]
    
    if not core_items:
        print("警告：没有符合核心2问的条目")
        return None
    
    # 按评分排序
    core_items.sort(key=lambda x: x['score'], reverse=True)
    
    # 优先选择有加分项的
    for item in core_items:
        if item['has_code'] and item['is_free'] and item['has_big_company']:
            # 生成选题理由
            reasons = []
            reasons.append(f"✅ **大众能听懂**：标题和内容易懂，不需要专业背景")
            reasons.append(f"✅ **能解释热门AI知识**：借热点讲清一个AI原理/概念")
            if item['has_code']:
                reasons.append(f"✅ **代码可复现**：读者可以跟着操作")
            if item['is_free']:
                reasons.append(f"✅ **免费属性**：读者能直接受益")
            if item['has_big_company']:
                reasons.append(f"✅ **大厂背书**：传播力强，搜索友好")
            item['selection_reason'] = "\n".join(reasons)
            return item
    
    # 返回评分最高的
    best = core_items[0]
    reasons = []
    reasons.append(f"✅ **大众能听懂**：标题和内容易懂")
    reasons.append(f"✅ **能解释热门AI知识**：借热点讲清一个AI原理/概念")
    if best['has_code']:
        reasons.append(f"✅ **代码可复现**")
    if best['is_free']:
        reasons.append(f"✅ **免费属性**")
    if best['has_big_company']:
        reasons.append(f"✅ **大厂背书**")
    best['selection_reason'] = "\n".join(reasons)
    return best

def create_slug(title):
    """从标题生成slug"""
    import re
    # 移除特殊字符，保留中文、英文、数字、空格
    slug = re.sub(r'[^\w\u4e00-\u9fff\s-]', '', title)
    # 将空格和中文标点替换为短横线
    slug = re.sub(r'[\s\u3000\u3001\u3002\uff0c\uff1b\uff1a\u201c\u201d\uff08\uff09\u300a\u300b\u3008\u3009\u3010\u3011\u300e\u300f\u300c\u300d\ufe43\ufe44\u3014\u3015\u2026\u2014\u2015]+', '-', slug)
    # 移除多余的短横线
    slug = re.sub(r'-+', '-', slug)
    # 转换为小写
    slug = slug.lower()
    # 移除首尾的短横线
    slug = slug.strip('-')
    
    # 如果slug为空或太短，使用时间戳
    if not slug or len(slug) < 3:
        slug = f"ai-hot-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    return slug

def save_daily_hotspots(today_items):
    """保存每日热点汇总到文件"""
    today = datetime.now().strftime('%Y%m%d')
    daily_dir = WORKFLOW_DIR / "每日热点"
    daily_dir.mkdir(parents=True, exist_ok=True)
    
    daily_file = daily_dir / f"{today}.md"
    
    # 如果文件不存在，先写入 Hexo Front Matter + 文件头
    if not daily_file.exists():
        # 生成标准时间
        now = datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        time_str = now.strftime('%H:%M:%S')
        
        # Hexo Front Matter 格式
        front_matter = f"""---
title: 每日AI热点汇总 · {date_str}
date: {date_str} {time_str}
tags: [每日AI热点, 内部文档]
categories: [工作流程, AI热点汇总]
cover: https://images.unsplash.com/photo-1611162600?w=1200&auto=format&fit=crop
description: AIHOT 每日热点自动汇总，{date_str} 当天共采集 {len(today_items)} 条
---

# 每日AI热点汇总 · {date_str}

> 自动收集于 {date_str} {time_str}
> 数据源：[AIHOT](https://aihot.virxact.com)
> 文件用途：每日选题参考，可直接用作内部追溯

"""
        with open(daily_file, 'w', encoding='utf-8') as f:
            f.write(front_matter)
    
    # 去重：基于标题去重
    existing_titles = set()
    with open(daily_file, 'r', encoding='utf-8') as f:
        content = f.read()
        # 提取已有标题（用 ## 标记）
        import re
        for match in re.finditer(r'## \d+\.\s+(.+)', content):
            existing_titles.add(match.group(1).strip())
    
    # 当前时间
    current_time = datetime.now().strftime('%H:%M:%S')
    
    # 构建新增内容
    new_content_lines = []
    new_content_lines.append(f"\n\n## 更新于 {current_time}\n")
    
    added_count = 0
    skipped_count = 0
    
    for idx, item in enumerate(today_items, 1):
        title = item.get('title', '无标题').strip()
        
        # 跳过已存在的
        if title in existing_titles:
            skipped_count += 1
            continue
        
        score = item.get('score', 0)
        pub_time = item.get('cst_time', '未知')
        source = item.get('source', item.get('sourceName', '未知来源'))
        url = item.get('url', item.get('link', ''))
        description = item.get('description', item.get('summary', ''))
        
        new_content_lines.append(f"### {added_count + 1}. {title}\n")
        new_content_lines.append(f"- **AIHOT 评分**：{score}")
        new_content_lines.append(f"- **发布时间**：{pub_time}")
        new_content_lines.append(f"- **来源**：{source}")
        if url:
            new_content_lines.append(f"- **链接**：{url}")
        if description:
            # 限制简介长度
            desc_clean = description.replace('\n', ' ').strip()
            if len(desc_clean) > 200:
                desc_clean = desc_clean[:200] + "..."
            new_content_lines.append(f"- **简介**：{desc_clean}")
        new_content_lines.append("")
        
        existing_titles.add(title)
        added_count += 1
    
    # 如果一个都没新增（全部重复）
    if added_count == 0:
        new_content_lines.append(f"> ⚠️ 本次采集的 {len(today_items)} 条热点全部已存在，无新增内容\n")
    else:
        new_content_lines.append(f"\n> 本次新增 {added_count} 条，跳过重复 {skipped_count} 条\n")
    
    new_content = "\n".join(new_content_lines)
    
    # 追加写入文件
    with open(daily_file, 'a', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\n✅ 每日热点已保存: {daily_file}")
    print(f"   新增 {added_count} 条，跳过重复 {skipped_count} 条")
    
    return str(daily_file)

def create_directories(slug, selected_item):
    """创建工作目录"""
    today = datetime.now().strftime('%Y%m%d')
    
    # 公众号目录
    wechat_dir = WORKFLOW_DIR / "公众号" / "task" / slug
    wechat_dir.mkdir(parents=True, exist_ok=True)
    
    # 口播稿目录
    voiceover_dir = WORKFLOW_DIR / "口播稿" / "task" / slug / "Process"
    voiceover_dir.mkdir(parents=True, exist_ok=True)
    
    # 创建口播稿子目录（7个步骤）
    subdirs = [
        "1-准备口播稿",
        "2-选模板定视觉规范", 
        "3-生成封面",
        "4-写动画",
        "5-合成配音",
        "6-注入渲染",
        "7-拼发布包"
    ]
    
    for subdir in subdirs:
        (voiceover_dir / subdir).mkdir(parents=True, exist_ok=True)
    
    # 创建公众号文章文件（带元数据）
    wechat_file = wechat_dir / f"{today}-{slug}.md"
    
    # 获取AIHOT评分
    score = selected_item['score']
    source_date = datetime.now().strftime('%Y-%m-%d')
    item = selected_item['item']
    
    # 提取链接和简介
    item_url = item.get('url', item.get('link', item.get('sourceUrl', '')))
    item_description = item.get('description', item.get('summary', item.get('content', '')))
    item_source = item.get('source', item.get('sourceName', ''))
    
    # 元数据 + 选题理由 + 链接 + 简介（不含创作内容）
    metadata = f"""> 选题来源：AIHOT {source_date}（评分 {score}）
> 栏目：AI 热点大白话（B2B 挂钩）
> 目标平台：python4office.cn 公众号

# {item.get('title', '标题待定')}

## 为什么选题

{selected_item.get('selection_reason', '符合核心2问：大众能听懂 + 能解释热门AI知识')}

- **评分**：{score}
- **符合核心2问**：{'是' if selected_item.get('meets_core') else '否'}
- **加分项**：代码={selected_item.get('has_code', False)}, 免费={selected_item.get('is_free', False)}, 大厂={selected_item.get('has_big_company', False)}

## 选题链接

- **AIHOT 永久页**：{item.get('permanentUrl', item.get('aihotUrl', f'https://aihot.virxact.com/items/{slug}'))}
- **原文链接**：{item_url if item_url else '暂无'}
- **来源**：{item_source if item_source else '暂无'}

## 选题简介

{item_description if item_description else '暂无简介'}

---

> ⚠️ **以下内容由作者按《公众号内容的创作指南.md》人工创作，不要用脚本生成**
"""
    
    with open(wechat_file, 'w', encoding='utf-8') as f:
        f.write(metadata)
    
    print(f"创建公众号文章: {wechat_file}")
    
    # 创建口播稿文件
    voiceover_file = voiceover_dir / "1-准备口播稿" / f"{today}-{slug}.md"
    
    voiceover_content = f"""> 选题来源：AIHOT {source_date}（评分 {score}）
> 栏目：AI 热点大白话（B2B 挂钩）
> 目标平台：小红书/抖音/视频号

# {item.get('title', '标题待定')}

## 为什么选题

{selected_item.get('selection_reason', '符合核心2问：大众能听懂 + 能解释热门AI知识')}

- **评分**：{score}
- **符合核心2问**：{'是' if selected_item.get('meets_core') else '否'}
- **加分项**：代码={selected_item.get('has_code', False)}, 免费={selected_item.get('is_free', False)}, 大厂={selected_item.get('has_big_company', False)}

## 选题链接

- **AIHOT 永久页**：{item.get('permanentUrl', item.get('aihotUrl', f'https://aihot.virxact.com/items/{slug}'))}
- **原文链接**：{item_url if item_url else '暂无'}
- **来源**：{item_source if item_source else '暂无'}

## 选题简介

{item_description if item_description else '暂无简介'}

---

> ⚠️ **以下内容由作者按《口播稿内容的创作指南.md》人工创作，不要用脚本生成**
"""
    
    with open(voiceover_file, 'w', encoding='utf-8') as f:
        f.write(voiceover_content)
    
    print(f"创建口播稿文件: {voiceover_file}")
    
    # 创建segments.txt文件
    segments_file = voiceover_dir / "1-准备口播稿" / "segments.txt"
    with open(segments_file, 'w', encoding='utf-8') as f:
        f.write("# 口播稿分段 (由作者按《口播稿内容的创作指南.md》人工创作)\n")
        f.write("# 每段带 [emotion] 标签，按 TTS 拆段规范执行\n")
        f.write("# 1. [excited] Hook: 3秒吸引注意力\n")
        f.write("# 2. [neutral] 正文第一部分\n")
        f.write("# 3. [neutral] 正文第二部分\n")
        f.write("# 4. [excited] 结尾: 行动号召\n")
    
    print(f"创建分段文件: {segments_file}")
    
    return {
        'slug': slug,
        'wechat_dir': str(wechat_dir),
        'voiceover_dir': str(voiceover_dir),
        'wechat_file': str(wechat_file),
        'voiceover_file': str(voiceover_file),
        'title': selected_item['item'].get('title', '')
    }

def main():
    """主函数"""
    print("=" * 60)
    print("AI热点选题脚本 v1.0")
    print("=" * 60)
    
    # 1. 获取AIHOT数据
    items = fetch_aihot_data()
    if not items:
        print("未获取到数据，退出")
        return
    
    # 2. 过滤今天条目
    today_items = filter_today_items(items)
    if not today_items:
        print("今天没有热点条目，退出")
        return
    
    # 2.5 保存每日热点汇总（新增功能）
    daily_file = save_daily_hotspots(today_items)
    
    # 3. 评估每个条目
    print("\n评估条目...")
    evaluations = []
    for item in today_items:
        eval_result = evaluate_item(item)
        evaluations.append(eval_result)
        
        if eval_result['meets_core']:
            print(f"✓ {item.get('title', '无标题')} (评分: {eval_result['score']})")
    
    # 4. 选择最佳条目
    selected = select_best_item(evaluations)
    if not selected:
        print("没有合适的选题，退出")
        return
    
    selected_item = selected['item']
    print(f"\n选中选题: {selected_item.get('title', '无标题')}")
    print(f"评分: {selected['score']}")
    print(f"符合核心2问: {selected['meets_core']}")
    print(f"加分项: 代码={selected['has_code']}, 免费={selected['is_free']}, 大厂={selected['has_big_company']}")
    
    # 5. 创建slug
    slug = create_slug(selected_item.get('title', 'ai-hot'))
    print(f"生成slug: {slug}")
    
    # 6. 创建工作目录
    print("\n创建工作目录...")
    result = create_directories(slug, selected)
    
    print("\n" + "=" * 60)
    print("选题完成！")
    print("=" * 60)
    print(f"选题标题: {result['title']}")
    print(f"Slug: {result['slug']}")
    print(f"公众号目录: {result['wechat_dir']}")
    print(f"口播稿目录: {result['voiceover_dir']}")
    print(f"公众号文章: {result['wechat_file']}")
    print(f"口播稿文件: {result['voiceover_file']}")
    print("\n下一步:")
    print("1. 编辑公众号文章: workflow/公众号/task/{slug}/")
    print("2. 编辑口播稿: workflow/口播稿/task/{slug}/Process/1-准备口播稿/")
    print("3. 按各自指南完成创作")
    print("=" * 60)

if __name__ == "__main__":
    main()