---
title: Python实战项目：我做了个自动邮件系统，每天定时发送数据报告
date: 2026-02-28 21:10:00
tags: [Python实战, 自动化, 邮件]
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

你有没有这样的经历？每天上班第一件事就是——打开Excel，复制昨天的数据，做个表格，截图，写邮件，发给老板。一套流程下来，半小时没了。更要命的是，这个活儿每天都在重复。

> 💡 **场景**：你是运营人员，每天要向老板汇报昨天的销售数据。以前你都是手动整理Excel、截图、发邮件——每天重复同样的工作。现在用Python自动化，设定好脚本，每天早上自动发到老板邮箱！

我就是受不了这种重复劳动，才写的这个自动邮件系统。今天把它分享给你，50行代码解放你的双手。

---

## 项目功能

- 自动生成数据报告（模拟销售数据）
- 创建HTML格式的美观邮件
- 添加附件（CSV文件）
- 支持多个收件人
- 可设置定时发送
- 完善的错误处理和日志

---

## 准备工作：获取邮箱授权码

在写代码之前，你需要先获取邮箱的SMTP授权码（不是登录密码！）。

### QQ邮箱获取步骤

1. 登录QQ邮箱 → 设置 → 账户
2. 找到"POP3/SMTP服务" → 开启
3. 点击"生成授权码" → 按提示用手机发短信
4. 获得16位授权码，保存好！

### Gmail获取步骤

1. 开启两步验证
2. 创建应用专用密码：Google账户 → 安全 → 应用专用密码
3. 生成16位密码

> ⚠️ **注意**：千万不要把授权码硬编码在代码里！建议用环境变量或配置文件。

---

## 完整代码

```python
import smtplib
import csv
import io
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def generate_sales_data():
    """生成模拟销售数据"""
    data = []
    products = ['产品A', '产品B', '产品C', '产品D']
    
    for i, product in enumerate(products):
        sales = {
            'product': product,
            'quantity': 100 + i * 50,
            'revenue': 5000 + i * 2500,
            'growth': round((i * 5.2 + 3.1), 1),  # 同比增长率
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        data.append(sales)
    
    return data

def create_csv_attachment(data):
    """将数据转换为CSV格式"""
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['product', 'quantity', 'revenue', 'growth', 'date'])
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()

def create_email_content(data):
    """创建HTML邮件内容"""
    total_revenue = sum(item['revenue'] for item in data)
    total_quantity = sum(item['quantity'] for item in data)
    avg_growth = sum(item['growth'] for item in data) / len(data)
    
    # 增长标识
    growth_icon = "📈" if avg_growth > 0 else "📉"
    
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; color: #333; }}
            h2 {{ color: #2c3e50; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
            th {{ background-color: #3498db; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            .summary {{ background-color: #ecf0f1; padding: 15px; margin: 20px 0; border-radius: 8px; }}
            .positive {{ color: #27ae60; }}
            .footer {{ color: #95a5a6; margin-top: 30px; font-size: 12px; }}
        </style>
    </head>
    <body>
        <h2>📊 每日销售报告</h2>
        <p>日期: {datetime.now().strftime('%Y年%m月%d日')}</p>
        
        <div class="summary">
            <h3>汇总数据</h3>
            <p><strong>总销售额:</strong> ¥{total_revenue:,}</p>
            <p><strong>总销量:</strong> {total_quantity}件</p>
            <p><strong>平均增长率:</strong> <span class="{'positive' if avg_growth > 0 else ''}">{growth_icon} {avg_growth}%</span></p>
        </div>
        
        <h3>详细数据</h3>
        <table>
            <tr>
                <th>产品</th>
                <th>销量</th>
                <th>销售额</th>
                <th>同比增长</th>
            </tr>
    """
    
    for item in data:
        growth_class = "positive" if item['growth'] > 0 else ""
        growth_icon_item = "📈" if item['growth'] > 0 else "📉"
        html += f"""
            <tr>
                <td>{item['product']}</td>
                <td>{item['quantity']}</td>
                <td>¥{item['revenue']:,}</td>
                <td class="{growth_class}">{growth_icon_item} {item['growth']}%</td>
            </tr>
        """
    
    html += """
        </table>
        <div class="footer">
            此邮件由Python自动发送，请勿回复。如有问题请联系数据团队。
        </div>
    </body>
    </html>
    """
    
    return html

def send_report(sender_email, sender_password, recipient_emails, smtp_server='smtp.qq.com', smtp_port=587):
    """发送邮件报告
    
    Args:
        sender_email: 发件人邮箱
        sender_password: 邮箱授权码（不是登录密码！）
        recipient_emails: 收件人列表
        smtp_server: SMTP服务器地址
        smtp_port: SMTP端口
    """
    
    # 生成数据
    data = generate_sales_data()
    
    # 创建邮件
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipient_emails)
    msg['Subject'] = f'销售日报 - {datetime.now().strftime("%Y-%m-%d")}'
    
    # 添加HTML内容
    html_content = create_email_content(data)
    msg.attach(MIMEText(html_content, 'html', 'utf-8'))
    
    # 添加CSV附件
    csv_data = create_csv_attachment(data)
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(csv_data.encode('utf-8'))
    encoders.encode_base64(attachment)
    attachment.add_header(
        'Content-Disposition',
        f'attachment; filename="sales_report_{datetime.now().strftime("%Y%m%d")}.csv"'
    )
    msg.attach(attachment)
    
    # 发送邮件
    try:
        print(f"正在连接 {smtp_server}:{smtp_port}...")
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        server.starttls()  # 启用TLS加密
        
        print(f"正在登录 {sender_email}...")
        server.login(sender_email, sender_password)
        
        print(f"正在发送邮件给 {len(recipient_emails)} 个收件人...")
        server.send_message(msg)
        
        server.quit()
        print("✅ 邮件发送成功！")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("❌ 认证失败：请检查邮箱和授权码是否正确")
    except smtplib.SMTPConnectError:
        print("❌ 连接失败：请检查SMTP服务器地址和端口")
    except smtplib.SMTPRecipientsRefused:
        print("❌ 收件人被拒绝：请检查收件人邮箱地址")
    except Exception as e:
        print(f"❌ 发送失败: {type(e).__name__}: {e}")
    
    return False

# 使用示例
if __name__ == "__main__":
    # ⚠️ 请替换为你的真实邮箱信息
    # 推荐用环境变量，不要硬编码！
    SENDER_EMAIL = os.environ.get('MAIL_USER', "your_email@qq.com")
    SENDER_PASSWORD = os.environ.get('MAIL_PASS', "your_auth_code")
    RECIPIENTS = ["boss@company.com", "manager@company.com"]
    
    send_report(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENTS)
```

