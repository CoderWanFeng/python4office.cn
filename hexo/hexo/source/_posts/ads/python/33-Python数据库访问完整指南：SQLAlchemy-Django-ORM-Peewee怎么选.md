---
title: "Python 数据库访问完整指南：SQLAlchemy + Django ORM + Peewee 怎么选？"
date: 2026-06-20 17:59:35
tags: ["Python", "数据库", "SQLAlchemy", "AI工具", "公众号文章"]
categories: ["公众号文章"]
description: "Python 数据库访问完整指南：SQLAlchemy vs Django ORM vs Peewee vs PyMongo vs redis-py，5 大库完整对比"
cover: https://images.unsplash.com/photo-1526379095098-d400fd0bf935?q=80&w=1200&auto=format&fit=crop
---

大家好，我是程序员晚枫。

**Python 写应用，几乎都要用数据库。**

**"Python 用什么库访问数据库？"**

**今天这篇文章，给你 5 大数据库库完整对比。**

---

## 一、5 大 Python 数据库库

| 库 | 数据库 | 类型 | 学习难度 |
|------|---------|------|---------|
| **SQLAlchemy** | 关系型 | ORM | ⭐⭐⭐ |
| **Django ORM** | 关系型 | ORM | ⭐⭐ |
| **Peewee** | 关系型 | 轻量 ORM | ⭐ |
| **PyMongo** | MongoDB | 驱动 | ⭐ |
| **redis-py** | Redis | 驱动 | ⭐ |

---

## 二、库 1：SQLAlchemy（ORM 之王）

**SQLAlchemy**：

- **Mike Bayer 开发**
- **Python ORM 事实标准**
- 2006 年发布
- **1.x 版本：工业级**

### 5 大优势

- ✅ **功能最强**：完整 ORM
- ✅ **性能优**：Core 模式速度极快
- ✅ **多种数据库**：PostgreSQL、MySQL、SQLite、Oracle
- ✅ **类型注解**：现代版本支持
- ✅ **异步支持**：2.x 支持 async/await

### 5 大特性

#### 特性 1：两种模式

- **ORM 模式**：面向对象
- **Core 模式**：SQL 表达式
- **混合模式**

#### 特性 2：完整事务支持

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    with session.begin():
        session.add(user)
        # 自动提交或回滚
```

#### 特性 3：连接池

- 自动连接池
- **性能优化**

#### 特性 4：迁移工具

- Alembic：数据库迁移
- **Django ORM 也有类似功能**

#### 特性 5：性能监控

- SQL 日志
- 慢查询分析

### 适合场景

- 任何关系型数据库项目
- 大型项目
- **企业级应用**

### 简单示例

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

with Session(engine) as session:
    user = User(name='Alice')
    session.add(user)
    session.commit()
```

---

## 三、库 2：Django ORM（Django 专属）

**Django ORM**：

- **Django 内置**
- 与 Django 深度集成
- **Web 框架首选**

### 5 大优势

- ✅ **Django 集成**：Admin、Form、View 全打通
- ✅ **简单**：学习曲线最平缓
- ✅ **自动迁移**：`makemigrations` + `migrate`
- ✅ **Admin 后台**：自动生成
- ✅ **完整 Web 生态**

### 适合场景

- Django 项目
- 中大型 Web
- **CMS、电商**

### 简单示例

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

# 自动生成 SQL
users = User.objects.filter(name__icontains='ali')
```

**比 SQLAlchemy 简单 3 倍**。

---

## 四、库 3：Peewee（轻量首选）

**Peewee**：

- **Charles Leifer 开发**
- **单文件 ORM**
- 极简设计

### 5 大优势

- ✅ **极简**：单文件
- ✅ **易学**：5 分钟上手
- ✅ **轻量**：依赖少
- ✅ **够用**：覆盖 80% 场景
- ✅ **扩展**：playhouse 提供高级功能

### 适合场景

- 小型项目
- 微服务
- **学习 ORM 原理**

### 简单示例

```python
from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    class Meta:
        database = db

db.create_tables([Person])
Person.create(name='Alice')
```

**比 SQLAlchemy 简单 5 倍**。

---

## 五、库 4：PyMongo（MongoDB 标准）

**PyMongo**：

- **MongoDB 官方 Python 驱动**
- 文档数据库首选

### 5 大优势

- ✅ **官方驱动**
- ✅ **性能优**
- ✅ **完整功能**
- ✅ **类型提示**
- ✅ **异步支持**：motor

### 适合场景

- MongoDB 项目
- 文档数据
- **大数据**

### 简单示例

```python
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']
collection = db['users']

collection.insert_one({'name': 'Alice', 'age': 30})
```

---

## 六、库 5：redis-py（Redis 标准）

**redis-py**：

- **Redis 官方 Python 驱动**
- 缓存标准

### 5 大优势

- ✅ **官方驱动**
- ✅ **功能全**
- ✅ **异步支持**
- ✅ **性能优**
- ✅ **集群支持**

### 适合场景

- 缓存
- Session
- **消息队列**

### 简单示例

```python
import redis

