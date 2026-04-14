import os
import re
from pathlib import Path

def check_hexo_format(file_path):
    """检查文件是否符合 hexo 格式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否有 front matter（以 --- 开头）
        if not content.startswith('---'):
            return False, "缺少 front matter 开头"
        
        # 检查是否有 front matter 结束
        first_end = content.find('---', 3)
        if first_end == -1:
            return False, "front matter 缺少结束标记"
        
        # 提取 front matter 内容
        front_matter = content[3:first_end]
        
        # 检查是否包含必要的字段
        if 'title:' not in front_matter:
            return False, "front matter 缺少 title 字段"
        
        if 'date:' not in front_matter:
            return False, "front matter 缺少 date 字段"
        
        return True, "格式正确"
    
    except Exception as e:
        return False, f"读取文件出错: {str(e)}"

def find_all_md_files(directory):
    """递归查找所有 md 文件"""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def main():
    posts_dir = '/home/admin/openclaw/workspace/code/python4office.cn/hexo/hexo/source/_posts'
    
    print("正在检查所有 md 文件...")
    print("=" * 80)
    
    md_files = find_all_md_files(posts_dir)
    print(f"共找到 {len(md_files)} 个 md 文件\n")
    
    invalid_files = []
    
    for i, file_path in enumerate(md_files, 1):
        is_valid, message = check_hexo_format(file_path)
        
        if not is_valid:
            relative_path = os.path.relpath(file_path, posts_dir)
            invalid_files.append((relative_path, message))
            print(f"❌ {i}. {relative_path}")
            print(f"   问题: {message}\n")
    
    print("=" * 80)
    print(f"\n检查完成！")
    print(f"✓ 符合格式: {len(md_files) - len(invalid_files)} 个")
    print(f"✗ 不符合格式: {len(invalid_files)} 个")
    
    if invalid_files:
        print("\n不符合格式的文件列表：")
        for i, (path, msg) in enumerate(invalid_files, 1):
            print(f"{i}. {path} - {msg}")
    
    return invalid_files

if __name__ == '__main__':
    main()
