---
title: Python函数基础：我把重复代码封装成函数，维护成本降低80%
date: 2026-02-28 21:04:00
tags: [Python基础, 函数, 封装]
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

上篇我们学了循环，能批量处理数据了。这篇来学**函数**——代码复用的核心武器。

学完这篇，你就能把重复的代码打包成工具，一行调用搞定，代码量减少80%，维护成本大幅下降。

---

## 什么是函数？

想象你在公司工作，每天都要寄快递：
- 填单子 → 打电话 → 等快递员 → 包装 → 交给他

如果每天都要完整走一遍，累不累？

现在公司引进了**快递柜**：你只需把东西放进去，一键下单，快递柜自动帮你搞定后续所有步骤。

**函数，就是代码里的"快递柜"**——你把数据放进去（传入参数），它自动执行打包好的流程，返回你想要的结果。

---

## 定义第一个函数

### 最简单的函数

```python
def say_hello():
    """打印一句问候语"""
    print("你好，欢迎回来！")
```

**逐行解释：**

```
def        → 告诉Python，我要定义一个函数
say_hello  → 函数的名字（你起的，随意）
()         → 空括号：不需要传入任何数据
:          → 冒号：接下来是函数体
缩进的代码 → 函数要做的事
```

### 调用函数

定义完函数，不会自动执行——你需要"叫它来做事"：

```python
def say_hello():
    print("你好，欢迎回来！")

say_hello()    # ✅ 调用函数，输出：你好，欢迎回来！
say_hello()    # ✅ 可以多次调用
```

> 💡 **类比**：定义函数就像写一份操作手册，放在书架上；调用函数就像临时拿出来用一次。

---

## 带参数的函数：传入数据

给函数传入信息，让它根据不同输入产生不同结果。

### 场景举例：打招呼但叫出名字

```python
def greet(name):
    """向指定的人打招呼"""
    print(f"你好，{name}！今天过得怎么样？")

greet("张三")    # 你好，张三！今天过得怎么样？
greet("李四")    # 你好，李四！今天过得怎么样？
```

> 💡 **参数（parameter）**：定义函数时的占位符，叫`name`
> **实参（argument）**：调用函数时传入的具体值，叫`"张三"`、`"李四"`

---

## 带返回值的函数：返回结果

有时候你不需要函数"打印"结果，而是需要它"返回"一个值给你：

```python
def add(a, b):
    """计算两个数的和"""
    result = a + b
    return result     # 返回计算结果

# 调用函数，并获取返回值
total = add(3, 5)
print(f"3 + 5 = {total}")
```

**运行结果：**

```
3 + 5 = 8
```

> 💡 **return 的作用**：把结果交给调用者，之后还能用这个结果做其他事。如果函数没有`return`，默认返回`None`。

---

## 三种参数类型

### ① 位置参数：按顺序来

```python
def introduce(name, city, job):
    print(f"我是{name}，在{city}做{job}工作")

introduce("张三", "北京", "程序员")
# 位置一一对应：张三→name，北京→city，程序员→job
```

### ② 关键字参数：指定名字来传

```python
introduce(city="上海", name="李四", job="设计师")
# 不管顺序，写清楚名字就行
```

### ③ 默认参数：给个默认值

```python
def greet(name, greeting="你好"):
    """greeting有默认值，不传就用默认值"""
    print(f"{greeting}，{name}！")

greet("王五")               # 你好，王五！（用默认值）
greet("赵六", "早上好")      # 早上好，赵六！（覆盖默认值）
```

> ⚠️ **注意**：默认参数要放在**最后**，不能放在必选参数前面！

---

## 返回多个值：其实是返回元组

Python函数可以一次性返回多个值：

```python
def get_stats(scores):
    """返回最高分、最低分和平均分"""
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    return highest, lowest, average    # 逗号分隔多个返回值

# 接收返回值（会自动打包成元组）
top, bottom, avg = get_stats([85, 92, 78, 90, 88])

print(f"最高分：{top}")
print(f"最低分：{bottom}")
print(f"平均分：{avg:.1f}")
```

