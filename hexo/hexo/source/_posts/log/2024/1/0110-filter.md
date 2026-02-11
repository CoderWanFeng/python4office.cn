---
title: Python过滤器入门到精通，全面介绍filter()函数的用法和相关知识点
date: 2024-1-10 21:16:17
tags: 内置函数
---


大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)，又来分享有用的Python知识了。

Python之所以好用，是因为有大量用于科学计算的内置函数和第三方库。用好这些第三方库，可以显著提高我们编程的速度和质量。

今天我们一起来看一下Python中一个重要的内置函数：``filter``。

filter() 是 Python 中的一个内置函数，用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。filter() 函数接收两个参数，一个是函数，一个是序列。序列的每个元素作为参数传递给函数进行判定，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

## 1、简单用法

先说明一下需求，我们现在需要从0-10中筛选出所有的偶数，如果没有filter函数，我们的代码会像下面这么写。

```python

# 创建一个包含奇数和偶数的列表
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 创建一个存放结果的列表
res_numbers = []


for n in numbers:
    if n%2==0:
        res_numbers.append(n)

print(res_numbers)


```

而如果我们使用filter函数，代码可以这么写，👇



```python
# 定义一个过滤函数，用于判断一个数是否为偶数  
def is_even(n):
    return n % 2 == 0


# 创建一个包含奇数和偶数的列表  
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用 filter() 函数过滤出偶数  
res_numbers = filter(is_even, numbers)

# 使用 list() 将结果转换为列表  
result = list(res_numbers)
print(result)  # 输出: [0, 2, 4, 6, 8, 10]
```

在这个例子中，filter() 函数接收了两个参数：一个是我们定义的 is_even 函数，用于判断一个数是否为偶数；另一个是 numbers 列表，我们希望从中筛选出偶数。filter() 函数将 is_even 函数应用到 numbers 中的每一个元素，然后返回一个迭代器，其中包含所有使 is_even 返回 True 的元素。最后，我们使用 list() 函数将这个迭代器转换为列表。


## 2、复杂用法

还是上面这个例子，细心的同学可能发现，用了filter函数，代码变得更加冗长了。

> 难道是filter不好用吗？

是因为我们没用上filter的精髓：filter可以结合lambda表达式，进行更加高效的筛选。如下面的代码所示。


```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(res_numbers)
```

在这个代码中，我们只用了1行代码，就实现了偶数的筛选，而其中的筛选条件就来自lambda表达式。


在实际的编程工作中，很多筛选条件，都不值得用几行代码去表达，非常的浪费时间。

而使用filter这种内置函数 + lambda表达式的方式，就可以很简洁的解决这种无聊的代码过多的问题。


------

你学会了吗？使用过程中有任何问题，欢迎在评论区交流~


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。