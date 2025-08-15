# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：wfdev7
@代码日期    ：2025/8/15 22:44 
@本段代码的视频说明     ：
'''


# 需求：大文件切片不复制
with open('big.bin', 'rb') as f:
    mm = memoryview(f.read())  # 零拷贝视图

# 只要前1MB与后1MB拼接，不额外占内存
new_data = mm[:1024 * 1024] + mm[-1024 * 1024:]
print(len(new_data))

# 需求：读取百万行日志，统计含“ERROR”的行数
# 传统写法，先把所有行读到内存
with open('晚枫的100G日志.log') as f:
    lines = f.readlines()
error_lines = [l for l in lines if 'ERROR' in l]

# 高阶写法：把 [] 换成 ()，边读边算，内存恒稳
error_lines = (l for l in open('晚枫的100G日志.log') if 'ERROR' in l)
print(sum(1 for _ in error_lines))     # 直接计数不占内存


