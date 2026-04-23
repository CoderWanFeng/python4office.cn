---
title: Python正则表达式：我用这10个模式，搞定了90%的文本处理需求
date: 2026-02-28 19:03:00
tags: [Python基础, 正则表达式, 文本处理]
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

今天聊一个让新手望而生畏、但学会后威力无穷的技能——**正则表达式（Regular Expression）**。

---

## 一个真实的文本处理灾难

去年有个学员问我："晚枫老师，我要从10万个HTML文件中提取邮箱地址，怎么办？"

他写的代码：

```python
# 提取邮箱（笨办法）
def extract_emails(text):
    emails = []
    # 找@
    at_pos = text.find('@')
    # 往前找开头
    # 往后找结尾
    # 检查是否合法
    # ... 写了100多行代码
    return emails

# 10万个文件，跑了一个小时
```

**用正则表达式**：

```python
import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

# 10万个文件，10分钟搞定
```

你可能觉得正则很难记、很晦涩。但其实只要掌握最常用的10个模式，就能搞定90%的文本处理需求。

这篇文章总结了我在数据处理中最常用的正则技巧，帮你快速上手。

---

## 为什么要学正则？

### 正则 vs 传统方法

```python
# 需求：从文本中提取所有数字

# 方法1：不用正则（痛苦）
def extract_numbers(text):
    numbers = []
    current = ''
    for char in text:
        if char.isdigit():
            current += char
        else:
            if current:
                numbers.append(int(current))
                current = ''
    if current:
        numbers.append(int(current))
    return numbers

# 方法2：用正则（一行搞定）
import re
numbers = [int(n) for n in re.findall(r'\d+', text)]
```

**正则就是文本处理的瑞士军刀。**

### 正则能做什么？

- ✅ 数据提取：邮箱、电话、URL、价格等
- ✅ 数据验证：格式检查、输入校验
- ✅ 数据清洗：去除多余空格、标点、特殊字符
- ✅ 数据转换：格式化、替换、重命名
- ✅ 日志分析：提取关键信息、错误定位

---

## Python中的正则模块

### 核心函数

```python
import re

# 1. match() - 从开头匹配
result = re.match(r'hello', 'hello world')
print(result.group())  # hello

# 2. search() - 搜索第一个匹配
result = re.search(r'world', 'hello world')
print(result.group())  # world

# 3. findall() - 找到所有匹配
results = re.findall(r'\d+', 'abc123def456')
print(results)  # ['123', '456']

# 4. finditer() - 返回迭代器
for match in re.finditer(r'\d+', 'abc123def456'):
    print(match.group(), match.span())

# 5. sub() - 替换
result = re.sub(r'\d+', 'X', 'abc123def456')
print(result)  # abcXdefX

# 6. split() - 分割
parts = re.split(r'[,;\s]+', 'a,b;c d')
print(parts)  # ['a', 'b', 'c', 'd']

# 7. compile() - 编译正则（提高性能）
pattern = re.compile(r'\d+')
results = pattern.findall('abc123def456')
```

### 匹配对象的方法

```python
import re

text = "Email: alice@example.com, Phone: 13812345678"
pattern = r'(\w+)@(\w+\.\w+)'

match = re.search(pattern, text)
if match:
    print(match.group())   # alice@example.com（完整匹配）
    print(match.group(0))  # alice@example.com（同上）
    print(match.group(1))  # alice（第一个分组）
    print(match.group(2))  # example.com（第二个分组）
    print(match.groups())  # ('alice', 'example.com')
    print(match.start())   # 7（匹配开始位置）
    print(match.end())     # 25（匹配结束位置）
    print(match.span())    # (7, 25)
```

---

## 正则语法速查表

### 基础元字符

| 符号 | 含义 | 示例 |
|-----|------|------|
| `.` | 任意字符（除换行） | `a.c` 匹配 "abc", "a1c" |
| `\d` | 数字 [0-9] | `\d+` 匹配 "123" |
| `\D` | 非数字 | `\D+` 匹配 "abc" |
| `\w` | 单词字符 [a-zA-Z0-9_] | `\w+` 匹配 "hello_123" |
| `\W` | 非单词字符 | `\W+` 匹配 "!@#" |
| `\s` | 空白字符（空格、制表、换行） | `\s+` 匹配 "  " |
| `\S` | 非空白字符 | `\S+` 匹配 "hello" |

### 量词

