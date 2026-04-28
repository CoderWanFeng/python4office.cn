---
title: 新功能！百度OCR可以识别离婚证了！
date: 2025-04-26 14:15:17
tags: [pobd]
---

<!-- more -->
<span style="font-size:20px;"><span style="color:#66a3e0;">哈喽啊，不知道你们发现没有，百度又有新功能了。话不多说，上图！ </span></span>
![community_de705ef.png](https://raw.atomgit.com/user-images/assets/5027920/bfd0034d-7009-415c-892f-fc6dcc5c2f45/community_de705ef.png)

我们从长期趋势来看，很多国家和地区的离婚率越来越高，对应的也加重了我们的工作量。辣么有没有什么办法可以帮助我们从冗杂的工作中解放出来呢？     	**答案是有滴！** 

#  一、1行黑科技
## 📍 1.1 安装库
> 【pobd】库是基于百度的API实现各种证件识别并且生成Excel文件的Python库。
```python
pip install pobd
```

## 📍 1.2 1行代码
```python

pobd.ocr2excel.divorce_certificate(img_path=input_file, output_excel_path=output_file,  api_key=api_key,  secret_key=secret_key)
```
只需这2步，就可以轻松解决这个问题啦！而我们的老朋友 api_key 和 secret_key ，不知道怎么申请的伙伴们，留言区见！


#  二、爱提问的朋友就要问了：How ？
<span style="color:#66a3e0;"><ins> *1、调接口*</ins></span>
```        self.access_token = self.get_token()
        base64_image = self.image_to_base64(img_path)
        request_url = f"https://aip.baidubce.com/rest/2.0/ocr/v1/divorce_certificate?access_token={self.access_token}"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            "image": base64_image
        }
        response = requests.post(request_url, headers=headers, data=data)
        return response.json()
```
就会得到像这样的数据
```{
  "words_result": {
    "姓名_男": [{"word": "王帆"}],
    "姓名_女": [{"word": "杨丹"}],
    "登记日期": [{"word": "2021年10月25日"}],
    ...
  }
}

```

<span style="color:#66a3e0;"><ins> *2、洗数据*</ins></span>
```data = {
    "姓名_男": res['words_result'].get("姓名_男", [{}])[0].get("word", ""),
    "姓名_女": res['words_result'].get("姓名_女", [{}])[0].get("word", ""),
    "登记日期": res['words_result'].get("登记日期", [{}])[0].get("word", ""),
    ...
}

```
结构化提取字段 → 转成 DataFrame

<span style="color:#66a3e0;"><ins> *3.成表格*</ins></span>
```df = pd.DataFrame([data])
df.to_excel('离婚证信息.xlsx', index=False)

```
以上，就完成工作啦。

![11c61c8.jpeg](https://raw.atomgit.com/user-images/assets/5027920/d744769a-6c9b-4c8a-99f3-2d165ab5f6e9/11c61c8.jpeg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


程序员晚枫专注AI编程培训，小白看完他和图灵社区合作的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)就能上手做AI项目。


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)

