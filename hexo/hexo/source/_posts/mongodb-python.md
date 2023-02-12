---
title: mongodb-python
date: 2022-09-06 15:14:23
tags:
---



<p align="center" id='支付宝-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/TSnAjBs2dILSI_pM1pPznQ'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2Falipay.jpg" width="100%"/>
    </a>   
</p>


<p align="center" id='外卖-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/fdQ0TbTocPvw-DAMsFUlVg'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F%E5%A4%96%E5%8D%96-1040-100.jpg" width="100%"/>
    </a>   
</p>

## 安装
```
docker pull mongo

docker run -itd --name mongo -p 27017:27017 -e TZ=Asia/Shanghai -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=123456 mongo
```
## 连接
```
import pymongo

myclient = pymongo.MongoClient("mongodb://admin:123456@localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycol.insert_one(mydict)
print(x)
print(x)
```