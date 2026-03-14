#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

# 需要插入的内容
COURSE_CONTENT = """

---

## 🎓 推荐课程

包含两门：

- [龙虾安装课（9元） 从软件下载、环境配置到完整部署，一步步教到能正常使用，适合只想先把工具装好的朋友。](https://mp.weixin.qq.com/s/xT6p7mHu5o6aMAqeuXQTXg)
- [龙虾高级课（199元，前50名优惠） 0基础也能学，从基础操作到进阶用法，教你真正用起来、提高效率，学完就能上手实操。](https://mp.weixin.qq.com/s/UKSwPXVKIeCn4Gh_Spkdfw)

"""

def insert_course_content(file_path):
    """在文件中插入课程内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已经包含课程内容
        if '龙虾安装课（9元）' in content:
            print(f"跳过 {os.path.basename(file_path)} - 已包含课程内容")
            return False

        # 查找插入位置：在"## 拓展阅读"之前插入
        if '## 拓展阅读' in content:
            # 在"## 拓展阅读"之前插入
            new_content = content.replace('## 拓展阅读', COURSE_CONTENT + '\n## 拓展阅读')
        else:
            # 如果没有"## 拓展阅读"，在文件末尾插入
            new_content = content.rstrip() + COURSE_CONTENT

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✓ 已处理 {os.path.basename(file_path)}")
        return True

    except Exception as e:
        print(f"✗ 处理 {os.path.basename(file_path)} 时出错: {str(e)}")
        return False

def main():
    # 目标文件夹
    target_dir = '/Users/wanfeng/code/python4office.cn/hexo/hexo/source/_posts/course/ai-related/posts-people/ads/openclaw'

    # 获取所有.md文件
    md_files = [f for f in os.listdir(target_dir) if f.endswith('.md')]

    print(f"找到 {len(md_files)} 个Markdown文件")
    print("=" * 50)

    success_count = 0
    skip_count = 0
    error_count = 0

    for filename in sorted(md_files):
        file_path = os.path.join(target_dir, filename)
        result = insert_course_content(file_path)
        if result is True:
            success_count += 1
        elif result is False:
            skip_count += 1
        else:
            error_count += 1

    print("=" * 50)
    print(f"处理完成！")
    print(f"成功: {success_count} 个")
    print(f"跳过: {skip_count} 个（已包含课程内容）")
    print(f"失败: {error_count} 个")

if __name__ == '__main__':
    main()
