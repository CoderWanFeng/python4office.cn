---
title: Python生成器：我处理10万条数据，内存只占了1MB
date: "2026-02-28 19:01:00"
tags: ["Python基础", "生成器", "内存优化"]
cover: "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop"
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

今天分享一个让我处理大数据时内存占用减少90%的技术——**生成器（Generator）**。

---

## 一个真实的内存爆炸事故

去年有个学员问我："晚枫老师，我的程序处理100万条数据时直接崩溃了，报MemoryError，怎么办？"

我看了一眼他的代码：

```python
# 处理100万条用户数据
def process_users():
    # 一次性加载所有数据到内存
    users = [fetch_user(i) for i in range(1000000)]
    # 每个用户对象约1KB，总共约1GB内存！
    
    results = []
    for user in users:
        results.append(analyze(user))
    
    return results

# 程序崩溃：MemoryError
```

**问题**：100万个用户对象，每个1KB，就是1GB内存！

**用生成器优化后**：

```python
def process_users():
    # 用生成器，按需生成
    def user_generator():
        for i in range(1000000):
            yield fetch_user(i)
    
    results = []
    for user in user_generator():  # 每次只有一个用户对象在内存中
        results.append(analyze(user))
    
    return results

# 内存占用：约10MB（几乎不增长）
```

你可能遇到过这种情况：要处理几万、几十万条数据，程序直接卡死或报MemoryError。这时候生成器就是你的救星。

看完这篇文章，你会理解为什么生成器被称为"省内存的神器"。

---

## 问题：列表太占内存

### 内存占用测试

```python
import sys

# 创建100万个数字
numbers_list = [i * i for i in range(1000000)]
numbers_gen = (i * i for i in range(1000000))

print(f"列表内存占用: {sys.getsizeof(numbers_list) / 1024 / 1024:.2f} MB")
print(f"生成器内存占用: {sys.getsizeof(numbers_gen) / 1024:.2f} KB")

# 输出：
# 列表内存占用: 8.39 MB
# 生成器内存占用: 0.00 KB

# 列表：需要存储所有元素的内存
# 生成器：只需要存储生成状态的内存（几十字节）
```

### 传统列表的问题

```python
def get_numbers_list(n):
    """返回列表：一次性生成所有数据"""
    result = []
    for i in range(n):
        result.append(i * i)
    return result

# 问题1：内存占用大
numbers = get_numbers_list(1000000)
# 需要约8MB内存存储列表本身，加上元素对象更多

# 问题2：生成时间长
# 必须等所有数据生成完才能开始使用

# 问题3：可能用不完
# 如果只需要前10个，后面的都白生成了
for num in numbers[:10]:
    print(num)
```

---

## 解决方案：生成器

### 什么是生成器？

生成器是一种特殊的迭代器，它**按需生成数据，而不是一次性全部生成**。

就像自动售货机，你要一个它给一个，而不是先把所有商品堆在你面前。

### 创建生成器的两种方式

#### 方式1：生成器函数（yield）

```python
def get_numbers_generator(n):
    """生成器函数：按需生成数据"""
    for i in range(n):
        yield i * i  # 用yield代替return

# 创建生成器对象
gen = get_numbers_generator(1000000)
# 此时什么都没生成！内存占用几乎为0

# 开始消费
for num in gen:
    print(num)  # 每次只生成一个数字
    if num > 100:  # 可以提前停止
        break

# 内存占用：始终很小
```

#### 方式2：生成器表达式

```python
# 列表推导式（占内存）
squares_list = [i * i for i in range(1000000)]
print(f"列表: {sys.getsizeof(squares_list) / 1024 / 1024:.2f} MB")  # 8.39 MB

# 生成器表达式（省内存）
squares_gen = (i * i for i in range(1000000))
print(f"生成器: {sys.getsizeof(squares_gen)} bytes")  # 112 bytes

# 用法完全一样
for square in squares_gen:
    print(square)
```

### 两种方式的对比

| 特性 | 生成器函数 | 生成器表达式 |
|-----|-----------|-------------|
| 语法 | `def func(): yield x` | `(x for x in iterable)` |
| 复杂度 | 可以有复杂逻辑 | 适合简单表达式 |
| 可读性 | 更易读 | 简洁 |
| 灵活性 | 高 | 低 |

