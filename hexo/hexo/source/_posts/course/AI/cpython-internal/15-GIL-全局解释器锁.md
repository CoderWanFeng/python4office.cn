---
title: 第 15 讲：GIL 全局解释器锁——原理、影响与应对策略
date: 2026-03-03 11:15:00
tags: [python, CPython, GIL, 全局解释器锁]
---

<!-- more -->

> 大家好，我是正在实战各种 AI 项目的程序员晚枫。

**为什么多线程不能加速 CPU 密集型任务？罪魁祸首是 GIL。**

---

## 🔒 GIL 是什么？

```c
// Python/ceval_gil.h
// GIL 确保任何时候只有一个线程执行 Python 字节码
static PyThread_type_lock GIL;

// 获取 GIL
void PyEval_AcquireLock(void) {
    PyThread_acquire_lock(GIL, WAIT_LOCK);
}

// 释放 GIL
void PyEval_ReleaseLock(void) {
    PyThread_release_lock(GIL);
}
```

---

## ⚡ GIL 的释放时机

1. **IO 操作时自动释放**：文件读写、网络请求、time.sleep()

2. **周期性检查（默认 5ms）**：
```c
// 每执行一定数量的字节码指令后检查
if (--_Py_Ticker < 0) {
    _Py_Ticker = _Py_CheckInterval;
    // 可能切换线程
}
```

---

## 🎯 应对策略

| 场景 | 解决方案 |
|------|---------|
| CPU 密集型 | multiprocessing |
| IO 密集型 | threading/asyncio |
| 混合场景 | ProcessPoolExecutor |

---

## 🎯 本讲总结

**GIL 原理**：确保单线程执行字节码。

**释放时机**：IO 操作、周期性检查。

**应对策略**：多进程、异步 IO。

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
