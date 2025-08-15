# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：wfdev7
@代码日期    ：2025/8/15 22:48 
@本段代码的视频说明     ：
'''


# 需求：函数返回多个值，忽略中间无用字段
def get_up():
    return '程序员晚枫', 150000, 'ChongQing'


name, _, city = get_up()  # _ 占位忽略粉丝量
print(name, city)

# 只想要首尾，中间全部打包
first, *_, last = get_up()
print(first, last)  # Alice Shanghai
