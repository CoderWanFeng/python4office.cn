
import os
import re

# 定义修复映射
fix_map = {
    'photo-151707730': 'photo-1517077304055-8e7232e8e848',
    'photo-152637909': 'photo-1526379095098-d400fd0bf935',
    'photo-149975031': 'photo-1499750310107-5fef28a66643',
    'photo-155128848': 'photo-1551288049-bebda4e38f71',
    'photo-1518709268805-4e6709f4': 'photo-1518709268805-4e9042af9f23'
}

source_dir = r'D:\code\python4office.cn\hexo\hexo\source\_posts'
fixed_count = 0
file_count = 0

for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                for old, new in fix_map.items():
                    content = re.sub(re.escape(old), new, content)
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    fixed_count += 1
                    print(f"Fixed: {file_path}")
                file_count += 1
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print(f"\nDone! Checked {file_count} files, fixed {fixed_count} files.")
