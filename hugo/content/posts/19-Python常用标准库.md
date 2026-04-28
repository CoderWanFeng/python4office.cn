---
title: "Python常用标准库：我每天都在用的10个内置模块，效率翻倍"
date: "2026-02-28T21:05:00+08:00"
tags:
  - "Python基础"
  - "标准库"
  - "实用工具"
---


<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw'>
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
<a href="https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

你有没有这样的经历？写了一半代码突然发现——要操作文件，`os`模块怎么写来着？要处理日期，`datetime`又要查文档？要解析JSON，到底用`json.load`还是`json.loads`？

说实话，我刚开始学Python的时候，每次用到标准库都要翻文档，效率低得要命。后来我强迫自己把这10个最常用的标准库全部吃透，现在写代码行云流水，再也不用来回查了。

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

### 标准库 vs 第三方库，区别在哪？

很多同学搞不清楚标准库和第三方库的区别，这里说清楚：

| 对比项 | 标准库 | 第三方库 |
|-------|--------|---------|
| 安装方式 | Python自带，无需安装 | 需要`pip install` |
| 示例 | os, json, datetime | requests, pandas, flask |
| 稳定性 | Python官方维护，非常稳定 | 社区维护，版本变化大 |
| 兼容性 | 随Python版本走 | 可能有不兼容问题 |

> 💡 **我的建议**：能用标准库解决的就别装第三方库。少一个依赖，少一个坑。

---

## 1. os - 操作系统接口

管文件、管目录，样样精通。这是我用得最多的标准库，没有之一。

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

### 进阶用法：环境变量和路径拼接

```python
import os

# 读取环境变量
home = os.environ.get('HOME')  # Mac/Linux
userprofile = os.environ.get('USERPROFILE')  # Windows
print(f"用户目录：{home or userprofile}")

# 路径拼接（不要手动拼！跨平台会出问题）
config_path = os.path.join(home, '.config', 'myapp', 'settings.json')
print(f"配置文件路径：{config_path}")

# 获取文件名和扩展名
filepath = "/home/user/docs/report.pdf"
print(f"文件名：{os.path.basename(filepath)}")    # report.pdf
print(f"目录名：{os.path.dirname(filepath)}")      # /home/user/docs
print(f"文件名+扩展名：{os.path.splitext('report.pdf')}")  # ('report', '.pdf')

# 递归遍历目录
for root, dirs, files in os.walk("."):
    for f in files:
        print(os.path.join(root, f))
```

### 避坑指南

```python
import os

# ❌ 错误：手动拼接路径（Windows用\，Mac用/）
path = home + "/Downloads/test.txt"  # Mac能跑，Windows可能翻车

# ✅ 正确：用os.path.join
path = os.path.join(home, "Downloads", "test.txt")

# ❌ 错误：直接用os.mkdir创建多层目录
os.mkdir("a/b/c")  # 如果a/b不存在，直接报错！

# ✅ 正确：用os.makedirs
os.makedirs("a/b/c", exist_ok=True)  # 递归创建，已存在也不报错
```

---

## 2. datetime - 日期和时间

处理日期、时间、算天数差。做报表、做定时任务都离不开它。

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

### 进阶用法：字符串和日期互转

```python
from datetime import datetime

# 字符串 → datetime（解析日期字符串）
date_str = "2026-04-16"
dt = datetime.strptime(date_str, "%Y-%m-%d")
print(f"解析结果：{dt}，类型：{type(dt)}")

# datetime → 字符串（格式化输出）
formatted = dt.strftime("%Y年%m月%d日 星期%w")
print(f"格式化后：{formatted}")

# 常用格式化符号
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))   # 2026-04-16 14:45:00
print(datetime.now().strftime("%Y/%m/%d"))              # 2026/04/16
print(datetime.now().strftime("%B %d, %Y"))             # April 16, 2026
```

### 实战：计算工作日天数

```python
from datetime import datetime, timedelta

def count_workdays(start_date, end_date):
    """计算两个日期之间的工作日天数"""
    workdays = 0
    current = start_date
    while current <= end_date:
        # 0=周一, 4=周五, 5=周六, 6=周日
        if current.weekday() < 5:
            workdays += 1
        current += timedelta(days=1)
    return workdays

start = datetime(2026, 4, 1)
end = datetime(2026, 4, 30)
print(f"4月工作日：{count_workdays(start, end)}天")
# 输出：4月工作日：22天
```

