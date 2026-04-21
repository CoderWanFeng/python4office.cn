---
title: Python字符串：我被忽略的20个实用方法，效率提升3倍
date: 2026-02-28 18:57:00
tags: [Python基础, 字符串, 编程技巧]
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

今天分享一个让我代码效率提升3倍的秘密——**Python字符串的20个实用方法**。

> 💡 **场景**：你有一段用户输入的文本，需要：去掉空格、转成小写、验证格式、提取关键词……如果一个个手写，要写几十行代码。学会字符串方法，一行搞定！

---

## 1. 大小写转换（3个）

```python
text = "Hello World"

print(text.upper())      # HELLO WORLD（全部大写）
print(text.lower())      # hello world（全部小写）
print(text.title())      # Hello World（每个单词首字母大写）
print(text.capitalize()) # Hello world（只有第一个字母大写）
print(text.swapcase())   # hELLO wORLD（大小写互换）
```

**实战：忽略大小写比对**

```python
answer = input("请输入YES继续：").lower().strip()

if answer == "yes":
    print("继续执行")
else:
    print("无效输入")

# 输入: YES  → 输出: 继续执行
# 输入: yes  → 输出: 继续执行
# 输入: No   → 输出: 无效输入
```

---

## 2. 查找与替换（4个）

```python
text = "Python is easy, Python is powerful"

# 查找位置（找不到返回-1）
print(text.find("Python"))     # 0
print(text.find("Java"))       # -1

# 统计出现次数
print(text.count("Python"))    # 2

# 替换
print(text.replace("Python", "JavaScript"))
# JavaScript is easy, JavaScript is powerful

# 只替换前N次
print(text.replace("Python", "JS", 1))
# JS is easy, Python is powerful
```

---

## 3. 判断方法（6个）

判断字符串是否符合某种规则。

```python
filename = "report.pdf"

# 判断开头/结尾
print(filename.startswith("report"))  # True
print(filename.endswith(".pdf"))      # True
print(filename.endswith((".pdf", ".docx")))  # True（支持元组）

# 判断类型
print("123".isdigit())      # True（纯数字）
print("abc".isalpha())      # True（纯字母）
print("abc123".isalnum())   # True（字母或数字）
print("   ".isspace())      # True（纯空格）
print("HELLO".isupper())    # True（全大写）
print("hello".islower())    # True（全小写）
```

**实战：验证文件类型**

```python
def is_image(filename):
    return filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))

print(is_image("photo.JPG"))    # True
print(is_image("document.pdf")) # False
```

---

## 4. 去除空白（3个）

```python
text = "  hello world  \n\t"

print(text.strip())   # "hello world"（两边都去掉）
print(text.lstrip())  # "hello world  \n\t"（只去左边）
print(text.rstrip())  # "  hello world"（只去右边）

# 去掉指定字符
print("...hello...".strip('.'))  # "hello"
```

**实战：处理用户输入**

```python
username = "  john  "
username = username.strip()  # 去掉首尾空格
print(f"欢迎，{username}！")
# 输出：欢迎，john！
```

---

## 5. 对齐与填充（3个）

```python
text = "Python"

print(text.center(20))       # "       Python       "（居中）
print(text.center(20, '-')) # "-------Python-------"（用-填充）
print(text.ljust(20, '*'))  # "Python**************"（左对齐）
print(text.rjust(20, '*'))  # "**************Python"（右对齐）

# 数字补零
print("42".zfill(5))  # "00042"
```

**实战：格式化表格输出**

```python
products = [
    ("Apple", 5.5),
    ("Banana", 3.0),
    ("Cherry", 12.5)
]

for name, price in products:
    print(f"{name.ljust(10)} ${price:.2f}")

# 输出：
# Apple      $5.50
# Banana     $3.00
# Cherry     $12.50
```

---

## 6. 分割与合并

```python
# 按空白分割（自动处理多个空格）
print("a  b\tc\nd".split())  # ['a', 'b', 'c', 'd']

# 按行分割
text = """第一行
第二行
第三行"""
print(text.splitlines())  # ['第一行', '第二行', '第三行']

# 分割成三部分
print("key=value".partition("="))  # ('key', '=', 'value')

# 合并
words = ['hello', 'world']
print(" ".join(words))  # hello world
print("-".join(words))  # hello-world
```

---

## 7. 格式化 f-string

最常用的字符串拼接方式。

```python
name = "张三"
age = 25
score = 92.5

# 基本用法
print(f"我是{name}，今年{age}岁")

# 数字格式化
print(f"成绩：{score:.1f}")     # 成绩：92.5
print(f"比例：{0.258:.1%}")     # 比例：25.8%
print(f"对齐：{name:>10}")      # 对齐：         张三
```

---


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


## 本讲小结

| 分类 | 常用方法 |
|-----|---------|
| 大小写 | `.upper()`, `.lower()`, `.title()` |
| 查找 | `.find()`, `.count()`, `.replace()` |
| 判断 | `.startswith()`, `.endswith()`, `.isdigit()` |
| 去除 | `.strip()`, `.lstrip()`, `.rstrip()` |
| 对齐 | `.center()`, `.ljust()`, `.zfill()` |
| 分割 | `.split()`, `.splitlines()`, `.join()` |

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

