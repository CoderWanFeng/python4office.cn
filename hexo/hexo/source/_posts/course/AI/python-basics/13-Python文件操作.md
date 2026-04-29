---
title: Python文件操作：我总结了读写文件的10种姿势，最后一种最优雅
date: 2026-02-28 18:58:00
tags: [Python基础, 文件操作, IO]
cover: https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1200&auto=format&fit=crop
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

今天聊一个每个Python开发者都必须掌握的技能——**文件操作**。

---

## 一个真实的崩溃场景

去年有个学员问我："晚枫老师，我的程序为什么跑着跑着就崩了？"

我看了一眼他的代码：

```python
# 处理10万条用户数据
for i in range(100000):
    f = open(f'user_{i}.txt', 'r')
    data = f.read()
    # 处理数据...
    # 忘记关闭文件了！
```

**问题**：打开的文件越来越多，系统资源耗尽，程序崩溃。

这就是不懂文件操作的代价。你可能觉得文件读写很简单，`open()`一下就行。但其实这里面有很多坑和技巧，用对了能省很多麻烦。

我总结了10种文件操作的姿势，从入门到进阶，最后一种最优雅。

---

## 姿势1：基础写法（有坑！）

### 简单示例
```python
# 最基础的文件读取
f = open('data.txt', 'r')
content = f.read()
print(content)
f.close()
```

### 坑在哪？
```python
# 看起来没问题，但如果这样呢？
f = open('data.txt', 'r')
content = f.read()  # 这里可能报错！比如文件编码问题
# 如果上面这行报错，close()就不会执行
# 文件句柄一直被占用，导致资源泄漏
f.close()
```

### 实际案例
```python
# 处理CSV文件时遇到编码错误
f = open('sales_data.csv', 'r')
try:
    # 如果文件是GBK编码，这里会报UnicodeDecodeError
    content = f.read()
except Exception as e:
    print(f"出错了: {e}")
# 文件没有被关闭！
```

**结论**：这种写法在生产环境绝对不能用！

---

## 姿势2：try-finally（安全但啰嗦）

### 基础用法
```python
f = open('data.txt', 'r')
try:
    content = f.read()
    print(content)
finally:
    f.close()
```

### 进阶用法：处理多种异常
```python
f = open('config.txt', 'r', encoding='utf-8')
try:
    content = f.read()
    data = json.loads(content)  # 可能JSON格式错误
    
except UnicodeDecodeError:
    print("编码错误，尝试其他编码...")
    f.close()
    f = open('config.txt', 'r', encoding='gbk')
    content = f.read()
    
except json.JSONDecodeError as e:
    print(f"JSON格式错误: {e}")
    
finally:
    if not f.closed:
        f.close()
```

**优点**：无论是否出错，都会关闭文件
**缺点**：代码太长了，容易写错

---

## 姿势3：with语句（推荐！）

### 基础用法
```python
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)
# 自动关闭，即使出错也会关闭
```

### 为什么推荐？
```python
# with语句的本质：上下文管理器
# 等价于：
f = open('data.txt', 'r')
try:
    content = f.read()
    print(content)
finally:
    f.close()

# 但写起来简洁多了！
```

### 同时操作多个文件
```python
# 同时读取和写入
with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    for line in fin:
        processed = line.upper()
        fout.write(processed)

# 复制文件
with open('source.jpg', 'rb') as src, open('dest.jpg', 'wb') as dst:
    dst.write(src.read())
```

### 自定义上下文管理器
```python
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode='r'):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

# 使用
with open_file('data.txt') as f:
    content = f.read()
```

**这是最推荐的方式**，简洁又安全。

---

## 姿势4：逐行读取（大文件必备）

### 方式1：直接遍历（推荐）
```python
# 内存友好：每次只读一行到内存
with open('big_file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # 处理每一行
        cleaned = line.strip()
        if cleaned:
            process(cleaned)
```

### 方式2：readlines()（小文件可以用）
```python
# 一次性读取所有行到列表
with open('data.txt', 'r') as f:
    lines = f.readlines()  # 返回列表，如 ['line1\n', 'line2\n']
    for line in lines:
        print(line.strip())
```

