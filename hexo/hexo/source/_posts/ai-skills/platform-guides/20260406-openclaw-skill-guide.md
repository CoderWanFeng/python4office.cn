---
title: OpenClaw Skill 安装与管理指南：1700+技能等你探索
date: 2026-04-06 10:32:00
tags: [OpenClaw, Skill, AI办公, 教程, ClawHub]
categories: [AI Skills, 平台攻略]
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

<p align="center">
    <a target="_blank" href='https://github.com/claw-ai/openclaw'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
    </a>
</p>

<!-- more -->

大家好，我是正在实战各种 AI 项目的程序员晚枫。

如果你追求更强大的 AI 自动化能力，**OpenClaw** 是目前最值得关注的开源 AI Agent 框架。截至 2026 年 3 月，其官方技能市场 **ClawHub** 已收录 **1700+ Skills**，覆盖开发、办公、创作全场景。

今天这篇指南，带你全面掌握 OpenClaw Skill 的安装与管理。

---

## 一、OpenClaw 简介

### 什么是 OpenClaw？
OpenClaw（原 Clawdbot）是一个**开源免费的 AI 执行引擎**，特点：
- ✅ 本地部署，数据安全
- ✅ 支持多平台接入（微信、钉钉、飞书、Telegram 等）
- ✅ 强大的 Skill 生态（1700+）
- ✅ 支持浏览器自动化

### 适合谁用？
| 人群 | 推荐理由 |
|---|---|
| 技术爱好者 | 开源免费，可深度定制 |
| 隐私敏感用户 | 本地部署，数据不上云 |
| 企业用户 | 可私有化部署，对接内部系统 |
| 开发者 | 可开发自定义 Skill |

---

## 二、安装 OpenClaw

### 环境要求
- Python 3.8+
- Node.js 16+
- Git

### 安装步骤

**步骤 1：克隆仓库**
```bash
git clone https://github.com/claw-ai/openclaw.git
cd openclaw
```

**步骤 2：安装依赖**
```bash
pip install -r requirements.txt
npm install
```

**步骤 3：配置环境变量**
```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 API Key
```

**步骤 4：启动服务**
```bash
python main.py
```

---

## 三、Skill 安装与管理

### 查看已安装 Skills
```bash
openclaw skills list
```

输出示例：
```
已安装 Skills (5):
  1. excel-tools     v1.2.0    Excel 处理工具集
  2. pdf-utils       v2.1.0    PDF 操作工具
  3. file-manager    v1.0.5    文件管理
  4. ocr-tools       v1.3.0    OCR 文字识别
  5. web-search      v2.0.0    网络搜索
```

### 从 ClawHub 安装 Skill

**搜索 Skill**
```bash
openclaw skills search excel
```

**安装 Skill**
```bash
openclaw skills install excel-tools
```

**指定版本安装**
```bash
openclaw skills install excel-tools@1.2.0
```

### 从 GitHub 安装 Skill
```bash
openclaw skills install https://github.com/user/excel-tools
```

### 从本地安装 Skill
```bash
openclaw skills install ./my-skill.tar.gz
```

### 更新 Skill
```bash
openclaw skills update excel-tools
```

### 卸载 Skill
```bash
openclaw skills uninstall excel-tools
```

---

## 四、必装的 15 个办公 Skills

根据我的实测，以下 Skills 办公场景最实用：

### 📊 Excel 处理
| Skill | 功能 | 安装命令 |
|---|---|---|
| excel-tools | Excel 读写、合并、拆分 | `openclaw skills install excel-tools` |
| excel-chart | Excel 图表生成 | `openclaw skills install excel-chart` |
| excel-pivot | 数据透视表 | `openclaw skills install excel-pivot` |

### 📑 PDF 处理
| Skill | 功能 | 安装命令 |
|---|---|---|
| pdf-utils | PDF 合并、拆分、旋转 | `openclaw skills install pdf-utils` |
| pdf-watermark | PDF 加水印 | `openclaw skills install pdf-watermark` |
| pdf-ocr | PDF 文字识别 | `openclaw skills install pdf-ocr` |

### 📄 文档处理
| Skill | 功能 | 安装命令 |
|---|---|---|
| docx-tools | Word 文档处理 | `openclaw skills install docx-tools` |
| pptx-tools | PPT 处理 | `openclaw skills install pptx-tools` |
| markdown-tools | Markdown 转换 | `openclaw skills install markdown-tools` |

