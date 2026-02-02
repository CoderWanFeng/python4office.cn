---
title: 手动识别 PDF发票太慢？用这个方法让速度提高 50 倍！
date: 2025-04-15 21:56:17
tags: 码匠er
---


> 大家好，我是`码匠er`。你是否遇到过处理几十页甚至更多的发票信息，既容易出错又速度慢，月底处理公司发票，老板一直催~

别愁了！这次 【potx-cloud】新版本让你体验黑科技，只需喝杯茶就可以很快处理几百页的发票文件！

# 1. 3行代码体验黑科技

你可能会想，现在变的这么厉害，我会不会很难用？优化后的接口依然保持简单，只需要3行代码就可以体验最新黑科技哦！

```
# pip install potx_cloud

import potx_cloud

potx_cloud.ocr2excel.VatInvoiceOCR2Excel(input_path='./test.pdf', output_path='./', id=SecretId, key=SecretKey)
```

只需上面三行代码，你就能享受`速度与激情`!

`SecretId`和`SecretKey`是腾讯API接口的`钥匙`，不知道怎么申请的可以留言找我哦！

# 2. 探寻问题根源

有用户使用【potx-cloud】库处理发票的过程中，发现有个PDF处理了接近一分钟才有结果，就反馈给我，我拿到他的PDF文件后，一看才25页啊，我测试了下，足足处理了44s，我都傻眼了！

![](https://cdn.jsdelivr.net/gh/wzllby/pic/img/202504152157952.jpg)

> 对于我这种技术人员，性能问题还是比较害怕的，毕竟不像错误那样有详细的日志打印~

经过漫长的定位，我发现在PDF处理的过程中，由于腾讯的每个接口每次处理的页数是不一致的，我们的代码是使用串行处理方式——将PDF的每一页分割发给腾讯API接口处理，然后腾讯API返回结果之后再处理下一页，导致当文件过大时，处理速度大大降低。

# 3. 优化结果

> 我们要怎么才能加快处理速度呢？我想到了`多线程技术`，你可能又想问了，什么是多线程呢？很简单：让「一个人搬砖」变成「一群人同时搬砖」

我使用一下几行代码就解决了这个问题。
```
semaphore = threading.Semaphore(get_max_concurrent_nums(OCR_NAME))
        with pymupdf.open(file_path) as pdf:
            # 使用线程池并行处理页面
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(process_pdf_page, OCR_NAME, pdf, page_num, ocr, semaphore)
                    for page_num in range(len(pdf))
                ]
                all_results = [future.result() for future in concurrent.futures.as_completed(futures)]
                
def process_pdf_page(OCR_NAME, pdf, page_num, ocr, semaphore):
    # 根据腾讯云官网每个接口的最大qps限制线程数量
    with semaphore:
        pdf_bytes = pdf.convert_to_pdf(page_num, page_num + 1)
        base64_encoded_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        return ocr.DoOCR(OCR_NAME, ImageBase64=base64_encoded_pdf, IsPdf=True)
```

优化完之后，我再用上面的PDF测试，发现只需要5s，整整提升了6倍。

![](https://cdn.jsdelivr.net/gh/wzllby/pic/img/202504152157997.jpg)

大家快来体验吧！

# 4. 最后

如果你还在为发票 PDF 处理速度发愁，赶紧试试这次的优化版本 ——让工具帮你「加速」！

> 对了，如果你觉得这次优化有点东西，记得「点赞 + 在看」，让更多做发票处理的小伙伴看到这个库～ 咱们下次更新见！有问题添加下二维码。

![](https://cdn.jsdelivr.net/gh/wzllby/pic/img/202504152157373.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)就能上手做AI项目。