---
title: "Python 装饰器深度解读：从入门到精通的 5 个层次"
date: 2026-06-20 18:04:29
tags: ["Python", "装饰器", "AI工具", "公众号文章"]
categories: ["公众号文章"]
description: "Python 装饰器深度解读：从入门到精通的 5 个层次，让你彻底掌握 Python 装饰器"
cover: https://images.unsplash.com/photo-1526379095098-d400fd0bf935?q=80&w=1200&auto=format&fit=crop
---

大家好，我是程序员晚枫。

**Python 装饰器，新手的"拦路虎"，老手的"瑞士军刀"。**

**今天这篇文章，给你 5 个层次，让你彻底掌握。**

---

## 一、什么是装饰器？

**装饰器 = 给函数穿"衣服"，不改函数本身，但能让它多些能力**。

### 通俗解释

**人穿衣**：

- 你（函数）+ 外套（装饰器）= 穿了外套的你
- 你还是你，但多了保暖功能

**函数装装饰器**：

```python
@my_decorator
def my_func():
    pass
```

**等价于**：

```python
def my_func():
    pass
my_func = my_decorator(my_func)
```

**装饰器就是"包装函数"的函数**。

---

## 二、层次 1：基础装饰器

### 第 1 个装饰器

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Before
# Hello!
# After
```

### 5 大要点

#### 要点 1：装饰器是高阶函数

**接受函数，返回函数**：

```python
def my_decorator(func):  # 接受函数
    def wrapper():  # 定义新函数
        return func()  # 调用原函数
    return wrapper  # 返回新函数
```

#### 要点 2：@ 语法糖

```python
@my_decorator
def my_func():
    pass
```

**等价于**：

```python
def my_func():
    pass
my_func = my_decorator(my_func)
```

#### 要点 3：装饰器不改变原函数

**原函数还在**，**只是被"包装"了**。

#### 要点 4：装饰器可以叠加

```python
@decorator_a
@decorator_b
def my_func():
    pass
# 装饰顺序：a 在外，b 在内
```

#### 要点 5：装饰器可以用 functools.wraps

**保留原函数元信息**：

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func()
    return wrapper
```

---

## 三、层次 2：带参数的装饰器

### 普通装饰器的问题

```python
@my_decorator
def add(x, y):
    return x + y
```

**装饰器怎么接收 x, y**？

### 解决方案：三层嵌套

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"Got {result}")
        return result
    return wrapper

@my_decorator
def add(x, y):
    return x + y

add(2, 3)
# Calling add with (2, 3)
# Got 5
```

**`*args, **kwargs` 接收所有参数**。

---

## 四、层次 3：带参数的装饰器（外层）

### 场景

**不同函数要不同"装饰"**：

```python
@repeat(3)  # 重复 3 次
def hello():
    print("Hello!")

@repeat(5)  # 重复 5 次
def goodbye():
    print("Goodbye!")
```

### 实现：4 层嵌套

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello!")

hello()  # 打印 3 次 Hello!
```

### 4 层结构

```python
# 1. 外层（接收装饰器参数）
def repeat(times):
    # 2. 装饰器（接收函数）
    def decorator(func):
        # 3. 包装器（接收函数参数）
        def wrapper(*args, **kwargs):
            # 4. 调用
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

---

## 五、层次 4：类装饰器

### 装饰类的装饰器

```python
def singleton(cls):
    instances = {}
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Database:
    pass

db1 = Database()
db2 = Database()
print(db1 is db2)  # True（同一个实例）
```

### 类作为装饰器

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def hello():
    print("Hello!")

hello()  # Call 1 of hello
hello()  # Call 2 of hello
```

**类装饰器可以**保存状态**（如调用次数）**。

---

## 六、层次 5：内置装饰器

### Python 内置的常用装饰器

#### 1. @property

**将方法转为属性**：

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area)  # 78.5（不用 c.area()）
```

#### 2. @staticmethod

**静态方法**：

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(2, 3))  # 5（不用实例化）
```

#### 3. @classmethod

**类方法**：

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def from_string(cls, s):
        name, age = s.split('-')
        return cls(name)

p = Person.from_string('Alice-30')
```

#### 4. @functools.lru_cache

**缓存函数结果**：

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

fib(35)  # 0.0001 秒
```

#### 5. @dataclasses.dataclass

**自动生成 `__init__`**：

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

user = User('Alice', 30)  # 自动生成 __init__
```

---

## 七、5 大常用装饰器模式

### 模式 1：日志装饰器

```python
import functools
import time

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f}s")
        return result
    return wrapper
```

### 模式 2：缓存装饰器

```python
def cache(func):
    cached = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cached:
            cached[args] = func(*args)
        return cached[args]
    return wrapper
