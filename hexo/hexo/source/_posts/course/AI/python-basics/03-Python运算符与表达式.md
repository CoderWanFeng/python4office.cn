---
title: Python运算符与表达式：我总结的运算规则，让你写出高效代码
date: 2026-02-28 19:56:00
tags: [Python基础, 运算符, 表达式]
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

## 一个真实的场景

去年有个读者问我："晚枫老师，我写了个计算折扣的程序，结果经常算错几分钱，老板说财务对不上账，怎么办？"

我看了一眼他的代码：

```python
# 原价147.5元，打8折
price = 147.5
discount = 0.8
final_price = price * discount
print(final_price)  # 118.0
```

看起来没问题对吧？但如果是这样呢：

```python
price = 147.7
final_price = price * 0.8  # 118.16
# 但实际计算可能是 118.15999999999998
```

**这是浮点数精度问题，很多新手都会踩坑！**

上篇我们学了数据类型——知道怎么存放数据了。这篇来学**怎么运算数据**，以及运算中的那些坑。

学完这篇，你的程序就能做加减乘除、比大小、做判断，真正"动起来"了。

---

## 算术运算符：数学运算

Python做数学运算，和计算器一样简单——但比计算器强大得多。

### 先来算一笔账

想象你和朋友吃完饭要AA，总价147元，3个人分：

```python
total = 147
people = 3

# 加减乘除
print(total / people)     # 49.0（每人49元，除法）
print(total // people)    # 49（只取整数部分，整除）
print(total % people)     # 0（有余数吗？没有，余数为0）

# 如果是148元呢？
total = 148
print(total / people)     # 49.333...（精确结果）
print(total // people)    # 49（每人49元）
print(total % people)     # 1（还剩1元，谁出？）
```

### 7种算术运算符一览

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

### 深入理解除法

Python有两种除法，一定要分清：

```python
# 普通除法 /：结果永远是浮点数
print(10 / 3)   # 3.3333333333333335（浮点数）
print(9 / 3)    # 3.0（还是浮点数！）
print(10 / 2)   # 5.0（还是浮点数！）

# 整除 //：向下取整
print(10 // 3)  # 3（向下取整）
print(-10 // 3) # -4（注意！负数向下取整是-4，不是-3）

# 为什么？因为 // 是"向下"取整，不是"向零"取整
# -10 / 3 = -3.333...
# -3.333... 向下取整 = -4
```

**记住：** `//` 是向下取整（floor division），不是截断。

### 负数取余的规则

```python
print(10 % 3)   # 1  （10 = 3*3 + 1）
print(-10 % 3)  # 2  （-10 = 3*(-4) + 2）
print(10 % -3)  # -2 （10 = -3*(-4) + (-2)）

# 规则：余数的符号和除数相同
```

### 生活中用得上的技巧

**判断奇偶数：**

```python
age = 25

# 方法1：取余判断
if age % 2 == 0:
    print("偶数")
else:
    print("奇数")
# 运行结果：奇数

# 方法2：位运算（更快）
if age & 1 == 0:
    print("偶数")
else:
    print("奇数")
```

**取数字的各个位：**

```python
num = 12345

# 取个位
print(num % 10)        # 5

# 取十位
print(num // 10 % 10)  # 4

# 取百位
print(num // 100 % 10) # 3

# 取后两位
print(num % 100)       # 45

# 去掉最后两位
print(num // 100)      # 123
```

**翻转数字：**

```python
num = 12345
reversed_num = 0

while num > 0:
    digit = num % 10           # 取最后一位
    reversed_num = reversed_num * 10 + digit
    num = num // 10            # 去掉最后一位

print(reversed_num)  # 54321
```

**四舍五入：**

```python
# 方法1：round函数
print(round(3.4))   # 3
print(round(3.5))   # 4（四舍五入）
print(round(3.6))   # 4

# 方法2：自己实现
def my_round(num):
    return int(num + 0.5)

print(my_round(3.4))  # 3
print(my_round(3.5))  # 4

# 方法3：指定小数位数
print(round(3.14159, 2))  # 3.14
print(round(3.14159, 3))  # 3.142
```

