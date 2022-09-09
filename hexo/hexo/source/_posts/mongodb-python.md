---
title: mongodb-python
date: 2022-09-06 15:14:23
tags:
---

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