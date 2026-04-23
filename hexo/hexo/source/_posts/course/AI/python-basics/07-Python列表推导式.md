---
title: Python列表推导式：我用一行代码替代了10行循环，效率翻倍
date: 2026-02-28 17:26:00
tags: [Python基础, 列表推导式, 编程技巧]
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

> 大家好，我是正在实战各种AI项目的程序员晚枫。

今天分享一个让我相见恨晚的Python技巧——**列表推导式**。

第一次学会它的时候，我直接把原来20行的代码压缩成了3行。同事看到都惊了："这是什么黑魔法？"

其实一点都不难，看完这篇文章你也能掌握。而且我会告诉你：**什么时候该用，什么时候不该用**——这比学会语法更重要。

---

## 从一个真实场景说起

假设你有一份学生成绩表，需要找出所有及格（≥60分）的学生，并把他们的成绩加10分作为奖励。

### 传统写法（6行代码）

```python
scores = [55, 70, 85, 40, 90, 60, 78, 92]
rewarded_scores = []

for score in scores:
    if score >= 60:           # 筛选及格
        rewarded_scores.append(score + 10)  # 加分

print(rewarded_scores)  # [80, 95, 70, 88, 102]
```

这段代码没问题，但有点啰嗦。我们看看列表推导式怎么写：

### 列表推导式（1行代码）

```python
scores = [55, 70, 85, 40, 90, 60, 78, 92]
rewarded_scores = [score + 10 for score in scores if score >= 60]
print(rewarded_scores)  # [80, 95, 70, 88, 102]
```

**效果完全一样，代码少了83%。** 而且性能还更好——后面我会用数据证明。

---

## 列表推导式的核心语法

列表推导式的基本结构就三部分：

```python
[表达式 for 变量 in 可迭代对象 if 条件]
#  ↑      ↑           ↑          ↑
# 要生成  每个元素    数据来源    筛选条件（可选）
# 什么    叫什么      是什么
```

### 三种常见模式

| 模式 | 语法 | 示例 |
|------|------|------|
| **基础型** | `[x for x in iterable]` | 复制列表 |
| **变换型** | `[x*2 for x in iterable]` | 每个元素乘2 |
| **筛选型** | `[x for x in iterable if x>0]` | 只保留正数 |
| **变换+筛选** | `[x*2 for x in iterable if x>0]` | 先筛选再变换 |

### 模式1：基础型——快速复制或转换

```python
# 把字符串列表转成大写
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# 提取字典列表中的某个字段
users = [{"name": "张三", "age": 25}, {"name": "李四", "age": 30}]
names = [user["name"] for user in users]
print(names)  # ['张三', '李四']
```

### 模式2：变换型——对每个元素做计算

```python
# 计算平方数
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# 格式化字符串
ids = [101, 102, 103]
labels = [f"订单-{id:04d}" for id in ids]
print(labels)  # ['订单-0101', '订单-0102', '订单-0103']
```

### 模式3：筛选型——只保留符合条件的

```python
# 筛选偶数
numbers = range(20)
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 筛选包含特定字符的字符串
words = ["apple", "banana", "cherry", "date"]
a_words = [w for w in words if 'a' in w]
print(a_words)  # ['apple', 'banana', 'date']
```

### 模式4：变换+筛选——组合使用

```python
# 只给及格的学生加分
scores = [55, 70, 85, 40, 90, 60]
passed_with_bonus = [s + 5 for s in scores if s >= 60]
print(passed_with_bonus)  # [75, 90, 95, 65]

# 处理文件：只读取非空行并去掉首尾空格
with open("data.txt") as f:
    lines = [line.strip() for line in f if line.strip()]
```

---

## 进阶用法：多重循环与嵌套

### 多重循环：生成组合数据

```python
# 生成坐标点（笛卡尔积）
x_coords = [1, 2, 3]
y_coords = ['a', 'b']
points = [(x, y) for x in x_coords for y in y_coords]
print(points)
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]

# 实际应用：生成测试数据
users = ["user1", "user2"]
actions = ["login", "logout", "click"]
events = [f"{u}:{a}" for u in users for a in actions]
print(events)
# ['user1:login', 'user1:logout', 'user1:click', 'user2:login', ...]
```

### 嵌套列表推导式：处理二维数据

```python
# 把二维列表"拍平"成一维
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 转置矩阵（行变列，列变行）
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # [[1, 4], [2, 5], [3, 6]]
```

> 💡 **理解嵌套推导式的技巧**：把它展开成普通循环就懂了。
> ```python
> # 上面的转置等价于：
> result = []
> for i in range(3):
>     row = []
>     for r in matrix:
>         row.append(r[i])
>     result.append(row)
> ```

---

## 性能对比：列表推导式真的更快吗？

很多人听说列表推导式快，但不知道快多少。我们来实测一下：

