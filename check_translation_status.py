#!/usr/bin/env python3
"""
检查 ads 目录下哪些中文 md 文件还没有对应的英文版，并更新 TASK_TRANSLATE.md
"""
import os
import re

ADS_DIR = "/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads"

def find_untranslated_files():
    """找出所有没有对应 -en.md 的中文 md 文件"""
    all_md_files = []
    untranslated = []
    
    # 遍历所有 md 文件
    for root, dirs, files in os.walk(ADS_DIR):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                all_md_files.append(full_path)
    
    # 检查哪些是中文文件（不是 -en.md）
    chinese_files = [f for f in all_md_files if not f.endswith('-en.md')]
    
    # 检查每个中文文件是否有对应的英文版
    for chinese_file in chinese_files:
        # 构造对应的英文文件名
        dir_name = os.path.dirname(chinese_file)
        base_name = os.path.basename(chinese_file)
        en_file = os.path.join(dir_name, base_name.replace('.md', '-en.md'))
        
        if not os.path.exists(en_file):
            untranslated.append(chinese_file)
    
    return untranslated, len(chinese_files), len(all_md_files)

def update_task_file(untranslated, total_chinese, total_files):
    """更新 TASK_TRANSLATE.md 文件"""
    task_file = os.path.join(ADS_DIR, "TASK_TRANSLATE.md")
    
    # 计算已完成数量
    completed = total_chinese - len(untranslated)
    
    content = f"""# 批量翻译任务说明

## 目标
将当前目录下的中文 Markdown 文件批量翻译为英文，生成 `-en.md` 后缀的英文版本。

## 目录路径
```
{ADS_DIR}
```

## 文件统计
- 总计 {total_chinese} 个中文 Markdown 文件需要翻译
- 已完成：{completed} 个（截至 2026-04-23）
- 剩余：{len(untranslated)} 个

## 最新进度
- 2026-04-23：完成 `atomgit` 目录下全部 8 个中文文件的翻译，新增 8 个英文版本
- 2026-04-23：完成 `deepseek` 目录下全部 8 个中文文件的翻译，新增 8 个英文版本
- 2026-04-23：完成 `xunfei` 目录下全部 6 个中文文件的翻译，新增 6 个英文版本
- 2026-04-23：完成 `ai` 目录下全部 7 个中文文件的翻译，新增 7 个英文版本
- 2026-04-23：完成 `ai-agent` 目录下全部 3 个中文文件的翻译，新增 3 个英文版本
- 2026-04-23：完成 `aliyun` 目录下全部 10 个中文文件的翻译，新增 10 个英文版本
- 2026-04-23：完成 `tencent` 目录下全部 10 个中文文件的翻译，新增 10 个英文版本

## 翻译方案
- 使用 **MyMemory API**（免费，https://mymemory.translated.net）
- 调用命令：
  ```bash
  python3 batch_translate.py "{ADS_DIR}" 0.3
  ```
- 进程 PID：8739
- 日志文件：`/Users/wanfeng/code/opc-website/python4office.cn/translate.log`

## 输出文件命名规则
- 原文：`xxx.md`
- 译文：`xxx-en.md`

## 监控命令
```bash
# 查看已翻译数量
ls {ADS_DIR}/**/*-en.md 2>/dev/null | wc -l

# 查看日志
tail -20 /Users/wanfeng/code/opc-website/python4office.cn/translate.log

# 停止翻译
pkill -f batch_translate.py
```

## 待翻译文件列表
"""
    
    # 添加待翻译文件列表
    for f in sorted(untranslated):
        content += f"{f}\n"
    
    with open(task_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"任务文件已更新：{task_file}")
    print(f"总计：{total_chinese} 个中文文件")
    print(f"已完成：{completed} 个")
    print(f"待翻译：{len(untranslated)} 个")

if __name__ == "__main__":
    untranslated, total_chinese, total_files = find_untranslated_files()
    update_task_file(untranslated, total_chinese, total_files)