r = redis.Redis(host='localhost', port=6379)
r.set('key', 'value')
r.get('key')
```

---

## 七、5 大库详细对比

| 维度 | SQLAlchemy | Django ORM | Peewee | PyMongo | redis-py |
|------|-----------|------------|--------|---------|----------|
| **数据库** | 关系型 | 关系型 | 关系型 | MongoDB | Redis |
| **学习难度** | ⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐ | ⭐ |
| **功能完整度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **性能** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **异步支持** | ✅ 2.0 | ⚠️ 部分 | ⚠️ 部分 | ✅ motor | ✅ |
| **类型注解** | ✅ 现代 | ⚠️ 部分 | ⚠️ 部分 | ✅ | ✅ |
| **企业用** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **文档** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **社区** | 最大 | 大 | 中 | 中 | 中 |

---

## 八、5 大场景选型

### 场景 1：Django 项目

**推荐**：**Django ORM**

- 集成度最高
- 自动 Admin
- **不用选**

### 场景 2：非 Django Web 项目

**推荐**：**SQLAlchemy**

- 功能最强
- 性能优
- **企业首选**

### 场景 3：小型项目

**推荐**：**Peewee**

- 简单
- 易学
- **够用就行**

### 场景 4：MongoDB 项目

**推荐**：**PyMongo**

- 官方驱动
- 性能好
- **事实标准**

### 场景 5：缓存需求

**推荐**：**redis-py**

- 官方驱动
- 高性能
- **缓存标配**

---

## 九、3 个真实案例

### 案例 1：Instagram

- **选择**：Django ORM
- **原因**：Django 项目
- **结果**：10 亿+ 用户

### 案例 2：Uber

- **选择**：SQLAlchemy + 自研
- **原因**：高并发、复杂查询
- **结果**：全球运营

### 案例 3：Dropbox

- **选择**：SQLAlchemy
- **原因**：多数据库支持
- **结果**：5 亿+ 用户

---

## 十、5 个性能优化技巧

### 技巧 1：连接池

```python
engine = create_engine(
    'postgresql://...',
    pool_size=20,
    max_overflow=10
)
```

### 技巧 2：批量操作

```python
# 慢
for user in users:
    session.add(user)

# 快
session.bulk_save_objects(users)
```

### 技巧 3：延迟加载

```python
# 慢
user.posts  # 每次都查

# 快
user.posts.select()  # 一次性查
```

### 技巧 4：索引

```python
class User(Base):
    name = Column(String, index=True)  # 索引
```

### 技巧 5：只查需要的字段

```python
# 慢
users = session.query(User).all()

# 快
users = session.query(User.name).all()
```

---

## 十一、5 个常见误区

### 误区 1：ORM 慢

- ❌ 错
- ✅ ORM 在大多数场景够用
- **慢是因为没用好**

### 误区 2：必须用 SQL

- ❌ 错
- ✅ ORM 处理 90% 场景
- **剩下 10% 优化**

### 误区 3：ORM 不可控

- ❌ 错
- ✅ SQLAlchemy 可写 SQL
- **Django ORM 也有 raw SQL**

### 误区 4：所有项目都要 ORM

- ⚠️ 部分对
- ✅ 简单查询用 SQL 更快
- **看场景**

### 误区 5：ORM 不安全

- ❌ 错
- ✅ SQLAlchemy/Django ORM 防 SQL 注入
- **比手写 SQL 更安全**

---

## 十二、5 个迁移工具

### 工具 1：Alembic（SQLAlchemy）

- https://alembic.sqlalchemy.org/
- **SQLAlchemy 官方**

### 工具 2：Django Migrations

- 内置
- `makemigrations` + `migrate`

### 工具 3：Peewee Migrations

- `peewee-migrate`
- 第三方

### 工具 4：Flyway（数据库迁移）

- 跨语言
- **企业用**

### 工具 5：Liquibase

- 跨语言
- **配置文件式**

---

## 十三、5 个数据库连接池配置

### 池 1：SQLAlchemy 默认

```python
engine = create_engine('postgresql://...')
```

### 池 2：QueuePool

```python
engine = create_engine('postgresql://...', poolclass=QueuePool)
```

### 池 3：AsyncAdaptedQueuePool

```python
engine = create_async_engine('postgresql+asyncpg://...')
```

### 池 4：NullPool（无池）

```python
engine = create_engine('postgresql://...', poolclass=NullPool)
```

### 池 5：StaticPool（单连接）

```python
engine = create_engine('sqlite:///:memory:', poolclass=StaticPool)
```

---

## 十四、给 Python 数据库开发者的 4 个建议

### 建议 1：ORM 是首选

- 90% 场景用 ORM
- **别再写裸 SQL 了**

### 建议 2：选 SQLAlchemy

- 非 Django 项目首选
- **未来 10 年 ORM 之王**

### 建议 3：学会迁移

- Alembic / Django migrations
- **数据库版本管理**

### 建议 4：性能优化

- 连接池
- 索引
- **慢查询分析**

---

## 十五、最后的最后

**Python 数据库访问，3 句话总结**：

1. **Django 项目用 Django ORM**
2. **非 Django 用 SQLAlchemy**
3. **小型用 Peewee，NoSQL 用 PyMongo/redis-py**

**学 Python 6 年，我学到的最重要的事：**

**"ORM 让数据库操作更简单、更安全。"**

**SQLAlchemy 是 Python 圈最值得学的 ORM。**

**Django ORM 是 Django 项目的"最佳拍档"。**

**2026 年，**选对 ORM，数据库开发效率翻 3 倍**。**

---

## 相关阅读

- [2026 年学习编程，你需要的不是更多教程](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)
- [🖊️ 想做视频号 / 抖音 / 小红书？AI 帮你一键生成，不用学剪辑，免费试用 3 次](https://libtv.cgref.cn/s/9omkl4jn4d)
- [🎁 国产 CodeX AI 办公助手 | 写方案/PPT/分析 一次搞定](https://www.codebuddy.cn/events/invite?inviteCode=bflfcx96gj)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [我开通了Google广告，把申请到收款的全流程教给你](https://mp.weixin.qq.com/s/scAleVOwH6kDLPuQT4BNlA)
- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT Plus 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)

---

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《50讲 · AI编程训练营》](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲，先看看适不适合自己](https://pan.quark.cn/s/8f7886f79569)
- 👉 - 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/3978Ig)
