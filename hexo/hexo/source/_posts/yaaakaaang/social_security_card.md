---
title: 识别社保卡信息，手动整理效率低，OCR 和 Python 来帮你！
date: 2025-04-15 21:56:17
tags: [pobd]
---

<span style="font-size:20px;"><span style="color:#66a3e0;">你是否曾因社保卡，一头变得两个大。现在不用再愁啦，一行代码解决它。【pobd】 你的办公好帮手。</span></span>




#  一、1行代码，体验魔法

`pobd.ocr2excel.social_security_card(img_path=input_file,output_excel_path=output_file,api_key=api_key,secret_key=secret_key)`

只需要上面这行代码，就能实现识别社保卡信息 + 生成excel 表格。不知道怎么申请百度API接口的 <span style="color:#66a3e0;">api_key</span> 和 <span style="color:#66a3e0;">secret_key</span> 的伙伴们，可以留言找我哦！

它是怎么做到的呢，接下来让我们揭开它神秘面纱吧。

# 二、抽丝剥茧，探寻根源

<span style="color:#66a3e0;"><ins> *1、首先我们选用的是 百度OCR接口**</ins></span>
`       

        base64_image = self.image_to_base64(img_path)
        request_url = f"https://aip.baidubce.com/rest/2.0/ocr/v1/social_security_card?access_token={self.access_token}"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            "image": base64_image
        }
        response = requests.post(request_url, headers=headers, data=data)
        return response.json()`
        
        

        
response 就是我们想要得到的信息了。不过现在得到的信息还比较混杂，需要进一步处理。        

<span style="color:#66a3e0;"> <ins>*2、使用pandas 组织数据**</ins></span>

`        df = pd.DataFrame(result_df)`

df 就是使用pandas 把数据转换为 DataFrame。这样得到的信息不仅清晰，而且还有一个用处，那就是...

<span style="color:#66a3e0;"><ins> *3、存为 excel 表格**</ins></span>

`s_output_excel), index=False, engine='openpyxl')`

有了 DataFrame ，我们就能很轻易的写入 excel 表格了。

# 三、效果展示

我们还使用了进度条，可以实时了解工作进度。

![community_476e8db.png](https://raw.atomgit.com/user-images/assets/5027920/551c6205-a1d7-47e4-a7af-0d72ec891cab/community_476e8db.png 'community_476e8db.png')

最后，就是我们的excel 表格展示啦。

![community_5e2bc74.png](https://raw.atomgit.com/user-images/assets/5027920/ae4f58bd-ed88-48c7-9420-cd132c5d74b9/community_5e2bc74.png 'community_5e2bc74.png')

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/uxCILtn9cfIsJR8PqOxlGQ)就能上手做AI项目。