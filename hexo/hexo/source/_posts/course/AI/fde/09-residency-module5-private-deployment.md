---
title: 模块 5 · 私有化部署与基础设施（第 9 周）
date: 2026-10-14 10:00:00
tags: [FDE, Residency, 私有化部署, Docker, K8s, 国产化]
categories: [AI 课程, FDE 实战课]
cover: https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=1200&auto=format&fit=crop
---


<p align="center" id='FDE-读者群-banner'>
    <a target="_blank" href='https://python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%" alt="加入AI学习交流群，第一时间获取FDE课程更新"/>
    </a>   
</p>


![模块 5 · 私有化部署与基础设施](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&h=400&fit=crop)


# 模块 5 · 私有化部署与基础设施（第 9 周）

> **💡 一句话总结**：把模块 3-4 的整套服务，部署到客户机房 / 私有云 / 测试环境——并能扛住国产化适配和离线场景。

---

## 🎯 本模块三大特点

> **📚 系统**：模块 5 在 12 周 Residency 中的定位是 **最后一公里交付**——之前都在你电脑上跑，这周开始跑客户环境
>
> **🔧 实战**：1 周内交付 1 套 Docker Compose 一键起 + 1 个 Helm Chart
>
> **⚡ 不啰嗦**：跳过 K8s 原理，直接给可用的部署脚本

---

## 📖 学习导航

| 上一模块 | 本模块位置 | 下一模块 |
|---|---|---|
| [模块 4 · 企业系统集成](./08-residency-module4-enterprise-integration) | **模块 5 / 共 8 模块（第 9 周）** | [模块 7 · 安全审查与合规](./10-residency-module7-security-compliance) |

---

## 📅 一周时间表

| 时间 | 任务 | 产出 |
|---|---|---|
| **Day 1-2** | Docker Compose 编排整套服务 | 1 个 docker-compose.yml |
| **Day 3-4** | K8s + Helm 打包 | 1 套 Helm Chart |
| **Day 5** | 国产化 / 离线场景适配 | 1 份部署手册 |

---

## 🚀 直接开始：3 个核心实战任务

### 任务 1：Docker Compose 一键起整套服务

**目标**：1 个 docker-compose.yml，启动 AI 服务 + 向量库 + 前端 + 数据库
**难度**：⭐⭐⭐
**时间**：2 天

```yaml
# docker-compose.yml
version: '3.8'

services:
  # AI 后端服务
  ai-service:
    build: ./ai-service
    ports:
      - "8000:8000"
    environment:
      - LLM_API_KEY=${LLM_API_KEY}
      - LLM_BASE_URL=${LLM_BASE_URL}
      - VECTOR_DB_URL=http://milvus:19530
    depends_on:
      - milvus
      - postgres
    restart: unless-stopped

  # 前端
  web:
    build: ./web
    ports:
      - "3000:3000"
    environment:
      - API_URL=http://ai-service:8000
    depends_on:
      - ai-service
    restart: unless-stopped

  # 向量数据库 Milvus
  milvus:
    image: milvusdb/milvus:v2.3.3
    ports:
      - "19530:19530"
      - "9091:9091"
    volumes:
      - milvus_data:/var/lib/milvus
    environment:
      - ETCD_ENDPOINTS=etcd:2379
      - MINIO_ADDRESS=minio:9000
    depends_on:
      - etcd
      - minio

  # 对象存储 MinIO
  minio:
    image: minio/minio:latest
    command: server /data --console-address ":9001"
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      - MINIO_ACCESS_KEY=minio
      - MINIO_SECRET_KEY=minio123
    volumes:
      - minio_data:/data

  # 元数据 etcd
  etcd:
    image: quay.io/coreos/etcd:v3.5.5
    command: etcd -advertise-client-urls=http://etcd:2379 -listen-client-urls http://0.0.0.0:2379 --data-dir /etcd-data
    volumes:
      - etcd_data:/etcd-data

  # 业务数据库
  postgres:
    image: postgres:15
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_DB=ai_assistant
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=admin123
    volumes:
      - postgres_data:/var/lib/postgresql/data

  # 监控
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin

volumes:
  milvus_data:
  minio_data:
  etcd_data:
  postgres_data:
```

**一键启动：**

```bash
# 启动
docker-compose up -d

# 查看状态
docker-compose ps

# 查看日志
docker-compose logs -f ai-service
```

---

### 任务 2：写 1 个 Helm Chart

**目标**：把 docker-compose 升级成 K8s 可部署的 Helm Chart
**难度**：⭐⭐⭐⭐
**时间**：2 天

**目录结构：**

```
helm/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── ai-service-deployment.yaml
    ├── ai-service-service.yaml
    ├── web-deployment.yaml
    ├── web-service.yaml
    ├── postgres-deployment.yaml
    ├── postgres-service.yaml
    ├── configmap.yaml
    └── secret.yaml
```

**示例：ai-service-deployment.yaml**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .Values.aiService.name }}
spec:
  replicas: {{ .Values.aiService.replicas }}
  selector:
    matchLabels:
      app: {{ .Values.aiService.name }}
  template:
    metadata:
      labels:
        app: {{ .Values.aiService.name }}
    spec:
      containers:
      - name: ai-service
        image: {{ .Values.aiService.image }}
        ports:
        - containerPort: 8000
        env:
        - name: LLM_API_KEY
          valueFrom:
            secretKeyRef:
              name: ai-secrets
              key: llm-api-key
        - name: VECTOR_DB_URL
          value: {{ .Values.vectorDb.url }}
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "2000m"
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 60
          periodSeconds: 30
