---
title: 一文掌握requests库：Python中的爬虫神器
date: 2024-11-16 00:41:49
tags: [第三方库,pip]
---


<p align="center" id='腾讯云-banner'>
    <a target="_blank" href='https://curl.qcloud.com/3csDz9jU'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F1040x100-tencent.jpg" width="100%"/>
    </a>   
</p>

> 这是专栏[优秀的第三方库](http://www.python4office.cn/course/%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93/all/)的第4篇原创文章。


大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。


`requests` 是一个非常流行的 Python HTTP 库，用于发送各种 HTTP 请求。以下是 `requests` 的一些基本用法：

## 安装

首先，确保你已经安装了 `requests` 库。如果没有安装，可以通过以下命令安装：

```bash
pip install requests
```

## 发送 GET 请求

```python
import requests

# 发送 GET 请求
response = requests.get('https://python-office.com/data')

# 检查请求是否成功
if response.status_code == 200:
    data = response.json()  # 将响应内容解析为 JSON
    print(data)
else:
    print('请求失败，状态码：', response.status_code)
```

## 发送 POST 请求

```python
import requests

# 发送 POST 请求
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://python-office.com/submit', data=payload)

# 检查请求是否成功
if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print('请求失败，状态码：', response.status_code)
```

## 发送带有 Headers 的请求

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get('https://python-office.com/data', headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print('请求失败，状态码：', response.status_code)
```

## 发送带有 Cookies 的请求

```python
import requests

cookies = {
    'session_id': '123456789',
    'token': 'abcdefg'
}

response = requests.get('https://python-office.com/data', cookies=cookies)

if response.status_code == 200:
    print(response.text)
else:
    print('请求失败，状态码：', response.status_code)
```

## 发送带有认证信息的请求

```python
import requests

auth = ('username', 'password')

response = requests.get('https://python-office.com/protected', auth=auth)

if response.status_code == 200:
    print(response.text)
else:
    print('请求失败，状态码：', response.status_code)
```

## 发送文件

```python
import requests

files = {'file': open('report.xls', 'rb')}

response = requests.post('https://python-office.com/upload', files=files)

if response.status_code == 200:
    print('文件上传成功')
else:
    print('文件上传失败，状态码：', response.status_code)
```

## 异常处理

```python
import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://python-office.com/data')
    response.raise_for_status()  # 如果响应状态码不是 200，将抛出 HTTPError 异常
    print(response.text)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
```

这些是 `requests` 库的一些基本用法。通过这些示例，你可以了解如何使用 `requests` 发送不同类型的 HTTP 请求，并处理响应和异常。




![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg)就能上手做AI项目。