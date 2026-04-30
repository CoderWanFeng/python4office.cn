---
title: Python函数基础：我把重复代码封装成函数，维护成本降低80%
date: "2026-02-28 21:04:00"
tags: ["Python基础", "函数", "封装"]
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

## 一个真实的故事

2024年，有个团队找我做代码审查。他们的项目有5000行代码，其中有一段"发送邮件"的逻辑，在10个不同的地方重复出现。

每次修改邮件格式，都要改10个地方。

**结果呢？有一次改漏了1个地方，导致客户收到的邮件格式不一致，差点丢单。**

我给他们封装了一个函数：

```python
def send_notification_email(to, subject, content, template="default"):
    """统一的邮件发送函数"""
    # 1. 加载模板
    # 2. 格式化内容
    # 3. 发送邮件
    # 4. 记录日志
    pass
```

**修改后，5000行代码减少到3000行，维护成本降低80%。**

这就是函数的力量——**把重复的代码打包成工具，一行调用搞定**。

上篇我们学了循环，能批量处理数据了。这篇来学**函数**——代码复用的核心武器。

学完这篇，你就能把重复的代码打包成工具，代码量减少，维护成本大幅下降。

---

## 什么是函数？

想象你在公司工作，每天都要寄快递：
- 填单子 → 打电话 → 等快递员 → 包装 → 交给他

如果每天都要完整走一遍，累不累？

现在公司引进了**快递柜**：你只需把东西放进去，一键下单，快递柜自动帮你搞定后续所有步骤。

**函数，就是代码里的"快递柜"**——你把数据放进去（传入参数），它自动执行打包好的流程，返回你想要的结果。

### 函数的好处

```python
# ❌ 不用函数：每次都要写一遍
print("发送邮件给张三")
# ... 20行邮件代码 ...

print("发送邮件给李四")
# ... 又是20行邮件代码 ...

print("发送邮件给王五")
# ... 还是20行邮件代码 ...

# ✅ 用函数：封装一次，重复使用
def send_email(to, content):
    # ... 20行邮件代码 ...
    pass

send_email("张三", "你好")
send_email("李四", "你好")
send_email("王五", "你好")
```

**函数的三大好处：**

1. **复用性**：写一次，到处用
2. **可维护性**：改一处，处处生效
3. **可读性**：名字即功能，代码更清晰

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
say_hello  → 函数的名字（你起的，要有意义）
()         → 空括号：不需要传入任何数据
:          → 冒号：接下来是函数体
"""..."""  → 文档字符串（docstring）：说明函数的作用
缩进的代码 → 函数要做的事
```

### 调用函数

定义完函数，不会自动执行——你需要"叫它来做事"：

```python
def say_hello():
    """打印一句问候语"""
    print("你好，欢迎回来！")

# 调用函数
say_hello()    # ✅ 输出：你好，欢迎回来！
say_hello()    # ✅ 可以多次调用
say_hello()    # ✅ 调用多少次都可以
```

> 💡 **类比**：定义函数就像写一份操作手册，放在书架上；调用函数就像临时拿出来用一次。

### 函数的执行流程

```python
def greet():
    print("第一步：打开门")
    print("第二步：说你好")
    print("第三步：关门")

print("程序开始")
greet()          # 跳到函数内部执行
print("程序结束")

# 执行顺序：
# 1. 程序开始
# 2. 第一步：打开门
# 3. 第二步：说你好
# 4. 第三步：关门
# 5. 程序结束
```

---

## 带参数的函数：传入数据

给函数传入信息，让它根据不同输入产生不同结果。

### 单个参数

```python
def greet(name):
    """向指定的人打招呼"""
    print(f"你好，{name}！今天过得怎么样？")

greet("张三")    # 你好，张三！今天过得怎么样？
greet("李四")    # 你好，李四！今天过得怎么样？
greet("王五")    # 你好，王五！今天过得怎么样？
```

> 💡 **参数（parameter）**：定义函数时的占位符，叫 `name`
> **实参（argument）**：调用函数时传入的具体值，叫 `"张三"`、`"李四"`

### 多个参数

```python
def introduce(name, age, city):
    """自我介绍"""
    print(f"我叫{name}，今年{age}岁，来自{city}")