| 符号 | 含义 | 示例 |
|-----|------|------|
| `*` | 0次或多次 | `a*` 匹配 "", "a", "aaa" |
| `+` | 1次或多次 | `a+` 匹配 "a", "aaa" |
| `?` | 0次或1次 | `a?` 匹配 "", "a" |
| `{n}` | 恰好n次 | `a{3}` 匹配 "aaa" |
| `{n,}` | 至少n次 | `a{2,}` 匹配 "aa", "aaa", ... |
| `{n,m}` | n到m次 | `a{2,4}` 匹配 "aa", "aaa", "aaaa" |

### 定位符

| 符号 | 含义 | 示例 |
|-----|------|------|
| `^` | 字符串开头 | `^hello` 匹配开头的hello |
| `$` | 字符串结尾 | `world$` 匹配结尾的world |
| `\b` | 单词边界 | `\bhello\b` 匹配单词hello |
| `\B` | 非单词边界 | `\Bhello` 匹配非边界的hello |

### 字符集

| 符号 | 含义 | 示例 |
|-----|------|------|
| `[abc]` | 匹配a、b、c任一个 | `[aeiou]` 匹配元音 |
| `[^abc]` | 匹配非a、b、c | `[^0-9]` 匹配非数字 |
| `[a-z]` | 匹配a到z | `[A-Za-z]` 匹配字母 |
| `[0-9]` | 匹配0到9 | 同`\d` |

### 分组

| 符号 | 含义 | 示例 |
|-----|------|------|
| `()` | 分组 | `(ab)+` 匹配 "ab", "abab" |
| `(?:)` | 非捕获分组 | `(?:ab)+` 不捕获分组 |
| `(?P<name>)` | 命名分组 | `(?P<email>\w+@\w+)` |
| `|` | 或 | `cat|dog` 匹配 "cat" 或 "dog" |

---

## 10个必备正则模式

### 模式1：匹配数字

```python
import re

text = "年龄：25，身高：175cm，体重：70.5kg，温度：-5°C"

# 匹配整数
integers = re.findall(r'\d+', text)
print(integers)  # ['25', '175', '70', '5']

# 匹配小数
decimals = re.findall(r'\d+\.\d+', text)
print(decimals)  # ['70.5']

# 匹配整数和小数
numbers = re.findall(r'-?\d+\.?\d*', text)
print(numbers)  # ['25', '175', '70.5', '-5']

# 匹配百分数
text2 = "完成度：85%，进度：99.5%"
percents = re.findall(r'\d+\.?\d*%', text2)
print(percents)  # ['85%', '99.5%']

# 匹配货币
text3 = "价格：$99.99，原价：¥199.00"
prices = re.findall(r'[$¥]\d+\.?\d*', text3)
print(prices)  # ['$99.99', '¥199.00']
```

### 模式2：匹配邮箱

```python
import re

# 基础邮箱匹配
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

text = """
联系我们：
- 技术支持：support@example.com
- 销售咨询：sales@company.co.uk
- 客服热线：service123@mail.test-site.cn
"""

emails = re.findall(pattern, text)
print(emails)
# ['support@example.com', 'sales@company.co.uk', 'service123@mail.test-site.cn']

# 更严格的邮箱验证
def is_valid_email(email):
    """验证邮箱格式"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(is_valid_email('test@example.com'))  # True
print(is_valid_email('invalid-email'))     # False
print(is_valid_email('test@.com'))         # False
```

### 模式3：匹配手机号（中国大陆）

```python
import re

text = """
联系方式：
- 手机：13800138000
- 座机：021-12345678
- 手机：15912345678
- 手机：18600001111
"""

# 中国大陆手机号
phones = re.findall(r'1[3-9]\d{9}', text)
print(phones)  # ['13800138000', '15912345678', '18600001111']

# 带格式的手机号
text2 = "电话：138-0013-8000 或 159 1234 5678"
phones = re.findall(r'1[3-9][- ]?\d{4}[- ]?\d{4}', text2)
print(phones)  # ['138-0013-8000', '159 1234 5678']

# 座机号码
landlines = re.findall(r'\d{3,4}-\d{7,8}', text)
print(landlines)  # ['021-12345678']

# 验证手机号
def is_valid_phone(phone):
    """验证手机号"""
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))

print(is_valid_phone('13800138000'))  # True
print(is_valid_phone('12800138000'))  # False（号段不对）
```

### 模式4：匹配URL

