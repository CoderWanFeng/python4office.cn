---
title: 加密100个小姐姐的PDF文档，1行代码搞定，网友：快男！
date: 2023-04-05 16:21:06
tags: 自动化办公
---

<p align="center">
  <a target="_blank" href='https://github.com/CoderWanFeng/popdf'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/popdf.svg?style=social" alt="github star"/>
    </a>
        <a target="_blank" href='https://gitcode.com/python4office/popdf'>
		<img src='https://gitcode.com/python4office/popdf/star/badge.svg?theme=dark' alt='gitcode star'/>
	</a>
 <a target="_blank" href='https://github.com/CoderWanFeng/popdf'>
<img src="https://static.pepy.tech/badge/popdf" alt="PyPI Downloads">
</a>
</p>


大家好，这里是程序员晚枫，今天给大家分享一个PDF的搞笑技能：**1行代码，批量给PDF加密。**

别人拿到加密的PDF开心不开心我不知道，反正你肯定开心了。

## 1、上代码

下载Python自动化办公的专用库：python-office，下载命令如下。

```python
pip install python-office -i https://pypi.python.org/simple -U
```
注意，最近清华镜像和阿里镜像都不怎么更新国外源了，不知道是什么原因。

所以，建议大家在条件允许的情况下，**像上面的代码那样，使用国外源来下载第三方库，才是最新版~**
```
# pip install python-office 一定要成功哦~
import office

office.pdf.encrypt4pdf(path=r'D:\程序员晚枫的文件夹\input_pdf',
                       password='程序员晚枫的密码',
                       output_path=r'D:\程序员晚枫的文件夹\output_pdf')
                      
```

## 2、使用说明

有以下几点使用技巧：
- path：可以填单个文件，也可以填一个路径，会自动搜索路径下所有pdf文件，包括子文件夹里的。

- 有加密就有解密。需要批量解密功能，请点赞本文后，在留言区告诉我~

- 进阶功能：有些朋友想根据文件名筛选pdf文档，或者更高阶的想通过正则来筛选。



----



## 加入开源

如果你喜欢以上这些开源项目，欢迎加入我们的开源小组，一起交流学习，一起进步。

> 加我的微信：hdylw1024，备注：开源

关于项目的介绍：

- GitCode：[DeepSeek浪潮下如何撑过35岁职场危机？跨界程序员：我不焦虑，40岁就退休｜CodeMaster#3](https://mp.weixin.qq.com/s/RC54o9C4F87fyAebJUE0kg)
- Python中国大会：[非程序员如何学习和使用 Python-程序员晚枫-科技博主&开源作者](https://www.bilibili.com/video/BV1Y6qWYWEyQ/?spm_id_from=333.1387.homepage.video_card.click&vd_source=ca20bb8763fcb18660aa74d7a87234fa)
- Pypi：[python-office](https://pypi.org/project/python-office/)
- 官网：[python-office.com](https://python-office.com)
- 开源中国：[Python-office Python 自动化办公库](https://www.oschina.net/p/python-office)
- B站视频教程：[官网发布：python-office库 | 专为Python自动化办公而生，一行代码提高办公效率 | 哪里不会点哪里，再也不用学习Python编程](https://www.bilibili.com/video/BV1pT4y1k7FH/?spm_id_from=333.1387.0.0&vd_source=ca20bb8763fcb18660aa74d7a87234fa)



<p align="center" id='CodeMaster-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/B9OOU5bb8fOd9KiG43GqAw'>
    <img src="https://cos.python-office.com/activity/CodeMaster-3.jpg" width="100%"/>
    </a>   
</p>

---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)