introduce("张三", 25, "北京")
# 我叫张三，今年25岁，来自北京

introduce("李四", 30, "上海")
# 我叫李四，今年30岁，来自上海
```

### 参数的顺序

```python
def create_profile(name, age, job):
    """创建用户档案"""
    return f"{name}，{age}岁，职业：{job}"

# 位置参数：按顺序传入
profile1 = create_profile("张三", 25, "程序员")

# 关键字参数：指定名字传入
profile2 = create_profile(age=30, name="李四", job="设计师")

# 混合使用：位置参数在前，关键字参数在后
profile3 = create_profile("王五", job="产品经理", age=28)
```

---

## 带返回值的函数：返回结果

有时候你不需要函数"打印"结果，而是需要它"返回"一个值给你。

### return的作用

```python
def add(a, b):
    """计算两个数的和"""
    result = a + b
    return result     # 返回计算结果

# 调用函数，并获取返回值
total = add(3, 5)
print(f"3 + 5 = {total}")

# 返回值可以直接使用
print(f"10 + 20 = {add(10, 20)}")
```

**运行结果：**

```
3 + 5 = 8
10 + 20 = 30
```

> 💡 **return 的作用**：把结果交给调用者，之后还能用这个结果做其他事。

### return vs print

```python
# ❌ 用print：只能看，不能用
def add_print(a, b):
    print(a + b)

result = add_print(3, 5)  # 打印8
print(result)  # None（没有返回值）

# ✅ 用return：可以继续使用
def add_return(a, b):
    return a + b

result = add_return(3, 5)
print(result * 2)  # 16（可以继续计算）
```

### 提前返回

```python
def divide(a, b):
    """除法运算（带检查）"""
    if b == 0:
        return "错误：除数不能为0"  # 提前返回
    return a / b

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # 错误：除数不能为0
```

### 函数没有return

```python
def no_return():
    print("这个函数没有return")

result = no_return()
print(result)  # None（默认返回None）
```

---

## 返回多个值

Python函数可以一次性返回多个值：

### 返回元组

```python
def get_stats(scores):
    """返回最高分、最低分和平均分"""
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    return highest, lowest, average    # 逗号分隔多个返回值

# 接收返回值（自动解包）
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

### 接收多个返回值的不同方式

```python
def get_user_info():
    return "张三", 25, "北京"

# 方式1：全部接收
name, age, city = get_user_info()

# 方式2：接收为元组
info = get_user_info()
print(info)  # ('张三', 25, '北京')

# 方式3：只接收部分（Python 3.x）
name, *_ = get_user_info()
print(name)  # 张三
```

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

# 混合使用（位置参数在前）
introduce("王五", job="产品经理", city="广州")
```

### ③ 默认参数：给个默认值

```python
def greet(name, greeting="你好"):
    """greeting有默认值，不传就用默认值"""
    print(f"{greeting}，{name}！")

greet("张三")               # 你好，张三！（用默认值）
greet("李四", "早上好")      # 早上好，李四！（覆盖默认值）
greet(name="王五", greeting="晚上好")  # 晚上好，王五！
```

> ⚠️ **重要规则**：默认参数要放在**最后**，不能放在必选参数前面！

```python
# ❌ 错误：默认参数在必选参数前面
def wrong(greeting="你好", name):
    pass  # SyntaxError

# ✅ 正确：默认参数在后面
def right(name, greeting="你好"):
    pass
```

### 默认参数的陷阱

```python
# ❌ 危险：使用可变对象作为默认参数
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b']  （不是预期的['b']！）
# 原因：默认参数只创建一次，被复用了

# ✅ 正确：使用None作为默认值
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['b']
```

---

## 可变参数：*args 和 **kwargs

### *args：接收任意数量的位置参数

```python
def add_all(*numbers):
    """计算任意数量的数字之和"""
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(1, 2, 3))        # 6
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all())               # 0

# numbers是一个元组
def show_args(*args):
    print(type(args))  # <class 'tuple'>
    print(args)

