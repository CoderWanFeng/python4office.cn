---
title: "Python 并发编程完整指南：threading vs multiprocessing vs asyncio 怎么选？"
date: 2026-06-20 18:09:12
tags: ["Python", "并发编程", "threading", "multiprocessing", "asyncio", "AI工具", "公众号文章"]
categories: ["公众号文章"]
description: "Python 并发编程完整指南：threading vs multiprocessing vs asyncio 三大并发模型怎么选？5 大场景实战"
cover: https://images.unsplash.com/photo-1526379095098-d400fd0bf935?q=80&w=1200&auto=format&fit=crop
---

大家好，我是程序员晚枫。

**Python 慢，是你的"并发模型"没选对。**

**threading、multiprocessing、asyncio 怎么选？**

**今天彻底讲透。**

---

## 一、为什么需要并发？

**3 类任务的瓶颈**：

| 任务类型 | 瓶颈 | 例子 |
|---------|------|------|
| **I/O 密集** | 等待网络/磁盘 | HTTP 请求、数据库查询 |
| **CPU 密集** | 计算 | 数据处理、ML 训练 |
| **混合** | 都有 | Web 服务 |

**单线程 = 串行 = 慢**。

**并发 = 多任务同时 = 快**。

---

## 二、Python 3 大并发模型

### 模型 1：threading（多线程）

```python
import threading
import time

def work():
    time.sleep(1)
    print("Done")

t = threading.Thread(target=work)
t.start()
t.join()
```

### 模型 2：multiprocessing（多进程）

```python
import multiprocessing
import time

def work():
    time.sleep(1)
    print("Done")

p = multiprocessing.Process(target=work)
p.start()
p.join()
```

### 模型 3：asyncio（异步）

```python
import asyncio

async def work():
    await asyncio.sleep(1)
    print("Done")

asyncio.run(work())
```

---

## 三、3 大模型详细对比

| 维度 | threading | multiprocessing | asyncio |
|------|-----------|----------------|---------|
| **并行** | ❌ 假并行（GIL） | ✅ 真并行 | ❌ 单线程 |
| **I/O 密集** | ✅ 适合 | ❌ 不适合 | ✅ **最适合** |
| **CPU 密集** | ❌ 不适合 | ✅ **最适合** | ❌ 不适合 |
| **多核** | ❌ 不能用 | ✅ **能用** | ❌ 不能用 |
| **内存占用** | 小 | 大（每进程独立） | 极小 |
| **创建开销** | 小 | 大 | 极小 |
| **通信** | 简单（共享变量） | 复杂（IPC） | 简单（队列）|
| **调试** | 难 | 难 | 较简单 |
| **学习曲线** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

---

## 四、5 大场景选型

### 场景 1：HTTP 客户端

**推荐**：**asyncio + aiohttp**

- I/O 密集
- **首选 asyncio**

### 场景 2：Web 服务器

**推荐**：**asyncio（FastAPI）+ threading**

- 混合型
- 现代用 asyncio

### 场景 3：数据处理

**推荐**：**multiprocessing**

- CPU 密集
- 必须用多进程

### 场景 4：ML 训练

**推荐**：**multiprocessing + numpy**

- CPU/GPU 密集
- 多进程或 GPU

### 场景 5：文件 I/O

**推荐**：**asyncio + aiofiles**

- I/O 密集
- asyncio 最佳

---

## 五、3 大模型底层原理

### 原理 1：GIL

**GIL = Global Interpreter Lock**（全局解释器锁）

- Python 一次只能跑一个线程
- 多线程 = 假并行
- **只对 CPU 密集任务有效**

**多线程适合**：I/O 等待时切换线程

### 原理 2：多进程

- 每个进程有独立 Python 解释器
- **真正的并行**
- 进程间通信用 IPC（Queue、Pipe）

### 原理 3：asyncio 事件循环

- 单线程
- 协程在 I/O 等待时切换
- **高效 I/O 并发**

---

## 六、5 大 threading 实战

### 实战 1：基础线程

```python
import threading

def work(n):
    print(f"Thread {n} running")

threads = []
for i in range(5):
    t = threading.Thread(target=work, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### 实战 2：线程锁

```python
import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter)  # 100
```

### 实战 3：ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor

def work(n):
    return n ** 2

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(work, range(10))
    print(list(results))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 实战 4：生产者-消费者

```python
import threading
import queue

q = queue.Queue()

def producer():
    for i in range(10):
        q.put(i)

def consumer():
    while True:
        item = q.get()
        print(f"Got: {item}")
        q.task_done()
        if item == 9:
            break

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()
```

### 实战 5：定时线程

```python
import threading
import time

def periodic():
    print(f"Time: {time.time()}")
    threading.Timer(1, periodic).start()

periodic()
```

---

## 七、5 大 multiprocessing 实战

### 实战 1：基础进程

```python
import multiprocessing

def work(n):
    return n ** 2

if __name__ == '__main__':
    p = multiprocessing.Process(target=work, args=(5,))
    p.start()
    p.join()
```

### 实战 2：进程池

```python
import multiprocessing

def work(n):
    return n ** 2

if __name__ == '__main__':
    with multiprocessing.Pool(4) as pool:
        results = pool.map(work, range(10))
        print(list(results))
