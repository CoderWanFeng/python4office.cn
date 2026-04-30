---
title: 第 15 讲：GIL 全局解释器锁——原理、影响与应对策略
date: 2026-03-03 11:15:00
tags: [python, CPython, GIL, 全局解释器锁]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<!-- more -->

![第 15 讲：GIL 全局解释器锁——原理、影响与应对策略](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)
![第 15 讲：GIL 全局解释器锁——原理、影响与应对策略](https://images.unsplash.com/photo-151707730?w=800&h=400&fit=crop)


> 大家好，我是正在实战各种 AI 项目的程序员晚枫。

**为什么多线程不能加速 CPU 密集型任务？Python 的 GIL（全局解释器锁）是罪魁祸首。这一讲，我们彻底搞懂它。**

---

## 📖 开篇：多线程为什么不加速？

```python
import threading
import time

def cpu_task(n):
    # CPU 密集型任务
    total = 0
    for i in range(n):
        total += i * i
    return total

# 单线程
start = time.perf_counter()
cpu_task(10**7)
cpu_task(10**7)
end = time.perf_counter()
print(f"单线程: {end - start:.2f}s")

# 多线程
start = time.perf_counter()
t1 = threading.Thread(target=cpu_task, args=(10**7,))
t2 = threading.Thread(target=cpu_task, args=(10**7,))
t1.start(); t2.start()
t1.join(); t2.join()
end = time.perf_counter()
print(f"多线程: {end - start:.2f}s")

# 输出：两者几乎一样！多线程没有加速！
```

**罪魁祸首：GIL（Global Interpreter Lock）**

---

## 🔒 GIL 是什么？

```c
// Python/ceval_gil.h
static PyThread_type_lock interpreter_lock = 0;  // GIL 本质是一个互斥锁

// 获取 GIL
void PyEval_AcquireLock(void) {
    PyThread_acquire_lock(interpreter_lock, WAIT_LOCK);
}

// 释放 GIL
void PyEval_ReleaseLock(void) {
    PyThread_release_lock(interpreter_lock);
}
```

### GIL 的作用

```
线程A ──→ 获取 GIL ──→ 执行字节码 ──→ 释放 GIL ──→ 
线程B ──→ 获取 GIL ──→ 执行字节码 ──→ 释放 GIL ──→
                              ↑
                        同一时刻只有一个线程
                      在执行 Python 字节码！
```

**GIL 确保**：同一时刻，CPython 解释器中只有一个线程在执行 Python 字节码。

### 为什么需要 GIL？

**原因：引用计数！**

```c
// 每次创建/销毁对象时，需要修改引用计数
PyObject* Py_INCREF(PyObject* o) {
    o->ob_refcnt++;  // 需要线程安全！
}

// 如果没有 GIL，两个线程同时操作引用计数：
// 线程A: ob_refcnt++
// 线程B: ob_refcnt--
// 结果：计数器错乱 → 对象被错误释放 → 内存泄漏或崩溃
```

GIL 让引用计数的操作「原子化」，不需要额外的锁，成本最低。

---

## ⚡ GIL 的释放时机

GIL 不是一直持有，而是**周期性释放**：

### 时机1：IO 操作

```c
// 文件/网络/数据库等 IO 操作时，Python 会释放 GIL
// 让其他线程有机会执行
```

```python
# IO 密集型任务可以从多线程获益
import threading
import time

def io_task():
    time.sleep(0.001)  # IO 等待，释放 GIL

start = time.perf_counter()
threads = [threading.Thread(target=io_task) for _ in range(100)]
for t in threads: t.start()
for t in threads: t.join()
end = time.perf_counter()
print(f"100个IO任务: {end - start:.2f}s")  # 比串行快很多！
```

### 时机2：字节码计数（Python 3.2+）

```c
// 每执行 N 条字节码指令后，释放 GIL
// 默认 N = 1000（Python 3.9+ 可通过配置）

if (--_Py_Ticker <= 0) {
    drop_gil(tstate);
    // 可能切换到其他线程
    take_gil(tstate);
    _Py_Ticker = checkinterval;
}
```

### Python 版本演进

| 版本 | GIL 行为 |
|------|----------|
| Python 2 | 每 100 条字节码检查一次 |
| Python 3.2 | 改为 15ms 时间片，减少切换开销 |
| Python 3.11+ | 优化了 GIL 的获取/释放速度 |
| Python 3.13 (实验) | 无 GIL 模式（PEP 703）|

---

## 🎯 应对策略

### CPU 密集型 → 多进程

```python
from multiprocessing import Pool
import time

def cpu_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

if __name__ == '__main__':
    start = time.perf_counter()
    with Pool(4) as p:
        results = p.map(cpu_task, [10**7] * 4)
    end = time.perf_counter()
    print(f"多进程: {end - start:.2f}s")  # 显著加速！
```

### IO 密集型 → 线程或异步

```python
# 方式 1：多线程
import threading

def fetch_url(url):
    import urllib.request
    return urllib.request.urlopen(url).read()

threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
# IO 时自动释放 GIL，线程并行效果好
```

```python
# 方式 2：asyncio（推荐！）
import asyncio

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```

### 混合场景 → ProcessPoolExecutor

```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

# CPU 密集用进程，IO 密集用线程
with ProcessPoolExecutor() as cpu_pool:
    with ThreadPoolExecutor() as io_pool:
        cpu_result = cpu_pool.submit(heavy_compute, data)
        io_result = io_pool.submit(fetch_data, url)
```

---

## 🧪 性能对比实验

```python
import threading, multiprocessing, time

def cpu_task(n):
    return sum(i * i for i in range(n))

def io_task(delay):
    time.sleep(delay)
    return 'done'

# ===== CPU 密集型 =====
# 单线程
t = time.perf_counter()
[cpu_task(10**6) for _ in range(4)]
print(f'单线程: {time.perf_counter() - t:.2f}s')

# 多线程（无加速！）
t = time.perf_counter()
[threading.Thread(target=cpu_task, args=(10**6,)) for _ in range(4)]
print(f'多线程: {time.perf_counter() - t:.2f}s')

# 多进程（显著加速！）
t = time.perf_counter()
with multiprocessing.Pool(4) as p:
    p.map(cpu_task, [10**6] * 4)
print(f'多进程: {time.perf_counter() - t:.2f}s')
```

---

## 💡 本节作业

1. 用 timeit 对比：多线程 vs 多进程处理 CPU 密集型任务
2. 用 asyncio 重写一个 IO 密集型任务
3. 搜索：Python 3.13 的 No-GIL 模式是什么进展？

---

## 🎯 本讲总结

**GIL 原理**：全局互斥锁，同一时刻只有一个线程执行 Python 字节码。

**GIL 原因**：保护引用计数，避免线程安全问题（最低成本方案）。

**释放时机**：IO 等待时、字节码计数耗尽时（~15ms）。

**应对策略**：CPU 密集型用多进程（ProcessPoolExecutor），IO 密集型用 asyncio/线程。

---

## 📚 推荐教材

**[《Python 编程从入门到实践（第 3 版）》](https://u.jd.com/NGMHz3T)** | **[《流畅的 Python（第 2 版）》](https://u.jd.com/NOMBOOz)** | **[《CPython 设计与实现》](https://u.jd.com/NaM5rNE)**

---

## 🔗 课程导航

← [上一讲：栈帧与调用约定](14-栈帧与调用约定.md) | [下一讲：线程与并发](16-线程与并发.md) →

---

## 💬 联系我

| 平台 | 账号/链接 |
|------|----------|
| 微信 | [扫码加好友](https://www.python4office.cn/wechat-qrcode/) |
| B 站 | [Python 自动化办公社区](https://space.bilibili.com/259649365) |

**主营业务**：AI 编程培训、企业内训、技术咨询


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