### 避坑指南

```python
from datetime import datetime

# ❌ 错误：直接比较字符串格式的日期
"2026-04-16" > "2026-04-15"  # 碰巧可以，但不靠谱

# ✅ 正确：转成datetime再比较
datetime(2026, 4, 16) > datetime(2026, 4, 15)  # 始终正确

# ❌ 错误：忘记时区问题
# 服务器可能在不同时区，datetime.now()取的是本地时间

# ✅ 正确：用UTC时间
from datetime import timezone
utc_now = datetime.now(timezone.utc)
print(f"UTC时间：{utc_now}")
```

---

## 3. json - 数据处理

存数据、读数据，JSON是互联网通用格式。做配置文件、API接口、数据存储都离不开它。

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

### 进阶用法：字符串和JSON互转

```python
import json

# JSON字符串 → Python对象
json_str = '{"name": "晚枫", "skills": ["Python", "AI"]}'
data = json.loads(json_str)
print(f"名字：{data['name']}，技能：{data['skills']}")

# Python对象 → JSON字符串
person = {"name": "晚枫", "age": 30, "is_dev": True}
json_text = json.dumps(person, ensure_ascii=False, indent=2)
print(json_text)
```

### load vs loads，dump vs dumps——别再搞混了！

| 函数 | 作用 | 记忆方法 |
|-----|------|---------|
| `json.load(f)` | 从**文件**读取JSON | load = 从文件**加载** |
| `json.loads(s)` | 从**字符串**读取JSON | **s** = **s**tring |
| `json.dump(obj, f)` | 写入**文件** | dump = 倒入文件 |
| `json.dumps(obj)` | 转成**字符串** | **s** = **s**tring |

### 避坑指南

```python
import json

# ❌ 错误：JSON不支持Python的元组、集合
data = {"tags": {1, 2, 3}}  # set不能序列化！
json.dumps(data)  # TypeError!

# ✅ 正确：先转成列表
data = {"tags": list({1, 2, 3})}

# ❌ 错误：文件没加encoding，中文乱码
with open("data.json", "w") as f:  # Windows下中文可能乱码
    json.dump(data, f)

# ✅ 正确：加上encoding和ensure_ascii
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ❌ 错误：读取损坏的JSON没做异常处理
with open("data.json") as f:
    data = json.load(f)  # 文件损坏直接崩！

# ✅ 正确：加异常处理
try:
    with open("data.json", encoding="utf-8") as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f"JSON解析失败：{e}")
except FileNotFoundError:
    print("配置文件不存在，使用默认配置")
    data = {}
```

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

### 进阶用法：随机数生成和种子

```python
import random

# 随机浮点数（0到1之间）
print(random.random())  # 0.723456...

# 随机浮点数（指定范围）
print(random.uniform(10, 20))  # 14.327...

# 从列表中按权重随机选择（抽奖概率不同）
prizes = ["一等奖", "二等奖", "谢谢参与"]
weights = [1, 5, 94]  # 1% 5% 94%
result = random.choices(prizes, weights=weights, k=5)  # 抽5次
print(f"抽奖结果：{result}")

# 设置随机种子（让结果可复现）
random.seed(42)
print(random.randint(1, 100))  # 每次运行都是同一个数
random.seed(42)  # 重置种子
print(random.randint(1, 100))  # 又是同一个数！
```

### 避坑指南

```python
import random

# ❌ 错误：用random做加密！
token = str(random.random())  # 不安全！random是伪随机

# ✅ 正确：用secrets做安全随机
import secrets
token = secrets.token_hex(16)  # 32位随机十六进制字符串
print(f"安全Token：{token}")

# ❌ 错误：random.sample数量超过列表长度
random.sample([1, 2, 3], 5)  # ValueError!

# ✅ 正确：先检查数量
data = [1, 2, 3]
k = min(5, len(data))
result = random.sample(data, k)

# ❌ 错误：直接shuffle原列表（会修改原数据）
employees = ["张三", "李四", "王五"]
random.shuffle(employees)  # 原列表被改了！

# ✅ 正确：先copy再shuffle
order = employees.copy()
random.shuffle(order)
```

