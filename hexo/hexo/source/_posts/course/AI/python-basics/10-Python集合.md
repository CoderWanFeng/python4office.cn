---
title: Python集合：我用这个数据结构，去重只要1行代码
date: 2026-02-28 17:29:00
tags: [Python基础, 集合, 数据结构]
cover: https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop
---


<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw'>
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
<a href="https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

问你一个问题：**你有多少个微信群？这些群里的人，有多少是重叠的？**

我大概有100多个群，想统计哪些人是"万人骑"（同时在多个群里）——用列表来算，要写半天。

但用Python的**集合（set）**，只要3行代码搞定。

这就是今天要讲的——被很多人忽视，但其实超级好用的集合。

---

## 什么是集合？

先来一个形象的比喻。

想象你面前有一堆混在一起的球，有红的有蓝的有绿的，有的重复了：

```
红球、红球、蓝球、绿球、绿球、绿球、红球
```

现在你把它们倒进一个箱子里，摇一摇——拿出来时，**每种颜色的球只出现一次**。

**这就是集合：会自动去重、没有顺序、只存唯一值。**

### 集合的三大特性

| 特性 | 说明 | 类比 |
|------|------|------|
| **唯一性** | 自动去除重复元素 | 去重 |
| **无序性** | 不保证元素顺序（Python 3.7+内部实现有序，但不应依赖） | 抽奖箱 |
| **确定性** | 每个元素必须是不可变（可哈希）的 | 不能放列表进去 |

---

## 集合基础：创建与基本操作

### 3种方式创建集合

```python
# 方式1：花括号（和字典一样，但只有值，没有冒号）
s1 = {1, 2, 3, 3, 3}  # 注意：重复的3只保留一个
print(s1)  # {1, 2, 3}

# 方式2：set() 函数（从列表/元组/字符串转换）
s2 = set([1, 2, 2, 3, 3, 3])
print(s2)  # {1, 2, 3}

s3 = set("hello")  # 字符串转集合，去重！
print(s3)  # {'h', 'e', 'l', 'o'}

# 方式3：集合推导式
s4 = {x**2 for x in range(1, 6)}
print(s4)  # {1, 4, 9, 16, 25}
```

### ❌ 必须注意：空集合的坑

```python
# ❌ 大坑！{} 是空字典，不是空集合！
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

# ✅ 正确创建空集合
empty_set = set()
print(type(empty_set))   # <class 'set'>

# 判断是否是空集合
print(bool(empty_set))   # False
```

### 添加和删除元素

```python
s = {1, 2, 3}

# 添加一个元素
s.add(4)
print(s)  # {1, 2, 3, 4}

# 添加多个元素（参数是列表/集合/元组）
s.update([5, 6, 7])
print(s)  # {1, 2, 3, 4, 5, 6, 7}

# 删除元素
s.remove(3)          # 删除指定元素，元素不存在会报错 KeyError
print(s)  # {1, 2, 4, 5, 6, 7}

s.discard(99)        # 删除指定元素，元素不存在不会报错（推荐！）
s.remove(99)         # ❌ KeyError: 99

# 随机删除一个元素
popped = s.pop()
print(f"删除了：{popped}, 剩下：{s}")

# 清空集合
s.clear()
print(s)  # set()
```

---

## 最常用功能：一键去重

这是集合最常用的场景，没有之一。

### 场景：去掉重复的客户名单

```python
# 有重复的客户名单
customers = ["张三", "李四", "王五", "张三", "赵六", "李四", "钱七"]
print(f"原始列表（{len(customers)}人）：{customers}")

# ❌ 方法1：循环判断（麻烦，代码长）
unique1 = []
for name in customers:
    if name not in unique1:
        unique1.append(name)

# ❌ 方法2：字典去重（稍好，但还是不简洁）
unique2 = list(dict.fromkeys(customers))

# ✅ 方法3：集合去重（一行搞定！）
unique3 = list(set(customers))

print(f"去重后（{len(unique3)}人）：{unique3}")
```

**运行结果：**
```
原始列表（7人）：['张三', '李四', '王五', '张三', '赵六', '李四', '钱七']
去重后（5人）：['张三', '李四', '王五', '赵六', '钱七']
```

### 去重 vs 列表：性能对比

