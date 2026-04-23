---
title: Pandas入门：我用2个数据结构，搞定了所有表格数据处理
date: 2026-02-28 23:20:00
tags: [数据分析, Pandas, Series, DataFrame]
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

大家好，我是正在实战各种<a href="https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw" target="_blank">AI项目</a>的程序员晚枫。

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


### 性能对比：DataFrame vs Excel vs SQL

```python
import pandas as pd
import numpy as np
import time

# 10万行数据，分组+聚合
df = pd.DataFrame({
    'category': np.random.choice(['A', 'B', 'C', 'D'], 100000),
    'value': np.random.randn(100000) * 100 + 500
})

# Pandas方式
start = time.time()
result = df.groupby('category')['value'].agg(['mean', 'sum', 'count'])
print(f"Pandas: {time.time()-start:.4f}秒")

# Excel方式：手动操作约5分钟（如果没崩溃的话）
# SQL方式：写查询约1分钟
```

| 操作 | Excel | SQL | Pandas |
|------|-------|-----|--------|
| 10万行分组聚合 | 5分钟 | 30秒 | 0.01秒 |
| 多条件筛选 | 2分钟 | 15秒 | 0.005秒 |
| 数据透视表 | 3分钟 | N/A | 0.02秒 |

## 进阶用法

### DataFrame的链式操作

```python
# 链式操作（pipe风格）——代码更优雅
result = (df
    .query('age >= 18')
    .assign(income_k=lambda x: x['income'] / 1000)
    .groupby('city')
    .agg({'income_k': ['mean', 'std'], 'age': 'median'})
    .round(2)
)
```

### MultiIndex多层索引

```python
# 创建多层索引
index = pd.MultiIndex.from_product([
    ['华东', '华南', '华北'],
    ['Q1', 'Q2', 'Q3', 'Q4']
], names=['区域', '季度'])

data = pd.Series(np.random.randint(100, 1000, 12), index=index)
print(data)

# 选取特定区域
print(data.loc['华东'])

# 选取特定季度（所有区域）
print(data.loc[:, 'Q1'])

# 展开为DataFrame
df = data.unstack()  # 区域为行，季度为列
```

## 避坑指南

### ❌ 坑1：SettingWithCopyWarning

```python
# 错误写法（触发警告，修改可能无效）
subset = df[df['age'] > 30]  # 这可能返回视图
subset['score'] = 100  # Warning! 可能没生效

# 正确写法1：显式copy
subset = df[df['age'] > 30].copy()
subset['score'] = 100  # 安全

# 正确写法2：用loc直接修改原表
df.loc[df['age'] > 30, 'score'] = 100
```

### ❌ 坑2：索引重置陷阱

```python
# 筛选后索引不连续
filtered = df[df['score'] > 80]
print(filtered.index)  # 可能是 [0, 3, 7, 15, ...]

# 用iloc按位置取和用loc按标签取结果不同
print(filtered.iloc[0])   # 第1行
print(filtered.loc[0])    # 标签为0的行（可能不存在！）

# 解决：重置索引
filtered = filtered.reset_index(drop=True)
```

## 实战案例：分析在线教育平台学员数据

```python
import pandas as pd
import numpy as np

# 模拟学员数据
np.random.seed(42)
n = 5000
df = pd.DataFrame({
    'user_id': range(10001, 10001 + n),
    'course': np.random.choice(['Python入门', '数据分析', 'AI编程', '自动化办公'], n),
    'progress': np.random.uniform(0, 100, n).round(1),
    'score': np.random.normal(75, 15, n).clip(0, 100).round(1),
    'study_hours': np.random.exponential(20, n).round(1),
    'signup_date': pd.date_range('2025-01-01', periods=n, freq='2H'),
    'is_vip': np.random.choice([True, False], n, p=[0.3, 0.7]),
    'city': np.random.choice(['北京', '上海', '广州', '深圳', '成都', '重庆'], n)
})

# 1. 数据概览
print(f"学员总数: {len(df)}")
print(f"\n各课程人数:")
print(df['course'].value_counts())
print(f"\n平均学习进度: {df['progress'].mean():.1f}%")

# 2. VIP vs 普通学员对比
print(f"\nVIP学员平均进度: {df[df['is_vip']]['progress'].mean():.1f}%")
print(f"普通学员平均进度: {df[~df['is_vip']]['progress'].mean():.1f}%")

# 3. 城市分布
print(f"\n各城市学员数:")
print(df['city'].value_counts())

# 4. 各课程完成率（进度>80%视为完成）
completion = df.assign(completed=df['progress'] > 80).groupby('course')['completed'].mean()
print(f"\n各课程完成率:")
print((completion * 100).round(1).astype(str) + '%')
```