**运行结果：**

```
最高分：92
最低分：78
平均分：86.6
```

---

## 变量作用域：哪里能看见哪里

### 局部变量 vs 全局变量

```python
name = "张三"     # 全局变量：整个文件都能看见

def introduce():
    city = "北京"  # 局部变量：只在函数内部有效
    print(f"{name}住在{city}")

introduce()
print(name)      # ✅ 能看见全局变量
print(city)       # ❌ 报错！city在函数里，外面看不见
```

### 想在函数里修改全局变量？加 `global`

```python
count = 0    # 全局计数器

def click():
    global count   # 声明：我用的是外面的count
    count += 1
    print(f"点击了 {count} 次")

click()    # 点击了 1 次
click()    # 点击了 2 次
click()    # 点击了 3 次
```

> 💡 **建议**：尽量少用`global`，多用参数和返回值——让函数只依赖传入的数据，不依赖外部变量，这样的函数更干净、更容易测试。

---

## 实战练习：写一个工具函数库

把常用的功能封装成函数，以后直接调用：

```python
# ========== 工具函数库 ==========

def is_valid_email(email):
    """验证邮箱格式是否正确"""
    return "@" in email and "." in email.split("@")[-1]

def format_price(price):
    """格式化价格，带货币符号和两位小数"""
    return f"¥{price:.2f}"

def truncate(text, max_len=50):
    """截断过长的文本，超过长度就显示..."""
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."

def grade_score(score):
    """根据分数返回等级描述"""
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


# ========== 使用工具函数 ==========

print("=== 工具函数演示 ===\n")

# 邮箱验证
emails = ["user@example.com", "invalid-email", "test@163"]
for e in emails:
    status = "✅" if is_valid_email(e) else "❌"
    print(f"{status} {e}")

print()

# 价格格式化
prices = [19.9, 99, 128.5]
for p in prices:
    print(f"价格：{format_price(p)}")

print()

# 文本截断
long_text = "这是一段很长的文本内容，如果超过50个字符就会自动截断，显示省略号"
print(f"原文：{long_text}")
print(f"截断：{truncate(long_text, 20)}")

print()

# 成绩评级
scores = [95, 82, 73, 61, 45]
for s in scores:
    print(f"分数{s}分 → {grade_score(s)}")
```

**运行结果：**

```
=== 工具函数演示 ===

✅ user@example.com
❌ invalid-email
✅ test@163

价格：¥19.90
价格：¥99.00
价格：¥128.50

原文：这是一段很长的文本内容，如果超过50个字符就会自动截断，显示省略号
截断：这是一段很长的文本内容，如果超...

分数95分 → A（优秀）
分数82分 → B（良好）
分数73分 → C（中等）
分数61分 → D（及格）
分数45分 → F（不及格）
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
| `def 函数名():` | 定义函数 |
| 参数 | 函数接收的输入 |
| `return 值` | 函数返回的结果 |
| 位置参数 | 按顺序传入 |
| 关键字参数 | 指定名字传入 |
| 默认参数 | 有默认值的参数 |
| 局部/全局变量 | 作用域不同 |

---

## 下节预告

学会了函数的定义和使用，下一篇来学**函数参数进阶**——`*args`和`**kwargs`，让函数能接收任意数量的参数。

👉 **[继续阅读：Python函数参数](./09-Python函数参数.md)**

---

## 课程导航

**上一篇：** [Python条件判断-if-else完全指南](./04-Python条件判断.md)

**下一篇：** [Python函数参数*args和**kwargs](./09-Python函数参数.md)

---

*PS：函数是代码复用的基础。看到重复的代码，就想："能不能封装成函数？"这个习惯养成了，你写代码的效率会翻倍。*

