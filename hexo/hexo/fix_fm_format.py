import os
import re

# 匹配front-matter的正则
fm_pattern = re.compile(r'^---\s*(.*?)\s*---', re.DOTALL)

def fix_front_matter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找front-matter
        match = fm_pattern.match(content)
        if not match:
            return False
        
        fm_content = match.group(1)
        # 按行拆分，去掉空行和首尾空白
        lines = [line.strip() for line in fm_content.split('\n') if line.strip()]
        
        if not lines:
            return False
        
        # 生成标准格式的front-matter
        new_fm = "---\n" + "\n".join(lines) + "\n---\n"
        
        # 替换原内容中的front-matter
        new_content = fm_pattern.sub(new_fm, content, count=1)
        
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
    
    print("开始扫描所有md文件，标准化front-matter格式...\n")
    
    for root, _, files in os.walk('source/_posts'):
        for file in files:
            if file.endswith('.md'):
                total_count += 1
                file_path = os.path.join(root, file)
                if fix_front_matter(file_path):
                    fixed_count += 1
                    # print(f"✅ 修复格式：{file_path}")
    
    print(f"\n处理完成！共扫描 {total_count} 个文件，修复 {fixed_count} 个front-matter格式不规范的文件。")
    print("现在所有文章的front-matter都是标准的无空行格式啦~")
