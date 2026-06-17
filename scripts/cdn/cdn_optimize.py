#!/usr/bin/env python3
"""
腾讯云 CDN 性能优化脚本（安全版）

做的事：
  - 启用 HTTP/2
  - 启用 Brotli 智能压缩
  - 验证修改结果

安全保证：
  - 用 DescribeDomainsConfig 先抓完整配置
  - 改 Https.Http2 时，把完整 Https 对象（含 CertInfo、TlsVersion 等）
    一起传回去，绝不重置任何未指定的字段
  - Compression 用 contentType 模式（不是 fileExtensions），覆盖 html/css/js
  - 不会动 Hsts、ForceRedirect、IpFilter 等其它配置

使用：
  export TENCENTCLOUD_SECRET_ID="你的 SecretId"
  export TENCENTCLOUD_SECRET_KEY="你的 SecretKey"
  python3 cdn_optimize.py

可调环境变量：
  CDN_DOMAIN        要配置的域名（默认 www.python4office.cn）
  CDN_DRY_RUN=1     只查看不修改
  CDN_VERIFY=1      只做验证（curl 检查 HTTP/2 + Brotli）
  CDN_SKIP_HTTP2=1  跳过 HTTP/2
  CDN_SKIP_BROTLI=1 跳过 Brotli
"""
import os
import sys
import json
import time
import hashlib
import hmac
import datetime
import urllib.request
import urllib.error

SECRET_ID = (
    os.environ.get("TENCENTCLOUD_SECRETID")
    or os.environ.get("TENCENTCLOUD_SECRET_ID")
)
SECRET_KEY = (
    os.environ.get("TENCENTCLOUD_SECRETKEY")
    or os.environ.get("TENCENTCLOUD_SECRET_KEY")
)
DOMAIN = os.environ.get("CDN_DOMAIN", "www.python4office.cn")
DRY_RUN = os.environ.get("CDN_DRY_RUN", "0") == "1"
VERIFY_ONLY = os.environ.get("CDN_VERIFY", "0") == "1"
SKIP_HTTP2 = os.environ.get("CDN_SKIP_HTTP2", "0") == "1"
SKIP_BROTLI = os.environ.get("CDN_SKIP_BROTLI", "0") == "1"

API_HOST = "cdn.tencentcloudapi.com"
API_VERSION = "2018-06-06"
ALGORITHM = "TC3-HMAC-SHA256"


def _now():
    # timezone-aware UTC，Python 3.12+ 兼容
    return datetime.datetime.now(datetime.timezone.utc)