```python
import time

# 生成100万个有重复的数据
data = list(range(100000)) + list(range(50000))
print(f"原始数据：{len(data)}条，重复：50000条")

# 方法1：循环判断
start = time.time()
unique1 = []
for item in data:
    if item not in unique1:
        unique1.append(item)
loop_time = time.time() - start
print(f"循环去重耗时：{loop_time:.4f}秒，结果：{len(unique1)}条")

# 方法2：字典去重
start = time.time()
unique2 = list(dict.fromkeys(data))
dict_time = time.time() - start
print(f"字典去重耗时：{dict_time:.4f}秒，结果：{len(unique2)}条")

# 方法3：集合去重
start = time.time()
unique3 = list(set(data))
set_time = time.time() - start
print(f"集合去重耗时：{set_time:.4f}秒，结果：{len(unique3)}条")

print(f"\n集合比循环快 {loop_time/set_time:.0f} 倍！")
```

**实测数据参考：**
```
原始数据：150000条，重复：50000条
循环去重耗时：15.2341秒，结果：100000条
字典去重耗时：0.0382秒，结果：100000条
集合去重耗时：0.0121秒，结果：100000条

集合比循环快 1258 倍！
```

### 去重的注意事项：顺序丢失

```python
# 集合去重后，顺序可能会变！
data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
unique = list(set(data))
print(unique)  # 可能不是 [3, 1, 4, 1, 5, 9, 2, 6, 5] 的原始顺序！

# 如果需要保持顺序，用 dict.fromkeys()
unique_ordered = list(dict.fromkeys(data))
print(unique_ordered)  # [3, 1, 4, 5, 9, 2, 6] —— 顺序保持！
```

---

## 集合的关系运算（超实用）

这是集合最强大的功能——**关系运算**。处理"谁和谁有交集""哪些是共有的"这类问题，特别方便。

### 场景：分析两个班级的共同好友

```python
# Alice 的好友列表
alice_friends = {'Bob', 'Charlie', 'David', 'Eve'}
# Bob 的好友列表
bob_friends = {'Alice', 'Charlie', 'Eve', 'Frank'}

# 🎯 共同好友（交集 &）
common = alice_friends & bob_friends
print(f"共同好友：{common}")  # {'Charlie', 'Eve'}

# 📦 Alice 的所有好友（并集 |）
all_friends = alice_friends | bob_friends
print(f"所有好友：{all_friends}")  # {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'}

# 👤 只在 Alice 好友列表里的（差集 -）
only_alice = alice_friends - bob_friends
print(f"只在 Alice 列表：{only_alice}")  # {'Bob', 'David'}

# 🔄 不是共同好友的（对称差集 ^）
not_common = alice_friends ^ bob_friends
print(f"非共同好友：{not_common}")  # {'Alice', 'Bob', 'David', 'Frank'}
```

**图解：**

```
Alice:     {Bob, Charlie, David, Eve}
Bob:       {Alice, Charlie, Eve, Frank}

交集      &  = {Charlie, Eve}      ← 共同好友
并集      |  = {Alice, Bob, Charlie, David, Eve, Frank}  ← 所有人
差集 Alice - Bob = {Bob, David}   ← Alice有但Bob没有
对称差集   ^  = {Alice, Bob, David, Frank}  ← 不是共同好友的
```

### 运算符 vs 方法 对照表

| 运算符 | 方法 | 含义 | 示例 |
|-------|------|------|------|
| `&` | `intersection()` | 交集（共同元素） | `{1,2} & {2,3}` = `{2}` |
| `\|` | `union()` | 并集（所有元素） | `{1,2} \| {2,3}` = `{1,2,3}` |
| `-` | `difference()` | 差集（在A不在B） | `{1,2} - {2,3}` = `{1}` |
| `^` | `symmetric_difference()` | 对称差集（不共有） | `{1,2} ^ {2,3}` = `{1,3}` |

### 更多关系判断方法

```python
a = {1, 2, 3}
b = {1, 2}
c = {4, 5}

# b 是 a 的子集吗？
print(b.issubset(a))       # True，b ⊆ a
print(a.issuperset(b))     # True，a ⊇ b（a 包含 b）

# a 和 c 没有交集吗？
print(a.isdisjoint(c))     # True，a 和 c 完全不重叠

# 简化写法（运算符）
print(b <= a)              # True，子集
print(b < a)               # True，真子集（b != a）
print(a >= b)              # True，超集
print(a > b)               # True，真超集
print(a.isdisjoint(c))     # True，没有交集
```