---

## 运行效果

**程序运行后：**

```
正在连接 smtp.qq.com:587...
正在登录 your_email@qq.com...
正在发送邮件给 2 个收件人...
✅ 邮件发送成功！
```

**收到的邮件（HTML格式）是这样子的：**

---

### 📧 邮件标题
```
主题：销售日报 - 2026-04-16
发件人：your_email@qq.com
收件人：boss@company.com, manager@company.com
```

### 📧 邮件正文

# 📊 每日销售报告

**日期: 2026年04月16日**

---

### 汇总数据

- **总销售额:** ¥35,000
- **总销量:** 550件
- **平均增长率:** 📈 13.4%

---

### 详细数据

| 产品 | 销量 | 销售额 | 同比增长 |
|-----|------|-------|---------|
| 产品A | 100 | ¥5,000 | 📈 3.1% |
| 产品B | 150 | ¥7,500 | 📈 8.3% |
| 产品C | 200 | ¥10,000 | 📈 13.5% |
| 产品D | 250 | ¥12,500 | 📈 18.7% |

---

*此邮件由Python自动发送，请勿回复。如有问题请联系数据团队。*

---

**📎 附件（sales_report_20260416.csv）：**

```csv
product,quantity,revenue,growth,date
产品A,100,5000,3.1,2026-04-16
产品B,150,7500,8.3,2026-04-16
产品C,200,10000,13.5,2026-04-16
产品D,250,12500,18.7,2026-04-16
```

---

## 常见邮箱的SMTP设置

