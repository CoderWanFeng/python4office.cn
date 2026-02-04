---
title: Python定时打开世界杯直播，还有小姐姐语音提醒哦~不错过每一场世界杯比赛
date: 2022-11-20 00:37:16
tags:
---



卡塔尔世界杯今晚0点就要开幕了，为了防止大家沉迷工作，忘记看球，小编用50行Python代码写了一个**定时提醒你看球的小程序**，还有**小姐姐语音提醒**哟~🎇

## 1、效果展示 + 源码下载
👇代码运行效果如视频所示👇



赶紧去领取源代码吧，关注下面的公众号：**程序员晚枫**，在后台发生关键词：**世界杯**，就可以24小时自动获取全部代码啦~


## 2、代码说明
获取上面的源代码，在PyCharm里打开，其中重点逻辑介绍如下。👇

### 系统提醒

```python
toaster.show_toast(
    title='世界杯开始',
    msg='大兄弟，看球了！',
    icon_path=r'./icon.jpg',
)
```

### 打开浏览器

```python
webbrowser.open_new_tab(url)  # 打开浏览器
```

### 从视频中提取音乐
```python
office.video.video2mp3(path='./video.mp4', mp3_name='song.mp3')
```
### 播放音乐
```python
def play_song(song):
    file_name = song
    pygame.mixer.init()  # 只初始化音频部分
    # 载入的音乐不会全部放到内容中，而是以流的形式播放的，即在播放的时候才会一点点从文件中读取。
    track = pygame.mixer.music.load(file_name)
    # 播放载入的音乐。该函数立即返回，音乐播放在后台进行。
    pygame.mixer.music.play()
    time.sleep(50)
    pygame.mixer.music.stop()
```
## 3、相关阅读
- []()
- []()
- []()
- [年轻人只想要退休，是多么悲哀的事](https://mp.weixin.qq.com/s/J3il8mIYyeKsh5GHepkLBA)


<p align="center" id='1w副业-banner'>
    <a target="_blank" href='http://t.cn/A6KiaiqK'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F1w-pro.jpg" width="100%"/>
    </a>   
</p>

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。