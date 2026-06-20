---
title: "Python 性能优化完整指南：从慢代码到快代码的 10 个方法"
date: 2026-06-20 18:04:29
tags: ["Python", "性能优化", "AI工具", "公众号文章"]
categories: ["公众号文章"]
description: "Python 性能优化完整指南：从慢代码到快代码的 10 个方法，让你的 Python 飞起来"
cover: https://images.unsplash.com/photo-1526379095098-d400fd0bf935?q=80&w=1200&auto=format&fit=crop
---

大家好，我是程序员晚枫。

**Python 慢？**别再怪 Python 了**。**

**你的代码烂，Python 才慢。**

**今天给你 10 个让 Python 飞起来的方法。**

---

## 一、为什么 Python 慢？

**Python 慢的真实原因**：

- ✅ **动态类型**：运行时检查
- ✅ **GIL**：全局解释器锁
- ✅ **解释执行**：非编译
- ✅ **垃圾回收**：GC 暂停
- ❌ **不是 Python 的问题**

**大多数情况**：

- 90% 的"慢"是 **代码烂**
- 9% 是 **架构差**
- 1% 才是 **语言限制**

**优化代码比换语言重要 10 倍。**

---

## 二、方法 1：用 NumPy 替代循环

**NumPy** 比 Python 循环快 **50-100 倍**。

### 慢代码

```python
import time

start = time.time()
result = 0
for i in range(10_000_000):
    result += i ** 2
print(time.time() - start)  # 3.5 秒
```

### 快代码

```python
import numpy as np
import time

start = time.time()
arr = np.arange(10_000_000)
result = np.sum(arr ** 2)
print(time.time() - start)  # 0.05 秒
```

**快 70 倍**。

---

## 三、方法 2：用列表推导式

**列表推导式**比循环 + append 快 **30%**。

### 慢代码

```python
result = []
for i in range(1000):
    result.append(i ** 2)
```

### 快代码

```python
result = [i ** 2 for i in range(1000)]
```

**快 30%**。

---

## 四、方法 3：用生成器处理大数据

**生成器**节省内存，**适合大数据**。

### 慢代码（占用 1GB 内存）

```python
def get_data():
    data = [i ** 2 for i in range(10_000_000)]
    return data

for x in get_data():
    process(x)
```

### 快代码（占用 100B 内存）

```python
def get_data():
    for i in range(10_000_000):
        yield i ** 2

for x in get_data():
    process(x)
```

**内存省 1 万倍**。

---

## 五、方法 4：用 lru_cache 缓存

**functools.lru_cache** 让函数自动缓存。

### 慢代码

```python
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))  # 5 秒
```

### 快代码

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))  # 0.0001 秒
```

**快 5 万倍**。

---

## 六、方法 5：用 Cython/C 扩展关键代码

**Cython** 把 Python 编译成 C。

### 示例

```python
# 慢的 Python
def add(x, y):
    return x + y

# 等价的 Cython
cdef int add(int x, int y):
    return x + y
```

**快 50-100 倍**。

---

## 七、方法 6：用 asyncio 做并发

**asyncio** 处理 **I/O 密集**任务。

### 慢代码（串行 10 秒）

```python
import requests
import time

urls = [f'https://api.example.com/{i}' for i in range(10)]
start = time.time()
for url in urls:
    requests.get(url)
print(time.time() - start)  # 10 秒
```

### 快代码（并发 1 秒）

```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        urls = [f'https://api.example.com/{i}' for i in range(10)]
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())  # 1 秒
```

**快 10 倍**。

---

## 八、方法 7：用 multiprocessing 做 CPU 密集

**多进程**处理 **CPU 密集**任务。

### 慢代码（单核 8 秒）

```python
def work(x):
    return x ** 2

result = [work(i) for i in range(8)]
```

### 快代码（8 核 1 秒）

```python
from multiprocessing import Pool

def work(x):
    return x ** 2

with Pool(8) as p:
    result = p.map(work, range(8))
```

**快 8 倍**。

---

## 九、方法 8：用 C 库（NumPy、pandas）

**调用 C 库**，比纯 Python 快。

### 示例

```python
# 慢
sum(range(10_000_000))

# 快（C 实现）
import numpy as np
np.sum(np.arange(10_000_000))
```

**快 10-100 倍**。

---

## 十、方法 9：用合适的数据结构

**数据结构**决定性能。

| 场景 | 用 | 不用 |
|------|---|------|
| 频繁查找 | **set / dict** | list |
| 频繁插入 | **deque** | list |
| 有序 | **OrderedDict** | dict |
| 大量数值 | **NumPy** | list |
| 字符串拼接 | **join** | + |

### 慢代码

```python
text = ""
for s in strings:
    text += s  # O(n²)
