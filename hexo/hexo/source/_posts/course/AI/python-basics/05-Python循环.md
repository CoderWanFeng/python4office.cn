---
title: Python循环：我用for和while自动化处理1000份文件
date: 2026-02-28 19:58:00
tags: [Python基础, 循环, for, while]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA'>
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
<a href="https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

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
# ... 还要写97次
```

**用循环（优雅模式）：**

```python
names = ["张三", "李四", "王五", ...]  # 100个名字

for name in names:
    print(f"欢迎{name}！")
```

**一句话，循环帮你省了99%的重复代码。**

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

---

## range函数：生成数字序列

如果想按顺序执行5次，用 `range()` 生成数字序列：

```python
# range(5) 生成：0, 1, 2, 3, 4
for i in range(5):
    print(f"第{i + 1}次执行")

# range(2, 6) 生成：2, 3, 4, 5（从2开始，到6之前结束）
for i in range(2, 6):
    print(i)

# range(0, 11, 2) 生成：0, 2, 4, 6, 8, 10（步长为2）
for i in range(0, 11, 2):
    print(f"偶数：{i}")
```

**运行结果：**

```
第1次执行
第2次执行
第3次执行
第4次执行
第5次执行

2
3
4
5

偶数：0
偶数：2
偶数：4
偶数：6
偶数：8
偶数：10
```

> 💡 **记住**：`range(5)` 是从0开始的，到5之前结束，不包含5。如果想要1到5，用 `range(1, 6)`。

---

## while循环：条件满足就一直做

`for` 适合知道要循环多少次的情况。`while` 适合**不知道要循环多少次，只要条件满足就一直做**的情况。

### 场景举例：猜数字游戏

你不知道对方要猜几次，只能一直猜，直到猜对为止：

```python
secret = 7       # 正确答案
guess = 0        # 一开始猜的是0

while guess != secret:   # 只要没猜对，就继续
    guess = int(input("猜一个数字（1-10）："))
    if guess < secret:
        print("太小了，再大一点")
    elif guess > secret:
        print("太大了，再小一点")

print("恭喜猜对了！")
```

**运行结果（假设正确答案7）：**

```
猜一个数字（1-10）：3
太小了，再大一点
猜一个数字（1-10）：8
太大了，再小一点
猜一个数字（1-10）：7
恭喜猜对了！
```

> ⚠️ **while的坑**：必须确保循环条件最终会变成`False`，否则会陷入**无限循环**（程序卡死）。每次循环结束，必须让条件朝着False的方向变化。

---

## 循环控制：break 和 continue

### break：中途退出

遇到某个条件就不做了，直接跳出整个循环：

```python
for i in range(10):
    if i == 5:
        break    # 遇到5就停止
    print(i)
```

**运行结果：**

```
0
1
2
3
4
```

### continue：跳过这次

遇到某个条件跳过这一次，继续下一个：

```python
for i in range(5):
    if i == 2:
        continue   # 遇到2就跳过
    print(i)
```

**运行结果：**

```
0
1
3
4
（2被跳过了，没有打印）
```

---

## for和while：什么时候用哪个？

| 场景 | 用哪个 | 原因 |
|-----|:---:|------|
| 遍历列表 | `for` | 已知有多少个元素 |
| 执行固定次数 | `for` + `range` | 知道要执行几次 |
| 不知道要几次 | `while` | 等某个条件满足 |
| 用户输入验证 | `while True` | 等用户输对为止 |

---

## 遍历字典：顺便取出名字和值

```python
person = {"姓名": "张三", "年龄": 25, "城市": "北京"}

for key in person:            # 遍历键
    print(key)

for value in person.values():  # 遍历值
    print(value)

for key, value in person.items():  # 同时取键和值
    print(f"{key}：{value}")
```

**运行结果：**

```
姓名
年龄
城市

张三
25
北京

姓名：张三
年龄：25
城市：北京
```

---

## 同时遍历两个列表：zip

如果有名字列表和年龄列表，想合并显示：

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

---

## 嵌套循环：九九乘法表

一个循环里再套一个循环：

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
...
```

---

## 避坑指南

### ❌ 坑1：忘记更新循环变量（while）

```python
count = 0
while count < 5:
    print(count)
    # ❌ 忘记写 count += 1，程序会永远卡在0，进入无限循环！

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

# ✅ 正确：创建新列表
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # [1, 3, 5]
```

---

## 实战练习：批量重命名文件夹里的文件

把下载文件夹里的文件统一加上日期前缀：

```python
import os

def batch_rename(folder, prefix):
    """给文件夹里的文件加前缀"""
    files = os.listdir(folder)  # 获取所有文件名
    count = 0

    for filename in files:
        filepath = os.path.join(folder, filename)

        # 跳过文件夹，只处理文件
        if os.path.isdir(filepath):
            continue

        # 新文件名 = 前缀_原名
        new_name = f"{prefix}_{filename}"
        new_path = os.path.join(folder, new_name)

        os.rename(filepath, new_path)
        count += 1
        print(f"  {filename} → {new_name}")

    print(f"\n✅ 完成，共处理 {count} 个文件")

# 假设给当前目录下的文件加前缀
# batch_rename(".", "2026-04-16")
```

**运行结果（模拟）：**

```
  报告.docx → 2026-04-16_报告.docx
  数据.xlsx → 2026-04-16_数据.xlsx
  照片.jpg → 2026-04-16_照片.jpg

✅ 完成，共处理 3 个文件
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

| 概念 | 说明 |
|-----|------|
| `for item in 列表:` | 依次取出每个元素来处理 |
| `range(n)` | 生成 0 到 n-1 的数字序列 |
| `while 条件:` | 条件满足就一直做 |
| `break` | 退出整个循环 |
| `continue` | 跳过本次，进入下一次 |
| `.items()` | 同时遍历字典的键和值 |
| `zip(a, b)` | 同时遍历两个列表 |

---

## 下节预告

掌握了循环，下一篇来学**函数**——把一段代码打包成一个工具，想用就用，让代码复用更方便。

👉 **[继续阅读：Python函数基础](./06-Python函数基础.md)**

---

## 课程导航

**上一篇：** [Python条件判断-if-else完全指南](./04-Python条件判断.md)

**下一篇：** [Python函数基础-从定义到调用](./06-Python函数基础.md)

---

*PS：循环是自动化的核心——搞定了循环，你就搞定了批量处理。生活中有什么重复性的事，试试用循环来实现吧！*

