---
title: "Python 测试完整指南：unittest + pytest + coverage 从入门到精通"
date: 2026-06-20 18:04:29
tags: ["Python", "测试", "pytest", "AI工具", "公众号文章"]
categories: ["公众号文章"]
description: "Python 测试完整指南：unittest vs pytest vs coverage 完整对比，5 大测试场景，从入门到精通"
cover: https://images.unsplash.com/photo-1526379095098-d400fd0bf935?q=80&w=1200&auto=format&fit=crop
---

大家好，我是程序员晚枫。

**写代码不测试 = 给自己挖坑。**

**"Python 用什么写测试？"**

**今天这篇文章，给你 5 大测试工具完整对比。**

---

## 一、5 大 Python 测试工具

| 工具 | 用途 | 类型 | 学习难度 |
|------|------|------|---------|
| **unittest** | 单元测试 | 内置 | ⭐⭐ |
| **pytest** | 单元测试 | 第三方 | ⭐ |
| **nose2** | 单元测试 | 第三方 | ⭐⭐ |
| **coverage** | 覆盖率 | 工具 | ⭐ |
| **tox** | 自动化测试 | 工具 | ⭐⭐⭐ |

---

## 二、工具 1：unittest（Python 内置）

**unittest**：

- **Python 内置**
- xUnit 风格
- **Java 程序员的最爱**

### 5 大优势

- ✅ **内置**
- ✅ **标准**：xUnit
- ✅ **完整**：setUp、tearDown
- ✅ **集成好**：Django、Flask 内置支持
- ✅ **稳定**

### 简单示例

```python
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
```

### 适合场景

- Java 转 Python 程序员
- 需要 xUnit 风格
- **Django 测试**

---

## 三、工具 2：pytest（首选）

**pytest**：

- **第三方**
- Python 事实标准
- **比 unittest 简单 5 倍**

### 5 大优势

- ✅ **更简单**：直接用 assert
- ✅ **强大 fixture**：测试前置/后置
- ✅ **参数化**：批量测试
- ✅ **插件丰富**：1000+ 插件
- ✅ **生态好**

### 简单示例

```python
# 不用类，直接写函数
def add(x, y):
    return x + y

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
```

**3 行代码 = 测试**。

**比 unittest 简单 5 倍**。

### pytest 高级特性

#### 1. Fixture

```python
import pytest

@pytest.fixture
def user():
    return {"name": "Alice", "age": 30}

def test_user_name(user):
    assert user["name"] == "Alice"
```

#### 2. 参数化

```python
@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_add(x, y, expected):
    assert add(x, y) == expected
```

#### 3. Mock

```python
from unittest.mock import patch

@patch('module.function')
def test_mock(mock_func):
    mock_func.return_value = 42
    # 测试
```

### 适合场景

- **所有 Python 项目**
- 简单易用
- **首选**

---

## 四、工具 3：coverage（覆盖率）

**coverage**：

- **测试覆盖率**
- 看哪些代码被测试
- **质量保证**

### 5 大优势

- ✅ **标准工具**
- ✅ **多种报告**：HTML、XML、JSON
- ✅ **分支覆盖**
- ✅ **集成 CI/CD**
- ✅ **可视化**

### 简单使用

```bash
# 安装
pip install coverage

# 运行
coverage run -m pytest

# 报告
coverage report
coverage html
```

### 覆盖率指标

- **行覆盖**：多少行被跑过
- **分支覆盖**：多少分支被覆盖
- **函数覆盖**：多少函数被调用
- **80% 覆盖率**是常见标准

### 适合场景

- **所有项目**
- 质量保证
- **CI/CD 必备**

---

## 五、工具 4：tox（自动化测试）

**tox**：

- **自动化测试工具**
- 多 Python 版本测试
- **CI/CD 必备**

### 5 大优势

- ✅ **多 Python 版本**
- ✅ **自动虚拟环境**
- ✅ **CI/CD 友好**
- ✅ **统一配置**
- ✅ **依赖管理**

### 简单配置（tox.ini）

```ini
[tox]
envlist = py310, py311, py312, py313, py314

[testenv]
deps = pytest
commands = pytest
```

### 适合场景

- 库开发
- 跨版本兼容
- **开源项目**

---

## 六、工具 5：nose2（pytest 之前的标准）

**nose2**：

- **unittest 增强版**
- pytest 之前的标准
- **目前已被 pytest 取代**

### 现状

- ⚠️ **不推荐新项目使用**
- 老项目可能还在用
- **新项目用 pytest**

---

## 七、5 大工具详细对比

| 维度 | unittest | pytest | coverage | tox | nose2 |
|------|----------|--------|----------|-----|-------|
| **学习难度** | ⭐⭐ | ⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐ |
| **功能** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **生态** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **速度** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **现代化** | ⚠️ 传统 | ✅ 现代 | ✅ 现代 | ✅ 现代 | ⚠️ 旧 |
| **CI/CD** | ✅ | ✅ | ✅ | ✅✅ | ✅ |
| **推荐度** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐ |

---

## 八、5 大测试类型

### 类型 1：单元测试

- **测试单个函数/类**
- 最基础
- **首选 pytest**

### 类型 2：集成测试

- **测试多个组件**
- 验证集成
- **pytest + fixture**

### 类型 3：端到端测试

- **测试整个系统**
- Selenium、Playwright
- **关键路径**

### 类型 4：性能测试

- **测试性能**
- locust、wrk
- **压力测试**

### 类型 5：安全测试

- **测试安全漏洞**
- bandit、safety
- **安全必备**

---

## 九、pytest 5 大最佳实践

### 实践 1：测试文件命名

- `test_*.py`
- `*_test.py`
- pytest 自动发现

