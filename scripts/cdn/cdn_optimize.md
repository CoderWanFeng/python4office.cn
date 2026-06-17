# 腾讯云 CDN 优化脚本

## 一次性配置
1. 登录 [腾讯云 API 密钥控制台](https://console.cloud.tencent.com/cam/capi)
2. 新建密钥（建议只授 CDN 权限 + IP 白名单）
3. 设环境变量（**不要把密钥直接写到任何文件里**）：

```bash
export TENCENTCLOUD_SECRET_ID="AKIDxxxxxxxx"
export TENCENTCLOUD_SECRET_KEY="xxxxxxxxxxxx"
# 脚本同时兼容 TENCENTCLOUD_SECRETID / TENCENTCLOUD_SECRETKEY（无下划线）

## 用法

```bash
# 1) 只看当前状态（不修改）
python3 scripts/cdn/cdn_optimize.py        # DRY_RUN 默认关闭，会执行修改

# 2) 试运行（不真改）
CDN_DRY_RUN=1 python3 scripts/cdn/cdn_optimize.py

# 3) 只验证
CDN_VERIFY=1 python3 scripts/cdn/cdn_optimize.py

# 4) 自定义域名
CDN_DOMAIN=cdn.example.com python3 scripts/cdn/cdn_optimize.py
```

## 做什么
- 启用 HTTP/2
- 启用 Brotli 智能压缩（覆盖 html/css/js/xml/json/svg/md/txt）
- 修改前/后打印配置
- 用本地 curl 验证协议版本 + content-encoding

## 撤销（如果想回退）
- 控制台：域名管理 → HTTPS 配置 → 关闭 HTTP/2
- 控制台：域名管理 → 智能压缩 → 关闭总开关 / 删规则