**货币计算（避免浮点数精度问题）：**

```python
# ❌ 错误示范
price = 0.1 + 0.2
print(price)  # 0.30000000000000004（精度丢失！）

# ✅ 方法1：用decimal模块
from decimal import Decimal, ROUND_HALF_UP

price = Decimal('0.1') + Decimal('0.2')
print(price)  # 0.3

# 方法2：整数分计算
price_fen = 10 + 20  # 单位：分
print(price_fen / 100)  # 0.3
```

---

## 比较运算符：比大小

比较运算符返回的是布尔值（True 或 False），是条件判断的基础。

### 6种比较运算符

```python
score = 85

print(score > 60)    # True（85大于60，及格了）
print(score >= 60)   # True（85大于等于60，及格）
print(score < 90)    # True（85小于90）
print(score <= 90)   # True（85小于等于90）
print(score == 85)   # True（等于85）
print(score != 100)  # True（不等于100）
```

### 链式比较：Python的优雅写法

```python
age = 25

# 判断年龄是否在18到60之间
# 传统写法（其他语言）：
result = age >= 18 and age <= 60
print(result)   # True

# Python专属写法（更简洁）：
result = 18 <= age <= 60
print(result)   # True

# 更多例子
score = 75
print(60 <= score < 80)  # True（60-79分，良好区间）
print(0 <= score <= 100) # True（合法分数）
```

### 比较不同类型

```python
# 数字之间可以比较
print(1 < 2.5)      # True
print(1.0 == 1)     # True（值相等）

# 字符串按字典序比较
print("apple" < "banana")  # True（a在b前面）
print("Apple" < "apple")   # True（大写字母ASCII码更小）

# 字符串比较逐字符进行
print("abc" < "abd")       # True（c < d）
print("ab" < "abc")        # True（短字符串是前缀）

# ❌ 不同类型不能直接比较（Python 3）
# print(1 < "2")  # TypeError
```

### 浮点数比较的坑

```python
# ❌ 错误示范
a = 0.1 + 0.2
b = 0.3
print(a == b)  # False！（精度问题）

# ✅ 正确方法：用容差比较
tolerance = 1e-9  # 允许的误差范围
print(abs(a - b) < tolerance)  # True

# 或者用math.isclose
import math
print(math.isclose(a, b))  # True
```

---

## 赋值运算符：边算边存

赋值运算符是把计算结果存回变量，简化代码。

### 复合赋值运算符

```python
x = 10

x += 5   # 等价于 x = x + 5，现在 x = 15
print(x)  # 15

x -= 3   # 等价于 x = x - 3，现在 x = 12
print(x)  # 12

x *= 2   # 等价于 x = x * 2，现在 x = 24
print(x)  # 24

x //= 5  # 等价于 x = x // 5，现在 x = 4
print(x)  # 4

x **= 2  # 等价于 x = x ** 2，现在 x = 16
print(x)  # 16

x %= 3   # 等价于 x = x % 3，现在 x = 1
print(x)  # 1
```

### 实际应用场景

```python
# 计数器
count = 0
count += 1  # 简单明了
count += 1
print(count)  # 2

# 累加求和
total = 0
prices = [10, 20, 30, 40]
for price in prices:
    total += price  # 累加
print(total)  # 100

# 累乘求积
product = 1
for i in range(1, 6):
    product *= i
print(product)  # 120 (1*2*3*4*5)
```

### 海象运算符（Python 3.8+）

```python
# 传统写法
text = input("请输入: ")
if len(text) > 5:
    print(f"输入了{len(text)}个字符")

# 海象运算符（在表达式内赋值）
if (n := len(input("请输入: "))) > 5:
    print(f"输入了{n}个字符")

# 实际应用：读取文件
# while (line := file.readline()):
#     process(line)
```

---

## 逻辑运算符：组合判断

`and`（且）、`or`（或）、`not`（非）用来组合多个条件。

### and：两个都要满足

