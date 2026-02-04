---
title: pipreqs：快速准确生成当前项目的requirements.txt，还有和freeze的对比
date: 2024-11-10 00:41:49
tags: [第三方库,pip]
---


<p align="center" id='腾讯云-banner'>
    <a target="_blank" href='https://curl.qcloud.com/3csDz9jU'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F1040x100-tencent.jpg" width="100%"/>
    </a>   
</p>

> 这是专栏[优秀的第三方库](http://www.python4office.cn/course/%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93/all/)的第1篇原创文章。

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。

今天给大家推荐一个快速生成``requirements.txt``的小工具：``pipreqs``。

## 什么是requirements.txt？

我们在开发Python项目的时候，需要用到``requirements.txt``来管理项目中使用的第三方库。

当我们把项目部署到一个没有第三方库的新环境，我们可以通过``pip install -r requirements.txt``来重新下载这些第三方库。

例如下面这个就是``python-office``的``requirements.txt``内容。


```shell
alive_progress==3.1.5
auto_mix_prep==0.2.0
Faker==25.2.0
moviepy==1.0.3
numpy==1.26.4
openpyxl==3.1.2
pandas==2.2.2
pdf2image==1.17.0
Pillow==10.3.0
pocode==0.0.3
poemail==0.0.3
pypandoc==1.13
PyPDF2==3.0.1
PyQt5==5.15.10
pytest==8.2.1
pywifi==1.1.12
pywin32==306
qt_material==2.14
reportlab==4.2.0
Requests==2.32.2
search4file==0.1.15
setuptools==69.0.2
tqdm==4.66.4
typer==0.12.3
wftools==0.0.9
xlrd==1.2.0
xlwt==1.3.0
```

## 如何生成requirements.txt？

常见的工具有：`pipreqs` 和 `pip freeze` 两种，它们在Python项目中用于管理依赖关系，但它们的用途和工作方式有所不同。

简单来说：

- 生成当前项目的requirements.txt，用pipreqs
- 生成当前环境的requirements.txt，用pip freeze

以下是它们的详细比较：

### pipreqs
- **用途**：`pipreqs` 是一个从项目代码中自动生成 `requirements.txt` 文件的工具。它分析项目中的Python文件，找出导入的模块，并生成一个包含这些模块及其对应版本的列表。
- **工作方式**：`pipreqs` 通过扫描项目目录中的Python文件，识别出项目实际使用的库，然后生成一个 `requirements.txt` 文件，这个文件只包含项目代码中用到的库。
- **优点**：
  - 只包含项目实际使用的库，避免包含不必要的依赖。
  - 可以忽略某些目录或文件，提高生成依赖列表的精确度。
  - 支持Jupyter Notebook，能够识别Notebook中的依赖。
- **缺点**：
  - 需要手动运行，不会自动更新 `requirements.txt` 文件。
  - 可能不会识别出所有间接依赖。

### pip freeze
- **用途**：`pip freeze` 是一个列出当前环境中所有已安装的Python包及其确切版本的命令。
- **工作方式**：`pip freeze` 会列出当前虚拟环境中安装的所有包，包括那些不是由项目直接依赖的包（例如，某些包的依赖）。
- **优点**：
  - 快速列出当前环境中所有已安装的包。
  - 可以用于确保在不同环境中重现相同的环境配置。
- **缺点**：
  - 包含所有环境包，可能会包含项目不需要的依赖。
  - 不能识别项目中未使用的包。

### 总结
- **项目依赖管理**：如果你需要一个精确的项目依赖列表，只包含项目实际使用的库，`pipreqs` 是更好的选择。
- **环境复制**：如果你需要复制整个Python环境，包括所有包及其版本，`pip freeze` 是更合适的工具。
- **自动化与手动**：`pipreqs` 需要手动运行以生成依赖列表，而 `pip freeze` 只需在环境中运行即可列出所有包。

总的来说，`pipreqs` 更适合用于项目开发阶段，生成精确的依赖列表，而 `pip freeze` 更适合用于环境管理，确保环境的一致性。


> 大家在阅读过程中有任何问题，或者觉得有收获的话，欢迎点赞、评论和收藏。



![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')


## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。