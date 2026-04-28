---
title: Python装饰器：我给函数加了计时功能，代码只多了2行
date: 2026-02-28 17:30:00
tags: [Python基础, 装饰器, 高级特性]
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

今天聊一个让Python代码瞬间变高级的特性——**装饰器（Decorator）**。

第一次听说这个词时，我以为是什么高深的东西。后来才发现，它就像给手机贴膜一样简单：**在不改变原函数的情况下，给它加上新功能。**

而且，面试必问。

看完这篇文章，你也能写出带@符号的"高端代码"。

---

## 从一个真实需求开始

假设你写了10个函数，老板说："给每个函数加个计时功能，我要知道每个函数跑了多久。"

### ❌ 笨方法：每个函数都手动加

```python
import time

def func1():
    start = time.time()
    # ... 原来的代码 ...
    time.sleep(0.1)
    # ... 原来的代码 ...
    print(f"func1 耗时：{time.time() - start}秒")

def func2():
    start = time.time()
    # ... 原来的代码 ...
    time.sleep(0.2)
    # ... 原来的代码 ...
    print(f"func2 耗时：{time.time() - start}秒")

def func3():
    start = time.time()
    # ... 原来的代码 ...
    time.sleep(0.15)
    # ... 原来的代码 ...
    print(f"func3 耗时：{time.time() - start}秒")

# func4... func10 还要继续重复...
```

**缺点：**
- 代码重复
- 维护困难
- 改一个漏一个
- 违反DRY原则（Don't Repeat Yourself）

### ✅ 聪明方法：用装饰器

```python
import time

# 定义一个装饰器
def timer(func):
    def wrapper():
        start = time.time()
        result = func()          # 调用原函数
        elapsed = time.time() - start
        print(f"{func.__name__} 耗时：{elapsed:.4f}秒")
        return result
    return wrapper

# 给函数加上装饰器（只需要一个 @）
@timer
def func1():
    time.sleep(0.1)
    return "func1完成"

@timer
def func2():
    time.sleep(0.2)
    return "func2完成"

@timer
def func3():
    time.sleep(0.15)
    return "func3完成"

# 调用 —— 完全不用改！
func1()
func2()
func3()
```

**运行结果：**
```
func1 耗时：0.1002秒
func2 耗时：0.2001秒
func3 耗时：0.1503秒
```

**你只加了一个 @，每个函数就自动拥有了计时功能！**

---

## 装饰器原理：其实就是一个函数

不要被 @ 符号吓到，装饰器的本质就是一个**接收函数作为参数，返回新函数的函数**。

### 拆解装饰器的执行过程

```python
def my_decorator(func):
    """这是一个装饰器"""
    def wrapper():
        print("🔔 函数执行前")
        func()           # 调用原函数
        print("🔔 函数执行后")
    return wrapper

# 不使用 @ 的写法（等价于下面的 @ 写法）
def say_hello():
    print("Hello!")

# 等价于：say_hello = my_decorator(say_hello)
say_hello()

print("--- 分割线 ---")

# 使用 @ 的写法（推荐）
@my_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye()
```

**输出：**
```
🔔 函数执行前
Hello!
🔔 函数执行后
--- 分割线 ---
🔔 函数执行前
Goodbye!
🔔 函数执行后
```

**@ 就是语法糖，让代码更优雅！**

### 图解装饰器原理

```
原始函数：say_hello
              ↓
装饰器 my_decorator(say_hello)
              ↓
新函数 wrapper（包含前后增强）
              ↓
say_hello 变量指向 wrapper

再次调用 say_hello() 时，
实际调用的是 wrapper()
```

---

## 带参数的装饰器（必须掌握）

上面的装饰器有个问题：**如果原函数有参数怎么办？**

```python
# ❌ 无参数版装饰器，不能用在有参数的函数上
def timer(func):
    def wrapper():
        start = time.time()
        func()  # 如果原函数需要参数，这里会报错！
        print(f"耗时：{time.time() - start}秒")
    return wrapper

@timer
def greet(name):  # ❌ 会报错！
    print(f"Hello, {name}!")
```

### ✅ 万能参数版装饰器

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):  # ← 关键：接收任意参数
        start = time.time()
        result = func(*args, **kwargs)  # ← 透传给原函数
        elapsed = time.time() - start
        print(f"{func.__name__} 耗时：{elapsed:.4f}秒")
        return result
    return wrapper

# 现在可以装饰任意参数的函数了！
@timer
def slow_add(a, b):
    time.sleep(1)
    return a + b

