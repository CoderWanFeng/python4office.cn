---
title: Python异常处理：我写了5年代码，总结的异常处理最佳实践
date: 2026-02-28 18:59:00
tags: [Python基础, 异常处理, 调试]
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

今天聊一个让新手头疼、老手也容易忽视的话题——**异常处理**。

---

## 一个真实的生产事故

去年有个学员的项目上线后频繁崩溃，日志里全是这种错误：

```
Traceback (most recent call last):
  File "app.py", line 45, in process_order
    result = calculate_price(order)
  File "app.py", line 23, in calculate_price
    return price / quantity
ZeroDivisionError: division by zero
```

**问题**：用户下单数量为0时，价格计算直接崩溃，整个订单系统挂掉。

**如果他用了异常处理**：

```python
def calculate_price(order):
    try:
        return order['price'] / order['quantity']
    except ZeroDivisionError:
        logger.error(f"订单数量为0: {order}")
        return 0  # 优雅降级
```

系统不会挂，只是这条订单处理失败，其他订单正常执行。

你可能遇到过这种情况：程序跑着跑着突然崩溃，满屏红色报错信息，却不知道哪里出了问题。

其实，只要掌握正确的异常处理方法，你的程序就能优雅地处理错误，而不是直接挂掉。

这篇文章总结了我在5年编程生涯中积累的异常处理最佳实践。

---

## 什么是异常？

简单说，**异常就是程序运行时出现的错误**。

### 程序为什么会崩溃？

```python
# 场景1：除以零
result = 10 / 0  # ZeroDivisionError

# 场景2：访问不存在的文件
with open('不存在的文件.txt', 'r') as f:
    content = f.read()  # FileNotFoundError

# 场景3：类型错误
age = int("abc")  # ValueError

# 场景4：索引越界
items = [1, 2, 3]
print(items[10])  # IndexError

# 场景5：字典key不存在
user = {'name': 'Alice'}
print(user['age'])  # KeyError
```

### 常见异常类型速查表

| 异常类型 | 触发场景 | 示例 |
|---------|---------|------|
| `ZeroDivisionError` | 除以零 | `10/0` |
| `FileNotFoundError` | 文件不存在 | `open('x.txt')` |
| `ValueError` | 值转换失败 | `int('abc')` |
| `TypeError` | 类型错误 | `len(123)` |
| `KeyError` | 字典key不存在 | `{'a':1}['b']` |
| `IndexError` | 索引越界 | `[1,2][10]` |
| `AttributeError` | 属性不存在 | `'str'.foo()` |
| `ImportError` | 导入失败 | `import xxx` |
| `PermissionError` | 权限不足 | 写入只读文件 |
| `ConnectionError` | 网络连接失败 | `requests.get()` |

### 异常层级结构

```
BaseException (所有异常的基类)
├── SystemExit (sys.exit())
├── KeyboardInterrupt (Ctrl+C)
├── GeneratorExit (生成器关闭)
└── Exception (我们主要处理这类)
    ├── StopIteration
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── OSError
    │   ├── FileNotFoundError
    │   ├── PermissionError
    │   └── ConnectionError
    ├── ValueError
    ├── TypeError
    └── ... 更多
```

---

## 基础：try-except

### 最简单的捕获

```python
try:
    result = 10 / 0
except:
    print("出错了！")
```

**问题**：捕获所有异常是坏习惯，会隐藏真正的bug。

### 捕获特定异常

```python
# 捕获特定异常
try:
    result = 10 / 0
except ZeroDivisionError:
    print("不能除以零！")

# 捕获多个异常
try:
    number = int(input("请输入数字："))
    result = 100 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"输入错误：{e}")
```

### 获取异常信息

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"错误类型：{type(e).__name__}")
    print(f"错误信息：{e}")
    print(f"错误详情：{repr(e)}")

# 输出：
# 错误类型：ZeroDivisionError
# 错误信息：division by zero
# 错误详情：ZeroDivisionError('division by zero')
```

### 获取完整堆栈信息

```python
import traceback

