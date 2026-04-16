---
title: Python集合：我用这个数据结构，去重只要1行代码
date: 2026-02-28 17:29:00
tags: [Python基础, 集合, 数据结构]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://www.bilibili.com/cheese/play/ss982042944'>
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
<a href="https://www.bilibili.com/cheese/play/ss982042944">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

今天聊一个Python中经常被忽视的数据结构——**集合（set）**。

很多人学Python时跳过了它，觉得用列表就够了。但你知道吗？**集合的去重功能，一行代码就能搞定，而且速度飞快！**

看完这篇文章，你会发现新大陆。

---

## 什么是集合？

想象你面前有一堆混在一起的球，有红的有蓝的有绿的，有的重复了：

```
红球、红球、蓝球、绿球、绿球、绿球、红球
```

现在你把它们倒进一个箱子里，摇一摇——拿出来时，**每种颜色的球只出现一次**。

**这就是集合：会自动去重、没有顺序、只存唯一值。**

### 创建集合

```python
# 方式1：花括号（和字典一样，但存的是值，不是键值对）
s1 = {1, 2, 3, 3, 3}
print(s1)  # {1, 2, 3}

# 方式2：set() 函数（从列表转换）
s2 = set([1, 2, 2, 3, 3, 3])
print(s2)  # {1, 2, 3}
```

> ⚠️ **注意**：`{}` 是空字典，不是空集合！空集合要用 `set()`

```python
empty_set = set()    # ✅ 正确：空集合
# empty_dict = {}     # ❌ 这是空字典，不是集合
```

---

## 最常用功能：一键去重

假设你有一个列表，里面有重复的名字，要去掉重复的：

### 场景：去掉重复的客户名单

```python
# 有重复的客户名单
customers = ["张三", "李四", "王五", "张三", "赵六", "李四", "钱七"]
print(f"原始列表（{len(customers)}人）：{customers}")

# ❌ 方法1：循环判断（麻烦）
unique1 = []
for name in customers:
    if name not in unique1:
        unique1.append(name)

# ❌ 方法2：字典去重（稍好）
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

> 💡 **为什么用集合？** 集合内部用哈希表实现，查找速度比列表快得多。数据量大时，优势明显。

---

## 集合的关系运算（超实用）

集合最强大的功能是**关系运算**，处理"谁和谁有交集"这类问题特别方便。

### 场景：找出两个班级的共同好友

```python
# Alice 的好友列表
alice_friends = {'Bob', 'Charlie', 'David', 'Eve'}
# Bob 的好友列表
bob_friends = {'Alice', 'Charlie', 'Eve', 'Frank'}

# 🎯 共同好友（交集 &）
common = alice_friends & bob_friends
print(f"共同好友：{common}")

# 📦 Alice 的所有好友（并集 |）
all_friends = alice_friends | bob_friends
print(f"所有好友：{all_friends}")

# 👤 只在 Alice 好友列表里的（差集 -）
only_alice = alice_friends - bob_friends
print(f"只在 Alice 列表：{only_alice}")

# 🔄 不是共同好友的（对称差集 ^）
not_common = alice_friends ^ bob_friends
print(f"非共同好友：{not_common}")
```

**运行结果：**

```
共同好友：{'Eve', 'Charlie'}
所有好友：{'Alice', 'David', 'Frank', 'Bob', 'Charlie', 'Eve'}
只在 Alice 列表：{'David', 'Bob'}
非共同好友：{'Alice', 'David', 'Frank', 'Bob'}
```

### 运算符对照表

| 运算符 | 方法 | 含义 | 记忆方式 |
|-------|------|------|---------|
| `&` | `intersection()` | 交集（共同元素） | 两个都要 |
| `\|` | `union()` | 并集（所有元素） | 合在一起 |
| `-` | `difference()` | 差集（在A不在B） | A减掉B |
| `^` | `symmetric_difference()` | 对称差集（不共有） | 去掉共同的 |

---

## 实战案例：销售数据分析

假设你有两个销售文件，想快速分析客户重叠情况：

```python
# 从文件A读取的客户ID
file_a = {1001, 1002, 1003, 1004, 1005}
# 从文件B读取的客户ID
file_b = {1004, 1005, 1006, 1007, 1008}

# 两个文件都有的客户
both_files = file_a & file_b
print(f"两个文件都有的客户：{both_files}")
print(f"人数：{len(both_files)}人")

# 只在A文件
only_a = file_a - file_b
print(f"只在A文件的客户：{only_a}")

# 总共有多少不同客户
total = len(file_a | file_b)
print(f"总客户数（去重后）：{total}人")
```

**运行结果：**

```
两个文件都有的客户：{1004, 1005}
人数：2人
只在A文件的客户：{1001, 1002, 1003}
总客户数（去重后）：8人
```

---

## 集合的其他操作

### 添加和删除元素

```python
s = {1, 2, 3}

# 添加一个
s.add(4)
print(s)  # {1, 2, 3, 4}

# 添加多个
s.update([5, 6])
print(s)  # {1, 2, 3, 4, 5, 6}

# 删除（元素不存在会报错）
s.remove(3)
print(s)  # {1, 2, 4, 5, 6}

# 删除（元素不存在不会报错）
s.discard(99)  # 什么都不发生

# 随机删除一个
popped = s.pop()
print(f"删除了：{popped}, 剩下：{s}")
```

### 判断子集/超集

```python
a = {1, 2, 3}
b = {1, 2}

print(b.issubset(a))    # True，b是a的子集
print(a.issuperset(b))  # True，a是b的超集
print(a.isdisjoint(b))  # False，a和b有交集
```

---

## 什么时候用集合？

### ✅ 适合用集合的场景
- **需要去重** → 一行搞定
- **判断成员是否存在** → 比列表快100倍！
- **求交集、并集、差集** → 直接用运算符
- **需要确保元素唯一性** → 自动去重

### ❌ 不适合用集合的场景
- **需要保持顺序** → 集合无序
- **需要通过索引访问** → 集合没有索引
- **需要存可变对象** → 列表不能放集合里

---


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


## 本讲小结

| 操作 | 代码 | 说明 |
|-----|------|------|
| 创建集合 | `{1, 2, 3}` 或 `set([1,2,3])` | 花括号或set函数 |
| 去重 | `list(set(data))` | 一行代码搞定 |
| 交集 | `a & b` | 共同的元素 |
| 并集 | `a \| b` | 所有元素合并 |
| 差集 | `a - b` | 在a里不在b里 |
| 添加 | `s.add(x)` | 加一个元素 |
| 删除 | `s.remove(x)` | 删除指定元素 |

> 💡 **记住一句话**：要去重？用 set！要做关系运算？用 set！

---

## 下节预告

学会了集合，下一篇来学**装饰器**——给函数加功能的"黑魔法"。

👉 **[继续阅读：Python装饰器](./11-Python装饰器.md)**

---

## 课程导航

**下一篇：** [Python函数参数*args和**kwargs详解](./09-Python函数参数.md)

**下一篇：** [Python装饰器：给函数加功能的黑魔法](./11-Python装饰器.md)

---

*PS：集合是Python最被低估的数据结构之一。记住：要去重用set，要快用set，要做关系运算还是用set！*