```

### 实战 3：ProcessPoolExecutor

```python
from concurrent.futures import ProcessPoolExecutor

def work(n):
    return n ** 2

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(work, range(10))
        print(list(results))
```

### 实战 4：进程间通信

```python
import multiprocessing

def producer(q):
    for i in range(5):
        q.put(i)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Got: {item}")

if __name__ == '__main__':
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    q.put(None)  # 结束信号
    p2.join()
```

### 实战 5：共享内存

```python
import multiprocessing

def work(n, return_dict):
    return_dict[n] = n ** 2

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=work, args=(i, return_dict))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print(dict(return_dict))
```

---

## 八、5 大 asyncio 实战

### 实战 1：基础协程

```python
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello())
```

### 实战 2：gather 并发

```python
import asyncio

async def work(n):
    await asyncio.sleep(1)
    return n * 2

async def main():
    results = await asyncio.gather(*[work(i) for i in range(5)])
    print(results)  # [0, 2, 4, 6, 8]

asyncio.run(main())
```

### 实战 3：Task

```python
import asyncio

async def work(n):
    await asyncio.sleep(1)
    return n

async def main():
    tasks = [asyncio.create_task(work(i)) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

### 实战 4：Queue

```python
import asyncio

async def producer(queue):
    for i in range(5):
        await queue.put(i)
        await asyncio.sleep(0.1)

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Got: {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    p = asyncio.create_task(producer(queue))
    c = asyncio.create_task(consumer(queue))
    await p
    await queue.put(None)
    await c

asyncio.run(main())
```

### 实战 5：Semaphore 限流

```python
import asyncio

sem = asyncio.Semaphore(3)

async def work(n):
    async with sem:
        print(f"Start {n}")
        await asyncio.sleep(1)
        print(f"End {n}")

async def main():
    await asyncio.gather(*[work(i) for i in range(10)])

asyncio.run(main())
```

---

## 九、3 大模型混合使用

### 混合 1：asyncio + threading

```python
import asyncio
import threading

def sync_work():
    # 同步阻塞操作
    import time
    time.sleep(1)
    return "Done"

async def main():
    loop = asyncio.get_event_loop()
    # 在线程池中运行同步代码
    result = await loop.run_in_executor(None, sync_work)
    print(result)

asyncio.run(main())
```

### 混合 2：asyncio + multiprocessing

```python
import asyncio
import multiprocessing

def cpu_work(n):
    return n ** 2

async def main():
    loop = asyncio.get_event_loop()
    # 在进程池中运行 CPU 密集
    result = await loop.run_in_executor(
        multiprocessing.Pool(4),
        cpu_work,
        5
    )
    print(result)

asyncio.run(main())
```

### 混合 3：FastAPI 混合

```python
from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(1)
    return {"type": "async"}

@app.get("/sync")
def sync_endpoint():
    time.sleep(1)
    return {"type": "sync"}
```

---

## 十、5 大常见误区

### 误区 1：多线程 = 加速

- ❌ 错
- ✅ **GIL 让 CPU 密集无效**
- 只有 I/O 密集有效

### 误区 2：多进程越多越好

- ❌ 错
- ✅ 进程太多反而慢
- **CPU 核心数 = 最佳进程数**

### 误区 3：asyncio 替代多线程

- ⚠️ 部分对
- ✅ asyncio 是单线程
- **不能多核**

### 误区 4：asyncio 替代多进程

- ❌ 错
- ✅ asyncio 不能 CPU 密集
- **必须用多进程**

### 误区 5：随便用

- ❌ 错
- ✅ **按场景选型**
- 不选型 = 性能差

---

## 十一、5 大真实项目案例

### 案例 1：Instagram

- **场景**：10 亿用户
- **方案**：Django + asyncio + multiprocessing
- **结果**：高并发稳定

### 案例 2：Dropbox

- **场景**：文件同步
- **方案**：threading + multiprocessing
- **结果**：5 亿用户

### 案例 3：OpenAI

- **场景**：API 服务
- **方案**：asyncio + multiprocessing
- **结果**：百万开发者

### 案例 4：YouTube

- **场景**：视频转码
- **方案**：multiprocessing + C 扩展
- **结果**：10 亿用户

### 案例 5：Instagram 照片处理

- **场景**：图片处理
- **方案**：multiprocessing + Pillow
- **结果**：亿级图片

---

## 十二、给 Python 并发学习者的 4 个建议

### 建议 1：先学 asyncio

- 现代、未来趋势
- **1 周上手**

### 建议 2：再学 multiprocessing

- CPU 密集必备
- **3 天上手**

### 建议 3：threading 按需

- 简单 I/O 密集
- **2 天上手**

### 建议 4：混合使用

- 复杂项目必混合
- **理解原理**

---

## 十三、最后的最后

**Python 并发编程，3 句话总结**：

1. **I/O 密集用 asyncio**：网络、文件
2. **CPU 密集用 multiprocessing**：数据处理、ML
3. **混合用按需**：asyncio + multiprocessing

**学 Python 6 年，我学到的最重要的事：**

**"并发模型选错，性能差 10-100 倍。"**

**新手用 asyncio，进阶用 multiprocessing，专家混合用。**

**会并发的 Python 工程师，**比不会的贵 50%**。**

**学并发，**5 年后你就是 Python 专家**。**

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