### 性能对比
```python
import time
import sys

# 测试文件：100MB，约100万行
filename = 'large_data.txt'

# 方式1：直接遍历（内存友好）
def read_line_by_line():
    total = 0
    with open(filename, 'r') as f:
        for line in f:
            total += len(line)
    return total

# 方式2：readlines()（内存爆炸）
def read_all_lines():
    with open(filename, 'r') as f:
        lines = f.readlines()
        total = sum(len(line) for line in lines)
    return total

# 方式3：read()（更可怕）
def read_all():
    with open(filename, 'r') as f:
        content = f.read()
        total = len(content)
    return total

# 内存占用测试
print("方式1（逐行遍历）：")
start = time.time()
result = read_line_by_line()
print(f"  结果: {result}, 用时: {time.time()-start:.2f}s")
print(f"  内存: 几乎不增长")

print("\n方式2（readlines）：")
start = time.time()
result = read_all_lines()
print(f"  结果: {result}, 用时: {time.time()-start:.2f}s")
print(f"  内存: 增加约200MB（列表开销）")

print("\n方式3（read）：")
start = time.time()
result = read_all()
print(f"  结果: {result}, 用时: {time.time()-start:.2f}s")
print(f"  内存: 增加约100MB")
```

### 处理超大日志文件实战
```python
def analyze_log(filename, target_date):
    """分析特定日期的日志"""
    error_count = 0
    warning_count = 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            # 只处理目标日期的日志
            if target_date in line:
                if 'ERROR' in line:
                    error_count += 1
                elif 'WARNING' in line:
                    warning_count += 1
    
    return error_count, warning_count

# 使用：处理GB级日志文件也不会爆内存
errors, warnings = analyze_log('app.log', '2024-01-15')
print(f"错误: {errors}, 警告: {warnings}")
```

**注意**：大文件不要用`read()`或`readlines()`，会占用大量内存。

---

## 姿势5：写入文件

### 覆盖写入（'w'模式）
```python
# 基础写入
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello World\n')
    f.write('第二行内容\n')

# 注意：'w'模式会清空原有内容！
```

### 追加写入（'a'模式）
```python
# 在文件末尾追加
with open('log.txt', 'a', encoding='utf-8') as f:
    import datetime
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(f'[{timestamp}] 新的日志记录\n')

# 追加多行
logs = [
    '2024-01-15 10:00:00 INFO Application started\n',
    '2024-01-15 10:05:00 ERROR Connection failed\n',
    '2024-01-15 10:10:00 INFO Retrying...\n'
]
with open('app.log', 'a', encoding='utf-8') as f:
    f.writelines(logs)
```

### 写入多行
```python
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# 更优雅的方式：列表推导式
data = ['apple', 'banana', 'cherry']
with open('fruits.txt', 'w', encoding='utf-8') as f:
    f.writelines(f'{item}\n' for item in data)
```

### 混合读写（'r+'模式）
```python
# 读写模式：文件必须存在
with open('data.txt', 'r+') as f:
    content = f.read()  # 读取
    f.seek(0)           # 回到文件开头
    f.write('New data') # 覆盖写入
```

### 性能对比：单次写入 vs 批量写入
```python
import time

# 写入10万行数据
data = [f'Line {i}\n' for i in range(100000)]

# 方式1：逐行写入（慢）
def write_line_by_line():
    with open('test1.txt', 'w') as f:
        for line in data:
            f.write(line)

# 方式2：批量写入（快）
def write_batch():
    with open('test2.txt', 'w') as f:
        f.writelines(data)

# 测试
start = time.time()
write_line_by_line()
print(f"逐行写入: {time.time()-start:.3f}s")

start = time.time()
write_batch()
print(f"批量写入: {time.time()-start:.3f}s")

# 结果：批量写入快5-10倍！
```

---

## 姿势6：二进制文件操作

### 读取二进制文件
```python
# 读取图片
with open('photo.jpg', 'rb') as f:
    data = f.read()
    print(f"图片大小: {len(data)} bytes")

# 分块读取（大文件）
def read_in_chunks(filename, chunk_size=8192):
    """分块读取大文件"""
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# 使用：处理大视频文件
for chunk in read_in_chunks('video.mp4'):
    process(chunk)
```

### 写入二进制文件
```python
# 复制图片
with open('photo.jpg', 'rb') as src:
    with open('photo_copy.jpg', 'wb') as dst:
        dst.write(src.read())

# 分块复制（大文件）
def copy_file(src_path, dst_path, chunk_size=8192):
    """分块复制文件"""
    with open(src_path, 'rb') as src:
        with open(dst_path, 'wb') as dst:
            while True:
                chunk = src.read(chunk_size)
                if not chunk:
                    break
                dst.write(chunk)
    print(f"复制完成: {dst_path}")

copy_file('large_video.mp4', 'backup_video.mp4')
```

