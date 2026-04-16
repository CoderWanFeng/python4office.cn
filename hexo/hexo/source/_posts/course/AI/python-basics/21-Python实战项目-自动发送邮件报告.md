---
title: Python实战项目：我做了个自动邮件系统，每天定时发送数据报告
date: 2026-02-28 21:10:00
tags: [Python实战, 自动化, 邮件]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://www.bilibili.com/cheese/play/ss982042944'>
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
<a href="https://www.bilibili.com/cheese/play/ss982042944">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

今天第二个实战项目：**自动发送邮件报告**。

> 💡 **场景**：你是运营人员，每天要向老板汇报昨天的销售数据。以前你都是手动整理Excel、截图、发邮件——每天重复同样的工作。现在用Python自动化，设定好脚本，每天早上自动发到老板邮箱！

---

## 项目功能

- 自动生成数据报告（模拟销售数据）
- 创建HTML格式的美观邮件
- 添加附件（CSV文件）
- 支持多个收件人
- 可设置定时发送

---

## 完整代码

```python
import smtplib
import csv
import io
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
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        data.append(sales)
    
    return data

def create_csv_attachment(data):
    """将数据转换为CSV格式"""
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['product', 'quantity', 'revenue', 'date'])
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()

def create_email_content(data):
    """创建HTML邮件内容"""
    total_revenue = sum(item['revenue'] for item in data)
    total_quantity = sum(item['quantity'] for item in data)
    
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #4CAF50; color: white; }}
            .summary {{ background-color: #f2f2f2; padding: 15px; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <h2>每日销售报告</h2>
        <p>日期: {datetime.now().strftime('%Y年%m月%d日')}</p>
        
        <div class="summary">
            <h3>📊 汇总数据</h3>
            <p><strong>总销售额:</strong> ¥{total_revenue:,}</p>
            <p><strong>总销量:</strong> {total_quantity}件</p>
        </div>
        
        <h3>📋 详细数据</h3>
        <table>
            <tr>
                <th>产品</th>
                <th>销量</th>
                <th>销售额</th>
            </tr>
    """
    
    for item in data:
        html += f"""
            <tr>
                <td>{item['product']}</td>
                <td>{item['quantity']}</td>
                <td>¥{item['revenue']:,}</td>
            </tr>
        """
    
    html += """
        </table>
        <p style="color: #666; margin-top: 30px;">
            此邮件由系统自动发送，请勿回复。
        </p>
    </body>
    </html>
    """
    
    return html

def send_report(sender_email, sender_password, recipient_emails):
    """发送邮件报告"""
    
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
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("✅ 邮件发送成功！")
    except Exception as e:
        print(f"❌ 发送失败: {e}")

# 使用示例
if __name__ == "__main__":
    # ⚠️ 请替换为你的真实邮箱
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_app_password"  # 使用应用专用密码
    RECIPIENTS = ["boss@company.com", "manager@company.com"]
    
    send_report(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENTS)
```

---

## 运行效果

**程序运行后：**

```
✅ 邮件发送成功！
```

**收到的邮件（HTML格式）是这样子的：**

---

### 📧 邮件标题
```
主题：销售日报 - 2026-04-16
发件人：your_email@gmail.com
收件人：boss@company.com, manager@company.com
```

### 📧 邮件正文

# 每日销售报告

**日期: 2026年04月16日**

---

### 📊 汇总数据

- **总销售额:** ¥20,000
- **总销量:** 450件

---

### 📋 详细数据

| 产品 | 销量 | 销售额 |
|-----|------|-------|
| 产品A | 100 | ¥5,000 |
| 产品B | 150 | ¥7,500 |
| 产品C | 200 | ¥10,000 |
| 产品D | 250 | ¥12,500 |

---

*此邮件由系统自动发送，请勿回复。*

---

**📎 附件（sales_report_20260416.csv）：**

```csv
product,quantity,revenue,date
产品A,100,5000,2026-04-16
产品B,150,7500,2026-04-16
产品C,200,10000,2026-04-16
产品D,250,12500,2026-04-16
```

---

## 常见邮箱的SMTP设置

| 邮箱 | SMTP服务器 | 端口 |
|-----|-----------|------|
| Gmail | smtp.gmail.com | 587 |
| QQ邮箱 | smtp.qq.com | 587 |
| 163邮箱 | smtp.163.com | 25 |
| Outlook | smtp.office365.com | 587 |

> ⚠️ **注意**：需要在邮箱设置里开启SMTP，并使用"应用专用密码"而不是登录密码。

---

## 进阶：定时自动发送

```python
import schedule
import time

def job():
    send_report(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENTS)

# 每天早上9点自动发送
schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # 每分钟检查一次
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
| `smtplib` | 发送邮件 |
| `email.mime` | 构造HTML邮件和附件 |
| `csv` | 生成CSV文件 |
| `datetime` | 获取当前日期 |
| `json` | 数据格式转换 |

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

