---
title: 深入解析 Python `__slots__`：内存优化与性能提升的利器
date: 2025-08-21 00:41:49
tags: [python,下载]
---




## 引言

在 Python 的世界里，“灵活性”是其核心哲学之一。默认情况下，Python 对象的实例属性都存储在一个动态的字典 `__dict__` 中，这使得我们可以随时随地、随心所欲地为对象添加新的属性。然而，这种灵活性并非没有代价，它带来了显著的内存开销和相对缓慢的属性访问速度。

当你需要创建成千上万个对象实例时（例如在科学计算、Web 框架处理大量请求、游戏开发中处理大量实体时），这种开销就会变得不可忽视。这时，`__slots__` 这个强大的魔术方法就派上了用场。它通过一种声明式的机制，在灵活性和性能之间提供了一个高效的权衡。

本文将深入探讨 `__slots__` 的工作原理、使用方法、性能优势以及需要注意的陷阱。

## 一、 `__slots__` 是什么？

`__slots__` 是一个类变量，它允许开发者显式地声明一个类所允许拥有的实例属性名称。其语法非常简单：

```python
class MyClass:
    __slots__ = ('attr1', 'attr2', 'attr3')
    # ... 类的其他定义 ...
```

通过这行声明，你告诉 Python 解释器：`MyClass` 的实例**只能**拥有 `attr1`, `attr2`, `attr3` 这三个属性。解释器会据此进行内存分配和属性访问管理，而不是使用默认的 `__dict__` 字典。

## 二、 默认行为 vs. `__slots__` 行为

### 1. 默认行为：基于 `__dict__` 的动态属性

在没有 `__slots__` 的普通类中，每个实例都拥有一个 `__dict__` 字典来存储其所有属性。

```python
class RegularUser:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

user1 = RegularUser('Alice', 1)
user1.email = 'alice@example.com' # 动态添加新属性，完全合法
print(user1.__dict__)
# 输出: {'name': 'Alice', 'user_id': 1, 'email': 'alice@example.com'}
```

**优点**：极高的灵活性。
**缺点**：
*   **内存开销大**：字典本身就需要占用不小的内存，尤其是当实例属性很少时，字典的开销占比会很高。
*   **访问速度慢**：属性访问需要在哈希表（字典）中进行查找，虽然平均时间复杂度是 O(1)，但比直接访问固定偏移量的内存要慢。

### 2. `__slots__` 行为：基于描述符的固定属性

使用 `__slots__` 后，Python 不再为每个实例创建 `__dict__`，而是为整个类创建一个**描述符** (Descriptor)，并为每个实例在 C 层分配一个固定的、紧凑的数组来存储 `__slots__` 中声明的属性。

```python
class SlotsUser:
    __slots__ = ('name', 'user_id') # 显式声明允许的属性

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

user2 = SlotsUser('Bob', 2)
print(user2.name) # 正常工作
# user2.email = 'bob@example.com' # AttributeError: 'SlotsUser' object has no attribute 'email'
# print(user2.__dict__) # AttributeError: 'SlotsUser' object has no attribute '__dict__'
```

**优点**：
*   **内存占用小**：实例不再需要维护一个字典，内存布局是固定的，极大减少了内存消耗。
*   **属性访问更快**：属性访问被转换为对那个固定数组的索引操作，速度更快。
**缺点**：
*   **失去灵活性**：无法动态添加未在 `__slots__` 中声明的属性。
*   **某些工具依赖 `__dict__`**：一些序列化或调试工具可能依赖于 `__dict__` 的存在。

## 三、 内存节省背后的原理

内存节省主要来自两个方面：

1.  **移除了 `__dict__`**：一个空的字典在 64 位 Python 解释器下大约占用 240 字节。对于属性数量很少但实例数量极多的类（例如坐标点 `Point(x, y)`），节省的内存是巨量的。内存节省的不是属性值的空间，而是存储这些属性所用的**数据结构**的空间。

2.  **紧凑的内存布局**：Python 解释器会为 `__slots__` 的实例预分配一块连续的内存空间，每个属性在其中的偏移量是固定的。这比使用字典（需要存储哈希表、键和值指针等）要高效得多。

### 量化内存节省

让我们用一个简单的例子来量化这种节省：

```python
import sys

class PointRegular:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointSlots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 创建实例
p_reg = PointRegular(1, 2)
p_slot = PointSlots(1, 2)

print(f"Regular instance size: {sys.getsizeof(p_reg)} bytes")
print(f"Slots instance size: {sys.getsizeof(p_slot)} bytes")
```

输出可能会类似于（具体数字因Python版本和系统而异）：
```
Regular instance size: 56 bytes
Slots instance size: 48 bytes
```

单个实例节省了 8 字节。看起来不多？让我们放大规模：