### 二进制文件操作实战
```python
# 图片水印（简化版）
def add_watermark(image_path, output_path):
    """给图片添加简单的文本水印"""
    with open(image_path, 'rb') as f:
        data = bytearray(f.read())
    
    # 在文件末尾添加水印信息（简化示例）
    watermark = b'\n[WATERMARK] Created by Python'
    data.extend(watermark)
    
    with open(output_path, 'wb') as f:
        f.write(data)

# 提取EXIF信息（简化）
def get_jpeg_size(filename):
    """获取JPEG图片尺寸"""
    with open(filename, 'rb') as f:
        # JPEG文件头检查
        magic = f.read(2)
        if magic != b'\xff\xd8':
            raise ValueError("不是有效的JPEG文件")
        
        # 简化：直接读取文件大小
        f.seek(0, 2)  # 移到文件末尾
        size = f.tell()
        return size
```

---

## 姿势7：指定编码（中文必备）

### 常见编码问题
```python
# 问题1：UnicodeDecodeError
# 文件是GBK编码，用UTF-8读取会报错
with open('chinese.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # UnicodeDecodeError!

# 解决方案：指定正确编码
with open('chinese.txt', 'r', encoding='gbk') as f:
    content = f.read()  # OK!
```

### 自动检测编码
```python
import chardet

def detect_encoding(filename):
    """检测文件编码"""
    with open(filename, 'rb') as f:
        raw = f.read(10000)  # 读取前10000字节
        result = chardet.detect(raw)
        return result['encoding']

# 使用
filename = 'unknown_encoding.txt'
encoding = detect_encoding(filename)
print(f"检测到编码: {encoding}")

with open(filename, 'r', encoding=encoding) as f:
    content = f.read()
```

### 编码转换
```python
def convert_encoding(input_file, output_file, from_enc, to_enc='utf-8'):
    """转换文件编码"""
    with open(input_file, 'r', encoding=from_enc) as f:
        content = f.read()
    
    with open(output_file, 'w', encoding=to_enc) as f:
        f.write(content)
    
    print(f"转换完成: {from_enc} -> {to_enc}")

# GBK转UTF-8
convert_encoding('gbk_file.txt', 'utf8_file.txt', 'gbk', 'utf-8')
```

### 常见编码类型
| 编码 | 适用场景 | 特点 |
|-----|---------|------|
| utf-8 | 国际通用 | 推荐，兼容ASCII |
| gbk | 中文Windows | 简体中文 |
| gb2312 | 中文 | 老系统 |
| big5 | 繁体中文 | 港台地区 |
| latin-1 | 西欧语言 | ISO-8859-1 |

### 避坑指南
```python
# 坑1：Windows默认编码不是UTF-8
# 在Windows上创建文件，默认是GBK编码

# 解决：统一使用UTF-8
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write('中文内容')

# 坑2：BOM问题
# 某些Windows软件会在UTF-8文件开头添加BOM标记

# 解决：使用utf-8-sig编码
with open('file.txt', 'r', encoding='utf-8-sig') as f:
    content = f.read()  # 自动去除BOM
```

---

## 姿势8：使用Path（现代写法）

### 基础用法
```python
from pathlib import Path

# 读取文本
content = Path('data.txt').read_text(encoding='utf-8')

# 写入文本
Path('output.txt').write_text('Hello World\n', encoding='utf-8')

# 读取二进制
image_data = Path('photo.jpg').read_bytes()

# 写入二进制
Path('output.jpg').write_bytes(image_data)
```

### 路径操作
```python
from pathlib import Path

# 创建路径对象
p = Path('/Users/wanfeng/projects/my_project/data.txt')

# 路径属性
print(p.name)      # data.txt
print(p.stem)      # data
print(p.suffix)    # .txt
print(p.parent)    # /Users/wanfeng/projects/my_project

# 路径操作
new_path = p.with_suffix('.csv')  # data.csv
new_path = p.with_name('config.json')  # config.json
new_path = p.parent / 'backup' / p.name  # backup/data.txt

# 检查路径
print(p.exists())   # 是否存在
print(p.is_file())  # 是否是文件
print(p.is_dir())   # 是否是目录
```