```

**部署命令：**

```bash
# 安装
helm install ai-assistant ./helm -n ai-system --create-namespace

# 升级
helm upgrade ai-assistant ./helm -n ai-system

# 卸载
helm uninstall ai-assistant -n ai-system
```

---

### 任务 3：处理国产化 / 离线场景

**目标**：在昇腾 / 海光 / 麒麟环境完成部署
**难度**：⭐⭐⭐⭐
**时间**：1 天

**典型国产化适配 3 个坑：**

| 坑 | 说明 | 解决方案 |
|---|---|---|
| **CPU 架构** | x86 vs ARM vs 国产 CPU | Docker buildx 多架构构建 |
| **GPU / NPU** | CUDA vs 昇腾 CANN vs 海光 DCU | 用对应推理框架（vLLM-Ascend） |
| **操作系统** | CentOS vs 麒麟 vs UOS | 基础镜像用对应的 |

**离线场景镜像分发脚本：**

```bash
# 1. 在有网络的机器导出镜像
docker save -o ai-service.tar ai-service:latest
docker save -o milvus.tar milvusdb/milvus:v2.3.3
docker save -o postgres.tar postgres:15
# ...

# 2. 拷贝到客户内网
scp ai-service.tar user@客户内网:/images/

# 3. 在客户内网加载
ssh user@客户内网
docker load -i /images/ai-service.tar
docker load -i /images/milvus.tar
docker load -i /images/postgres.tar

# 4. 启动
docker-compose up -d
```

**模型权重离线分发：**

```bash
# 1. 打包模型权重（外网）
tar -czf qwen3-72b.tar.gz ~/.cache/huggingface/Qwen/Qwen3-72B-Instruct/

# 2. 传到客户内网
scp qwen3-72b.tar.gz user@客户内网:/models/

# 3. 内网部署
ssh user@客户内网
tar -xzf /models/qwen3-72b.tar.gz -C /opt/models/
```

---

## 📚 系统学习：核心概念

### 概念 1：私有化部署的 3 个层次

**为什么重要**：FDE 经常被问到"我们的 AI 系统部署在哪一层？"

| 层次 | 部署位置 | 适用 |
|---|---|---|
| **应用层** | 只部署 AI 应用，模型调 API | 中等合规 |
| **模型层** | 模型 + 应用都在客户机房 | 强合规 |
| **数据层** | 模型 + 应用 + 业务数据都在客户机房 | 最高合规 |

---

### 概念 2：Docker vs K8s vs Helm 三者关系

- **Docker**：单个容器打包
- **K8s**：多容器编排（Pod / Service / Deployment）
- **Helm**：K8s 的包管理工具（Chart = 模板 + values）

**FDE 实战建议：**
- POC 阶段用 docker-compose 就够
- 客户生产环境必须用 K8s + Helm
- 离线场景用 docker save/load 镜像分发

---

### 概念 3：国产化适配的"4 个对齐"

1. **架构对齐**：x86 → ARM / 国产 CPU
2. **算力对齐**：CUDA → 昇腾 CANN / 海光 DCU / 寒武纪 MLU
3. **OS 对齐**：CentOS → 麒麟 / UOS / 中标麒麟
4. **数据库对齐**：MySQL → 达梦 / 人大金仓 / 神通

---

## ⚡ 避坑指南：常见错误

| 错误类型 | 错误做法 | 正确做法 | 为什么 |
|---|---|---|---|
| docker-compose 直接上生产 | 没 K8s，单机挂了就挂了 | 生产用 K8s 多副本 | 高可用是基础要求 |
| 镜像没做版本管理 | "用 latest 就行" | 明确打 tag | latest 升级 = 线上事故 |
| 密钥硬编码 | API Key 写在代码里 | 用 K8s Secret | 硬编码 = 泄露 |
| 没做健康检查 | 服务挂了 K8s 不知道 | readinessProbe + livenessProbe | 没健康检查 = 用户先发现 |
| 国产化直接试错 | "应该能跑" | 提前确认客户硬件 / OS | 到现场才发现不兼容 = 工期翻倍 |

---

## 🎯 模块 5 总结

### 你学到了什么
- ✅ Docker Compose 编排整套 AI 服务（8 个组件）
- ✅ Helm Chart 的目录结构与 K8s 部署
- ✅ 国产化适配的 4 个对齐
- ✅ 离线场景的镜像 + 模型分发脚本

### 模块交付物 Checklist
- [ ] 1 个 docker-compose.yml（8+ 服务编排）
- [ ] 1 套 Helm Chart（部署到客户测试 K8s）
- [ ] 1 份《国产化适配清单》
- [ ] 1 份《离线部署手册》

### 下一步行动
1. [ ] 进入 [模块 7 · 安全审查与合规（第 10 周）](./10-residency-module7-security-compliance)
2. [ ] 给整套服务补安全审查
3. [ ] 输出 1 份《安全审查报告 v1.0》

---

## ➡️ 下模块预告

**模块 7 · 安全审查与合规闭环（第 10 周，贯穿全程）**
- 你将学到：提示词注入防护、数据脱敏、Guardrails、红队测试
- 实战任务：1 份《安全审查报告 v1.0》+ 1 次红队测试记录

👉 [继续阅读模块 7](./10-residency-module7-security-compliance)

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

*💡 记住：私有化部署不是"把代码拷过去"，是"能跑、能升级、能扩容、能审计"——每一条都要有脚本和文档支撑。*