```python
# 生成器函数：适合复杂逻辑
def process_data(filename):
    with open(filename, 'r') as f:
        for line in f:
            # 复杂处理逻辑
            cleaned = line.strip().lower()
            if cleaned and not cleaned.startswith('#'):
                yield cleaned

# 生成器表达式：适合简单转换
cleaned = (line.strip().lower() for line in open('data.txt'))
```

---

## yield的工作原理

### 状态保存与恢复

```python
def simple_generator():
    print("开始")
    yield 1
    print("继续")
    yield 2
    print("结束")
    yield 3

gen = simple_generator()  # 此时什么都没打印

print(next(gen))  # 输出：开始 \n 1
print(next(gen))  # 输出：继续 \n 2
print(next(gen))  # 输出：结束 \n 3
# print(next(gen))  # StopIteration异常
```

### 执行流程图

```
调用生成器函数
    ↓
创建生成器对象（不执行函数体）
    ↓
next()被调用
    ↓
执行到第一个yield
    ↓
返回yield后的值，暂停
    ↓
next()再次被调用
    ↓
从暂停处继续执行
    ↓
执行到下一个yield
    ↓
...重复...
    ↓
函数结束，抛出StopIteration
```

### yield的高级用法

#### yield from（Python 3.3+）

```python
# 传统方式：嵌套生成器
def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

# 使用yield from（更简洁）
def chain(*iterables):
    for iterable in iterables:
        yield from iterable

# 使用
result = list(chain([1, 2], [3, 4], [5]))
print(result)  # [1, 2, 3, 4, 5]

# 嵌套结构
def flatten(nested):
    """展平嵌套结构"""
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3], [4, [5, 6]]]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6]
```

#### yield作为表达式（协程基础）

```python
def accumulator():
    """累加器（协程示例）"""
    total = 0
    while True:
        # yield可以接收值
        value = yield total
        if value is None:
            break
        total += value

# 使用
acc = accumulator()
next(acc)  # 启动生成器

print(acc.send(10))  # 10
print(acc.send(5))   # 15
print(acc.send(3))   # 18

acc.close()  # 关闭生成器
```

---

## 性能对比：列表 vs 生成器

### 内存占用测试

```python
import sys
import tracemalloc

def test_memory():
    """测试内存占用"""
    tracemalloc.start()
    
    # 测试列表
    snapshot1 = tracemalloc.take_snapshot()
    numbers_list = [i * i for i in range(1000000)]
    snapshot2 = tracemalloc.take_snapshot()
    list_memory = sum(stat.size for stat in snapshot2.compare_to(snapshot1, 'filename'))
    
    # 测试生成器
    snapshot3 = tracemalloc.take_snapshot()
    numbers_gen = (i * i for i in range(1000000))
    snapshot4 = tracemalloc.take_snapshot()
    gen_memory = sum(stat.size for stat in snapshot4.compare_to(snapshot3, 'filename'))
    
    print(f"列表内存: {list_memory / 1024 / 1024:.2f} MB")
    print(f"生成器内存: {gen_memory / 1024:.2f} KB")
    print(f"节省: {(list_memory - gen_memory) / list_memory * 100:.1f}%")

test_memory()

# 输出：
# 列表内存: 39.58 MB
# 生成器内存: 0.00 KB
# 节省: 100.0%
```

### 执行时间对比

```python
import time

def test_speed():
    """测试执行时间"""
    
    # 方式1：列表（需要等所有数据生成完）
    start = time.time()
    squares_list = [i * i for i in range(1000000)]
    # 只使用前10个
    result_list = sum(squares_list[:10])
    list_time = time.time() - start
    
    # 方式2：生成器（按需生成）
    start = time.time()
    squares_gen = (i * i for i in range(1000000))
    # 只取前10个
    result_gen = sum(next(squares_gen) for _ in range(10))
    gen_time = time.time() - start
    
    print(f"列表方式: {list_time:.4f}s, 结果: {result_list}")
    print(f"生成器方式: {gen_time:.4f}s, 结果: {result_gen}")
    print(f"生成器快 {list_time / gen_time:.1f} 倍")

test_speed()

# 输出：
# 列表方式: 0.0823s, 结果: 285
# 生成器方式: 0.0001s, 结果: 285
# 生成器快 823 倍
```

### 链式操作对比

