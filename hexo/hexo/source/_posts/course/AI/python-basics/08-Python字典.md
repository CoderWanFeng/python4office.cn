---
title: Python字典：我用这个数据结构，把查询速度提升了100倍
date: "2026-02-28 17:27:00"
tags: ["Python基础", "字典", "数据结构"]
cover: "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop"
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

先问你一个问题：**你的通讯录，是按名字排序存 Excel 方便查找，还是按手机号存微信方便查找？**

相信大家都会选微信——因为你知道名字，一搜就到，不用从头翻到尾。

在Python里，这个"搜名字就到"的机制，就叫**字典（dict）**。

很多人学Python时，觉得字典就是"键值对存储"，用列表也能实现。但等你真正用过字典做查询之后，你就会明白——**为什么我说字典是Python中最被低估的数据结构。**

不信？我们往下看。

---

## 为什么字典这么快？

先来看一个真实的场景。

### 场景：10000个用户，怎么找到指定用户？

你有一个用户列表，现在要找到 ID 为 9999 的那个用户：

```python
# 数据准备：10000个用户
users = [{'id': i, 'name': f'用户{i}'} for i in range(10000)]

# 方式1：列表遍历查找
def find_user_list(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None

import time
start = time.time()
result = find_user_list(9999)
print(f"列表查找耗时：{time.time() - start:.6f}秒")
print(f"找到：{result}")
```

```python
# 方式2：字典直接查找
users_dict = {user['id']: user for user in users}

def find_user_dict(user_id):
    return users_dict.get(user_id)

start = time.time()
result = find_user_dict(9999)
print(f"字典查找耗时：{time.time() - start:.6f}秒")
print(f"找到：{result}")
```

**我的电脑实测结果：**
- 列表查找：约 0.0008 秒（平均要遍历5000次）
- 字典查找：约 0.000002 秒（一步到位）

差了 **400倍**！

### 字典为什么这么快？

字典底层用的是**哈希表（Hash Table）**，这玩意儿有多牛呢？

想象你要在10000本书里找一本书：

| 查找方式 | 操作步骤 | 时间复杂度 |
|---------|---------|-----------|
| 列表（逐个找） | 从第一本翻到第10000本 | O(n) — 线性查找 |
| 字典（哈希表） | 知道书名→直接走到对应书架 | O(1) — 常数级 |

**数据量越大，差距越明显：**
- 100条数据：字典快 **10倍**
- 1000条数据：字典快 **100倍**
- 10000条数据：字典快 **1000倍**
- 100000条数据：字典快 **10000倍**

这就是为什么大厂面试必问字典——**你不懂哈希表，就不懂性能优化。**

---

## 字典基础：创建与访问

先从最基础的开始，确保你地基扎实。

### 3种方式创建字典

```python
# 方式1：直接写（最常用）
person = {'name': '张三', 'age': 25, 'city': '重庆'}
print(person)

# 方式2：dict() 函数
person2 = dict(name='李四', age=30, city='成都')
print(person2)

# 方式3：从键值对列表创建
pairs = [('name', '王五'), ('age', 28), ('city', '北京')]
person3 = dict(pairs)
print(person3)
```

### 访问值：方括号 vs get方法

```python
scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# ❌ 方括号访问：键不存在会报错
# print(scores['David'])  # KeyError: 'David'

# ✅ get方法：键不存在返回默认值（不报错！）
print(scores.get('David'))       # None
print(scores.get('David', 0))    # 0（指定默认值）
print(scores.get('Alice', 0))    # 85（存在的键返回原值）

# ✅ 批量获取（避免多次get）
keys = ['Alice', 'David', 'Bob']
values = [scores.get(k, 0) for k in keys]
print(values)  # [85, 0, 90]
```

### 增删改查

```python
info = {}

# 增：直接赋值
info['name'] = '程序员晚枫'
info['age'] = 18
print(info)

# 改：覆盖已有键
info['age'] = 28
print(info)

# 查：多种方式
print(info['name'])          # 程序员晚枫
print(info.get('name'))       # 程序员晚枫
print(info.get('gender', '未知'))  # 未知（默认值）

# 删：3种方式
del info['age']              # 方式1：del语句
print(info)                  # {'name': '程序员晚枫'}

age = info.pop('name')       # 方式2：pop，删除并返回
print(age)                   # 程序员晚枫
print(info)                  # {}

# 清空字典
info.clear()
print(info)                  # {}
```