### DataFrame的常用属性和方法速查

```python
# 创建示例DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'city': ['北京', '上海', '广州', '深圳', '成都'],
    'salary': [15000, 20000, 25000, 18000, 22000]
})

# 形状和维度
print(df.shape)     # (5, 4) - 5行4列
print(df.ndim)      # 2 - 二维
print(df.size)      # 20 - 总元素数

# 列和索引
print(df.columns)   # 列名
print(df.index)     # 行索引
print(df.dtypes)    # 每列数据类型

# 查看数据
print(df.head(3))       # 前3行
print(df.tail(3))       # 后3行
print(df.sample(2))     # 随机2行
print(df.describe())    # 统计摘要
print(df.info())        # 数据概览

# 转换
print(df.values)        # 转为NumPy数组
print(df.to_dict())     # 转为字典
print(df.to_csv())      # 转为CSV字符串
```

### DataFrame数据选取速查

```python
# 选取列
df['name']             # 单列，返回Series
df[['name', 'age']]    # 多列，返回DataFrame

# 按位置选取（iloc）
df.iloc[0]             # 第1行
df.iloc[0:3]           # 前3行
df.iloc[:, 0:2]        # 前2列
df.iloc[[0, 2], [1, 3]] # 指定行和列

# 按标签选取（loc）
df.loc[0]              # 索引为0的行
df.loc[0:2]            # 索引0到2的行（含2）
df.loc[:, 'name':'age'] # name到age列
df.loc[df['age'] > 30]  # 条件筛选

# at和iat（取单个值，更快）
df.at[0, 'name']       # 按标签
df.iat[0, 0]           # 按位置
```

### Series vs DataFrame对比

```python
# Series是一维，DataFrame是二维
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Series运算
s + 10           # 广播
s * 2            # 广播
s > 2            # 布尔索引

# Series常用方法
s.value_counts()  # 值计数
s.unique()        # 唯一值
s.sort_values()   # 排序
s.isna()          # 检查缺失
s.fillna(0)       # 填充缺失
s.astype(float)   # 类型转换

# DataFrame的每列都是Series
type(df['A'])     # pandas.core.series.Series
```


## 下节预告

下一课我们将学习**Pandas数据读取与保存**，掌握如何导入导出各种格式的数据。

👉 **[继续阅读：Pandas数据读取与保存](/course/AI相关/人民邮电出版社/ads/openclaw/data-analysis/20260228232101-Pandas数据读取与保存/)**

---

## 💬 加入学习交流群

扫码加入**Python学习交流群**，和数千名同学一起进步：

👉 **[点击加入交流群](https://www.python4office.cn/wechat-group/)**

群里不定期分享：
- 数据分析实战案例
- Python学习资料
- 求职面试经验
- 行业最新动态

---

## 推荐：AI Python数据分析实战营

🎁 **限时福利**：送《利用Python进行数据分析》实体书

👉 **[点击了解详情](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**

---

## 课程导航

**上一篇：** [NumPy进阶-数学运算](/course/AI相关/人民邮电出版社/ads/openclaw/data-analysis/20260228231901-NumPy进阶-数学运算/)

**下一篇：** [Pandas数据读取与保存](/course/AI相关/人民邮电出版社/ads/openclaw/data-analysis/20260228232101-Pandas数据读取与保存/)

---

*PS：Pandas是数据分析的核心。Series和DataFrame这两个概念一定要理解透彻。*

---


---

## 📚 推荐教材

**主教材**：[《Excel+Python 飞速搞定数据分析与处理（图灵出品）》](https://u.jd.com/N6MUwXO)

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
