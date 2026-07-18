---
title: "Python 生成器深度解读：让内存省 100 倍的黑科技"
date: 2026-06-20 18:04:29
tags: ["Python", "生成器", "AI工具", "公众号文章"]
categories: ["公众号文章"]
description: "Python 生成器深度解读：yield、生成器表达式、async 生成器，让内存省 100 倍的黑科技"
cover: https://images.unsplash.com/photo-1526379095098-d400fd0bf935?q=80&w=1200&auto=format&fit=crop
---

大家好，我是程序员晚枫。

**生成器是 Python 的"黑科技"。**

**不会用生成器，你的代码"浪费"内存。**

**今天彻底讲透。**

---

## 一、什么是生成器？

**生成器 = "懒人函数"**。

**普通函数**：一次性返回所有结果

**生成器**：**一次只返回一个，需要时再算下一个**

### 通俗解释

**普通函数像一次性买一年的菜**：

```python
# 一次性返回所有 365 天的菜
def all_meals():
    return [f"第{i}天菜" for i in range(365)]
```

**生成器像每天去菜市场**：

```python
# 每天返回一个
def daily_meal():
    for i in range(365):
        yield f"第{i}天菜"
```

**生成器的好处**：

- **内存省**：不用一次性存所有
- **速度快**：不用等全部算完
- **可处理无限数据**

---

## 二、5 个生成器基础

### 基础 1：yield 创建生成器

```python
def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
```

### 基础 2：生成器是迭代器

**可以用 for 循环**：

```python
for x in my_gen():
    print(x)
# 1
# 2
# 3
```

### 基础 3：生成器只能迭代一次

```python
g = my_gen()
list(g)  # [1, 2, 3]
list(g)  # []（已经耗尽）
```

### 基础 4：生成器有状态

**yield 暂停，下次 next 从暂停处继续**。

### 基础 5：StopIteration

**迭代完抛出 StopIteration**：

```python
g = my_gen()
next(g)  # 1
next(g)  # 2
next(g)  # 3
next(g)  # StopIteration
```

---

## 三、生成器 vs 列表（性能对比）

### 内存对比

```python
import sys

# 列表
list_comp = [i ** 2 for i in range(1_000_000)]
print(sys.getsizeof(list_comp))  # 约 8 MB

# 生成器
gen_comp = (i ** 2 for i in range(1_000_000))
print(sys.getsizeof(gen_comp))  # 约 200 B
```

**内存省 4 万倍**。

### 速度对比

```python
import time

# 列表
start = time.time()
list_comp = [i ** 2 for i in range(1_000_000)]
print(time.time() - start)  # 0.1 秒

# 生成器
start = time.time()
gen_comp = (i ** 2 for i in range(1_000_000))
print(time.time() - start)  # 0.0001 秒
```

**快 1000 倍**。

### 5 大对比

| 维度 | 列表 | 生成器 |
|------|------|------|
| **内存** | 大 | **小** |
| **速度（创建）** | 慢 | **快** |
| **速度（迭代）** | 快 | 慢一点 |
| **可重复迭代** | ✅ | ❌ |
| **支持 len()** | ✅ | ❌ |
| **支持索引** | ✅ | ❌ |

**生成器适合"大数据"**。

---

## 四、5 大生成器表达式

### 表达式 1：基础

```python
gen = (x ** 2 for x in range(10))
```

### 表达式 2：带 if

```python
gen = (x for x in range(10) if x % 2 == 0)
```

### 表达式 3：带函数

```python
gen = (str(x) for x in range(10))
```

### 表达式 4：嵌套

```python
gen = (x * y for x in range(3) for y in range(3))
```

### 表达式 5：复杂

```python
gen = (
    process(item)
    for item in items
    if condition(item)
)
```

---

## 五、5 大生成器高级用法

### 高级 1：send() 发送值

```python
def my_gen():
    value = yield 1
    print(f"Got: {value}")
    value = yield 2
    print(f"Got: {value}")

g = my_gen()
next(g)  # 1
g.send("Hello")  # Got: Hello
g.send("World")  # Got: World
```

### 高级 2：throw() 抛异常

```python
def my_gen():
    try:
        yield 1
        yield 2
    except ValueError:
        print("Got ValueError")

g = my_gen()
next(g)  # 1
g.throw(ValueError)  # Got ValueError
```

### 高级 3：close() 关闭

```python
def my_gen():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("Closing")

g = my_gen()
next(g)  # 1
g.close()  # Closing
```

### 高级 4：yield from 委托

```python
def gen1():
    yield 1
    yield 2

def gen2():
    yield from gen1()  # 委托给 gen1
    yield 3
    yield 4

list(gen2())  # [1, 2, 3, 4]
```

### 高级 5：async 生成器

```python
import asyncio

async def async_gen():
    for i in range(3):
        await asyncio.sleep(1)
        yield i

async def main():
    async for x in async_gen():
        print(x)

asyncio.run(main())
```

---

## 六、5 大真实场景

### 场景 1：读大文件

