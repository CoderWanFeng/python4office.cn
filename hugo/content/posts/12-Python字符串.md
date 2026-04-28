---
title: "Python字符串：我被忽略的20个实用方法，效率提升3倍"
date: "2026-02-28T18:57:00+08:00"
tags:
  - "Python基础"
  - "字符串"
  - "编程技巧"
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

你知道程序员最头疼什么吗？**处理字符串。**

用户输入有空格要去掉、邮箱格式要验证、文件后缀要判断、文本要拼接替换……写起来零零碎碎，查文档查到崩溃。

今天我把我自己常用的**Python字符串20个方法**全部整理出来，**配合实战场景**，让你一次搞明白，效率提升3倍！

> 💡 **场景预告**：你有一段用户输入的文本，需要：去掉空格、转成小写、验证格式、提取关键词……学会这些方法，一行搞定！

---

## 1. 大小写转换（5个方法）

### 基本转换

```python
text = "Hello World Python"

print(text.upper())       # HELLO WORLD PYTHON（全部大写）
print(text.lower())       # hello world python（全部小写）
print(text.title())       # Hello World Python（每个单词首字母大写）
print(text.capitalize())  # Hello world python（只有首字母大写）
print(text.swapcase())    # hELLO wORLD pYTHON（大小写互换）
```

### 实战：忽略大小写的用户验证

```python
# 场景：用户输入 YES/yEs/yes 都要接受
answer = input("确认继续吗？").strip().lower()

if answer == "yes":
    print("✅ 继续执行")
else:
    print("❌ 无效输入")

# 测试：
# 输入: YES  → ✅ 继续执行
# 输入: yes  → ✅ 继续执行
# 输入:  No  → ❌ 无效输入（去掉了空格也判断了大小写）
```

### 实战：首字母大写的姓名格式化

```python
def format_name(name):
    """规范化用户输入的姓名"""
    return name.strip().title()

names = ["  alice  ", "BOB", "charlie smith", "DR. JOHN DOE"]
for name in names:
    print(f"'{name}' -> '{format_name(name)}'")

# 输出：
# '  alice  ' -> 'Alice'
# 'BOB' -> 'Bob'
# 'charlie smith' -> 'Charlie Smith'
# 'DR. JOHN DOE' -> 'Dr. John Doe'
```

---

## 2. 查找与计数（4个方法）

### 基础用法

```python
text = "Python is easy, Python is powerful, Python is fun!"

# 查找子串位置（找不到返回 -1）
print(text.find("Python"))    # 0（第一次出现的位置）
print(text.find("Java"))     # -1（不存在）
print(text.find("Python", 10)) # 12（从第10个位置开始找）

# rfind：从右边开始找（最后一次出现）
print(text.rfind("Python"))   # 27（最后一次出现的位置）

# 统计出现次数
print(text.count("Python"))   # 3

# index：和find一样，但找不到会报错
print(text.index("Python"))  # 0
# print(text.index("Java"))   # ValueError: substring not found
```

### 实战：日志分析

```python
log = """[2024-01-01 10:00:00] INFO: 服务启动
[2024-01-01 10:00:01] ERROR: 连接数据库失败
[2024-01-01 10:00:02] INFO: 重试连接
[2024-01-01 10:00:03] ERROR: 连接数据库失败
[2024-01-01 10:00:04] ERROR: 连接数据库失败
[2024-01-01 10:00:05] INFO: 连接成功"""

# 统计错误数量
error_count = log.count("ERROR")
print(f"错误数量：{error_count}")  # 3

# 找出所有错误的行
lines = log.split("\n")
error_lines = [line for line in lines if "ERROR" in line]
print("所有错误：")
for line in error_lines:
    print(f"  {line}")
```

---

## 3. 替换（2个方法）

### 基础用法