```python
# 用户要同时满足：年满18岁 AND 充值金额>=100元 才能开通VIP
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

```python
# 用户满足：VIP用户 OR 充值金额>=500元 之一，即可享受折扣
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

# not常用于判断空值
name = ""
if not name:
    print("姓名不能为空")
```

### 真值表

| A | B | A and B | A or B | not A |
|:---:|:---:|:---:|:---:|:---:|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

### 短路求值：Python很聪明

```python
# and短路：第一个是False，后面的不看了
result = False and print("这里不会执行")
print(result)  # False

# or短路：第一个是True，后面的不看了
result = True or print("这里也不会执行")
print(result)  # True

# 实际应用：避免报错
user = None
# 如果user是None，后面的user.name不会执行，避免AttributeError
if user and user.name:
    print(user.name)
else:
    print("用户不存在")
```

**为什么叫短路？** Python在`and`的左边已经知道结果为False，或者`or`的左边已经知道结果为True时，就不再看后面的代码了——因为后面再怎么看，也不会改变最终结果。这能**省时间，有时候还能避免报错**。

### 逻辑运算返回值

```python
# and返回第一个为False的值，或最后一个值
print(3 and 5)    # 5（都为真，返回最后一个）
print(0 and 5)    # 0（0是假，返回它）
print(3 and 0)    # 0（返回第一个假值）
print(0 and "")   # 0

# or返回第一个为True的值，或最后一个值
print(3 or 5)     # 3（3是真，返回它）
print(0 or 5)     # 5（返回第一个真值）
print(0 or "")    # ""（都为假，返回最后一个）

# 实际应用：设置默认值
name = input("请输入姓名: ") or "匿名用户"
print(name)  # 如果没输入，默认"匿名用户"
```

---

## 成员运算符：在一堆东西里找

判断某个元素是否在一组数据中。

### in 和 not in

```python
fruits = ["苹果", "香蕉", "橙子"]

print("苹果" in fruits)       # True（在列表里）
print("葡萄" in fruits)      # False（不在列表里）
print("葡萄" not in fruits)   # True（确实不在）
```

### 不同类型的应用

```python
# 字符串中查找
print("a" in "apple")      # True
print("app" in "apple")    # True（子串也可以）
print("x" not in "apple")  # True

# 列表中查找
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)        # True
print(6 in numbers)        # False

# 元组中查找
coordinates = (0, 0)
print(0 in coordinates)    # True

# 集合中查找（速度快！）
unique_numbers = {1, 2, 3, 4, 5}
print(3 in unique_numbers)  # True

# 字典中查找（查的是key）
person = {"name": "张三", "age": 25}
print("name" in person)   # True（"name"是键）
print("张三" in person)   # False（"张三"是值，键里没有它）
print("张三" in person.values())  # True（查值要用values()）
```

### 性能对比

```python
import time

# 列表查找：O(n)
large_list = list(range(1000000))
start = time.time()
print(999999 in large_list)
print(f"列表查找: {time.time() - start:.6f}秒")

# 集合查找：O(1)
large_set = set(range(1000000))
start = time.time()
print(999999 in large_set)
print(f"集合查找: {time.time() - start:.6f}秒")
```

**结论：** 频繁查找用集合，速度快几个数量级！

---

## 身份运算符：是不是同一个东西

`is`判断的是两个变量是不是**同一个对象**（内存地址相同），`==`判断的是**内容是否相同**。

### is vs ==

```python
a = [1, 2, 3]
b = a           # b和a指向同一个列表（同一个东西）
c = [1, 2, 3]  # c是一个新创建的列表（内容相同，但不是同一个）

print(a is b)   # True（a和b是同一个人）
print(a is c)   # False（a和c不是同一个人，虽然长得一样）
print(a == c)  # True（a和c的内容相等）
```

### 比喻理解

- `is`：这两个人是不是**同一个人**（双胞胎也不行，是本人）
- `==`：这两个人**长得像不像**

### None的判断

```python
# ✅ 推荐写法
x = None
if x is None:
    print("x是None")

# ❌ 不推荐（虽然能用）
if x == None:
    print("x是None")