**普通方式**（占用 1GB 内存）：

```python
with open('big.txt') as f:
    lines = f.readlines()  # 一次性读所有
    for line in lines:
        process(line)
```

**生成器方式**（占用 1KB 内存）：

```python
def read_lines(file):
    with open(file) as f:
        for line in f:
            yield line

for line in read_lines('big.txt'):
    process(line)
```

**内存省 100 万倍**。

### 场景 2：数据流处理

```python
def data_stream():
    for record in get_data():
        yield transform(record)

for data in data_stream():
    save(data)
```

### 场景 3：无限序列

```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

g = fib()
for i in range(10):
    print(next(g))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### 场景 4：管道（pipeline）

```python
def read_data():
    with open('data.txt') as f:
        for line in f:
            yield line

def parse_data(lines):
    for line in lines:
        yield line.strip().split(',')

def process_data(records):
    for record in records:
        yield [int(x) for x in record]

# 管道式处理
data = process_data(parse_data(read_data()))
for record in data:
    print(record)
```

### 场景 5：爬虫分页

```python
def fetch_pages():
    page = 1
    while True:
        data = api.get(f'?page={page}')
        if not data:
            break
        yield data
        page += 1

for items in fetch_pages():
    for item in items:
        process(item)
```

---

## 七、5 大常见误区

### 误区 1：生成器 = 列表

- ❌ 错
- ✅ **生成器是迭代器**

### 误区 2：生成器可以重复

- ❌ 错
- ✅ **只能迭代一次**

### 误区 3：生成器可以 len()

- ❌ 错
- ✅ **没有 len()**

### 误区 4：生成器快

- ⚠️ 部分对
- ✅ 创建快，迭代慢
- **大数据用生成器**

### 误区 5：生成器很难

- ⚠️ 部分对
- ✅ yield 概念
- **1 周上手**

---

## 八、生成器 vs 列表推导式

### 列表推导式 `[...]`

```python
# 一次性计算
squares = [x ** 2 for x in range(10)]
```

### 生成器表达式 `(...)`

```python
# 懒计算
squares = (x ** 2 for x in range(10))
```

### 怎么选？

- **小数据 + 多次用**：列表推导式
- **大数据 + 一次用**：生成器
- **无限数据**：生成器
- **需要 len/index/slice**：列表

---

## 九、5 个生成器实战项目

### 项目 1：日志分析器

```python
def read_log(file):
    with open(file) as f:
        for line in f:
            yield parse(line)

for log in read_log('huge.log'):
    if 'ERROR' in log['level']:
        send_alert(log)
```

### 项目 2：CSV 处理

```python
import csv

def read_csv(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

for row in read_csv('big.csv'):
    save_to_db(row)
```

### 项目 3：API 分页

```python
def fetch_all_pages(api):
    page = 1
    while True:
        data = api.get(f'?page={page}')
        if not data:
            break
        yield data
        page += 1
```

### 项目 4：实时数据流

```python
def stream_data():
    while True:
        data = get_realtime_data()
        yield data
```

### 项目 5：数据管道

```python
def pipeline():
    yield from step1(read_input())
    yield from step2(process_output())
```

---

## 十、给 Python 生成器学习者的 4 个建议

### 建议 1：从 yield 开始

- 写一个 yield 函数
- **理解"暂停"概念**

### 建议 2：替换大列表

- 把 `[...]` 改成 `(...)`
- **立刻省内存**

### 建议 3：用生成器读大文件

- 文件处理是经典场景
- **每天用**

### 建议 4：组合生成器

- `yield from`
- 管道式处理
- **进阶技能**

---

## 十一、最后的最后

**Python 生成器，3 句话总结**：

1. **生成器是懒人函数**：一次一个，不存所有
2. **内存省 100 倍**：处理大数据必备
3. **yield 是核心**：理解 yield = 理解生成器

**学 Python 6 年，我学到的最重要的事：**

**"不会生成器，你的 Python 是'入门级'。"**

**会生成器，**你的代码能处理 100GB 数据**。**

**数据科学家、AI 工程师、Web 开发者**都用得上**。**

**学 Python 6 年，**生成器是性价比最高的学习**。**

---

## 相关阅读

- [2026 年学习编程，你需要的不是更多教程](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)
- [🖊️ 想做视频号 / 抖音 / 小红书？AI 帮你一键生成，不用学剪辑，免费试用 3 次](https://libtv.cgref.cn/s/9omkl4jn4d)
- [🎁 国产 CodeX AI 办公助手 | 写方案/PPT/分析 一次搞定](https://www.codebuddy.cn/events/invite?inviteCode=ic1tpbrj2x)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [我的建站搭子skill，入职腾讯QClaw了！动动嘴就能建网站](https://mp.weixin.qq.com/s/XEe9yMpseRvMizhWcbnEoA)
- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)

---

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《50讲 · AI编程训练营》](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲，先看看适不适合自己](https://pan.quark.cn/s/8f7886f79569)
- 👉 - 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/3978Ig)
