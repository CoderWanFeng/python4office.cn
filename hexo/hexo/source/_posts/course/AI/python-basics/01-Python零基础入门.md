---
title: Python零基础入门：写下你的第一行代码，开启编程之旅
date: 2026-02-28 19:54:00
tags: [Python基础, 入门, 零基础]
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

## 一个真实的故事

2024年，我的一个读者小王发微信给我：

> "晚枫老师，我花了3个月学Java，现在连个Excel自动处理的小工具都写不出来。是不是我太笨了？"

我问他："你为什么要学Java？"

他说："网上说Java就业前景好..."

我给他发了一个Python脚本，3行代码就能自动处理Excel。他惊呆了。

**很多时候，不是你不够努力，而是选择比努力更重要。**

如果你是想快速实现自动化办公、数据分析、或者AI应用开发，Python就是你的最佳选择。这篇文章，我会用最通俗的语言，带你写下第一行Python代码。

不需要任何前置知识，跟着做就行。

---

## 为什么要学Python？

在开始前，先说说为什么Python是初学者的最佳选择：

✅ **语法简单**：接近自然语言，容易理解
✅ **应用广泛**：数据分析、AI、自动化、Web开发都能做
✅ **生态丰富**：有成千上万的免费工具包
✅ **社区活跃**：遇到问题很容易找到答案

**2026年了，Python依然是最值得学的编程语言。**

### 与其他语言的对比

让我们看看Python和其他语言的代码对比：

**打印Hello World：**

```python
# Python - 1行代码
print("Hello, World!")
```

```java
// Java - 5行代码
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

```c
// C语言 - 4行代码
#include <stdio.h>
int main() {
    printf("Hello, World!\n");
    return 0;
}
```

看出差距了吗？Python用1行代码做的事，Java要用5行。**这就是Python的哲学：简单优于复杂。**

### Python的应用领域

你可能不知道，这些都在用Python：

| 领域 | 典型应用 | 案例 |
|------|----------|------|
| 📊 数据分析 | 数据清洗、可视化 | Excel自动化、报表生成 |
| 🤖 AI/机器学习 | 模型训练、推理 | ChatGPT、Stable Diffusion |
| 🌐 Web开发 | 后端服务 | Instagram、YouTube |
| 🧪 自动化测试 | 脚本测试 | 自动化测试框架 |
| 📱 爬虫 | 数据采集 | 价格监控、舆情分析 |
| 🔧 运维脚本 | 自动化部署 | 服务器管理 |

---

## 第一步：安装Python

### Windows用户

**方法一：官网下载（推荐新手）**
1. 访问 [python.org](https://www.python.org/downloads/)
2. 下载最新版Python（建议3.10+，当前最新是3.13）
3. **重要**：安装时勾选"Add Python to PATH"（这个一定要勾选！）
4. 点击 Install Now

**方法二：Microsoft Store**
1. 打开 Microsoft Store
2. 搜索 "Python"
3. 点击安装

### Mac用户

**方法一：Homebrew安装（推荐）**
```bash
# 先安装Homebrew（如果没有）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装Python
brew install python

# 验证安装
python3 --version
```

**方法二：官网下载**
直接从 python.org 下载 macOS 安装包，双击安装即可。

### Linux用户

大多数Linux发行版已经预装了Python。如果没有：

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3

# CentOS/RHEL
sudo yum install python3
```

### 验证安装成功

打开终端/命令行，输入：

```bash
# Windows
python --version

# Mac/Linux
python3 --version
```

看到版本号（如 `Python 3.13.0`），说明安装成功！

**常见问题：**

```bash
# Windows上可能出现的问题
'python' 不是内部或外部命令

# 解决方法：
# 1. 确认安装时勾选了"Add Python to PATH"
# 2. 或者使用 py 命令代替 python
py --version
```

---

## 第二步：选择编辑器

推荐几个适合新手的编辑器：

### VS Code（强烈推荐）

**优点：**
- 免费、轻量、启动快
- 插件生态丰富
- 微软官方维护
- 支持多种编程语言