---

## 5. sys - 系统相关

查看Python版本、退出程序、修改模块路径。写命令行工具时必备。

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

### 进阶用法：命令行参数处理

```python
import sys

# sys.argv 获取命令行参数
# python script.py input.txt --mode fast
# sys.argv = ['script.py', 'input.txt', '--mode', 'fast']

if len(sys.argv) < 2:
    print("用法：python script.py <文件名>")
    sys.exit(1)  # 退出程序，1表示错误

filename = sys.argv[1]
print(f"处理文件：{filename}")

# 进度条输出（不换行）
import time
for i in range(100):
    sys.stdout.write(f"\r进度：{i+1}%")
    sys.stdout.flush()
    time.sleep(0.05)
print("\n完成！")
```

### 实战：简单的命令行工具

```python
import sys

def main():
    """一个简单的文件统计工具"""
    if len(sys.argv) < 2:
        print("用法：python wordcount.py <文件名>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        chars = len(content)
        words = len(content.split())
        lines = content.count('\n') + 1
        
        print(f"文件：{filename}")
        print(f"行数：{lines}")
        print(f"词数：{words}")
        print(f"字符数：{chars}")
    except FileNotFoundError:
        print(f"文件不存在：{filename}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

---

## 6. pathlib - 路径操作（推荐用这个）

比os.path更优雅的路径处理方式。Python 3.4+推荐使用，代码可读性大幅提升。

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

### pathlib vs os.path 写法对比

```python
import os
from pathlib import Path

# pathlib写法：直观、链式调用
p = Path.home() / "Downloads" / "report.pdf"
print(p.stem)    # "report"（文件名，不含扩展名）
print(p.suffix)  # ".pdf"（扩展名）
print(p.parent)  # 上一级目录

# os.path写法：嵌套函数调用
p = os.path.join(os.path.expanduser("~"), "Downloads", "report.pdf")
print(os.path.splitext(os.path.basename(p))[0])  # "report"（好丑！）
```

> 💡 **结论**：功能一样，但pathlib代码更清晰。新项目推荐用pathlib！

### 进阶用法：glob模式匹配

```python
from pathlib import Path

# 递归搜索所有Python文件
py_files = list(Path(".").rglob("*.py"))
print(f"当前目录下有 {len(py_files)} 个Python文件")

# 按修改时间排序
sorted_files = sorted(py_files, key=lambda f: f.stat().st_mtime, reverse=True)
print("最近修改的5个文件：")
for f in sorted_files[:5]:
    print(f"  {f.name} ({f.stat().st_size} bytes)")

# 读写文件（pathlib直接支持！）
config = Path("config.txt")
config.write_text("debug=True\n", encoding="utf-8")  # 写
content = config.read_text(encoding="utf-8")           # 读
print(f"配置内容：{content}")
```

---

## 7. collections - 特殊数据结构

一些有用的数据结构工具。用好了能让代码更简洁、更高效。

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

### 进阶用法：defaultdict和namedtuple

```python
from collections import defaultdict, namedtuple

# defaultdict：不再怕KeyError
word_count = defaultdict(int)  # 默认值为0
for word in ["python", "java", "python", "go"]:
    word_count[word] += 1  # 不需要先判断key存不存在！
print(dict(word_count))

# 分组示例：按首字母分组
names = ["Alice", "Anna", "Bob", "Charlie", "Cathy"]
groups = defaultdict(list)
for name in names:
    groups[name[0]].append(name)
print(dict(groups))
# {'A': ['Alice', 'Anna'], 'B': ['Bob'], 'C': ['Charlie', 'Cathy']}

# namedtuple：轻量级类，比普通tuple更可读
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(f"坐标：({p.x}, {p.y})，距离原点：{(p.x**2 + p.y**2)**0.5}")

# 实战：用namedtuple表示学生
Student = namedtuple('Student', ['name', 'age', 'score'])
students = [
    Student("张三", 20, 85),
    Student("李四", 21, 92),
    Student("王五", 19, 78),
]
top_student = max(students, key=lambda s: s.score)
print(f"最高分：{top_student.name}，分数：{top_student.score}")
```

---

## 8. re - 正则表达式

文本处理的瑞士军刀。提取、替换、验证，一个正则搞定。

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

### 进阶用法：替换和分组

```python
import re