try:
    result = 10 / 0
except Exception as e:
    print("=== 错误堆栈 ===")
    traceback.print_exc()
    
    # 或者获取字符串
    error_stack = traceback.format_exc()
    logger.error(error_stack)
```

---

## 进阶：多个except

### 按异常类型分别处理

```python
def convert_and_divide(a_str, b_str):
    """将字符串转换为数字并相除"""
    try:
        a = int(a_str)
        b = int(b_str)
        return a / b
        
    except ValueError as e:
        print(f"参数必须是数字：{e}")
        return None
        
    except ZeroDivisionError:
        print("除数不能为0")
        return None
        
    except Exception as e:
        print(f"未知错误：{e}")
        return None

# 测试
print(convert_and_divide("10", "2"))   # 5.0
print(convert_and_divide("abc", "2"))  # 参数必须是数字
print(convert_and_divide("10", "0"))   # 除数不能为0
```

### 注意：顺序很重要！

```python
# 错误：父类在前，子类永远捕获不到
try:
    risky_operation()
except Exception:        # 捕获所有异常
    print("Exception")
except ValueError:       # 永远不会执行！
    print("ValueError")

# 正确：子类在前，父类在后
try:
    risky_operation()
except ValueError:       # 先捕获特定异常
    print("ValueError")
except Exception:        # 再捕获其他异常
    print("Exception")
```

### 捕获异常层级

```python
def safe_division(a, b):
    """安全的除法运算"""
    try:
        return a / b
        
    except ZeroDivisionError:
        # 最具体的异常
        print("错误：除数为零")
        
    except ArithmeticError:
        # 算术错误的父类
        print("错误：算术异常")
        
    except Exception:
        # 所有异常的基类（除了SystemExit等）
        print("错误：未知异常")

safe_division(10, 0)   # 错误：除数为零
safe_division(10, 'a') # 错误：未知异常（TypeError）
```

---

## 完整结构：try-except-else-finally

### 完整语法

```python
try:
    # 尝试执行的代码（可能抛出异常）
    file = open('data.txt', 'r')
    content = file.read()
    
except FileNotFoundError:
    # 发生异常时执行
    print("文件不存在！")
    content = ""
    
except PermissionError:
    print("没有权限访问文件！")
    content = ""
    
else:
    # 没有异常时执行（可选）
    print(f"成功读取 {len(content)} 个字符")
    
finally:
    # 无论是否异常都执行（清理工作）
    if 'file' in locals() and not file.closed:
        file.close()
        print("文件已关闭")
```

### 执行流程图

```
开始
  ↓
try块执行
  ↓
有异常？
  ├─ 是 → 匹配except块 → finally块 → 结束
  └─ 否 → else块 → finally块 → 结束
```

### 实战案例：数据库操作

```python
import sqlite3

def query_user(user_id):
    """查询用户信息"""
    conn = None
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        
    except sqlite3.Error as e:
        print(f"数据库错误：{e}")
        return None
        
    else:
        if result:
            return {
                'id': result[0],
                'name': result[1],
                'email': result[2]
            }
        return None
        
    finally:
        if conn:
            conn.close()
            print("数据库连接已关闭")

user = query_user(1)
print(user)
```

---

## 主动抛出异常：raise

### 基础用法

```python
def set_age(age):
    """设置年龄"""
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0 or age > 150:
        raise ValueError("年龄必须在0-150之间")
    return age

# 使用
try:
    set_age(-5)
except ValueError as e:
    print(e)  # 年龄必须在0-150之间

try:
    set_age("20")
except TypeError as e:
    print(e)  # 年龄必须是整数
```

### 重新抛出异常

```python
def process_data(data):
    try:
        result = parse_json(data)
    except json.JSONDecodeError as e:
        # 记录日志
        logger.error(f"JSON解析失败：{e}")
        # 重新抛出，让调用者处理
        raise

# 调用者可以继续处理
try:
    process_data('invalid json')
