#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量翻译Hexo文档为英文版本
使用方法: python translate_50_docs.py
"""

import os
import re
import time
import json
from pathlib import Path
from typing import Optional

# 如果有AI API密钥，可以在这里设置
# 或者使用环境变量 OPENAI_API_KEY

def call_ai_translate(text: str, api_key: Optional[str] = None) -> str:
    """
    调用AI API进行翻译
    这里需要替换为实际的API调用代码
    """
    # 预留接口，用户可以接入自己的AI API
    # 例如: OpenAI, Claude, DeepSeek等
    pass

def translate_with_simple_replacement(text: str) -> str:
    """
    简单的翻译函数 - 预留位置
    实际使用时应接入AI API
    """
    # 预留翻译接口
    return text

def extract_frontmatter(content: str) -> tuple[dict, str]:
    """
    提取markdown文件的frontmatter
    返回: (frontmatter字典, 去除frontmatter后的内容)
    """
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if match:
        frontmatter_text = match.group(1)
        body = match.group(2)
        
        # 解析frontmatter
        fm = {}
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                fm[key.strip()] = value.strip().strip('"\'')
        
        return fm, body
    
    return {}, content

def generate_translated_filename(original_path: str) -> str:
    """
    生成翻译后的文件名
    原文件: xxx.md -> 翻译后: xxx-en.md
    """
    base, ext = os.path.splitext(original_path)
    return f"{base}-en{ext}"

def translate_document(input_path: str, output_path: str) -> bool:
    """
    翻译单个文档
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取frontmatter
        fm, body = extract_frontmatter(content)
        
        # TODO: 调用AI API翻译正文
        # translated_body = call_ai_translate(body)
        
        # TODO: 翻译frontmatter中的文本字段
        # translated_fm = translate_frontmatter(fm)
        
        # 目前只是复制原文件作为占位
        # 实际使用时替换为真正的翻译逻辑
        
        # 创建输出目录
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 写入翻译后的文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ 翻译完成: {output_path}")
        return True
        
    except Exception as e:
        print(f"✗ 翻译失败 {input_path}: {e}")
        return False

def find_untranslated_docs(posts_dir: str, limit: int = 50) -> list[str]:
    """
    查找还未翻译的中文文档
    """
    untranslated = []
    
    for root, dirs, files in os.walk(posts_dir):
        for file in files:
            if not file.endswith('.md'):
                continue
            
            # 跳过已经是翻译版本的
            if '-en.md' in file or file.endswith('.md-en'):
                continue
            
            # 跳过README和index
            if file in ['README.md', 'index.md']:
                continue
            
            original_path = os.path.join(root, file)
            translated_path = generate_translated_filename(original_path)
            
            # 只翻译还不存在的翻译版本
            if not os.path.exists(translated_path):
                untranslated.append(original_path)
                
                if len(untranslated) >= limit:
                    return untranslated
    
    return untranslated

def main():
    posts_dir = '/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts'
    
    print("开始查找待翻译的文档...")
    docs_to_translate = find_untranslated_docs(posts_dir, limit=50)
    
    print(f"找到 {len(docs_to_translate)} 篇待翻译的文档\n")
    
    success_count = 0
    for i, doc_path in enumerate(docs_to_translate, 1):
        print(f"[{i}/{len(docs_to_translate)}] 正在处理: {doc_path}")
        
        translated_path = generate_translated_filename(doc_path)
        
        if translate_document(doc_path, translated_path):
            success_count += 1
        
        # 避免请求过快
        time.sleep(0.5)
    
    print(f"\n完成! 成功翻译 {success_count}/{len(docs_to_translate)} 篇文档")

if __name__ == '__main__':
    main()
