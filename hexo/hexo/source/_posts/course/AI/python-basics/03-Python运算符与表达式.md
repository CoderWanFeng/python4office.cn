---
title: Python运算符与表达式：我总结的运算规则，让你写出高效代码
date: 2026-02-28 19:56:00
tags: [Python基础, 运算符, 表达式]
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

上篇我们学了数据类型——知道怎么存放数据了。这篇来学**怎么运算数据**。

学完这篇，你的程序就能做加减乘除、比大小、做判断，真正"动起来"了。

---

## 算术运算符：数学运算

Python做数学运算，和计算器一样简单。

### 先来算一笔账

想象你和朋友吃完饭要AA，总价147元，3个人分：

```python
total = 147
people = 3

# 加减乘除
print(total / people)     # 49.0（每人49元，除法）
print(total // people)    # 49（只取整数部分，整除）
print(total % people)     # 0（有余数吗？没有，余数为0）
```

### 6种算术运算符一览

```python
a, b = 10, 3

print(a + b)   # 13  → 加法
print(a - b)   # 7   → 减法
print(a * b)   # 30  → 乘法
print(a / b)   # 3.333... → 除法（结果是浮点数）
print(a // b)  # 3   → 整除（只取整数部分，去掉小数）
print(a % b)   # 1   → 取余（除法剩下的余数）
print(a ** b)  # 1000 → 幂运算（10的3次方）
```

**运行结果：**

```
13
7
30
3.3333333333333335
3
1
1000
```

### 生活中用得上的技巧

**判断奇偶数（余数判断）：**

```python
age = 25

if age % 2 == 0:
    print("偶数")
else:
    print("奇数")

# 运行结果：奇数
```

**取数字的个位：**

```python
num = 123
print(num % 10)   # 3（取余得到最后一位）
print(num // 10)  # 12（去掉最后一位）
```

**四舍五入：**

```python
price = 19.7
rounded = int(price + 0.5)  # 20
print(rounded)
```

---

## 比较运算符：比大小

比较运算符返回的是布尔值（True 或 False）。

### 用成绩来理解

```python
score = 85

print(score > 60)    # True（85大于60，及格了）
print(score >= 60)   # True（85大于等于60，及格）
print(score == 100)  # False（85不等于100，不是满分）
print(score != 100)  # True（85不等于100，对的）
print(score < 60)   # False（85不小于60，没挂科）
```

**Python有个很人性化的写法——链式比较：**

```python
age = 25

# 判断年龄是否在18到60之间
# 传统写法：
print(age >= 18 and age <= 60)   # True

# Python专属写法（更简洁）：
print(18 <= age <= 60)          # True
```

---

## 赋值运算符：边算边存

赋值运算符是把计算结果存回变量。

```python
x = 10

x += 5   # 等价于 x = x + 5，现在 x = 15
print(x)  # 15

x -= 3   # 等价于 x = x - 3，现在 x = 12
print(x)  # 12

x *= 2   # 等价于 x = x * 2，现在 x = 24
print(x)  # 24
```

> 💡 **什么时候用？** 当你只想修改变量本身时，比如计数器`count += 1`。

---

## 逻辑运算符：组合判断

`and`（且）、`or`（或）、`not`（非）用来组合多个条件。

### and：两个都要满足

```
用户要同时满足：年满18岁 AND 充值金额>=100元 才能开通VIP
```

```python
age = 20
balance = 150

can_vip = (age >= 18) and (balance >= 100)
print(can_vip)  # True

# 其中一个不满足：
age = 16
can_vip = (age >= 18) and (balance >= 100)
print(can_vip)  # False（年龄不够）
```

### or：满足一个就行

```
用户满足：VIP用户 OR 充值金额>=500元 之一，即可享受折扣
```

```python
is_vip = False
balance = 600

can_discount = is_vip or (balance >= 500)
print(can_discount)  # True（虽然不是VIP，但充值够了）

is_vip = False
balance = 200
can_discount = is_vip or (balance >= 500)
print(can_discount)  # False（两个条件都不满足）
```

### not：取反

```python
is_locked = True
print(not is_locked)  # False（解锁后就不是锁定状态了）

is_logged_in = False
if not is_logged_in:
    print("请先登录")   # 会执行这句
```

### 短路求值：Python很聪明

```python
# and短路：第一个是False，后面的不看了
result = False and print("这里不会执行")
print(result)  # False

# or短路：第一个是True，后面的不看了
result = True or print("这里也不会执行")
print(result)  # True
```