| 邮箱 | SMTP服务器 | 端口 | 说明 |
|-----|-----------|------|------|
| QQ邮箱 | smtp.qq.com | 587 | 需要授权码 |
| Gmail | smtp.gmail.com | 587 | 需要应用专用密码 |
| 163邮箱 | smtp.163.com | 465 | 需要授权码 |
| Outlook | smtp.office365.com | 587 | 需要应用密码 |
| 新浪邮箱 | smtp.sina.com | 587 | 需要开启SMTP |

> ⚠️ **注意**：需要在邮箱设置里开启SMTP，并使用"授权码/应用专用密码"而不是登录密码。

---

## 代码关键点解析

### 1. SMTP发送流程

```
1. 连接SMTP服务器
   ↓
2. 开启TLS加密（starttls）
   ↓
3. 登录认证（login）
   ↓
4. 构建邮件（MIMEMultipart）
   ↓
5. 添加HTML正文 + 附件
   ↓
6. 发送（send_message）
   ↓
7. 退出连接（quit）
```

### 2. MIME邮件结构

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# 邮件容器
msg = MIMEMultipart()
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'
msg['Subject'] = '邮件标题'

# 添加HTML正文
html_part = MIMEText('<h1>Hello</h1>', 'html', 'utf-8')
msg.attach(html_part)

# 添加附件
file_part = MIMEBase('application', 'octet-stream')
file_part.set_payload(file_data)
encoders.encode_base64(file_part)
file_part.add_header('Content-Disposition', 'attachment; filename="report.csv"')
msg.attach(file_part)
```

### 3. 安全地使用密码

```python
import os

# ❌ 危险：硬编码密码
PASSWORD = "abcd1234"  # 别人看到代码就知道了！

# ✅ 正确：用环境变量
PASSWORD = os.environ.get('MAIL_PASS')

# ✅ 更好：用配置文件（不要提交到Git！）
import json
with open('config.json', 'r') as f:
    config = json.load(f)
PASSWORD = config['mail_password']
```

### 4. 多种错误处理

```python
try:
    server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
except smtplib.SMTPAuthenticationError:
    print("❌ 认证失败：请检查邮箱和授权码")
except smtplib.SMTPConnectError:
    print("❌ 连接失败：请检查SMTP服务器地址")
except smtplib.SMTPRecipientsRefused:
    print("❌ 收件人被拒绝")
except smtplib.SMTPDataError:
    print("❌ 邮件内容被拒绝")
except TimeoutError:
    print("❌ 连接超时：请检查网络")
except Exception as e:
    print(f"❌ 未知错误：{e}")
```

---

## 进阶功能

### 发送带图片的邮件（内嵌图片）

```python
from email.mime.image import MIMEImage

