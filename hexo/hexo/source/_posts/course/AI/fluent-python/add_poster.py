# -*- coding: utf-8 -*-
import os

course_dir = r'D:\code\python4office.cn\hexo\hexo\source\_posts\course\AI\fluent-python'
poster = '\n\n![fluent-python.png](https://raw.atomgit.com/user-images/assets/5027920/4f7696ff-fbef-423c-8874-38dfb05b165f/fluent-python.png \'fluent-python.png\')\n'

count = 0
for fname in os.listdir(course_dir):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(course_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 已有的不再重复添加
    if 'atomgit.com/user-images/assets/5027920/4f7696ff' in content:
        print(f'跳过(已有): {fname}')
        continue

    # 去掉末尾换行，加上海报
    content = content.rstrip() + poster

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'已添加: {fname}')
    count += 1

print(f'\n完成，共处理 {count} 个文件')