```

### 小整数缓存

```python
# 小整数（-5到256）会被缓存
a = 256
b = 256
print(a is b)  # True（同一个对象）

a = 257
b = 257
print(a is b)  # 可能是False（不同对象）

# 字符串也有类似缓存
a = "hello"
b = "hello"
print(a is b)  # True（短字符串会被缓存）

a = "hello world!"
b = "hello world!"
print(a is b)  # 可能是False
```

### 最佳实践

```python
# ✅ 用 is 判断None
if x is None:
    pass

# ✅ 用 == 比较值
if a == b:
    pass

# ❌ 不要用 is 比较数字和字符串
if a is 5:  # 不推荐
    pass
```

---

## 位运算符：底层操作

位运算直接对二进制位操作，速度快但可读性差。

### 位运算符一览

```python
a, b = 60, 13  # 60 = 00111100, 13 = 00001101

print(a & b)   # 12  → 按位与（都为1才是1）
print(a | b)   # 61  → 按位或（有1就是1）
print(a ^ b)   # 49  → 按位异或（不同为1）
print(~a)      # -61 → 按位取反
print(a << 2)  # 240 → 左移2位（乘4）
print(a >> 2)  # 15  → 右移2位（除4）
```

### 实际应用

```python
# 判断奇偶（更快）
num = 7
print(num & 1)  # 1（奇数）
num = 8
print(num & 1)  # 0（偶数）

# 交换变量（不用临时变量）
a, b = 10, 20
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)  # 20 10

# 或者更简单
a, b = 10, 20
a, b = b, a  # Python特有的交换方式
print(a, b)  # 20 10

# 权限判断
READ = 1      # 001
WRITE = 2     # 010
EXECUTE = 4   # 100

permission = READ | WRITE  # 011（可读可写）
print(permission & READ)   # 1（有读权限）
print(permission & EXECUTE)  # 0（无执行权限）

# 快速乘除
num = 10
print(num << 1)  # 20（乘2）
print(num >> 1)  # 5（除2）
```

---

## 运算符优先级：先算谁？

数学里先乘除后加减，Python也一样：

| 优先级（高→低） | 运算符 |
|:---:|------|
| 1 | `()` 括号 |
| 2 | `**` 幂 |
| 3 | `+x, -x, ~x` 正负号、按位取反 |
| 4 | `* / // %` 乘除取余 |
| 5 | `+ -` 加减 |
| 6 | `<< >>` 移位 |
| 7 | `&` 按位与 |
| 8 | `^` 按位异或 |
| 9 | `|` 按位或 |
| 10 | `> < >= <= == !=` 比较 |
| 11 | `is, is not, in, not in` 身份和成员 |
| 12 | `not` 非 |
| 13 | `and` 且 |
| 14 | `or` 或 |

### 经典陷阱

```python
# 陷阱1：幂运算从右到左
print(2 ** 3 ** 2)  # 512（不是64！），等价于 2 ** (3 ** 2)

# 陷阱2：比较和逻辑
print(True == False or True)  # True
# 解析：(True == False) or True → False or True → True

# 陷阱3：is和==
print(a is b == c)  # 等价于 (a is b) and (b == c)
```

### 最佳实践：用括号

```python
# 不加括号（先算乘法）
result = 2 + 3 * 4
print(result)  # 14

# 加括号（先算加法）
result = (2 + 3) * 4
print(result)  # 20

# 复杂表达式：加括号增加可读性
result = ((a + b) * c - d) / e
```

**黄金法则：** 不确定优先级时，用括号明确意图。

---

## 避坑指南：常见错误

### 错误1：混淆 = 和 ==

```python
# ❌ 错误
if x = 5:  # 语法错误！= 是赋值，== 才是比较
    pass

# ✅ 正确
if x == 5:
    pass
```

### 错误2：浮点数精度

```python
# ❌ 问题代码
a = 0.1 + 0.2
if a == 0.3:
    print("相等")  # 不会执行！

# ✅ 正确方法
import math
if math.isclose(a, 0.3):
    print("相等")
```

