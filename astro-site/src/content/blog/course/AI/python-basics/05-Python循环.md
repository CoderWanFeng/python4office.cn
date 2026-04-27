---
title: Python循环：我用for和while自动化处理1000份文件
date: 2026-02-28 19:58:00
tags: [Python基础, 循环, for, while]
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

## 一个真实的故事

2023年，有个财务小姐姐找我求助：

> "晚枫老师，我每个月要处理1000多个Excel文件，每个都要打开、复制数据、粘贴到汇总表...一天都做不完，有没有办法？"

我看了一眼，给了她一个脚本：

```python
import os
import pandas as pd

# 读取所有Excel文件并合并
all_data = []
for filename in os.listdir("文件夹路径"):
    if filename.endswith(".xlsx"):
        data = pd.read_excel(filename)
        all_data.append(data)

# 合并并保存
result = pd.concat(all_data)
result.to_excel("汇总.xlsx", index=False)
print("完成！共处理", len(all_data), "个文件")
```

**原本一天的工作，变成了3秒钟。**

这就是循环的力量——**让程序自动重复做事，批量处理大量数据**。

上篇我们学了条件判断，程序能做选择了。这篇来学**循环**——让程序自动重复做事。

学完这篇，你就能批量处理100条、1000条、10000条数据，真正实现自动化办公。

---

## 为什么需要循环？

先看一个痛苦的需求：给100个人发欢迎消息。

**不用循环（痛苦模式）：**

```python
print("欢迎张三！")
print("欢迎李四！")
print("欢迎王五！")
# ... 还要写97次，手都要断了...
```

**用循环（优雅模式）：**

```python
names = ["张三", "李四", "王五", ...]  # 100个名字

for name in names:
    print(f"欢迎{name}！")
```

**一句话，循环帮你省了99%的重复代码。**

### 循环的本质

循环就是让计算机帮你做重复的事：

```
人：做这件事100次 → 累死
计算机：做这件事100次 → 毫秒级完成
```

**循环的应用场景：**
- 批量处理文件（1000个Excel合并）
- 批量发送消息（100封邮件群发）
- 批量数据处理（爬取100页数据）
- 批量重命名（给500个文件加前缀）
- 批量下载（下载整个相册）

---

## for循环：遍历（一件一件地处理）

`for`循环的工作方式，就像服务员依次接待排队的客人——来一个处理一个。

### 基本语法

```python
fruits = ["苹果", "香蕉", "橙子"]

for fruit in fruits:
    print(f"我要吃：{fruit}")
```

**逐行解析：**

```
fruits 的每个元素，依次取出，命名为 fruit
然后执行一次循环体（print那一行）
遍历完了，循环结束
```

**运行结果：**

```
我要吃：苹果
我要吃：香蕉
我要吃：橙子
```

### for循环的执行流程

```python
names = ["张三", "李四", "王五"]

for name in names:     # 第1次：name = "张三"
    print(name)        # 执行：打印"张三"
                       # 第2次：name = "李四"
                       # 执行：打印"李四"
                       # 第3次：name = "王五"
                       # 执行：打印"王五"
                       # 没有元素了，结束循环
```

### 遍历不同类型的数据

```python
# 遍历字符串
for char in "Python":
    print(char)
# P y t h o n

# 遍历列表
for num in [1, 2, 3, 4, 5]:
    print(num * 2)
# 2 4 6 8 10

# 遍历元组
for item in (1, 2, 3):
    print(item)
# 1 2 3

# 遍历集合
for fruit in {"苹果", "香蕉", "橙子"}:
    print(fruit)
# 注意：集合无序，顺序可能不同

# 遍历字典的键
person = {"name": "张三", "age": 25}
for key in person:
    print(key)
# name age
```

---

## range函数：生成数字序列

如果想按顺序执行N次，用 `range()` 生成数字序列：

### range的三种用法