### 实践 2：测试函数命名

```python
def test_add_two_positive_numbers():
    # 名字说明场景
    pass
```

### 实践 3：AAA 模式

- **Arrange**：准备
- **Act**：执行
- **Assert**：断言

### 实践 4：一个测试一个断言

```python
# 不好：多个断言
def test_user():
    assert user.name == 'Alice'
    assert user.age == 30
    assert user.email == 'a@b.com'

# 好：分开
def test_user_name():
    assert user.name == 'Alice'

def test_user_age():
    assert user.age == 30
```

### 实践 5：测试覆盖率 80%+

- 关键模块 90%+
- 一般模块 80%+
- **CI 必须有覆盖率门槛**

---

## 十、5 个常见误区

### 误区 1：测试浪费时间

- ❌ 错
- ✅ 写测试时间 < 修 bug 时间
- **长期赚**

### 误区 2：测试覆盖率越高越好

- ❌ 错
- ✅ 100% 覆盖率 ≠ 0 bug
- **关键是关键路径**

### 误区 3：测试 = pytest

- ⚠️ 部分对
- ✅ pytest 是首选
- **但也要覆盖率、Mock、CI**

### 误区 4：写测试不写文档

- ❌ 错
- ✅ 测试也是文档
- **好的测试 = 好的示例**

### 误区 5：测试慢没关系

- ❌ 错
- ✅ 测试要快
- **慢了没人愿意跑**

---

## 十一、5 个真实项目测试案例

### 案例 1：requests

- **选择**：pytest
- **覆盖率**：90%+
- **结果**：最流行的 Python HTTP 库

### 案例 2：Flask

- **选择**：pytest + coverage
- **覆盖率**：95%+
- **结果**：最流行的 Web 框架

### 案例 3：Django

- **选择**：unittest
- **覆盖率**：85%+
- **结果**：最流行的全栈框架

### 案例 4：FastAPI

- **选择**：pytest
- **覆盖率**：90%+
- **结果**：最快的 Python Web 框架

### 案例 5：Pandas

- **选择**：pytest + numpy testing
- **覆盖率**：80%+
- **结果**：最流行的数据分析库

---

## 十二、5 个测试工具组合

### 组合 1：标准项目

```python
pytest + coverage + tox
```

### 组合 2：Django 项目

```python
pytest-django + coverage
```

### 组合 3：Web 项目

```python
pytest + pytest-flask + coverage + locust
```

### 组合 4：数据科学

```python
pytest + coverage + great_expectations
```

### 组合 5：开源库

```python
pytest + coverage + tox + sphinx
```

---

## 十三、5 个 CI/CD 集成示例

### CI 1：GitHub Actions

```yaml
- name: Test
  run: |
    pip install pytest coverage
    coverage run -m pytest
    coverage report
```

### CI 2：GitLab CI

```yaml
test:
  script:
    - pip install pytest coverage
    - coverage run -m pytest
    - coverage report
```

### CI 3：Jenkins

```groovy
stage('Test') {
    steps {
        sh 'pip install pytest coverage'
        sh 'coverage run -m pytest'
        sh 'coverage report'
    }
}
```

### CI 4：CircleCI

```yaml
- run: pip install pytest coverage
- run: coverage run -m pytest
- run: coverage report
```

### CI 5：Travis CI

```yaml
script:
  - pip install pytest coverage
  - coverage run -m pytest
  - coverage report
```

---

## 十四、给 Python 测试学习者的 4 个建议

### 建议 1：先学 pytest

- 最简单
- 1 周上手
- **首选**

### 建议 2：覆盖率达到 80%

- 关键模块 90%+
- **质量保证**

### 建议 3：CI/CD 集成

- 每次提交自动跑测试
- **不能漏**

### 建议 4：TDD（测试驱动开发）

- 先写测试
- 再写代码
- **专业做法**

---

## 十五、最后的最后

**Python 测试，3 句话总结**：

1. **pytest 是首选**：简单、强大、生态好
2. **coverage 是必备**：80% 覆盖率
3. **CI/CD 集成**：每次提交跑测试

**学 Python 6 年，我学到的最重要的事：**

**"测试不是浪费时间，**是节省时间**。"**

**写 1 小时测试，节省 10 小时修 bug。**

**pytest + coverage + CI/CD = 任何 Python 项目的"金标准"。**

**从今天开始，**每个项目都写测试**。**

**3 个月后，你会感谢自己。**

---

## 相关阅读

- [2026 年学习编程，你需要的不是更多教程](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)
- [🖊️ 想做视频号 / 抖音 / 小红书？AI 帮你一键生成，不用学剪辑，免费试用 3 次](https://libtv.cgref.cn/s/9omkl4jn4d)
- [🎁 国产 CodeX AI 办公助手 | 写方案/PPT/分析 一次搞定](https://www.codebuddy.cn/events/invite?inviteCode=bflfcx96gj)
- [Codex 入门指南，从零基础到实战，看这一篇就够了！](https://mp.weixin.qq.com/s/ilvNENMEiPy2uEYyDflvQA)
- [我开通了Google广告，把申请到收款的全流程教给你](https://mp.weixin.qq.com/s/scAleVOwH6kDLPuQT4BNlA)
- [用上 OpenCode 的5 个免费大模型，省了我 200 刀 ChatGPT Plus 年费](https://mp.weixin.qq.com/s/0eL4-CvFDkqHmDYY0YrrwA)

---

**科技不高冷，AI很好用。**
我是晚枫，关注我，带你一起玩AI！


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《50讲 · AI编程训练营》](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲，先看看适不适合自己](https://pan.quark.cn/s/8f7886f79569)
- 👉 - 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://r7up9.xetslk.com/s/3978Ig)