### 批量处理文件
```python
from pathlib import Path

# 遍历目录中所有txt文件
folder = Path('./documents')
for txt_file in folder.glob('*.txt'):
    content = txt_file.read_text(encoding='utf-8')
    print(f"{txt_file.name}: {len(content)}字符")

# 递归遍历所有Python文件
for py_file in folder.rglob('*.py'):
    print(py_file)

# 创建目录
Path('./new_folder/sub_folder').mkdir(parents=True, exist_ok=True)
```

### Path vs open 性能对比
```python
import time
from pathlib import Path

# 测试读取10000次小文件
test_file = 'small.txt'
Path(test_file).write_text('test content')

# 方式1：传统open
def test_open():
    start = time.time()
    for _ in range(10000):
        with open(test_file, 'r') as f:
            content = f.read()
    return time.time() - start

# 方式2：Path
def test_path():
    start = time.time()
    for _ in range(10000):
        content = Path(test_file).read_text()
    return time.time() - start

print(f"传统open: {test_open():.3f}s")
print(f"Path方式: {test_path():.3f}s")

# 结果：性能差不多，但Path更简洁
```

**优点**：
- 一行搞定，自动处理关闭
- 路径操作更优雅
- 跨平台兼容性好（Windows/Mac/Linux）

---

## 姿势9：CSV文件处理

### 使用csv模块
```python
import csv

# 读取CSV
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['Name', 'Age', 'City']

# 写入CSV
with open('output.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', '25', 'Beijing'])
    writer.writerow(['Bob', '30', 'Shanghai'])
    
    # 批量写入
    data = [
        ['Charlie', '35', 'Guangzhou'],
        ['David', '28', 'Shenzhen']
    ]
    writer.writerows(data)
```

### 使用DictReader/DictWriter
```python
import csv

# 字典方式读取（更直观）
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']}: {row['Age']}岁")  # Alice: 25岁

# 字典方式写入
with open('output.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': 25, 'City': 'Beijing'})
    writer.writerow({'Name': 'Bob', 'Age': 30, 'City': 'Shanghai'})
```

### 处理大CSV文件
```python
import csv

def process_large_csv(input_file, output_file):
    """处理大CSV文件，内存友好"""
    with open(input_file, 'r', encoding='utf-8') as fin, \
         open(output_file, 'w', encoding='utf-8', newline='') as fout:
        
        reader = csv.DictReader(fin)
        writer = csv.DictWriter(fout, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            # 处理每一行
            row['Age'] = str(int(row['Age']) + 1)  # 年龄+1
            writer.writerow(row)

# 处理100万行CSV也不会爆内存
process_large_csv('users.csv', 'users_updated.csv')
```

---

## 姿势10：JSON文件处理

### 基础操作
```python
import json

# 读取JSON
with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data['name'])

# 写入JSON
data = {'name': 'Alice', 'age': 25, 'skills': ['Python', 'JavaScript']}
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

### 格式化选项
```python
import json

data = {
    'name': '张三',
    'age': 30,
    'hobbies': ['reading', 'coding', 'gaming']
}

# 不同格式选项
print(json.dumps(data))  # 单行，转义中文
print(json.dumps(data, ensure_ascii=False))  # 保留中文
print(json.dumps(data, ensure_ascii=False, indent=2))  # 美化输出
print(json.dumps(data, ensure_ascii=False, sort_keys=True))  # 按key排序

