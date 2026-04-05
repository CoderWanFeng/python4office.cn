---
title: 第 2 讲：Python 对象模型深度解析——PyObject 与引用计数机制
date: 2026-03-03 10:10:00
tags: [python, CPython, PyObject, 引用计数，对象模型]
---

<!-- more -->

> 大家好，我是正在实战各种 AI 项目的程序员晚枫。

**Python 中"一切皆对象"，但你知道这个"对象"在 C 语言层面长什么样吗？**

当你写下 `a = 1`，Python 内部创建了一个对象；当你写下 `b = a`，并没有复制数据，只是增加了引用计数。理解这些底层机制，是掌握 Python 内存管理的基础。

想象一下，Python 世界就像一个巨大的仓库。仓库里的每一件物品都是一个"对象"，而每个对象都有一个统一的"标签"，上面记录着这个物品的基本信息。这个标签，就是 PyObject 结构体。

---

## 🔍 PyObject 结构体——所有对象的基石

在 CPython 中，所有的 Python 对象在 C 语言层面都是 `PyObject` 结构体的指针。这是 Python 对象系统的核心设计。

### PyObject 的定义

```c
// Include/object.h

typedef struct _object {
    _PyObject_HEAD_EXTRA  // 调试用的额外字段（通常为空）
    Py_ssize_t ob_refcnt;     // 引用计数
    struct _typeobject *ob_type;  // 指向类型对象的指针
} PyObject;
```

这个结构体只有两个核心字段，却支撑起了整个 Python 的对象系统：

| 字段 | 类型 | 作用 |
|------|------|------|
| ob_refcnt | Py_ssize_t | 记录有多少个引用指向这个对象 |
| ob_type | struct _typeobject* | 指向该对象的类型描述符 |

### 为什么只有两个字段？

这种设计的精妙之处在于：**统一性**。

```c
// 任何 Python 对象都可以表示为 PyObject*
PyObject *obj;  // 可以是整数、字符串、列表...

// 统一的操作接口
Py_INCREF(obj);  // 增加引用计数
Py_DECREF(obj);  // 减少引用计数
Py_TYPE(obj);    // 获取类型
```

具体的数据存储在子类中。例如，整数对象：

```c
// Include/longintrepr.h
struct _longobject {
    PyObject_HEAD          // 继承 PyObject 的头部
    digit ob_digit[1];     // 变长数组存储数字
};
```

`PyObject_HEAD` 是一个宏，展开后就是 `ob_refcnt` 和 `ob_type`。这种设计让所有对象都有一个共同的"头部"，便于统一管理。

### 对象内存布局示意

```
整数对象 100 的内存布局：
┌─────────────────────────────────┐
│  PyObject_HEAD                  │
│  ├─ ob_refcnt: 3               │  ← 有 3 个引用
│  └─ ob_type: → int 类型对象    │  ← 指向类型
├─────────────────────────────────┤
│  ob_digit: [100]               │  ← 实际存储的值
└─────────────────────────────────┘
```

---

## 📊 引用计数机制详解

### 什么是引用计数？

引用计数是 Python 最主要的内存管理机制。每个对象维护一个计数器，记录有多少个变量引用它：

- **创建对象**：计数器初始化为 1
- **新增引用**：计数器 +1
- **删除引用**：计数器 -1
- **计数器归零**：销毁对象，释放内存

这个过程是自动的，你不需要手动管理。但理解它，能帮你写出更高效的代码。

### Python 层面的观察

```python
import sys

# 创建对象，引用计数为 1
a = []
print(sys.getrefcount(a))  # 输出 2（a + getrefcount 参数）

# 新增引用，计数 +1
b = a
print(sys.getrefcount(a))  # 输出 3

# 删除引用，计数 -1
del b
print(sys.getrefcount(a))  # 输出 2

# 小整数被缓存，引用计数很高
c = 100
print(sys.getrefcount(100))  # 输出几百甚至上千
```

注意：`getrefcount` 函数本身会临时增加引用计数，所以返回值要减 1 才是实际的引用数。

### C 语言层面的实现

```c
// Include/object.h

// 增加引用计数
static inline void Py_INCREF(PyObject *op)
{
    op->ob_refcnt++;
}

// 减少引用计数
static inline void Py_DECREF(PyObject *op)
{
    if (--op->ob_refcnt == 0) {
        _Py_Dealloc(op);  // 销毁对象
    }
}
```

这些宏看起来简单，但它们是 Python 内存管理的核心。每次你创建一个变量、传递一个参数、返回一个值，都会触发这些操作。

