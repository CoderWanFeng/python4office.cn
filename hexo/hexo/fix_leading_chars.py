import os
import re

# 匹配开头的所有不可见字符（包括零宽空格、BOM、制表符、换行等）
leading_invisible_pattern = re.compile(r'^[\s\ufeff\u200b\u200c\u200d\u2060]+')

def fix_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换开头的不可见字符
        new_content = leading_invisible_pattern.sub('', content)
        
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"❌ 处理失败：{file_path}，错误：{e}")
        return False

if __name__ == "__main__":
    fixed_count = 0
    total_count = 0
    
    print("开始扫描所有md文件，清理开头不可见字符...\n")
    
    for root, _, files in os.walk('source/_posts'):
        for file in files:
            if file.endswith('.md'):
                total_count += 1
                file_path = os.path.join(root, file)
                if fix_file(file_path):
                    fixed_count += 1
                    print(f"✅ 修复：{file_path}")
    
    print(f"\n处理完成！共扫描 {total_count} 个文件，修复 {fixed_count} 个有问题的文件。")
    print("现在页面上的无题文章应该都恢复正常显示标题了~")