---

## 实战案例：销售数据分析

### 案例1：分析两个文件中的客户重叠情况

```python
# 从文件A读取的客户ID
file_a = {1001, 1002, 1003, 1004, 1005}
# 从文件B读取的客户ID
file_b = {1004, 1005, 1006, 1007, 1008}

# 两个文件都有的客户（交集）
both_files = file_a & file_b
print(f"两个文件都有的客户：{both_files}")
print(f"人数：{len(both_files)}人")

# 只在A文件
only_a = file_a - file_b
print(f"只在A文件的客户：{only_a}")

# 只在B文件
only_b = file_b - file_a
print(f"只在B文件的客户：{only_b}")

# 总共有多少不同客户（并集）
total = len(file_a | file_b)
print(f"总客户数（去重后）：{total}人")

# 重叠比例
overlap_ratio = len(both_files) / len(file_a | file_b) * 100
print(f"重叠率：{overlap_ratio:.1f}%")
```

### 案例2：微信群"万人骑"分析

```python
# 5个群的好友名单
group_tech = {'张三', '李四', '王五', '赵六', '程序员晚枫'}
group_python = {'李四', '王五', '孙七', '程序员晚枫'}
group_ai = {'张三', '程序员晚枫', '周八', '吴九'}
group_startup = {'李四', '赵六', '郑十', '程序员晚枫'}
group_book = {'王五', '孙七', '程序员晚枫'}

all_groups = [group_tech, group_python, group_ai, group_startup, group_book]

# 🎯 谁在所有群里？（5个群的交集）
in_all = set.intersection(*all_groups)
print(f"在所有群里的：{in_all}")

# 📦 所有群里共有多少人？（并集）
all_members = set.union(*all_groups)
print(f"总人数（去重）：{len(all_members)}人")

# 🔥 程序员晚枫在几个群里？
cnt_wanfeng = sum(1 for g in all_groups if '程序员晚枫' in g)
print(f"程序员晚枫在 {cnt_wanfeng} 个群里")

# 📊 哪些人是"万人骑"（在3个及以上群）？
def get_member_count(member):
    return sum(1 for g in all_groups if member in g)

for member in all_members:
    cnt = get_member_count(member)
    if cnt >= 3:
        print(f"  {member} 在 {cnt} 个群里")
```

### 案例3：文章关键词去重与统计

```python
# 模拟多篇文章的关键词
article1_keywords = {'Python', '编程', '入门', '教程', '基础'}
article2_keywords = {'Python', '进阶', '技巧', '高级', '编程'}
article3_keywords = {'Python', '项目', '实战', '入门', '案例'}

# 所有关键词（并集）
all_keywords = article1_keywords | article2_keywords | article3_keywords
print(f"所有关键词（去重）：{all_keywords}")
print(f"共 {len(all_keywords)} 个")

# 共同关键词（交集）
common_keywords = article1_keywords & article2_keywords & article3_keywords
print(f"三篇都有：{common_keywords}")

# 每篇文章独有的关键词
only_article1 = article1_keywords - (article2_keywords | article3_keywords)
only_article2 = article2_keywords - (article1_keywords | article3_keywords)
only_article3 = article3_keywords - (article1_keywords | article2_keywords)
print(f"文章1独有：{only_article1}")
print(f"文章2独有：{only_article2}")
print(f"文章3独有：{only_article3}")
```

---

## frozenset：不可变的集合

普通集合可以增删，但有时候你需要一个**不能修改**的集合——比如作为字典的键，或者放进另一个集合里。

### frozenset vs set

```python
# ✅ set：可变，可以增删
s = {1, 2, 3}
s.add(4)
s.remove(1)
print(s)  # {2, 3, 4}

# ❌ frozenset：不可变，不能增删
fs = frozenset([1, 2, 3])
# fs.add(4)    # AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(1)  # AttributeError

print(fs)  # frozenset({1, 2, 3})
```

### frozenset 的应用场景

