---
title: Python文件操作：我总结了读写文件的10种姿势，最后一种最优雅
date: 2026-02-28 18:58:00
tags: [Python基础, 文件操作, IO]
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

今天聊一个每个Python开发者都必须掌握的技能——**文件操作**。

你可能觉得文件读写很简单，`open()`一下就行。但其实这里面有很多坑和技巧，用对了能省很多麻烦。

我总结了10种文件操作的姿势，从入门到进阶，最后一种最优雅。

---

## 姿势1：基础写法（有坑）

```python
f = open('data.txt', 'r')
content = f.read()
print(content)
f.close()
```

**坑在哪？**如果`read()`的时候报错，`close()`就不会执行，文件一直占着资源。

---

## 姿势2：try-finally（安全但啰嗦）

```python
f = open('data.txt', 'r')
try:
    content = f.read()
    print(content)
finally:
    f.close()
```

**优点**：无论是否出错，都会关闭文件
**缺点**：代码太长了

---

## 姿势3：with语句（推荐！）

```python
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)
# 自动关闭，即使出错也会关闭
```

**这是最推荐的方式**，简洁又安全。

---

## 姿势4：逐行读取（大文件必备）

```python
# 方式1：直接遍历
with open('big_file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# 方式2：readlines()（小文件可以用）
with open('data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

**注意**：大文件不要用`read()`或`readlines()`，会占用大量内存。

---

## 姿势5：写入文件

```python
# 覆盖写入
with open('output.txt', 'w') as f:
    f.write('Hello World\n')
    f.write('第二行内容\n')

# 追加写入
with open('log.txt', 'a') as f:
    f.write('新的日志记录\n')

# 写入多行
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as f:
    f.writelines(lines)
```

---

## 姿势6：二进制文件操作

```python
# 读取图片
with open('photo.jpg', 'rb') as f:
    data = f.read()
    print(f"图片大小: {len(data)} bytes")

# 复制图片
with open('photo.jpg', 'rb') as src:
    with open('photo_copy.jpg', 'wb') as dst:
        dst.write(src.read())
```

---

## 姿势7：指定编码（中文必备）

```python
# 读取中文文件
with open('chinese.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 写入中文
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('中文内容')
```

**常见编码**：utf-8、gbk、gb2312、latin-1

---

## 姿势8：使用Path（现代写法）

```python
from pathlib import Path

# 读取
content = Path('data.txt').read_text(encoding='utf-8')

# 写入
Path('output.txt').write_text('Hello World', encoding='utf-8')

# 读取二进制
image_data = Path('photo.jpg').read_bytes()
```

**优点**：一行搞定，自动处理关闭

---

## 姿势9：CSV文件处理

```python
import csv

# 读取CSV
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 写入CSV
with open('output.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', '25', 'Beijing'])
    writer.writerow(['Bob', '30', 'Shanghai'])
```

---

## 姿势10：JSON文件处理

```python
import json

# 读取JSON
with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data['name'])

# 写入JSON
data = {'name': 'Alice', 'age': 25}
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

---

## 实战：批量处理文本文件

```python
from pathlib import Path

def batch_process_txt(folder_path):
    """批量处理文件夹中的所有txt文件"""
    folder = Path(folder_path)
    
    for txt_file in folder.glob('*.txt'):
        # 读取内容
        content = txt_file.read_text(encoding='utf-8')
        
        # 处理：统计字数
        word_count = len(content)
        
        # 输出结果
        print(f"{txt_file.name}: {word_count}字")

# 使用
batch_process_txt('./documents')
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

👉 **[点击了解详情](https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA)**

---

## 相关阅读

- [Python字符串：我被忽略的20个实用方法](/course/AI相关/人民邮电出版社/ads/openclaw/python/12-Python字符串/)
- [Python字典：我用这个数据结构，把查询速度提升了100倍](/course/AI相关/人民邮电出版社/ads/openclaw/python/08-Python字典/)
- [Python列表推导式：一行代码搞定循环](/course/AI相关/人民邮电出版社/ads/openclaw/python/07-Python列表推导式/)

---

*PS：文件操作是编程的基础功，掌握这些技巧，数据处理会轻松很多。*

---


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


