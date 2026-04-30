---
title: 专题B 代码规范 — PEP 8入门指南
date: "2026-04-28 23:54:00"
tags: ["python", "入门", "课程", "专题"]
cover: "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop"
---


<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<!-- more -->
<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/a8bdeb7d-f6a8-4ad5-8020-e206055dd039/Python编程：从入门到实践_第3版__.png" alt="Python编程：从入门到实践（第3版）" width="400"/>
</p>
> 📖 **一起读书吧！** 加入《Python编程：从入门到实践》共读营 👉 [点击参加](https://mp.weixin.qq.com/s/ehe2vMrfAFscRLqbM9TF-g)



## 本讲内容

- 缩进与空白
- 命名规范（变量、函数、类、模块）
- 每行长度和换行
- 导入(import)的顺序
- 注释规范

## 学习目标

写出团队都愿意维护的代码 👔

---

## 1. 缩进

```python
# ✅ 每级缩进用4个空格
def greet(name):
    print(f"Hello, {name}")

# ❌ 不要用Tab（在VS Code中设置Tab自动转空格）
#     print("hello")

# ❌ 不要混用Tab和空格
```

> VS Code设置：设置 → Editor: Tab Size → 4，勾选"Insert Spaces"

## 2. 空白

```python
# ✅ 操作符两边加空格
x = 1
y = 2 + 3

# ❌ 紧贴
x=1
y=2+3

# ✅ 函数参数 / 索引周围不加空格
func(arg1, arg2)
arr[0]
dic['key']

# ❌ 不要这样
func( arg1, arg2 )
arr[ 0 ]

# ✅ 字典 / 赋值等号两边加空格
name = "晚枫"
dic = {'a': 1, 'b': 2}

# ✅ 多行对齐时用额外空格
name = "程序员晚枫"
age  = 30           # 用空格对齐
city = "深圳"
```

> 官方文档：[PEP 8 — Whitespace in Expressions and Statements](https://pep8.org/#whitespace-in-expressions-and-statements)

## 3. 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| 变量 | 小写下划线 | `user_name`, `is_active` |
| 常量 | 全大写下划线 | `MAX_SIZE`, `DEFAULT_PORT` |
| 函数 | 小写下划线 | `get_user()`, `send_email()` |
| 类 | 驼峰（首字母大写） | `UserProfile`, `CarFactory` |
| 模块 | 简短小写 | `utils.py`, `json_handler.py` |
| 包 | 简短小写 | `mypackage/` |

```python
# ✅ 变量
user_name = "晚枫"
is_registered = True
item_count = 42

# ✅ 常量
MAX_RETRY = 3
API_BASE_URL = "https://api.example.com"

# ✅ 函数
def get_user_info(user_id):
    pass

def calculate_total(items):
    pass

# ✅ 类
class UserAccount:
    pass

class DataProcessor:
    pass
```

## 4. 每行长度

```python
# 每行不超过79字符
# 如果一行太长，用以下方式换行

# 方式一：括号包裹（推荐）
result = some_function(
    arg1='value1',
    arg2='value2',
    arg3='value3'
)

# 方式二：反斜杠续行
total = first_variable + second_variable + \
        third_variable + fourth_variable

# 方式三：隐式括号（字符串连接）
text = (
    "这是第一段文字。"
    "这是第二段文字。"
)
```

## 5. 导入顺序

```python
# 标准库
import os
import sys
from collections import defaultdict

# 第三方库
import numpy as np
import pandas as pd

# 本地应用
from mymodule import MyClass
```

> 顺序：标准库 → 第三方 → 本地，且每组之间空一行。

## 6. 注释

```python
# ✅ 单行注释：解释"为什么"，不解释"是什么"
# 因为用户可能未验证，所以不发送邮件
if user.is_verified:
    send_email()

# ❌ 不要写废话注释
# 将i加1
i += 1

# ✅ docstring：每个公开的类/函数都要写
def fetch_data(url, timeout=30):
    """
    从URL获取数据。

    Args:
        url (str): 目标URL
        timeout (int): 超时时间（秒），默认30

    Returns:
        dict: 解析后的JSON数据

    Raises:
        requests.RequestException: 网络错误时抛出
    """
    pass
```

## 7. VS Code自动格式化

安装扩展：`autopep8` 或 `black`

```json
// .vscode/settings.json
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.python"
}
```

保存文件时自动格式化，手动格式化：`Shift+Alt+F`

---

## 📚 官方文档参考

- [PEP 8 — Style Guide for Python Code](https://pep8.org/) — 完整规范（强烈推荐阅读）
- [PEP 257 — Docstring Conventions](https://peps.python.org/pep-0257/) — 文档字符串规范
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) — Google的Python风格指南
- [The Hitchhiker's Guide to Python — Code Style](https://docs.python-guide.org/writing/style/) — 实践指南

---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲](https://www.bilibili.com/cheese/play/ss982042944)