```python
text = "Hello World, Hello Python"

# replace：替换所有
print(text.replace("Hello", "Hi"))  
# Hi World, Hi Python

# replace：只替换前N次
print(text.replace("Hello", "Hi", 1))  
# Hi World, Hello Python

# 多重替换
text = "苹果的价格是10元，香蕉的价格是20元"
text = text.replace("苹果", "橙子").replace("10", "15").replace("20", "25")
print(text)  # 橙子的价格是15元，香蕉的价格是25元
```

### 实战：敏感词过滤

```python
def filter_sensitive(text, sensitive_words, replacement="*"):
    """敏感词过滤"""
    for word in sensitive_words:
        # 把敏感词替换成对应数量的 *
        text = text.replace(word, replacement * len(word))
    return text

content = "这个产品质量太差了，简直是垃圾！"
sensitive = ["差", "垃圾"]

result = filter_sensitive(content, sensitive)
print(result)  # 这个产品**量太*了，简直是**！
```

---

## 4. 判断方法（10个方法）

判断字符串是否符合某种规则，返回 True 或 False。

### 基础判断

```python
# 判断开头/结尾
filename = "report.pdf"
print(filename.startswith("report"))     # True
print(filename.endswith(".pdf"))         # True
print(filename.endswith((".pdf", ".docx", ".txt")))  # True（支持元组）

url = "https://www.python.org"
print(url.startswith("https://"))        # True
print(url.startswith("http://"))         # False

# 判断纯数字/字母/混合
print("123".isdigit())       # True（纯数字）
print("123a".isdigit())      # False
print("abc".isalpha())       # True（纯字母）
print("abc123".isalnum())    # True（字母或数字）
print("username_123".isalnum())  # False（因为有下划线）

# 判断大小写
print("hello".islower())     # True（全小写）
print("HELLO".isupper())     # True（全大写）
print("Hello".istitle())     # True（每个单词首字母大写）

# 判断空白字符
print("   ".isspace())       # True（空格/tab/换行）
print("\t\n".isspace())      # True
print("".isspace())          # False（空字符串不是空白）
```

### 实战：验证用户输入

```python
def validate_user_input(username, email, password):
    """验证用户注册信息"""
    errors = []

    # 验证用户名：字母或数字，3-20位
    if not (username.isalnum() and 3 <= len(username) <= 20):
        errors.append("用户名必须是3-20位的字母或数字")

    # 验证邮箱：必须包含@
    if "@" not in email or not email.endswith((".com", ".cn", ".org")):
        errors.append("邮箱格式不正确")

    # 验证密码：至少8位，至少一个大写一个小写一个数字
    if len(password) < 8:
        errors.append("密码至少8位")
    if not any(c.isupper() for c in password):
        errors.append("密码需要包含大写字母")
    if not any(c.islower() for c in password):
        errors.append("密码需要包含小写字母")
    if not any(c.isdigit() for c in password):
        errors.append("密码需要包含数字")

    return errors

# 测试
errors = validate_user_input("alice123", "alice@example.com", "Pass1234")
if errors:
    print("❌ 验证失败：")
    for e in errors:
        print(f"  - {e}")
else:
    print("✅ 验证通过")
```

### 实战：文件类型判断

```python
def get_file_type(filename):
    """根据文件后缀判断文件类型"""
    ext = filename.lower()
    
    if ext.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
        return "图片"
    elif ext.endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv')):
        return "视频"
    elif ext.endswith(('.mp3', '.wav', '.flac', '.aac', '.ogg')):
        return "音频"
    elif ext.endswith(('.pdf', '.doc', '.docx', '.txt', '.rtf')):
        return "文档"
    elif ext.endswith(('.zip', '.rar', '.7z', '.tar', '.gz')):
        return "压缩包"
    elif ext.endswith(('.py', '.js', '.java', '.cpp', '.c', '.go', '.rs')):
        return "代码"
    else:
        return "未知"

files = ["photo.jpg", "movie.mp4", "song.mp3", "report.pdf", "code.py", ".gitignore"]
for f in files:
    print(f"{f}: {get_file_type(f)}")
```

---

## 5. 去除空白（3个方法）