@timer
def slow_greet(name, greeting="Hello"):
    time.sleep(0.5)
    return f"{greeting}, {name}!"

@timer
def slow_calc(n, **options):
    time.sleep(0.3)
    return sum(range(n)) * options.get('multiplier', 1)

# 测试
print(slow_add(1, 2))
print(slow_greet("程序员晚枫", greeting="你好"))
print(slow_calc(100, multiplier=2))
```

**输出：**
```
slow_add 耗时：1.0012秒
3
slow_greet 耗时：0.5003秒
你好, 程序员晚枫!
slow_calc 耗时：0.3002秒
4950
```

**🎯 记住这个万能模板：**

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):      # 接收任意参数
        # 增强逻辑1
        result = func(*args, **kwargs)  # 透传给原函数
        # 增强逻辑2
        return result
    return wrapper
```

---

## 带参数的装饰器（双层嵌套）

有时候你需要在装饰器上**传参数**，比如控制重试次数、日志级别等。

### 场景：可配置的重试装饰器

```python
import time
import random

def retry(max_attempts=3, delay=1):
    """
    重试装饰器工厂
    - max_attempts: 最大重试次数
    - delay: 重试间隔（秒）
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_attempts - 1:
                        print(f"⚠️ 第{attempt+1}次失败，{delay}秒后重试...")
                        time.sleep(delay)
                    else:
                        print(f"❌ 最终失败：{e}")
                        raise  # 重新抛出异常
        return wrapper
    return decorator

# 使用方式
@retry(max_attempts=5, delay=0.5)
def fetch_data():
    """模拟可能失败的网络请求"""
    if random.random() < 0.7:  # 70%概率失败
        raise ConnectionError("网络连接失败")
    return "数据获取成功！"

# 测试
try:
    result = fetch_data()
    print(result)
except:
    print("请求失败，已重试5次")
```

### 理解三层嵌套

```python
# 装饰器定义
def outer(参数):
    def middle(func):
        def inner(*args, **kwargs):
            # 这里可以访问 outer 的参数
            # 这里可以访问 func 的参数
            result = func(*args, **kwargs)
            return result
        return inner
    return middle

# 使用
@outer(参数)
def target():
    pass

# 等价于
target = outer(参数)(target)
```

---

## functools.wraps：保留原函数信息

装饰器有个副作用：**会覆盖原函数的 `__name__`、`__doc__` 等元信息**。

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """这是 say_hello 函数的文档"""
    print("Hello!")

# ❌ 装饰后，元信息被 wrapper 覆盖了
print(say_hello.__name__)  # wrapper
print(say_hello.__doc__)   # None
```

### ✅ 用 functools.wraps 解决

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # ← 关键：保留原函数元信息
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """这是 say_hello 函数的文档"""
    print("Hello!")

# ✅ 元信息保留了
print(say_hello.__name__)  # say_hello
print(say_hello.__doc__)   # 这是 say_hello 函数的文档
```

**@wraps 的作用：把原函数的 `__name__`、`__doc__`、`__annotations__` 等信息复制到 wrapper 上。**

---

## 常用装饰器示例（收藏备用）

### 1. 计时装饰器（完整版）

```python
import time
from functools import wraps

def timer(func):
    """记录函数执行时间"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"⏱️ {func.__name__} 执行耗时：{elapsed:.4f}秒")
        return result
    return wrapper

@timer
def process_data(n):
    """模拟数据处理"""
    return sum(range(n))

print(process_data(100000))
```

### 2. 权限检查装饰器

```python
from functools import wraps

def require_login(func):
    """检查用户是否登录"""
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not getattr(user, 'is_logged_in', False):
            raise PermissionError("请先登录！")
        return func(user, *args, **kwargs)
    return wrapper

def require_admin(func):
    """检查用户是否是管理员"""
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not getattr(user, 'is_admin', False):
            raise PermissionError("需要管理员权限！")
        return func(user, *args, **kwargs)
    return wrapper

class User:
    def __init__(self, name, is_logged_in=True, is_admin=False):
        self.name = name
        self.is_logged_in = is_logged_in
        self.is_admin = is_admin

@require_login
def view_dashboard(user):
    return f"{user.name} 的仪表盘"

@require_admin
def delete_user(user, user_id):
    return f"{user.name} 删除了用户 {user_id}"

# 测试
guest = User("游客", is_logged_in=False)
normal_user = User("张三", is_logged_in=True, is_admin=False)
admin = User("管理员", is_logged_in=True, is_admin=True)

try:
    print(view_dashboard(guest))
except PermissionError as e:
    print(f"❌ {e}")

print(view_dashboard(normal_user))  # 张三 的仪表盘
print(delete_user(admin, 123))       # 管理员 删除了用户 123
```