```python
# 1. range(n)：生成0到n-1
for i in range(5):
    print(i)
# 0 1 2 3 4

# 2. range(start, end)：生成start到end-1
for i in range(2, 6):
    print(i)
# 2 3 4 5

# 3. range(start, end, step)：指定步长
for i in range(0, 11, 2):
    print(i)
# 0 2 4 6 8 10（偶数）

# 倒序：步长为负数
for i in range(5, 0, -1):
    print(i)
# 5 4 3 2 1
```

### range的实际应用

```python
# 执行某操作N次
for i in range(10):
    print("Hello!")

# 生成1-100
for i in range(1, 101):
    print(i)

# 遍历列表索引
fruits = ["苹果", "香蕉", "橙子"]
for i in range(len(fruits)):
    print(f"第{i+1}个水果：{fruits[i]}")

# 批量创建文件名
for i in range(1, 6):
    filename = f"报告_{i:03d}.txt"  # 001, 002, 003...
    print(filename)
# 报告_001.txt 报告_002.txt 报告_003.txt 报告_004.txt 报告_005.txt
```

### range的性能优势

```python
# range是惰性的，不会立即生成所有数字
r = range(1000000)  # 不占用内存
print(r)  # range(0, 1000000)

# 只有遍历时才生成
for i in r:
    if i > 5:
        break
    print(i)
```

---

## while循环：条件满足就一直做

`for` 适合知道要循环多少次的情况。`while` 适合**不知道要循环多少次，只要条件满足就一直做**的情况。

### 基本语法

```python
count = 0
while count < 5:
    print(count)
    count += 1
# 0 1 2 3 4
```

### 场景举例：猜数字游戏

你不知道对方要猜几次，只能一直猜，直到猜对为止：

```python
import random

secret = random.randint(1, 100)  # 随机生成1-100的数字
guess = 0
attempts = 0

print("猜数字游戏（1-100）")

while guess != secret:
    guess = int(input("请输入你的猜测："))
    attempts += 1
    
    if guess < secret:
        print("太小了，再大一点")
    elif guess > secret:
        print("太大了，再小一点")

print(f"恭喜猜对了！答案就是{secret}，你用了{attempts}次")
```

### while的应用场景

```python
# 1. 等待用户输入正确
while True:
    password = input("请输入密码：")
    if password == "123456":
        print("密码正确！")
        break
    print("密码错误，请重试")

# 2. 读取数据直到结束
data = []
while True:
    line = input("请输入数据（输入q结束）：")
    if line == 'q':
        break
    data.append(line)

# 3. 重试机制
max_retries = 3
retry_count = 0

while retry_count < max_retries:
    success = send_email()  # 假设的发送函数
    if success:
        print("发送成功！")
        break
    retry_count += 1
    print(f"发送失败，重试第{retry_count}次...")

if retry_count == max_retries:
    print("发送失败，请稍后重试")
```

### while的陷阱：无限循环

```python
# ❌ 危险：无限循环
count = 0
while count < 5:
    print(count)
    # 忘记写 count += 1
    # count永远是0，条件永远为True
    # 程序卡死！Ctrl+C强制退出

# ✅ 正确：确保条件会变化
count = 0
while count < 5:
    print(count)
    count += 1  # 每次加1，最终会退出
```

---

## 循环控制：break 和 continue

### break：中途退出

遇到某个条件就不做了，直接跳出整个循环：

```python
# 找到第一个负数就停止
numbers = [1, 3, 5, -2, 7, 9]

for num in numbers:
    if num < 0:
        print(f"发现负数：{num}")
        break
    print(f"处理：{num}")

print("循环结束")
```

**运行结果：**

```
处理：1
处理：3
处理：5
发现负数：-2
循环结束
```

### continue：跳过这次

遇到某个条件跳过这一次，继续下一个：

```python
# 只打印奇数
for i in range(10):
    if i % 2 == 0:  # 偶数跳过
        continue
    print(i)
```

**运行结果：**

```
1
3
5
7
9
```

### break vs continue

