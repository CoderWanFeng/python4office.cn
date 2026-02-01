---
title: 用Python自动生成图文并茂的数据分析报告
date: 2022-08-08 09:44:27
tags: 自动化办公
---



<p align="center" id='支付宝-banner'>
    <a target="_blank" href='http://www.python4office.cn/fuli/zhifubao-0923/'>
    <img src="https://ads-1300615378.cos.ap-guangzhou.myqcloud.com/alipay/hong-3.jpg" width="100%"/>
    </a>   
</p>


<p align="center" id='外卖-banner'>
    <a target="_blank" href='https://kzurl19.cn/7CAHjq'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F%E5%A4%96%E5%8D%96-1040-100.jpg" width="100%"/>
    </a>   
</p>

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。

最近Python星球里的一位朋友私信我，想学习一下Python自动化生成数据分析报告。

作为[有问必答的知识星球](http://www.python4office.cn/wechat-group/)，今天我们来一起学习一下~
> reportlab是Python的一个标准库，可以画图、画表格、编辑文字，最后可以输出PDF格式。它的逻辑和编辑一个word文档或者PPT很像。有两种方法：

1. 建立一个空白文档，然后在上面写文字、画图等；
2. 建立一个空白list，以填充表格的形式插入各种文本框、图片等，最后生成PDF文档。

因为需要产生一份给用户看的报告，里面需要插入图片、表格等，所以采用的是第二种方法。

获取本文**全套源代码 + 字体 + 报告全文**，请关注下方公众号后，在后台发送：**报告自动化**，即可24小时自动获取~


## 1、一行命令，安装这个库
reportlab输入Python的第三方库，使用前需要先安装，

为了方便大家使用，我已经将这个库集成到[Python自动化办公的专用库：python-office](https://mp.weixin.qq.com/s/QhaUoB7Q4CJHR29uD6JSHQ)中了，

因此**一行命令**就可以完成的安装命令如下👇

```python
pip install -i https://mirrors.aliyun.com/pypi/simple python-office -U
```
## 2、核心代码模块导入
#### ①提前导入相关内容，并且注册字体。（注册字体前需要先准备好字体文件）
```python
from reportlab.pdfbase import pdfmetrics   # 注册字体
from reportlab.pdfbase.ttfonts import TTFont # 字体类
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Image  # 报告内容相关类
from reportlab.lib.pagesizes import letter  # 页面的标志尺寸(8.5*inch, 11*inch)
from reportlab.lib.styles import getSampleStyleSheet  # 文本样式
from reportlab.lib import colors  # 颜色模块
from reportlab.graphics.charts.barcharts import VerticalBarChart  # 图表类
from reportlab.graphics.charts.legends import Legend  # 图例类
from reportlab.graphics.shapes import Drawing  # 绘图工具
from reportlab.lib.units import cm  # 单位：cm
```
#### ②注册字体
提前准备好字体文件, 如果同一个文件需要多种字体可以注册多个
```python
pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))
封装不同内容对应的函数
创建一个Graphs类，通过不同的静态方法提供不同的报告内容，包括：标题、普通段落、图片、表格和图表。函数中的相关数据目前绝大多数都是固定值，可以根据情况自行设置成相关参数。
# Graphs类的全部内容，见后台获取的源代码。获取方式，见文末。
```

#### ③生成报告
```python
if __name__ == '__main__':  
    # 创建内容对应的空列表  
    content = list()  
    
    # 添加标题   
    content.append(Graphs.draw_title('数据分析就业薪资'))   
    
    # 添加图片   
    content.append(Graphs.draw_img('资料全集.jpg'))  
    
    # 添加段落文字  
    content.append(Graphs.draw_text('众所周知，大数据分析师岗位是香饽饽，近几年数据分析热席卷了整个互联网行业，与数据分析的相关的岗位招聘、培训数不胜数。很多人前赴后继，想要参与到这波红利当中。那么数据分析师就业前景到底怎么样呢？需要学习Python + 大数据分析，可以添加我的微信：python-office'))   
    
    # 添加小标题  
    content.append(Graphs.draw_title(''))  
    content.append(Graphs.draw_little_title('不同级别的平均薪资'))   
    
    # 添加表格   
    data = [    
        ('职位名称', '平均薪资', '较上年增长率'),    
        ('数据分析师', '18.5K', '25%'),     
        ('高级数据分析师', '25.5K', '14%'),    
        ('资深数据分析师', '29.3K', '10%') 
    ]  
    content.append(Graphs.draw_table(*data)) 
    
    # 生成图表  
    content.append(Graphs.draw_title(''))  
    content.append(Graphs.draw_little_title('热门城市的就业情况'))  
    b_data = [(25400, 12900, 20100, 20300, 20300, 17400), (15800, 9700, 12982, 9283, 13900, 7623)]  
    ax_data = ['BeiJing', 'ChengDu', 'ShenZhen', 'ShangHai', 'HangZhou', 'NanJing'] 
    leg_items = [(colors.red, '平均薪资'), (colors.green, '招聘量')]   
    content.append(Graphs.draw_bar(b_data, ax_data, leg_items))  
    
    # 生成pdf文件   
    doc = SimpleDocTemplate('report.pdf', pagesize=letter)  
    doc.build(content)
```
**生成报告的结果如下**

发

---
获取本文**全套源代码 + 字体 + 报告全文**，请关注下方公众号后，在后台发送：**报告自动化**，即可24小时自动获取~



## 相关阅读

- [给小白的《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](http://www.python4office.cn/course/AI%E7%9B%B8%E5%85%B3/AI%E7%BC%96%E7%A8%8B%E8%AE%AD%E7%BB%83%E8%90%A5/ads/260111-30%E8%AE%B2-599/)就能上手做AI项目。