### 3. 缓存装饰器（记忆化）

```python
from functools import wraps

def memoize(func):
    """缓存函数结果，避免重复计算"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 用 args 和 kwargs 做一个缓存键
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            print(f"📦 缓存 miss：{func.__name__}{key}")
        else:
            print(f"📦 缓存 hit：{func.__name__}{key}")
        return cache[key]
    
    return wrapper

@memoize
def fibonacci(n):
    """斐波那契数列"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 测试：用了缓存，fib(30) 从 1秒 变成 瞬时！
print(fibonacci(10))
print(fibonacci(10))  # 这次直接命中缓存
```

### 4. 日志装饰器

```python
import logging
from functools import wraps

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def log(func):
    """记录函数调用日志"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"📥 调用 {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        logger.info(f"📤 返回 {func.__name__} -> {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

@log
def process(name, times=1):
    return f"处理 {name} {times} 次"

print(add(1, 2))
print(process("数据"))
```

### 5. 重试装饰器

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """失败时自动重试的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"⚠️ 第{attempt+1}次失败：{e}，{delay}秒后重试...")
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def call_api(endpoint):
    """模拟API调用"""
    import random
    if random.random() < 0.8:
        raise TimeoutError("请求超时")
    return f"API响应：{endpoint}"

# 测试
for i in range(3):
    print(f"\n=== 第{i+1}次调用 ===")
    try:
        print(call_api("/users"))
    except TimeoutError as e:
        print(f"❌ 彻底失败：{e}")
```

### 6. 单例装饰器

```python
from functools import wraps

def singleton(cls):
    """确保类只有一个实例"""
    instances = {}
    
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return wrapper

@singleton
class Database:
    def __init__(self):
        print("🔄 创建数据库连接")
    
    def query(self, sql):
        return f"执行：{sql}"

# 测试：多次实例化，返回同一个对象
db1 = Database()
db2 = Database()
print(db1 is db2)  # True —— 是同一个实例！
db1.query("SELECT * FROM users")
```

---

## 多个装饰器叠加

可以给一个函数加多个装饰器，它们的执行顺序是**从下往上**。

```python
def decorator_a(func):
    def wrapper(*args, **kwargs):
        print("A 开始")
        result = func(*args, **kwargs)
        print("A 结束")
        return result
    return wrapper

def decorator_b(func):
    def wrapper(*args, **kwargs):
        print("B 开始")
        result = func(*args, **kwargs)
        print("B 结束")
        return result
    return wrapper

@decorator_a
@decorator_b
def my_func():
    print("my_func 执行中")

my_func()
```

**输出：**
```
A 开始
B 开始
my_func 执行中
B 结束
A 结束
```

**等价于：**
```python
my_func = decorator_a(decorator_b(my_func))
```

**执行顺序：** 从下往上（B先执行）→ 从上往下（A先结束）

---

## 类装饰器：装饰器的高级玩法

装饰器不一定是函数，**类也可以做装饰器**！

### 场景：给函数加上调用计数

```python
class Counter:
    """统计函数被调用了多少次"""
    def __init__(self, func):
        self.func = func
        self.count = 0
        # 让装饰后的函数保留原函数的信息
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"📊 {self.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)

@Counter
def say_hello():
    return "Hello!"

@Counter
def add(a, b):
    return a + b

say_hello()  # 📊 say_hello 被调用了 1 次
say_hello()  # 📊 say_hello 被调用了 2 次
say_hello()  # 📊 say_hello 被调用了 3 次
print(add(1, 2))  # 📊 add 被调用了 1 次 -> 3
print(add(10, 20))  # 📊 add 被调用了 2 次 -> 30
```

### 类装饰器 vs 函数装饰器

| 特性 | 函数装饰器 | 类装饰器 |
|------|-----------|---------|
| 适用场景 | 简单增强 | 需要维护状态 |
| 状态保持 | 需要闭包 | 可以用实例属性 |
| 代码复杂度 | 较简单 | 较复杂 |

---

## 避坑指南：装饰器最容易踩的6个坑

### 坑1：装饰器参数顺序写反

```python
# ❌ 错误：装饰器带参数时，顺序错了
# @retry()  # 这是对的
# def func():  # 但下面这样写就错了
# @func
# @retry  # 这里 func 是普通函数，不是装饰器

# ✅ 正确写法
@retry(max_attempts=3)
def api_call():
    pass
```

### 坑2：忘记用 @wraps 导致调试困难

```python
from functools import wraps

# ❌ 没有 @wraps
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def greet():
    """打招呼函数"""
    pass

print(greet.__name__)  # wrapper —— 错误！

# ✅ 有 @wraps
def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def greet2():
    """打招呼函数"""
    pass

print(greet2.__name__)  # greet2 —— 正确！
```

### 坑3：装饰器改变了返回值

```python
# ❌ 错误：装饰器没有返回原函数的返回值
def bad_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)  # ❌ 没有 return！
        print(f"耗时：{time.time() - start}秒")
    return wrapper

@bad_timer
def add(a, b):
    return a + b

result = add(1, 2)  # ❌ result 是 None！
print(result)

# ✅ 正确：有 return
def good_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # ✅ 保存返回值
        print(f"耗时：{time.time() - start}秒")
        return result  # ✅ 返回
    return wrapper
```

### 坑4：装饰器改变了异常行为

```python
# ❌ 错误：装饰器吞掉了异常
def bad_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            pass  # ❌ 异常被吞掉了！
    return wrapper

@bad_handler
def divide(a, b):
    return a / b

result = divide(1, 0)  # ❌ 应该报错，但返回了 None！

# ✅ 正确：异常应该重新抛出
def good_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"处理异常：{e}")
            raise  # ✅ 重新抛出
    return wrapper
```

### 坑5：在装饰器中使用了可变默认参数

```python
# ❌ 错误：用了可变默认参数，导致状态污染
def bad_cache(func):
    cache = []  # ❌ 这个列表会累积！
    
    def wrapper(*args):
        if args in cache:
            print("命中缓存")
            return
        result = func(*args)
        cache.append(args)
        return result
    return wrapper

# ✅ 正确：用闭包或者放到外面
def good_cache(func):
    _cache = {}  # ✅ 字典作为缓存
    
    def wrapper(*args):
        if args in _cache:
            print("命中缓存")
            return _cache[args]
        result = func(*args)
        _cache[args] = result
        return result
    return wrapper
```

### 坑6：装饰器顺序影响结果

```python
def tag(tag_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f"<{tag_name}>{func(*args, **kwargs)}</{tag_name}>"
        return wrapper
    return decorator

@tag("b")  # 先加粗
@tag("i")  # 后斜体
def text():
    return "Hello"

print(text())  # <b><i>Hello</i></b> —— 先斜后粗！
```

---

## 实战案例：Flask路由装饰器原理

Flask 之所以简洁，就是用了装饰器。让我们仿写一个简化版：

```python
from functools import wraps

# 路由表
routes = {}

def route(path):
    """Flask风格路由装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        routes[path] = func
        return wrapper
    return decorator

