#!/usr/bin/env python3
"""
腾讯云 CDN 缓存刷新脚本（按 URL）

用途：origin nginx 改了 header 或文件修改后，把 CDN 边缘缓存强制刷新成新版本。

用法：
    python3 purge_static_assets.py             # 刷首页 / 关键 css/js
    python3 purge_static_assets.py --all       # 刷全部 public/ 静态资源

需要环境变量：
    TENCENTCLOUD_SECRETID / TENCENTCLOUD_SECRETKEY

API: tencentcloudapi.com / cdn / 2018-06-06 / PurgeUrlsCache
"""
import os
import sys
import json
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

API_HOST = "cdn.tencentcloudapi.com"
API_VERSION = "2018-06-06"
ALGORITHM = "TC3-HMAC-SHA256"


def _now():
    return datetime.datetime.now(datetime.timezone.utc)


def sign_and_call(action, payload):
    """通用签名 + 调腾讯云 API"""
    service = "cdn"
    timestamp = int(_now().timestamp())
    date = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).strftime("%Y-%m-%d")

    # 1. canonical request
    canonical_uri = "/"
    canonical_querystring = ""
    canonical_headers = (
        f"content-type:application/json; charset=utf-8\n"
        f"host:{API_HOST}\n"
        f"x-tc-action:{action.lower()}\n"
    )
    signed_headers = "content-type;host;x-tc-action"
    payload_str = json.dumps(payload, separators=(",", ":"))
    hashed_payload = hashlib.sha256(payload_str.encode("utf-8")).hexdigest()
    canonical_request = (
        f"POST\n{canonical_uri}\n{canonical_querystring}\n"
        f"{canonical_headers}\n{signed_headers}\n{hashed_payload}"
    )

    # 2. string to sign
    credential_scope = f"{date}/{service}/tc3_request"
    hashed_canonical = hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
    string_to_sign = f"{ALGORITHM}\n{timestamp}\n{credential_scope}\n{hashed_canonical}"

    # 3. signature
    secret_date = hmac.new(
        f"TC3{SECRET_KEY}".encode("utf-8"), date.encode("utf-8"), hashlib.sha256
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

    # 4. authorization
    authorization = (
        f"{ALGORITHM} Credential={SECRET_ID}/{credential_scope}, "
        f"SignedHeaders={signed_headers}, Signature={signature}"
    )

    # 5. call
    headers = {
        "Authorization": authorization,
        "Content-Type": "application/json; charset=utf-8",
        "Host": API_HOST,
        "X-TC-Action": action,
        "X-TC-Timestamp": str(timestamp),
        "X-TC-Version": API_VERSION,
    }

    req = urllib.request.Request(
        f"https://{API_HOST}/",
        data=payload_str.encode("utf-8"),
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read()
        try:
            return json.loads(body)
        except Exception:
            return {"error": f"HTTP {e.code}", "body": body.decode("utf-8", errors="replace")}


def purge_urls(urls):
    """PurgeUrlsCache"""
    if not urls:
        return {"Urls": []}
    payload = {"Urls": urls}
    return sign_and_call("PurgeUrlsCache", payload)


# ============================================================
# 默认要刷新的 URL（关键静态资源）
# ============================================================
DEFAULT_URLS = [
    # 首页
    f"https://{DOMAIN}/",
    # 首页相关 CSS
    f"https://{DOMAIN}/css/index.css",
    f"https://{DOMAIN}/css/promo.css",
    f"https://{DOMAIN}/css/fontawesome.min.css",
    f"https://{DOMAIN}/css/index.css",  # 重复无聊，确保 cache invalidate
    # JS
    f"https://{DOMAIN}/js/utils.js",
    f"https://{DOMAIN}/js/main.js",
    f"https://{DOMAIN}/js/promo.js",
]


def main():
    if not SECRET_ID or not SECRET_KEY:
        print("❌ 缺少环境变量：TENCENTCLOUD_SECRETID / TENCENTCLOUD_SECRETKEY")
        print("   export TENCENTCLOUD_SECRET_ID=...")
        print("   export TENCENTCLOUD_SECRET_KEY=...")
        sys.exit(2)

    print(f"Domain: {DOMAIN}")
    print(f"Mode:    {'DRY-RUN' if DRY_RUN else 'REAL'}")

    # 查 public/ 所有静态资源（如果 --all）
    if "--all" in sys.argv:
        import glob

        base = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "hexo", "hexo", "public",
        )
        urls = []
        for ext in ("css", "js", "png", "jpg", "jpeg", "gif", "svg", "ico", "woff", "woff2", "ttf"):
            for p in glob.glob(f"{base}/**/*.{ext}", recursive=True):
                rel = os.path.relpath(p, base).replace(os.sep, "/")
                urls.append(f"https://{DOMAIN}/{rel}")
        # 去重
        urls = sorted(set(urls))
        print(f"找到 {len(urls)} 个静态资源 URL（glob 模式）")
    else:
        urls = DEFAULT_URLS
        print(f"使用默认 {len(urls)} 个关键 URL")

    # 去重
    urls = sorted(set(urls))

    if DRY_RUN:
        for u in urls:
            print("  DRY", u)
        return

    # 调 API（一次最多 10000 URL）
    print(f"\n正在刷新 CDN 缓存...")
    batch_size = 100
    for i in range(0, len(urls), batch_size):
        batch = urls[i:i+batch_size]
        result = purge_urls(batch)
        if "error" in result or "Response" not in result:
            print(f"❌ batch {i//batch_size+1}: {result}")
            sys.exit(1)
        else:
            reqid = result["Response"].get("RequestId", "?")
            print(f"✅ batch {i//batch_size+1}: {len(batch)} URLs  RequestId={reqid}")

    print(f"\n🎉 完成。{len(urls)} 个 URL 已提交刷新。")
    print("注意：CDN 节点同步需要 30s ~ 5min（国内通常 1min）。")


if __name__ == "__main__":
    main()