def _sign_and_call(action: str, payload: dict) -> dict:
    if not SECRET_ID or not SECRET_KEY:
        print(
            "❌ 需要 TENCENTCLOUD_SECRET_ID / TENCENTCLOUD_SECRET_KEY"
        )
        sys.exit(1)

    service = "cdn"
    content_type = "application/json; charset=utf-8"

    t = _now()
    timestamp = str(int(t.timestamp()))
    date = t.strftime("%Y-%m-%d")

    body = json.dumps(payload)
    payload_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()

    canonical_headers = (
        f"content-type:{content_type}\n"
        f"host:{API_HOST}\n"
        f"x-tc-action:{action.lower()}\n"
    )
    signed_headers = "content-type;host;x-tc-action"
    canonical_request = (
        f"POST\n/\n\n{canonical_headers}\n{signed_headers}\n{payload_hash}"
    )

    credential_scope = f"{date}/{service}/tc3_request"
    string_to_sign = (
        f"{ALGORITHM}\n{timestamp}\n{credential_scope}\n"
        f"{hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()}"
    )

    secret_date = hmac.new(
        f"TC3{SECRET_KEY}".encode("utf-8"),
        date.encode("utf-8"),
        hashlib.sha256,
    ).digest()
    secret_service = hmac.new(
        secret_date, service.encode("utf-8"), hashlib.sha256
    ).digest()
    secret_signing = hmac.new(
        secret_service, "tc3_request".encode("utf-8"), hashlib.sha256
    ).digest()
    signature = hmac.new(
        secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256
    ).hexdigest()

    authorization = (
        f"{ALGORITHM} Credential={SECRET_ID}/{credential_scope}, "
        f"SignedHeaders={signed_headers}, Signature={signature}"
    )

    headers = {
        "Authorization": authorization,
        "Content-Type": content_type,
        "Host": API_HOST,
        "X-TC-Action": action,
        "X-TC-Timestamp": timestamp,
        "X-TC-Version": API_VERSION,
    }

    req = urllib.request.Request(
        f"https://{API_HOST}",
        data=body.encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        data = json.loads(e.read().decode("utf-8"))

    if "Response" in data and "Error" in data["Response"]:
        err = data["Response"]["Error"]
        print(f"❌ API 错误 [{action}]: {err.get('Code')} - {err.get('Message')}")
        return {}
    return data.get("Response", {})


def get_full_config():
    """拉取完整配置（必须在做任何修改前调用）"""
    print(f"\n=== DescribeDomainsConfig: {DOMAIN} ===")
    resp = _sign_and_call(
        "DescribeDomainsConfig",
        {"Filters": [{"Name": "domain", "Value": [DOMAIN]}]},
    )
    if not resp or "Domains" not in resp or not resp["Domains"]:
        print("  ❌ 获取配置失败")
        return None
    cfg = resp["Domains"][0]
    https = cfg.get("Https", {})
    comp = cfg.get("Compression", {})
    print(f"  Https.Switch: {https.get('Switch')}")
    print(f"  Https.Http2: {https.get('Http2')}")
    print(f"  Https.TlsVersion: {https.get('TlsVersion')}")
    print(f"  Https.CertInfo.CertId: {(https.get('CertInfo') or {}).get('CertId')}")
    print(f"  Https.SslStatus: {https.get('SslStatus')}")
    print(f"  Compression.Switch: {comp.get('Switch')}")
    print(f"  Compression.Algorithms: {comp.get('CompressionRules')[0].get('Algorithms') if comp.get('CompressionRules') else 'n/a'}")
    return cfg


def enable_http2(cfg):
    if SKIP_HTTP2:
        print("\n=== 跳过 HTTP/2 ===")
        return
    print("\n=== 启用 HTTP/2 ===")
    https = cfg.get("Https", {})
    new_https = dict(https)
    new_https["Http2"] = "on"
    # Switch 必须是 on 才有意义
    new_https["Switch"] = "on"
    # 关键：把 CertInfo 等重要字段原样保留
    payload = {"Domain": DOMAIN, "Https": new_https}
    print(f"  payload.Https: {json.dumps({k: v for k, v in new_https.items() if k not in ['CertInfo']}, ensure_ascii=False)}")
    if DRY_RUN:
        print(f"  [DRY RUN] 完整 payload 大小: {len(json.dumps(payload))} chars")
        return
    resp = _sign_and_call("UpdateDomainConfig", payload)
    if resp:
        print(f"  ✅ ok: {resp.get('RequestId')}")


def enable_brotli(cfg):
    if SKIP_BROTLI:
        print("\n=== 跳过 Brotli ===")
        return
    print("\n=== 启用 Brotli 智能压缩（contentType 模式）===")
    new_comp = {
        "Switch": "on",
        "CompressionRules": [
            {
                "Compress": True,
                "Algorithms": ["brotli", "gzip"],  # brotli 优先
                "RuleType": "contentType",
                "RulePaths": [
                    "text/html",
                    "text/xml",
                    "text/plain",
                    "text/css",
                    "text/javascript",
                    "application/json",
                    "application/javascript",
                    "application/x-javascript",
                    "application/rss+xml",
                    "application/xml",
                    "image/svg+xml",
                ],
                "MinLength": 256,
                "MaxLength": 20971520,
            }
        ],
    }
    payload = {"Domain": DOMAIN, "Compression": new_comp}
    if DRY_RUN:
        print(f"  [DRY RUN] payload: {json.dumps(payload, ensure_ascii=False, indent=2)[:300]}")
        return
    resp = _sign_and_call("UpdateDomainConfig", payload)
    if resp:
        print(f"  ✅ ok: {resp.get('RequestId')}")


def verify_with_curl():
    """用本地 curl 实际探测线上响应"""
    import subprocess
    print(f"\n=== 验证: {DOMAIN} ===")
    paths = ["/", "/css/main.css", "/js/main.js"]
    for path in paths:
        url = f"https://{DOMAIN}{path}"
        r = subprocess.run(
            [
                "/usr/bin/curl", "-sI",
                "-H", "User-Agent: Mozilla/5.0",
                "-H", "Accept-Encoding: br, gzip",
                url,
            ],
            capture_output=True, text=True, timeout=15,
        )
        lines = r.stdout.splitlines()
        first = lines[0] if lines else "(no response)"
        print(f"\n  {url}")
        print(f"    {first}")
        for h in lines[1:]:
            low = h.lower()
            if any(k in low for k in [
                "content-encoding", "content-length",
                "x-cache-lookup", "alt-svc", "server",
            ]):
                print(f"    {h}")


if __name__ == "__main__":
    if VERIFY_ONLY:
        verify_with_curl()
        sys.exit(0)

    print(f"Domain: {DOMAIN}")
    print(f"Dry run: {DRY_RUN}")

    cfg = get_full_config()
    if not cfg:
        sys.exit(1)

    enable_http2(cfg)
    enable_brotli(cfg)

    print("\n--- 修改后状态 ---")
    time.sleep(2)
    get_full_config()
    verify_with_curl()

    print("\n✅ 完成。1-5 分钟后全网生效。")
