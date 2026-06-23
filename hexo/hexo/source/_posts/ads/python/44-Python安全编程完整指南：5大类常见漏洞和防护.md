---
title: "Python 安全编程完整指南：5 大类常见漏洞和防护"
date: 2026-06-20 18:09:12
tags: ["Python", "安全", "SQL注入", "XSS", "AI工具", "公众号文章"]
categories: ["公众号文章"]
description: "Python 安全编程完整指南：SQL 注入、XSS、CSRF、命令注入、文件上传，5 大漏洞防护实战"
cover: https://images.unsplash.com/photo-1526379095098-d400fd0bf935?q=80&w=1200&auto=format&fit=crop
---

大家好，我是程序员晚枫。

**Python 写的应用被黑了？**

**99% 是你没做好安全防护。**

**今天讲透 5 大类常见漏洞。**

---

## 一、为什么 Python 应用会被黑？

**5 大常见漏洞**：

1. SQL 注入
2. XSS
3. CSRF
4. 命令注入
5. 文件上传漏洞

**每一个都"低级但致命"**。

---

## 二、漏洞 1：SQL 注入（最常见）

### 危险代码

```python
# 危险
def login(username, password):
    query = f"SELECT * FROM users WHERE name = '{username}' AND password = '{password}'"
    cursor.execute(query)
```

**攻击者输入**：

```
username = "admin' OR '1'='1"
password = "anything"
```

**生成的 SQL**：

```sql
SELECT * FROM users WHERE name = 'admin' OR '1'='1' AND password = 'anything'
```

**结果**：绕过密码验证！

### 安全代码

```python
# 安全
def login(username, password):
    query = "SELECT * FROM users WHERE name = %s AND password = %s"
    cursor.execute(query, (username, password))
```

**用参数化查询，100% 防 SQL 注入**。

### 真实案例

- **某电商平台**：被 SQL 注入，泄露 100 万用户
- **某政府网站**：被攻击，数据被篡改
- **SQL 注入是 OWASP Top 10 第一名**

---

## 三、漏洞 2：XSS（跨站脚本）

### 危险代码

```python
# 危险
@app.route('/search')
def search():
    query = request.args.get('q')
    return f"搜索结果：{query}"  # 直接返回用户输入
```

**攻击者输入**：

```
?q=<script>alert(document.cookie)</script>
```

**结果**：用户的 cookie 被窃取！

### 安全代码

```python
# 安全
from markupsafe import escape

@app.route('/search')
def search():
    query = request.args.get('q')
    return f"搜索结果：{escape(query)}"  # 转义
```

**或者用模板自动转义**：

```html
<!-- Jinja2 自动转义 -->
<p>搜索结果：{{ query }}</p>
```

### 真实案例

- **微博 XSS**：蠕虫传播
- **论坛 XSS**：管理员账号被盗
- **XSS 是 OWASP Top 10 第 3 名**

---

## 四、漏洞 3：CSRF（跨站请求伪造）

### 攻击原理

**用户登录了银行 A**，**同时访问了恶意网站 B**。

**B 网站向银行 A 发送转账请求**，**因为用户已登录，银行执行**。

### 防护 1：CSRF Token

```python
# Django 自带 CSRF 防护
# 模板中
<form method="post">
    {% csrf_token %}
    <input type="text" name="amount">
    <button type="submit">转账</button>
</form>

# 视图
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def transfer(request):
    amount = request.POST.get('amount')
    # 处理转账
```

### 防护 2：SameSite Cookie

```python
# Flask
from flask import Flask
app = Flask(__name__)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
```

### 防护 3：检查 Referer

```python
def transfer(request):
    referer = request.headers.get('Referer')
    if not referer or 'mybank.com' not in referer:
        return 'Forbidden', 403
    # 处理转账
```

### 真实案例

- **GitHub 曾经有 CSRF 漏洞**：用户仓库被自动创建
- **NYT 曾经被攻击**：用户被自动点赞**

---

## 五、漏洞 4：命令注入

### 危险代码

```python
# 危险
import os

def ping(host):
    return os.popen(f"ping -c 1 {host}").read()
```

**攻击者输入**：

```
host = "8.8.8.8; rm -rf /"
```

**结果**：**删除整个服务器！**

### 安全代码

```python
# 安全
import subprocess

def ping(host):
    # 验证输入
    if not host.replace('.', '').isdigit():
        return "Invalid host"
    # 用列表参数，不传 shell=True
    return subprocess.run(
        ['ping', '-c', '1', host],
        capture_output=True, text=True
    ).stdout
```

**关键**：

- **不要用 shell=True**
- **验证输入**
- **用列表参数**

### 真实案例

- **某云服务**：被命令注入，服务器被攻击
- **命令注入是 OWASP Top 10 重要项**

---

## 六、漏洞 5：文件上传漏洞

### 危险代码

```python
# 危险
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f"/uploads/{file.filename}")  # 危险！
```

**攻击者上传**：

- `shell.php`（Web shell）
- `image.jpg.php`（伪装图片的 PHP）
- `../../../etc/passwd`（路径穿越）

### 安全代码

