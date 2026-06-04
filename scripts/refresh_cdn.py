#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
腾讯云CDN域名刷新工具
用于刷新域名的CDN缓存
使用腾讯云官方Python SDK
"""

import os
import sys

# 要刷新的URL列表（main 和 refresh_cdn_cache 共享同一个源）
PATHS = [
    "https://www.python4office.cn/",
    "https://python4office.cn/",
    "https://www.python-office.com/",
    "https://python-office.com/",
    "https://cos.python-office.com/"
]

# 检查是否安装了腾讯云SDK
try:
    from tencentcloud.common import credential
    from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
    from tencentcloud.cdn.v20180606 import cdn_client, models
except ImportError:
    print("错误: 未安装腾讯云Python SDK")
    print("请先安装: pip install tencentcloud-sdk-python")
    sys.exit(1)


def refresh_cdn_cache():
    """刷新CDN缓存"""
    # 从环境变量获取腾讯云凭证
    secret_id = os.getenv('SecretId')
    secret_key = os.getenv('SecretKey')

    if not secret_id or not secret_key:
        print("错误: 请设置环境变量 SecretId 和 SecretKey")
        sys.exit(1)

    try:
        # 创建凭证对象
        cred = credential.Credential(secret_id, secret_key)

        # 创建CDN客户端
        client = cdn_client.CdnClient(cred, "")

        # 创建目录刷新请求
        req = models.PurgePathCacheRequest()
        req.Paths = list(PATHS)
        req.FlushType = "flush"

        # 发送刷新请求
        resp = client.PurgePathCache(req)

        print("CDN缓存刷新请求已发送")
        print(f"任务ID: {resp.TaskId}")
        return True

    except TencentCloudSDKException as e:
        print(f"腾讯云SDK错误: {e}")
        return False
    except Exception as e:
        print(f"未知错误: {str(e)}")
        return False


def main():
    """主函数"""
    print("=== 腾讯云CDN缓存刷新工具 ===")
    print()
    print(f"将刷新以下 {len(PATHS)} 个 URL:")
    for p in PATHS:
        print(f"  - {p}")
    print()

    # 检查环境变量
    secret_id = os.getenv('SecretId')
    secret_key = os.getenv('SecretKey')

    if not secret_id or not secret_key:
        print("环境变量检查:")
        print(f"  SecretId: {'已设置' if secret_id else '未设置'}")
        print(f"  SecretKey: {'已设置' if secret_key else '未设置'}")
        print()
        print("请先设置环境变量:")
        print("  export SecretId=你的SecretId")
        print("  export SecretKey=你的SecretKey")
        sys.exit(1)

    print("环境变量检查通过")
    print("开始刷新CDN缓存...")
    print()

    # 执行刷新
    success = refresh_cdn_cache()

    if success:
        print()
        print("刷新完成！")
        print(f"已提交 {len(PATHS)} 个 URL 的刷新任务")
        print("注意: CDN缓存刷新通常需要几分钟时间生效")
    else:
        print()
        print("刷新失败，请检查错误信息")
        sys.exit(1)


if __name__ == "__main__":
    main()