# 替换：脱敏手机号中间4位
text = "联系电话：13812345678，备用：18687654321"
masked = re.sub(r'(\d{3})\d{4}(\d{4})', r'\1****\2', text)
print(f"脱敏后：{masked}")
# 联系电话：138****5678，备用：186****4321

# 分组提取：解析日志
log = '2026-04-16 14:30:00 [ERROR] Connection timeout'
pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)'
match = re.match(pattern, log)
if match:
    date, time, level, msg = match.groups()
    print(f"日期：{date}，时间：{time}，级别：{level}，信息：{msg}")

# 批量替换：HTML标签清理
html = "<p>这是<b>重要</b>的内容</p>"
clean = re.sub(r'<[^>]+>', '', html)
print(f"清理后：{clean}")  # 这是重要的内容
```

### 避坑指南

```python
import re

# ❌ 错误：贪婪匹配吞掉太多内容
text = "<div>第一段</div><div>第二段</div>"
result = re.findall(r'<div>.*</div>', text)
print(result)  # ['<div>第一段</div><div>第二段</div>'] 只匹配到一个！

# ✅ 正确：用非贪婪匹配
result = re.findall(r'<div>.*?</div>', text)
print(result)  # ['<div>第一段</div>', '<div>第二段</div>']

# ❌ 错误：复杂的正则不加注释，过几天自己都看不懂
# ✅ 正确：用re.VERBOSE加注释
pattern = re.compile(r"""
    \d{4}      # 年份
    -          # 分隔符
    \d{2}      # 月份
    -          # 分隔符
    \d{2}      # 日期
""", re.VERBOSE)
```

---

## 9. math - 数学运算

开方、绝对值、三角函数等。科学计算、游戏开发都用得到。

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

### 进阶用法：角度弧度和对数

```python
import math

# 角度转弧度
angle_deg = 90
angle_rad = math.radians(angle_deg)
print(f"90度 = {angle_rad:.4f}弧度")

# 三角函数
print(f"sin(90°) = {math.sin(angle_rad):.4f}")
print(f"cos(90°) = {math.cos(angle_rad):.6f}")  # 接近0

# 对数运算
print(f"ln(e) = {math.log(math.e):.4f}")    # 1.0
print(f"log2(8) = {math.log2(8)}")          # 3.0
print(f"log10(100) = {math.log10(100)}")    # 2.0

# 最大公约数和阶乘
print(f"gcd(12, 8) = {math.gcd(12, 8)}")    # 4
print(f"5! = {math.factorial(5)}")          # 120
```

### 避坑：math vs cmath

```python
import math

# ❌ 错误：对负数开方会报错
# math.sqrt(-1)  # ValueError!

# ✅ 正确：用cmath处理复数
import cmath
result = cmath.sqrt(-1)
print(f"√(-1) = {result}")  # 1j
```

---

## 10. itertools - 迭代器工具

生成排列、组合、无限序列。处理大数据时特别省内存。

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

### 进阶用法：排列组合和分组

```python
import itertools

# 排列：从3个人中选2个排队（有序）
people = ['A', 'B', 'C']
perms = list(itertools.permutations(people, 2))
print(f"排列数：{len(perms)}，结果：{perms}")
# 排列数：6，结果：[('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]

# 组合：从3个人中选2个（无序）
combs = list(itertools.combinations(people, 2))
print(f"组合数：{len(combs)}，结果：{combs}")
# 组合数：3，结果：[('A','B'), ('A','C'), ('B','C')]

# 分组：每3个一组
data = range(10)
groups = list(itertools.batched(data, 3))  # Python 3.12+
print(f"分组结果：{groups}")  # [(0,1,2), (3,4,5), (6,7,8), (9,)]

# 链接多个迭代器
list1 = [1, 2]
list2 = ['a', 'b']
chained = list(itertools.chain(list1, list2))
print(f"链接后：{chained}")  # [1, 2, 'a', 'b']
```

### 性能对比：itertools vs 列表推导

```python
import itertools
import time