```python
# break：退出整个循环
for i in range(5):
    if i == 3:
        break
    print(i)
# 输出：0 1 2

# continue：跳过当前这次，继续下一次
for i in range(5):
    if i == 3:
        continue
    print(i)
# 输出：0 1 2 4
```

### 实际应用

```python
# 1. 验证用户输入
while True:
    age = input("请输入年龄：")
    if not age.isdigit():
        print("请输入数字！")
        continue
    age = int(age)
    if age < 0 or age > 150:
        print("年龄不合理，请重新输入")
        continue
    print(f"你的年龄是{age}岁")
    break

# 2. 查找数据
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]

target = "李四"
for student in students:
    if student["name"] == target:
        print(f"找到{target}，分数：{student['score']}")
        break
else:
    print(f"没找到{target}")
```

---

## for-else和while-else

Python特有的语法：循环正常结束（没有break）时执行else：

```python
# 查找质数
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x} × {n//x}")
            break
    else:
        print(f"{n} 是质数")
```

**运行结果：**

```
2 是质数
3 是质数
4 = 2 × 2
5 是质数
6 = 2 × 3
7 是质数
8 = 2 × 4
9 = 3 × 3
```

**注意：** else在循环正常结束时执行，如果break退出了，else不会执行。

---

## 遍历字典：键、值、键值对

```python
person = {"姓名": "张三", "年龄": 25, "城市": "北京"}

# 1. 遍历键（默认）
for key in person:
    print(key)
# 姓名 年龄 城市

# 2. 显式遍历键
for key in person.keys():
    print(key)
# 姓名 年龄 城市

# 3. 遍历值
for value in person.values():
    print(value)
# 张三 25 北京

# 4. 同时遍历键和值（推荐）
for key, value in person.items():
    print(f"{key}：{value}")
# 姓名：张三
# 年龄：25
# 城市：北京
```

### 嵌套字典的遍历

```python
students = {
    "张三": {"语文": 85, "数学": 92, "英语": 78},
    "李四": {"语文": 90, "数学": 88, "英语": 95},
    "王五": {"语文": 75, "数学": 85, "英语": 82}
}

# 遍历每个学生的成绩
for name, scores in students.items():
    print(f"\n{name}的成绩：")
    for subject, score in scores.items():
        print(f"  {subject}：{score}")
    avg = sum(scores.values()) / len(scores)
    print(f"  平均分：{avg:.1f}")
```

---

## 同时遍历多个序列：zip

### 基本用法

```python
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]

for name, age in zip(names, ages):
    print(f"{name}，{age}岁")
```

**运行结果：**

```
张三，25岁
李四，30岁
王五，28岁
```

### zip的特性

```python
# zip以最短的序列为准
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

for num, char in zip(list1, list2):
    print(num, char)
# 1 a  2 b  3 c  （4和5被忽略）

# 同时遍历三个列表
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]
cities = ["北京", "上海", "广州"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}，{age}岁，来自{city}")
```

### 创建字典

```python
keys = ['name', 'age', 'city']
values = ['张三', 25, '北京']

person = dict(zip(keys, values))
print(person)
# {'name': '张三', 'age': 25, 'city': '北京'}
```

---

## enumerate：获取索引和值

```python
fruits = ["苹果", "香蕉", "橙子"]

# 普通方式
for i in range(len(fruits)):
    print(f"{i}：{fruits[i]}")

# enumerate方式（更优雅）
for index, fruit in enumerate(fruits):
    print(f"{index}：{fruit}")

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"第{index}个：{fruit}")
```

**运行结果：**

```
第1个：苹果
第2个：香蕉
第3个：橙子
```

---

## 嵌套循环：循环里的循环

### 九九乘法表

```python
for i in range(1, 10):       # 外层：1到9
    for j in range(1, i + 1):  # 内层：1到i
        print(f"{j}×{i}={i*j}", end="\t")
    print()   # 换行
```

**运行结果：**

