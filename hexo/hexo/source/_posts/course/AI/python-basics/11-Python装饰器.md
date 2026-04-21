---
title: Python装饰器：我给函数加了计时功能，代码只多了2行
date: 2026-02-28 17:30:00
tags: [Python基础, 装饰器, 高级特性]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/UHvLPWCqmx_zeoCjky7u8A'>
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
<a href="https://mp.weixin.qq.com/s/UHvLPWCqmx_zeoCjky7u8A">
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

看完这篇文章，你也能写出带@符号的"高端代码"。

---

## 从一个实际需求开始

假设你有10个函数，想统计每个函数运行了多长时间。

### 笨方法（复制粘贴10次）
```python
import time

def func1():
    start = time.time()
    # ... 原来的代码 ...
    print(f"耗时：{time.time() - start}秒")

def func2():
    start = time.time()
    # ... 原来的代码 ...
    print(f"耗时：{time.time() - start}秒")

# 还有func3, func4... func10
```

**缺点**：代码重复、维护困难、容易漏改。

### 聪明方法（用装饰器）
```python
import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        print(f"耗时：{time.time() - start}秒")
        return result
    return wrapper

@timer
def func1():
    # ... 原来的代码 ...
    pass

@timer
def func2():
    # ... 原来的代码 ...
    pass
```

**只需在函数前加@timer，自动拥有计时功能！**

---

## 装饰器原理：其实就是一个函数

不要被@符号吓到，装饰器本质上就是**接收函数作为参数，返回新函数的函数**。

### 拆解来看
```python
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()           # 调用原函数
        print("函数执行后")
    return wrapper

# 使用方式1：手动调用
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()

# 使用方式2：用@语法糖（效果完全一样）
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**@就是语法糖，让代码更优雅。**

---

## 带参数的装饰器

上面的例子有个问题：如果原函数有参数怎么办？

### 万能版本（支持任意参数）
```python
import time

def timer(func):
    def wrapper(*args, **kwargs):  # 接收任意参数
        start = time.time()
        result = func(*args, **kwargs)  # 传递参数给原函数
        print(f"{func.__name__} 耗时：{time.time() - start:.4f}秒")
        return result
    return wrapper

@timer
def slow_function(n):
    time.sleep(n)
    return n * 2

result = slow_function(2)  # slow_function 耗时：2.0012秒
print(result)  # 4
```

**记住这个模板，90%的场景都能用！**

---

## 常用装饰器示例

### 1. 权限检查
```python
def require_login(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_logged_in:
            raise Exception("请先登录")
        return func(user, *args, **kwargs)
    return wrapper

@require_login
def view_profile(user):
    return user.profile
```

### 2. 缓存结果
```python
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 没有缓存：计算fib(30)需要1秒
# 有缓存：瞬间完成
```

### 3. 重试机制
```python
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"尝试{attempt+1}失败，{delay}秒后重试...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def fetch_data():
    # 可能失败的网络请求
    pass
```

---

## 多个装饰器叠加

可以同时使用多个装饰器，顺序是从下往上执行：

```python
@decorator_a
@decorator_b
@decorator_c
def my_func():
    pass

# 等价于
my_func = decorator_a(decorator_b(decorator_c(my_func)))
```

---

## 推荐：AI Python零基础实战营

想深入学习Python高级特性？

**课程内容：**
- ✅ Python基础语法
- ✅ 函数与面向对象
- ✅ 装饰器、生成器、上下文管理器
- ✅ 实战项目练习

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/UHvLPWCqmx_zeoCjky7u8A)**

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


