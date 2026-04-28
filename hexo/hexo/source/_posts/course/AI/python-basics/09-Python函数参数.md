---
title: Python函数参数*args和**kwargs：我面试挂3次后才搞懂的知识点
date: 2026-02-28 17:28:00
tags: [Python基础, 函数, 面试题]
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

先说一个我自己的黑历史。

当年面试一家大厂，面试官问我："Python函数参数`*args`和`**kwargs`是什么？有什么区别？"

我当场回答："就是...可以传多个参数的意思？"

面试官笑了笑，下一题。

后来我又挂了2次，才彻底把这个知识点搞明白。

如果你也被这两个星号搞晕过，这篇文章就是为你写的。**花10分钟，我用最通俗的方式，让你一次搞明白。**

---

## 从一个真实场景开始

假设你在写一个电商系统，需要处理订单。

### 场景：计算订单总价

你写了一个计算总和的函数：

```python
# ❌ 笨方法：参数写死
def total_price(p1, p2):
    return p1 + p2

# 问题：3个商品怎么办？重新写一个函数？
# 4个商品呢？继续写？
```

老板说："我们以后可能有100个商品打折！"

你陷入了沉思...

**这时候，*args 就登场了。**

```python
# ✅ 用 *args：参数数量不限
def total_price(*prices):
    total = 0
    for price in prices:
        total += price
    return total

print(total_price(100, 200))           # 300
print(total_price(50, 80, 120, 200))    # 450
print(total_price(10, 20, 30, 40, 50))  # 150
print(total_price())                     # 0（一个参数都没有也可以）
```

**一个函数，搞定所有情况！**

---

## 深入理解 *args

### args 到底是什么？

```python
def show_args(*args):
    # 看看 args 是什么类型
    print(f"类型：{type(args)}")
    print(f"内容：{args}")
    print(f"长度：{len(args)}")

show_args(1, 2, 3, 'hello', True)
```

**输出：**
```
类型：<class 'tuple'>
内容：(1, 2, 3, 'hello', True)
长度：5
```

**结论：`*args` 接收到的是一个元组（tuple）！**

这就是为什么：
- 你可以传任意多个参数
- 参数的顺序保持不变
- 长度可以动态变化

### 为什么要叫 args？

其实叫什么名字都行，约定俗成叫 `args`（arguments 的缩写，意思是"参数"）。

```python
# 叫什么都行，但大家约定叫 args
def foo(*numbers):
    return sum(numbers)

print(foo(1, 2, 3))  # 6

# 不推荐的命名（会误导自己）
def bar(*apple):
    print(apple)

bar(1, 2, 3)  # (1, 2, 3)
```

### *args 的典型用法

**1. 求最大值/最小值**
```python
def my_max(*numbers):
    return max(numbers)

print(my_max(3, 1, 4, 1, 5, 9, 2, 6))  # 9
```

**2. 拼接字符串**
```python
def join_words(*words, separator=' '):
    return separator.join(words)

print(join_words('Hello', 'World'))              # Hello World
print(join_words('a', 'b', 'c', separator='-'))   # a-b-c
```

**3. 注册回调函数**
```python
def register_handlers(*handlers):
    for handler in handlers:
        print(f"注册：{handler}")

register_handlers('on_click', 'on_hover', 'on_scroll')
# 注册：on_click
# 注册：on_hover
# 注册：on_scroll
```

---

## 深入理解 **kwargs

### kwargs 到底是什么？

```python
def show_kwargs(**kwargs):
    print(f"类型：{type(kwargs)}")
    print(f"内容：{kwargs}")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

show_kwargs(name='张三', age=28, city='重庆')
```

**输出：**
```
类型：<class 'dict'>
内容：{'name': '张三', 'age': 28, 'city': '重庆'}
  name = 张三
  age = 28
  city = 重庆
```

**结论：`**kwargs` 接收到的是一个字典（dict）！**

### kwargs 的典型用法

**1. 打印配置信息**
```python
def print_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

print_config(
    db_host='localhost',
    db_port=3306,
    db_name='myapp',
    debug=True
)
```

**2. 动态创建对象**
```python
class User:
    def __init__(self, name, age, **extra):
        self.name = name
        self.age = age
        self.extra = extra

user = User('程序员晚枫', 28, hobby='编程', city='重庆')
print(user.name)    # 程序员晚枫
print(user.extra)   # {'hobby': '编程', 'city': '重庆'}
```

**3. 转发参数给其他函数**
```python
def inner(a, b, c):
    print(f"inner: a={a}, b={b}, c={c}")

def outer(a, b, c, **kwargs):
    # 把 kwargs 传给 inner
    inner(a, b, c)
    if kwargs.get('debug'):
        print(f"调试信息：{kwargs}")

outer(1, 2, 3, debug=True)
```

---

## 四种参数类型：完整图谱

Python 函数的参数一共有 4 种类型，它们有严格的顺序要求：

```python
def func(普通参数, *args, 默认参数, **kwargs):
    pass
```

让我用图解说明：

