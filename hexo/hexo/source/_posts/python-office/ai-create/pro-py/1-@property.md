---
title: Python中@property的用法和作用
date: 2024-05-31 01:25:17
tags: Python进阶
---
<!-- more -->
在Python中，`@property` 装饰器用于将一个类的方法转变为属性访问的形式。这通常用于当你想提供一个方法，让它表现得像是一个属性，或者当你想在访问属性时加入一些逻辑处理。

下面是一个使用 `@property` 的例子：

```python

class Circle:
    def __init__(self, radius):
        self._radius = radius  # 私有属性，用来存储圆的半径

    @property
    def radius(self):
        # 这是radius属性的getter方法
        return self._radius

    @radius.setter
    def radius(self, value):
        # 这是radius属性的setter方法
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

    @property
    def area(self):
        # 这是一个只读属性，计算圆的面积
        return 3.14159 * (self._radius ** 2)

# 使用示例
circle = Circle(5)  # 创建一个半径为5的圆
print(circle.radius)  # 输出: 5
print(circle.area)    # 输出: 78.53975

# 尝试设置半径
circle.radius = 10
print(circle.radius)  # 输出: 10
print(circle.area)    # 输出: 157.0795

# 尝试设置一个无效的半径值
try:
    circle.radius = -5
except ValueError as e:
    print(e)  # 输出: 半径不能为负数
```

在这个例子中，`Circle` 类有两个属性：`radius` 和 `area`。通过使用 `@property` 装饰器，我们定义了 `radius` 的 getter 和 setter 方法，以及 `area` 的只读属性。

- `@property` 装饰器将 `radius` 方法转换为属性，这样我们就可以使用 `circle.radius` 来访问或设置圆的半径。
- `@radius.setter` 装饰器定义了设置 `radius` 属性时应该执行的代码，这里我们添加了一个检查，确保半径不会是负数。
- `area` 属性使用了 `@property` 装饰器，但没有对应的 setter 方法，因此它是一个只读属性。我们不能直接设置 `area` 的值，但可以通过访问 `circle.area` 来获取圆的面积。

使用 `@property` 的好处是代码更加清晰易读，同时可以在访问属性时加入逻辑处理，使得类的接口更加安全和灵活。


Python学习交流群，欢迎加入，👇

![](https://cos.python-office.com/group/0816.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)

