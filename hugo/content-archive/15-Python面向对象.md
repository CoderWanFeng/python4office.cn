---
title: "Python面向对象：我从零学会类和对象，全靠这7个核心概念"
date: "2026-02-28T19:00:00+08:00"
tags:
  - "Python基础"
  - "面向对象"
  - "OOP"
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

今天聊一个让新手望而生畏的话题——**面向对象编程（OOP）**。

---

## 从一个真实的代码灾难说起

去年接手一个老项目，看到这样的代码：

```python
# 学生成绩管理系统（面向过程版本）
students = []

def add_student(name, age, scores):
    students.append({'name': name, 'age': age, 'scores': scores})

def get_average(name):
    for s in students:
        if s['name'] == name:
            return sum(s['scores']) / len(s['scores'])

def get_grade(name):
    avg = get_average(name)
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    # ... 300行类似代码
```

**问题**：
- 数据和逻辑分散，难以维护
- 修改一个功能要改多个函数
- 添加新功能要大改代码

**如果用面向对象**：

```python
class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores
    
    def get_average(self):
        return sum(self.scores) / len(self.scores)
    
    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        # ...

# 使用
alice = Student('Alice', 20, [85, 90, 88])
print(alice.get_average())
print(alice.get_grade())
```

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
    """狗类"""
    
    # 类属性（所有狗共享）
    species = "Canis familiaris"
    
    # 构造方法
    def __init__(self, name, age):
        # 实例属性（每只狗独有）
        self.name = name
        self.age = age
    
    # 实例方法
    def bark(self):
        return f"{self.name} says: Woof!"
    
    def info(self):
        return f"{self.name} is {self.age} years old"

# 创建对象（实例）
my_dog = Dog("Buddy", 3)
your_dog = Dog("Max", 2)

# 访问属性
print(my_dog.name)           # Buddy
print(my_dog.species)        # Canis familiaris
print(your_dog.species)      # Canis familiaris（共享）

# 调用方法
print(my_dog.bark())         # Buddy says: Woof!
print(my_dog.info())         # Buddy is 3 years old
```

### 类属性 vs 实例属性

```python
class Dog:
    # 类属性：所有实例共享
    species = "狗"
    count = 0
    
    def __init__(self, name):
        # 实例属性：每个实例独有
        self.name = name
        Dog.count += 1  # 统计创建了多少只狗

# 创建实例
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name)        # Buddy
print(dog2.name)        # Max

print(dog1.species)     # 狗
print(dog2.species)     # 狗

# 修改类属性
Dog.species = "犬科"
print(dog1.species)     # 犬科（都改变了）

# 修改实例属性
dog1.name = "Charlie"
print(dog1.name)        # Charlie
print(dog2.name)        # Max（不受影响）

print(f"总共创建了{Dog.count}只狗")  # 总共创建了2只狗
```

---

## 概念2：__init__是构造函数

### 基础用法

```python
class Person:
    def __init__(self, name, age):
        # self代表当前对象
        self.name = name  # 给对象添加name属性
        self.age = age    # 给对象添加age属性
        
    def introduce(self):
        return f"我是{self.name}，今年{self.age}岁"

# 创建对象时自动调用__init__
person = Person("Alice", 25)
print(person.introduce())  # 我是Alice，今年25岁
```

### __init__的进阶用法

```python
class Student:
    def __init__(self, name, age, scores=None):
        self.name = name
        self.age = age
        # 默认参数
        self.scores = scores if scores else []
        # 计算属性
        self.average = sum(self.scores) / len(self.scores) if self.scores else 0
    
    def add_score(self, score):
        self.scores.append(score)
        # 更新平均值
        self.average = sum(self.scores) / len(self.scores)

# 创建学生
alice = Student("Alice", 20, [85, 90, 88])
print(alice.average)  # 87.67

bob = Student("Bob", 19)  # 没有成绩
print(bob.scores)     # []
print(bob.average)    # 0
```

### 参数验证

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        # 参数验证
        if not isinstance(owner, str):
            raise TypeError("账户名必须是字符串")
        if balance < 0:
            raise ValueError("余额不能为负数")
        
        self.owner = owner
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须大于0")
        self.balance += amount
        self.transactions.append(('存入', amount))
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("取款金额必须大于0")
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount
        self.transactions.append(('取出', amount))

# 使用
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print(f"余额：{account.balance}")  # 1300
```

