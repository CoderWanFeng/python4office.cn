---
title: Python函数参数*args和**kwargs：我面试挂3次后才搞懂的知识点
date: 2026-02-28 17:28:00
tags: [Python基础, 函数, 面试题]
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

今天聊一个让我面试挂了3次才彻底搞懂的知识点——**Python函数参数的*args和**kwargs**。

如果你也被这两个星号搞晕过，这篇文章就是为你写的。我会用最通俗的方式，让你一次搞明白。

---

## 为什么要学这个？

先看一个场景：

你要写一个求和函数，但不确定用户会传几个数：
```python
# 只能处理2个数
def add(a, b):
    return a + b

# 想处理3个数，得重新定义
def add3(a, b, c):
    return a + b + c

# 那100个数呢？？？
```

这时候就需要`*args`出场了。

---

## *args：接收任意多个位置参数

### 基本用法
```python
def total(*args):
    result = 0
    for num in args:
        result += num
    return result

# 调用方式
print(total(1, 2))      # 3
print(total(1, 2, 3))   # 6
print(total())          # 0
```

### args到底是什么？
```python
def show_args(*args):
    print(type(args))  # <class 'tuple'>
    print(args)        # (1, 2, 3)

show_args(1, 2, 3)
```

**args是一个元组！**里面包含了所有多余的位置参数。

### 为什么叫args？
可以改名字，但约定俗成叫args（arguments的缩写）。

---

## **kwargs：接收任意多个关键字参数

### 基本用法
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 调用方式
print_info(name="Alice", age=25, city="Beijing")
# 输出：
# name: Alice
# age: 25
# city: Beijing
```

### kwargs到底是什么？
```python
def show_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)        # {'name': 'Alice', 'age': 25}

show_kwargs(name="Alice", age=25)
```

**kwargs是一个字典！**里面包含了所有多余的关键字参数。

---

## 四种参数类型的完整顺序

Python函数参数有4种类型，必须按这个顺序写：

```python
def func(位置参数, *args, 默认参数, **kwargs):
    pass

# 举例
def example(a, b, *args, c=10, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"c={c}")
    print(f"kwargs={kwargs}")

example(1, 2, 3, 4, 5, c=20, d=30, e=40)
# 输出：
# a=1, b=2
# args=(3, 4, 5)
# c=20
# kwargs={'d': 30, 'e': 40}
```

**记忆口诀：先位置，后不定，再默认，最后关键字。**

---

## 实战案例：灵活的日志函数

写一个既能打印普通信息，又能打印详细信息的函数：

```python
def log(message, *details, **metadata):
    print(f"[LOG] {message}")
    
    if details:
        print("Details:")
        for detail in details:
            print(f"  - {detail}")
    
    if metadata:
        print("Metadata:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")

# 简单调用
log("User logged in")

# 带详情
log("Error occurred", "File not found", "Retrying...")

# 带元数据
log("Request completed", 
    status="200 OK", 
    time="0.5s", 
    user="Alice")

# 全都要
log("Payment processed",
    "Validated card",
    "Charged $100",
    order_id="12345",
    user="Bob",
    timestamp="2024-01-01")
```

**这就是*args和**kwargs的威力——超级灵活！**

---

## 解包操作：*和**的另一面

除了定义函数时用，调用函数时也能用：

### 列表解包 *
```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # 6，等价于 add(1, 2, 3)
```

### 字典解包 **
```python
def greet(name, age):
    print(f"Hi {name}, you are {age}")

person = {"name": "Alice", "age": 25}
greet(**person)  # Hi Alice, you are 25
# 等价于 greet(name="Alice", age=25)
```

---

## 常见面试题

**Q：*args和**kwargs的作用是什么？**
A：让函数接收任意数量的参数，提高灵活性。

**Q：可以只用其中一个吗？**
A：可以，根据需求选择。*args收位置参数，**kwargs收关键字参数。

**Q：下面代码的输出是什么？**
```python
def foo(a, *args, b=2, **kwargs):
    print(a, args, b, kwargs)

foo(1, 3, 4, b=5, c=6, d=7)
```
A：`1 (3, 4) 5 {'c': 6, 'd': 7}`

---

## 推荐：AI Python零基础实战营

想系统学习Python函数和高级特性？

**课程内容：**
- ✅ Python基础语法
- ✅ 函数详解（参数、返回值、作用域）
- ✅ *args和**kwargs深度解析
- ✅ 装饰器、生成器等高级特性
- ✅ 实战项目练习

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

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