# 输出到文件
with open('pretty.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
```

### 处理复杂数据类型
```python
import json
from datetime import datetime

# 自定义编码器
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# 使用
data = {
    'name': 'Event',
    'time': datetime.now(),
    'participants': ['Alice', 'Bob']
}

json_str = json.dumps(data, cls=DateTimeEncoder, ensure_ascii=False)
print(json_str)

# 自定义解码器
def datetime_decoder(dct):
    for key, value in dct.items():
        if key.endswith('_time') or key == 'time':
            try:
                dct[key] = datetime.fromisoformat(value)
            except:
                pass
    return dct

# 读取时自动转换
data = json.loads(json_str, object_hook=datetime_decoder)
```

---

## 避坑指南：我踩过的10个坑

### 坑1：忘记关闭文件
```python
# 错误
f = open('file.txt', 'r')
data = f.read()
# 忘记 f.close()，资源泄漏

# 正确
with open('file.txt', 'r') as f:
    data = f.read()
```

### 坑2：编码错误
```python
# 错误：Windows上打开UTF-8文件可能报错
with open('chinese.txt', 'r') as f:  # Windows默认GBK
    content = f.read()

# 正确：明确指定编码
with open('chinese.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### 坑3：'w'模式清空文件
```python
# 错误：想追加却用'w'模式，原有内容被清空
with open('log.txt', 'w') as f:  # 文件被清空！
    f.write('new log')

# 正确：追加用'a'模式
with open('log.txt', 'a') as f:
    f.write('new log\n')
```

### 坑4：大文件一次性读取
```python
# 错误：读取GB级文件
with open('huge_file.txt', 'r') as f:
    content = f.read()  # 内存爆炸！

# 正确：逐行处理
with open('huge_file.txt', 'r') as f:
    for line in f:
        process(line)
```

### 坑5：Windows换行符问题
```python
# Windows: \r\n
# Mac/Linux: \n

# 问题：跨平台处理时多出\r
with open('windows_file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # strip()会处理\r和\n

# 更好的方式
with open('file.txt', 'r', newline='') as f:
    # 不自动转换换行符
    for line in f:
        line = line.rstrip('\r\n')
```

### 坑6：路径拼接错误
```python
# 错误：硬编码路径分隔符
path = 'folder' + '/' + 'file.txt'  # Windows上可能出错

# 正确：使用Path或os.path.join
from pathlib import Path
path = Path('folder') / 'file.txt'

import os
path = os.path.join('folder', 'file.txt')
```

### 坑7：文件不存在错误
```python
# 错误：直接打开可能不存在的文件
with open('config.txt', 'r') as f:
    config = f.read()  # FileNotFoundError

# 正确：先检查
from pathlib import Path
config_file = Path('config.txt')
if config_file.exists():
    config = config_file.read_text()
else:
    config = default_config
```

### 坑8：并发写入冲突
```python
# 问题：多个进程同时写入同一文件
# 解决：使用文件锁
import fcntl

def safe_write(filename, content):
    with open(filename, 'a') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)  # 加锁
        try:
            f.write(content)
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)  # 解锁
```

### 坑9：临时文件残留
```python
# 错误：手动创建临时文件
f = open('temp_xxx.txt', 'w')
# 忘记删除

# 正确：使用tempfile
import tempfile

# 自动删除
with tempfile.NamedTemporaryFile(mode='w', delete=True) as f:
    f.write('temporary content')
    # 文件会在关闭时自动删除

# 或者指定位置
temp_dir = tempfile.mkdtemp()
# 使用完毕后手动清理
import shutil
shutil.rmtree(temp_dir)
```

### 坑10：CSV写入空行
```python
# 问题：Windows上写入CSV多出空行
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'b'])  # 会多出一行空行

# 正确：指定newline=''
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'b'])
```

---

## 实战案例：批量文件处理工具

### 案例1：批量重命名文件
```python
from pathlib import Path
import re

def batch_rename(folder, pattern, replacement):
    """批量重命名文件"""
    folder = Path(folder)
    for file in folder.iterdir():
        if file.is_file():
            new_name = re.sub(pattern, replacement, file.name)
            new_path = file.parent / new_name
            file.rename(new_path)
            print(f"{file.name} -> {new_name}")

# 使用：给所有图片添加日期前缀
batch_rename('./images', r'(.+)\.jpg', r'2024_\1.jpg')
```

### 案例2：统计代码行数
```python
from pathlib import Path

def count_lines(folder, extension='.py'):
    """统计代码行数"""
    total_lines = 0
    file_count = 0
    
    for file in Path(folder).rglob(f'*{extension}'):
        with open(file, 'r', encoding='utf-8') as f:
            lines = len(f.readlines())
            total_lines += lines
            file_count += 1
            print(f"{file.name}: {lines}行")
    
    print(f"\n总计: {file_count}个文件, {total_lines}行代码")
    return total_lines

count_lines('./my_project', '.py')
```

### 案例3：日志分析工具
```python
from pathlib import Path
from collections import Counter
import re

def analyze_logs(log_dir):
    """分析日志目录中的所有日志文件"""
    error_types = Counter()
    hourly_errors = Counter()
    
    for log_file in Path(log_dir).glob('*.log'):
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                # 统计错误类型
                if 'ERROR' in line:
                    error_match = re.search(r'ERROR (\w+)', line)
                    if error_match:
                        error_types[error_match.group(1)] += 1
                    
                    # 统计每小时错误数
                    time_match = re.search(r'(\d{2}):\d{2}:\d{2}', line)
                    if time_match:
                        hourly_errors[time_match.group(1)] += 1
    
    # 输出报告
    print("=== 错误类型统计 ===")
    for error, count in error_types.most_common(10):
        print(f"{error}: {count}次")
    
    print("\n=== 每小时错误分布 ===")
    for hour in sorted(hourly_errors.keys()):
        print(f"{hour}时: {hourly_errors[hour]}个错误")

analyze_logs('./logs')
```

### 案例4：文件同步备份
```python
from pathlib import Path
import shutil
import hashlib

def get_file_hash(filepath):
    """计算文件MD5"""
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def sync_folders(source, target):
    """同步两个文件夹"""
    source = Path(source)
    target = Path(target)
    target.mkdir(exist_ok=True)
    
    # 复制新增/修改的文件
    for src_file in source.rglob('*'):
        if src_file.is_file():
            rel_path = src_file.relative_to(source)
            tgt_file = target / rel_path
            
            if not tgt_file.exists():
                tgt_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, tgt_file)
                print(f"新增: {rel_path}")
            elif get_file_hash(src_file) != get_file_hash(tgt_file):
                shutil.copy2(src_file, tgt_file)
                print(f"更新: {rel_path}")
    
    # 删除目标中多余的文件
    for tgt_file in target.rglob('*'):
        if tgt_file.is_file():
            rel_path = tgt_file.relative_to(target)
            src_file = source / rel_path
            
            if not src_file.exists():
                tgt_file.unlink()
                print(f"删除: {rel_path}")

sync_folders('./project', './backup')
```

---

## 性能优化技巧

### 技巧1：使用缓冲
```python
# 默认缓冲区大小通常是8KB
# 对于大文件，可以增大缓冲区
with open('large_file.txt', 'r', buffering=65536) as f:
    for line in f:
        process(line)
```

### 技巧2：批量写入
```python
# 慢：逐行写入
with open('output.txt', 'w') as f:
    for i in range(100000):
        f.write(f'Line {i}\n')

# 快：批量写入
lines = [f'Line {i}\n' for i in range(100000)]
with open('output.txt', 'w') as f:
    f.writelines(lines)
```

### 技巧3：使用内存映射
```python
import mmap

# 对于超大文件的随机访问
with open('huge_file.bin', 'rb') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
        # 可以像操作内存一样操作文件
        data = mm[1000:2000]  # 只读取1000-2000字节
        position = mm.find(b'pattern')  # 快速搜索
```

### 技巧4：异步IO（Python 3.7+）
```python
import asyncio
import aiofiles

async def async_read_file(filename):
    """异步读取文件"""
    async with aiofiles.open(filename, 'r', encoding='utf-8') as f:
        content = await f.read()
    return content

async def async_write_file(filename, content):
    """异步写入文件"""
    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write(content)

async def process_multiple_files(filenames):
    """并发处理多个文件"""
    tasks = [async_read_file(f) for f in filenames]
    contents = await asyncio.gather(*tasks)
    return contents

# 使用
filenames = ['file1.txt', 'file2.txt', 'file3.txt']
results = asyncio.run(process_multiple_files(filenames))
```

---

## 推荐：AI Python零基础实战营

想系统学习Python文件操作和数据处理？

**课程内容：**
- ✅ Python基础语法
- ✅ 文件读写与数据处理
- ✅ CSV、Excel、JSON操作
- ✅ 实战项目练习

🎁 **限时福利**：送《Python编程从入门到实践》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 相关阅读

- [Python字符串：我被忽略的20个实用方法](/course/AI相关/人民邮电出版社/ads/openclaw/python/12-Python字符串/)
- [Python字典：我用这个数据结构，把查询速度提升了100倍](/course/AI相关/人民邮电出版社/ads/openclaw/python/08-Python字典/)
- [Python列表推导式：一行代码搞定循环](/course/AI相关/人民邮电出版社/ads/openclaw/python/07-Python列表推导式/)

---

*PS：文件操作是编程的基础功，掌握这些技巧，数据处理会轻松很多。记住核心原则：用with语句、指定编码、大文件逐行处理。*

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



