---
title: Python条件判断：我用if-else写出了会思考的程序
date: 2026-02-28 19:57:00
tags: [Python基础, 条件判断, if-else]
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

上篇我们学了运算符，会做比较和判断了。这篇来学**条件判断**——让程序自己"做决定"。

学完这篇，你的程序就不再是死板地执行一条条命令，而是能根据不同情况走不同的路了。

---

## 生活中的条件判断

你每天都在做条件判断，只是没意识到：

```
如果（今天下雨）→ 带伞
否则 → 不带伞

如果（余额>=票价）→ 可以买
否则 → 回家取钱
```

**条件判断就是程序里的"如果...否则..."**

---

## if语句：最基本的判断

### 场景举例

你去买奶茶，如果余额足够，就买：

```python
balance = 15   # 钱包里有15元
price = 12      # 奶茶12元

if balance >= price:      # 如果余额 >= 价格
    print("买！奶茶真香~")

print("程序结束")
```

**运行结果：**

```
买！奶茶真香~
程序结束
```

> 💡 **语法要点**：if后面跟一个条件（结果必须是True或False），条件成立后，才会执行缩进的代码。

---

## if-else：两个分支

只有一个分支不够用——如果条件不成立呢？

```python
balance = 8    # 只有8元
price = 12     # 奶茶12元

if balance >= price:
    print("买！奶茶真香~")
else:           # 余额不够的情况
    print("算了，奶茶太贵，喝白开水吧")
```

**运行结果：**

```
算了，奶茶太贵，喝白开水吧
```

---

## if-elif-else：多个条件分支

生活中的判断往往不止两个选项。比如考试成绩：

```
- 90分以上：A（优秀）
- 80~89分：B（良好）
- 60~79分：C（及格）
- 60分以下：D（不及格）
```

用 `elif`（else if 的缩写）来处理多个条件：

```python
score = 73

if score >= 90:
    grade = "A（优秀）"
elif score >= 80:
    grade = "B（良好）"
elif score >= 60:
    grade = "C（及格）"
else:
    grade = "D（不及格）"

print(f"你的成绩等级：{grade}")
```

**运行结果：**

```
你的成绩等级：C（及格）
```

> 💡 **执行顺序**：Python从上往下看，遇到第一个满足的条件就执行对应的代码块，然后**跳过其余所有elif/else**，不会再看了。所以要把范围小的条件写在前面。

---

## 嵌套条件：条件里还有条件

假设你要判断：是不是会员？会员的话是否满100元？如果两个都满足，就打8折：

```python
is_vip = True
balance = 150

if is_vip:
    if balance >= 100:
        discount = 0.8
        print(f"VIP满减价：¥{balance * discount}")
    else:
        discount = 0.9
        print(f"VIP普通价：¥{balance * discount}")
else:
    print(f"普通价：¥{balance}")
```

**运行结果：**

```
VIP满减价：¥120.0
```

> ⚠️ **嵌套别太深**：嵌套超过3层，代码就变得很难读懂了。如果逻辑复杂，考虑拆成多个变量或者多个函数。

---

## 简化写法：三元运算符

简单的 if-else 可以写成一行，更简洁：

```python
age = 20

# 传统写法（4行）
if age >= 18:
    status = "成年"
else:
    status = "未成年"

# 简化写法（1行）
status = "成年" if age >= 18 else "未成年"

print(status)
```

**运行结果：**

```
成年
```

**格式**：`值1 if 条件 else 值2`

---

## 常见判断模式

### ① 判断是否为空

```python
name = ""

# ❌ 不推荐：显式比较
if name == "":
    print("名字不能为空")

# ✅ 推荐：空字符串在条件里自动视为False
if not name:
    print("名字不能为空")
```

### ② 同时满足多个条件

```python
age = 25
has_ticket = True

# 两个都要满足（and）
if age >= 18 and has_ticket:
    print("可以入场")
```

### ③ 满足任一条件

