# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：wfdev7
@代码日期    ：2025/8/15 22:44 
@本段代码的视频说明     ：
'''

import functools
import time
from potime import RunTime


@RunTime
@functools.lru_cache(maxsize=None)  # 无限缓存
def slow_func(x):
    time.sleep(5)  # 一些很慢的逻辑
    return x * x


print(slow_func(10))  # 第一次1秒
print(slow_func(10))  # 第二次直接读缓存，毫秒级
