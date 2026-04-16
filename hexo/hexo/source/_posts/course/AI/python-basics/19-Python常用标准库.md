---
title: Python常用标准库：我每天都在用的10个内置模块，效率翻倍
date: 2026-02-28 21:05:00
tags: [Python基础, 标准库, 实用工具]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://www.bilibili.com/cheese/play/ss982042944'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
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
<a href="https://www.bilibili.com/cheese/play/ss982042944">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

上篇我们学习了函数。今天来介绍**Python标准库**——这是Python自带的"工具箱"，不用安装，导入就能用。

我每天工作至少用10个标准库。学会它们，你的开发效率会大幅提升。

---

## 为什么学标准库？

想象你搬家，需要：
- 打包箱子（os）
- 查日历算日期（datetime）
- 随机抽签决定谁搬重物（random）
- 读写合同文件（json）

如果这些都要自己造轮子，会累死。好消息是：**Python已经帮你造好了这些轮子，直接用！**

---

## 1. os - 操作系统接口

管文件、管目录，样样精通。

### 场景：看看今天下载文件夹里有什么

```python
import os

# 当前目录
print(os.getcwd())

# 列出文件
files = os.listdir(".")
print("当前目录的文件：")
for f in files:
    print(f"  - {f}")

# 创建文件夹
os.mkdir("test_folder")

# 检查文件存在吗？
print(os.path.exists("test_folder"))  # True
print(os.path.isfile("test.py"))      # False
print(os.path.isdir("test_folder"))   # True
```

**运行结果：**

```
C:\Users\admin\project
当前目录的文件：
  - test.py
  - main.py
  - README.md
  - test_folder
True
False
True
```

---

## 2. datetime - 日期和时间

处理日期、时间、算天数差。

### 场景：距离过年还有多少天？

```python
from datetime import datetime, timedelta

# 当前时间
now = datetime.now()
print(f"现在是：{now}")

# 格式化输出（好看）
print(now.strftime("%Y年%m月%d日 %H:%M:%S"))

# 算天数
target = datetime(2027, 1, 29)  # 2027年春节
delta = target - now
print(f"距离过年还有 {delta.days} 天")

# 加减日期
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print(f"明天是：{tomorrow.strftime('%Y-%m-%d')}")
```

**运行结果：**

```
现在是：2026-04-16 14:45:00.123456
2026年04月16日 14:45:00
距离过年还有 288 天
明天是：2026-04-17
```

---

## 3. json - 数据处理

存数据、读数据，JSON是互联网通用格式。

### 场景：保存和读取用户配置

```python
import json

# 要保存的数据
user_config = {
    "username": "张三",
    "theme": "dark",
    "notifications": True,
    "languages": ["Python", "JavaScript"]
}

# 保存到文件（格式化后好看）
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(user_config, f, ensure_ascii=False, indent=2)

# 读取回来
with open("config.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"用户名：{loaded['username']}")
print(f"主题：{loaded['theme']}")
```

**运行结果：**

```
用户名：张三
主题：dark
```

> 💡 **小技巧**：`indent=2` 让JSON格式化后好看，`ensure_ascii=False` 让中文正常显示。

---

## 4. random - 随机数

抽奖、摇号、模拟测试，随机数用处大。

### 场景：年会抽奖

```python
import random

# 员工名单
employees = ["张三", "李四", "王五", "赵六", "钱七", "孙八"]

# 随机抽一个
lucky = random.choice(employees)
print(f"幸运员工：{lucky}")

# 随机抽3个（不重复）
winners = random.sample(employees, 3)
print(f"中奖的3位：{winners}")

# 随机打乱顺序（抽签顺序）
order = employees.copy()
random.shuffle(order)
print(f"抽签顺序：{order}")

# 随机整数（掷骰子）
dice = random.randint(1, 6)
print(f"掷出的点数：{dice}")
```

**运行结果（每次不同）：**

```
幸运员工：王五
中奖的3位：['钱七', '张三', '孙八']
抽签顺序：['赵六', '钱七', '王五', '张三', '孙八', '李四']
掷出的点数：4
```

---

## 5. sys - 系统相关

查看Python版本、退出程序、修改模块路径。

### 查看Python环境

```python
import sys

print(f"Python版本：{sys.version}")
print(f"当前平台：{sys.platform}")
print(f"命令行参数：{sys.argv}")
print(f"模块搜索路径数量：{len(sys.path)}")
```

**运行结果：**

```
Python版本：3.11.1 (tags/v3.11.1:a0e29fc, Jan 15 2024, 11:53:16) [MSC v.1928 64 bit (AMD64)]
当前平台：win32
命令行参数：['app.py']
模块搜索路径数量：45
```

---

## 6. pathlib - 路径操作（推荐用这个）

比os.path更优雅的路径处理方式。

### 场景：批量处理文件