### 引用计数的线程安全问题

在多线程环境下，简单的 `++` 和 `--` 操作不是原子性的，可能导致竞态条件。CPython 通过 GIL（全局解释器锁）来解决这个问题——任何时候只有一个线程执行 Python 字节码，因此引用计数操作是线程安全的。

但这同时也是多线程不能并行执行的原因（第 15 讲详细讨论）。

---

## 🏷️ 类型对象系统

### PyTypeObject 结构体

每个对象都知道自己的类型，类型本身也是对象：

```c
// Include/cpython/object.h
typedef struct _typeobject {
    PyObject_VAR_HEAD           // 类型对象也是对象
    const char *tp_name;        // 类型名称（如"int"）
    Py_ssize_t tp_basicsize;    // 实例大小
    
    // 方法族（函数指针集合）
    PyNumberMethods *tp_as_number;      // 数值方法
    PySequenceMethods *tp_as_sequence;  // 序列方法
    PyMappingMethods *tp_as_mapping;    // 映射方法
    
    // 属性访问
    getattrfunc tp_getattr;
    setattrfunc tp_setattr;
    
    // 标准操作
    reprfunc tp_repr;           // __repr__
    hashfunc tp_hash;           // __hash__
    ternaryfunc tp_call;        // __call__
    
    // ... 更多字段
} PyTypeObject;
```

这个结构体定义了类型的所有特性：

| 字段组 | 作用 |
|--------|------|
| tp_name | 类型的名称，用于打印和调试 |
| tp_basicsize | 实例对象的大小（字节） |
| tp_as_number | 数值运算方法（+、-、*等） |
| tp_as_sequence | 序列操作方法（索引、切片等） |
| tp_as_mapping | 映射操作方法（键值访问等） |
| tp_repr | __repr__方法的实现 |
| tp_call | __call__方法的实现 |

### 类型的类型

有趣的是，类型对象的类型是 `type`：

```python
>>> type(1)
<class 'int'>

>>> type(int)
<class 'type'>

>>> type(type)
<class 'type'>  # type 是自己的类型！
```

这形成了完美的自举系统：

```
对象 ← 由类型创建
  ↓
type ← 也是对象，由自己创建
  ↓
（闭环）
```

### 类型继承关系

```
object (所有类的基类)
  │
  ├── int
  ├── str
  ├── list
  ├── dict
  └── ... (更多内置类型)
```

在 C 层面，这种继承关系通过结构体嵌套实现。子类结构体的第一个字段一定是父类结构体，这样保证了类型转换的安全性。

---

## 🔄 对象的生命周期

### 创建对象

```c
// 以创建整数为例
PyObject *PyLong_FromLong(long ival)
{
    PyLongObject *v;
    
    // 1. 检查是否在小整数缓存范围内
    if (-NSMALLNEGINTS <= ival && ival < NSMALLPOSINTS) {
        return small_ints[ival + NSMALLNEGINTS];
    }
    
    // 2. 分配内存
    v = _PyLong_New(ndigits);
    if (v == NULL)
        return NULL;
    
    // 3. 初始化数据
    # ... 设置数字值 ...
    
    # 4. 返回对象（引用计数已为 1）
    return (PyObject *)v;
}
```

这个过程展示了对象创建的标准流程：检查缓存→分配内存→初始化→返回。

### 销毁对象

当引用计数归零时：

```c
void _Py_Dealloc(PyObject *op)
{
    // 1. 获取类型的析构函数
    destructor dealloc = Py_TYPE(op)->tp_dealloc;
    
    // 2. 调用析构函数（如果有）
    if (dealloc != NULL) {
        dealloc(op);
    }
}
```

### 完整生命周期示例

```python
# 1. 创建，引用计数=1
a = [1, 2, 3]

# 2. 新增引用，计数=2
b = a

# 3. 删除一个引用，计数=1
del b

# 4. 删除最后一个引用，计数=0，对象销毁
del a
```

在 C 层面，这个过程对应着：

```
创建：PyLong_FromLong() → ob_refcnt = 1
新增：Py_INCREF() → ob_refcnt = 2
删除：Py_DECREF() → ob_refcnt = 1
销毁：Py_DECREF() → ob_refcnt = 0 → _Py_Dealloc()
```

---

## 💡 实战：跟踪对象生命周期

让我们用 `weakref` 和自定义类来观察对象的生命周期：