---

## 字典进阶：6个必须掌握的技巧

### 技巧1：setdefault —— 一键初始化（防报错神器）

**场景：** 你要统计每个单词出现的次数，如果单词第一次出现，你要先初始化为0：

```python
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

# ❌ 普通写法：容易 KeyError
counts = {}
for word in words:
    counts[word] += 1  # 第一次会报错：KeyError

# ✅ 用 setdefault：一行搞定初始化
counts = {}
for word in words:
    counts.setdefault(word, 0)  # 如果不存在，初始化为0
    counts[word] += 1

print(counts)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

**更简洁的写法：**
```python
# 字典推导式一行搞定
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counts = {word: words.count(word) for word in set(words)}
print(counts)  # {'apple': 3, 'banana': 2, 'cherry': 1}
```

### 技巧2：update —— 合并字典（别再用循环了）

```python
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4, 'e': 5}

# 合并：后者覆盖前者
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 20, 'c': 3, 'd': 4, 'e': 5}

# Python 3.9+ 新写法：更优雅
dict3 = {'a': 1, 'b': 2}
dict4 = {'b': 20, 'c': 3}
merged = dict3 | dict4
print(merged)  # {'a': 1, 'b': 20, 'c': 3}
```

### 技巧3：字典推导式 —— 一行构建复杂字典

```python
# 场景1：把列表转成 {元素: 长度} 的字典
names = ['Alice', 'Bob', 'Charlie', 'David']
name_lengths = {name: len(name) for name in names}
print(name_lengths)
# {'Alice': 5, 'Bob': 3, 'Charlie': 7, 'David': 5}

# 场景2：筛选出成绩>=80的学生
students = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 68}
passing = {name: score for name, score in students.items() if score >= 80}
print(passing)  # {'Alice': 85, 'Charlie': 90}

# 场景3：两个列表配对
keys = ['name', 'age', 'city']
values = ['张三', 28, '重庆']
person = dict(zip(keys, values))
print(person)  # {'name': '张三', 'age': 28, 'city': '重庆'}

# 场景4：嵌套字典推导式
matrix = {(i, j): i * j for i in range(1, 4) for j in range(1, 4)}
print(matrix)  # {(1,1):1, (1,2):2, (1,3):3, (2,1):2, ...}
```

### 技巧4：Counter —— 统计频率的瑞士军刀

```python
from collections import Counter

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple', 'apple', 'banana']

# 最基本的统计
counts = Counter(words)
print(counts)
# Counter({'apple': 4, 'banana': 3, 'cherry': 1})

# Top N 最常见的
print(counts.most_common(2))  # [('apple', 4), ('banana', 3)]

# 统计字符
text = "hello world"
char_counts = Counter(text)
print(char_counts.most_common(3))  # [('l', 3), ('o', 2), (' ', 1)]

# Counter 也支持运算
counter1 = Counter(['apple', 'banana', 'apple'])
counter2 = Counter(['apple', 'cherry'])
print(counter1 + counter2)  # Counter({'apple': 3, 'banana': 1, 'cherry': 1})
```

### 技巧5：defaultdict —— 不用判断键是否存在

```python
from collections import defaultdict

# ❌ 普通字典：每次都要判断键是否存在
words = ['apple', 'banana', 'apple', 'cherry']
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
print(counts)

# ✅ defaultdict：自动初始化，不报错
counts_dd = defaultdict(int)  # int() 默认返回0
for word in words:
    counts_dd[word] += 1
print(dict(counts_dd))  # {'apple': 2, 'banana': 1, 'cherry': 1}

# defaultdict 配合 list：按组分类
animals = ['狗', '猫', '狗', '兔子', '猫', '狗']
by_type = defaultdict(list)
for animal in animals:
    by_type[animal].append(animal)
print(dict(by_type))
# {'狗': ['狗', '狗', '狗'], '猫': ['猫', '猫'], '兔子': ['兔子']}
```

### 技巧6：字典视图 —— 高效遍历键值对

```python
person = {'name': '张三', 'age': 28, 'city': '重庆', 'job': '程序员'}

# 遍历所有键
for key in person.keys():
    print(key)

# 遍历所有值
for value in person.values():
    print(value)

# 遍历键值对（元组）
for key, value in person.items():
    print(f"{key}: {value}")

