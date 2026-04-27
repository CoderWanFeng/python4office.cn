#!/usr/bin/env python3
"""
Hexo to Astro 文章迁移脚本
功能：对比Hexo和Astro站点，自动迁移缺失的文章
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict

# 配置路径
HEXO_PATH = "/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts"
ASTRO_PATH = "/Users/wanfeng/code/opc-website/python4office.cn/astro-site/src/content/blog"

def get_all_md_files(directory, exclude_english=False):
    """获取目录下所有md文件"""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                # 排除英文版本（如果需要）
                if exclude_english and file.endswith('-en.md'):
                    continue
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                md_files.append(relative_path)
    return md_files

def get_category_from_path(hexo_path, relative_path):
    """从Hexo路径提取分类目录"""
    parts = relative_path.split(os.sep)
    if len(parts) > 1:
        category = parts[0]
        # 特殊处理 ads 目录
        if category == 'ads' and len(parts) > 1:
            # ads/ai/xxx.md -> ads/ai/xxx.md
            category = os.path.join(parts[0], parts[1])
        return category
    return 'root'

def extract_astro_category(hexo_relative_path):
    """从Hexo路径提取Astro分类"""
    parts = hexo_relative_path.split(os.sep)

    if parts[0] == 'ads':
        # ads/ai/xxx.md -> ads/ai/xxx.md
        if len(parts) >= 2:
            return os.path.join('ads', parts[1])
        return 'ads'
    elif parts[0] == 'course':
        # course/AI/xxx.md -> 保持 course
        return 'course'
    elif parts[0] == 'ai-skills':
        # ai-skills/xxx.md -> ai-skills/xxx.md
        if len(parts) >= 2:
            return os.path.join('ai-skills', parts[1])
        return 'ai-skills'
    else:
        # 其他目录保持原样
        return parts[0] if parts else 'root'

def create_directory_if_not_exists(path):
    """创建目录（如果不存在）"""
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        return True
    return False

def migrate_files():
    """执行迁移"""
    print("=" * 60)
    print("🔄 Hexo to Astro 文章迁移工具")
    print("=" * 60)

    # 1. 获取Hexo所有文章
    print("\n📂 扫描Hexo站点...")
    hexo_files = get_all_md_files(HEXO_PATH, exclude_english=False)
    print(f"   Hexo文章总数: {len(hexo_files)}")

    # 2. 获取Astro所有文章
    print("\n📂 扫描Astro站点...")
    astro_files = get_all_md_files(ASTRO_PATH, exclude_english=False)
    print(f"   Astro文章总数: {len(astro_files)}")

    # 3. 找出缺失的文章
    print("\n🔍 对比文章...")
    hexo_set = set(hexo_files)
    astro_set = set(astro_files)

    missing_files = hexo_set - astro_set
    print(f"   缺失文章数量: {len(missing_files)}")

    # 4. 按分类统计缺失文章
    category_stats = defaultdict(list)
    for file in missing_files:
        category = extract_astro_category(file)
        category_stats[category].append(file)

    print("\n📊 缺失文章分类统计:")
    print("-" * 60)
    for category, files in sorted(category_stats.items()):
        print(f"  {category}: {len(files)}篇")

    # 5. 执行迁移
    print("\n🚀 开始迁移...")
    migrated_count = 0
    skipped_count = 0
    error_count = 0

    created_dirs = set()

    for file in sorted(missing_files):
        try:
            # 源文件
            src_file = os.path.join(HEXO_PATH, file)

            # 目标文件
            dst_file = os.path.join(ASTRO_PATH, file)

            # 创建目标目录
            dst_dir = os.path.dirname(dst_file)
            if dst_dir not in created_dirs:
                created_dirs.add(dst_dir)
                if create_directory_if_not_exists(dst_dir):
                    pass  # 目录已创建

            # 复制文件
            shutil.copy2(src_file, dst_file)
            migrated_count += 1

        except Exception as e:
            error_count += 1
            print(f"   ❌ 错误: {file} - {str(e)}")

    # 6. 验证结果
    print("\n✅ 迁移完成!")
    print("-" * 60)
    print(f"   成功迁移: {migrated_count}篇")
    print(f"   错误数量: {error_count}篇")

    # 重新统计Astro文章数
    print("\n📊 最终统计:")
    astro_files_after = get_all_md_files(ASTRO_PATH, exclude_english=False)
    print(f"   Astro文章总数: {len(astro_files_after)}")

    # 7. 差异对比
    hexo_after = set(get_all_md_files(HEXO_PATH, exclude_english=False))
    astro_after = set(get_all_md_files(ASTRO_PATH, exclude_english=False))
    still_missing = hexo_after - astro_after

    print(f"   Hexo文章总数: {len(hexo_after)}")
    print(f"   仍有差异: {len(still_missing)}篇")

    if still_missing:
        print("\n⚠️  仍有差异的文章:")
        for file in list(still_missing)[:10]:
            print(f"   - {file}")
        if len(still_missing) > 10:
            print(f"   ... 还有 {len(still_missing) - 10} 篇")

    print("\n" + "=" * 60)
    print("🎉 迁移任务完成!")
    print("=" * 60)

if __name__ == "__main__":
    migrate_files()
