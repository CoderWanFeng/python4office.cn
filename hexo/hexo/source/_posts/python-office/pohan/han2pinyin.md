---
title: 老大给了个新需求：如何将汉字转换成拼音字母？1行Python代码搞定！
date: 2023-06-24 23:51:25
tags: 开源
---




![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pohan/02-han2pinyin/cover.jpg)

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，小红薯也叫这个名。读者群👉[点我直达](http://www.python4office.cn/wechat-group/)。

之前的视频给大家分享了：中文编程，一行代码实现。

今天给大家分享一下，**如何通过1行Python代码，实现汉语转拼音**。

<!-- more -->

## 1、先上代码

实现汉语转拼音效果的第三方库是：``pohan``，免费下载&安装命令如下：

```
pip install pohan
```

1行代码，实现汉语转拼音的效果。
```
# pip install pohan
import pohan
from pohan.pinyin.pinyin import Style

# 不带声调的
pinyin_list = pohan.pinyin.han2pinyin("程序员晚枫", style=Style.NORMAL)
print(f'我是不带声调的结果：{pinyin_list}')

# 带声调的
pinyin_list = pohan.pinyin.han2pinyin("程序员晚枫", style=Style.TONE)
print(f'我是带声调的结果：{pinyin_list}')


# 带数字声调的
pinyin_list = pohan.pinyin.han2pinyin("程序员晚枫", style=Style.TONE3)
print(f'我是带数字声调的结果：{pinyin_list}')

```

以上代码运行的结果，如下图所示：

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/pohan/02-han2pinyin/res.jpg?q-sign-algorithm=sha1&q-ak=AKIDH3KlaLFcC6-CwRoisJT6b8yBYt_VtvRLwCfOBJPV-JHlPP-mdK3-HhV_Ul9KT4y-&q-sign-time=1687539502;1687543102&q-key-time=1687539502;1687543102&q-header-list=host&q-url-param-list=ci-process&q-signature=14fee479eb299ed0be0c3db83114d31bcf8394fb&x-cos-security-token=cyG3a0nxD1bakr3wu10UTNYxYLIKLpza10eea011fc039f423deaeacb0383e0acW8IleUcwWZFZICbh7Lr9nnSBDbnsEspiJdOZuRtehUCTx9Q7sR2eqk8v36Dwbt-aknvIn1759UnRpGmAnfnPcbQm0ofRWWXjH3fW9sV1o4IQMNlZcwNBpSFVi-XD0rrR-OM0Absm-Qc77FRjO6NwgQvZE2VJxx1f2ALXJ3V6xxHtgKSYgxSYzfSnHouIMWW1&ci-process=originImage)

## 2、参数说明

1行代码实现功能，可以填入的参数有以下几个（小白可以不填，都有默认值）：

- hans (unicode 字符串或字符串列表) – 汉字字符串( '程序员晚枫' )或列表( ['程序员', '晚枫'] ). 可以使用自己喜爱的分词模块对字符串进行分词处理,
  只需将经过分词处理的字符串列表传进来就可以了。

- style: 指定拼音风格，默认是 TONE 风格。 更多拼音风格详见 Style

- errors: 指定如何处理没有拼音的字符。详见 处理不包含拼音的字符

- default: 保留原始字符

- ignore: 忽略该字符

- replace: 替换为去掉 \u 的 unicode 编码字符串 ('\u90aa' => '90aa')

- callable 对象: 回调函数之类的可调用对象。

- heteronym: 是否启用多音字

- strict: 只获取声母或只获取韵母相关拼音风格的返回结果 是否严格遵照《汉语拼音方案》来处理声母和韵母， 详见 strict 参数的影响

- v_to_u (bool): 无声调相关拼音风格下的结果是否使用 ü 代替原来的 v 当为 False 时结果中将使用 v 表示 ü

- neutral_tone_with_five (bool): 声调使用数字表示的相关拼音风格下的结果是否 使用 5 标识轻声

以上参数中，最常使用的是``style``，使用方法，见上面的代码。


---






---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。