# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：wfdev7
@代码日期    ：2025/8/15 22:42 
@本段代码的视频说明     ：
'''




from collections import Counter

text = '''
Python 自动化 晚枫 python-office 办公 python-office Python 自动化 python-office 自动化 办公 晚枫 程序员 晚枫 python-office
'''

# 一行出词频排行榜
top3 = Counter(text.split()).most_common(3)
print(top3)  # [('python-office', 4), ('自动化', 3), ('晚枫', 3)]