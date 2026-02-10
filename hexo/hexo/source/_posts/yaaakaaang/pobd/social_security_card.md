---
title: 用AI自动识别社保卡，让数据处理更高效！
date: 2025-05-09 10:32:40
tags: [pobd]
---



<span style="font-size:20px;"><span style="color:#66a3e0;">在上次分享的发票识别工具之后，许多用户反馈希望能够扩展功能，支持其他类型证件的识别，比如社保卡。社保卡作为重要的个人信息载体，其识别和处理同样是一项繁琐的任务。为了满足这一需求，我开发了一个基于AI的自动识别社保卡工具，可以将社保卡信息自动识别并保存为Excel文件，进一步提升数据处理的效率。
 </span></span>
 
 
#  一、📍 基于百度OCR接口开发


我继续利用百度OCR接口，开发了一个能够自动识别社保卡信息的工具。通过这个工具，用户只需上传社保卡图片，系统就能自动提取社保卡中的关键信息，如姓名、身份证号、社保卡号等，并将这些信息保存为Excel文件，方便后续管理和使用。


#  二、📍 技术实现方案
仍然是调用一行代码，就可以实现识别社保卡上的所有信息，并且生成excel 表格
```
pobd.ocr2excel.social_security_card(img_path=input_file,output_excel_path=output_file,api_key=api_key,secret_key=secret_key)
```

如果你感兴趣是怎么实现的，那么下面这段核心代码的你一定要看看。
```    
	base64_image = self.image_to_base64(img_path)
    request_url = f"https://aip.baidubce.com/rest/2.0/ocr/v1/social_security_card?access_token={self.access_token}"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        "image": base64_image
    }
    response = requests.post(request_url, headers=headers, data=data)
    return response.json()
   
   ```

#  三、📍 效果展示
![](https://raw.atomgit.com/yaaakaaang/pic/raw/main/1746688217942.jpg)

当然，我也把这个功能加进了exe的小程序里，感兴趣的话，请在评论区留言，我会尽快将发送给你。

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。