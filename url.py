# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：python-office
@代码日期    ：2024/12/1 19:31 
@本段代码的视频说明     ：
'''
import json
import logging
import os
from tencentcloud.common import credential
from tencentcloud.cdn.v20180606 import cdn_client, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

# 配置日志

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 为你的腾讯云API密钥

secret_id = os.getenv('t_id')
secret_key = os.getenv('t_key')

# 设置认证信息

cred = credential.Credential(secret_id, secret_key)
httpProfile = HttpProfile()
httpProfile.endpoint = "cdn.tencentcloudapi.com"
#httpProfile.verify = False  # 禁用SSL验证,可选
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile

# 初始化CDN客户端

client = cdn_client.CdnClient(cred, "", clientProfile)

def refresh_urls(urls):
    try:
        req = models.PurgeUrlsCacheRequest()
        params = {
            "Urls": urls
        }
        req.from_json_string(json.dumps(params))
        resp = client.PurgeUrlsCache(req)
        logging.info("Response: %s", resp.to_json_string())
    except Exception as e:
        logging.error("Error: %s", str(e))

# 刷新缓存(替换你的url)

urls_to_refresh = [
    "http://python4office.cn"
]

logging.info("Starting URL refresh...")
refresh_urls(urls_to_refresh)
logging.info("URL refresh completed.")
