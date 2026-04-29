---

title: Python变量与数据类型：我用7大数据类型，处理所有业务场景
date: 2026-02-28 19:55:00
tags: [Python基础, 变量, 数据类型]
cover: https://images.unsplash.com/photo-152637909?w=800&h=400&fit=crop

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

上篇文章我们写下了第一行代码。今天来学编程的根基——**变量和数据类型**。

学完这篇，你就能用Python表达世界上的一切信息了。

---

## 什么是变量？

想象你的办公桌上有一排抽屉，每个抽屉上贴着标签。你在`姓名`抽屉里放了"张三"，在`年龄`抽屉里放了`25`。

变量，就是这个带标签的抽屉。**给数据起个名字，方便以后找。**

### 一行代码创建变量

Python不需要声明变量类型，直接写就行：

```python
name = "张三"       # 把"张三"这个名字，存进 name 这个抽屉
age = 25           # 把数字 25，存进 age 这个抽屉
is_vip = True      # 把 True，存进 is_vip 这个抽屉
```

> 💡 **注意**：等号`=`在编程里叫"赋值"，意思是把右边的值放进左边的变量里，不是数学里的"等于"。

### 运行结果

```python
print(name)    # 输出：张三
print(age)     # 输出：25
print(is_vip)  # 输出：True
```

---

## 变量命名规则

给变量起名字，有几个规矩要遵守：

```python
user_name = "Alice"    # ✅ 可以：字母+下划线
userName = "Bob"       # ✅ 可以：驼峰命名（但不推荐）
name2 = "Charlie"      # ✅ 可以：字母中间加数字

2name = "David"       # ❌ 错误：不能以数字开头
user-name = "Eve"     # ❌ 错误：不能有连字符-
class = "Math"        # ❌ 错误：不能是Python的关键字（如 class、if、for）
```

**实际开发中的好习惯：**

```python
# ❌ 差的名字（不知道存的是什么）
x = 25
y = "北京"

# ✅ 好的名字（一眼就知道是什么）
age = 25
city = "北京"
```

> 💡 **小技巧**：变量名用英文，不要用拼音。在团队协作时，拼音变量名会让同事看不懂。

---

## 7大基本数据类型

现实生活中的数据五花八门：姓名是文字，年龄是数字，状态是"是/否"。Python 把这些分成7种类型来处理。

### ① 整数（int）—— 没有小数点的数字

生活中用到的整数无处不在：年龄、人数、价格（取整）、年份……

```python
age = 25              # 年龄
student_count = 120  # 学生人数
year = 2026           # 年份
temperature = -5      # 温度（可以是负数）
```

**Python 处理大数非常轻松，其他语言可能会溢出：**

```python
print(2 ** 100)
# 输出：1267650600228229401496703205376
# 2的100次方，瞬间算出来
```

### ② 浮点数（float）—— 带小数点的数字

购物价格、身高体重、测量数据……凡是有小数点的，都是浮点数。

```python
price = 19.99        # 商品价格
height = 1.75        # 身高（米）
pi = 3.14159         # 圆周率
```

> ⚠️ **有个小坑要记住**：计算机处理小数有精度问题

```python
print(0.1 + 0.2)
# 输出：0.30000000000000004
# 不是算错了，是计算机表示小数的固有误差
# 实际开发中，如果需要精确计算（如财务），用专门的 decimal 库
```

### ③ 字符串（str）—— 一串文字

姓名、地址、一段话……所有文字内容都是字符串，用引号包起来。

```python
name = "张三"                    # 双引号
city = '北京'                    # 单引号（效果一样）
bio = """我叫张三，               # 三引号可以写多行
         来自北京，
         是一名Python程序员"""   

# 常用操作
print(len(name))                 # 3（中文字符，一个字算一个长度）
print(name.upper())              # 张三（中文不支持大写，换成英文演示）
print("Hello " + name)           # Hello 张三（文字拼接）
```

**字符串的索引（像编号一样取其中的字）：**

```python
word = "Python"
print(word[0])   # P（从左边第1个开始）
print(word[1])   # y
print(word[-1])  # n（-1表示倒数第1个）
print(word[0:3]) # Pyt（从第0个到第3个之前，0/1/2）
```

> 💡 **类比**：字符串就像一列火车，每个车厢有编号（索引）。`word[0]`就是第1节车厢，`word[-1]`是最后一节。

👉 **[深入学习：Python字符串20个实用方法](./12-Python字符串.md)**

### ④ 布尔值（bool）—— 是或否

表示"对/错"、"是/否"，只有两个值：`True`（真）和`False`（假）。

**布尔值通常来自比较运算：**

```python
print(5 > 3)     # True  （5大于3吗？是的）
print(10 == 10)  # True  （10等于10吗？是的）
print(7 != 3)    # True  （7不等于3吗？是的）
print(5 >= 5)    # True  （5大于等于5吗？是的）
```

**在生活中，布尔值就是判断题：**

```python
is_adult = age >= 18        # 年龄>=18就是成年人
is_summer = month >= 6 and month <= 8  # 6到8月是夏天
has_ticket = True           # 有票吗？有（True）

print(is_adult)   # True（25岁，是成年人）
```

### ⑤ 空值（None）—— 什么都没有

表示"这个抽屉是空的"，或者"数据未知"。

**最常见的场景：函数找不到结果时返回 None**

```python
def find_user(user_id):
    """根据ID查找用户，找不到就返回None"""
    database = {1: "张三", 2: "李四"}
    if user_id in database:
        return database[user_id]
    return None  # 找不到，返回空

result = find_user(3)
print(result)  # None（3号用户不存在）
```

> 💡 **类比**：空值就像快递柜里一个空的格子——格子存在（变量存在），但里面没东西（值是空的）。

