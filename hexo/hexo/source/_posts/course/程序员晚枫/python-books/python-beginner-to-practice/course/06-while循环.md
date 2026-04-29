---
title: 第6讲 用户输入与while循环
date: 2026-04-28 23:54:00
tags: [python,入门,课程,第6讲]
cover: https://images.unsplash.com/photo-1526379095098-d400fd0bf935?q=80&w=1200&auto=format&fit=crop
---

<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<!-- more -->
<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/a8bdeb7d-f6a8-4ad5-8020-e206055dd039/Python编程：从入门到实践_第3版__.png" alt="Python编程：从入门到实践（第3版）" width="400"/>
</p>
> 📖 **一起读书吧！** 加入《Python编程：从入门到实践》共读营 👉 [点击参加](https://mp.weixin.qq.com/s/ehe2vMrfAFscRLqbM9TF-g)



## 本讲内容

- input() 获取用户输入
- while 循环
- for 循环与 range()
- break 和 continue

## 学习目标

和程序"对话" 💬

---

## 1. 获取用户输入

```python
name = input("请输入你的名字：")
print(f"你好，{name}！")
```

> ⚠️ `input()` 返回的**永远是字符串**！需要数字时要手动转换：

```python
age = input("请输入年龄：")  # age 是字符串 "25"
age = int(input("请输入年龄："))  # age 是整数 25
```

> 官方文档：[input() 函数](https://docs.python.org/3/library/functions.html#input) — 从标准输入读取一行文本。

## 2. while 循环

```python
# 基本while循环
count = 0
while count < 5:
    print(f"第{count}次")
    count += 1
```

### 让用户选择何时退出

```python
message = ""
while message != "quit":
    message = input("输入消息（输入quit退出）：")
    if message != "quit":
        print(f"你说了：{message}")
```

### 使用标志位

```python
active = True
while active:
    message = input("输入消息（输入quit退出）：")
    if message == "quit":
        active = False
    else:
        print(f"你说了：{message}")
```

## 3. for 循环

```python
# 遍历列表
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "Python":
    print(char)

# 使用 range()
for i in range(5):
    print(i)  # 0 1 2 3 4

# range(起始, 结束, 步长)
for i in range(2, 10, 3):
    print(i)  # 2 5 8
```

> 官方文档：[4.2. for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements) — Python的for循环遍历任何序列的元素。
>
> [4.3. The range() Function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function) — `range()` 生成算术序列，不实际创建列表，节省内存。

## 4. break 和 continue

```python
# break — 立即退出整个循环
while True:
    city = input("输入城市名（quit退出）：")
    if city == "quit":
        break
    print(f"你想去{city}")

# continue — 跳过本次循环，进入下一次
for num in range(10):
    if num % 2 == 0:
        continue  # 跳过偶数
    print(num)  # 只打印奇数：1 3 5 7 9
```

> 官方文档：[4.4. break and continue Statements](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements)

## 5. 循环的 else 子句

Python有个独特的语法：循环可以带 `else`，当循环**正常结束**（没有被break打断）时执行。

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x} * {n//x}")
            break
    else:
        # 循环没有被break打断 → n是质数
        print(f"{n} 是质数")
```

> 官方文档：[4.5. else Clauses on Loops](https://docs.python.org/3/tutorial/controlflow.html#else-clauses-on-loops) — 循环的else子句在for循环耗尽或while条件为假时执行，但break会跳过它。

## 6. enumerate() — 同时获取索引和值

```python
fruits = ['apple', 'banana', 'orange']

# 传统写法
for i in range(len(fruits)):
    print(i, fruits[i])

# Pythonic写法
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 orange
```

## 7. zip() — 同时遍历多个序列

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

> 官方文档：[5.6. Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques) — enumerate()、zip()、items()等循环技巧。

---

## 📚 官方文档参考

- [4.2. for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [4.3. The range() Function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)
- [4.4. break and continue Statements](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements)
- [4.5. else Clauses on Loops](https://docs.python.org/3/tutorial/controlflow.html#else-clauses-on-loops)
- [4.6. pass Statements](https://docs.python.org/3/tutorial/controlflow.html#pass-statements)
- [5.6. Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)
- [input()](https://docs.python.org/3/library/functions.html#input)

---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲](https://www.bilibili.com/cheese/play/ss982042944)