except json.JSONDecodeError:
    print("数据处理失败")
```

### 链式异常（Python 3.x）

```python
def load_config(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError as e:
        # 将FileNotFoundError转换为更具体的异常
        raise ConfigError(f"配置文件不存在: {filename}") from e

class ConfigError(Exception):
    """配置错误"""
    pass

# 使用
try:
    config = load_config('config.json')
except ConfigError as e:
    print(f"配置加载失败: {e}")
    print(f"原始错误: {e.__cause__}")
```

---

## 自定义异常

### 为什么需要自定义异常？

```python
# 内置异常不够具体
def withdraw(account, amount):
    if amount > account.balance:
        raise ValueError("余额不足")  # 不够清晰
    
# 自定义异常更明确
class InsufficientBalanceError(Exception):
    """余额不足异常"""
    pass

def withdraw(account, amount):
    if amount > account.balance:
        raise InsufficientBalanceError(f"余额不足：需要{amount}，实际{account.balance}")
```

### 简单自定义异常

```python
class ValidationError(Exception):
    """数据验证错误"""
    pass

# 使用
def validate_email(email):
    if '@' not in email:
        raise ValidationError(f"无效的邮箱地址：{email}")

try:
    validate_email("invalid-email")
except ValidationError as e:
    print(e)
```

### 带属性的自定义异常

```python
class AgeError(ValidationError):
    """年龄不合法异常"""
    def __init__(self, age, message="年龄必须在0-150之间"):
        self.age = age
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}，你输入了：{self.age}"

# 使用
def set_age(age):
    if not 0 <= age <= 150:
        raise AgeError(age)
    return age

try:
    set_age(200)
except AgeError as e:
    print(e)  # 年龄必须在0-150之间，你输入了：200
    print(f"输入值：{e.age}")
```

### 异常层次结构设计

```python
# 基类：应用异常
class AppError(Exception):
    """应用程序基础异常"""
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        super().__init__(self.message)

# 数据库相关异常
class DatabaseError(AppError):
    """数据库异常"""
    pass

class ConnectionError(DatabaseError):
    """连接异常"""
    pass

class QueryError(DatabaseError):
    """查询异常"""
    pass

# 业务逻辑异常
class BusinessError(AppError):
    """业务异常"""
    pass

class InsufficientBalanceError(BusinessError):
    """余额不足"""
    def __init__(self, required, actual):
        super().__init__(
            f"余额不足：需要{required}，实际{actual}",
            code="INSUFFICIENT_BALANCE"
        )
        self.required = required
        self.actual = actual

# 使用
try:
    raise InsufficientBalanceError(1000, 500)
except BusinessError as e:
    print(f"业务错误 [{e.code}]: {e}")
```

---

## 上下文管理器与异常

### with语句自动处理异常

```python
# 文件操作
with open('file.txt', 'r') as f:
    content = f.read()
    # 即使这里抛出异常，文件也会自动关闭

# 锁
from threading import Lock
lock = Lock()

with lock:
    # 临界区代码
    # 即使异常，锁也会自动释放
    pass
```

### 自定义上下文管理器

```python
from contextlib import contextmanager

@contextmanager
def error_handler(error_msg="操作失败"):
    """异常处理上下文管理器"""
    try:
        yield
    except Exception as e:
        print(f"{error_msg}: {e}")
        # 可以选择吞掉异常，或者重新抛出
        # raise

# 使用
with error_handler("数据库操作失败"):
    conn.execute("INSERT INTO users ...")

# 自定义计时器
import time

@contextmanager
def timer(operation_name):
    """计时上下文管理器"""
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{operation_name} 耗时: {elapsed:.2f}秒")

# 使用
with timer("数据处理"):
    process_large_dataset()
```

### suppress：忽略特定异常

```python
from contextlib import suppress

# 传统方式
try:
    os.remove('temp.txt')
except FileNotFoundError:
    pass

# suppress方式（Python 3.4+）
with suppress(FileNotFoundError):
    os.remove('temp.txt')

