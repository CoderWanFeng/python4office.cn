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

## 一个真实的故事

2024年，有个读者找我求助：

> "晚枫老师，我写了一个自动发邮件的脚本，结果半夜给我老板发了100封一样的邮件！怎么回事？"

我看了一眼他的代码：

```python
# 发送邮件
send_email()

# 这里应该判断是否发送成功，但没有
log("邮件发送成功")
```

**问题在于：代码没有判断发送是否成功，就直接记录"成功"了。**

如果加了条件判断：

```python
# 发送邮件
if send_email():  # 判断是否成功
    log("邮件发送成功")
else:
    log("发送失败，正在重试...")
    retry_send()
```

这就是条件判断的价值——**让程序会思考，而不是盲目执行**。

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

如果（时间>=22:00 且 没有急事）→ 睡觉
否则 → 继续工作
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

### if语句的语法规则

```python
if 条件:
    # 条件为True时执行的代码
    代码块1
    代码块2
```

**要点：**
1. `if` 后面跟一个条件（结果必须是 True 或 False）
2. 条件后面要加冒号 `:`
3. 缩进的代码块在条件成立时执行
4. Python 靠缩进判断代码块的范围（推荐4个空格）

### 条件可以是任何表达式

```python
# 比较表达式
if age >= 18:
    print("成年")

# 逻辑表达式
if has_ticket and age >= 18:
    print("可以进场")

# 函数返回值
if is_valid_email(email):
    print("邮箱格式正确")

# 成员判断
if "admin" in username:
    print("管理员账号")

# 布尔值直接判断
if is_logged_in:
    print("已登录")
```

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

### else的作用

`else` 是"否则"的意思，当 `if` 条件不成立时执行：

```python
if 条件:
    # 条件为True时执行
    代码块A
else:
    # 条件为False时执行
    代码块B
```

**注意：** `else` 后面不需要条件，直接加冒号。

### 省略else的情况

如果条件不成立时什么都不做，可以省略 `else`：

```python
# 检查库存
stock = 0

if stock > 0:
    print("有库存，可以购买")
    # 没有 else，库存<=0时什么都不做

print("继续执行后面的代码")
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

### 执行顺序（重要！）

Python 从上往下检查，遇到第一个满足的条件就执行，然后**跳出整个结构**：

```python
score = 95

if score >= 60:
    print("及格")      # ✅ 会执行这个
elif score >= 80:
    print("良好")      # ❌ 不会执行
elif score >= 90:
    print("优秀")      # ❌ 不会执行（虽然也满足）

# 输出：及格
```

**正确写法：** 把范围小的条件写在前面：

```python
score = 95

if score >= 90:
    print("优秀")      # ✅ 执行这个
elif score >= 80:
    print("良好")      # ❌ 不会检查了
elif score >= 60:
    print("及格")      # ❌ 不会检查了

# 输出：优秀
```

### 多个elif的例子

```python
# 星期几的判断
day = 3

if day == 1:
    print("星期一，新的一周开始")
elif day == 2:
    print("星期二")
elif day == 3:
    print("星期三，一周过半")
elif day == 4:
    print("星期四")
elif day == 5:
    print("星期五，快周末了")
elif day == 6 or day == 7:
    print("周末愉快！")
else:
    print("输入错误，请输入1-7的数字")
```

---

## 嵌套条件：条件里还有条件

当需要多层判断时，可以在 `if` 里面再写 `if`：

### VIP折扣示例

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

### 登录验证示例

```python
username = "admin"
password = "123456"
is_active = True

if username == "admin":
    if password == "123456":
        if is_active:
            print("登录成功！欢迎回来")
        else:
            print("账号已被禁用，请联系管理员")
    else:
        print("密码错误")
else:
    print("用户名不存在")
```

### 嵌套层级建议

```python
# ❌ 嵌套太深（超过3层），难以阅读
if condition1:
    if condition2:
        if condition3:
            if condition4:
                if condition5:
                    print("太多了...")

# ✅ 使用 and 合并条件
if condition1 and condition2 and condition3:
    if condition4 and condition5:
        print("清晰多了")