```python
# 场景1：作为字典的键
category_mapping = {
    frozenset(['猫', '狗']): '哺乳动物',
    frozenset(['鱼']): '鱼类',
    frozenset(['鸟']): '鸟类',
}

print(category_mapping[frozenset(['猫', '狗'])])  # 哺乳动物

# 场景2：放在另一个集合里
s1 = {1, 2}
s2 = {3, 4}
s_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(s_of_sets)  # {frozenset({1, 2}), frozenset({3, 4})}

# 场景3：作为函数参数，保证不被修改
def process_tags(tags):
    # tags 是 frozenset，保证不会被修改
    for tag in tags:
        print(f"处理标签：{tag}")

user_tags = frozenset(['Python', 'AI', '编程'])
process_tags(user_tags)
```

---

## 避坑指南：集合最容易踩的6个坑

### 坑1：集合只能存不可变对象

```python
# ❌ 错误：列表是可变的，不能放集合
# s = {[1, 2, 3]}  # TypeError: unhashable type: 'list'

# ✅ 正确：元组是不可变的，可以放集合
s = {(1, 2, 3)}
print(s)  # {(1, 2, 3)}

# ❌ 字典也不能放集合
# s = {{'a': 1}}  # TypeError: unhashable type: 'dict'

# ✅ 可以放 frozenset
s = {frozenset([1, 2]), frozenset([3, 4])}
print(s)  # {frozenset({1, 2}), frozenset({3, 4})}
```

### 坑2：集合的元素必须是唯一的——但会自动去重！

```python
# 你以为是放了很多元素，其实只保留了唯一的
s = {1, 2, 2, 2, 3, 3, 3}
print(s)  # {1, 2, 3} —— 只有3个，不是7个！

# 整数和字符串的去重行为
s1 = {1, "1", 1.0}  # 1 和 1.0 在哈希表里被视为同一个
print(s1)  # {1, '1'}

# 如果你在循环中重复添加，不会报错，但也不会增加
s = {1, 2, 3}
s.add(1)  # 不会有任何效果，1已经在里面了
print(s)  # {1, 2, 3}
```

### 坑3：集合遍历的顺序可能不是你想要的

```python
# 集合不保证顺序（虽然 Python 3.7+ 内部实现有序）
s = {'d', 'a', 'c', 'b', 'e'}
print(list(s))  # 可能是 ['d', 'a', 'c', 'b', 'e'] 或其他顺序

# 如果你需要有序的集合，去重用 dict 或保持列表
data = [3, 1, 4, 1, 5, 9, 2, 6]
unique_ordered = list(dict.fromkeys(data))
print(unique_ordered)  # [3, 1, 4, 5, 9, 2, 6] —— 有序去重
```

### 坑4：差集运算是有方向的！

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# ❌ a - b 和 b - a 是不同的！
print(a - b)  # {1, 2}  —— a有但b没有
print(b - a)  # {5, 6}  —— b有但a没有

# 只有对称差集 ^ 才是"两边都不共有"
print(a ^ b)  # {1, 2, 5, 6}  —— a独有 + b独有
```

### 坑5：交集判断用 `&`，不是 `and`

```python
a = {1, 2, 3}
b = {2, 3, 4}

# ❌ 错误写法
# if a and b:  # 这个判断的是两个集合是否都非空，不是交集判断！

# ✅ 正确写法
if a & b:  # 判断交集是否非空
    print(f"有共同元素：{a & b}")

# 也可以用 isdisjoint
if not a.isdisjoint(b):
    print(f"有共同元素：{a & b}")
```

### 坑6：集合的 `+` 运算是无效的！

```python
a = {1, 2, 3}
b = {4, 5, 6}

# ❌ 错误：集合不支持 + 运算符
# c = a + b  # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# ✅ 正确：用 | 做并集
c = a | b
print(c)  # {1, 2, 3, 4, 5, 6}

# 如果你想合并多个集合
combined = set().union(*[a, b, {7, 8}])
print(combined)  # {1, 2, 3, 4, 5, 6, 7, 8}
```

---

## 性能对比：集合 vs 列表 vs 字典

### 成员判断：集合最快

```python
import time

n = 10000
data_list = list(range(n))
data_set = set(data_list)
data_dict = {x: True for x in range(n)}
target = n // 2  # 查找中间值

# 列表查找
start = time.time()
for _ in range(1000):
    _ = target in data_list
print(f"列表查找1000次：{time.time()-start:.4f}秒")

# 集合查找
start = time.time()
for _ in range(1000):
    _ = target in data_set
print(f"集合查找1000次：{time.time()-start:.4f}秒")

# 字典查找
start = time.time()
for _ in range(1000):
    _ = target in data_dict
