---
title: 这1道华为笔试题，让我陷入了沉思，整理了Python里的正则表达式的12种写法
date: 2022-07-13 14:25:03
tags: 正则表达式
---

![](https://www.python-office.com/api/img-cdn/pro-python/re.py/re-cover.jpg)

大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)。

上次我们分享了：[4千字总结！Python生成随机数的22种方法，random函数太强了~](https://mp.weixin.qq.com/s/l6Tq3QtkFPOdj4SdYJCPcg)

今天用一道华为笔试题，带大家深入掌握一项Python技巧：正则表达式。

>本文主要分为4个部分：题目解析、常用方法、专业方法、注意事项

## 一、题目解析

先来看一下题目。
![](https://www.python-office.com/api/img-cdn/pro-python/re.py/question.jpg)

看完题目，有以下2个解题思路：
1. 纯手写：首先把输入的字符串，用0补全为8的倍数，然后遍历字符串，每8个组成一个新的字符。
2. 使用内置方法和标准库：使用str的内置方法，用0补全右侧，然后使用正则每8个字符进行匹配。
### 1、思路1：纯手写
```python
def cut_8ch(str):
    if len(str) < 8:
        str = str.ljust(8, '0')
    elif len(str) > 8:
        if (len(str) % 8) != 0:
            width = len(str) + (8 - len(str) % 8)
            str = str.ljust(width, '0')
    str2List = []
    i = 0
    while i < len(str):
        if (i + 8) < len(str):
            str2List.append(str[i:i+8])
        else:
            str2List.append(str[i:len(str)])
            break
        i = i + 8
    return str2List

output = []
tmp = input('请输入字符串-->>').strip()
output.append(cut_8ch(tmp))

for x in output:
    for y in x:
        print(y)
```

### 2、思路2：使用内置方法和标准库
```python
import re

str = input('请输入字符串-->>')
if len(s) % 8 != 0:
    s = s.ljust(len(s) + (8 - len(s) % 8), str(0))

res = re.findall('.{8}', s)
[print(r) for r in res]
```

很明显，思路2实现起来，逻辑更清晰，代码更简洁。原因在哪里呢？
> 因为使用了str的自带方法和Python自带的标准库：re模块。
> 之前给大家整理了：
> - [Python打基础一定要吃透这68个内置函数](https://mp.weixin.qq.com/s/zkqHTof0nRKkeeXtcn_7hQ)
> - [超全！我把 Python 的 200个标准库整理出来了](https://mp.weixin.qq.com/s/wPpw1wneX_PO3pIY7t8T3Q)

今天我们重点讲一下re模块的使用。
关于str的所有自带方法，如果大家想看的话，可以加入交流群告诉我：[交流群](http://www.python4office.cn/wechat-group/)。我可以另写一个篇新的文章来介绍。

## 二、常用方法

按照惯例，我们对Python知识的解析，直接拿源码来研究。先看一下python源码里，re模块提供的12个方法👇
![](https://www.python-office.com/api/img-cdn/pro-python/re.py/func.jpg)

### findall方法
找出所有符合条件的内容。

**举例：**

我们现在有一句话，里面有一些数字，我们想把这些数字都提取出来：程序员晚枫，今年``18``岁，家里存款``100``多，车有``0``辆，多谢各位的``10086``+个点赞
```python
import re

str = '程序员晚枫，今年18岁，家里存款100多，车有0辆，多谢各位的10086+个点赞'
res = re.findall('[0-9]+',string=str)
print(res)
# 输出：['18', '100', '0', '10086']
```

### split方法

对字符串进行分割。

**举例：**

假如我们现在有一组字符串:程序员晚枫``5``程序员晚枫``4``程序员晚枫``7``程序员晚枫，其中混进了一些无规律的数字：5、4、7，这次我们想根据这些数字，把这个字符串分割。

```python
import re

str = '程序员晚枫5程序员晚枫4程序员晚枫7程序员晚枫'
res = re.split(pattern='[0-9]',string=str)
print(res)
# 输出：['程序员晚枫', '程序员晚枫', '程序员晚枫', '程序员晚枫，']
```


### sub方法
可以替换字符串中的内容。

**举例：**

假如我们现在有一组字符串:程序员晚枫``5``程序员晚枫``4``程序员晚枫``7``程序员晚枫，其中混进了一些无规律的数字：5、4、7，我们想根据这些数字，替换成逗号：``，``。
```python
import re

str = '程序员晚枫5程序员晚枫4程序员晚枫7程序员晚枫，'
res = re.sub(pattern='[0-9]', repl='，', string=str, count=0)
print(res)
# 输出：程序员晚枫，程序员晚枫，程序员晚枫，程序员晚枫，
# -----

# 参数1：pattern：表示正则中的模式字符串。
# 参数2：repl：就是replacement，表示被替换的字符串，可以是字符串也可以是函数。
# 参数3：string：表示要被处理和替换的原始字符串
# 参数4：count：可选参数，表示是要替换的最大次数，而且必须是非负整数，该参数默认为0，即所有的匹配都会被替换；


```

### match方法
re.match()必须从字符串开头匹配！

**举例：**

match方法，可以帮我们匹配出这段文字中的英文字母，``"CoderWanFeng，加好友，联系程序员晚枫"``
```python
import re

text = "CoderWanFeng，加好友，联系程序员晚枫"

res = re.match("[a-zA-Z]+", text)

print(res)  # 查看是否匹配到结果
print(res.group())  # 取出匹配的内容
```
### fullmatch方法
fullmatch见名知义：只有在给定的字符串全部匹配时，才返回正确。

**举例：**

匹配用户输入的电话号码是否都是数字+符合11位。

```python
import re

input = "19512345678"
pattern = "[0-9]+"

print(re.fullmatch(pattern, input))
print(re.fullmatch(pattern,input).group())
```


### search方法

查找字符串中是否有符合条件的内容。
```python
import re

str = "程序员晚枫"
# search 字符串第一次出现的位置
print(re.search("晚", str))
# 输出：<re.Match object; span=(3, 4), match='晚'>
```
## 三、专业方法

### subn方法
subn和sub的方法类似，区别在于：subn()方法返回一个元组，其中包含所有替换的总数以及新字符串。
看到subn方法我困惑了一下，它和sub的区别时什么？

看过源码👇才知道，区别就是那个n。
![](https://www.python-office.com/api/img-cdn/pro-python/re.py/sub-subn.jpg)
```python
import re

str = '程序员晚枫，程序员晚枫，程序员晚枫，程序员晚枫，'
res = re.subn(pattern='程序员晚枫', repl='点赞+关注', string=str, count=2)
print(res)
# 参数1：pattern：表示正则中的模式字符串。
# 参数2：repl：就是replacement，表示被替换的字符串，可以是字符串也可以是函数。
# 参数3：string：表示要被处理和替换的原始字符串
# 参数4：count：可选参数，表示是要替换的最大次数，而且必须是非负整数，该参数默认为0，即所有的匹配都会被替换；
# -----
# ('点赞+关注，点赞+关注，程序员晚枫，程序员晚枫，', 2)
```


### finditer
这个方法返回的是一个迭代器。
```python
import re

str = '程序员晚枫，今年18岁，家里存款100多，车有0辆，多谢各位的10086+个点赞'
res = re.finditer('[0-9]+',string=str)
print(res)
# 输出：<callable_iterator object at 0x000001C3E94D3F40>
```

### compile
re.compile()是用来优化正则的，它将正则表达式转化为对象，re.search(pattern, string)的调用方式就转换为 pattern.search(string)的调用方式，多次调用一个正则表达式就重复利用这个正则对象，可以实现更有效率的匹配。

如下列代码所示，**re.compile生成pattern后，依然需要调用re的方法。**

```python
import re

str = '程序员晚枫，今年18岁，家里存款100多，车有0辆，多谢各位的10086+个点赞'
reg = re.compile('[0-9]+')
res = reg.findall(string=str)
print(res)
# 输出：['18', '100', '0', '10086']
```

### purge
如源码所说，这个方法主要是用来清楚缓存。

> Python标准库中唯一调用re.purge()的位置是在测试中（特别是test_re模块的re单元测试和回归测试套件中的参考泄漏测试）。

![](https://www.python-office.com/api/img-cdn/pro-python/re.py/sub-subn.jpg)

### template
这个方法我没找到怎么使用，欢迎大家在评论区补充。


### escape
可以将字符串中所有可能被解释为正则运算符的字符进行转译。
```python
re.escape('www.python-office.com')

# 输出：'www\\.python-office\\.com'
```

## 四、注意事项

- match只能从头开始匹配
- match和search的区别：search可以从全部内容中匹配
- 所有的匹配方法，都有一个属性：flags：
  - 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
-----
#### 参考资料
1. 固定长度分割：https://blog.csdn.net/weixin_43273051/article/details/106445550
2. re.match: https://www.jianshu.com/p/cc26837242b1
3. re.fullmatch: https://vimsky.com/examples/usage/re-fullmatch-function-in-python.html
4. re.search: https://www.w3cschool.cn/article/81381190.html
5. re.sub: https://blog.csdn.net/m0_46483236/article/details/117708084
6. re.subn: https://www.nhooo.com/note/qa0rvh.html
7. re.split: https://blog.csdn.net/qq_31672701/article/details/100711585
8. re.compile: https://www.cnblogs.com/xp1315458571/articles/13720333.html
9. re.escape: https://www.cnblogs.com/zeke-python-road/p/9583814.html

----

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。