```python
from pathlib import Path

# 当前目录的更优雅写法
home = Path.home()
downloads = home / "Downloads"

# 遍历所有图片文件
pics = list(downloads.glob("*.jpg")) + list(downloads.glob("*.png"))
print(f"下载文件夹里有 {len(pics)} 张图片")

# 创建子目录
new_folder = downloads / "整理" / "图片"
new_folder.mkdir(parents=True, exist_ok=True)
print(f"已创建：{new_folder}")

# 检查文件属性
readme = Path("README.md")
print(f"README.md 存在吗？{readme.exists()}")
print(f"文件大小：{readme.stat().st_size} 字节")
```

**运行结果：**

```
下载文件夹里有 23 张图片
已创建：C:\Users\admin\Downloads\整理\图片
README.md 存在吗？True
文件大小：1523 字节
```

---

## 7. collections - 特殊数据结构

一些有用的数据结构工具。

### 场景：统计词频

```python
from collections import Counter

# 一段文字
text = "python java python go python rust java python"

# 统计每个词出现几次
words = text.split()
counter = Counter(words)

print("词频统计：")
for word, count in counter.most_common():
    print(f"  {word}: {count}次")

# 最常见的2个
print(f"\n最常见的2个：{counter.most_common(2)}")
```

**运行结果：**

```
词频统计：
  python: 4次
  java: 2次
  go: 1次
  rust: 1次

最常见的2个：[('python', 4), ('java', 2)]
```

---

## 8. re - 正则表达式

文本处理的瑞士军刀。

### 场景：从文本中提取手机号

```python
import re

text = "我的手机是13800138000，还有18512345678，紧急联系13999999999"

# 找出所有手机号（中国大陆）
phones = re.findall(r'1[3-9]\d{9}', text)
print(f"找到的手机号：{phones}")

# 验证邮箱格式
email = "user@example.com"
pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
is_valid = bool(re.match(pattern, email))
print(f"{email} 是有效邮箱吗？{is_valid}")
```

**运行结果：**

```
找到的手机号：['13800138000', '18512345678', '13999999999']
user@example.com 是有效邮箱吗？True
```

---

## 9. math - 数学运算

开方、绝对值、三角函数等。

### 场景：计算圆面积和两点距离

```python
import math

# 圆面积
radius = 5
area = math.pi * radius ** 2
print(f"半径{radius}的圆，面积：{area:.2f}")

# 两点之间的距离（勾股定理）
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"点(0,0)到点(3,4)的距离：{distance}")

# 向上取整、向下取整
print(f"向上取整 4.3 = {math.ceil(4.3)}")
print(f"向下取整 4.7 = {math.floor(4.7)}")
```

**运行结果：**

```
半径5的圆，面积：78.54
点(0,0)到点(3,4)的距离：5.0
向上取整 4.3 = 5
向下取整 4.7 = 4
```

---

## 10. itertools - 迭代器工具

生成排列、组合、无限序列。

### 场景：生成密码字典

```python
import itertools

# 数字组合（0000-9999）
codes = itertools.product('01', repeat=4)
for i, code in enumerate(codes):
    print(''.join(code), end=' ')
    if i >= 10:  # 只展示前11个
        print('...')
        break
```

**运行结果：**

```
0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 ...
```

---


---

## 📚 推荐：Python 零基础实战营

**系统学习Python，推荐这个免费入门课程 👇**

| 特点 | 说明 |
|-----|------|
| 🎯 专为0基础设计 | 门槛低，上手快 |
| 📹 配套视频讲解 | 配合文章学习效果更好 |
| 💬 专属答疑群 | 遇到问题有人带 |
| 🎁 实体书赠送 | 优秀学员送《Python编程从入门到实践》 |

👉 **[点击免费领取 Python 零基础实战营](https://appycyfaqcq1951.pc.xiaoe-tech.com/p/t_pc/goods_pc_detail/goods_detail/course_38vSeD9XU0XdsWnT6jLTaDeRxjT?channel_id=1515397)**


## 本讲小结

| 模块 | 用途 | 常用函数 |
|-----|------|---------|
| `os` | 文件/目录操作 | `listdir`, `mkdir`, `path.exists` |
| `datetime` | 日期时间 | `now`, `strftime`, `timedelta` |
| `json` | 数据格式转换 | `dump`, `load` |
| `random` | 随机数 | `choice`, `sample`, `randint` |
| `pathlib` | 路径操作 | `glob`, `mkdir`, `stat` |
| `collections` | 特殊数据结构 | `Counter`, `defaultdict` |
| `re` | 正则表达式 | `findall`, `match`, `sub` |
| `math` | 数学运算 | `sqrt`, `pi`, `ceil`, `floor` |

---

## 下节预告

标准库学完了，下一篇开始**实战项目**，把学到的知识用起来！

👉 **[继续阅读：Python实战项目-自动整理下载文件夹](./20-Python实战项目-自动整理下载文件夹.md)**

---

## 课程导航

**上一篇：** [Python函数基础](./06-Python函数基础.md)

**下一篇：** [Python实战项目-自动整理下载文件夹](./20-Python实战项目-自动整理下载文件夹.md)

---

*PS：标准库是Python自带的"百宝箱"。用好了这些工具，效率翻倍！*