# 忽略多种异常
with suppress(FileNotFoundError, PermissionError):
    os.remove('temp.txt')
```

---

## 最佳实践

### ✅ 应该做的

#### 1. 具体捕获，不要裸except

```python
# ✅ 好的做法
try:
    value = int(user_input)
except ValueError as e:
    logger.error(f"参数错误：{e}")
    
# ❌ 坏的做法（会捕获KeyboardInterrupt等）
try:
    value = int(user_input)
except:
    pass  # 会捕获所有异常，包括Ctrl+C！
```

#### 2. 记录日志，不要静默处理

```python
import logging

logging.basicConfig(level=logging.ERROR)

# ✅ 好的做法
try:
    risky_operation()
except Exception as e:
    logging.error(f"操作失败：{e}", exc_info=True)
    raise  # 重新抛出，或者返回错误信息

# ❌ 坏的做法
try:
    important_operation()
except Exception:
    pass  # 错误被吞掉了，没人知道发生了什么！
```

#### 3. 使用上下文管理器

```python
# ✅ 自动处理资源释放
with open('file.txt', 'r') as f:
    content = f.read()
```

#### 4. 优雅降级

```python
def get_user_info(user_id):
    """获取用户信息，失败时返回默认值"""
    try:
        response = requests.get(f'/api/users/{user_id}')
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as e:
        logger.warning(f"获取用户信息失败: {e}")
        return {
            'id': user_id,
            'name': 'Unknown',
            'error': str(e)
        }
```

#### 5. 异常链：保留原始信息

```python
def process_config(config_file):
    try:
        with open(config_file) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ConfigError(f"配置文件处理失败") from e
```

### ❌ 不应该做的

#### 1. 不要裸except

```python
# ❌ 捕获所有异常，包括KeyboardInterrupt
try:
    do_something()
except:
    pass

# ✅ 至少捕获Exception
try:
    do_something()
except Exception:
    pass
```

#### 2. 不要忽略异常

```python
# ❌ 错误被吞掉
try:
    important_operation()
except Exception:
    pass

# ✅ 至少记录日志
try:
    important_operation()
except Exception as e:
    logger.error(f"重要操作失败: {e}")
    raise
```

#### 3. 不要用异常控制流程

```python
# ❌ 用异常代替条件判断（性能差）
try:
    value = my_dict[key]
except KeyError:
    value = default

# ✅ 使用dict.get()
value = my_dict.get(key, default)

# ❌ 用异常检查文件存在
try:
    with open('file.txt'):
        pass
except FileNotFoundError:
    pass

# ✅ 使用Path.exists()
from pathlib import Path
if Path('file.txt').exists():
    pass
```

#### 4. 不要在finally中抛出异常

```python
# ❌ finally中的异常会覆盖原来的异常
try:
    raise ValueError("原始错误")
finally:
    raise TypeError("finally中的错误")  # ValueError丢失了！

# ✅ 正确做法
try:
    raise ValueError("原始错误")
finally:
    try:
        cleanup()
    except Exception as e:
        logger.error(f"清理失败: {e}")
```

---

## 异常处理性能对比

### 异常 vs 条件判断

```python
import time

# 测试：处理100万次字典访问
my_dict = {'a': 1, 'b': 2}

# 方式1：异常处理
def get_with_exception(key):
    try:
        return my_dict[key]
    except KeyError:
        return None

# 方式2：条件判断
def get_with_if(key):
    if key in my_dict:
        return my_dict[key]
    return None

# 方式3：dict.get()
def get_with_get(key):
    return my_dict.get(key)