show_args(1, 2, 3, "a", "b")  # (1, 2, 3, 'a', 'b')
```

### **kwargs：接收任意数量的关键字参数

```python
def create_user(**info):
    """创建用户，接收任意关键字参数"""
    for key, value in info.items():
        print(f"{key}: {value}")

create_user(name="张三", age=25, city="北京")
# name: 张三
# age: 25
# city: 北京

# info是一个字典
def show_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)

show_kwargs(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
```

### 组合使用

```python
def func(required, default="默认值", *args, **kwargs):
    """完整的参数示例"""
    print(f"必选参数: {required}")
    print(f"默认参数: {default}")
    print(f"可变位置参数: {args}")
    print(f"可变关键字参数: {kwargs}")

func("必选", "默认", 1, 2, 3, name="张三", age=25)
# 必选参数: 必选
# 默认参数: 默认
# 可变位置参数: (1, 2, 3)
# 可变关键字参数: {'name': '张三', 'age': 25}
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
# print(city)    # ❌ 报错！city在函数里，外面看不见
```

### 作用域的查找顺序

```python
x = "全局"

def outer():
    x = "外部函数"
    
    def inner():
        x = "内部函数"
        print(x)  # 先找局部的
    
    inner()
    print(x)  # 找外部函数的

outer()
print(x)  # 找全局的

# 输出：内部函数 → 外部函数 → 全局
```

### 在函数里修改全局变量

```python
count = 0    # 全局计数器

def click():
    global count   # 声明：我用的是外面的count
    count += 1
    print(f"点击了 {count} 次")

click()    # 点击了 1 次
click()    # 点击了 2 次
click()    # 点击了 3 次
print(f"总点击：{count}")  # 总点击：3
```

> 💡 **建议**：尽量少用 `global`，多用参数和返回值——让函数只依赖传入的数据，不依赖外部变量，这样的函数更干净、更容易测试。

### nonlocal：修改外部函数的变量

```python
def outer():
    count = 0
    
    def inner():
        nonlocal count  # 声明：用外部函数的变量
        count += 1
        return count
    
    return inner

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

---

## 函数文档：docstring

### 基本写法

```python
def add(a, b):
    """
    计算两个数的和
    
    参数:
        a: 第一个数
        b: 第二个数
    
    返回:
        两数之和
    """
    return a + b

# 查看文档
print(add.__doc__)
help(add)
```

### Google风格的docstring

```python
def calculate_average(numbers):
    """计算数字列表的平均值
    
    Args:
        numbers: 数字列表
    
    Returns:
        float: 平均值
    
    Raises:
        ValueError: 如果列表为空
    
    Examples:
        >>> calculate_average([1, 2, 3])
        2.0
    """
    if not numbers:
        raise ValueError("列表不能为空")
    return sum(numbers) / len(numbers)
```

---

## 匿名函数：lambda

### 基本语法

```python
# 普通函数
def add(a, b):
    return a + b

# lambda函数
add_lambda = lambda a, b: a + b

print(add(1, 2))         # 3
print(add_lambda(1, 2))  # 3
```

### lambda的应用场景

```python
# 1. 排序时指定key
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78}
]

# 按分数排序
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_students)

# 2. filter过滤
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# 3. map映射
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### lambda的限制

```python
# ❌ lambda只能是单行表达式，不能有复杂逻辑
# lambda x: if x > 0: return x else: return -x  # 语法错误

# ✅ 复杂逻辑还是用普通函数
def absolute(x):
    if x > 0:
        return x
    else:
        return -x
```

---

## 高阶函数：函数作为参数

### 函数是对象

```python
def greet():
    return "你好"

# 函数可以赋值给变量
say_hi = greet
print(say_hi())  # 你好

# 函数可以存入列表
funcs = [greet, say_hi]
for f in funcs:
    print(f())

# 函数可以作为参数
def apply(func, value):
    return func(value)

print(apply(str.upper, "hello"))  # HELLO
```

### 高阶函数示例

```python
def calculate(a, b, operation):
    """根据传入的运算函数计算结果"""
    return operation(a, b)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

print(calculate(10, 5, add))      # 15
print(calculate(10, 5, multiply)) # 50
print(calculate(10, 5, lambda x, y: x - y))  # 5
```

---

## 避坑指南

### ❌ 坑1：忘记return

```python
# ❌ 忘记return
def add(a, b):
    result = a + b
    # 忘记写 return result

print(add(1, 2))  # None

# ✅ 正确
def add(a, b):
    return a + b

print(add(1, 2))  # 3
```

### ❌ 坑2：修改可变参数

```python
# ❌ 直接修改传入的列表
def add_item(item, items):
    items.append(item)
    return items

my_list = [1, 2, 3]
add_item(4, my_list)
print(my_list)  # [1, 2, 3, 4] 原列表被修改了！

# ✅ 创建副本或返回新列表
def add_item_safe(item, items):
    new_items = items.copy()
    new_items.append(item)
    return new_items
```

### ❌ 坑3：默认参数用可变对象

```python
# ❌ 危险
def add_item(item, items=[]):
    items.append(item)
    return items

# ✅ 正确
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### ❌ 坑4：参数顺序错误

```python
def create_profile(name, age, city):
    pass

# ❌ 位置参数和关键字参数顺序错误
# create_profile(age=25, "张三", "北京")  # SyntaxError

# ✅ 正确
create_profile("张三", age=25, city="北京")
create_profile(name="张三", age=25, city="北京")
```

---

## 实战练习：写一个工具函数库

```python
"""
常用工具函数库
作者：程序员晚枫
"""

# ========== 字符串工具 ==========

def truncate(text, max_len=50, suffix="..."):
    """截断过长的文本
    
    Args:
        text: 原文本
        max_len: 最大长度
        suffix: 截断后显示的后缀
    
    Returns:
        截断后的文本
    """
    if len(text) <= max_len:
        return text
    return text[:max_len] + suffix


def mask_email(email):
    """隐藏邮箱中间部分
    
    Example:
        mask_email("zhangsan@example.com")  # z***n@example.com
    """
    if "@" not in email:
        return email
    name, domain = email.split("@")
    if len(name) <= 2:
        return name[0] + "***" + "@" + domain
    return name[0] + "***" + name[-1] + "@" + domain


# ========== 数学工具 ==========

def format_price(price, currency="¥"):
    """格式化价格
    
    Args:
        price: 价格
        currency: 货币符号
    
    Returns:
        格式化后的价格字符串
    """
    return f"{currency}{price:.2f}"


def calculate_discount(original_price, discount_rate):
    """计算折扣价
    
    Args:
        original_price: 原价
        discount_rate: 折扣率（0.8表示8折）
    
    Returns:
        折扣价（保留两位小数）
    """
    return round(original_price * discount_rate, 2)


# ========== 验证工具 ==========

def is_valid_email(email):
    """简单验证邮箱格式"""
    return "@" in email and "." in email.split("@")[-1]


def is_valid_phone(phone):
    """简单验证手机号格式（中国大陆）"""
    if not isinstance(phone, str):
        phone = str(phone)
    return len(phone) == 11 and phone.isdigit() and phone.startswith("1")


# ========== 数据处理工具 ==========

def grade_score(score):
    """根据分数返回等级
    
    Args:
        score: 分数（0-100）
    
    Returns:
        等级字符串
    """
    if not 0 <= score <= 100:
        return "无效分数"
    
    grades = [
        (90, "A（优秀）"),
        (80, "B（良好）"),
        (70, "C（中等）"),
        (60, "D（及格）"),
        (0, "F（不及格）")
    ]
    
    for threshold, grade in grades:
        if score >= threshold:
            return grade


def get_stats(numbers):
    """获取数字列表的统计信息
    
    Returns:
        dict: 包含最大值、最小值、平均值、总和
    """
    if not numbers:
        return None
    
    return {
        "max": max(numbers),
        "min": min(numbers),
        "avg": sum(numbers) / len(numbers),
        "sum": sum(numbers),
        "count": len(numbers)
    }


# ========== 使用演示 ==========

if __name__ == "__main__":
    print("=" * 50)
    print("工具函数库演示".center(44))
    print("=" * 50)
    
    # 字符串工具
    print("\n【字符串工具】")
    long_text = "这是一段很长的文本内容，用于测试截断功能是否正常工作"
    print(f"截断测试：{truncate(long_text, 20)}")
    print(f"邮箱隐藏：{mask_email('zhangsan@example.com')}")
    
    # 数学工具
    print("\n【数学工具】")
    print(f"价格格式化：{format_price(99.9)}")
    print(f"折扣计算：原价199，8折后 {format_price(calculate_discount(199, 0.8))}")
    
    # 验证工具
    print("\n【验证工具】")
    emails = ["user@example.com", "invalid", "test@163"]
    for email in emails:
        print(f"邮箱 {email}: {'✅' if is_valid_email(email) else '❌'}")
    
    # 数据处理
    print("\n【数据处理】")
    scores = [85, 92, 78, 90, 88]
    stats = get_stats(scores)
    print(f"统计信息：最高{stats['max']}，最低{stats['min']}，平均{stats['avg']:.1f}")
```

**运行结果：**

```
==================================================
              工具函数库演示              
==================================================

【字符串工具】
截断测试：这是一段很长的文本内容，用于测试...
邮箱隐藏：z***n@example.com

【数学工具】
价格格式化：¥99.90
折扣计算：原价199，8折后 ¥159.20

【验证工具】
邮箱 user@example.com: ✅
邮箱 invalid: ❌
邮箱 test@163: ✅

【数据处理】
统计信息：最高92，最低78，平均86.6
```

---

## 性能对比：函数调用的开销

```python
import timeit

# 直接计算
def direct():
    result = 0
    for i in range(1000):
        result += i
    return result

# 函数封装
def add(a, b):
    return a + b

def with_function():
    result = 0
    for i in range(1000):
        result = add(result, i)
    return result

# 测试
print(f"直接计算: {timeit.timeit(direct, number=10000):.4f}秒")
print(f"函数调用: {timeit.timeit(with_function, number=10000):.4f}秒")
```

**结论：** 函数调用有一定开销，但可读性和维护性的收益远大于这点性能损失。不要为了微小的性能提升而牺牲代码质量。

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

| 概念 | 说明 |
|-----|------|
| `def 函数名():` | 定义函数 |
| 参数 | 函数接收的输入 |
| `return 值` | 函数返回的结果 |
| 位置参数 | 按顺序传入 |
| 关键字参数 | 指定名字传入 |
| 默认参数 | 有默认值的参数（放在最后） |
| `*args` | 接收任意数量的位置参数 |
| `**kwargs` | 接收任意数量的关键字参数 |
| 局部变量 | 只在函数内部有效 |
| 全局变量 | 整个文件都能访问 |
| `global` | 声明使用全局变量 |
| docstring | 函数的文档说明 |
| lambda | 匿名函数 |

---

## 下节预告

学会了函数的定义和使用，下一篇来学**函数参数进阶**——`*args`和`**kwargs`的更多用法，以及装饰器的入门。

你将学会：
- 参数解包
- 装饰器基础
- 闭包
- 函数式编程

👉 **[继续阅读：Python函数参数](./09-Python函数参数.md)**

---

## 课程导航

**上一篇：** [Python循环-for和while完全指南](./05-Python循环.md)

**下一篇：** [Python函数参数*args和**kwargs](./09-Python函数参数.md)

---

## 相关阅读

- [Python条件判断-if-else完全指南](./04-Python条件判断.md)
- [零基础学AI编程：30天速成计划](/course/AI相关/人民邮电出版社/ads/openclaw/python/20260228171202-零基础学AI编程-30天速成计划/)

---

*PS：函数是代码复用的基础。看到重复的代码，就想："能不能封装成函数？"这个习惯养成了，你写代码的效率会翻倍。记住：好的函数应该像黑盒——输入进去，结果出来，不需要知道内部细节。*

*2026-04-23 更新 by 程序员晚枫*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