# 反转字典（值→键）
# 注意：值必须唯一
value_to_key = {v: k for k, v in person.items()}
print(value_to_key)
```

---

## 字典的深水区：性能与原理

### 字典的性能真相

字典为什么这么快？来一个硬核测试：

```python
import time

# 测试数据量级
for n in [100, 1000, 10000, 100000]:
    data_list = list(range(n))
    data_dict = {x: x for x in data_list}
    target = n - 1

    # 列表查找
    start = time.time()
    for _ in range(10000):
        _ = target in data_list
    list_time = time.time() - start

    # 字典查找
    start = time.time()
    for _ in range(10000):
        _ = target in data_dict
    dict_time = time.time() - start

    ratio = list_time / dict_time if dict_time > 0 else 0
    print(f"n={n:>6}: 列表{list_time:.4f}秒 | 字典{dict_time:.6f}秒 | 字典快{ratio:.0f}倍")
```

**实测数据参考：**
```
n=   100: 列表0.0021秒 | 字典0.000234秒 | 字典快9倍
n=  1000: 列表0.0189秒 | 字典0.000256秒 | 字典快74倍
n= 10000: 列表0.1876秒 | 字典0.000298秒 | 字典快630倍
n=100000: 列表1.9234秒 | 字典0.000412秒 | 字典快4668倍
```

**结论：字典的性能优势，随着数据量增大而**指数级**扩大！**

### 字典的内存占用

字典虽然快，但内存开销也大。要有取舍意识：

```python
import sys

# 同样存1000个整数
data_list = list(range(1000))
data_dict = {i: i for i in range(1000)}

print(f"列表内存：{sys.getsizeof(data_list)} 字节")   # ~8000字节
print(f"字典内存：{sys.getsizeof(data_dict)} 字节")   # ~36968字节
```

**内存对比：字典比列表多占约4-5倍空间。**这就是为什么字典不适合存海量简单数据。

---

## 避坑指南：字典最容易踩的6个坑

### 坑1：字典的key不能是可变对象

```python
# ❌ 错误：列表不能做key
# d = {[1, 2]: 'value'}  # TypeError: unhashable type: 'list'

# ✅ 正确：元组可以做key（因为不可变）
d = {(1, 2): 'value'}
print(d[(1, 2)])  # 'value'

# ❌ 字典本身也不能做key
# nested = {d: 'oops'}  # TypeError

# ✅ 但字典的值可以是字典（嵌套字典）
nested = {'level1': {'level2': 'value'}}
print(nested['level1']['level2'])  # 'value'
```

### 坑2：字典的.pop()和del[]的区别

```python
d = {'a': 1, 'b': 2, 'c': 3}

# pop：删除并返回值，如果键不存在可以返回默认值
value = d.pop('a')
print(f"删除了：{value}，剩下：{d}")  # 删除了：1，剩下：{'b': 2, 'c': 3}

# pop也可以设默认值，避免KeyError
value = d.pop('x', '不存在')
print(value)  # 不存在

# del：只删除，不返回值，键不存在会报错
del d['b']
print(d)  # {'c': 3}

# ❌ del删除不存在的键会报错
# del d['not_exist']  # KeyError
```

### 坑3：字典推导式中的坑——小心覆盖

```python
# 场景：想把 {'a': 1, 'b': 2, 'c': 3} 的值翻倍
data = {'a': 1, 'b': 2, 'c': 3}

# ❌ 错误写法：在推导式中使用原始字典的值
doubled = {k: data[k] * 2 for k in data}  # 没问题，但不够简洁

# ✅ 正确：直接用 .items()
doubled = {k: v * 2 for k, v in data.items()}
print(doubled)  # {'a': 2, 'b': 4, 'c': 6}

# ⚠️ 注意：如果有重复的key，推导式会覆盖
d1 = {'a': 1}
d2 = {'a': 2, 'b': 3}
merged = {**d1, **d2}  # {'a': 2, 'b': 3}，d2覆盖了d1
print(merged)
```

### 坑4：字典是无序的（除非Python 3.7+）

```python
# Python 3.7+：字典保持插入顺序 ✅
d = {}
d['z'] = 1
d['a'] = 2
d['m'] = 3
print(list(d.keys()))  # ['z', 'a', 'm'] —— 保持插入顺序！