@route("/")
def index():
    return "首页"

@route("/about")
def about():
    return "关于我们"

@route("/user/<name>")
def user(name):
    return f"用户：{name}"

# 查看路由表
print("注册的路由：")
for path, func in routes.items():
    print(f"  {path} -> {func.__name__}")

# 模拟请求
def simulate_request(path):
    if path in routes:
        return routes[path]()
    return "404 Not Found"

print(simulate_request("/"))      # 首页
print(simulate_request("/about")) # 关于我们
print(simulate_request("/user/程序员晚枫"))  # 用户：程序员晚枫
```

---

## 推荐：AI Python零基础实战营

想深入学习Python高级特性，写出面试官眼前一亮的代码？

**课程内容：**
- ✅ Python基础语法
- ✅ 函数与面向对象
- ✅ 装饰器、生成器、上下文管理器
- ✅ 实战项目练习

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 本讲小结

| 概念 | 说明 |
|-----|------|
| 装饰器本质 | 接收函数，返回新函数 |
| @语法糖 | `func = decorator(func)` 的简写 |
| 万能参数 | `def wrapper(*args, **kwargs)` |
| 保留元信息 | `@wraps(func)` |
| 多装饰器 | 从下往上执行 |

> 💡 **记住核心**：不修改原函数，给它加功能。核心模板只有3行！

---

## 相关阅读

- [Python函数参数*args和**kwargs详解](/course/AI相关/人民邮电出版社/ads/openclaw/09-Python函数参数/)
- [Python列表推导式：一行代码搞定循环](/course/AI相关/人民邮电出版社/ads/openclaw/07-Python列表推导式/)
- [Python字典：我用这个数据结构，把查询速度提升了100倍](/course/AI相关/人民邮电出版社/ads/openclaw/08-Python字典/)

---

*PS：装饰器是Python的"黑魔法"之一，掌握它，你的代码会简洁又强大。记住核心：不修改原函数，给它加功能。*

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