```
1×1=1	
1×2=2	2×2=4	
1×3=3	2×3=6	3×3=9	
1×4=4	2×4=8	3×4=12	4×4=16	
1×5=5	2×5=10	3×5=15	4×5=20	5×5=25	
...
```

### 遍历嵌套结构

```python
# 二维列表
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# 查找元素
target = 5
found = False
for i, row in enumerate(matrix):
    for j, item in enumerate(row):
        if item == target:
            print(f"找到{target}，位置：第{i}行第{j}列")
            found = True
            break
    if found:
        break
```

### 打印各种图案

```python
# 直角三角形
for i in range(1, 6):
    print("*" * i)

# 倒三角形
for i in range(5, 0, -1):
    print("*" * i)

# 等腰三角形
n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

---

## 列表推导式：一行写循环

Python特有的简洁写法：

```python
# 传统循环
squares = []
for i in range(10):
    squares.append(i ** 2)

# 列表推导式
squares = [i ** 2 for i in range(10)]

# 带条件的列表推导式
evens = [i for i in range(20) if i % 2 == 0]

# 嵌套推导式
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

### 字典推导式

```python
# 创建平方字典
squares = {i: i**2 for i in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 键值互换
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

---

## 避坑指南

### ❌ 坑1：忘记更新循环变量（while）

```python
count = 0
while count < 5:
    print(count)
    # ❌ 忘记写 count += 1，程序会永远卡在0

# ✅ 正确做法：
count = 0
while count < 5:
    print(count)
    count += 1   # 每次加1，确保最终能退出
```

### ❌ 坑2：在循环中修改正在遍历的列表

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)   # ❌ 危险！可能导致某些元素被跳过

# ✅ 方法1：创建新列表
numbers = [num for num in numbers if num % 2 != 0]

# ✅ 方法2：遍历副本
for num in numbers[:]:  # 注意[:]
    if num % 2 == 0:
        numbers.remove(num)
```

### ❌ 坑3：range的边界

```python
# ❌ 错误：range(5)不包含5
for i in range(5):
    print(i)  # 0 1 2 3 4，没有5

# ✅ 如果想要1-5
for i in range(1, 6):
    print(i)  # 1 2 3 4 5
```

### ❌ 坑4：无限循环无法退出

```python
# ❌ 危险
while True:
    user_input = input("输入q退出：")
    # 忘记检查退出条件！

# ✅ 正确
while True:
    user_input = input("输入q退出：")
    if user_input == 'q':
        break
```

### ❌ 坑5：浮点数循环

```python
# ❌ 不要用浮点数做循环变量
i = 0
while i != 1:
    i += 0.1
    # 可能永远不等1（精度问题）

# ✅ 用整数或比较
i = 0
while i < 10:
    i += 1
    x = i / 10
```

---

## 性能对比：不同的循环方式

```python
import time

# 方法1：普通for循环
def method1():
    result = []
    for i in range(10000):
        result.append(i ** 2)
    return result

# 方法2：列表推导式
def method2():
    return [i ** 2 for i in range(10000)]

# 方法3：map函数
def method3():
    return list(map(lambda x: x ** 2, range(10000)))

# 测试
start = time.time()
method1()
print(f"普通for循环: {time.time() - start:.4f}秒")

start = time.time()
method2()
print(f"列表推导式: {time.time() - start:.4f}秒")

start = time.time()
method3()
print(f"map函数: {time.time() - start:.4f}秒")
```

**结论：** 列表推导式通常最快，也最易读。

---

## 实战练习：批量重命名文件