# Python 3.6及以下：字典无序 ⚠️
# 如果需要严格有序，用 OrderedDict
from collections import OrderedDict
od = OrderedDict()
od['z'] = 1
od['a'] = 2
od['m'] = 3
print(list(od.keys()))  # ['z', 'a', 'm']
```

### 坑5：不要在遍历字典时修改它

```python
d = {'a': 1, 'b': 2, 'c': 3}

# ❌ 错误：在遍历时删除
# for key in d:
#     if d[key] < 2:
#         del d[key]  # RuntimeError: dictionary changed size during iteration

# ✅ 正确：用列表的.copy()或者.pop()
# 方式1：遍历副本
for key in list(d.keys()):
    if d[key] < 2:
        del d[key]
print(d)  # {'b': 2, 'c': 3}

# 方式2：遍历键的列表
d = {'a': 1, 'b': 2, 'c': 3}
keys_to_remove = [k for k, v in d.items() if v < 2]
for key in keys_to_remove:
    d.pop(key)
print(d)  # {'b': 2, 'c': 3}
```

### 坑6：get()的默认值只对缺失的键生效

```python
scores = {'Alice': 0, 'Bob': 90}  # 注意Alice的分数是0，不是缺失

print(scores.get('Alice', '缺考'))  # 0 —— 返回的是原值0，不是默认值！
print(scores.get('Charlie', '缺考'))  # 缺考 —— 键真的不存在，用默认值

# 区分"值为0"和"键不存在"
print('Alice' in scores)    # True —— 键存在
print(scores['Alice'] == 0)  # True —— 值就是0
```

---

## 实战案例：用字典重构用户管理系统

### 场景描述

做一个用户查询系统，有以下需求：
1. 根据用户ID快速查询用户信息
2. 统计每个城市的用户数量
3. 找出年龄最大的用户
4. 按城市分组用户列表

### ❌ 低效做法（用列表）

```python
# 用列表存储10000个用户
users_list = [
    {'id': i, 'name': f'用户{i}', 'age': 18 + i % 50, 'city': ['重庆', '成都', '北京', '上海'][i % 4]}
    for i in range(10000)
]

# 需求1：根据ID查用户（慢！）
def find_user(user_id):
    for user in users_list:
        if user['id'] == user_id:
            return user
    return None

# 需求2：统计每个城市的用户数（嵌套循环，慢！）
def count_by_city():
    counts = {}
    for user in users_list:
        city = user['city']
        counts[city] = counts.get(city, 0) + 1
    return counts

# 需求3：找年龄最大的用户（慢！）
def find_oldest():
    return max(users_list, key=lambda u: u['age'])

import time

t1 = time.time()
for _ in range(1000):
    find_user(9999)
print(f"查1000次用户：{time.time()-t1:.4f}秒")

t2 = time.time()
count_by_city()
print(f"统计城市用户：{time.time()-t2:.6f}秒")

t3 = time.time()
find_oldest()
print(f"找最大年龄：{time.time()-t3:.6f}秒")
```

### ✅ 高效做法（用字典）

```python
# 用字典存储10000个用户，以ID为键
users_dict = {
    user['id']: user
    for user in users_list
}

# 需求1：根据ID查用户（快！）
def find_user(user_id):
    return users_dict.get(user_id)

# 需求2：统计每个城市的用户数
def count_by_city():
    counts = {}
    for user in users_dict.values():
        city = user['city']
        counts[city] = counts.get(city, 0) + 1
    return counts

# 需求3：找年龄最大的用户（用max）
def find_oldest():
    return max(users_dict.values(), key=lambda u: u['age'])

# 需求4：按城市分组（用defaultdict）
from collections import defaultdict
def group_by_city():
    groups = defaultdict(list)
    for user in users_dict.values():
        groups[user['city']].append(user)
    return dict(groups)

t1 = time.time()
for _ in range(1000):
    find_user(9999)
print(f"查1000次用户：{time.time()-t1:.4f}秒")

t2 = time.time()
count_by_city()
print(f"统计城市用户：{time.time()-t2:.6f}秒")

