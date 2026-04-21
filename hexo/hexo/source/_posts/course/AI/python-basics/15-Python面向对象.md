---
title: Python面向对象：我从零学会类和对象，全靠这7个核心概念
date: 2026-02-28 19:00:00
tags: [Python基础, 面向对象, OOP]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA'>
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
<a href="https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

今天聊一个让新手望而生畏的话题——**面向对象编程（OOP）**。

类、对象、继承、多态...这些词听起来很抽象。但其实只要抓住核心概念，你会发现它其实很直观。

这篇文章总结了我在学习过程中总结的7个核心概念，帮你从零掌握Python面向对象。

---

## 概念1：类是蓝图，对象是实例

### 类比理解
- **类（Class）**：就像建筑图纸，定义了房子应该有什么
- **对象（Object）**：就像根据图纸建好的具体房子

### 代码示例
```python
# 定义类（蓝图）
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says: Woof!"

# 创建对象（实例）
my_dog = Dog("Buddy", 3)
your_dog = Dog("Max", 2)

print(my_dog.bark())   # Buddy says: Woof!
print(your_dog.bark()) # Max says: Woof!
```

---

## 概念2：__init__是构造函数

```python
class Person:
    def __init__(self, name, age):
        # self代表当前对象
        self.name = name  # 给对象添加name属性
        self.age = age    # 给对象添加age属性

# 创建对象时自动调用__init__
person = Person("Alice", 25)
print(person.name)  # Alice
```

**关键点**：
- `__init__`在创建对象时自动执行
- `self`代表对象本身，必须作为第一个参数
- 通过`self.属性名`给对象添加属性

---

## 概念3：方法是类的函数

```python
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result
    
    def subtract(self, num):
        self.result -= num
        return self.result
    
    def reset(self):
        self.result = 0

calc = Calculator()
print(calc.add(5))       # 5
print(calc.add(3))       # 8
print(calc.subtract(2))  # 6
```

---

## 概念4：继承实现代码复用

```python
# 父类（基类）
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("子类必须实现这个方法")

# 子类（派生类）
class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

# 使用
cat = Cat("Kitty")
dog = Dog("Buddy")

print(cat.speak())  # Kitty says: Meow!
print(dog.speak())  # Buddy says: Woof!
```

**继承的好处**：
- 复用父类的代码
- 子类可以重写（override）父类的方法
- 可以扩展新的功能

---

## 概念5：super()调用父类方法

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_info(self):
        return f"{self.name}: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # 调用父类的__init__
        self.department = department
    
    def get_info(self):
        base_info = super().get_info()  # 调用父类的方法
        return f"{base_info}, Dept: {self.department}"

manager = Manager("Alice", 80000, "IT")
print(manager.get_info())  # Alice: $80000, Dept: IT
```

---

## 概念6：私有属性和方法

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # 私有属性（双下划线）
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)
print(account.get_balance())  # 1000
# print(account.__balance)    # 错误！无法直接访问
```

**命名约定**：
- `_属性名`：受保护（约定俗成，仍可访问）
- `__属性名`：私有（名字改编，难以直接访问）

---

## 概念7：类方法和静态方法

```python
class DateUtil:
    # 类属性
    default_format = "%Y-%m-%d"
    
    @classmethod
    def set_default_format(cls, format_str):
        """类方法：操作类属性"""
        cls.default_format = format_str
    
    @staticmethod
    def is_valid_date(date_str):
        """静态方法：不需要访问类或实例"""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

# 使用类方法
DateUtil.set_default_format("%d/%m/%Y")

# 使用静态方法
print(DateUtil.is_valid_date("2024-01-01"))  # True
print(DateUtil.is_valid_date("2024-13-01"))  # False
```

---

## 实战：设计一个学生管理系统

```python
class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []
    
    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
    
    def get_info(self):
        return f"{self.name}({self.student_id}), Age: {self.age}"

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.students = []
    
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
    
    def get_student_count(self):
        return len(self.students)

# 使用
math = Course("MATH101", "Mathematics")
alice = Student("S001", "Alice", 20)
bob = Student("S002", "Bob", 21)

alice.enroll(math)
bob.enroll(math)

print(f"{math.name} has {math.get_student_count()} students")
```

---

## 推荐：AI Python零基础实战营

想系统学习Python面向对象编程？

**课程内容：**
- ✅ Python基础语法
- ✅ 面向对象编程详解
- ✅ 类设计最佳实践
- ✅ 实战项目练习

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA)**

---

## 相关阅读

- [Python异常处理：我写了5年代码，总结的异常处理最佳实践](/course/AI相关/人民邮电出版社/ads/openclaw/python/14-Python异常处理/)
- [Python装饰器：给函数加功能的黑魔法](/course/AI相关/人民邮电出版社/ads/openclaw/python/11-Python装饰器/)
- [Python字典：我用这个数据结构，把查询速度提升了100倍](/course/AI相关/人民邮电出版社/ads/openclaw/python/08-Python字典/)

---

*PS：面向对象是一种思维方式，不只是语法。多用、多练，自然就理解了。*

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