### 关键点总结
- `__init__`在创建对象时自动执行
- `self`代表对象本身，必须作为第一个参数
- 通过`self.属性名`给对象添加属性
- 可以在`__init__`中做参数验证和初始化逻辑

---

## 概念3：方法是类的函数

### 实例方法

```python
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        """加法"""
        self.result += num
        return self
    
    def subtract(self, num):
        """减法"""
        self.result -= num
        return self
    
    def multiply(self, num):
        """乘法"""
        self.result *= num
        return self
    
    def reset(self):
        """重置"""
        self.result = 0
        return self
    
    def get_result(self):
        """获取结果"""
        return self.result

# 链式调用
calc = Calculator()
result = calc.add(10).multiply(2).subtract(5).get_result()
print(result)  # 15
```

### 方法可以返回值或self

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        """添加商品（返回self支持链式调用）"""
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
        return self
    
    def remove_item(self, name):
        """移除商品"""
        self.items = [i for i in self.items if i['name'] != name]
        return self
    
    def get_total(self):
        """计算总价（返回数值）"""
        return sum(i['price'] * i['quantity'] for i in self.items)
    
    def get_summary(self):
        """获取摘要（返回字典）"""
        return {
            'items': len(self.items),
            'total': self.get_total()
        }

# 链式调用
cart = ShoppingCart()
cart.add_item('Apple', 5, 3).add_item('Banana', 3, 2)
print(cart.get_total())  # 21
print(cart.get_summary())  # {'items': 2, 'total': 21}
```

---

## 概念4：继承实现代码复用

### 单继承

```python
# 父类（基类）
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("子类必须实现这个方法")
    
    def info(self):
        return f"我是{self.name}"

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
print(cat.info())   # 我是Kitty（继承自父类）
```

### 继承的好处

```python
# 1. 复用父类的代码
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_info(self):
        return f"{self.name}: ${self.salary}"

class Manager(Employee):
    # 不需要重写__init__，直接继承
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # 调用父类__init__
        self.department = department

# 2. 子类可以重写（override）父类的方法
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    def get_info(self):
        # 重写父类方法
        return f"{self.name}: ${self.salary}, {self.language} Developer"

# 3. 可以扩展新的功能
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.team = []
    
    def add_team_member(self, employee):
        self.team.append(employee)
    
    def get_team_size(self):
        return len(self.team)
```

### 多继承

```python
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

# 多继承
class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return f"{self.name} says: Quack!"

# 使用
duck = Duck("Donald")
print(duck.fly())   # I can fly!
print(duck.swim())  # I can swim!
print(duck.quack()) # Donald says: Quack!

# MRO（方法解析顺序）
print(Duck.__mro__)
# (<class '__main__.Duck'>, <class '__main__.Flyable'>, <class '__main__.Swimmable'>, <class 'object'>)
```

### Mixin模式

```python
# Mixin类：提供额外功能的小类
class LoggingMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class SerializableMixin:
    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