# 生成100万个数的平方
# 方式1：列表推导（占内存）
start = time.time()
squares = [x**2 for x in range(1000000)]
print(f"列表推导耗时：{time.time()-start:.3f}s，内存：约{len(squares)*8/1024/1024:.1f}MB")

# 方式2：生成器表达式（几乎不占内存）
start = time.time()
square_iter = (x**2 for x in range(1000000))
print(f"生成器耗时：{time.time()-start:.3f}s，内存：约0MB")
```

> 💡 **结论**：数据量大时，用迭代器比列表省内存。100万条数据，列表占几十MB，迭代器几乎为0。

---

## 🔥 实战案例：用标准库写一个日志分析工具

把上面学的标准库串起来，写一个实用的小工具：

```python
import re
import json
from pathlib import Path
from collections import Counter
from datetime import datetime

def analyze_log(log_path):
    """分析日志文件，统计错误和访问趋势"""
    log_file = Path(log_path)
    if not log_file.exists():
        print(f"文件不存在：{log_path}")
        return
    
    # 统计数据
    error_counter = Counter()     # 错误类型统计
    hourly_counter = Counter()    # 每小时访问量
    total_lines = 0
    error_lines = 0
    
    # 逐行读取（大文件也不会撑爆内存）
    for line in log_file.read_text(encoding='utf-8').splitlines():
        total_lines += 1
        
        # 提取时间
        time_match = re.search(r'(\d{2}):\d{2}:\d{2}', line)
        if time_match:
            hour = time_match.group(1)
            hourly_counter[hour] += 1
        
        # 提取错误级别
        level_match = re.search(r'\[(ERROR|WARN|INFO)\]', line)
        if level_match:
            level = level_match.group(1)
            if level == 'ERROR':
                error_lines += 1
                # 提取错误信息
                msg_match = re.search(r'\[ERROR\] (.+)', line)
                if msg_match:
                    error_counter[msg_match.group(1)[:50]] += 1
    
    # 输出报告
    print("\n" + "="*50)
    print(f"📊 日志分析报告")
    print(f"文件：{log_file.name}")
    print(f"总行数：{total_lines}")
    print(f"错误行数：{error_lines}")
    if total_lines > 0:
        print(f"错误率：{error_lines/total_lines*100:.1f}%")
    
    print(f"\n🔴 Top 5 错误：")
    for msg, count in error_counter.most_common(5):
        print(f"  [{count}次] {msg}")
    
    print(f"\n📈 每小时访问量：")
    for hour in sorted(hourly_counter.keys()):
        bar = '█' * (hourly_counter[hour] // 10)
        print(f"  {hour}:00 {bar} ({hourly_counter[hour]})")
    print("="*50)
    
    # 保存结果为JSON
    report = {
        "file": log_file.name,
        "total_lines": total_lines,
        "error_lines": error_lines,
        "top_errors": error_counter.most_common(5),
        "hourly_stats": dict(hourly_counter)
    }
    report_path = log_file.with_suffix('.report.json')
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )
    print(f"\n报告已保存：{report_path}")

# 使用
analyze_log('app.log')
```

这个实战案例一口气用到了5个标准库：**re**解析日志、**Counter**统计词频、**Path**操作文件、**json**保存报告、**datetime**处理时间。这就是标准库的威力——不用装任何第三方包，就能做出实用工具！

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
|-----|------|----------|
| `os` | 文件/目录操作 | `listdir`, `mkdir`, `path.exists`, `environ` |
| `datetime` | 日期时间 | `now`, `strftime`, `strptime`, `timedelta` |
| `json` | 数据格式转换 | `dump`, `load`, `dumps`, `loads` |
| `random` | 随机数 | `choice`, `sample`, `randint`, `choices`, `seed` |
| `pathlib` | 路径操作 | `glob`, `rglob`, `mkdir`, `stat`, `read_text` |
| `collections` | 特殊数据结构 | `Counter`, `defaultdict`, `namedtuple` |
| `re` | 正则表达式 | `findall`, `match`, `sub`, `search` |
| `math` | 数学运算 | `sqrt`, `pi`, `ceil`, `floor`, `gcd`, `log2` |
| `itertools` | 迭代器工具 | `product`, `permutations`, `combinations`, `chain` |
| `sys` | 系统相关 | `argv`, `exit`, `version`, `platform` |

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


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)

