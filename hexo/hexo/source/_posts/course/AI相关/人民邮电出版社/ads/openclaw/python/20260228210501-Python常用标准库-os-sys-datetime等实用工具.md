---
title: Python常用标准库：我每天都在用的10个内置模块，效率翻倍
date: 2026-02-28 21:05:00
tags: [Python基础, 标准库, 实用工具]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9209df5a-99d2-40dc-af34-b10b43be9026/12-ai.jpg" />
    </a>   
</p>

<p align="center" name="atomgit">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

上一篇我们学习了函数。今天来介绍**Python标准库**——这是Python内置的工具箱，不用安装就能用。

掌握这些常用模块，你的开发效率会大幅提升。

---

## 1. os - 操作系统接口

```python
import os

# 文件和目录操作
os.getcwd()           # 获取当前工作目录
os.listdir('.')       # 列出目录内容
os.mkdir('new_folder') # 创建目录
os.remove('file.txt')  # 删除文件
os.rename('old.txt', 'new.txt')  # 重命名

# 路径操作（推荐用os.path）
os.path.exists('file.txt')   # 检查是否存在
os.path.isfile('file.txt')   # 是否是文件
os.path.isdir('folder')      # 是否是目录
os.path.join('folder', 'file.txt')  # 拼接路径
os.path.abspath('file.txt')  # 获取绝对路径
```

👉 **[深入学习：Python文件操作10种姿势](/course/AI相关/人民邮电出版社/ads/openclaw/python/20260228185801-Python文件操作-读写文件的10种姿势/)**

---

## 2. sys - 系统相关

```python
import sys

sys.argv        # 命令行参数列表
sys.exit(0)     # 退出程序
sys.platform    # 当前平台（'win32', 'darwin', 'linux'）
sys.version     # Python版本信息

# 修改模块搜索路径
sys.path.append('/my/modules')
```

---

## 3. datetime - 日期和时间

```python
from datetime import datetime, date, timedelta

# 当前时间
now = datetime.now()
print(now)  # 2024-01-15 14:30:00.123456

# 格式化输出
print(now.strftime('%Y-%m-%d %H:%M:%S'))  # 2024-01-15 14:30:00

# 解析字符串为日期
dt = datetime.strptime('2024-01-15', '%Y-%m-%d')

# 日期计算
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)

# 两个日期差
delta = datetime(2024, 12, 31) - now
print(delta.days)  # 距离年底还有多少天
```

---

## 4. json - JSON数据处理

```python
import json

data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "JavaScript"]
}

# Python对象转JSON字符串
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)

# JSON字符串转Python对象
parsed = json.loads(json_str)
print(parsed['name'])  # Alice

# 读写JSON文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open('data.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)
```

---

## 5. random - 随机数

```python
import random

random.random()       # 0到1之间的随机浮点数
random.randint(1, 10) # 1到10之间的随机整数
random.choice(['A', 'B', 'C'])  # 从列表中随机选择
random.shuffle(my_list)  # 打乱列表顺序
random.sample(range(100), 5)  # 从范围内随机选5个不重复的数
```

---

## 6. re - 正则表达式

```python
import re

text = "我的邮箱是 test@example.com"

# 查找邮箱
pattern = r'\w+@\w+\.\w+'
match = re.search(pattern, text)
if match:
    print(match.group())  # test@example.com

# 替换
new_text = re.sub(r'\d+', '***', '电话: 13800138000')
print(new_text)  # 电话: ***
```

👉 **[深入学习：Python正则表达式](/course/AI相关/人民邮电出版社/ads/openclaw/python/20260228190301-Python正则表达式-文本处理的瑞士军刀/)**

---

## 7. collections - 高级数据结构

```python
from collections import Counter, defaultdict, namedtuple

# Counter - 计数器
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
count = Counter(words)
print(count.most_common(2))  # [('apple', 3), ('banana', 2)]

# defaultdict - 带默认值的字典
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1

# namedtuple - 命名元组
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)  # 3 4
```

---

## 8. itertools - 迭代器工具

```python
import itertools

# 无限计数器
for i in itertools.count(10):
    if i > 15:
        break
    print(i)  # 10, 11, 12, 13, 14, 15

# 循环迭代
cycle = itertools.cycle(['A', 'B', 'C'])
for _ in range(5):
    print(next(cycle))  # A, B, C, A, B

# 排列组合
list(itertools.permutations([1, 2, 3]))  # 全排列
list(itertools.combinations([1, 2, 3], 2))  # 两两组合
```

---

## 9. math / statistics - 数学运算

```python
import math
import statistics

math.sqrt(16)        # 开方，4.0
math.ceil(4.2)       # 向上取整，5
math.floor(4.8)      # 向下取整，4
math.pi              # 圆周率
math.e               # 自然常数

data = [1, 2, 3, 4, 5]
statistics.mean(data)    # 平均值，3
statistics.median(data)  # 中位数，3
statistics.stdev(data)   # 标准差
```

---

## 10. logging - 日志记录

```python
import logging

# 配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

# 使用
logging.debug('调试信息')
logging.info('普通信息')
logging.warning('警告信息')
logging.error('错误信息')
logging.critical('严重错误')
```

---

## 实战：综合应用

```python
import os
import json
from datetime import datetime
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)

def backup_config():
    """备份配置文件"""
    config_file = 'config.json'
    
    if not os.path.exists(config_file):
        logging.error(f"配置文件不存在: {config_file}")
        return
    
    # 读取配置
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    # 创建备份文件名
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f'config_backup_{timestamp}.json'
    
    # 保存备份
    with open(backup_name, 'w') as f:
        json.dump(config, f, indent=2)
    
    logging.info(f"配置已备份到: {backup_name}")

backup_config()
```

---

## 下节预告

下一篇我们将进入**实战项目**，把学到的知识用起来。

👉 **[继续阅读：Python实战项目-自动整理下载文件夹](/course/AI相关/人民邮电出版社/ads/openclaw/python/20260228210601-Python实战项目-自动整理下载文件夹/)**

---

## 推荐：AI Python零基础实战营

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)**

---

## 课程导航

**上一篇：** [Python函数基础-从定义到调用](/course/AI相关/人民邮电出版社/ads/openclaw/python/20260228210401-Python函数基础-从定义到调用/)

**下一篇：** [Python实战项目-自动整理下载文件夹](/course/AI相关/人民邮电出版社/ads/openclaw/python/20260228210601-Python实战项目-自动整理下载文件夹/)

---

*PS：标准库是Python的宝藏。熟悉这些模块，能解决80%的日常需求。*
