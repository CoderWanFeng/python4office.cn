---
title: 性能优化必备！深入掌握Python性能分析神器cProfile
date: 2024-11-11 00:41:49
tags: [第三方库,pip]
---


<p align="center" id='腾讯云-banner'>
    <a target="_blank" href='https://curl.qcloud.com/3csDz9jU'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F1040x100-tencent.jpg" width="100%"/>
    </a>   
</p>

> 这是专栏[优秀的第三方库](http://www.python4office.cn/course/%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93/all/)的第7篇原创文章。

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。
poocr是一个具有OCR功能的Python第三方库，支持识别100多种场景下的文字识别，例如发票、驾驶证、身份证等。以下是使用poocr的基本步骤：

## **安装poocr库**

在终端或命令提示符中运行以下命令来安装poocr库：
```
pip install poocr
```
   

## **配置腾讯AI的id和key**


使用poocr库之前，需要配置腾讯AI的id和key。每个人都有1000次的免费额度。可以在腾讯云控制台获取这些信息：

![](https://ads-1300615378.cos.ap-guangzhou.myqcloud.com/%E8%85%BE%E8%AE%AF%E4%BA%91/ocr.jpg)


## **使用poocr进行OCR识别**

安装并配置好之后，就可以使用poocr进行OCR识别了。以下是一些示例代码：

     

- **识别发票并保存为Excel**

```
import poocr
poocr.ocr2excel.VatInvoiceOCR2Excel(input_path='发票图片路径',
                                output_excel='输出Excel文件路径',
                                configPath='poocr配置文件路径')
```
     

- **识别PDF格式的发票**
```
import poocr
SecretId = '你的腾讯云SecretId'
SecretKey = '你的腾讯云SecretKey'
pdf_path = 'PDF发票文件夹路径'
poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=pdf_path, id=SecretId, key=SecretKey, file_name=True)
```


这些步骤和代码示例应该能帮助你开始使用poocr进行OCR识别。更多详细的使用案例和功能介绍，可以查看poocr的官方文档和教程。


![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')



## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。