# 性能测试
def test_performance():
    # 测试存在的key
    start = time.time()
    for _ in range(1000000):
        get_with_exception('a')
    print(f"异常处理（存在）: {time.time()-start:.3f}s")
    
    start = time.time()
    for _ in range(1000000):
        get_with_if('a')
    print(f"条件判断（存在）: {time.time()-start:.3f}s")
    
    start = time.time()
    for _ in range(1000000):
        get_with_get('a')
    print(f"dict.get（存在）: {time.time()-start:.3f}s")
    
    # 测试不存在的key
    start = time.time()
    for _ in range(1000000):
        get_with_exception('c')
    print(f"异常处理（不存在）: {time.time()-start:.3f}s")
    
    start = time.time()
    for _ in range(1000000):
        get_with_if('c')
    print(f"条件判断（不存在）: {time.time()-start:.3f}s")
    
    start = time.time()
    for _ in range(1000000):
        get_with_get('c')
    print(f"dict.get（不存在）: {time.time()-start:.3f}s")

test_performance()

# 结果：
# 异常处理（存在）: 0.15s
# 条件判断（存在）: 0.08s
# dict.get（存在）: 0.10s
# 异常处理（不存在）: 1.20s  ← 异常处理不存在的key很慢！
# 条件判断（不存在）: 0.08s
# dict.get（不存在）: 0.10s
```

**结论**：异常处理在"正常"情况下性能还可以，但一旦抛出异常，性能急剧下降。**不要用异常控制流程！**

---

## 实战案例

### 案例1：健壮的API请求

```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError
import time

def fetch_data(url, max_retries=3, timeout=5):
    """带重试机制的HTTP请求"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  # 检查HTTP错误
            return response.json()
            
        except Timeout:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 指数退避
                print(f"超时，{wait_time}秒后重试（第{attempt + 1}次）...")
                time.sleep(wait_time)
                continue
            raise TimeoutError(f"请求超时，已重试{max_retries}次")
            
        except ConnectionError as e:
            raise ConnectionError(f"连接失败：{e}")
            
        except requests.HTTPError as e:
            if response.status_code == 404:
                return None  # 资源不存在
            elif response.status_code == 429:
                # 请求太频繁，等待后重试
                retry_after = int(response.headers.get('Retry-After', 60))
                time.sleep(retry_after)
                continue
            raise
            
        except ValueError as e:
            raise ValueError(f"JSON解析失败：{e}")
            
        except RequestException as e:
            raise RequestError(f"请求失败：{e}")

# 使用
try:
    data = fetch_data('https://api.example.com/data')
    if data:
        print(data)
    else:
        print("数据不存在")
except Exception as e:
    print(f"获取数据失败：{e}")
```

### 案例2：文件处理工具

```python
import json
from pathlib import Path

class FileHandler:
    """健壮的文件处理工具"""
    
    @staticmethod
    def read_json(filepath, default=None):
        """读取JSON文件"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"文件不存在：{filepath}")
            return default
        except json.JSONDecodeError as e:
            print(f"JSON格式错误：{e}")
            return default
        except Exception as e:
            print(f"读取失败：{e}")
            return default
    
    @staticmethod
    def write_json(filepath, data, indent=2):
        """写入JSON文件"""
        try:
            path = Path(filepath)
            path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=indent)
            return True
        except PermissionError:
            print(f"没有写入权限：{filepath}")
            return False
        except Exception as e:
            print(f"写入失败：{e}")
            return False
    
    @staticmethod
    def safe_delete(filepath):
        """安全删除文件"""
        try:
            Path(filepath).unlink()
            return True
        except FileNotFoundError:
            print(f"文件不存在，无需删除：{filepath}")
            return True
        except PermissionError:
            print(f"没有删除权限：{filepath}")
            return False
        except Exception as e:
            print(f"删除失败：{e}")
            return False

# 使用
config = FileHandler.read_json('config.json', default={'debug': False})
FileHandler.write_json('output.json', {'result': 'success'})
```

### 案例3：数据库事务处理

```python
import sqlite3

