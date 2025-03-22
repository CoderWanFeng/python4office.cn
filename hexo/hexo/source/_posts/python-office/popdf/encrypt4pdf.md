---
title: 加密100个小姐姐的PDF文档，1行代码搞定，网友：快男！
date: 2023-04-05 16:21:06
tags: 自动化办公
---


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


---

![](https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)