```
def example(普通参数, *args, 默认参数=None, **kwargs):
               ↑          ↑         ↑          ↑
             必须传      可选     有默认值    可选
           位置传参    位置传多    可不传    关键字传多
```

### 4种参数同时出现的完整例子

```python
def full_example(position, *args, default='默认', **kwargs):
    print(f"普通参数 position = {position}")
    print(f"*args = {args}")
    print(f"默认参数 default = {default}")
    print(f"**kwargs = {kwargs}")

# 各种调用方式
print("=== 调用1 ===")
full_example(1, 2, 3, 4, 5, default='新值', x=10, y=20)

print("\n=== 调用2 ===")
full_example('唯一', debug=True)

print("\n=== 调用3 ===")
full_example(100)
```

**输出：**
```
=== 调用1 ===
普通参数 position = 1
*args = (2, 3, 4, 5)
默认参数 default = 新值
**kwargs = {'x': 10, 'y': 20}

=== 调用2 ===
普通参数 position = 唯一
*args = ()
默认参数 default = 默认
**kwargs = {'debug': True}

=== 调用3 ===
普通参数 position = 100
*args = ()
默认参数 default = 默认
**kwargs = {}
```

### 记忆口诀

> **先位置，后星号args，再默认，最后双星kwargs。**

```
def func(位置, *可变位置, 默认=值, **可变关键字):
    ...
```

---

## 常见错误与纠正

### 错误1：参数顺序写反

```python
# ❌ 错误写法
# def func(a=1, *args, b):  # SyntaxError: non-default argument follows default argument
#     pass

# ✅ 正确写法
def func(*args, b=2):
    print(args, b)

func(1, 2, 3, b=10)  # (1, 2, 3) 10
```

### 错误2：同一个参数传两次

```python
def func(a, *args, **kwargs):
    print(f"a={a}, args={args}, kwargs={kwargs}")

# ❌ 错误：同一个参数传了两次
# func(1, a=2)  # TypeError: func() got multiple values for argument 'a'

# ✅ 正确
func(1)
func(a=1)
```

### 错误3：拆包类型不匹配

```python
def func(a, b, c):
    print(a, b, c)

# ❌ 列表给 *args，但函数需要3个位置参数
numbers = [1, 2, 3, 4]
# func(numbers)  # TypeError: func() missing 2 required positional arguments

# ✅ 用 * 拆包
func(*numbers)  # 1 2 3（只取前3个）

# ✅ 字典给 **kwargs
info = {'a': 10, 'b': 20, 'c': 30}
func(**info)  # 10 20 30
```

---

## 解包操作：*和**的另一种用法

前面说的是定义函数时用 `*args` 和 `**kwargs`，**调用函数时**也可以用 `*` 和 `**` 来解包。

### 列表/元组解包：*

```python
def add_three(a, b, c):
    return a + b + c

# 从列表拆包
numbers = [1, 2, 3]
result = add_three(*numbers)  # 等价于 add_three(1, 2, 3)
print(result)  # 6

# 从元组拆包
coords = (10, 20, 30)
result = add_three(*coords)
print(result)  # 60

# 混合使用
base = [1, 2]
extra = [3, 4, 5]
combined = add_three(*base, 999)  # 1 + 2 + 999 = 1002
print(combined)
```

### 字典解包：**

```python
def greet(name, age, city='未知'):
    print(f"大家好，我是{name}，{age}岁，来自{city}")

# 从字典拆包
person = {'name': '程序员晚枫', 'age': 28, 'city': '重庆'}
greet(**person)  # 等价于 greet(name='程序员晚枫', age=28, city='重庆')

# 只传部分参数
basic_info = {'name': '小明', 'age': 18}
greet(**basic_info)  # city 用默认值

# 合并多个字典
defaults = {'city': '北京', 'job': '工程师'}
override = {'job': '产品经理', 'age': 30}
merged = {**defaults, **override}  # {'city': '北京', 'job': '产品经理', 'age': 30}
greet(**merged, name='老王')
```

### 解包在创建数据结构中的应用

```python
# 快速合并列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = [*list1, *list2]
print(merged)  # [1, 2, 3, 4, 5, 6]

# 快速合并字典（Python 3.9+）
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 20, 'c': 3}
merged_dict = {**dict1, **dict2}  # {'a': 1, 'b': 20, 'c': 3}
print(merged_dict)

# 集合解包
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = {*set1, *set2}
print(union)  # {1, 2, 3, 4, 5}
```

---

## 实战案例：通用日志装饰器

这是一个综合运用 `*args` 和 `**kwargs` 的真实案例——写一个日志装饰器，可以装饰任何函数：

```python
import time
from functools import wraps

def log(func):
    """记录函数调用日志"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用函数：{func.__name__}")
        print(f"       位置参数：{args}")
        print(f"       关键字参数：{kwargs}")
        
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        
        print(f"       返回值：{result}")
        print(f"       耗时：{elapsed:.4f}秒")
        return result
    
    return wrapper

# 应用装饰器
@log
def calculate_total(*items):
    """计算总价"""
    return sum(items)

@log
def fetch_user(user_id, include_profile=False, include_history=False):
    """获取用户信息"""
    return {'id': user_id, 'name': f'用户{user_id}'}

# 测试
print("=== 计算总价 ===")
total = calculate_total(100, 200, 300, 50)

print("\n=== 获取用户 ===")
user = fetch_user(123, include_profile=True)
```