```python
import re

text = """
网站链接：
- 官网：https://www.example.com
- 论坛：http://bbs.test-site.org/page?id=123
- 文档：https://docs.python.org/3/library/re.html
- 图片：https://cdn.example.com/images/logo.png
"""

# 匹配URL
urls = re.findall(r'https?://[^\s<>"{}|\\^`[\]]+', text)
for url in urls:
    print(url)

# 提取域名
domains = re.findall(r'https?://([^/]+)', text)
print(domains)
# ['www.example.com', 'bbs.test-site.org', 'docs.python.org', 'cdn.example.com']

# 提取路径
paths = re.findall(r'https?://[^/]+(/[^\s]*)?', text)
print(paths)

# 验证URL
def is_valid_url(url):
    """验证URL"""
    pattern = r'^https?://[^\s<>"{}|\\^`[\]]+$'
    return bool(re.match(pattern, url))
```

### 模式5：提取HTML标签内容

```python
import re

html = """
<html>
<head><title>我的网站</title></head>
<body>
    <h1>欢迎</h1>
    <p class="intro">这是一段介绍文字</p>
    <a href="https://example.com">链接</a>
    <img src="logo.png" alt="Logo">
</body>
</html>
"""

# 提取title内容
title = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
if title:
    print(title.group(1))  # 我的网站