class DatabaseManager:
    """数据库管理器"""
    
    def __init__(self, db_path):
        self.db_path = db_path
    
    def execute_transaction(self, operations):
        """执行事务"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 开始事务
            for sql, params in operations:
                cursor.execute(sql, params)
            
            # 提交事务
            conn.commit()
            return True
            
        except sqlite3.Error as e:
            # 回滚事务
            if conn:
                conn.rollback()
            print(f"事务执行失败：{e}")
            return False
            
        finally:
            if conn:
                conn.close()

# 使用
db = DatabaseManager('app.db')
operations = [
    ("INSERT INTO orders (user_id, amount) VALUES (?, ?)", (1, 100)),
    ("UPDATE users SET balance = balance - ? WHERE id = ?", (100, 1)),
    ("INSERT INTO logs (action, user_id) VALUES (?, ?)", ('purchase', 1))
]

if db.execute_transaction(operations):
    print("交易成功")
else:
    print("交易失败，已回滚")
```

### 案例4：批量数据处理

```python
def batch_process(items, process_func, continue_on_error=True):
    """批量处理数据"""
    results = []
    errors = []
    
    for i, item in enumerate(items):
        try:
            result = process_func(item)
            results.append(result)
        except Exception as e:
            error_info = {
                'index': i,
                'item': item,
                'error': str(e)
            }
            errors.append(error_info)
            
            if not continue_on_error:
                raise
    
    return {
        'success_count': len(results),
        'error_count': len(errors),
        'results': results,
        'errors': errors
    }

# 使用
def process_user(user):
    """处理单个用户"""
    if user.get('invalid'):
        raise ValueError("无效用户")
    return user['name'].upper()

users = [
    {'name': 'Alice'},
    {'name': 'Bob', 'invalid': True},
    {'name': 'Charlie'}
]

result = batch_process(users, process_user)
print(f"成功：{result['success_count']}")
print(f"失败：{result['error_count']}")
print(f"结果：{result['results']}")
```

---

## 调试技巧

### 使用断点调试异常

```python
# 方法1：使用pdb
try:
    result = risky_operation()
except Exception as e:
    import pdb; pdb.post_mortem()  # 在异常处进入调试

# 方法2：使用breakpoint()（Python 3.7+）
try:
    result = risky_operation()
except Exception as e:
    breakpoint()  # 交互式调试
```

### 记录异常上下文

```python
import logging
import traceback

logging.basicConfig(level=logging.DEBUG)

def log_exception_context():
    """记录异常的完整上下文"""
    try:
        result = risky_operation()
    except Exception as e:
        # 记录完整信息
        logging.error(
            f"异常发生",
            exc_info=True,  # 包含堆栈
            extra={
                'exception_type': type(e).__name__,
                'exception_message': str(e),
                'local_vars': locals()
            }
        )
        raise
```

### 单元测试异常

```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_divide_by_zero(self):
        """测试除以零异常"""
        with self.assertRaises(ZeroDivisionError):
            10 / 0
    
    def test_custom_exception(self):
        """测试自定义异常"""
        with self.assertRaises(ValidationError) as context:
            validate_age(-5)
        
        self.assertIn("年龄", str(context.exception))
    
    def test_exception_message(self):
        """测试异常消息"""
        with self.assertRaises(ValueError) as context:
            int('abc')
        
        self.assertEqual(str(context.exception), "invalid literal for int()")

if __name__ == '__main__':
    unittest.main()
```

---

## 推荐：AI Python零基础实战营

想系统学习Python异常处理和调试技巧？

**课程内容：**
- ✅ Python基础语法
- ✅ 异常处理与调试
- ✅ 日志记录最佳实践
- ✅ 实战项目练习

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 相关阅读

- [Python文件操作：读写文件的10种姿势](/course/AI相关/人民邮电出版社/ads/openclaw/python/13-Python文件操作/)
- [Python字符串：我被忽略的20个实用方法](/course/AI相关/人民邮电出版社/ads/openclaw/python/12-Python字符串/)
- [Python装饰器：给函数加功能的黑魔法](/course/AI相关/人民邮电出版社/ads/openclaw/python/11-Python装饰器/)

---

*PS：好的异常处理能让程序更健壮。记住原则：具体捕获、记录日志、优雅降级。别让你的程序裸奔！*

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