### ⑥ 列表（list）—— 装很多东西的列表

当你要存**多个相关的东西**，比如一列商品、一组成绩、一堆名字，用列表。

**生活中的列表就是购物清单：**

```python
# 购物清单（列表）
fruits = ["苹果", "香蕉", "橙子"]
scores = [85, 92, 78, 90]

# 读取第1个（索引从0开始）
print(fruits[0])   # 苹果（第一个）
print(fruits[-1])  # 橙子（倒数第一个）

# 增删改查
fruits.append("葡萄")    # 添加一项
fruits.remove("香蕉")    # 删除一项
print(len(fruits))       # 4（现在有4种水果了）

# 列表可以混合类型（但实际开发中不推荐）
mixed = ["张三", 25, 1.75, True]
```

**运行结果：**

```python
print(fruits)
# ['苹果', '香蕉', '橙子', '葡萄']

print(f"一共买了 {len(fruits)} 种水果，分别是：")
for fruit in fruits:
    print(f"  - {fruit}")
#   - 苹果
#   - 香蕉
#   - 橙子
#   - 葡萄
```

👉 **[深入学习：Python列表推导式，让列表操作更优雅](./07-Python列表推导式.md)**

### ⑦ 字典（dict）—— 有名字的抽屉

列表用数字编号存取，但如果数据有明确的名字/属性，用字典更清晰。

**生活中的字典就是信息卡片：**

```python
# 一张人物信息卡（字典）
person = {
    "姓名": "张三",
    "年龄": 25,
    "城市": "北京",
    "VIP": True
}

# 用名字（key）来存取，不用记编号
print(person["姓名"])          # 张三
person["职业"] = "程序员"      # 新增一个字段
print(person["职业"])           # 程序员

# 遍历字典
for key, value in person.items():
    print(f"{key}：{value}")
```

**运行结果：**

```
姓名：张三
年龄：25
城市：北京
VIP：True
职业：程序员
```

> 💡 **什么时候用列表，什么时候用字典？**
> - **列表**：东西是一排同类的，用索引存取。比如：`["苹果", "香蕉"]`
> - **字典**：东西有不同属性，用名字存取。比如：一个人的姓名、年龄、地址……

👉 **[深入学习：Python字典使用技巧](./08-Python字典.md)**

---

## 类型转换：数据类型之间怎么互转？

有时候同一个数据需要换一种形式，比如数字`25`变成字符串`"25"`。

```python
# 字符串转整数（用户输入的年龄是字符串，需要转成数字计算）
age_str = "25"
age = int(age_str)        # "25" → 25
print(age + 5)            # 30

# 整数转字符串（数字拼接到文字里）
count = 10
message = "你收到了" + str(count) + "条消息"
print(message)            # 你收到了10条消息

# 转浮点数
price = float("19.99")   # "19.99" → 19.99

# 字符串转列表（拆成单个字符）
chars = list("hello")
print(chars)              # ['h', 'e', 'l', 'l', 'o']
```

> ⚠️ **注意**：不是所有转换都行得通。`int("hello")`会报错——"hello"不是数字，没法转成整数。

---

## 查看数据类型：type()函数

想知道一个变量是什么类型，用`type()`：

```python
print(type(25))           # <class 'int'>
print(type(19.99))        # <class 'float'>
print(type("你好"))        # <class 'str'>
print(type(True))         # <class 'bool'>
print(type(None))         # <class 'NoneType'>
print(type([1, 2, 3]))    # <class 'list'>
print(type({"a": 1}))     # <class 'dict'>
```

---

## 实战练习：创建一个学生信息卡

综合运用所有数据类型，做一个学生报告：

```python
# 学生信息
name = "小明"
age = 20
scores = [85, 90, 78, 92]  # 语数英体四科成绩
info = {
    "专业": "计算机科学",
    "年级": "大二",
    "VIP学员": True
}

# 计算平均分
average = sum(scores) / len(scores)

# 打印完整报告
print("=" * 30)
print(f"📋 学生报告")
print("=" * 30)
print(f"姓名：{name}")
print(f"年龄：{age}岁")
print(f"专业：{info['专业']}")
print(f"年级：{info['年级']}")
print(f"平均成绩：{average:.1f}分")
print(f"是否VIP：{'是' if info['VIP学员'] else '否'}")
print("=" * 30)
```

**运行结果：**

```
==============================
📋 学生报告
==============================
姓名：小明
年龄：20岁
专业：计算机科学
年级：大二
平均成绩：86.2分
是否VIP：是
==============================
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

| 概念 | 说明 |
|-----|------|
| 变量 | 给数据起的名字，像带标签的抽屉 |
| 整数（int） | 没有小数的数字：1、100、-5 |
| 浮点数（float） | 有小数的数字：3.14、19.99 |
| 字符串（str） | 用引号包起来的文字 |
| 布尔值（bool） | True（真）或 False（假） |
| 空值（None） | 表示"什么都没有" |
| 列表（list） | 一列数据，用索引存取 |
| 字典（dict） | 带名字的数据，用key存取 |
| 类型转换 | int()、str()、float() 互相转换 |

---

## 下节预告

下一篇我们将学习**运算符和表达式**，掌握Python中的数学运算和逻辑判断。

👉 **[继续阅读：Python运算符与表达式](./03-Python运算符与表达式.md)**

---

## 课程导航

**上一篇：** [Python零基础入门：写下你的第一行代码](./01-Python零基础入门.md)

**下一篇：** [Python运算符与表达式详解](./03-Python运算符与表达式.md)

---

*PS：理解数据类型是编程的基础。每种类型都有它的用武之地，多写几个例子练练手，后面的学习会轻松很多。*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)