```

### 模式 3：重试装饰器

```python
import time

def retry(times=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == times - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator
```

### 模式 4：权限装饰器

```python
def require_login(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise PermissionError("请先登录")
        return func(user, *args, **kwargs)
    return wrapper
```

### 模式 5：缓存属性

```python
class CachedProperty:
    def __init__(self, func):
        self.func = func
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        attr = f'_cached_{self.func.__name__}'
        if not hasattr(instance, attr):
            setattr(instance, attr, self.func(instance))
        return getattr(instance, attr)
```

---

## 八、5 大真实项目案例

### 案例 1：Flask 路由

```python
@app.route('/')
def home():
    return 'Hello, World!'
```

**Flask 用装饰器定义路由**。

### 案例 2：Django 视图

```python
@login_required
def profile(request):
    return render(request, 'profile.html')
```

**Django 用装饰器实现登录验证**。

### 案例 3：pytest 测试

```python
@pytest.fixture
def user():
    return User('Alice')

def test_user(user):
    assert user.name == 'Alice'
```

**pytest 用装饰器定义 fixture**。

### 案例 4：click CLI

```python
import click

@click.command()
@click.option('--name', default='World')
def hello(name):
    click.echo(f'Hello {name}!')
```

**click 用装饰器定义命令行参数**。

### 案例 5：functools

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def expensive_function(n):
    # 计算
    return n ** 2
```

**functools 用装饰器缓存**。

---

## 九、5 大常见误区

### 误区 1：装饰器改变原函数

- ❌ 错
- ✅ **只是包装，不改变**

### 误区 2：忘记 functools.wraps

- ⚠️ 常见错
- ✅ **必须用**，保留元信息

### 误区 3：装饰器无法接受参数

- ❌ 错
- ✅ **4 层嵌套可以**

### 误区 4：装饰器 = 性能优化

- ❌ 错
- ✅ 装饰器是**结构**，不优化性能

### 误区 5：装饰器很难

- ⚠️ 部分对
- ✅ 概念多
- **掌握 5 个层次就够**

---

## 十、5 个学习路径

### 路径 1：完全新手

```
基础装饰器（3 天）→ 带参数装饰器（3 天）→ 简单项目
```

### 路径 2：Web 开发者

```
Flask/Django 装饰器（1 周）→ 自定义装饰器（2 周）→ 实战
```

### 路径 3：测试驱动

```
pytest fixture（1 周）→ 自定义 fixture（1 周）→ 实战
```

### 路径 4：AI 工程师

```
functools.lru_cache（1 周）→ 异步装饰器（1 周）→ 模型部署
```

### 路径 5：库开发者

```
类装饰器（1 周）→ 元类（1 周）→ 高级装饰器（2 周）
```

---

## 十一、给 Python 装饰器学习者的 4 个建议

### 建议 1：先学基础

- 不带参数装饰器
- **1 周搞定**

### 建议 2：再学带参数

- 4 层嵌套
- **3 天搞定**

### 建议 3：用 functools.wraps

- **保留元信息**
- 必须用

### 建议 4：多看内置装饰器

- @property、@staticmethod
- **理解原理**

---

## 十二、最后的最后

**Python 装饰器，3 句话总结**：

1. **5 个层次**：基础→带参数→外层参数→类→内置
2. **本质是函数包装**：不改原函数
3. **用 functools.wraps**：保留元信息

**学 Python 6 年，我学到的最重要的事：**

**"装饰器是 Python 高级编程的'分水岭'。"**

**掌握装饰器，**你看代码的眼光都不一样**。**

**Flask、Django、pytest、click 全是装饰器。**

**学装饰器，**5 年后你看 Python 框架如看"自己写的代码"**。**

---

## 相关阅读

- [2026 年学习编程，你需要的不是更多教程](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)
- [🖊️ 想做视频号 / 抖音 / 小红书？AI 帮你一键生成，不用学剪辑，免费试用 3 次](https://www.liblib.tv/?sourceid=005902&utm=cg&cgv=9omkl4jn4d)
- [🎁 国产 CodeX AI 办公助手 | 写方案/PPT/分析 一次搞定](https://www.codebuddy.cn/events/invite?inviteCode=bflfcx96gj)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [我开通了Google广告，把申请到收款的全流程教给你](https://mp.weixin.qq.com/s/scAleVOwH6kDLPuQT4BNlA)
- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT Plus 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)

---

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《50讲 · AI编程训练营》](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲，先看看适不适合自己](https://pan.quark.cn/s/8f7886f79569)
- 👉 - 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/3978Ig)