### 🖼 图片处理
| Skill | 功能 | 安装命令 |
|---|---|---|
| image-tools | 图片格式转换 | `openclaw skills install image-tools` |
| image-watermark | 图片加水印 | `openclaw skills install image-watermark` |
| image-ocr | 图片文字识别 | `openclaw skills install image-ocr` |

### 🤖 自动化
| Skill | 功能 | 安装命令 |
|---|---|---|
| file-manager | 文件批量管理 | `openclaw skills install file-manager` |
| email-tools | 邮件自动化 | `openclaw skills install email-tools` |
| calendar-tools | 日历管理 | `openclaw skills install calendar-tools` |

### 🔧 系统工具
| Skill | 功能 | 安装命令 |
|---|---|---|
| web-search | 网络搜索 | `openclaw skills install web-search` |
| system-info | 系统信息获取 | `openclaw skills install system-info` |

---

## 五、Skill 配置

### 全局配置
编辑 `~/.openclaw/config.json`：
```json
{
  "skills": {
    "enabled": ["excel-tools", "pdf-utils", "file-manager"],
    "directory": "~/.openclaw/skills",
    "auto_update": true
  }
}
```

### Skill 单独配置
每个 Skill 可能有独立配置，位于：
```
~/.openclaw/skills/{skill-name}/config.json
```

例如配置 excel-tools：
```json
{
  "default_encoding": "utf-8",
  "max_file_size": "100MB",
  "temp_directory": "~/.openclaw/temp"
}
```

---

## 六、使用 Skills

### 命令行使用
```bash
openclaw run "合并这些 Excel 文件" --files data/*.xlsx
```

### 对话中使用
```
你：帮我把 /data/ 目录下的所有 Excel 合并成一个文件

AI：我来帮你合并 Excel 文件。
🔧 Using skill: excel-tools
   action: merge
   files: 5个文件
   
📤 Result:
   已合并为: /data/merged.xlsx
   总行数: 15,234
   耗时: 2.3秒
```

---

## 七、Skill 开发入门

如果你想开发自己的 Skill：

**创建 Skill 目录**
```bash
mkdir -p ~/.openclaw/skills/my-skill
cd ~/.openclaw/skills/my-skill
```

**编写 SKILL.md**
```markdown
# My Skill

## 描述
我的第一个 OpenClaw Skill

## 工具
### my_tool
参数：
- input (string): 输入内容

返回：
- output (string): 处理结果
```

**实现工具**
创建 `tools/my_tool.py`：
```python
def my_tool(input: str) -> str:
    return f"处理结果: {input}"
```

**注册 Skill**
创建 `index.py`：
```python
from tools.my_tool import my_tool

SKILL = {
    "name": "my-skill",
    "version": "1.0.0",
    "tools": {
        "my_tool": my_tool
    }
}
```

---

## 八、常见问题

### Q1：Skill 安装失败怎么办？
- 检查网络连接
- 确认 Python/Node.js 版本
- 查看错误日志：`openclaw logs`

### Q2：如何查看 Skill 文档？
```bash
openclaw skills docs excel-tools
```

### Q3：Skill 冲突怎么办？
如果两个 Skill 功能重复，可以在配置中禁用：
```json
{
  "skills": {
    "disabled": ["old-excel-tools"]
  }
}
```

### Q4：如何贡献 Skill 到 ClawHub？
1. 在 GitHub 发布你的 Skill
2. 提交 PR 到 ClawHub 仓库
3. 等待审核通过

---

## 九、相关资源

- **OpenClaw 官网**：https://openclaw.ai
- **ClawHub 市场**：https://hub.openclaw.ai
- **GitHub 仓库**：https://github.com/claw-ai/openclaw
- **开发文档**：https://docs.openclaw.ai

---

## 十、下一步学习

- [《从零开发你的第一个办公 Skill》](/ai-skills/skill-dev/first-skill/)
- [《Coze 扣子 Skill 商店全攻略》](/ai-skills/platform-guides/coze-skill-guide/)
- [《飞书 CLI 办公 Skill 快速上手》](/ai-skills/platform-guides/feishu-cli-guide/)

---

## 💬 加入交流群

OpenClaw 使用问题？加群交流：

👉 **[加入AI编程学习交流群](https://www.python4office.cn/wechat-group/)**

![点击加入](https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png)

---

*OpenClaw 的强大之处在于其开放的 Skill 生态。1700+ Skills 等你来探索！*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