```python
day = "周六"

# 满足任一条件就行（or）
if day == "周六" or day == "周日":
    print("周末快乐！")
```

### ④ 判断是否在范围内

```python
score = 85

# Python支持这种写法，比 60<=score and score<=100 更直观
if 60 <= score <= 100:
    print("成绩有效")
```

### ⑤ 判断元素是否在列表里

```python
fruits = ["苹果", "香蕉", "橙子"]

if "苹果" in fruits:
    print("有苹果！可以做个苹果派")
```

---

## 避坑指南

### ❌ 坑1：忘记缩进

Python靠缩进判断代码属于哪个块，忘了缩进就会报错：

```python
age = 20

if age >= 18:
print("成年")    # ❌ 缩进错误！会报错 IndentationError
    print("成年") # ✅ 正确：4个空格缩进
```

### ❌ 坑2：把 `=` 和 `==` 搞混

`=` 是赋值（把右边的值存进左边），`==` 是比较（左右是否相等）：

```python
x = 5

if x == 10:   # ✅ 正确：比较x和10是否相等
    print("x是10")

if x = 10:    # ❌ 错误：这是把10赋值给x，不是比较
```

### ❌ 坑3：条件写反了

```python
age = 20

# ❌ 这个条件永远为True：20永远不小于12
if age > 18 and age < 12:
    print("...")

# ✅ 正确
if age < 12 or age > 65:
    print("享受优惠票")
```

---

## 实战练习：智能客服机器人

写一个根据关键词自动回复的客服程序：

```python
def smart_reply(message):
    """根据用户消息返回自动回复"""
    message = message.lower()  # 统一转成小写，方便匹配

    if "价格" in message or "多少钱" in message:
        return "基础版免费，专业版¥99/月，企业版¥399/月"
    elif "退款" in message or "退货" in message:
        return "7天无理由退款，请联系客服：400-123-4567"
    elif "账号" in message or "登录" in message:
        return "请尝试重置密码，或发送'人工'转人工客服"
    elif "谢谢" in message:
        return "不客气！有其他问题随时找我 😊"
    else:
        return "抱歉，我没听懂你的问题。请输入'人工'转人工客服"

# 模拟几次对话
questions = [
    "这个软件多少钱？",
    "我想退款怎么办",
    "我登录不上账号",
    "谢谢你的帮助"
]

print("🤖 智能客服已上线\n")
for q in questions:
    print(f"用户：{q}")
    print(f"客服：{smart_reply(q)}\n")
```

**运行结果：**

```
🤖 智能客服已上线

用户：这个软件多少钱？
客服：基础版免费，专业版¥99/月，企业版¥399/月

用户：我想退款怎么办
客服：7天无理由退款，请联系客服：400-123-4567

用户：我登录不上账号
客服：请尝试重置密码，或发送'人工'转人工客服

用户：谢谢你的帮助
客服：不客气！有其他问题随时找我 😊
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

| 语法 | 说明 |
|-----|------|
| `if 条件:` | 如果满足条件，执行下面的代码 |
| `else:` | 前面条件不满足时，执行这里 |
| `elif 条件:` | 前面的if不满足，再来判断这个 |
| `条件1 and 条件2` | 两个都要满足 |
| `条件1 or 条件2` | 满足任一个就行 |
| `not 条件` | 取反 |
| `值1 if 条件 else 值2` | 三元运算符，简化写法 |

---

## 下节预告

学会了做选择，下一篇来学**循环**——让程序自动重复做事，批量处理大量数据。

👉 **[继续阅读：Python循环](./05-Python循环.md)**

---

## 课程导航

**上一篇：** [Python运算符与表达式](./03-Python运算符与表达式.md)

**下一篇：** [Python循环-for和while完全指南](./05-Python循环.md)

---

*PS：条件判断让程序拥有了"智慧"。多观察生活中的"如果...否则..."，编程思维就慢慢养成了。*