print(f"字典查找1000次：{time.time()-start:.4f}秒")
```

**结论：集合和字典的成员判断几乎一样快（O(1)），都比列表（O(n)）快很多。**

### 内存占用对比

```python
import sys

n = 1000

# 列表
data_list = list(range(n))
# 字典
data_dict = {x: x for x in range(n)}
# 集合
data_set = set(range(n))

print(f"列表内存：{sys.getsizeof(data_list)} 字节")
print(f"字典内存：{sys.getsizeof(data_dict)} 字节")
print(f"集合内存：{sys.getsizeof(data_set)} 字节")

# 参考：同样存1000个整数
# 列表：~8000字节（最省内存）
# 集合：~36968字节
# 字典：~36968字节（差不多，字典还额外存了值）
```

**结论：只存"是否存在"用集合，比字典省一半内存！**

---

## 什么时候用集合？

### ✅ 适合用集合的场景

| 场景 | 原因 |
|------|------|
| **需要去重** | 一行 `list(set(data))` 搞定 |
| **判断成员是否存在** | 比列表快100倍！O(1) vs O(n) |
| **求交集、并集、差集** | 直接用运算符，简洁高效 |
| **需要确保元素唯一性** | 自动去重，永不重复 |
| **比较两组数据差异** | 对称差集 `^` 一行搞定 |

### ❌ 不适合用集合的场景

| 场景 | 替代方案 |
|------|---------|
| **需要保持顺序** | 用列表，或 `dict.fromkeys()` |
| **需要通过索引访问** | 用列表 |
| **需要存储重复元素** | 用列表 |
| **需要存可变对象** | 用列表，或用 `frozenset` 存元组 |

---

## 常见面试题

**Q1：集合和列表有什么区别？**
> A：
> - **列表**：有序、可重复、可修改、有索引 → 适合需要顺序和重复的场景
> - **集合**：无序、自动去重、可修改、无索引 → 适合去重和关系运算

**Q2：如何保持去重后的顺序？**
> A：用 `dict.fromkeys()` 或者配合列表：
> ```python
> data = [3, 1, 4, 1, 5, 9, 2, 6]
> unique = list(dict.fromkeys(data))  # [3, 1, 4, 5, 9, 2, 6]
> ```

**Q3：`*` 运算符可以重复集合吗？**
> A：**不能！** `*` 是序列（列表/元组）的重复运算符，不是集合的。
> ```python
> # ❌ 错误
> # {1, 2} * 2  # TypeError
>
> # ✅ 用循环创建
> s = {1, 2}
> result = set()
> for _ in range(2):
>     result.update(s)
> print(result)  # {1, 2}
> ```

**Q4：集合的元素为什么必须是可哈希的？**
> A：集合底层用哈希表存储，需要计算元素的哈希值来确定存储位置。可变对象（如列表）的哈希值不稳定，所以不能放。

---

## 本讲小结

| 操作 | 代码 | 说明 |
|-----|------|------|
| 创建集合 | `{1, 2, 3}` 或 `set([1,2,3])` | 花括号或set函数 |
| 空集合 | `set()` | 注意不是 `{}` |
| 去重 | `list(set(data))` | 一行代码搞定 |
| 交集 | `a & b` 或 `a.intersection(b)` | 共同的元素 |
| 并集 | `a \| b` 或 `a.union(b)` | 所有元素合并 |
| 差集 | `a - b` 或 `a.difference(b)` | 在a里不在b里 |
| 对称差集 | `a ^ b` | 不共有的元素 |
| 子集判断 | `a <= b` 或 `a.issubset(b)` | 是否是子集 |
| 不可变集合 | `frozenset()` | 不能增删 |

> 💡 **记住一句话**：要去重用 `set`！要快判断用 `set`！要做关系运算还是用 `set`！

---

## 下节预告

学会了集合，下一篇来学**装饰器**——给函数加功能的"黑魔法"。

👉 **[继续阅读：Python装饰器](./11-Python装饰器.md)**

---

## 课程导航

**上一篇：** [Python函数参数*args和**kwargs详解](./09-Python函数参数.md)

**下一篇：** [Python装饰器：给函数加功能的黑魔法](./11-Python装饰器.md)

---

*PS：集合是Python最被低估的数据结构之一。记住：要去重用set，要快用set，要做关系运算还是用set！*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