# ✅ 提前返回（函数中）
def check_user(username, password):
    if username != "admin":
        return "用户名不存在"
    if password != "123456":
        return "密码错误"
    return "登录成功"
```

---

## 简化写法：三元运算符

简单的 if-else 可以写成一行，更简洁：

### 基本语法

```python
age = 20

# 传统写法（4行）
if age >= 18:
    status = "成年"
else:
    status = "未成年"

# 三元运算符（1行）
status = "成年" if age >= 18 else "未成年"

print(status)  # 成年
```

**格式：** `值1 if 条件 else 值2`

### 实际应用

```python
# 设置默认值
name = input("请输入姓名: ") or "匿名用户"
# 或者
name = input("请输入姓名: ")
name = name if name else "匿名用户"

# 条件赋值
score = 75
result = "及格" if score >= 60 else "不及格"

# 计算折扣
price = 100
is_vip = True
final_price = price * 0.8 if is_vip else price

# 在列表推导式中
numbers = [1, 2, 3, 4, 5]
labels = ["偶数" if n % 2 == 0 else "奇数" for n in numbers]
print(labels)  # ['奇数', '偶数', '奇数', '偶数', '奇数']
```

### 三元运算符的嵌套（不推荐）

```python
# ❌ 可读性差
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 60 else "D"

# ✅ 用 if-elif-else 更清晰
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"
```

---

## Python 3.10新特性：match-case

Python 3.10 引入了类似其他语言的 switch-case 结构：

### 基本用法

```python
day = 3

match day:
    case 1:
        print("星期一")
    case 2:
        print("星期二")
    case 3:
        print("星期三")
    case 4:
        print("星期四")
    case 5:
        print("星期五")
    case 6 | 7:  # 多个值用 | 连接
        print("周末")
    case _:  # 默认情况（类似 else）
        print("无效输入")
```

### 模式匹配

```python
# 匹配列表结构
point = [1, 2]

match point:
    case [0, 0]:
        print("原点")
    case [x, 0]:
        print(f"在x轴上，x={x}")
    case [0, y]:
        print(f"在y轴上，y={y}")
    case [x, y]:
        print(f"坐标：({x}, {y})")
```

### 匹配字典

```python
user = {"type": "vip", "level": 3}

match user:
    case {"type": "vip", "level": level} if level >= 5:
        print(f"高级VIP，等级：{level}")
    case {"type": "vip"}:
        print("普通VIP")
    case {"type": "normal"}:
        print("普通用户")
    case _:
        print("未知用户类型")
```

---

## 常见判断模式

### ① 判断是否为空

```python
name = ""
items = []
data = None

# ❌ 不推荐：显式比较
if name == "":
    print("名字不能为空")
if len(items) == 0:
    print("列表为空")

# ✅ 推荐：利用"假值"特性
if not name:
    print("名字不能为空")
if not items:
    print("列表为空")
if data is None:
    print("数据为None")
```

**Python中的"假值"：**
- `False`
- `None`
- `0`, `0.0`
- `""`（空字符串）
- `[]`, `{}`, `()`（空容器）

### ② 同时满足多个条件

```python
age = 25
has_ticket = True

# 两个都要满足（and）
if age >= 18 and has_ticket:
    print("可以入场")

# 更简洁的写法
if age >= 18 and has_ticket:  # 可以省略括号
    print("可以入场")
```

### ③ 满足任一条件

```python
day = "周六"

# 满足任一条件就行（or）
if day == "周六" or day == "周日":
    print("周末快乐！")

# 或者用 in
if day in ["周六", "周日"]:
    print("周末快乐！")
```

### ④ 判断是否在范围内

```python
score = 85

# ✅ Python的链式比较，非常优雅
if 60 <= score <= 100:
    print("成绩有效")

# ❌ 其他语言的写法（也能用，但不推荐）
if score >= 60 and score <= 100:
    print("成绩有效")
```

### ⑤ 判断元素是否在列表里

```python
fruits = ["苹果", "香蕉", "橙子"]

if "苹果" in fruits:
    print("有苹果！可以做个苹果派")