**运行结果：**
```
=== 计算总价 ===
[LOG] 调用函数：calculate_total
       位置参数：(100, 200, 300, 50)
       关键字参数：{}
       返回值：650
       耗时：0.0001秒

=== 获取用户 ===
[LOG] 调用函数：fetch_user
       位置参数：(123,)
       关键字参数：{'include_profile': True, 'include_history': False}
       返回值：{'id': 123, 'name': '用户123'}
       耗时：0.0001秒
```

**这就是装饰器的核心原理——用 `*args` 和 `**kwargs` 接收任意参数，然后透传给原函数！**

---

## 实战案例：灵活的API调用函数

在实际工作中，`*args` 和 `**kwargs` 最常见的用法是**封装第三方API**，让你写的函数比官方接口更简洁：

```python
import requests

def api_get(url, **params):
    """
    封装 requests.get
    简化调用：不用每次写 timeout、headers 等
    """
    # 设置默认参数
    defaults = {
        'timeout': 5,
        'headers': {'User-Agent': 'MyApp/1.0'},
        'verify': True
    }
    # 用传入的参数覆盖默认参数
    defaults.update(params)
    
    print(f"请求 URL：{url}")
    print(f"参数：{defaults}")
    
    response = requests.get(url, **defaults)
    return response.json()

# 使用起来超级简洁
result = api_get(
    'https://api.example.com/users',
    params={'page': 1, 'limit': 10},
    timeout=10,
    headers={'Authorization': 'Bearer xxx'}
)
```

---

## 面试题详解

### 面试题1：下面的代码输出什么？

```python
def foo(a, *args, b=2, **kwargs):
    print(f"a = {a}")
    print(f"args = {args}")
    print(f"b = {b}")
    print(f"kwargs = {kwargs}")

foo(1, 3, 4, b=5, c=6, d=7)
```

**解析：**
- `a = 1` → 普通参数
- `args = (3, 4)` → 多余的位置参数被 *args 收集
- `b = 5` → 关键字参数，覆盖默认值 2
- `kwargs = {'c': 6, 'd': 7}` → 多余的关键字参数被 **kwargs 收集

**答案：**
```
a = 1
args = (3, 4)
b = 5
kwargs = {'c': 6, 'd': 7}
```

### 面试题2：`*args` 和 `**kwargs` 可以同时省略吗？

```python
# 可以省略其中一个
def func1(*args):
    print(args)

def func2(**kwargs):
    print(kwargs)

def func3():
    print("什么参数都不要")

# 也可以两个都省略
func1(1, 2, 3)      # (1, 2, 3)
func2(name='张三')  # {'name': '张三'}
func3()             # None
```

### 面试题3：装饰器中为什么必须用 `*args` 和 `**kwargs`？

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):  # ← 必须用，否则无法装饰带参数的函数
        print("装饰前")
        result = func(*args, **kwargs)  # ← 透传参数
        print("装饰后")
        return result
    return wrapper

@my_decorator
def greet(name, greeting="Hello"):
    """带有参数的函数"""
    print(f"{greeting}, {name}!")

greet("程序员晚枫", greeting="你好")
```

**如果不加 `*args` 和 `**kwargs`**，就无法装饰带参数的函数！

---

## 推荐：AI Python零基础实战营

想系统学习Python函数和高级特性，把面试题全部拿下？

**课程内容：**
- ✅ Python基础语法
- ✅ 函数详解（参数、返回值、作用域）
- ✅ *args和**kwargs深度解析
- ✅ 装饰器、生成器等高级特性
- ✅ 实战项目练习

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 本讲小结

| 概念 | 写法 | 接收内容 | 类型 |
|-----|------|---------|------|
| 位置可变参数 | `*args` | 任意多个位置参数 | tuple |
| 关键字可变参数 | `**kwargs` | 任意多个关键字参数 | dict |
| 参数解包 | `*序列` | 拆包列表/元组 | - |
| 字典解包 | `**字典` | 拆包字典为关键字参数 | - |

> 💡 **记忆口诀**：`*args` 收位置，`**kwargs` 收关键字，先位置后关键字，顺序千万别搞混！

---

## 相关阅读

- [Python列表推导式：一行代码搞定循环](/course/AI相关/人民邮电出版社/ads/openclaw/07-Python列表推导式/)
- [Python字典：我用这个数据结构，把查询速度提升了100倍](/course/AI相关/人民邮电出版社/ads/openclaw/08-Python字典/)
- [Python装饰器：给函数加功能的黑魔法](/course/AI相关/人民邮电出版社/ads/openclaw/11-Python装饰器/)

---

*PS：*args和**kwargs是Python面试必考点，也是写出优雅代码的关键。花10分钟搞懂，值！*

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