# 组合使用
class User(LoggingMixin, SerializableMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

# 使用
user = User("Alice", "alice@example.com")
user.log("用户创建")  # [User] 用户创建
print(user.to_dict())  # {'name': 'Alice', 'email': 'alice@example.com'}
```

---

## 概念5：super()调用父类方法

### 基础用法

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

### super()在多继承中的行为

```python
class A:
    def __init__(self):
        print("A.__init__")
        super().__init__()

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

# 使用
d = D()
# 输出：
# D.__init__
# B.__init__
# C.__init__
# A.__init__

# MRO: D -> B -> C -> A -> object
print(D.__mro__)
```

### 实战：扩展内置类

```python
class SmartList(list):
    """智能列表"""
    
    def __init__(self, *args):
        super().__init__(*args)
    
    def sum(self):
        """求和"""
        return sum(self)
    
    def average(self):
        """平均值"""
        return self.sum() / len(self) if self else 0
    
    def unique(self):
        """去重"""
        return SmartList(dict.fromkeys(self))
    
    def first(self):
        """第一个元素"""
        return self[0] if self else None
    
    def last(self):
        """最后一个元素"""
        return self[-1] if self else None

# 使用
nums = SmartList([1, 2, 2, 3, 3, 4])
print(nums.sum())      # 15
print(nums.average())  # 2.5
print(nums.unique())   # [1, 2, 3, 4]
print(nums.first())    # 1
print(nums.last())     # 4
```

---

## 概念6：私有属性和方法

### 私有属性

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

### 名称改编（Name Mangling）

```python
class Secret:
    def __init__(self):
        self.__private = "secret"  # 私有属性
        self._protected = "protected"  # 受保护属性
        self.public = "public"  # 公开属性

s = Secret()
print(s.public)       # public
print(s._protected)   # protected（可以访问，但不应该）
# print(s.__private)  # AttributeError

# 实际上Python把__private改名了
print(s._Secret__private)  # secret（可以访问，但不推荐）
```

### 私有方法

```python
class EmailSender:
    def send(self, to, subject, body):
        """公开方法：发送邮件"""
        if not self._validate_email(to):
            raise ValueError("无效的邮箱地址")
        
        self._log(f"发送邮件到 {to}")
        self._connect()
        self._send_email(to, subject, body)
        self._disconnect()
    
    def _validate_email(self, email):
        """受保护方法：验证邮箱"""
        return '@' in email
    
    def __connect(self):
        """私有方法：连接服务器"""
        pass
    
    def __send_email(self, to, subject, body):
        """私有方法：发送邮件"""
        pass
    
    def __disconnect(self):
        """私有方法：断开连接"""
        pass
    
    def _log(self, message):
        """受保护方法：记录日志"""
        print(f"[LOG] {message}")

sender = EmailSender()
sender.send("test@example.com", "Hello", "World")
# sender.__connect()  # 错误！无法访问
```

### 命名约定

| 命名 | 含义 | 可访问性 |
|-----|------|---------|
| `name` | 公开属性 | 随意访问 |
| `_name` | 受保护属性 | 可访问，但约定不外部使用 |
| `__name` | 私有属性 | 名称改编，难以直接访问 |
| `__name__` | 魔术方法 | Python内置，不要自定义 |

---

## 概念7：类方法和静态方法

### 实例方法 vs 类方法 vs 静态方法

```python
class MyClass:
    class_var = "类属性"
    
    def __init__(self):
        self.instance_var = "实例属性"
    
    # 实例方法：第一个参数是self
    def instance_method(self):
        return f"实例方法：{self.instance_var}"
    
    # 类方法：第一个参数是cls
    @classmethod
    def class_method(cls):
        return f"类方法：{cls.class_var}"
    
    # 静态方法：没有self或cls
    @staticmethod
    def static_method():
        return "静态方法：不需要访问实例或类"

# 使用
obj = MyClass()

print(obj.instance_method())  # 实例方法：实例属性
print(MyClass.class_method())  # 类方法：类属性
print(MyClass.static_method())  # 静态方法：不需要访问实例或类
```

### 类方法的应用场景

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    # 类方法：工厂方法
    @classmethod
    def from_string(cls, date_string):
        """从字符串创建日期"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """获取今天的日期"""
        import datetime
        t = datetime.date.today()
        return cls(t.year, t.month, t.day)

# 使用
d1 = Date(2024, 1, 15)
print(d1)  # 2024-01-15

d2 = Date.from_string("2024-01-15")
print(d2)  # 2024-01-15

d3 = Date.today()
print(d3)  # 今天的日期
```

### 静态方法的应用场景

```python
class MathUtils:
    """数学工具类"""
    
    @staticmethod
    def is_prime(n):
        """判断是否为质数"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n):
        """阶乘"""
        if n < 0:
            raise ValueError("n不能为负数")
        return 1 if n <= 1 else n * MathUtils.factorial(n - 1)
    
    @staticmethod
    def gcd(a, b):
        """最大公约数"""
        while b:
            a, b = b, a % b
        return a

# 使用
print(MathUtils.is_prime(17))    # True
print(MathUtils.factorial(5))    # 120
print(MathUtils.gcd(48, 18))     # 6
```

### property装饰器

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """获取半径"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """设置半径"""
        if value <= 0:
            raise ValueError("半径必须大于0")
        self._radius = value
    
    @property
    def area(self):
        """计算面积（只读属性）"""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        """计算周长（只读属性）"""
        import math
        return 2 * math.pi * self._radius

# 使用
circle = Circle(5)
print(circle.radius)        # 5
print(circle.area)          # 78.54...
print(circle.circumference) # 31.42...

circle.radius = 10  # 调用setter
print(circle.area)  # 自动更新

# circle.area = 100  # 错误！只读属性
```

---

## 魔术方法

### 常用魔术方法

```python
class Point:
    """二维点"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 字符串表示
    def __str__(self):
        """用户友好的字符串"""
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        """开发者友好的字符串"""
        return f"Point({self.x}, {self.y})"
    
    # 比较操作
    def __eq__(self, other):
        """等于"""
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        """小于"""
        return (self.x, self.y) < (other.x, other.y)
    
    # 算术操作
    def __add__(self, other):
        """加法"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """减法"""
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """乘法（标量）"""
        return Point(self.x * scalar, self.y * scalar)
    
    # 长度
    def __len__(self):
        """到原点的距离（取整）"""
        import math
        return int(math.sqrt(self.x**2 + self.y**2))
    
    # 布尔值
    def __bool__(self):
        """是否为原点"""
        return self.x != 0 or self.y != 0
    
    # 可调用
    def __call__(self):
        """调用时返回坐标"""
        return (self.x, self.y)

# 使用
p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1)           # (3, 4) - __str__
print(repr(p1))     # Point(3, 4) - __repr__

print(p1 == p2)     # False - __eq__
print(p1 > p2)      # True - __lt__

p3 = p1 + p2        # __add__
print(p3)           # (4, 6)

print(len(p1))      # 5 - __len__
print(bool(Point(0, 0)))  # False - __bool__

print(p1())         # (3, 4) - __call__
```

### 容器类魔术方法

```python
class Deck:
    """一副扑克牌"""
    
    def __init__(self):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [f"{suit}{rank}" for suit in suits for rank in ranks]
    
    def __len__(self):
        """牌数"""
        return len(self.cards)
    
    def __getitem__(self, index):
        """通过索引获取牌"""
        return self.cards[index]
    
    def __setitem__(self, index, value):
        """设置牌"""
        self.cards[index] = value
    
    def __contains__(self, card):
        """判断是否包含"""
        return card in self.cards
    
    def __iter__(self):
        """迭代"""
        return iter(self.cards)

# 使用
deck = Deck()
print(len(deck))        # 52
print(deck[0])          # ♠A
print('♠A' in deck)     # True

for card in deck[:5]:   # 迭代前5张
    print(card)
```

---

## 实战：设计一个学生管理系统

```python
from typing import List, Dict, Optional
from datetime import datetime

class Student:
    """学生类"""
    
    def __init__(self, student_id: str, name: str, age: int):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses: List['Course'] = []
        self.scores: Dict[str, float] = {}
    
    def enroll(self, course: 'Course'):
        """选课"""
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
    
    def add_score(self, course_name: str, score: float):
        """添加成绩"""
        self.scores[course_name] = score
    
    def get_average(self) -> float:
        """获取平均分"""
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)
    
    def get_info(self) -> str:
        """获取学生信息"""
        return f"{self.name}({self.student_id}), 年龄: {self.age}, 平均分: {self.get_average():.1f}"
    
    def __str__(self):
        return self.get_info()
    
    def __repr__(self):
        return f"Student({self.student_id}, {self.name})"


class Course:
    """课程类"""
    
    def __init__(self, course_id: str, name: str, credit: int = 3):
        self.course_id = course_id
        self.name = name
        self.credit = credit
        self.students: List[Student] = []
        self.teacher: Optional[str] = None
    
    def add_student(self, student: Student):
        """添加学生"""
        if student not in self.students:
            self.students.append(student)
    
    def set_teacher(self, teacher_name: str):
        """设置教师"""
        self.teacher = teacher_name
    
    def get_student_count(self) -> int:
        """获取学生数量"""
        return len(self.students)
    
    def get_average_score(self) -> float:
        """获取课程平均分"""
        scores = [s.scores.get(self.name, 0) for s in self.students if self.name in s.scores]
        return sum(scores) / len(scores) if scores else 0
    
    def __str__(self):
        return f"{self.name}({self.course_id}), 学分: {self.credit}, 学生: {self.get_student_count()}人"


class GradeBook:
    """成绩管理类"""
    
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.courses: Dict[str, Course] = {}
    
    def add_student(self, student_id: str, name: str, age: int):
        """添加学生"""
        student = Student(student_id, name, age)
        self.students[student_id] = student
        return student
    
    def add_course(self, course_id: str, name: str, credit: int = 3):
        """添加课程"""
        course = Course(course_id, name, credit)
        self.courses[course_id] = course
        return course
    
    def enroll_student(self, student_id: str, course_id: str):
        """学生选课"""
        student = self.students.get(student_id)
        course = self.courses.get(course_id)
        if student and course:
            student.enroll(course)
    
    def record_score(self, student_id: str, course_name: str, score: float):
        """记录成绩"""
        student = self.students.get(student_id)
        if student:
            student.add_score(course_name, score)
    
    def get_student_ranking(self) -> List[Student]:
        """获取学生排名（按平均分）"""
        return sorted(self.students.values(), key=lambda s: s.get_average(), reverse=True)
    
    def get_course_report(self, course_id: str) -> Dict:
        """获取课程报告"""
        course = self.courses.get(course_id)
        if not course:
            return {}
        
        return {
            'course_name': course.name,
            'student_count': course.get_student_count(),
            'average_score': course.get_average_score(),
            'teacher': course.teacher
        }
    
    def export_report(self) -> str:
        """导出报告"""
        lines = ["=== 学生成绩管理系统报告 ===", ""]
        
        # 课程统计
        lines.append("【课程统计】")
        for course in self.courses.values():
            lines.append(f"  {course}")
        lines.append("")
        
        # 学生排名
        lines.append("【学生排名】")
        for i, student in enumerate(self.get_student_ranking(), 1):
            lines.append(f"  第{i}名: {student.get_info()}")
        
        return "\n".join(lines)


# 使用示例
grade_book = GradeBook()

# 添加学生
grade_book.add_student("S001", "张三", 20)
grade_book.add_student("S002", "李四", 19)
grade_book.add_student("S003", "王五", 21)

# 添加课程
math = grade_book.add_course("MATH101", "高等数学", 4)
english = grade_book.add_course("ENG101", "大学英语", 3)

# 选课
grade_book.enroll_student("S001", "MATH101")
grade_book.enroll_student("S001", "ENG101")
grade_book.enroll_student("S002", "MATH101")
grade_book.enroll_student("S003", "MATH101")

# 录入成绩
grade_book.record_score("S001", "高等数学", 95)
grade_book.record_score("S001", "大学英语", 88)
grade_book.record_score("S002", "高等数学", 82)
grade_book.record_score("S003", "高等数学", 90)

# 导出报告
print(grade_book.export_report())
```

---

## 设计原则

### SOLID原则

```python
# S - 单一职责原则（Single Responsibility）
# 一个类只做一件事

# ❌ 违反单一职责
class User:
    def __init__(self, name):
        self.name = name
    
    def save_to_database(self):
        pass
    
    def send_email(self):
        pass

# ✅ 遵循单一职责
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        pass

class EmailService:
    def send(self, user, message):
        pass


# O - 开闭原则（Open/Closed）
# 对扩展开放，对修改关闭

# ❌ 违反开闭原则
class Discount:
    def calculate(self, type, price):
        if type == 'normal':
            return price
        elif type == 'vip':
            return price * 0.9
        # 添加新类型需要修改代码

# ✅ 遵循开闭原则
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class NormalDiscount(DiscountStrategy):
    def calculate(self, price):
        return price

class VIPDiscount(DiscountStrategy):
    def calculate(self, price):
        return price * 0.9

# 添加新策略不需要修改现有代码
class SVIPDiscount(DiscountStrategy):
    def calculate(self, price):
        return price * 0.8
```

### 组合优于继承

```python
# ❌ 过度使用继承
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    pass

class Penguin(Bird):  # 企鹅不会飞！
    def fly(self):
        raise Exception("企鹅不会飞")

# ✅ 使用组合
class Flyable:
    def fly(self):
        return "I can fly!"

class NonFlyable:
    def fly(self):
        raise Exception("我不会飞")

class Bird:
    def __init__(self, flying_behavior):
        self.flying_behavior = flying_behavior

class Sparrow(Bird):
    def __init__(self):
        super().__init__(Flyable())

class Penguin(Bird):
    def __init__(self):
        super().__init__(NonFlyable())
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

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 相关阅读

- [Python异常处理：我写了5年代码，总结的异常处理最佳实践](/course/AI相关/人民邮电出版社/ads/openclaw/python/14-Python异常处理/)
- [Python装饰器：给函数加功能的黑魔法](/course/AI相关/人民邮电出版社/ads/openclaw/python/11-Python装饰器/)
- [Python字典：我用这个数据结构，把查询速度提升了100倍](/course/AI相关/人民邮电出版社/ads/openclaw/python/08-Python字典/)

---

*PS：面向对象是一种思维方式，不只是语法。多用、多练，自然就理解了。记住：组合优于继承、单一职责、优先组合。*

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