### 错误3：链式赋值陷阱

```python
# ❌ 常见错误
a = b = []
a.append(1)
print(b)  # [1]（b也变了！它们指向同一个列表）

# ✅ 正确方法
a = []
b = []
a.append(1)
print(b)  # []
```

### 错误4：运算顺序错误

```python
# ❌ 错误：想表达 2^(3^2)，写成了这样
result = 2 ** 3 ** 2  # 512，正确但容易误解

# ✅ 明确意图
result = 2 ** (3 ** 2)  # 512
result = (2 ** 3) ** 2  # 64
```

### 错误5：整数除法方向

```python
# ❌ 理解错误
print(-10 // 3)  # -4（向下取整，不是-3）

# ✅ 正确理解
# -10 / 3 = -3.333...
# 向下取整 = -4
```

---

## 实战案例：智能评分系统

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

### 实战案例：购物车计算

```python
def calculate_total(items, discount_rate=0, member_level="普通"):
    """计算购物车总价"""
    
    # 计算原价
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    
    # 会员折扣
    member_discount = {
        "普通": 1.0,
        "银卡": 0.95,
        "金卡": 0.9,
        "钻石": 0.85
    }
    
    # 计算折扣
    discount = max(discount_rate, 1 - member_discount.get(member_level, 1.0))
    
    # 最终价格
    final_price = subtotal * (1 - discount)
    
    return {
        "subtotal": subtotal,
        "discount_rate": discount * 100,
        "final_price": round(final_price, 2)
    }

# 测试
cart = [
    {"name": "苹果", "price": 5.5, "quantity": 3},
    {"name": "香蕉", "price": 3.0, "quantity": 5},
    {"name": "橙子", "price": 4.5, "quantity": 2}
]

result = calculate_total(cart, discount_rate=0.1, member_level="金卡")
print(f"商品总价：{result['subtotal']}元")
print(f"优惠折扣：{result['discount_rate']}%")
print(f"实付金额：{result['final_price']}元")
```

### 实战案例：时间计算器

```python
def calculate_time(seconds):
    """将秒数转换为时分秒"""
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    return f"{hours}小时{minutes}分钟{secs}秒"

# 测试
print(calculate_time(3661))   # 1小时1分钟1秒
print(calculate_time(7325))   # 2小时2分钟5秒
print(calculate_time(86400))  # 24小时0分钟0秒
```

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

---

## 本讲小结

| 运算符 | 作用 | 例子 |
|:---:|------|------|
| `+ - * / // % **` | 算术运算 | `10 / 3 = 3.33` |
| `> < >= <= == !=` | 比较大小 | `5 > 3 = True` |
| `and or not` | 逻辑组合 | `True and False = False` |
| `in / not in` | 成员判断 | `"a" in "abc" = True` |
| `is / is not` | 身份判断 | 比较是否同一对象 |
| `+= -= *= /=` | 赋值运算 | `x += 1`（x加1） |
| `& | ^ ~ << >>` | 位运算 | `8 >> 1 = 4` |

---

## 下节预告

学会了运算，下一篇来学**条件判断（if/else）**——让程序学会做选择。

你将学会：
- if/elif/else的完整用法
- 嵌套条件判断
- 三元表达式
- match-case新模式（Python 3.10+）

👉 **[继续阅读：Python条件判断](./04-Python条件判断.md)**

---

## 课程导航

**上一篇：** [Python零基础入门：写下你的第一行代码](./01-Python零基础入门.md)

**下一篇：** [Python条件判断-if-else完全指南](./04-Python条件判断.md)

---

## 相关阅读

- [Python变量与数据类型完全指南](./02-Python变量与数据类型.md)
- [零基础学AI编程：30天速成计划](/course/AI相关/人民邮电出版社/ads/openclaw/python/20260228171202-零基础学AI编程-30天速成计划/)

---

*PS：运算符是编程的"算盘"，多动手算几个生活中的例子，比死记硬背有用得多。记住：代码是写给人看的，顺便给机器运行。*

*2026-04-23 更新 by 程序员晚枫*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