> 💡 **为什么叫短路？** Python在`and`的左边已经知道结果为False，或者`or`的左边已经知道结果为True时，就不再看后面的代码了——因为后面再怎么看，也不会改变最终结果。这能**省时间，有时候还能避免报错**。

---

## 成员运算符：在一堆东西里找

判断某个元素是否在一组数据中。

```python
fruits = ["苹果", "香蕉", "橙子"]

print("苹果" in fruits)       # True（在列表里）
print("葡萄" in fruits)      # False（不在列表里）
print("葡萄" not in fruits)   # True（确实不在）
```

**在字典里，`in`查的是键（key），不是值（value）：**

```python
person = {"name": "张三", "age": 25}

print("name" in person)   # True（"name"是键）
print("张三" in person)   # False（"张三"是值，键里没有它）
```

---

## 身份运算符：是不是同一个东西

`is`判断的是两个变量是不是**同一个对象**（内存地址相同），`==`判断的是**内容是否相同**。

### 比喻理解

- `is`：这两个人是不是**同一个人**（双胞胎也不行，是本人）
- `==`：这两个人**长得像不像**

```python
a = [1, 2, 3]
b = a           # b和a指向同一个列表（同一个东西）
c = [1, 2, 3]  # c是一个新创建的列表（内容相同，但不是同一个）

print(a is b)   # True（a和b是同一个人）
print(a is c)   # False（a和c不是同一个人，虽然长得一样）
print(a == c)  # True（a和c的内容相等）
```

> ⚠️ **常见坑**：比较字符串和数字时，不要用`is`：

```python
x = "hello"
y = "hello"
print(x is y)   # 可能在某些情况下是True，但不是绝对的，不可靠
print(x == y)   # ✅ 正确：比较内容永远用 ==
```

---

## 运算符优先级：先算谁？

数学里先乘除后加减，Python也一样：

| 优先级（高→低） | 运算符 |
|:---:|------|
| 1 | `()` 括号 |
| 2 | `**` 幂 |
| 3 | `* / // %` 乘除取余 |
| 4 | `+ -` 加减 |
| 5 | `> < >= <= == !=` 比较 |
| 6 | `not` 非 |
| 7 | `and` 且 |
| 8 | `or` 或 |

**遇到复杂表达式，用括号最安全：**

```python
# 不加括号（先算乘法）
result = 2 + 3 * 4
print(result)  # 14

# 加括号（先算加法）
result = (2 + 3) * 4
print(result)  # 20
```

---

## 实战练习：智能评分系统

用运算符写一个成绩评级程序：

```python
def grade_score(score):
    """根据分数返回等级"""
    if score >= 90:
        return "A（优秀）"
    elif score >= 80:
        return "B（良好）"
    elif score >= 70:
        return "C（中等）"
    elif score >= 60:
        return "D（及格）"
    else:
        return "F（不及格）"

# 测试几个成绩
scores = [95, 82, 73, 61, 45]

print("=" * 20)
print("考试成绩评级")
print("=" * 20)
for s in scores:
    result = "及格" if s >= 60 else "不及格"
    print(f"分数：{s}  →  等级：{grade_score(s)}  【{result}】")
print("=" * 20)
```

**运行结果：**

```
====================
考试成绩评级
====================
分数：95  →  等级：A（优秀）  【及格】
分数：82  →  等级：B（良好）  【及格】
分数：73  →  等级：C（中等）  【及格】
分数：61  →  等级：D（及格）  【及格】
分数：45  →  等级：F（不及格）  【不及格】
====================
```

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

| 运算符 | 作用 | 例子 |
|:---:|------|------|
| `+ - * / // % **` | 算术运算 | `10 / 3 = 3.33` |
| `> < >= <= == !=` | 比较大小 | `5 > 3 = True` |
| `and or not` | 逻辑组合 | `True and False = False` |
| `in / not in` | 成员判断 | `"a" in "abc" = True` |
| `is / is not` | 身份判断 | 比较是否同一对象 |
| `+= -= *= /=` | 赋值运算 | `x += 1`（x加1） |

---

## 下节预告

学会了运算，下一篇来学**条件判断（if/else）**——让程序学会做选择。

👉 **[继续阅读：Python条件判断](./04-Python条件判断.md)**

---

## 课程导航

**上一篇：** [Python零基础入门：写下你的第一行代码](./01-Python零基础入门.md)

**下一篇：** [Python条件判断-if-else完全指南](./04-Python条件判断.md)

---

*PS：运算符是编程的"算盘"，多动手算几个生活中的例子，比死记硬背有用得多。*

