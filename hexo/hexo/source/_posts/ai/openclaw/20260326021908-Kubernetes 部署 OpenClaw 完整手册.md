---
title: Kubernetes 部署 OpenClaw 完整手册！高可用架构就靠它
date: 2026-03-26 02:19:08
tags: [OpenClaw, Kubernetes, K8s, 高可用]
categories: AI 编程实战
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---


<!-- more -->

![Kubernetes 部署 OpenClaw 完整手册！高可用架构就靠它](https://images.unsplash.com/photo-1677443994799-97b6aae1?w=800&h=400&fit=crop)
![Kubernetes 部署 OpenClaw 完整手册！高可用架构就靠它](https://images.unsplash.com/photo-1518709268805-4e6709f4?w=800&h=400&fit=crop)

大家好，我是正在实战各种 AI 项目的程序员晚枫。

## 😫 开篇：K8s 部署是生产环境的终极方案

"晚枫，我们用户量大，需要高可用，怎么部署？"

这种情况，Kubernetes（K8s）是终极方案。**自动扩缩容、故障自愈、负载均衡，全都有**。

今天把 K8s 部署 OpenClaw 的完整手册整理出来，照着做，90 分钟搞定生产级高可用架构。

## 📋 部署前准备

### 1. K8s 集群要求

| 组件 | 最低配置 | 推荐配置 |
|------|----------|----------|
| Master 节点 | 2 核 4G | 4 核 8G × 3（高可用） |
| Worker 节点 | 2 核 4G | 4 核 8G × N（按需） |
| 网络 | 千兆 | 万兆 |
| 存储 | 50G SSD | 200G SSD × N |

### 2. K8s 发行版选择

```
推荐：
✓ K3s（轻量级，适合中小规模）
✓ KubeSphere（易用，带管理界面）
✓ 云厂商托管 K8s（最省心）

备选：
✓ 原生 Kubernetes（功能最全）
✓ Rancher（多集群管理）
```

### 3. 部署方式选择

```
方案 1：云厂商托管 K8s（推荐）
- 阿里云 ACK
- 腾讯云 TKE
- 华为云 CCE
- 火山引擎 VKE
优点：免运维，高可用
缺点：成本略高

方案 2：自建 K8s
- 用 kubeadm 部署
- 用 K3s 部署
优点：成本低，可控
缺点：需要运维能力
```

## 🚀 部署步骤（云托管 K8s）

### 第 1 步：创建 K8s 集群

```
以阿里云 ACK 为例：

1. 登录阿里云控制台
2. 进入"容器服务 Kubernetes"
3. 点击"创建集群"
4. 选择配置：
   - 集群类型：托管版（免运维）
   - Worker 节点：2 台 4 核 8G
   - 网络：VPC 专有网络
   - 存储：云盘
5. 确认配置，完成支付
6. 等待集群创建（约 10 分钟）
```

### 第 2 步：配置 kubectl

```bash
# 下载集群配置
# 阿里云控制台 → ACK → 集群信息 → 连接信息

# 配置 kubectl
mkdir -p ~/.kube
# 下载 kubeconfig 文件到 ~/.kube/config

# 验证连接
kubectl cluster-info
kubectl get nodes

# 应该看到：
# NAME         STATUS   ROLES    AGE   VERSION
# node-1       Ready    <none>   10m   v1.26.0
# node-2       Ready    <none>   10m   v1.26.0
```

### 第 3 步：创建 Namespace

```bash
# 创建命名空间
kubectl create namespace openclaw

# 验证
kubectl get namespaces | grep openclaw
```

### 第 4 步：创建 ConfigMap

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: openclaw-config
  namespace: openclaw
data:
  OPENCLAW_PORT: "8000"
  OPENCLAW_HOST: "0.0.0.0"
  DEBUG: "False"
  REDIS_URL: "redis://openclaw-redis:6379/0"
```

```bash
kubectl apply -f configmap.yaml
```

### 第 5 步：创建 Secret

```yaml
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: openclaw-secret
  namespace: openclaw
type: Opaque
stringData:
  DATABASE_URL: "postgresql://openclaw:secure_password@postgres:5432/openclaw"
  SECRET_KEY: "your-secret-key-here"
```

```bash
kubectl apply -f secret.yaml
```

### 第 6 步：部署 PostgreSQL

```yaml
# postgres-statefulset.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: openclaw-postgres
  namespace: openclaw
spec:
  serviceName: postgres
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:14-alpine
        ports:
        - containerPort: 5432
        env:
        - name: POSTGRES_USER
          value: "openclaw"
        - name: POSTGRES_PASSWORD
          value: "secure_password"
        - name: POSTGRES_DB
          value: "openclaw"
        volumeMounts:
        - name: postgres-storage
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: postgres-storage
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 10Gi
```

```bash
kubectl apply -f postgres-statefulset.yaml
```

### 第 7 步：部署 Redis

```yaml
# redis-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: openclaw-redis
  namespace: openclaw
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:7-alpine
        ports:
        - containerPort: 6379
        command: ["redis-server", "--appendonly", "yes"]
        volumeMounts:
        - name: redis-storage
          mountPath: /data
      volumes:
      - name: redis-storage
        emptyDir: {}
```

```bash
kubectl apply -f redis-deployment.yaml
```

### 第 8 步：部署 OpenClaw 应用

```yaml
# openclaw-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: openclaw-app
  namespace: openclaw
spec:
  replicas: 3  # 3 个副本，高可用
  selector:
    matchLabels:
      app: openclaw
  template:
    metadata:
      labels:
        app: openclaw
    spec:
      containers:
      - name: openclaw
        image: your-registry/openclaw:latest
        ports:
        - containerPort: 8000
        envFrom:
        - configMapRef:
            name: openclaw-config
        - secretRef:
            name: openclaw-secret
        resources:
          requests:
            cpu: "500m"
            memory: "512Mi"
          limits:
            cpu: "1000m"
            memory: "1Gi"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5
```

```bash
kubectl apply -f openclaw-deployment.yaml
```

### 第 9 步：创建 Service

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: openclaw-service
  namespace: openclaw
spec:
  selector:
    app: openclaw
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer  # 云厂商会自动创建负载均衡
```

```bash
kubectl apply -f service.yaml
```

### 第 10 步：配置 Ingress

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: openclaw-ingress
  namespace: openclaw
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  rules:
  - host: openclaw.your-domain.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: openclaw-service
            port:
              number: 80
  tls:
  - hosts:
    - openclaw.your-domain.com
    secretName: openclaw-tls
```

```bash
kubectl apply -f ingress.yaml
```

## 🔧 高级功能配置

### 1. 自动扩缩容（HPA）

```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: openclaw-hpa
  namespace: openclaw
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: openclaw-app
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

```bash
kubectl apply -f hpa.yaml
```

### 2. 健康检查

```yaml
# 在 Deployment 中添加
livenessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 30
  periodSeconds: 10
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /ready
    port: 8000
  initialDelaySeconds: 5
  periodSeconds: 5
  failureThreshold: 3
```

### 3. 持久化存储

```yaml
# 创建 PVC
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: openclaw-data
  namespace: openclaw
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 20Gi
  storageClassName: nas
```

### 4. 监控告警

```bash
# 安装 Prometheus
helm install prometheus prometheus-community/kube-prometheus-stack

# 访问 Grafana
kubectl port-forward svc/prometheus-grafana 3000:80
# 浏览器访问 http://localhost:3000
```

## 📊 运维命令速查

### 查看状态

```bash
# 查看所有资源
kubectl get all -n openclaw

# 查看 Pod 状态
kubectl get pods -n openclaw

# 查看 Pod 详情
kubectl describe pod openclaw-app-xxx -n openclaw
```

### 查看日志

```bash
# 查看 Pod 日志
kubectl logs openclaw-app-xxx -n openclaw

# 实时查看
kubectl logs -f openclaw-app-xxx -n openclaw
```

### 进入容器

```bash
kubectl exec -it openclaw-app-xxx -n openclaw -- bash
```

### 滚动更新

```bash
# 更新镜像
kubectl set image deployment/openclaw-app openclaw=your-registry/openclaw:v2 -n openclaw

# 查看更新状态
kubectl rollout status deployment/openclaw-app -n openclaw

# 回滚
kubectl rollout undo deployment/openclaw-app -n openclaw
```

### 扩缩容

```bash
# 手动扩容
kubectl scale deployment openclaw-app --replicas=5 -n openclaw

# 查看副本状态
kubectl get pods -n openclaw
```

## 💰 成本分析

### 云托管 K8s 成本

| 项目 | 配置 | 月成本 |
|------|------|--------|
| K8s 管理费 | 托管版 | 500 元 |
| Worker 节点 | 4 核 8G × 3 | 6000 元 |
| 负载均衡 | SLB | 200 元 |
| 存储 | 100G SSD | 100 元 |
| **合计** | | **6800 元/月** |

### 自建 K8s 成本

| 项目 | 配置 | 月成本 |
|------|------|--------|
| 服务器 | 4 核 8G × 3 | 6000 元 |
| 运维人力 | 0.2 人 | 4000 元 |
| **合计** | | **10000 元/月** |

**结论：云托管 K8s 更省心，综合成本更低。**

## 🔧 常见问题排查

### 问题 1：Pod 无法启动

```bash
# 查看 Pod 状态
kubectl describe pod openclaw-app-xxx -n openclaw

# 查看日志
kubectl logs openclaw-app-xxx -n openclaw

# 常见原因：
# - 镜像拉取失败
# - 资源不足
# - 配置错误
```

### 问题 2：Service 无法访问

```bash
# 查看 Service
kubectl get svc -n openclaw

# 查看 Endpoints
kubectl get endpoints -n openclaw

# 检查 Pod 是否就绪
kubectl get pods -n openclaw
```

### 问题 3：Ingress 无法访问

```bash
# 查看 Ingress
kubectl get ingress -n openclaw

# 查看 Ingress Controller
kubectl get pods -n ingress-nginx

# 检查 DNS 解析
nslookup openclaw.your-domain.com
```

## 🚀 更多应用场景

- 多环境部署
- 蓝绿部署
- 金丝雀发布
- 多集群管理

## 💬 金句总结

> K8s 不是银弹，但大规模场景下是必选项。

**高可用架构，从 K8s 开始。**

## 📚 相关阅读

- [OpenClaw 部署教程](https://www.python-office.com/openclaw/deploy/)
- [AI 编程学习入口](https://www.python-office.com/)
- [程序员晚枫 AI 编程课](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw/)

## 🔗 联系方式

| 平台 | 账号/链接 |
|------|----------|
| 微信 | [扫码加好友](https://www.python4office.cn/wechat-qrcode/) |
| 微博 | [@程序员晚枫](https://weibo.com/u/7726957925) |
| 知乎 | [@程序员晚枫](https://www.zhihu.com/people/CoderWanFeng) |
| 抖音 | [@程序员晚枫](https://www.douyin.com/user/MS4wLjABAAAA259649365) |
| 小红书 | [@程序员晚枫](https://xhslink.com/m/4i8OhkfTvW3) |
| B 站 | [Python 自动化办公社区](https://space.bilibili.com/259649365) |

**主营业务**：AI 编程培训、企业内训、技术咨询

---

*K8s 部署，生产级高可用架构！*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