```python
text = "  hello world  \n\t"

# strip：去掉两边
print(f"'{text.strip()}'")   # 'hello world'

# lstrip：只去左边
print(f"'{text.lstrip()}'")  # 'hello world  \n\t'

# rstrip：只去右边
print(f"'{text.rstrip()}'")  # '  hello world'

# 去掉指定字符
print("...hello...".strip('.'))  # 'hello'
print("!!!hi!!!".strip('!'))     # 'hi'
print("###code###".strip('#'))   # 'code'

# 去掉多个字符（全部出现的都去掉）
print("abcHelloabc".strip('abc'))  # 'Hell'
```

### 实战：处理用户输入

```python
def clean_input(prompt):
    """清理用户输入"""
    user_input = input(prompt)
    # 去掉首尾空格
    user_input = user_input.strip()
    # 把多个空格替换成单个
    user_input = " ".join(user_input.split())
    return user_input

# 测试
name = clean_input("请输入姓名：")
email = clean_input("请输入邮箱：")
print(f"\n姓名：'{name}'")
print(f"邮箱：'{email}'")

# 输入: "   程序员   晚枫   " -> "程序员 晚枫"
# 输入: "  alice@example.com  " -> "alice@example.com"
```

---

## 6. 对齐与填充（3个方法）

```python
text = "Python"

# center：居中对齐
print(text.center(20))           # '       Python       '
print(text.center(20, '-'))      # '-------Python-------'
print(text.center(11, '*'))       # '***Python**'

# ljust：左对齐
print(text.ljust(20, '*'))       # 'Python**************'
print(text.ljust(10))             # 'Python    '

# rjust：右对齐
print(text.rjust(20, '*'))       # '**************Python'
print(text.rjust(10))             # '    Python'

# zfill：数字前面补零（超实用！）
print("42".zfill(5))             # '00042'
print("-42".zfill(6))           # '-00042'
print("abc".zfill(10))          # '0000000abc'
```

### 实战：格式化输出表格

```python
# 格式化商品列表
products = [
    ("Apple iPhone", 5999, 500),
    ("Samsung Galaxy", 4999, 300),
    ("Xiaomi Phone", 2999, 1000),
]

# 表头
print(f"{'商品名称'.ljust(20)} {'价格'.rjust(10)} {'销量'.rjust(10)}")
print("-" * 42)

# 数据行
for name, price, sales in products:
    print(f"{name.ljust(20)} {price:>10,} {sales:>10,}")

# 输出：
# 商品名称                         价格         销量
# ----------------------------------------
# Apple iPhone                  5,999        500
# Samsung Galaxy                4,999        300
# Xiaomi Phone                  2,999      1,000
```

### 实战：格式化流水号

```python
# 生成订单号
for i in range(1, 11):
    order_id = f"ORD{str(i).zfill(6)}"
    print(order_id)

# 输出：
# ORD000001
# ORD000002
# ...
# ORD000010
```

---

## 7. 分割与合并

### 分割

```python
text = "apple, banana, cherry, date"

# split：按分隔符分割
print(text.split(", "))        # ['apple', 'banana', 'cherry', 'date']

# split：只分割前N次
print(text.split(", ", 2))     # ['apple', 'banana', 'cherry, date']

# splitlines：按行分割
multiline = """第一行
第二行
第三行
"""
print(multiline.splitlines())  # ['第一行', '第二行', '第三行']

# 按空白分割（自动处理多个空格、tab、换行）
messy = "a\t  b\n c   d"
print(messy.split())           # ['a', 'b', 'c', 'd']（自动清理空白）
print(messy.split(" "))        # ['a', '', 'b', '', 'c', '', 'd']（保留空）

# partition：分割成三部分
path = "https://www.example.com/index.html"
result = path.partition("://")
print(result)  # ('https', '://', 'www.example.com/index.html')

# rpartition：从右边分割
email = "user@example.com"
print(email.rpartition("@"))  # ('user', '@', 'example.com')
```

### 合并