```python
import time

# 测试数据：100万个数字
data = range(1_000_000)

# 方法1：传统for循环
start = time.time()
result1 = []
for x in data:
    result1.append(x * 2)
time1 = time.time() - start

# 方法2：列表推导式
start = time.time()
result2 = [x * 2 for x in data]
time2 = time.time() - start

print(f"for循环: {time1:.4f}秒")
print(f"列表推导式: {time2:.4f}秒")
print(f"提速: {time1/time2:.1f}倍")
```

**典型输出：**
```
for循环: 0.1856秒
列表推导式: 0.0892秒
提速: 2.1倍
```

### 为什么列表推导式更快？

1. **C语言实现**：列表推导式在Python底层用C实现，避免了Python解释器的额外开销
2. **局部变量优化**：推导式内的变量访问更快
3. **预分配内存**：Python能预先知道列表大小，一次性分配内存，而不是多次扩容

---

## 列表推导式 vs 生成器表达式：什么时候用哪个？

列表推导式有个"缺点"：它会一次性把所有数据加载到内存。如果数据量很大，可能会爆内存。

这时候就该用**生成器表达式**了：

```python
# 列表推导式——一次性生成所有数据
squares_list = [x**2 for x in range(1000000)]  # 占用大量内存

# 生成器表达式——按需生成，省内存
squares_gen = (x**2 for x in range(1000000))   # 几乎不占内存

# 使用时才计算
for sq in squares_gen:
    if sq > 100:
        break  # 找到就停，后面的不计算了
```

### 对比总结

| 特性 | 列表推导式 `[...]` | 生成器表达式 `(...)` |
|------|-------------------|---------------------|
| **语法** | 方括号 | 圆括号 |
| **内存** | 一次性占用 | 惰性计算，省内存 |
| **速度** | 创建时慢（要算完） | 创建时快（不算） |
| **访问** | 可随机访问 `list[5]` | 只能顺序遍历 |
| **复用** | 可多次使用 | 一次性，用完就没了 |
| **适用场景** | 数据量小，需要多次访问 | 数据量大，只需遍历一次 |

### 实际选择建议

```python
# ✅ 用列表推导式：数据量小，需要随机访问
small_data = [x**2 for x in range(1000)]
print(small_data[50])  # 随机访问第50个

# ✅ 用生成器表达式：数据量大，只需遍历
big_data = (x**2 for x in range(10000000))
for x in big_data:
    process(x)  # 处理完就扔，不占内存

# ✅ 用生成器表达式：链式处理，中间结果不需要存
result = sum(x**2 for x in range(1000000) if x % 2 == 0)
```

---

## 字典推导式 & 集合推导式

列表有推导式，字典和集合也有类似的语法：

### 字典推导式 `{k: v for ...}`

```python
# 把两个列表组合成字典
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# 交换字典的键值（值必须可哈希）
original = {'apple': 5, 'banana': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {5: 'apple', 3: 'banana'}

# 过滤字典（只保留值大于10的项）
scores = {'张三': 85, '李四': 55, '王五': 92}
passed = {k: v for k, v in scores.items() if v >= 60}
print(passed)  # {'张三': 85, '王五': 92}
```

### 集合推导式 `{x for ...}`

```python
# 提取字符串列表的长度集合（去重）
words = ["apple", "banana", "cherry", "date"]
lengths = {len(w) for w in words}
print(lengths)  # {4, 5, 6}（去重后的长度）

# 找出所有包含字母'a'的单词的首字母
words = ["apple", "banana", "cherry", "date", "apricot"]
first_chars = {w[0] for w in words if 'a' in w}
print(first_chars)  # {'a', 'b', 'd'}
```

---

## ⚠️ 什么时候不该用列表推导式？

列表推导式很酷，但不是万能的。以下情况**建议用普通循环**：

### 1. 逻辑太复杂（超过2个条件或嵌套太深）

```python
# ❌ 太难读懂了
result = [y for x in data for y in x if y > 0 if y % 2 == 0]

# ✅ 用普通循环更清晰
result = []
for x in data:
    for y in x:
        if y > 0 and y % 2 == 0:
            result.append(y)
```

### 2. 需要打印调试信息

```python
# ❌ 推导式里没法print
result = [x*2 for x in data]  # 中间过程看不见

# ✅ 用循环可以调试
result = []
for x in data:
    doubled = x * 2
    print(f"{x} -> {doubled}")  # 看中间结果
    result.append(doubled)
```

### 3. 需要异常处理

```python
# ❌ 推导式里不好处理异常
result = [int(x) for x in strings]  # 如果x不能转int会崩溃

# ✅ 用循环可以try-except
result = []
for x in strings:
    try:
        result.append(int(x))
    except ValueError:
        result.append(0)  # 给个默认值
```

### 4. 需要break/continue控制流程

```python
# ❌ 推导式不支持break
first_positive = [x for x in data if x > 0][0]  # 会遍历全部

# ✅ 用循环找到就停
first_positive = None
for x in data:
    if x > 0:
        first_positive = x
        break  # 找到了，不继续了
```

**原则：可读性 > 简洁性。** 如果推导式让人看不懂，就用普通循环。

---

## 常见错误与避坑指南

### 错误1：忘记方括号

