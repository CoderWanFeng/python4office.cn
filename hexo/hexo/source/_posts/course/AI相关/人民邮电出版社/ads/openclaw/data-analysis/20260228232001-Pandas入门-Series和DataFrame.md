---
title: Pandas入门：我用2个数据结构，搞定了所有表格数据处理
date: 2026-02-28 23:20:00
tags: [数据分析, Pandas, Series, DataFrame]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9209df5a-99d2-40dc-af34-b10b43be9026/12-ai.jpg" />
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
<a href="https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种<a href="https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ" target="_blank">AI项目</a>的程序员晚枫。

欢迎来到Pandas的世界！

**Pandas是Python数据分析的核心库**，它提供了两个强大的数据结构：Series和DataFrame。掌握它们，你就能像操作Excel一样处理数据，而且更快更强。

---

## 为什么用Pandas？

### Excel vs Pandas

| 能力 | Excel | Pandas |
|-----|-------|--------|
| 数据量 | 100万行卡顿 | 千万行流畅 |
| 自动化 | 手动操作 | 代码复现 |
| 复杂计算 | 公式受限 | Python灵活 |
| 数据源 | 本地文件 | 数据库/API |

**一句话：Excel能做的Pandas都能做，而且做得更好。**

---

## Series：一维数据

Series就像Excel的一列，带索引的数组。

### 创建Series
```python
import pandas as pd

# 从列表创建
s = pd.Series([85, 90, 78, 92])
print(s)
# 0    85
# 1    90
# 2    78
# 3    92
# dtype: int64

# 自定义索引
s = pd.Series([85, 90, 78, 92], index=['Alice', 'Bob', 'Charlie', 'David'])
print(s)
# Alice      85
# Bob        90
# Charlie    78
# David      92
# dtype: int64
```

### Series基本操作
```python
# 通过索引访问
print(s['Alice'])       # 85
print(s[0])             # 85（位置索引）

# 切片
print(s['Alice':'Charlie'])  # 包含两端

# 条件筛选
print(s[s > 80])        # 大于80的

# 统计信息
print(s.mean())         # 平均值
print(s.max())          # 最大值
print(s.describe())     # 完整统计描述
```

---

## DataFrame：二维表格

DataFrame就是Excel的整张表，有行索引和列名。

### 创建DataFrame
```python
# 方式1：从字典创建
data = {
    '姓名': ['Alice', 'Bob', 'Charlie'],
    '年龄': [25, 30, 35],
    '城市': ['北京', '上海', '广州'],
    '薪资': [8000, 12000, 15000]
}
df = pd.DataFrame(data)
print(df)

# 方式2：从列表创建
df = pd.DataFrame([
    ['Alice', 25, '北京', 8000],
    ['Bob', 30, '上海', 12000],
    ['Charlie', 35, '广州', 15000]
], columns=['姓名', '年龄', '城市', '薪资'])

# 方式3：从NumPy数组创建
import numpy as np
df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=['A', 'B', 'C'],
    index=['a', 'b', 'c', 'd', 'e']
)
```

### 查看数据
```python
# 基本信息
print(df.shape)         # (3, 4) - 3行4列
print(df.columns)       # 列名
print(df.index)         # 行索引
print(df.dtypes)        # 每列的数据类型

# 查看内容
print(df.head(2))       # 前2行
print(df.tail(2))       # 后2行
print(df.info())        # 详细信息
print(df.describe())    # 统计描述
```

---

## 数据选择

### 选择列
```python
# 单列（返回Series）
ages = df['年龄']

# 多列（返回DataFrame）
subset = df[['姓名', '薪资']]

# 新增列
df['工作年限'] = df['年龄'] - 22
```

### 选择行
```python
# 按位置（iloc）
df.iloc[0]              # 第0行
df.iloc[0:2]            # 第0到1行
df.iloc[[0, 2]]         # 第0和第2行

# 按标签（loc）
df.loc[0]               # 索引为0的行
df.loc[0:2]             # 索引0到2（包含2）
```

### 同时选择行列
```python
# loc[行标签, 列标签]
df.loc[0, '姓名']       # 第0行的姓名
df.loc[0:2, ['姓名', '薪资']]  # 多行多列

# iloc[行位置, 列位置]
df.iloc[0, 0]           # 第0行第0列
df.iloc[0:2, 0:3]       # 切片
```

---

## 条件筛选

```python
# 单条件
high_salary = df[df['薪资'] > 10000]

# 多条件（与）
result = df[(df['薪资'] > 10000) & (df['年龄'] < 35)]

# 多条件（或）
result = df[(df['城市'] == '北京') | (df['城市'] == '上海')]

# isin方法
result = df[df['城市'].isin(['北京', '上海'])]

# 字符串匹配
result = df[df['姓名'].str.contains('li')]
```

---

## 排序和排名

```python
# 按单列排序
df.sort_values('薪资')           # 升序
df.sort_values('薪资', ascending=False)  # 降序

# 按多列排序
df.sort_values(['城市', '薪资'], ascending=[True, False])

# 排名
df['薪资排名'] = df['薪资'].rank(ascending=False)
```

---

## 常用属性

```python
print(df.values)        # 转为NumPy数组
print(df.T)             # 转置
print(df.size)          # 元素总数
print(df.empty)         # 是否为空
```

---

## 实战：员工信息管理

```python
import pandas as pd

# 创建员工数据
employees = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '部门': ['技术', '销售', '技术', '人事', '销售'],
    '入职年份': [2019, 2020, 2021, 2019, 2022],
    '月薪': [15000, 12000, 18000, 10000, 11000]
})

# 计算年薪
employees['年薪'] = employees['月薪'] * 14

# 找出技术部高薪员工（月薪>16000）
tech_high = employees[(employees['部门'] == '技术') & (employees['月薪'] > 16000)]

# 按部门分组统计
dept_stats = employees.groupby('部门').agg({
    '月薪': ['mean', 'min', 'max'],
    '姓名': 'count'
})

print("=== 员工信息 ===")
print(employees)
print("\n=== 技术部高薪员工 ===")
print(tech_high)
print("\n=== 部门统计 ===")
print(dept_stats)
```

---

## 下节预告

下一课我们将学习**Pandas数据读取与保存**，掌握如何导入导出各种格式的数据。

👉 **[继续阅读：Pandas数据读取与保存](/course/AI相关/人民邮电出版社/ads/openclaw/data-analysis/20260228232101-Pandas数据读取与保存/)**

---

## 💬 加入学习交流群

扫码加入**Python学习交流群**，和数千名同学一起进步：

👉 **[点击加入交流群](http://www.python4office.cn/wechat-group/)**

群里不定期分享：
- 数据分析实战案例
- Python学习资料
- 求职面试经验
- 行业最新动态

---

## 推荐：AI Python数据分析实战营

🎁 **限时福利**：送《利用Python进行数据分析》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)**

---

## 课程导航

**上一篇：** [NumPy进阶-数学运算](/course/AI相关/人民邮电出版社/ads/openclaw/data-analysis/20260228231901-NumPy进阶-数学运算/)

**下一篇：** [Pandas数据读取与保存](/course/AI相关/人民邮电出版社/ads/openclaw/data-analysis/20260228232101-Pandas数据读取与保存/)

---

*PS：Pandas是数据分析的核心。Series和DataFrame这两个概念一定要理解透彻。*