```python
import weakref
import sys

class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"[{self.name}] 对象创建")
    
    def __del__(self):
        print(f"[{self.name}] 对象销毁")

# 创建对象
obj = MyClass("测试")
print(f"引用计数：{sys.getrefcount(obj) - 1}")  # 减 1 排除 getrefcount 参数

# 创建弱引用（不增加引用计数）
weak_ref = weakref.ref(obj, lambda ref: print("弱引用回调：对象已死亡"))

# 新增引用
another_ref = obj
print(f"引用计数：{sys.getrefcount(obj) - 1}")

# 删除引用
del another_ref
print(f"引用计数：{sys.getrefcount(obj) - 1}")

# 删除最后一个引用，触发销毁
del obj
# 输出：[测试] 对象销毁
# 输出：弱引用回调：对象已死亡
```

这个实验展示了：
1. 对象创建和销毁的时机
2. 弱引用不增加引用计数
3. `__del__` 方法在对象销毁时被调用

---

## ⚠️ 引用计数的陷阱

### 循环引用问题

```python
# 循环引用示例
a = {}
b = {}
a['other'] = b  # a 引用 b
b['other'] = a  # b 引用 a

# 此时即使删除 a 和 b，引用计数都不为 0
del a
del b
# 内存泄漏！对象无法被回收
```

这就是需要垃圾回收（GC）的原因，我们将在第 4 讲详细讨论。

### 引用计数泄漏

```python
# 错误示例：C 扩展中忘记 DECREF
void bad_function() {
    PyObject *obj = PyLong_FromLong(100);
    # ... 使用 obj ...
    # 忘记 Py_DECREF(obj)
    # 导致内存泄漏
}
```

在编写 C 扩展时，必须小心管理引用计数。每个 `Py_INCREF` 都应有对应的 `Py_DECREF`。

### 提前释放问题

```c
// 错误示例：提前释放导致悬空指针
Py_DECREF(obj);
# ... 其他代码 ...
Py_INCREF(obj);  # 危险！obj 可能已被销毁
```

---

## 🎯 本讲总结

通过本讲，我们深入理解了：

**PyObject 结构体**：所有 Python 对象的统一基类，包含引用计数和类型指针两个核心字段。

**引用计数机制**：Python 主要的内存管理方式，通过自动增减计数器来跟踪对象的使用情况。

**类型对象系统**：`type`和`object` 的关系，类型本身也是对象，形成自举系统。

**对象生命周期**：从创建到销毁的完整流程，包括缓存检查、内存分配、初始化、销毁等步骤。

**实际陷阱**：循环引用、引用计数泄漏等问题，需要垃圾回收机制来补充。

这些知识是理解后续内存管理、垃圾回收等内容的基础。

---

## 📚 推荐教材

**[《Python 编程从入门到实践（第 3 版）》](https://u.jd.com/NGMHz3T)** - Eric Matthes 著

Python 零基础入门首选。本书分为基础语法和项目实战两部分，适合完全没有编程经验的读者。学完可掌握 Python 基础，为后续进阶打下坚实基础。

**[《流畅的 Python（第 2 版）》](https://u.jd.com/NOMBOOz)** - Luciano Ramalho 著

Python 进阶经典之作。深入讲解 Python 的高级特性，包括数据模型、函数式编程、面向对象、元编程等。建议在掌握基础后阅读，为学习 CPython 源码做好准备。

**[《CPython 设计与实现》](https://u.jd.com/NaM5rNE)** - Anthony Shaw 著

本书深入讲解 CPython 内部机制，从内存管理到字节码执行，从对象模型到并发编程。配合本课程学习，效果更佳。

**学习路线建议：**
```
零基础 → 《从入门到实践》 → 《流畅的 Python》 → 本门课程 → 《CPython 设计与实现》
```

---

## 🔗 课程导航

← [上一讲：CPython 概览与源码编译](01-CPython-概览.md) | [下一讲：内存管理机制](03-内存管理基础.md) →

---

## 💬 联系我

| 平台 | 账号/链接 |
|------|----------|
| 微信 | [扫码加好友](https://www.python4office.cn/wechat-qrcode/) |
| 微博 | [@程序员晚枫](https://weibo.com/u/7726957925) |
| 知乎 | [@程序员晚枫](https://www.zhihu.com/people/CoderWanFeng) |
| 抖音 | [@程序员晚枫](https://www.douyin.com/user/MS4wLjABAAAA259649365) |
| 小红书 | [@程序员晚枫](https://xhslink.com/m/4i8OhkfTvW3) |
| B 站 | [Python 自动化办公社区](https://space.bilibili.com/259649365) |

**主营业务**：AI 编程培训、企业内训、技术咨询