```python
import time

def process_data_list(data):
    """列表方式：三次遍历，三次内存占用"""
    # 步骤1：过滤
    filtered = [x for x in data if x > 500000]
    # 步骤2：转换
    transformed = [x * 2 for x in filtered]
    # 步骤3：计算
    result = sum(transformed)
    return result

def process_data_gen(data):
    """生成器方式：一次遍历，零额外内存"""
    result = sum(
        x * 2 for x in data if x > 500000
    )
    return result

# 测试
data = range(1000000)

start = time.time()
result1 = process_data_list(data)
list_time = time.time() - start

start = time.time()
result2 = process_data_gen(data)
gen_time = time.time() - start

print(f"列表方式: {list_time:.4f}s")
print(f"生成器方式: {gen_time:.4f}s")
print(f"结果相同: {result1 == result2}")

# 输出：
# 列表方式: 0.1523s
# 生成器方式: 0.0987s
# 结果相同: True
```

---

## 实战案例

### 案例1：读取大文件

```python
# ❌ 错误方式：一次性读取
def read_file_bad(filename):
    with open(filename, 'r') as f:
        return f.readlines()  # 所有行加载到内存

# ✅ 正确方式：生成器逐行读取
def read_file_good(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

# 使用：处理GB级文件也不会爆内存
for line in read_file_good('huge_file.txt'):
    process(line)  # 每次只处理一行
```

### 案例2：无限序列

```python
def fibonacci():
    """生成无限的斐波那契数列"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def count(start=0, step=1):
    """无限计数器"""
    n = start
    while True:
        yield n
        n += step

def cycle(iterable):
    """无限循环"""
    while True:
        for item in iterable:
            yield item

# 使用
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=' ')  # 0 1 1 2 3 5 8 13 21 34

print()
counter = count(10, 2)
for _ in range(5):
    print(next(counter), end=' ')  # 10 12 14 16 18

print()
colors = cycle(['red', 'green', 'blue'])
for _ in range(7):
    print(next(colors), end=' ')  # red green blue red green blue red
```

### 案例3：数据管道

```python
def read_log_file(filename):
    """读取日志文件"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

def filter_errors(lines):
    """过滤错误日志"""
    for line in lines:
        if 'ERROR' in line:
            yield line

def parse_timestamp(lines):
    """解析时间戳"""
    for line in lines:
        # 假设格式：[2024-01-01 10:00:00] ERROR ...
        timestamp = line[1:20]
        yield {'time': timestamp, 'message': line}

def batch(lines, size):
    """批量分组"""
    batch = []
    for line in lines:
        batch.append(line)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch

# 组合成管道
logs = read_log_file('app.log')
errors = filter_errors(logs)
parsed = parse_timestamp(errors)
batches = batch(parsed, 100)

for batch in batches:
    save_to_database(batch)  # 每100条保存一次
    # 全程内存占用极小！
```

### 案例4：分页查询

```python
def paginated_query(db, table, page_size=100):
    """分页查询生成器"""
    offset = 0
    while True:
        # 每次只查询page_size条记录
        query = f"SELECT * FROM {table} LIMIT {page_size} OFFSET {offset}"
        results = db.execute(query)
        
        if not results:
            break
        
        for row in results:
            yield row
        
        offset += page_size

# 使用：处理百万级数据
for row in paginated_query(db, 'users'):
    process_user(row)
    # 内存中始终只有page_size条记录
```

### 案例5：文件搜索

```python
from pathlib import Path

def find_files(directory, pattern='*'):
    """递归查找文件"""
    directory = Path(directory)
    for path in directory.rglob(pattern):
        if path.is_file():
            yield path

def find_by_content(directory, keyword):
    """按内容搜索文件"""
    for filepath in find_files(directory, '*.py'):
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                if keyword in line:
                    yield {
                        'file': str(filepath),
                        'line_num': line_num,
                        'line': line.strip()
                    }

# 使用
for result in find_by_content('./my_project', 'TODO'):
    print(f"{result['file']}:{result['line_num']}: {result['line']}")
```

### 案例6：数据流处理