```python
# 安全
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    
    # 1. 检查文件名
    if not allowed_file(file.filename):
        return 'Invalid file', 400
    
    # 2. 用 secure_filename
    filename = secure_filename(file.filename)
    
    # 3. 不覆盖原文件名
    file.save(os.path.join('/uploads', filename))
    
    return 'OK'
```

### 真实案例

- **某论坛**：被上传 Web shell
- **很多 CMS**：被上传木马
- **文件上传是 Web 漏洞第一名**

---

## 七、5 大其他常见漏洞

### 漏洞 6：密码明文存储

**错误**：

```python
# 危险
user.password = password  # 明文存储
```

**正确**：

```python
import bcrypt

password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

### 漏洞 7：硬编码密钥

**错误**：

```python
# 危险
SECRET_KEY = "my-secret-key-12345"  # 硬编码
```

**正确**：

```python
import os
SECRET_KEY = os.environ.get('SECRET_KEY')  # 环境变量
```

### 漏洞 8：日志泄露敏感信息

**错误**：

```python
logger.info(f"User {username} logged in with password {password}")
```

**正确**：

```python
logger.info(f"User {username} logged in")
```

### 漏洞 9：反序列化漏洞

**危险**：

```python
# 危险
import pickle
data = pickle.loads(user_input)  # 可执行任意代码
```

**正确**：

```python
# 用 JSON 代替 pickle
import json
data = json.loads(user_input)
```

### 漏洞 10：依赖库漏洞

**风险**：

- requests 旧版本有漏洞
- numpy 旧版本有问题

**防护**：

```bash
# 用 safety 检查
pip install safety
safety check

# 用 pip-audit
pip install pip-audit
pip-audit
```

---

## 八、5 大安全工具

### 工具 1：bandit（代码扫描）

```bash
pip install bandit
bandit -r my_project/
```

### 工具 2：safety（依赖检查）

```bash
pip install safety
safety check
```

### 工具 3：pip-audit（依赖审计）

```bash
pip install pip-audit
pip-audit
```

### 工具 4：OWASP ZAP（Web 扫描）

- 专业的 Web 漏洞扫描器
- **企业级**

### 工具 5：Snyk（持续监控）

- GitHub 集成
- **PR 自动检查**

---

## 九、5 大安全最佳实践

### 实践 1：参数化查询

```python
# ✅ 永远
cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
```

### 实践 2：转义输出

```python
# ✅ 永远
return escape(user_input)
```

### 实践 3：环境变量存密钥

```python
# ✅ 永远
SECRET_KEY = os.environ['SECRET_KEY']
```

### 实践 4：HTTPS

```python
# ✅ 永远
# 强制 HTTPS
@app.before_request
def force_https():
    if not request.is_secure:
        return redirect(url_for(request.endpoint, _external=True, **request.view_args), code=301)
```

### 实践 5：定期更新依赖

```bash
# 每月
pip list --outdated
pip install --upgrade <package>
```

---

## 十、5 个真实安全漏洞案例

### 案例 1：Equifax 数据泄露

- **漏洞**：Apache Struts 漏洞
- **损失**：1.43 亿用户数据
- **原因**：未及时更新依赖

### 案例 2：Yahoo 30 亿账号泄露

- **漏洞**：弱加密 + 内部威胁
- **损失**：30 亿账号
- **原因**：密码哈希弱

### 案例 3：WannaCry 勒索病毒

- **漏洞**：Windows SMB 漏洞
- **损失**：100 亿美元
- **原因**：未打补丁

### 案例 4：Capital One 数据泄露

- **漏洞**：SSRF + 错误配置
- **损失**：1 亿用户
- **原因**：WAF 配置错误

### 案例 5：Facebook 数据泄露

- **漏洞**：API 权限问题
- **损失**：8700 万用户
- **原因**：API 设计缺陷

---

## 十一、给 Python 安全编程学习者的 4 个建议

### 建议 1：OWASP Top 10

- 必读
- **每 1-2 年更新**
- https://owasp.org/

### 建议 2：用 bandit 扫代码

- 每次提交
- **CI 必备**

### 建议 3：定期更新依赖

- 每月
- **自动化**

### 建议 4：HTTPS 强制

- 全站
- **HSTS、CSP**

---

## 十二、最后的最后

**Python 安全编程，3 句话总结**：

1. **5 大漏洞必防**：SQL 注入、XSS、CSRF、命令注入、文件上传
2. **参数化查询 + 转义 + Token**：3 大防护
3. **bandit + safety + 定期更新**：3 大工具

**学 Python 6 年，我学到的最重要的事：**

**"安全不是功能，是责任。"**

**每一个漏洞，**都可能让公司损失百万**。**

**OWASP Top 10 + bandit + safety = 任何 Python 项目的"安全金标准"。**

**从今天开始，**每个项目都做安全检查**。**

---

## 相关阅读

- [2026 年学习编程，你需要的不是更多教程](https://mp.weixin.qq.com/s/YS0shsl6vJD_wUzow7NOnw)
- [🖊️ 想做视频号 / 抖音 / 小红书？AI 帮你一键生成，不用学剪辑，免费试用 3 次](https://www.liblib.tv/?sourceid=005902&utm=cg&cgv=9omkl4jn4d)
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