```python
import os
from datetime import datetime

def batch_rename(folder, prefix=None, suffix=None):
    """批量重命名文件"""
    if not os.path.exists(folder):
        print("文件夹不存在")
        return
    
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    count = 0
    
    print(f"找到 {len(files)} 个文件")
    print("-" * 40)
    
    for i, filename in enumerate(files, 1):
        # 获取文件名和扩展名
        name, ext = os.path.splitext(filename)
        
        # 构建新文件名
        parts = []
        if prefix:
            parts.append(prefix)
        parts.append(name)
        if suffix:
            parts.append(suffix)
        
        new_name = "_".join(parts) + ext
        new_path = os.path.join(folder, new_name)
        old_path = os.path.join(folder, filename)
        
        # 重命名
        os.rename(old_path, new_path)
        count += 1
        print(f"{i}. {filename} → {new_name}")
    
    print("-" * 40)
    print(f"✅ 完成，共处理 {count} 个文件")

# 使用示例
# batch_rename("下载文件夹", prefix="2026-04-23", suffix="晚枫")
```

### 实战练习：批量处理Excel

```python
import pandas as pd
import os

def merge_excel_files(folder, output_file="汇总.xlsx"):
    """合并文件夹中的所有Excel文件"""
    all_data = []
    
    # 遍历文件夹
    for filename in os.listdir(folder):
        if filename.endswith(('.xlsx', '.xls')):
            filepath = os.path.join(folder, filename)
            try:
                # 读取Excel
                df = pd.read_excel(filepath)
                # 添加来源列
                df['来源文件'] = filename
                all_data.append(df)
                print(f"✓ 已读取：{filename}（{len(df)}行）")
            except Exception as e:
                print(f"✗ 读取失败：{filename}，错误：{e}")
    
    if not all_data:
        print("没有找到Excel文件")
        return
    
    # 合并所有数据
    result = pd.concat(all_data, ignore_index=True)
    
    # 保存
    result.to_excel(output_file, index=False)
    print("-" * 40)
    print(f"✅ 合并完成！共 {len(result)} 行数据")
    print(f"📄 保存到：{output_file}")

# 使用示例
# merge_excel_files("月度报表")
```

### 实战练习：进度条效果

```python
import time

def progress_bar(total, task_name="处理中"):
    """显示进度条"""
    for i in range(total + 1):
        percent = i / total * 100
        bar_length = int(percent / 2)
        bar = '█' * bar_length + '░' * (50 - bar_length)
        print(f'\r{task_name}: [{bar}] {percent:.1f}%', end='')
        time.sleep(0.05)
    print()

# 使用
progress_bar(100, "下载文件")
```

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

---

## 本讲小结

| 概念 | 说明 |
|-----|------|
| `for item in 列表:` | 依次取出每个元素来处理 |
| `range(n)` | 生成 0 到 n-1 的数字序列 |
| `while 条件:` | 条件满足就一直做 |
| `break` | 退出整个循环 |
| `continue` | 跳过本次，进入下一次 |
| `.items()` | 同时遍历字典的键和值 |
| `zip(a, b)` | 同时遍历两个列表 |
| `enumerate()` | 获取索引和值 |
| 列表推导式 | `[x for x in 列表 if 条件]` |

---

## 下节预告

掌握了循环，下一篇来学**函数**——把一段代码打包成一个工具，想用就用，让代码复用更方便。

你将学会：
- 函数的定义和调用
- 参数和返回值
- 默认参数和关键字参数
- 变量作用域
- 递归函数

👉 **[继续阅读：Python函数基础](./06-Python函数基础.md)**

---

## 课程导航

**上一篇：** [Python条件判断-if-else完全指南](./04-Python条件判断.md)

**下一篇：** [Python函数基础-从定义到调用](./06-Python函数基础.md)

---

## 相关阅读

- [Python运算符与表达式](./03-Python运算符与表达式.md)
- [零基础学AI编程：30天速成计划](/course/AI相关/人民邮电出版社/ads/openclaw/python/20260228171202-零基础学AI编程-30天速成计划/)

---

*PS：循环是自动化的核心——搞定了循环，你就搞定了批量处理。生活中有什么重复性的事，试试用循环来实现吧！记住：程序员最讨厌的事就是重复做同样的事，所以我们发明了循环。*

*2026-04-23 更新 by 程序员晚枫*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