```python
words = ['hello', 'world', 'python']

# join：拼接字符串
print(" ".join(words))        # hello world python
print("-".join(words))        # hello-world-python
print(", ".join(words))       # hello, world, python
print("".join(words))         # helloworldpython

# 实战：构建SQL语句
fields = ["name", "age", "city"]
values = ["'张三'", "28", "'重庆'"]

# INSERT INTO users (name, age, city) VALUES ('张三', '28', '重庆');
sql = f"INSERT INTO users ({', '.join(fields)}) VALUES ({', '.join(values)});"
print(sql)
```

### 实战：解析日志文件

```python
log = """2024-01-01 10:00:00 INFO 服务启动
2024-01-01 10:00:01 ERROR 数据库连接失败
2024-01-01 10:00:02 WARNING 内存使用率高
2024-01-01 10:00:03 ERROR 重试连接"""

for line in log.strip().split("\n"):
    # 分割成：日期、时间、级别、消息
    parts = line.split(" ", 3)
    if len(parts) == 4:
        date, time, level, message = parts
        print(f"[{level}] {message}")
```

---

## 8. f-string 格式化（最常用）

f-string 是 Python 3.6+ 引入的字符串格式化方式，比 `%` 和 `.format()` 都简洁。

### 基础用法

```python
name = "程序员晚枫"
age = 28
city = "重庆"

# 基本替换
print(f"我叫{name}，今年{age}岁，来自{city}")
# 我叫程序员晚枫，今年28岁，来自重庆

# 支持表达式
print(f"明年就{age + 1}岁了")
print(f"名字长度：{len(name)}")

# 支持函数调用
print(f"大写名字：{name.upper()}")
```

### 数字格式化

```python
import math

# 保留小数
pi = math.pi
print(f"π ≈ {pi:.2f}")        # π ≈ 3.14
print(f"π ≈ {pi:.4f}")        # π ≈ 3.1416

# 百分比
ratio = 0.2589
print(f"占比：{ratio:.1%}")   # 占比：25.9%

# 千分位分隔符
big_num = 1234567890
print(f"大数字：{big_num:,}")  # 1,234,567,890
print(f"大数字：{big_num:_}")  # 1_234_567_890

# 科学计数法
print(f"科学：{big_num:.2e}")  # 1.23e+09
```

### 对齐格式化

```python
name = "晚枫"
score = 95.5

# 左对齐 <
print(f"{name:<10}得分：{score:.1f}")   
# 晚枫        得分：95.5

# 右对齐 >
print(f"{name:>10}得分：{score:.1f}")   
#         晚枫得分：95.5

# 居中 ^
print(f"{name:^10}得分：{score:.1f}")   
#     晚枫     得分：95.5

# 用指定字符填充
print(f"{name:*^10}得分：{score:.1f}")   
# ****晚枫****得分：95.5
```

### 日期格式化

```python
from datetime import datetime

now = datetime(2024, 1, 15, 14, 30, 45)

print(f"日期：{now:%Y年%m月%d日}")       # 2024年01月15日
print(f"时间：{now:%H:%M:%S}")           # 14:30:45
print(f"完整：{now:%Y-%m-%d %H:%M}")    # 2024-01-15 14:30
```

### f-string 进阶：嵌套与条件

```python
# 嵌套格式化
for width in [5, 10, 15]:
    print(f"{'Hi':^{width}}")  # 分别居中对齐到5/10/15宽度

# 条件表达式
value = 75
print(f"等级：{'及格' if value >= 60 else '不及格'}")

# f-string 中使用引号
print(f"他说：'Hello'")   # 他说：'Hello'
print(f'他说："Hello"')   # 他说："Hello"
print(f"路径：C:\\Users\\Name")  # C:\Users\Name
```

---

## 9. 正则表达式增强（re模块）

对于复杂字符串处理，f-string 不够用，需要正则表达式：

