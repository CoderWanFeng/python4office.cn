---
title: 告别手动录入！AI自动识别发票
date: 2025-05-8 11:15:32
tags: [pobd]
---

<span style="font-size:20px;"><span style="color:#66a3e0;">最近有朋友向我吐槽："每天对着几十张发票手动录入系统，眼睛都快看花了，还总担心数字打错。" 这种重复性高、容错率低的工作，确实让财务和行政人员苦不堪言。作为程序员，我深知这类场景完全可以通过技术手段优化。 </span></span>

#  一、解决方案：AI+OCR智能发票处理
## 📍 基于百度OCR接口开发

我利用百度OCR接口，开发了一个能够自动识别发票信息的工具。通过这个工具，用户只需上传发票图片，系统就能自动提取发票中的关键信息，如发票号码、金额、日期等，并将这些信息保存为Excel文件，方便后续管理和分析。
而且调用百度OCR每日都有免费的额度，这意味着你可以免费使用这个工具进行发票识别。对于大多数个人用户和小型企业来说，这个免费额度已经足够日常使用。

#  二、技术实现方案
## 📍 源代码免费提供

为了让更多人受益，我将这个工具的源代码免费开源，并托管在atomgit上。你可以访问以下链接获取源代码
[https://atomgit.com/python4office/pobd](url)

## 📍 一行代码实现功能
为了让不懂代码的朋友也能轻松使用，我将功能都封装到了一行代码里。你把源代码下载下来后，只需要调用下面这行代码，就可以实现识别发票，并保存为excel表格。

这行代码在文件  pobd\exmaples\course\code\11_vat_invoice.py  里。

```        
       pobd.ocr2excel.vat_invoice(img_path=input_file, output_excel_path=output_file,  app_id=app_id, api_key=api_key,  secret_key=secret_key)

```
input_file 就是你存放增值税发票的目录， output_file 是生成excel表格的目录。 

而 <span style="color:#e60000;">app_id、api_key、secret_key </span>的获取方法，可以留言区联系我，也可以访问参考文档 [https://blog.csdn.net/2301_81016982/article/details/147276083?spm=1001.2014.3001.5502](url)

## 📍 效果展示
发票上的信息几乎都能识别，这里只截图了一部分。
![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1746678968379(1).jpg)

#  三、零代码方案（exe小程序）
如果你觉得这样还是不得劲，我还开发了一个exe版的小程序。你可以直接下载并运行这个程序，无需安装任何额外的软件。

如果你也受困于发票录入工作，不妨试试这个方案。技术本应服务于人，让AI帮我们完成这些机械劳动，把时间留给更有价值的工作吧！

感兴趣的话，请在评论区留言，我会尽快将发送给你。


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。