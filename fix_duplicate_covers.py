import os
import re

# 要删除的重复cover行
duplicate_cover = 'cover: https://images.unsplash.com/photo-1518709268805-4e6709f4?w=800&h=400&fit=crop'

def fix_duplicate_covers(file_path):
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否包含重复的cover行
        if duplicate_cover not in content:
            return False
        
        # 删除重复的cover行
        lines = content.split('\n')
        new_lines = []
        skip_next = False
        
        for i, line in enumerate(lines):
            if line.strip() == duplicate_cover:
                # 检查这一行前面是否有cover行
                if i > 0 and 'cover:' in lines[i-1] and lines[i-1].strip().startswith('cover:'):
                    print(f"删除重复cover: {os.path.basename(file_path)}")
                    continue
            new_lines.append(line)
        
        new_content = '\n'.join(new_lines)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"处理文件失败: {file_path}, 错误: {e}")
        return False

def main():
    files = [
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\project-updates\20260423231924-openclaw-update.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\project-updates\20260423224808-openclaw-update.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\project-updates\20260423195604-openclaw-update.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\project-updates\20260419120911-openclaw-update.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\project-updates\20260413000641-openclaw-update.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\course\AI\ai-basic-concepts\29-claude.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ai-tools\tool-reviews\trae\20260412-trae-vs-cursor-windsurf-en.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ai-tools\tool-reviews\trae\20260412-trae-real-project-crawler-en.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ai-tools\tool-reviews\trae\20260412-trae-free-vs-paid.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ai-tools\tool-reviews\trae\20260412-trae-alternative-volc-coding-plan.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ai-tools\tool-reviews\trae\20260412-trae-free-vs-paid-en.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ai-tools\tool-reviews\trae\20260412-trae-alternative-volc-coding-plan-en.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ai-tools\20260415-ai-tools-nav-100-plus.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ai-tools\20260415-ai-tools-nav-100-plus-en.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\tencent\tokenplan\20260422-tokenplan-for-student.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\tencent\tokenplan\20260416-claude-code-tokenplan-model.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\tencent\tokenplan\20260416-claude-code-tokenplan-free.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\tencent\tokenplan\20260416-claude-code-tokenplan-cheaper.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\tencent\tokenplan\20260411-mbti-ai-coding-5-faq.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\tencent\tokenplan\20260411-mbti-ai-coding-4-comparison.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\tencent\tokenplan\20260411-mbti-ai-coding-3-business.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\tencent\tokenplan\20260411-mbti-ai-coding-2-tutorial.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\tencent\tokenplan\20260411-mbti-ai-coding-1-intro.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\tencent\openclaw\20260408-tencent-openclaw-deploy.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\minimax\20260422-minimax-vs-volcengine-en.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\bytedance\huoshan\20260416-claude-code-free.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\bytedance\huoshan\20260416-claude-code-huoshan-model.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\bytedance\huoshan\20260416-claude-code-cheaper.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\bytedance\huoshan\20260413-ark-coding-plan-price-rise-all.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\bytedance\huoshan\20260413-ark-coding-plan-price-increase-reason.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\ads\bytedance\huoshan\20260413-ark-coding-plan-copilot-hard-to-use.md",
        r"d:\code\python4office.cn\hexo\hexo\source\_posts\github-profile.md",
    ]
    
    fixed_count = 0
    for file_path in files:
        if fix_duplicate_covers(file_path):
            fixed_count += 1
    
    print(f"\n修复完成！共修复 {fixed_count} 个文件。")

if __name__ == "__main__":
    main()