```python
# ❌ 错的——这创建的是生成器，不是列表
squares = n ** 2 for n in numbers

# ✅ 对的
squares = [n ** 2 for n in numbers]
```

### 错误2：变量名冲突（遮蔽外部变量）

```python
x = 100
data = [1, 2, 3]

# ⚠️ 推导式里的x会暂时覆盖外面的x
result = [x * 2 for x in data]
print(x)  # 100（Python 3.x里推导式有自己的作用域，不受影响）

# 但为了代码清晰，建议避免同名
result = [item * 2 for item in data]  # 用不同的名字
```

### 错误3：在推导式里修改正在遍历的列表

```python
# ❌ 危险！不要在遍历列表时修改它
numbers = [1, 2, 3, 4, 5]
[n for n in numbers if numbers.remove(n)]  # 结果不可预测！

# ✅ 正确做法：创建新列表
numbers = [1, 2, 3, 4, 5]
evens = [n for n in numbers if n % 2 == 0]  # 筛选偶数到新列表
```

### 错误4：过度追求一行代码

```python
# ❌ 为了用推导式而推导式，可读性极差
result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# ✅ 拆成函数，加注释
def transpose(matrix):
    """转置矩阵：行变列，列变行"""
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]
```

---

## 实战案例：数据处理中的列表推导式

### 案例1：清洗用户输入数据

```python
# 用户输入（可能包含空值、前后空格、大小写不一致）
raw_inputs = ["  Alice  ", "BOB", "", "  Charlie", None, "  david  "]

# 清洗：去空值、去空格、统一小写
cleaned = [name.strip().lower() for name in raw_inputs if name]
print(cleaned)  # ['alice', 'bob', 'charlie', 'david']
```

### 案例2：处理API返回的JSON数据

```python
import requests

# 假设从API获取用户列表
response = requests.get("https://api.example.com/users")
users = response.json()

# 提取需要的字段
user_summaries = [
    {
        "id": u["id"],
        "name": u["profile"]["name"],
        "email": u["contact"]["email"]
    }
    for u in users
    if u.get("active")  # 只保留活跃用户
]
```

### 案例3：文件批处理

```python
import os

# 获取当前目录下所有.py文件（不包括test_开头和__开头的）
py_files = [
    f for f in os.listdir('.')
    if f.endswith('.py')
    and not f.startswith('test_')
    and not f.startswith('__')
]

# 读取所有文件内容
contents = []
for filename in py_files:
    with open(filename, encoding='utf-8') as f:
        contents.append({
            "filename": filename,
            "lines": len(f.readlines()),
            "size": os.path.getsize(filename)
        })

# 筛选大文件（超过100行）
large_files = [c for c in contents if c["lines"] > 100]
```

---

## 本讲小结

| 概念 | 说明 | 示例 |
|------|------|------|
| 列表推导式 | 一行代码创建列表 | `[x*2 for x in data]` |
| 带条件筛选 | 只保留符合条件的 | `[x for x in data if x>0]` |
| 多重循环 | 处理多维数据 | `[(x,y) for x in a for y in b]` |
| 生成器表达式 | 惰性计算，省内存 | `(x*2 for x in data)` |
| 字典推导式 | 创建字典 | `{k:v for k,v in zip(keys,vals)}` |
| 集合推导式 | 创建集合（去重） | `{len(w) for w in words}` |

### 核心原则

1. **简单场景用推导式**：逻辑清晰、条件简单时，推导式更优雅
2. **复杂场景用循环**：需要调试、异常处理、复杂逻辑时，循环更清晰
3. **大数据用生成器**：数据量大且只需遍历时，用生成器表达式省内存
4. **可读性优先**：如果推导式让人看不懂，就拆成循环

---

## 下节预告

下一篇我们将学习**Python字典的高级用法**，包括defaultdict、Counter等神器，让数据处理更加高效。

👉 **[继续阅读：Python字典使用技巧](./08-Python字典.md)**

---

## 课程导航

**上一篇：** [Python函数基础](./06-Python函数基础.md)

**下一篇：** [Python字典使用技巧](./08-Python字典.md)

---

## 推荐：AI Python零基础实战营

如果你想系统学习Python，从基础到实战：

**课程包含：**
- ✅ Python基础语法（变量、循环、函数）
- ✅ 高级特性（推导式、生成器、装饰器）
- ✅ 数据处理（Excel、CSV、数据库）
- ✅ 自动化办公实战
- ✅ AI辅助编程技巧

🎁 **限时福利**：前100名送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 相关阅读

- [零基础学AI编程：30天速成计划](/course/AI相关/人民邮电出版社/ads/openclaw/20260228171202-零基础学AI编程-30天速成计划/)
- [Python字典使用技巧大全](/course/AI相关/人民邮电出版社/ads/openclaw/08-Python字典/)
- [Python函数参数*args和**kwargs详解](/course/AI相关/人民邮电出版社/ads/openclaw/09-Python函数参数/)

---

*PS：列表推导式是Python的精髓之一，掌握它，你的代码会优雅很多。但记住：**可读性永远比炫技更重要**。*

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

---

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
