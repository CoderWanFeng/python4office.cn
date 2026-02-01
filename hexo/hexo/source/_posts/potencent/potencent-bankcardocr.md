---
title: 腾讯云+Pandas，批量识别银行卡号码并且写入Excel，小白也可以轻松使用
date: 2023-01-25 22:14:07
tags:
---

腾讯云+Pandas，批量识别银行卡号码并且写入Excel，小白也可以轻松使用

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/potencent%2FBankCardOCR%2Fcover.jpg)

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，
昨天我们学习了：[实战案例！用1行Python代码识别增值税发票，然后将数据自动录入系统](https://mp.weixin.qq.com/s/agsF8ttwxOiZyizsTKBxMQ)。

今天我们继续学习Python自动化办公：每次有新员工入职，都要收集大量的工资卡信息，并且生成Excel文档，能不能用Python**准确、快速**地解决呢？

今天我们就来学习一下，如何**用1行代码，自动识别银行卡信息并且自动生成Excel文件**~

![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/potencent%2FBankCardOCR%2FSnipaste_2023-01-26_07-37-32.jpg)

## 第一步：识别一张银行卡

识别银行卡的代码最简单，只需要1行腾讯云AI的第三方库``potencent``的代码，如下所示。左右滑动，查看全部。👇

```python
# pip install potencent
import potencent

# 可以填写本地图片的地址：img_path，也可以填写在线图片的地址：img_url
# 如果2个都填，则只用在线图片
res = potencent.ocr.BankCardOCR(
            img_path=r'C:\Users\程序员晚枫的文件夹\银行卡图片',
            img_url='https://wanfeng-156569856.cos.ap-beijing.myqcloud.com/bank_card.jpg',
            configPath=r'配置文件的信息，可以不填，默认是同级目录下的potencent-config.toml')

print(res)
```

识别后的返回结果，几乎涵盖所有银行卡上肉眼可见的内容。👇
```shell
{
  "CardNo": "621700888888888889",
  "BankInfo": "建设银行(01050000)",
  "ValidDate": "08/2026",
  "CardType": "借记卡",
  "CardName": "龙卡通",
  "RequestId": "86b70007-3ef5-4b7e-8685-556b0a7df1c9"
}
```
支持对中国大陆主流银行卡正反面关键字段的检测与识别，包括卡号、卡类型、卡名字、银行信息、有效期。支持竖排异形卡识别、多角度旋转图片识别。支持对复印件、翻拍件、边框遮挡的银行卡进行告警，可应用于各种银行卡信息有效性校验场景，如金融行业身份认证、第三方支付绑卡等场景。

以上代码中，关于``potencent-config.toml``的配置方法，可以参考昨天视频的讲解👇

的



## 第二步：写入Excel

想把上面这个代码用来识别大量银行卡信息，并且将识别后的返回数据，全部写入Excel文件，可以直接使用之前推荐过的``30讲 Python + Excel自动化办公``，传送门：[点我直达](https://mp.weixin.qq.com/s/waAgnrK_RFIQnUss998vnA)

代码如下👇。


```python
import os
from os.path import join
import pandas as pd

# home_path = "你存放大量银行卡图片的位置"
home_path = r"C:\Users\Lenovo\Desktop\temp\test\card"
res_df = pd.DataFrame()
for (root, dirs, files) in os.walk(home_path):
    for file in files:
        single_res = potencent.ocr.BankCardOCR(img_path=join(root, file))
        single_res = json.loads(single_res.to_json_string())
        line_df = pd.DataFrame(single_res, index=[0])
        print(line_df)
        res_df = res_df.append(other=line_df)
print(res_df)
res_df.to_excel(r"./银行卡信息（程序员晚枫）.xlsx")
```

运行后的结果如下，会在同级目录下，生成一个Excel文件
![](https://article-1300615378.cos.ap-nanjing.myqcloud.com/potencent%2FBankCardOCR%2FSnipaste_2023-01-26_07-39-05.jpg)

## 第三步：优化思路

以上代码还可以进一步优化，例如：
- 路径处理改为Path方法，适配更多的平台
- 变量名称更简洁
-index改为序号

但优化的前提是程序能运行成功，赶紧去跑起来吧~

---

大家在阅读本文和使用代码中有任何问题，欢迎在评论区进行交流~

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。