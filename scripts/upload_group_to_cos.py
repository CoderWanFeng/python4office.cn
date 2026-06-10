#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
腾讯云COS图片上传工具
将指定本地目录下的图片上传到 COS 桶的 group/ 目录下
"""

import os
import sys

# 本地图片目录
LOCAL_DIR = "/Users/wanfeng/晚枫工作室/相关图片/group"

# COS 桶配置
BUCKET = "python-office-1300615378"
REGION = "ap-chongqing"
COS_DIR = "group"  # 桶内目录

# 允许上传的图片后缀
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"}


def get_cos_client(secret_id, secret_key):
    """创建并返回 COS 客户端"""
    from qcloud_cos import CosConfig, CosS3Client
    config = CosConfig(Region=REGION, SecretId=secret_id, SecretKey=secret_key)
    return CosS3Client(config)


def upload_images(client):
    """上传 LOCAL_DIR 下所有图片到 COS 桶的 COS_DIR 目录"""
    if not os.path.isdir(LOCAL_DIR):
        print(f"错误: 本地目录不存在: {LOCAL_DIR}")
        return False

    files = [f for f in os.listdir(LOCAL_DIR)
             if os.path.splitext(f)[1].lower() in IMAGE_EXTS]

    if not files:
        print(f"提示: 目录 {LOCAL_DIR} 下没有找到图片文件")
        return True

    print(f"共发现 {len(files)} 个图片文件，开始上传...")
    print(f"目标: https://{BUCKET}.cos.{REGION}.myqcloud.com/{COS_DIR}/")
    print("-" * 60)

    success_count = 0
    fail_count = 0

    for name in files:
        local_path = os.path.join(LOCAL_DIR, name)
        cos_key = f"{COS_DIR}/{name}"
        local_size = os.path.getsize(local_path)
        try:
            print(f"上传: {name} (本地 {local_size} 字节) -> {cos_key}")
            # 必须以二进制方式打开文件再上传，避免 Body=字符串路径导致的内容截断问题
            with open(local_path, "rb") as fp:
                response = client.put_object(
                    Bucket=BUCKET,
                    Body=fp,
                    Key=cos_key,
                )
            # 上传后立即校验远端大小，不一致则删除并报错
            head = client.head_object(Bucket=BUCKET, Key=cos_key)
            remote_size = int(head.get("Content-Length", 0))
            if remote_size != local_size:
                client.delete_object(Bucket=BUCKET, Key=cos_key)
                raise RuntimeError(
                    f"大小校验失败: 本地 {local_size} 字节, 远端 {remote_size} 字节, 已删除"
                )
            print(f"  成功  ETag: {response.get('ETag', '')}  远端大小: {remote_size} 字节")
            success_count += 1
        except Exception as e:
            print(f"  失败: {e}")
            fail_count += 1

    print("-" * 60)
    print(f"上传完成: 成功 {success_count} 个, 失败 {fail_count} 个")
    return fail_count == 0


def _guess_content_type(filename):
    """根据后缀简单判断 Content-Type"""
    import mimetypes
    ctype, _ = mimetypes.guess_type(filename)
    return ctype or "application/octet-stream"


def main():
    """主函数"""
    print("=== 腾讯云COS图片上传工具 ===")
    print(f"本地目录: {LOCAL_DIR}")
    print(f"存储桶:   {BUCKET}  地域: {REGION}")
    print(f"桶内目录: {COS_DIR}/")
    print()

    secret_id = os.getenv("SecretId")
    secret_key = os.getenv("SecretKey")

    if not secret_id or not secret_key:
        print("环境变量检查:")
        print(f"  SecretId:  {'已设置' if secret_id else '未设置'}")
        print(f"  SecretKey: {'已设置' if secret_key else '未设置'}")
        print()
        print("请先设置环境变量:")
        print("  export SecretId=你的SecretId")
        print("  export SecretKey=你的SecretKey")
        sys.exit(1)

    print("环境变量检查通过，开始上传...")
    print()

    try:
        client = get_cos_client(secret_id, secret_key)
    except ImportError:
        print("错误: 未安装 cos-python-sdk-v5")
        print("请先安装: pip install cos-python-sdk-v5")
        sys.exit(1)

    ok = upload_images(client)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