if "葡萄" not in fruits:
    print("没有葡萄")
```

### ⑥ 判断字典的键

```python
user = {"name": "张三", "age": 25}

# 判断键是否存在
if "name" in user:
    print(f"姓名：{user['name']}")

# 安全获取值
if "email" in user:
    email = user["email"]
else:
    email = "未设置"

# 或者用 get 方法（更推荐）
email = user.get("email", "未设置")
```

---

## 避坑指南

### ❌ 坑1：忘记缩进

Python靠缩进判断代码属于哪个块，忘了缩进就会报错：

```python
age = 20

if age >= 18:
print("成年")    # ❌ IndentationError: expected an indented block

# ✅ 正确
if age >= 18:
    print("成年")  # 4个空格缩进
```

### ❌ 坑2：把 `=` 和 `==` 搞混

```python
x = 5

if x == 10:   # ✅ 正确：比较x和10是否相等
    print("x是10")

if x = 10:    # ❌ SyntaxError: invalid syntax
    print("...")
```

**记忆技巧：**
- `=` 一个等号是"赋值"（把右边的值存到左边）
- `==` 两个等号是"比较"（左右是否相等）

### ❌ 坑3：条件写反了

```python
age = 20

# ❌ 这个条件永远为False：20不可能同时大于18又小于12
if age > 18 and age < 12:
    print("...")

# ✅ 如果想表达"儿童或老年人"
if age < 12 or age > 65:
    print("享受优惠票")

# ✅ 如果想表达"青少年"
if 12 <= age <= 18:
    print("青少年")
```

### ❌ 坑4：浮点数精度问题

```python
# ❌ 直接比较可能失败
result = 0.1 + 0.2
if result == 0.3:
    print("相等")  # 可能不会执行！

# ✅ 使用容差比较
import math
if math.isclose(result, 0.3):
    print("相等")
```

### ❌ 坑5：多余的else

```python
# ❌ 不必要的else
if x > 0:
    return True
else:
    return False

# ✅ 直接返回
return x > 0
```

### ❌ 坑6：使用is比较值

```python
# ❌ 不要用 is 比较值
x = 500
if x is 500:  # 可能是False
    print("相等")

# ✅ 用 == 比较值
if x == 500:
    print("相等")
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
    elif "人工" in message:
        return "正在为您转接人工客服，请稍候..."
    else:
        return "抱歉，我没听懂你的问题。请输入'人工'转人工客服"

# 模拟几次对话
questions = [
    "这个软件多少钱？",
    "我想退款怎么办",
    "我登录不上账号",
    "谢谢你的帮助",
    "你们营业时间？"
]

print("🤖 智能客服已上线\n")
print("=" * 40)
for q in questions:
    print(f"用户：{q}")
    print(f"客服：{smart_reply(q)}")
    print("-" * 40)
```

**运行结果：**

```
🤖 智能客服已上线

========================================
用户：这个软件多少钱？
客服：基础版免费，专业版¥99/月，企业版¥399/月
----------------------------------------
用户：我想退款怎么办
客服：7天无理由退款，请联系客服：400-123-4567
----------------------------------------
用户：我登录不上账号
客服：请尝试重置密码，或发送'人工'转人工客服
----------------------------------------
用户：谢谢你的帮助
客服：不客气！有其他问题随时找我 😊
----------------------------------------
用户：你们营业时间？
客服：抱歉，我没听懂你的问题。请输入'人工'转人工客服
----------------------------------------
```

### 实战练习：用户登录系统

```python
def login_system():
    """简单的登录系统"""
    # 模拟数据库
    users = {
        "admin": {"password": "admin123", "role": "管理员"},
        "user1": {"password": "user123", "role": "普通用户"},
        "vip": {"password": "vip123", "role": "VIP用户"}
    }
    
    print("=" * 40)
    print("欢迎登录系统".center(34))
    print("=" * 40)
    
    # 输入用户名和密码
    username = input("用户名：")
    password = input("密码：")
    
    # 判断用户名是否存在
    if username not in users:
        print("❌ 用户名不存在")
        return
    
    # 判断密码是否正确
    if users[username]["password"] != password:
        print("❌ 密码错误")
        return
    
    # 登录成功
    role = users[username]["role"]
    print(f"\n✅ 登录成功！")
    print(f"欢迎回来，{username}（{role}）")
    
    # 根据角色显示不同菜单
    if role == "管理员":
        print("\n管理员菜单：")
        print("1. 用户管理")
        print("2. 系统设置")
        print("3. 数据统计")
    elif role == "VIP用户":
        print("\nVIP用户菜单：")
        print("1. 查看报告")
        print("2. 下载资源")
    else:
        print("\n用户菜单：")
        print("1. 查看信息")
        print("2. 修改密码")