```python
import re

text = "我的邮箱是 alice@example.com，电话是 138-1234-5678，备用邮箱 bob@test.cn"

# 提取邮箱
emails = re.findall(r'\w+@\w+\.\w+', text)
print(f"邮箱：{emails}")  # ['alice@example.com', 'bob@test.cn']

# 提取手机号
phones = re.findall(r'\d{3}-\d{4}-\d{4}', text)
print(f"电话：{phones}")  # ['138-1234-5678']

# 提取所有数字
numbers = re.findall(r'\d+', text)
print(f"数字：{numbers}")  # ['138', '1234', '5678']

# 替换：把邮箱打码
masked = re.sub(r'\w+@\w+\.\w+', '[邮箱已隐藏]', text)
print(masked)  # 我的邮箱是 [邮箱已隐藏]，电话是 138-1234-5678，备用邮箱 [邮箱已隐藏]

# 验证手机号格式
def validate_phone(phone):
    pattern = r'^1[3-9]\d{9}$'  # 1开头，第二位3-9，后面9位数字
    return bool(re.match(pattern, phone))

tests = ["13812345678", "12345678901", "abc12345678", "1381234567"]
for t in tests:
    print(f"{t}: {'✅' if validate_phone(t) else '❌'}")
```

---

## 10. bytes 字符串处理

在处理文件、网络数据时，需要用 bytes 类型：

```python
# 字符串转 bytes
text = "你好，世界！"
bytes_data = text.encode("utf-8")
print(bytes_data)  # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'

# bytes 转字符串
back = bytes_data.decode("utf-8")
print(back)  # 你好，世界！

# bytes 的常用操作
b = b"Hello World"
print(b.upper())          # b'HELLO WORLD'
print(b.replace(b"World", b"Python"))  # b'Hello Python'
print(b.split(b" "))     # [b'Hello', b'World']
print(b.find(b"World"))  # 6
```

---

## 避坑指南：字符串最容易踩的6个坑

### 坑1：字符串是不可变的！

```python
# ❌ 错误：字符串不能直接修改
# s = "hello"
# s[0] = "H"  # TypeError: 'str' object does not support item assignment

# ✅ 正确：需要生成新字符串
s = "hello"
s = s.replace("h", "H")
print(s)  # Hello

# 或者用列表
s_list = list("hello")
s_list[0] = "H"
s = "".join(s_list)
print(s)  # Hello
```

### 坑2：中文编码问题

```python
# ❌ 编码不一致会导致乱码
text = "你好"
bytes1 = text.encode("utf-8")
bytes2 = text.encode("gbk")

print(bytes1.decode("utf-8"))   # 正常
# print(bytes1.decode("gbk"))  # 乱码！

# ✅ 正确：编码和解码用同一种方式
text = "你好"
encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")
print(decoded == text)  # True
```

### 坑3：strip() 会去掉所有空白字符

```python
# ❌ 误以为只去掉空格
text = "\n\t  hello  \r\n"
print(f"'{text.strip()}'")  # 'hello' —— 换行、空格、tab全没了！

# 如果你只想去掉空格
print(f"'{text.strip(' ')}'")  # '\n\t  hello  \r\n' —— 只去空格
```

### 坑4：split() 和 splitlines() 的区别

```python
# split() 不保留空行，splitlines() 保留
text = "a\n\nb\n"
print(text.split("\n"))      # ['a', '', 'b', '']
print(text.splitlines())    # ['a', '', 'b']

# splitlines() 不保留换行符
print(text.splitlines(True)) # ['a\n', '\n', 'b\n'] —— 保留换行符
```

### 坑5：+ 拼接 vs join()

```python
# ❌ + 拼接（每次创建新字符串，慢！）
parts = ["hello"] * 1000
result = ""
for p in parts:
    result += p  # 每次都创建新字符串，O(n²)

# ✅ join()（推荐，快！）
result = "".join(parts)  # 一次性拼接，O(n)
```

### 坑6：f-string 中要计算要用 !r

```python
# ❌ 直接放字典/列表会报错（太长的表达式）
data = {"name": "test"}
# print(f"数据：{data.items()}")  # 不推荐，太长

# ✅ 或者用变量
items = list(data.items())
print(f"数据：{items}")  # 数据：[('name', 'test')]

# 转义花括号
print(f"输出花括号：{{和}}")  # 输出花括号：{和}
```