```

### 快代码

```python
text = "".join(strings)  # O(n)
```

**快 100 倍**。

---

## 十一、方法 10：用 profiling 找瓶颈

**不要猜，要测**。

### 工具 1：cProfile

```python
import cProfile
import pstats

cProfile.run('my_function()', 'profile_data')
stats = pstats.Stats('profile_data')
stats.sort_stats('cumulative')
stats.print_stats(10)
```

### 工具 2：line_profiler

```bash
pip install line_profiler
kernprof -l -v my_script.py
```

### 工具 3：memory_profiler

```bash
pip install memory_profiler
python -m memory_profiler my_script.py
```

### 工具 4：py-spy

- 实时 profiling
- **生产环境可用**

**找到瓶颈，再优化**。

---

## 十二、5 大性能误区

### 误区 1：过早优化

- ❌ 错
- ✅ **先写对，再写快**
- Donald Knuth: "过早优化是万恶之源"

### 误区 2：所有代码都要优化

- ❌ 错
- ✅ **80/20 法则**
- 优化 20% 关键代码

### 误区 3：换语言更快

- ❌ 错
- ✅ 90% 情况优化 Python 就够
- **学习成本高**

### 误区 4：Python 不适合生产

- ❌ 错
- ✅ Instagram、Dropbox 都在用
- **架构 > 语言**

### 误区 5：多线程 = 加速

- ❌ 错
- ✅ GIL 让多线程无效
- **多进程或 asyncio**

---

## 十三、5 大性能工具

### 工具 1：NumPy

- 数值计算
- **必备**

### 工具 2：Pandas

- 数据处理
- **数据科学必备**

### 工具 3：Cython

- 编译 Python
- **快 50-100 倍**

### 工具 4：PyPy

- 替代 CPython
- **快 5-10 倍**

### 工具 5：Numba

- JIT 编译器
- **快 10-100 倍**

### 简单示例（Numba）

```python
from numba import njit
import numpy as np

@njit
def fast_function(arr):
    total = 0
    for x in arr:
        total += x ** 2
    return total

arr = np.arange(1_000_000)
print(fast_function(arr))  # 0.001 秒
```

**比纯 Python 快 1000 倍**。

---

## 十四、5 个性能优化真实案例

### 案例 1：Instagram

- **优化前**：Python 慢
- **优化后**：JIT、缓存、CDN
- **结果**：10 亿用户

### 案例 2：Dropbox

- **优化前**：同步上传慢
- **优化后**：分片 + 并发
- **结果**：5 亿用户

### 案例 3：YouTube

- **优化前**：视频处理慢
- **优化后**：C 扩展 + 缓存
- **结果**：10 亿用户

### 案例 4：Spotify

- **优化前**：推荐慢
- **优化后**：NumPy + Kafka
- **结果**：千万级用户

### 案例 5：Uber

- **优化前**：调度慢
- **优化后**：C++ 核心 + Python 接口
- **结果**：全球服务

---

## 十五、给 Python 性能优化学习者的 4 个建议

### 建议 1：先 profile 再优化

- 找到瓶颈
- **不要猜**

### 建议 2：选对数据结构

- set > list 查找
- **基础决定性能**

### 建议 3：用 C 库

- NumPy、pandas
- **C 实现比 Python 快**

### 建议 4：架构 > 优化

- 缓存、CDN、并发
- **比代码优化更有效**

---

## 十六、最后的最后

**Python 性能优化，3 句话总结**：

1. **90% 的慢是代码烂**：先写对再写快
2. **NumPy + asyncio 是基础**：C 库 + 异步
3. **架构 > 优化**：缓存、CDN、并发更有效

**学 Python 6 年，我学到的最重要的事：**

**"Python 慢不慢，看你怎么写。"**

**同样的功能，**好代码快 10-100 倍**。**

**会优化的 Python 工程师，**比会用 C++ 的值钱**。**

**因为你能用 Python 写出 C 的速度，**效率是普通人的 10 倍**。**

---

## 相关阅读

- [2026 年学习编程，你需要的不是更多教程](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)
- [我用AI做PPT，同事说你是PPT设计师吗](https://mp.weixin.qq.com/s/aLo7mW3BLnglwhSZCKoOow)
- [设计师花3天做的图，我用 AI 15分钟搞定了](https://mp.weixin.qq.com/s/BQZUEFVCWhx8lLDaQsbRTg)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [HR看简历只花6秒，我用AI让我的简历过了第一关](https://mp.weixin.qq.com/s/XD8bk9Wf6p47HEoP8h84RQ)
- [我用AI做数字人播报，老板问"你什么时候请的主播？"](https://mp.weixin.qq.com/s/7vngGHvX-HxIsUsQHGp1Dw)

---

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《50讲 · AI编程训练营》](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲，先看看适不适合自己](https://pan.quark.cn/s/8f7886f79569)
- 👉 - 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/3978Ig)