**安装步骤：**
1. 下载 [VS Code](https://code.visualstudio.com/)
2. 安装 Python 插件（打开VS Code，按 `Cmd+,` 打开设置，搜索 Python，安装官方插件）

**推荐插件：**
- Python（微软官方）
- Pylance（智能提示）
- Python Indent（缩进辅助）
- Code Runner（一键运行）

### PyCharm Community

**优点：**
- Python专用IDE，功能强大
- 智能提示非常完善
- 调试功能强大

**缺点：**
- 比较重，启动慢
- Community版功能够用，Professional版收费

### Jupyter Notebook

**优点：**
- 交互式编程，适合学习
- 可以一行一行执行看结果
- 支持Markdown笔记

**适合场景：**
- 数据分析
- 学习阶段
- 算法验证

```bash
# 安装Jupyter
pip install jupyter

# 启动
jupyter notebook
```

### IDLE（Python自带）

Python安装后自带的编辑器，功能简单，但不需要额外安装。

**适合场景：**
- 临时测试小段代码
- 不想安装其他编辑器时

---

## 第三步：写下第一行代码

### 方法一：交互式命令行

打开终端，输入 `python`（Mac/Linux输入 `python3`），进入交互模式：

```bash
$ python
Python 3.13.0 (main, Oct 16, 2026)
>>> print("Hello, World!")
Hello, World!
>>> print("你好，Python！")
你好，Python！
>>> exit()  # 退出
```

### 方法二：创建脚本文件（推荐）

创建一个文件 `hello.py`，写入：

```python
print("Hello, World!")
print("你好，Python！")
```

运行：
```bash
python hello.py
```

看到输出？恭喜你，你已经是程序员了！🎉

### 方法三：VS Code中运行

1. 在VS Code中打开 `hello.py`
2. 点击右上角的运行按钮（▶️）
3. 或右键选择"在终端中运行Python文件"

---

## 深入理解print函数

`print()` 是Python最常用的函数之一，作用是在屏幕显示内容。让我们深入了解它。

### 基础用法

```python
# 打印文字
print("Hello, Python!")

# 打印数字
print(123)
print(3.14)

# 打印布尔值
print(True)
print(False)
```

### 打印多个内容

```python
# 用逗号分隔，自动添加空格
print("姓名:", "张三", "年龄:", 25)
# 输出：姓名: 张三 年龄: 25

# 打印不同类型的数据
print("价格:", 99.9, "元")
# 输出：价格: 99.9 元
```

### sep参数：自定义分隔符

```python
# 默认是用空格分隔
print("A", "B", "C")  # A B C

# 用短横线分隔
print("A", "B", "C", sep="-")  # A-B-C

# 用逗号分隔
print("2024", "01", "15", sep="/")  # 2024/01/15

# 不分隔
print("A", "B", "C", sep="")  # ABC

# 用换行分隔
print("第一行", "第二行", "第三行", sep="\n")
```

### end参数：自定义结束符

```python
# 默认是换行
print("第一行")
print("第二行")
# 输出：
# 第一行
# 第二行

# 不换行
print("Loading", end="...")
print("Done!")
# 输出：Loading...Done!

# 制作进度条效果
import time
for i in range(5):
    print(f"\r进度: {(i+1)*20}%", end="")
    time.sleep(0.5)
print("\n完成！")
```

### file参数：输出到文件

```python
# 输出到文件
with open("output.txt", "w", encoding="utf-8") as f:
    print("这一行会写入文件", file=f)
    print("而不是打印到屏幕", file=f)
```

### flush参数：立即刷新

```python
import time

# 默认不立即刷新
print("正在加载", end="")
for i in range(3):
    time.sleep(1)
    print(".", end="")
# 会等所有print执行完才显示

# 立即刷新
print("正在加载", end="", flush=True)
for i in range(3):
    time.sleep(1)
    print(".", end="", flush=True)
# 每个点立即显示
```

### 实战：美化输出

```python
# 分隔线
print("=" * 50)
print("欢迎使用Python自动化办公系统".center(46))
print("=" * 50)

# 表格输出
print("-" * 40)
print(f"{'姓名':<10}{'年龄':^10}{'城市':>10}")
print("-" * 40)
print(f"{'张三':<10}{25:^10}{'北京':>10}")
print(f"{'李四':<10}{30:^10}{'上海':>10}")
print("-" * 40)

# 带颜色的输出（需要支持ANSI的终端）
print("\033[31m红色文字\033[0m")
print("\033[32m绿色文字\033[0m")
print("\033[33m黄色文字\033[0m")
```

---

## Python的注释

注释是给程序员看的，程序会忽略它。

### 单行注释

```python
# 这是单行注释
print("Hello")  # 这也是注释，写在代码后面
```

### 多行注释

```python
"""
这是多行注释
也叫文档字符串（docstring）
可以跨越多行
通常用于函数或类的说明
"""

'''
单引号也可以
效果和双引号一样
'''
```

### 文档字符串（docstring）

```python
def calculate_sum(a, b):
    """
    计算两个数的和
    
    参数:
        a: 第一个数
        b: 第二个数
    
    返回:
        两数之和
    """
    return a + b

# 查看函数文档
print(calculate_sum.__doc__)
```

### 注释的最佳实践

```python
# ❌ 不好的注释
x = x + 1  # x加1

# ✅ 好的注释
x = x + 1  # 补偿边界值的影响

# ❌ 无意义的注释
# 打印Hello
print("Hello")

# ✅ 解释原因的注释
# 使用二分查找提高查找效率
index = binary_search(arr, target)
```

**黄金法则**：注释应该解释"为什么"，而不是"是什么"。

---

## Python代码规范

Python有一套官方的代码风格指南，叫 PEP 8。虽然不会强制要求，但遵循它能让你的代码更专业。

### 缩进

```python
# ✅ 正确：使用4个空格缩进
if True:
    print("Yes")

# ❌ 错误：使用Tab（虽然能运行，但不推荐）
if True:
	print("Yes")

# ❌ 错误：缩进不一致
if True:
    print("Yes")
  print("No")  # 这行会报错
```

### 命名规范

```python
# 变量名：小写+下划线
user_name = "张三"
total_count = 100

# 常量名：大写+下划线
MAX_SIZE = 100
PI = 3.14159

# 函数名：小写+下划线
def calculate_total():
    pass

# 类名：驼峰命名法
class UserProfile:
    pass
```

### 行长度

```python
# 每行不超过79个字符（PEP 8建议）
# 超长时可以换行

# 方法一：使用括号
long_string = (
    "这是一个很长的字符串"
    "可以分成多行写"
    "Python会自动连接"
)

# 方法二：使用反斜杠（不推荐）
long_string = "这是一个很长的字符串" \
              "可以分成多行写"
```

---

## 第一个小练习

试着完成这个程序，把信息换成你自己的：

```python
# ========== 个人信息展示 ==========
print("=" * 40)
print("个人信息".center(34))
print("=" * 40)
print("姓名:", "张三")
print("年龄:", 25)
print("职业:", "Python开发者")
print("爱好:", "编程", "阅读", "旅行", sep=" | ")
print("=" * 40)
```

**进阶练习：** 制作一个名片程序

```python
# 名片生成器
name = input("请输入姓名: ")
title = input("请输入职位: ")
company = input("请输入公司: ")
phone = input("请输入电话: ")

print("\n" + "=" * 40)
print(f"{name} - {title}".center(34))
print("=" * 40)
print(f"公司: {company}")
print(f"电话: {phone}")
print(f"邮箱: {phone}@example.com")
print("=" * 40)
```

---

## 避坑指南：常见错误

### 错误1：拼写错误

```python
# ❌ 错误
Print("Hello")  # Python区分大小写
printt("Hello")  # 拼写错误

# ✅ 正确
print("Hello")
```

**错误信息：**
```
NameError: name 'Print' is not defined
```

### 错误2：引号不匹配

```python
# ❌ 错误
print("Hello')   # 引号不匹配
print('Hello")   # 引号不匹配

# ✅ 正确
print("Hello")
print('Hello')
print("""Hello""")  # 三引号也可以
```

### 错误3：中英文符号混淆

```python
# ❌ 错误：使用了中文标点
print（"Hello"）  # 中文括号
print"Hello"     # 缺少括号

# ✅ 正确：使用英文标点
print("Hello")
```

**这是新手最容易犯的错误！** 如果代码看起来没错但就是报错，检查一下是不是用了中文标点。

### 错误4：缩进错误

```python
# ❌ 错误
print("第一行")
  print("第二行")  # 不要无故缩进

# ✅ 正确
print("第一行")
print("第二行")
```

**错误信息：**
```
IndentationError: unexpected indent
```

### 错误5：忘记引号

```python
# ❌ 错误
print(Hello)  # 字符串需要引号

# ✅ 正确
print("Hello")
```

**错误信息：**
```
NameError: name 'Hello' is not defined
```

### 错误6：括号不匹配

```python
# ❌ 错误
print("Hello"  # 缺少右括号

# ✅ 正确
print("Hello")
```

### 错误7：混用Tab和空格

```python
# ❌ 错误：混用Tab和空格
if True:
	print("Tab缩进")    # Tab
    print("空格缩进")   # 空格

# ✅ 正确：统一使用空格（推荐4个空格）
if True:
    print("统一缩进")
    print("代码更整洁")
```

**解决方法：** 在编辑器中设置"将Tab转换为空格"。

---

## 实战案例：自动化欢迎程序

让我们把学到的知识用起来，写一个实用的欢迎程序：

```python
"""
自动化欢迎程序
作者：程序员晚枫
功能：显示欢迎信息和用户配置
"""

import os
import platform
from datetime import datetime

# 获取当前时间
now = datetime.now()
hour = now.hour

# 根据时间判断问候语
if hour < 12:
    greeting = "早上好"
elif hour < 18:
    greeting = "下午好"
else:
    greeting = "晚上好"

# 获取系统信息
system = platform.system()
user = os.environ.get('USERNAME', 'User')

# 打印欢迎信息
print("\n" + "=" * 50)
print(f"{greeting}，{user}！".center(44))
print("=" * 50)
print(f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"操作系统: {system}")
print(f"Python版本: {platform.python_version()}")
print("=" * 50)
print("提示: 今天也要加油学习Python哦！".center(40))
print("=" * 50 + "\n")
```

**运行效果：**
```
==================================================
               下午好，WanFeng！
==================================================
当前时间: 2026-04-23 14:30:00
操作系统: macOS
Python版本: 3.13.0
==================================================
          提示: 今天也要加油学习Python哦！          
==================================================
```

---

## 进阶：理解Python的执行原理

你可能好奇，Python代码是怎么运行的？

### 编译型 vs 解释型

```
编译型语言（如C/C++）：
源代码 → 编译器 → 机器码 → CPU执行

解释型语言（如Python）：
源代码 → 解释器 → 逐行执行
```

### Python的运行过程

```python
# hello.py
print("Hello")
```

1. **词法分析**：把代码分解成token
   ```
   print → NAME
   (     → LPAR
   "Hello" → STRING
   )     → RPAR
   ```

2. **语法分析**：构建语法树（AST）
   ```
   Call(func=Name('print'), args=[Str('Hello')])
   ```

3. **编译成字节码**：生成 .pyc 文件
   ```
   LOAD_GLOBAL     0 (print)
   LOAD_CONST      0 ('Hello')
   CALL_FUNCTION   1
   POP_TOP
   ```

4. **Python虚拟机执行**：逐条执行字节码

**为什么要了解这个？**

理解Python的执行原理，能帮你：
- 更好地理解错误信息
- 写出更高效的代码
- 使用调试工具排查问题

---

## 性能对比：print的不同写法

虽然 `print()` 很简单，但不同的写法性能有差异：

```python
import timeit

# 方法1：多个print
def method1():
    print("A")
    print("B")
    print("C")

# 方法2：单个print多行
def method2():
    print("A\nB\nC")

# 方法3：sep参数
def method3():
    print("A", "B", "C", sep="\n")

# 性能测试
print("方法1:", timeit.timeit(method1, number=10000))
print("方法2:", timeit.timeit(method2, number=10000))
print("方法3:", timeit.timeit(method3, number=10000))
```

**结论：** 方法2（单个print多行）最快，因为减少了函数调用次数。

但在实际开发中，**可读性比性能更重要**。除非你在写性能敏感的代码，否则选择最清晰的写法。

---

## 调试技巧

当你遇到错误时，如何调试？

### 方法1：打印调试

```python
# 最简单的方法：打印中间结果
a = 10
b = 20
print(f"a = {a}, b = {b}")  # 调试信息
result = a + b
print(f"result = {result}")  # 调试信息
```

### 方法2：使用type()检查类型

```python
value = "123"
print(type(value))  # <class 'str'>
print(type(int(value)))  # <class 'int'>
```

### 方法3：使用dir()查看属性

```python
text = "Hello"
print(dir(text))  # 查看字符串的所有方法
```

### 方法4：使用help()查看帮助

```python
help(print)  # 查看print函数的帮助文档
```

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

## 下节预告

下一篇我们将学习**变量和数据类型**，这是编程的基础概念。

你将学会：
- 什么是变量，为什么需要变量
- Python有哪些数据类型
- 如何进行基本的数学运算
- 字符串的常用操作

👉 **[继续阅读：Python变量与数据类型完全指南](/course/AI相关/人民邮电出版社/ads/openclaw/python/02-Python变量与数据类型/)**

---

## 推荐：AI Python零基础实战营

如果你想系统学习Python：

**课程内容：**
- ✅ 从零开始，手把手教学
- ✅ 30讲视频课程
- ✅ 15+实战项目
- ✅ 专属答疑群

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 相关阅读

- [Python变量与数据类型完全指南](/course/AI相关/人民邮电出版社/ads/openclaw/python/02-Python变量与数据类型/)
- [零基础学AI编程：30天速成计划](/course/AI相关/人民邮电出版社/ads/openclaw/python/20260228171202-零基础学AI编程-30天速成计划/)
- [Python环境搭建完全指南](https://www.python4office.cn/python-env/)

---

## 📚 推荐教材

**主教材**：[《Python 编程从入门到实践（第 3 版）》](https://u.jd.com/NGMHz3T)

这本书的特点：
- 零基础友好，循序渐进
- 项目驱动，边学边练
- 涵盖Web开发、数据可视化、游戏开发

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

---

*PS：万事开头难，但你已经迈出了第一步。记住，每个程序员都是从print("Hello, World!")开始的。继续加油！*

*2026-04-23 更新 by 程序员晚枫*