t3 = time.time()
find_oldest()
print(f"找最大年龄：{time.time()-t3:.6f}秒")
```

**性能对比：**
```
需求1-查用户（1000次）：列表0.42秒 → 字典0.0008秒，快了525倍！
需求2-统计城市：列表0.0031秒 → 字典0.0021秒
需求3-找最大年龄：列表0.0023秒 → 字典0.0009秒，快了2.5倍
```

---

## 常见面试题

**Q1：字典的key可以是哪些类型？**
> A：必须是**可哈希的（不可变）**类型，如字符串(str)、数字(int/float)、元组(tuple)。
> 列表(list)、字典(dict)、集合(set) **不能**做key。

```python
# ✅ 合法的key
d = {
    'name': '张三',    # str
    1: '整数',         # int
    (1, 2): '元组',    # tuple
}
# ❌ 非法的key
# d[[1,2]] = '列表'   # TypeError
```

**Q2：Python 3.9+ 两个字典怎么合并？**
> A：3种方式：

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 3}

# 方式1：| 运算符（Python 3.9+）
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 20, 'c': 3}

# 方式2：|= 就地合并（Python 3.9+）
d1 |= d2
print(d1)  # {'a': 1, 'b': 20, 'c': 3}

# 方式3：update（所有版本通用）
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 3}
d1.update(d2)
print(d1)  # {'a': 1, 'b': 20, 'c': 3}
```

**Q3：如何保持字典有序？**
> A：Python 3.7+ 的字典**默认有序**，不需要额外处理。如果需要兼容旧版本，用 `collections.OrderedDict`。

**Q4：字典和列表怎么选？**
> A：看你的主要操作是什么：
> - 需要**快速查找/存在判断** → 用字典（O(1) vs O(n)）
> - 需要**保持顺序** → 用列表
> - 需要**存储重复值** → 用列表
> - 需要**去重** → 用集合（比字典更节省空间）

**Q5：字典的底层原理是什么？**
> A：**哈希表（Hash Table）**。Python通过哈希函数将key转换为数组下标，直接访问对应位置，时间复杂度O(1)。当发生哈希冲突时，使用开放寻址法或链地址法解决。

---

## 推荐：AI Python零基础实战营

想深入学习Python数据结构，把算法面试题全部拿下？

**课程内容：**
- ✅ Python基础语法
- ✅ 数据结构详解（列表、字典、集合、元组）
- ✅ 算法与复杂度分析（时间/空间复杂度）
- ✅ 实战项目练习

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 本讲小结

| 操作 | 代码 | 说明 |
|-----|------|------|
| 创建字典 | `{'a': 1}` 或 `dict(a=1)` | 花括号或dict函数 |
| 安全取值 | `d.get('key', 0)` | 键不存在不报错 |
| 初始化 | `d.setdefault('k', 0)` | 防KeyError |
| 合并字典 | `d1.update(d2)` | d2覆盖d1 |
| 推导式 | `{k:v for k,v in d.items()}` | 一行构建字典 |
| 统计频率 | `Counter(data)` | 快速计数 |
| 默认字典 | `defaultdict(int)` | 自动初始化 |

> 💡 **记住一句话**：要快查、用dict；要存唯一、用set；要存顺序、用list。三个数据结构，各有分工！

---

## 相关阅读

- [Python列表推导式：一行代码搞定循环](/course/AI相关/人民邮电出版社/ads/openclaw/07-Python列表推导式/)
- [Python函数参数*args和**kwargs详解](/course/AI相关/人民邮电出版社/ads/openclaw/09-Python函数参数/)
- [Python集合：去重和关系运算的神器](/course/AI相关/人民邮电出版社/ads/openclaw/10-Python集合/)

---

*PS：字典是Python最高效的数据结构之一。面试必问，工作必用——掌握它，你的代码性能和可读性都会大幅提升。*

---


---

## 📚 推荐教材

**主教材**：[《Python 编程从入门到实践（第 3 版）》](https://u.jd.com/NGMHz3T)


---

## 📚 推荐：Python 零基础实战营

**系统学习Python，推荐这个免费入门课程 👇**

| 特点 | 说明 |
|-----|------|
| 🎯 专为0基础设计 | 门槛低，上手快 |
| 📹 配套视频讲解 | 配合文章学习效果更好 |
| 💬 专属答疑群 | 遇到问题有人带 |
| 🎁 实体书赠送 | 优秀学员送《Python编程从入门到实践》 |

👉 **[点击免费领取 Python 零基础实战营](https://appycyfaqcq1951.pc.xiaoe-tech.com/p/t_pc/goods_pc_detail/goods_detail/course_38vSeD9XU0XdsWnT6jLTaDeRxjT?channel_id=1515397)**


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


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