# 提取所有链接
links = re.findall(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', html, re.DOTALL)
for url, text in links:
    print(f"{text}: {url}")

# 提取所有图片
images = re.findall(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"', html)
for src, alt in images:
    print(f"{alt}: {src}")

# 提取所有标签内容
def extract_tag_content(html, tag):
    """提取指定标签的内容"""
    pattern = rf'<{tag}[^>]*>(.*?)</{tag}>'
    return re.findall(pattern, html, re.DOTALL)

print(extract_tag_content(html, 'h1'))  # ['欢迎']
print(extract_tag_content(html, 'p'))   # ['这是一段介绍文字']
```

### 模式6：验证密码强度

```python
import re

def check_password_strength(password):
    """检查密码强度"""
    # 至少8位，包含大小写字母和数字
    if len(password) < 8:
        return "弱：少于8位"
    
    has_lower = re.search(r'[a-z]', password)
    has_upper = re.search(r'[A-Z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    if all([has_lower, has_upper, has_digit, has_special]):
        return "强：包含大小写字母、数字和特殊字符"
    elif all([has_lower, has_upper, has_digit]):
        return "中：包含大小写字母和数字"
    else:
        return "弱：缺少必要字符"

# 测试
print(check_password_strength("abc"))          # 弱：少于8位
print(check_password_strength("hello123"))     # 弱：缺少必要字符
print(check_password_strength("Hello123"))     # 中：包含大小写字母和数字
print(check_password_strength("Hello123!"))    # 强：包含大小写字母、数字和特殊字符

def validate_password(password):
    """严格验证密码（返回True/False）"""
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
    return bool(re.match(pattern, password))

print(validate_password("Hello123!"))  # True
print(validate_password("hello123"))   # False
```

### 模式7：格式化字符串

```python
import re

# 驼峰转下划线
def camel_to_snake(name):
    """驼峰命名转下划线命名"""
    # 方式1：简单转换
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return result

print(camel_to_snake('myVariableName'))  # my_variable_name
print(camel_to_snake('getHTTPResponse')) # get_h_t_t_p_response

# 改进版
def camel_to_snake_better(name):
    """改进版：处理连续大写字母"""
    result = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', name)
    result = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', result)
    return result.lower()

print(camel_to_snake_better('getHTTPResponse'))  # get_http_response

# 下划线转驼峰
def snake_to_camel(name):
    """下划线命名转驼峰命名"""
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

print(snake_to_camel('my_variable_name'))  # myVariableName

# 首字母大写
def snake_to_pascal(name):
    """下划线命名转帕斯卡命名"""
    return ''.join(x.title() for x in name.split('_'))

print(snake_to_pascal('my_variable_name'))  # MyVariableName

# 格式化手机号
def format_phone(phone):
    """格式化手机号：13800138000 -> 138-0013-8000"""
    phone = re.sub(r'\D', '', phone)  # 去除非数字
    if len(phone) == 11:
        return f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"
    return phone

print(format_phone('13800138000'))  # 138-0013-8000
print(format_phone('138-0013-8000'))  # 138-0013-8000
```

### 模式8：清理文本

```python
import re

text = "  Hello!!!   World???  \n\n  这是一个  测试\t文本...  "

# 1. 去除多余空格
cleaned = re.sub(r'\s+', ' ', text).strip()
print(cleaned)  # "Hello!!! World??? 这是一个 测试文本..."

# 2. 去除标点符号
no_punct = re.sub(r'[^\w\s]', '', cleaned)
print(no_punct)  # "Hello World 这是一个 测试文本"

# 3. 只保留中文和字母
chinese_and_letters = re.sub(r'[^\u4e00-\u9fa5a-zA-Z\s]', '', text)
print(chinese_and_letters)

# 4. 只保留数字
text2 = "价格：￥199.00，数量：100"
numbers_only = re.sub(r'[^\d]', '', text2)
print(numbers_only)  # 19900100

# 5. 清理HTML标签
html_text = "<p>Hello <b>World</b></p>"
no_html = re.sub(r'<[^>]+>', '', html_text)
print(no_html)  # "Hello World"

# 6. 清理特殊字符
text3 = "Hello\x00World\x1FTest"
cleaned = re.sub(r'[\x00-\x1F\x7F]', '', text3)
print(cleaned)  # "HelloWorldTest"

# 7. 统一引号
text4 = '他说："Hello"，她回答'Hi''
normalized = re.sub(r'["""]', '"', text4)
normalized = re.sub(r"['']", "'", normalized)
print(normalized)  # '他说："Hello"，她回答'Hi''
```

### 模式9：解析日志

```python
import re
from collections import Counter

# Apache日志格式
log_line = '192.168.1.1 - - [15/Jan/2024:10:30:45 +0800] "GET /index.html HTTP/1.1" 200 1234'

# 解析日志
pattern = r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) ([^"]+) HTTP/\d\.\d" (\d+) (\d+)'
match = re.match(pattern, log_line)

if match:
    ip = match.group(1)
    timestamp = match.group(2)
    method = match.group(3)
    path = match.group(4)
    status = match.group(5)
    size = match.group(6)
    
    print(f"IP: {ip}")
    print(f"时间: {timestamp}")
    print(f"方法: {method}")
    print(f"路径: {path}")
    print(f"状态码: {status}")
    print(f"大小: {size}")

# 批量分析日志
def analyze_logs(log_file):
    """分析日志文件"""
    ip_counter = Counter()
    path_counter = Counter()
    status_counter = Counter()
    
    pattern = r'^(\S+) .+? "(\S+) ([^"]+) .+?" (\d+)'
    
    with open(log_file, 'r') as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                ip_counter[match.group(1)] += 1
                path_counter[match.group(3)] += 1
                status_counter[match.group(4)] += 1
    
    return {
        'top_ips': ip_counter.most_common(10),
        'top_paths': path_counter.most_common(10),
        'status_codes': dict(status_counter)
    }
```

### 模式10：批量重命名

```python
import re
import os
from pathlib import Path

# 批量重命名文件

def batch_rename(directory, pattern, replacement):
    """批量重命名文件"""
    directory = Path(directory)
    
    for filepath in directory.iterdir():
        if filepath.is_file():
            new_name = re.sub(pattern, replacement, filepath.name)
            if new_name != filepath.name:
                new_path = filepath.parent / new_name
                filepath.rename(new_path)
                print(f"Renamed: {filepath.name} -> {new_name}")

# 示例1：给所有图片添加日期前缀
batch_rename('./images', r'^(.*)\.jpg$', r'2024_\1.jpg')

# 示例2：统一文件名格式
# IMG_001.JPG -> img_001.jpg
batch_rename('./photos', r'IMG_(\d+)\.JPG', r'img_\1.jpg')

# 示例3：删除文件名中的特殊字符
batch_rename('./files', r'[^\w\-.]', r'_')

# 批量替换文件内容
def batch_replace(directory, file_pattern, old_text, new_text):
    """批量替换文件内容"""
    directory = Path(directory)
    
    for filepath in directory.rglob(file_pattern):
        if filepath.is_file():
            content = filepath.read_text(encoding='utf-8')
            new_content = re.sub(old_text, new_text, content)
            
            if content != new_content:
                filepath.write_text(new_content, encoding='utf-8')
                print(f"Updated: {filepath}")

# 示例：替换所有Python文件中的老API
batch_replace('./project', '*.py', r'old_api\.call', r'new_api.run')
```

---

## 高级技巧

### 贪婪 vs 非贪婪

```python
import re

text = "<div>内容1</div><div>内容2</div>"

# 贪婪匹配（默认）
greedy = re.findall(r'<div>.*</div>', text)
print(greedy)  # ['<div>内容1</div><div>内容2</div>']

# 非贪婪匹配（加?）
non_greedy = re.findall(r'<div>.*?</div>', text)
print(non_greedy)  # ['<div>内容1</div>', '<div>内容2</div>']

# 另一个例子
text2 = "价格：$10.99，优惠：$5.50"

# 贪婪
greedy = re.findall(r'\$.+\$', text2)
print(greedy)  # ['$10.99，优惠：$5.50']

# 非贪婪
non_greedy = re.findall(r'\$.+?\$', text2)
print(non_greedy)  # ['$10.99，优惠：$']（还是不对）

# 正确：使用非字符集
correct = re.findall(r'\$[\d.]+', text2)
print(correct)  # ['$10.99', '$5.50']
```

### 前瞻和后顾

```python
import re

# 正向前瞻 (?=...)
text = "hello123world456"

# 匹配数字前面是字母的位置
result = re.findall(r'(?<=[a-z])\d+', text)
print(result)  # ['123', '456']

# 匹配字母后面是数字的字母
result = re.findall(r'[a-z]+(?=\d)', text)
print(result)  # ['hello', 'world']

# 负向前瞻 (?!...)
# 匹配后面不是数字的字母
result = re.findall(r'[a-z]+(?!\d)', text)
print(result)  # ['hell', 'world']（hello被分成hell和o）

# 正向后顾 (?<=...)
# 匹配前面是$的数字
text2 = "价格：$100，数量：5"
result = re.findall(r'(?<=\$)\d+', text2)
print(result)  # ['100']

# 负向后顾 (?<!...)
# 匹配前面不是$的数字
result = re.findall(r'(?<!\$)\d+', text2)
print(result)  # ['5']
```

### 命名分组

```python
import re

text = "张三，男，25岁，来自北京"

# 使用命名分组
pattern = r'(?P<name>\w+)，(?P<gender>\w)，(?P<age>\d+)岁，来自(?P<city>\w+)'

match = re.search(pattern, text)
if match:
    print(match.group('name'))   # 张三
    print(match.group('gender')) # 男
    print(match.group('age'))    # 25
    print(match.group('city'))   # 北京
    
    # 获取所有命名分组
    print(match.groupdict())
    # {'name': '张三', 'gender': '男', 'age': '25', 'city': '北京'}

# 在替换中使用
text2 = "2024-01-15"
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
result = re.sub(pattern, r'\g<month>/\g<day>/\g<year>', text2)
print(result)  # 01/15/2024
```

### 条件匹配

```python
import re

# (?(id)yes|no) - 条件匹配

# 示例：匹配带引号或不带引号的内容
text = '名称："测试" 或 测试'

pattern = r'(")?(.*?)(?(1)"|)'
matches = re.findall(pattern, text)
print(matches)
```

### 修饰符

```python
import re

text = """Hello
World
Test"""

# re.DOTALL - . 匹配换行符
result = re.findall(r'.+', text, re.DOTALL)
print(result)  # ['Hello\nWorld\nTest']

# re.IGNORECASE - 忽略大小写
result = re.findall(r'hello', 'Hello World', re.IGNORECASE)
print(result)  # ['Hello']

# re.MULTILINE - 多行模式
text2 = """第一行
第二行
第三行"""
result = re.findall(r'^第', text2, re.MULTILINE)
print(result)  # ['第', '第', '第']

# re.VERBOSE - 详细模式（允许注释和换行）
pattern = re.compile(r"""
    \b              # 单词边界
    \d{3}           # 区号
    [-\s]?          # 分隔符
    \d{4}           # 前四位
    [-\s]?          # 分隔符
    \d{4}           # 后四位
    \b              # 单词边界
""", re.VERBOSE)

result = pattern.findall("电话：138-0013-8000")
print(result)

# 组合修饰符
result = re.findall(r'hello', 'HELLO\nHello', re.IGNORECASE | re.MULTILINE)
```

---

## 性能优化

### 编译正则表达式

```python
import re
import time

# 测试匹配10万次
text = "这是一段测试文本，包含邮箱 test@example.com"

# 方式1：每次编译
def test_no_compile():
    start = time.time()
    for _ in range(100000):
        re.search(r'\w+@\w+\.\w+', text)
    return time.time() - start

# 方式2：预编译
pattern = re.compile(r'\w+@\w+\.\w+')
def test_compile():
    start = time.time()
    for _ in range(100000):
        pattern.search(text)
    return time.time() - start

print(f"不编译: {test_no_compile():.3f}s")
print(f"预编译: {test_compile():.3f}s")

# 结果：预编译快2-3倍
```

### 避免回溯

```python
import re

# 危险的正则（可能导致灾难性回溯）
bad_pattern = r'(a+)+b'
# 匹配 "aaaaaaaaaaaaaaaaaac" 会非常慢

# 安全的正则
good_pattern = r'a+b'

# 测试
import time
text = 'a' * 30 + 'c'

start = time.time()
try:
    re.search(bad_pattern, text, timeout=1)  # Python 3.11+
except:
    pass
print(f"危险模式: {time.time() - start:.3f}s")

start = time.time()
re.search(good_pattern, text)
print(f"安全模式: {time.time() - start:.6f}s")
```

### 使用re.Scanner

```python
import re

# 词法分析器
def scanner_example():
    tokens = [
        ('NUMBER', r'\d+'),
        ('WORD', r'\w+'),
        ('SPACE', r'\s+'),
        ('PUNCT', r'[^\w\s]'),
    ]
    
    pattern = '|'.join(f'(?P<{name}>{regex})' for name, regex in tokens)
    
    text = "Hello 123 world!"
    
    for match in re.finditer(pattern, text):
        kind = match.lastgroup
        value = match.group()
        print(f"{kind}: {value}")

scanner_example()
```

---

## 避坑指南

### 坑1：忘记转义

```python
import re

# . 在正则中表示任意字符
# 如果想匹配真正的点，需要转义

text = "file.txt file2txt"

# 错误：匹配了file.txt和file2txt
result = re.findall(r'file.txt', text)
print(result)  # ['file.txt', 'file2txt']

# 正确：转义点
result = re.findall(r'file\.txt', text)
print(result)  # ['file.txt']
```

### 坑2：贪婪匹配陷阱

```python
import re

text = "<div>内容1</div><div>内容2</div>"

# 错误：贪婪匹配
result = re.findall(r'<div>.*</div>', text)
print(result)  # ['<div>内容1</div><div>内容2</div>']

# 正确：非贪婪匹配
result = re.findall(r'<div>.*?</div>', text)
print(result)  # ['<div>内容1</div>', '<div>内容2</div>']
```

### 坑3：中文字符匹配

```python
import re

text = "Hello 世界 Python"

# \w 不匹配中文
result = re.findall(r'\w+', text)
print(result)  # ['Hello', 'Python']

# 匹配中文
result = re.findall(r'[\u4e00-\u9fa5]+', text)
print(result)  # ['世界']

# 匹配所有字符（包括中文）
result = re.findall(r'[\u4e00-\u9fa5\w]+', text)
print(result)  # ['Hello', '世界', 'Python']
```

### 坑4：多行匹配

```python
import re

text = """第一行
第二行
第三行"""

# ^只匹配开头
result = re.findall(r'^第', text)
print(result)  # ['第']

# 使用多行模式
result = re.findall(r'^第', text, re.MULTILINE)
print(result)  # ['第', '第', '第']
```

### 坑5：特殊字符处理

```python
import re

# 用户输入的正则表达式可能包含特殊字符
user_input = "file.txt"
pattern = re.escape(user_input)  # 自动转义

result = re.findall(pattern, "file.txt file2txt")
print(result)  # ['file.txt']
```

---

## 推荐：AI Python零基础实战营

想系统学习Python文本处理？

**课程内容：**
- ✅ Python基础语法
- ✅ 正则表达式详解
- ✅ 数据清洗与处理
- ✅ 实战项目练习

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 相关阅读

- [Python字符串：我被忽略的20个实用方法](/course/AI相关/人民邮电出版社/ads/openclaw/python/12-Python字符串/)
- [Python文件操作：读写文件的10种姿势](/course/AI相关/人民邮电出版社/ads/openclaw/python/13-Python文件操作/)
- [Python字典：我用这个数据结构，把查询速度提升了100倍](/course/AI相关/人民邮电出版社/ads/openclaw/python/08-Python字典/)

---

*PS：正则表达式是程序员的必备技能。记不住没关系，收藏这篇当速查手册。记住：能用简单方法就别用复杂正则！*

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