---

## 性能对比：字符串拼接方法

```python
import time

# 生成10000个字符串
parts = ["item" + str(i) for i in range(10000)]

# 方法1：+ 拼接
start = time.time()
result = ""
for p in parts:
    result += p
plus_time = time.time() - start

# 方法2：join()
start = time.time()
result = "".join(parts)
join_time = time.time() - start

print(f"+ 拼接耗时：{plus_time:.4f}秒")
print(f"join耗时：{join_time:.4f}秒")
print(f"join快 {(plus_time/join_time):.0f} 倍")

# 参考结果：
# + 拼接耗时：0.8234秒
# join耗时：0.0002秒
# join快 4117 倍！
```

---

## 常见面试题

**Q1：如何统计字符串中每个字符出现的次数？**
```python
from collections import Counter

text = "hello world"
counts = Counter(text)
print(counts)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 去掉空格再统计
counts = Counter(text.replace(" ", ""))
print(counts.most_common(3))  # [('l', 3), ('o', 2), ('h', 1)]
```

**Q2：反转字符串有几种方式？**
```python
s = "hello"

# 方式1：切片
print(s[::-1])  # olleh

# 方式2：reversed + join
print("".join(reversed(s)))  # olleh

# 方式3：循环（不推荐，慢）
result = ""
for c in s:
    result = c + result
print(result)  # olleh
```

**Q3：如何判断字符串是否是回文？**
```python
def is_palindrome(s):
    # 只考虑字母和数字，忽略大小写
    s = "".join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

tests = ["A man, a plan, a canal: Panama", "race a car", "hello", "Madam, I'm Adam"]
for t in tests:
    print(f"'{t}': {'是' if is_palindrome(t) else '不是'}回文")
```

**Q4：Python 字符串有哪些不可变特性？**
> A：字符串一旦创建就不能修改，所有"修改"操作实际上都创建了新的字符串。这带来了以下特点：
> - 线程安全
> - 可以用作字典的键和集合的元素
> - 但拼接操作较多时性能差，应该用 `join()`

---

## 推荐：AI Python零基础实战营

想系统学习Python，把字符串处理和文本分析全部拿下？

**课程内容：**
- ✅ Python基础语法
- ✅ 字符串全面详解
- ✅ 正则表达式实战
- ✅ 文件读写操作
- ✅ 文本处理项目

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 本讲小结

| 分类 | 常用方法 |
|-----|---------|
| 大小写 | `.upper()`, `.lower()`, `.title()`, `.capitalize()`, `.swapcase()` |
| 查找 | `.find()`, `.rfind()`, `.index()`, `.count()` |
| 替换 | `.replace()` |
| 判断 | `.startswith()`, `.endswith()`, `.isdigit()`, `.isalpha()`, `.isalnum()`, `.isspace()`, `.islower()`, `.isupper()`, `.istitle()` |
| 去除 | `.strip()`, `.lstrip()`, `.rstrip()` |
| 对齐 | `.center()`, `.ljust()`, `.rjust()`, `.zfill()` |
| 分割 | `.split()`, `.splitlines()`, `.partition()`, `.rpartition()` |
| 合并 | `.join()` |
| 格式化 | `f"..."`, `.format()` |

> 💡 **记住**：字符串是 Python 最常用的数据类型，方法很多但都很简单。**多练几次，自然就记住了！**

---

## 下节预告

字符串学完了，下一篇来学**文件操作**——读写文件是编程的基本功。

👉 **[继续阅读：Python文件操作](./13-Python文件操作.md)**

---

## 课程导航

**上一篇：** [Python装饰器](./11-Python装饰器.md)

**下一步：** [Python文件操作-读写文件的10种姿势](./13-Python文件操作.md)

---

*PS：字符串是Python最常用的数据类型之一。熟练使用这些方法，代码效率翻倍！*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