```python
# 创建一百万个实例，估算总内存消耗
num_instances = 1_000_000
mem_regular = sys.getsizeof(p_reg) * num_instances
mem_slots = sys.getsizeof(p_slot) * num_instances

print(f"Estimated memory for 1,000,000 Regular instances: {mem_regular / 1024**2:.2f} MB")
print(f"Estimated memory for 1,000,000 Slots instances: {mem_slots / 1024**2:.2f} MB")
print(f"Memory saved: {(mem_regular - mem_slots) / 1024**2:.2f} MB")
```
输出可能类似于：
```
Estimated memory for 1,000,000 Regular instances: 53.41 MB
Estimated memory for 1,000,000 Slots instances: 45.78 MB
Memory saved: 7.63 MB
```
**节省了超过 7MB 的内存！** 对于属性更少的类，比例会更加惊人。

## 四、 如何使用 `__slots__`

### 1. 基础用法

```python
class Vector2D:
    __slots__ = ('_x', '_y') # 通常使用元组或列表

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
```

### 2. 继承中的使用

使用 `__slots__` 时，继承链需要小心处理。

*   **如果父类没有 `__slots__`**：子类使用 `__slots__` 后，实例仍然会有 `__dict__`（除非子类的 `__slots__` 也阻止了它），因为需要容纳父类的潜在动态属性。这会削弱 `__slots__` 的效果。
*   **如果父类有 `__slots__`**：子类也需要定义自己的 `__slots__`，它应该**包含**父类的 `__slots__`。

```python
class Base:
    __slots__ = ('base_attr',)

class Derived(Base):
    __slots__ = ('derived_attr',) # 不需要重复 base_attr

    def __init__(self):
        self.base_attr = "Base"
        self.derived_attr = "Derived"

d = Derived()
```

### 3. 支持弱引用

如果需要对你的类实例使用弱引用 (`weakref`)，你需要将 `'__weakref__'`  explicitly 加入到 `__slots__` 中。

```python
class WeakRefableSlots:
    __slots__ = ('data', '__weakref__')
    def __init__(self, data):
        self.data = data
```

## 五、 性能测试：内存与速度

除了内存，`__slots__` 还能提升属性访问速度。

```python
import timeit

class TestRegular:
    def __init__(self, x):
        self.x = x

class TestSlots:
    __slots__ = ('x',)
    def __init__(self, x):
        self.x = x

# 创建实例
reg_obj = TestRegular(5)
slot_obj = TestSlots(5)

# 测试属性访问速度
def get_attribute_reg():
    return reg_obj.x

def get_attribute_slot():
    return slot_obj.x

time_reg = timeit.timeit(get_attribute_reg, number=10_000_000)
time_slot = timeit.timeit(get_attribute_slot, number=10_000_000)

print(f"Regular attribute access (10M times): {time_reg:.3f} seconds")
print(f"Slots attribute access (10M times): {time_slot:.3f} seconds")
print(f"Speedup: {time_reg / time_slot:.2f}x")
```
输出可能显示 `__slots__` 的属性访问有 20%-40% 的速度提升。

## 六、 适用场景与注意事项

### 何时使用 `__slots__`？

1.  **内存敏感的应用**：当你需要创建大量（数万、数百万）实例时，它是必须考虑的优化手段。
2.  **属性固定的对象**：例如数据结构（树节点、链表节点、几何图形）、配置项、数据传输对象（DTO）、ORM 中的模型实例（虽然ORM框架通常会自己处理）。
3.  **需要极致性能的场景**：在紧密循环中频繁访问属性的代码。

### 注意事项与陷阱

1.  **不能动态添加属性**：这是最大的限制。确保你的类在设计阶段就能确定所有需要的属性。
2.  **与部分库和工具的兼容性**：一些序列化库（如 `pickle`）可以正常工作，但某些深度依赖 `__dict__` 或 `__dir__` 的库或调试工具可能会出现问题。
3.  **继承链的复杂性**：如前所述，在复杂的继承关系中需要小心管理 `__slots__`。
4.  **不要滥用**：如果你的类只会创建几个实例，或者确实需要动态属性，那么使用 `__slots__` 是自找麻烦。**“明确优于隐晦”，只在真正需要时使用。**

## 结论

`__slots__` 是 Python 提供给开发者的一个强大工具，它在牺牲一部分动态灵活性的前提下，换来了显著的内存节省和一定的性能提升。它完美体现了 Python “实用主义” 的哲学：提供机制，让开发者根据实际情况决定策略。

在开发大型应用、处理海量数据或编写底层基础构件时，善用 `__slots__` 可以有效地优化程序资源消耗。然而，就像所有优化技巧一样，它的首要原则是 **“不要过早优化”** 。首先保证代码的正确性和清晰度，然后在性能分析工具的指导下，有针对性地使用 `__slots__` 来解决实际存在的内存或性能瓶颈。

## 入门课程 + 读者群

- 加入学习👉[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)

大家学习 或 使用代码过程中，有任何问题，都可以加入读者群交流哟~👇


![](https://cos.python-office.com/group/0816.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)就能上手做AI项目。