# 运行登录系统
if __name__ == "__main__":
    login_system()
```

### 实战练习：成绩管理系统

```python
def grade_management():
    """成绩管理系统"""
    print("=" * 50)
    print("成绩管理系统".center(44))
    print("=" * 50)
    
    while True:
        print("\n请选择操作：")
        print("1. 录入成绩")
        print("2. 查询成绩")
        print("3. 统计分析")
        print("0. 退出系统")
        
        choice = input("\n请输入选项：")
        
        if choice == "1":
            score = float(input("请输入成绩（0-100）："))
            if 0 <= score <= 100:
                if score >= 90:
                    grade = "A"
                elif score >= 80:
                    grade = "B"
                elif score >= 60:
                    grade = "C"
                else:
                    grade = "D"
                print(f"成绩：{score}，等级：{grade}")
            else:
                print("❌ 成绩必须在0-100之间")
        
        elif choice == "2":
            print("查询功能开发中...")
        
        elif choice == "3":
            print("统计功能开发中...")
        
        elif choice == "0":
            print("感谢使用，再见！")
            break
        
        else:
            print("❌ 无效选项，请重新输入")

if __name__ == "__main__":
    grade_management()
```

---

## 性能对比：不同的条件写法

```python
import timeit

# 方法1：多个 if
def method1(x):
    if x == 1:
        return "一"
    if x == 2:
        return "二"
    if x == 3:
        return "三"
    return "其他"

# 方法2：if-elif-else
def method2(x):
    if x == 1:
        return "一"
    elif x == 2:
        return "二"
    elif x == 3:
        return "三"
    else:
        return "其他"

# 方法3：字典映射
def method3(x):
    mapping = {1: "一", 2: "二", 3: "三"}
    return mapping.get(x, "其他")

# 方法4：match-case (Python 3.10+)
def method4(x):
    match x:
        case 1:
            return "一"
        case 2:
            return "二"
        case 3:
            return "三"
        case _:
            return "其他"

# 性能测试
print("多个if:", timeit.timeit(lambda: method1(3), number=1000000))
print("if-elif:", timeit.timeit(lambda: method2(3), number=1000000))
print("字典映射:", timeit.timeit(lambda: method3(3), number=1000000))
```

**结论：** 
- 字典映射最快（O(1)查找）
- if-elif 次之
- 多个 if 最慢（每次都要判断所有条件）

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
| `match x: case 1:` | Python 3.10+的模式匹配 |

---

## 下节预告

学会了做选择，下一篇来学**循环**——让程序自动重复做事，批量处理大量数据。

你将学会：
- for循环：遍历序列
- while循环：条件循环
- break和continue：控制循环
- 循环的高级用法

👉 **[继续阅读：Python循环](./05-Python循环.md)**

---

## 课程导航

**上一篇：** [Python运算符与表达式](./03-Python运算符与表达式.md)

**下一篇：** [Python循环-for和while完全指南](./05-Python循环.md)

---

## 相关阅读

- [Python变量与数据类型完全指南](./02-Python变量与数据类型.md)
- [零基础学AI编程：30天速成计划](/course/AI相关/人民邮电出版社/ads/openclaw/python/20260228171202-零基础学AI编程-30天速成计划/)

---

*PS：条件判断让程序拥有了"智慧"。多观察生活中的"如果...否则..."，编程思维就慢慢养成了。记住：好的代码要像人一样会做选择，而不是盲目执行。*

*2026-04-23 更新 by 程序员晚枫*
