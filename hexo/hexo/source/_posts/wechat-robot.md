---
title: 一个15分钟的视频，教你用Python创建自己的微信机器人！（源代码）
date: 2022-03-30 17:01:54
tags: 机器人
---

### 你好呀，我是[程序员晚枫](http://www.python4office.cn/wechat-qrcode/)
- 🐧 编程知识博主
- 👨‍💻 我的B站，点击查看👉[千万别来重庆工作，别问为什么](https://www.bilibili.com/video/BV1aD4y1N7ai)
- 💬 我的微信，点击添加👉[python-office](https://cos.python-office.com/wechat/wechat.jpg)
- ⚡ 学习资料，点击领取👉[60套Python课程的合集](http://www.python4office.cn/vedio-course/)
- 🎁 粉丝福利👉[我的短视频，欢迎3连](https://space.bilibili.com/1989702333)



### 机器人代码



- 视频教程：[一个15分钟的视频，教你用Python创建自己的微信机器人！](https://www.bilibili.com/video/BV11L411L7oi)
- 代码：👇

<!-- more -->



```python
# -*- coding: UTF- -*-
# @公众号 :Python自动化办公社区
# @Docs: 学习网站：https://www.python-office.com/video/video.html
# @Description: 用Python开发微信聊天机器人
# Python全套学习资源：https://www.python-office.com/video/video.html
from wxpy import *
import requests, json, time

# 创建机器人
# bot = Bot()
bot = Bot(console_qr=-2, cache_path=True)  # 移植到linux，console_qr设置True和2都无法扫描登录,设置-之后正常登录。

# 创建机器人
bot = Bot()


# bot = Bot(console_qr=-, cache_path=True)  # 移植到linux，console_qr设置True和都无法扫描登录,设置-之后正常登录。


@bot.register(Group)
def print_messages(msg):
    # 登陆微信的用户群昵称
    user_name = msg.sender.self.name
    # 信息内容
    content = msg.raw['Content']
    # 发信息好友名称
    friend_name = msg.raw['ActualNickName']
    # 打印出对方说的话
    print("{} - 说 - {}".format(friend_name, content))

    # 类型
    type = msg.raw['Type']

    # 请自行添加关键词对应的内容
    keywords_dic = {

        '你好': '你好，我是机器人',
        '写作变现': '写作变现系列，真香！http://t.cn/AxHLdYK',
        '自动化办公': '基础如何学习自动化办公? http://t.cn/AxHPxpx',

    }
    # 把昵称，改为你自己的
    if '程序员晚枫' in user_name:
        # 以下代码，不要修改
        for key in keywords_dic.keys():
            if key in content:
                res_keyword_reply = '''{}'''
                reply_content = res_keyword_reply.format(keywords_dic[key])
                return reply_content


# 堵塞线程，并进入 Python 命令行
# embed()
bot.join()


```



---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)就能上手做AI项目。