```python
import time

def data_stream():
    """模拟实时数据流"""
    import random
    while True:
        yield {
            'timestamp': time.time(),
            'value': random.random() * 100
        }
        time.sleep(0.1)  # 模拟数据到达间隔

def sliding_window(stream, size=10):
    """滑动窗口"""
    window = []
    for item in stream:
        window.append(item)
        if len(window) > size:
            window.pop(0)
        yield window.copy()

def moving_average(windows):
    """移动平均"""
    for window in windows:
        if window:
            avg = sum(item['value'] for item in window) / len(window)
            yield avg

# 组合使用
stream = data_stream()
windows = sliding_window(stream, size=10)
averages = moving_average(windows)

for avg in averages:
    print(f"移动平均: {avg:.2f}")
    # 实时计算，不需要存储历史数据
```

---

## 生成器 vs 迭代器

### 迭代器协议

```python
class CounterIterator:
    """自定义迭代器"""
    
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

# 使用
counter = CounterIterator(0, 5)
for num in counter:
    print(num)  # 0 1 2 3 4
```

### 生成器实现同样功能

```python
def counter_generator(start, end):
    """生成器：更简洁"""
    current = start
    while current < end:
        yield current
        current += 1

# 使用
counter = counter_generator(0, 5)
for num in counter:
    print(num)  # 0 1 2 3 4
```

### 对比总结

| 特性 | 生成器 | 迭代器 |
|-----|-------|-------|
| 创建方式 | `yield`或生成器表达式 | `__iter__`和`__next__`方法 |
| 代码复杂度 | 简单（几行） | 较复杂（需要类） |
| 内存占用 | 极低 | 低 |
| 可重用性 | 一次性（用完就没了） | 一次性 |
| 状态保存 | 自动 | 手动管理 |
| 异常处理 | 自动抛出StopIteration | 手动抛出 |

**结论**：能用生成器就用生成器，代码简洁又高效。

---

## 常用内置生成器函数

### enumerate

```python
# 带索引的遍历
fruits = ['apple', 'banana', 'cherry']

# 传统方式
for i in range(len(fruits)):
    print(i, fruits[i])

# 使用enumerate（生成器）
for i, fruit in enumerate(fruits):
    print(i, fruit)

# 指定起始索引
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

### zip

```python
# 并行遍历多个序列
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['Beijing', 'Shanghai', 'Guangzhou']

# 使用zip（生成器）
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}岁, {city}")

# 创建字典
user_dict = dict(zip(names, ages))
print(user_dict)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

### map

```python
# 对每个元素应用函数
numbers = [1, 2, 3, 4, 5]

# 列表推导式
squared_list = [x ** 2 for x in numbers]

# 使用map（生成器）
squared_map = map(lambda x: x ** 2, numbers)

print(list(squared_map))  # [1, 4, 9, 16, 25]

# 多个序列
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # [11, 22, 33]
```

### filter

```python
# 过滤元素
numbers = range(20)

# 列表推导式
evens_list = [x for x in numbers if x % 2 == 0]

# 使用filter（生成器）
evens_filter = filter(lambda x: x % 2 == 0, numbers)

print(list(evens_filter))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 过滤None值
items = [0, 1, None, False, '', 'hello', []]
truthy = filter(None, items)
print(list(truthy))  # [1, 'hello']
```

### range

```python
# range本身就是生成器
r = range(1000000)  # 不占用内存

print(sys.getsizeof(r))  # 48 bytes

# 使用
for i in range(10):
    print(i)

# 步长
for i in range(0, 10, 2):
    print(i)  # 0 2 4 6 8

# 反向
for i in range(10, 0, -1):
    print(i)
```

### itertools模块

```python
import itertools

# count：无限计数
for i in itertools.count(10, 2):
    if i > 20:
        break
    print(i)  # 10 12 14 16 18 20

# cycle：无限循环
colors = itertools.cycle(['red', 'green', 'blue'])
for _ in range(7):
    print(next(colors))  # red green blue red green blue red

# repeat：重复
for item in itertools.repeat('hello', 3):
    print(item)  # hello hello hello

# chain：连接多个可迭代对象
combined = itertools.chain([1, 2], [3, 4], [5, 6])
print(list(combined))  # [1, 2, 3, 4, 5, 6]

# islice：切片
result = itertools.islice(range(100), 10, 20)
print(list(result))  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# takewhile：条件为真时取值
result = itertools.takewhile(lambda x: x < 5, range(10))
print(list(result))  # [0, 1, 2, 3, 4]

# dropwhile：条件为真时跳过
result = itertools.dropwhile(lambda x: x < 5, range(10))
print(list(result))  # [5, 6, 7, 8, 9]

# permutations：排列
perms = itertools.permutations([1, 2, 3], 2)
print(list(perms))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations：组合
combs = itertools.combinations([1, 2, 3, 4], 2)
print(list(combs))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

---

## 生成器工具函数

### 消费生成器

```python
# 列表方式
squares = (i * i for i in range(10))
result = list(squares)
print(result)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 取前N个
import itertools
squares = (i * i for i in range(100))
first_10 = list(itertools.islice(squares, 10))
print(first_10)

