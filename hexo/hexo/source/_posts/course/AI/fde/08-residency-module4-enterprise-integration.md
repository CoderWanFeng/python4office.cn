---
title: 模块 4 · 企业系统集成（第 8 周）
date: 2026-10-14 10:00:00
tags: [FDE, Residency, 企业集成, Webhook, SSO, 数据合规]
categories: [AI 课程, FDE 实战课]
cover: https://images.unsplash.com/photo-1551434678-e076c223a692?q=80&w=1200&auto=format&fit=crop
---


<p align="center" id='FDE-读者群-banner'>
    <a target="_blank" href='https://python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%" alt="加入AI学习交流群，第一时间获取FDE课程更新"/>
    </a>   
</p>


![模块 4 · 企业系统集成](https://images.unsplash.com/photo-1551434678-e076c223a692?w=800&h=400&fit=crop)


# 模块 4 · 企业系统集成（第 8 周）

> **💡 一句话总结**：把模块 3 跑通的 LLM 系统，接到客户的 OA / CRM / 飞书 / 企微 / SSO 里——AI 才能真正被业务方"用起来"。

---

## 🎯 本模块三大特点

> **📚 系统**：模块 4 在 12 周 Residency 中的定位是 **最后一公里**——技术再好，接不进客户系统也白搭
>
> **🔧 实战**：1 周内跑通端到端集成（客户系统 → AI 服务 → 客户系统）
>
> **⚡ 不啰嗦**：直接给 3 种对接模式的最小代码

---

## 📖 学习导航

| 上一模块 | 本模块位置 | 下一模块 |
|---|---|---|
| [模块 3 · LLM 生产化工程](./07-residency-module3-llm-engineering) | **模块 4 / 共 8 模块（第 8 周）** | [模块 5 · 私有化部署](./09-residency-module5-private-deployment) |

---

## 📅 一周时间表

| 时间 | 任务 | 产出 |
|---|---|---|
| **Day 1-2** | 选对接模式（Webhook / 中间表 / iPaaS） | 1 份对接方案 |
| **Day 3-4** | 实现端到端集成 | 跑通的集成链路 |
| **Day 5** | 接入 SSO / SAML + RBAC | 权限集成完成 |

---

## 🚀 直接开始：3 个核心实战任务

### 任务 1：选对接模式（Webhook vs 中间表 vs iPaaS）

**目标**：根据客户已有系统，选最合适的一种
**难度**：⭐⭐
**时间**：半天

**3 种对接模式对比：**

| 模式 | 适用场景 | 优点 | 缺点 |
|---|---|---|---|
| **Webhook** | 客户系统支持事件触发 | 实时、简单 | 客户系统需支持 |
| **中间表** | 客户有共享数据库 | 稳定、易调试 | 需建表 / 同步机制 |
| **iPaaS**（n8n / Airflow） | 复杂多系统 | 可视化、易维护 | 引入第三方依赖 |

**决策树：**

```
客户系统支持 webhook？
├─ 是 → 用 Webhook
└─ 否 → 客户有共享 DB？
         ├─ 是 → 用中间表
         └─ 否 → 用 iPaaS（n8n 最常用）
```

---

### 任务 2：用 Webhook 把 AI 接入飞书 / 企微

**难度**：⭐⭐⭐
**时间**：2 天

#### 示例：把 AI Agent 接入飞书机器人

```python
# 1. 创建飞书应用，拿到 App ID / App Secret
import requests
import json

FEISHU_APP_ID = "cli_xxx"
FEISHU_APP_SECRET = "xxx"

# 2. 启动 Web 服务，接收飞书消息
from fastapi import FastAPI, Request
app = FastAPI()

@app.post("/feishu/webhook")
async def feishu_webhook(req: Request):
    data = await req.json()

    # 解析飞书消息
    user_message = data["event"]["text"]
    user_id = data["event"]["sender"]["sender_id"]["open_id"]

    # 调 AI Agent
    response = run_agent(user_message, user_role="employee")

    # 调飞书 API 回复
    send_feishu_message(user_id, response)

    return {"code": 0}


def send_feishu_message(user_id, text):
    # 1. 拿 access_token
    token_resp = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": FEISHU_APP_ID, "app_secret": FEISHU_APP_SECRET},
    )
    access_token = token_resp.json()["tenant_access_token"]

    # 2. 发消息
    requests.post(
        "https://open.feishu.cn/open-apis/im/v1/messages",
        params={"receive_id_type": "open_id"},
        headers={"Authorization": f"Bearer {access_token}"},
        json={
            "receive_id": user_id,
            "msg_type": "text",
            "content": json.dumps({"text": text}),
        },
    )
```

**端到端集成流程：**

```
用户在飞书发消息
  ↓
飞书 Webhook → 你的 API
  ↓
AI Agent 处理
  ↓
调飞书 API 回复
  ↓
用户在飞书看到回复
```

---

### 任务 3：处理"数据不能出域"的合规要求

**难度**：⭐⭐⭐
**时间**：1 天

**典型 3 种处理方案：**

| 方案 | 实现 | 适用 |
|---|---|---|
| **VPC 专属部署** | 模型在客户 VPC 内，API 在内网调用 | 中等合规 |
| **完全私有化** | 模型 + 数据 + 应用全在客户机房 | 强合规 |
| **混合方案** | 敏感数据本地处理，非敏感走 API | 折中 |

**FDE 实战建议**：跟客户合规部门对齐后，在 ADR 里写清楚数据流向图。

---

## 📚 系统学习：核心概念

### 概念 1：3 种对接模式的本质

**为什么重要**：90% 的 FDE 项目卡在集成环节，选错模式 = 工期翻倍。

- **Webhook**：客户系统发起，你是被动响应
- **中间表**：双方读写同一张表，需要约定 schema
- **iPaaS**：可视化编排，适合 IT 部门主导的项目

---

### 概念 2：SSO / SAML / OAuth 在 AI 系统里的实现

**一句话解释**：让员工用公司账号登录 AI 系统，不用单独注册。

**典型实现（用 Auth0 / Keycloak）：**

```python
# Keycloak 集成示例
from fastapi import FastAPI, Depends, Header
from keycloak import KeycloakOpenID

keycloak = KeycloakOpenID(
    server_url="https://keycloak客户地址/auth",
    client_id="ai-assistant",
    realm_name="客户域名",
)

async def verify_token(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    userinfo = keycloak.decode_token(token)
    return userinfo

@app.get("/api/chat")
async def chat(query: str, user=Depends(verify_token)):
    role = user["realm_access"]["roles"][0]
    return run_agent(query, user_role=role)
```

---

### 概念 3：客户私有环境的 4 个常见约束

**FDE 派驻前必问客户的 4 个问题：**
1. 数据能出域吗？（决定 API / 私有化）
2. 网络有防火墙 / 代理吗？（决定能否调外部服务）
3. 证书是自签还是 CA？（决定 HTTPS 配置）
4. 有合规扫描要求吗？（决定是否能直接用某个镜像）

---

## ⚡ 避坑指南：常见错误

| 错误类型 | 错误做法 | 正确做法 | 为什么 |
|---|---|---|---|
| 集成方案没评审 | 直接动手做 | 先和客户 IT 评审方案 | IT 一句话"这个不行" = 重做 |
| 没做幂等 | Webhook 重复触发 → 重复扣款 | 加重试 + 幂等键 | Webhook 一定会有重复 |
| Token 硬编码 | "access_token 写在代码里" | 走 OAuth 自动刷新 | 硬编码 Token 过期 = 全系统挂 |
| 没 RBAC | 所有用户都能调所有工具 | 按角色限制 | 没权限 = 合规事故 |
| 跨域没处理 | 浏览器调 API 报 CORS 错误 | 服务端配 CORS 头 | 前端联调时 90% 会卡这里 |

---

## 🎯 模块 4 总结

### 你学到了什么
- ✅ 3 种对接模式（Webhook / 中间表 / iPaaS）的选择方法
- ✅ 把 AI Agent 接入飞书 / 企微的完整代码
- ✅ 数据合规的 3 种处理方案
- ✅ SSO / SAML 集成与 RBAC 权限设计

### 模块交付物 Checklist
- [ ] 1 份对接方案文档（与客户 IT 评审通过）
- [ ] 端到端集成跑通（飞书 / 企微 demo）
- [ ] SSO / RBAC 接入完成
- [ ] 数据流向图（在 ADR 里更新）

### 下一步行动
1. [ ] 进入 [模块 5 · 私有化部署（第 9 周）](./09-residency-module5-private-deployment)
2. [ ] 把整套服务打包 Docker
3. [ ] 准备客户的 K8s 部署

---

## ➡️ 下模块预告

**模块 5 · 私有化部署与基础设施（第 9 周）**
- 你将学到：Docker / Compose / K8s / Helm + 国产化
- 实战任务：把模块 3-4 的系统部署到客户测试环境

👉 [继续阅读模块 5](./09-residency-module5-private-deployment)

---

---

## 📞 联系作者

| 联系方式 | 入口 |
|---|---|
| 📱 微信 | `aiwf365`（扫码加好友，备注"FDE"） |
| 💬 **AI 学习交流群** | [点我扫码加入 →](https://python4office.cn/wechat-group/) |
| 🌐 个人网站 | https://python4office.cn/ |

<p align="center">
  <img src="https://raw.githubusercontent.com/CoderWanFeng/img-cdn/master/wx-aifw365.png" width="200" alt="程序员晚枫微信二维码"/>
</p>

> 加入 AI 编程交流群，第一时间获取 FDE 课程更新 + AI 落地实战案例。

*💡 记住：集成做完，才能真正说"AI 接进了客户业务"——前面再多技术亮点，这一周没交付都不算。*