def send_email_with_image(sender, password, recipient):
    """发送内嵌图片的邮件"""
    msg = MIMEMultipart('related')  # related类型支持内嵌资源
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = '图表报告'
    
    # HTML正文（引用图片cid:chart）
    html = """
    <h2>销售趋势图</h2>
    <img src="cid:chart" alt="销售趋势图">
    """
    msg.attach(MIMEText(html, 'html', 'utf-8'))
    
    # 内嵌图片
    with open('sales_chart.png', 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-ID', '<chart>')  # 对应cid:chart
        msg.attach(img)
    
    # 发送...
    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()
```

### 发送给不同收件人不同的内容

```python
def send_personalized_report(sender, password, recipient_configs):
    """给不同收件人发送个性化报告"""
    for config in recipient_configs:
        email = config['email']
        departments = config['departments']
        
        # 只生成该收件人关心的部门数据
        data = [d for d in generate_sales_data() if d['department'] in departments]
        
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = email
        msg['Subject'] = f'部门日报 - {datetime.now().strftime("%Y-%m-%d")}'
        msg.attach(MIMEText(create_email_content(data), 'html', 'utf-8'))
        
        try:
            server = smtplib.SMTP('smtp.qq.com', 587)
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
            server.quit()
            print(f"✅ 已发送给 {email}")
        except Exception as e:
            print(f"❌ 发送给 {email} 失败：{e}")

# 配置
recipient_configs = [
    {'email': 'sales_boss@company.com', 'departments': ['销售部', '市场部']},
    {'email': 'tech_boss@company.com', 'departments': ['技术部', '产品部']},
]
```

### 邮件发送日志

```python
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(
    filename='mail_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def send_report_with_logging(sender, password, recipients):
    """带日志记录的邮件发送"""
    try:
        result = send_report(sender, password, recipients)
        if result:
            logging.info(f"邮件发送成功：{recipients}")
        else:
            logging.warning(f"邮件发送失败：{recipients}")
        return result
    except Exception as e:
        logging.error(f"邮件发送异常：{e}")
        return False
```

---

## 避坑指南

### 1. QQ邮箱端口问题

```python
# QQ邮箱有时587端口连不上，试试465（SSL）
# 方式1：587 + starttls
server = smtplib.SMTP('smtp.qq.com', 587)
server.starttls()

# 方式2：465直接SSL
server = smtplib.SMTP_SSL('smtp.qq.com', 465)
```

### 2. 中文附件名乱码

```python
from email.header import Header

# ❌ 错误：中文文件名直接写
attachment.add_header('Content-Disposition', 'attachment; filename="销售报告.csv"')

# ✅ 正确：用Header编码
filename = Header('销售报告.csv', 'utf-8').encode()
attachment.add_header('Content-Disposition', 'attachment', filename=filename)
```

### 3. 邮件被识别为垃圾邮件

```python
# 避免被识别为垃圾邮件的技巧：
# 1. 使用HTML格式（比纯文本通过率高）
# 2. 邮件标题不要用太多感叹号和促销词
# 3. 添加纯文本备选（multipart/alternative）
# 4. 控制发送频率，不要1分钟发100封

# 添加纯文本备选
msg = MIMEMultipart('alternative')
msg.attach(MIMEText('纯文本版本', 'plain', 'utf-8'))
msg.attach(MIMEText('<h1>HTML版本</h1>', 'html', 'utf-8'))
```

### 4. 授权码过期

```python
# 授权码可能过期，需要处理这种情况
try:
    server.login(sender_email, sender_password)
except smtplib.SMTPAuthenticationError:
    print("❌ 授权码可能已过期，请重新获取")
    print("QQ邮箱：设置 → 账户 → 生成授权码")
```

---

## 进阶：定时自动发送

```python
import schedule
import time
import logging

logging.basicConfig(level=logging.INFO)

def job():
    """定时任务"""
    logging.info(f"开始执行定时邮件任务 - {datetime.now()}")
    result = send_report(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENTS)
    if result:
        logging.info("邮件发送成功")
    else:
        logging.error("邮件发送失败")

# 每天早上9点自动发送
schedule.every().day.at("09:00").do(job)

# 工作日发送（周一到周五）
# schedule.every().monday.at("09:00").do(job)
# schedule.every().tuesday.at("09:00").do(job)
# ... 或者自己判断

print("🤖 邮件自动发送服务已启动")
print(f"⏰ 每天早上 09:00 自动发送报告")

while True:
    schedule.run_pending()
    time.sleep(60)  # 每分钟检查一次
```

### 工作日判断版本

```python
import schedule
from datetime import datetime

def weekday_job():
    """只在工作日执行"""
    today = datetime.now()
    # 0=周一, 4=周五, 5=周六, 6=周日
    if today.weekday() <= 4:
        send_report(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENTS)
    else:
        print(f"今天是周末，跳过发送")

# 每天9点检查
schedule.every().day.at("09:00").do(weekday_job)
```

---


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


## 本讲小结

用到的知识：

| 知识 | 用途 |
|-----|------|
| `smtplib` | SMTP协议发送邮件 |
| `email.mime` | 构造HTML邮件和附件 |
| `csv` | 生成CSV文件 |
| `datetime` | 获取当前日期 |
| `os.environ` | 安全获取环境变量 |
| `schedule` | 定时任务调度 |
| `logging` | 日志记录 |

---

## 下节预告

第三个实战项目是**天气查询机器人**——查天气、做提醒，特别实用！

👉 **[继续阅读：Python实战项目-天气查询机器人](./22-Python实战项目-天气查询机器人.md)**

---

## 课程导航

**上一篇：** [Python实战项目-自动整理下载文件夹](./20-Python实战项目-自动整理下载文件夹.md)

**下一篇：** [Python实战项目-天气查询机器人](./22-Python实战项目-天气查询机器人.md)

---

*PS：邮件自动化是办公提效的神器。学会这个，每天省下半小时！*
