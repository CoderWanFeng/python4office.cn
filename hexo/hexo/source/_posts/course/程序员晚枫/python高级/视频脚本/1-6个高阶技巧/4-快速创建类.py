# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：wfdev7
@代码日期    ：2025/8/15 22:47 
@本段代码的视频说明     ：
'''

from dataclasses import dataclass


@dataclass
class UP:
    name: str
    fans: int
    city: str


# 两行搞定__init__/__repr__/__eq__
wfdev7 = UP('程序员晚枫', 150000, '重庆')
print(wfdev7)  # UP(name='程序员晚枫', fans=150000, city='重庆')
