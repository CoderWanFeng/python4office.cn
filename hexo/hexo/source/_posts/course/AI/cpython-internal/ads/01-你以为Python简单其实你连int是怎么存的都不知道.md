---
title: 你以为Python简单？其实你连int是怎么存的都不知道
date: 2026-04-17 08:00:00
tags: [Python进阶, CPython, 源码解析]
cover: https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop
---

大家好，这里是程序员晚枫，正在all in AI编程实战。

今天聊一个扎心的话题：**你天天写Python，但你真的了解Python吗？**

```python
a = 1
b = 1
print(a is b)  # True

a = 257
b = 257
print(a is b)  # False ???
```

看到这个结果，你是不是懵了？同样都是赋值，为什么一个True一个False？

**答案藏在CPython的源码里。**

---

## 小整数缓存：-5到256的秘密

CPython会预先创建-5到256的整数对象：

```c
#define NSMALLPOSINTS 257
#define NSMALLNEGINTS 5
static PyLongObject *small_ints[NSMALLNEGINTS + NSMALLPOSINTS];
```

所以1是同一个对象（缓存命中），257是两个不同的对象。

**这就是为什么Python程序员需要了解底层实现——不然你永远解释不了这种"诡异"行为。**

---

## 大整数怎么存？

Python的int可以无限大，它是怎么做到的？

答案是用变长数组：

```c
// 2^30进制存储
#define PyLong_SHIFT 30
struct _longobject {
    PyObject_HEAD
    digit ob_digit[1];  // 按需扩展
};
```

也就是说，999999999在Python内部是一个数组，不是简单的C int。

**想要彻底搞懂这些？** 我的《CPython设计与实现》20讲课程，从对象模型到垃圾回收，从字节码到GIL，带你一行行读源码。

👉 [查看课程大纲](/course/AI/cpython-internal/00-课程大纲/)

---

## 你会得到什么？

- 理解Python的执行原理，写出更高效的代码
- 面试时从"会用"变成"精通"，碾压其他候选人
- 能看懂CPython源码，遇到bug自己排查

**别再用"Python很简单"来麻痹自己了。真正的差距，就在底层。**

---

有问题欢迎加微信 python-office 进群交流~

程序员晚枫专注AI编程培训，小白看完他和图灵社区合作的教程[《30讲·AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)就能上手做AI项目。


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