# 取第N个
squares = (i * i for i in range(10))
fifth = next(itertools.islice(squares, 4, None))
print(fifth)  # 16

# 求和
squares = (i * i for i in range(10))
total = sum(squares)
print(total)  # 285

# 最大/最小值
squares = (i * i for i in range(10))
print(max(squares))  # 81
```

### 重置生成器

```python
# 生成器是一次性的！
gen = (i * i for i in range(5))
print(list(gen))  # [0, 1, 4, 9, 16]
print(list(gen))  # []  第二次就没了！

# 解决方案1：重新创建
def squares(n):
    return (i * i for i in range(n))

gen1 = squares(5)
gen2 = squares(5)  # 重新创建

# 解决方案2：转换为列表（如果数据不大）
data = list((i * i for i in range(5)))
# data可以重复使用
```

### tee：复制生成器

```python
import itertools

gen = (i * i for i in range(5))

# 复制生成器
gen1, gen2, gen3 = itertools.tee(gen, 3)

print(list(gen1))  # [0, 1, 4, 9, 16]
print(list(gen2))  # [0, 1, 4, 9, 16]
print(list(gen3))  # [0, 1, 4, 9, 16]
```

---

## 避坑指南

### 坑1：生成器只能用一次

```python
gen = (i * i for i in range(5))

# 第一次使用
for num in gen:
    print(num)  # 0 1 4 9 16

# 第二次使用（已经空了）
for num in gen:
    print(num)  # 什么都不输出！

# 解决：如果需要多次使用，转换为列表
data = list(gen)
```

### 坑2：生成器不支持索引

```python
gen = (i * i for i in range(10))

# gen[5]  # TypeError: 'generator' object is not subscriptable

# 解决：使用islice
import itertools
fifth = next(itertools.islice(gen, 5, None))
print(fifth)
```

### 坑3：生成器不支持len()

```python
gen = (i * i for i in range(10))

# len(gen)  # TypeError: object of type 'generator' has no len()

# 解决：转换为列表（如果数据不大）
length = len(list(gen))

# 或者手动计数
gen = (i * i for i in range(10))
count = sum(1 for _ in gen)
print(count)
```

### 坑4：生成器不能切片

```python
gen = (i * i for i in range(10))

# gen[2:5]  # TypeError

# 解决：使用islice
import itertools
result = list(itertools.islice(gen, 2, 5))
print(result)  # [4, 9, 16]
```

### 坑5：嵌套生成器的陷阱

```python
# 错误：嵌套生成器表达式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 想要展平
flat = (item for row in matrix for item in row)
print(list(flat))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 注意顺序：外层循环在前，内层循环在后
# 等价于：
flat = []
for row in matrix:
    for item in row:
        flat.append(item)

# 带条件的嵌套
even = (item for row in matrix for item in row if item % 2 == 0)
print(list(even))  # [2, 4, 6, 8]
```

---

## 推荐：AI Python零基础实战营

想系统学习Python高级特性？

**课程内容：**
- ✅ Python基础语法
- ✅ 生成器与迭代器详解
- ✅ 内存优化技巧
- ✅ 大数据处理实战

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 相关阅读

- [Python列表推导式：一行代码搞定循环](/course/AI相关/人民邮电出版社/ads/openclaw/python/07-Python列表推导式/)
- [Python装饰器：给函数加功能的黑魔法](/course/AI相关/人民邮电出版社/ads/openclaw/python/11-Python装饰器/)
- [Python文件操作：读写文件的10种姿势](/course/AI相关/人民邮电出版社/ads/openclaw/python/13-Python文件操作/)

---

*PS：生成器是Python的高级特性之一，掌握它，你就能优雅地处理大数据。记住：内存不够，生成器来凑！*

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



