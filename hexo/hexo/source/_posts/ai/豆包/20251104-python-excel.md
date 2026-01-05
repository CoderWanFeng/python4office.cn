---
title: Python处理Excel的5个“神仙库”，办公效率直接翻倍！
date: 2025-11-05 02:38:37
tags: 自动化办公
---



<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='http://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>




<p align="center" name="atomgit">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://mp.weixin.qq.com/s/7rH5U6s91hnTKCKZy4BHCg">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>



<div align="center">
    <a href="https://github.com/CoderWanFeng"> <img src="https://badgen.net/badge/Github/%E7%A8%8B%E5%BA%8F%E5%91%98?icon=github&color=red"></a>
    <a href="http://www.python4office.cn/account-display/"> <img src="https://badgen.net/badge/follow/%E5%85%AC%E4%BC%97%E5%8F%B7?icon=rss&color=green"></a>
    <a href="https://space.bilibili.com/259649365"> <img src="https://badgen.net/badge/pick/B%E7%AB%99?icon=dependabot&color=blue"></a>
    <a href="http://www.python4office.cn/wechat-group/"> <img src="https://badgen.net/badge/join/%E4%BA%A4%E6%B5%81%E7%BE%A4?icon=atom&color=yellow"></a>
</div>

![image.png](https://raw.atomgit.com/user-images/assets/5027920/4f517dd7-c189-4f62-b937-2e37aef2b96d/image.png 'image.png')


<!-- more -->

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/h0MExYJag6hLnQg26yx98w)。

还在手动录入Excel到深夜？百份表格批量改格式改到手腕发酸？跨表核对数据反复出错返工？打工人别硬扛了！Python里藏着5个处理Excel的“神仙库”——从基础读写、批量分析到格式美化，全场景覆盖，直接帮你省出2小时摸鱼时间！下面逐个拆解，按需捡走～

## 一、openpyxl：.xlsx处理的“入门首选”

openpyxl是Python处理Excel 2010+版本（.xlsx/.xlsm）的“入门界顶流”——纯Python开发，Windows、Mac、Linux都能用，API设计得清爽不绕弯，官方文档还带详细示例。新手花半小时跟着示例敲代码，就能搞定基础操作，日常办公的读写、改格式需求基本都能cover。

![image.png](https://raw.atomgit.com/user-images/assets/5027920/aa664ffc-bede-4660-a1a8-073cb8e83059/image.png 'image.png')

### 核心功能

基础操作全拿捏：创建/打开工作簿、工作表；轻松搞定单元格数据的读写和修改；字体（加粗、变色、调字号）、对齐方式、边框、背景色这些格式随便改；合并单元格、冻结窗格也能实现；还支持“读写模式优化”，打开大文件不卡顿。

### 优缺点

优点很实在：免费开源不花钱，跨平台不用挑电脑，新手看示例就会用，还不用装Microsoft Excel；优化后能扛大文件，处理几MB的表格也不卡。缺点也得提：只认.xlsx系列格式，老掉牙的.xls文件打不开；想做复杂图表的话，它就有点力不从心了。

### 适用场景

日常办公直接用：比如给程序员晚枫的员工信息表统一加表头颜色、加粗标题；批量更新表格里的固定字段（像全公司部门调整，一键改完）；或者简单读写.xlsx文件，替代手动复制粘贴。

### 安装与示例

安装超简单，命令行敲一行：`pip install openpyxl`

给新手整个“创建带格式表格”的实用示例，复制就能跑：

```python

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

# 新建工作簿和工作表
wb = Workbook()
ws = wb.active
ws.title = "程序员晚枫的员工信息表"  # 给工作表改个名

# 写表头+加样式（加粗白字+蓝色背景）
headers = ["姓名", "部门", "入职日期"]
for col, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col, value=header)
    cell.font = Font(bold=True, color="FFFFFF")  # 加粗白字
    cell.fill = PatternFill(start_color="4472C4", fill_type="solid")  # 蓝色背景

# 写数据
data = [["张三", "研发部", "2025-01-15"], ["李四", "市场部", "2025-02-20"]]
for row, row_data in enumerate(data, 2):  # 从第2行开始写数据
    for col, value in enumerate(row_data, 1):
        ws.cell(row=row, column=col, value=value)

# 保存文件（直接生成在当前文件夹）
wb.save("程序员晚枫的员工信息表.xlsx")
```

## 二、xlrd/xlwt：旧版.xls的“专属搭档”

xlrd和xlwt是处理“老古董”.xls文件的“黄金搭档”——分工超明确：xlrd负责读.xls数据，xlwt负责写.xls文件，再配个xlutils库，还能改已有.xls文件，完美解决旧格式兼容问题。重点提醒：xlrd 2.0以上版本不支持.xlsx，要处理旧文件得装1.2.0版本。

![image.png](https://raw.atomgit.com/user-images/assets/5027920/1a4ee732-8800-406c-bb78-2e656c2320c7/image.png 'image.png')

### 核心功能

核心能力精准匹配旧格式：xlrd能读.xls的工作表、单元格数据，还能算出行数列数，按需加载工作表省内存；xlwt能新建.xls，写数据时加基础格式（加粗、边框），合并单元格也能用；xlutils就是“粘合剂”，让xlrd读的内容能通过xlwt修改。

### 优缺点

优点就是“专”：专为.xls设计，老报表打开不乱码，兼容性拉满；体积小运行快，轻量不占资源。缺点也明显：xlrd不支持新格式.xlsx，xlwt写的文件最多只能放65536行（超了会报错）；高级格式和图表基本做不了，只能满足基础需求。

### 适用场景

适配场景很明确：公司整理历史档案，一堆2010年前的.xls报表要提取数据；批量汇总多个旧版销售报表的关键数据；生成不超过6万行的旧格式报表（比如给还在用老Excel的客户发文件）。

### 安装与示例

安装要指定xlrd版本，命令行敲：`pip install xlrd==1.2.0 xlwt xlutils`

最常用的“读旧版.xls”示例，复制即用：

```python

import xlrd

# 打开旧版.xls文件（路径换成自己的）
workbook = xlrd.open_workbook("旧版销售数据.xls")
# 取第一个工作表（也能按名字取：sheet_by_name("1月销售")）
worksheet = workbook.sheet_by_index(0)

# 读表头（第一行）
headers = [worksheet.cell_value(0, col) for col in range(worksheet.ncols)]
print("表头：", headers)

# 读所有数据行（跳过表头）
for row in range(1, worksheet.nrows):
    row_data = [worksheet.cell_value(row, col) for col in range(worksheet.ncols)]
    print(f"第{row}行数据：", row_data)
```

## 三、pandas：Excel数据处理的“效率王者”

pandas虽不是专门为Excel设计的，但处理Excel批量数据的能力，堪称办公界的“天花板”！它能用“DataFrame”表格格式加载Excel数据，筛选、排序、汇总都是秒级完成，再搭openpyxl或xlrd当“引擎”，新旧格式都能搞定。

![image.png](https://raw.atomgit.com/user-images/assets/5027920/af7adb77-7ee0-4462-a73d-a09f4efac457/image.png 'image.png')

### 核心功能

批量操作是强项：单份/多份Excel一键读取，还能指定读某张工作表；用DataFrame做数据筛选、去重、分组统计（比如按区域算销售额），甚至补缺失值；多表合并也轻松（比如把业绩表和考勤表按员工ID拼在一起）；处理完的数据直接写回Excel，还能分拆到不同工作表。

### 优缺点

优点太香了：批量数据处理速度飞起，一行代码搞定人工几小时的统计；多表合并、数据清洗这些复杂操作不用写循环；新旧格式都兼容。缺点也得接受：对Excel的格式（字体、颜色）控制很弱，想美化报表得换别的库；新手要先学下DataFrame的基础用法（不难，半小时入门）。

### 适用场景

办公场景高频用：月度销售数据汇总（按区域、产品统计）；十几份Excel报表合并去重（比如各门店的销售表汇总成全国表）；清洗数据（删除空行、修正错误格式）；生成数据透视表风格的统计结果（比Excel手动拖更灵活）。

### 安装与示例

安装要带引擎（处理.xlsx用openpyxl）：`pip install pandas openpyxl`

打工人最常用的“多表汇总”示例，超实用：

```python

import pandas as pd

# 要汇总的Excel文件列表（换成自己的文件名）
file_names = ["1月销售.xlsx", "2月销售.xlsx"]
# 批量读取所有文件并合并成一个表格
all_data = pd.concat([
    pd.read_excel(file, engine="openpyxl")  # 用openpyxl当引擎读.xlsx
    for file in file_names
])

# 按“区域”汇总“销售额”（表格要真有这两列哦）
sales_summary = all_data.groupby("区域")["销售额"].sum().reset_index()

# 写回新Excel，分两个工作表存
with pd.ExcelWriter("季度销售汇总.xlsx", engine="openpyxl") as writer:
    all_data.to_excel(writer, sheet_name="原始数据", index=False)  # 存原始数据
    sales_summary.to_excel(writer, sheet_name="区域汇总", index=False)  # 存汇总结果

print("汇总完成！直接打开‘季度销售汇总.xlsx’看结果～")
```

## 四、xlsxwriter：Excel格式美化的“颜值担当”

xlsxwriter是Excel“颜值担当”——虽然不能读Excel文件，但做格式美化和图表的能力拉满！单元格格式、条件格式、数据验证都能精细控制，还能做折线图、柱状图这些专业图表，生成的Excel报表堪比专业排版，拿去给老板汇报超有面。

![image.png](https://raw.atomgit.com/user-images/assets/5027920/98e756d5-c245-488c-b8ca-b2d957e92bdf/image.png 'image.png')

### 核心功能

美化能力拉满：字体、颜色、边框、背景色想怎么调就怎么调；条件格式超实用（比如销售额低于5万标红预警）；还能限制单元格输入（比如只能填数字）；生成的图表带标题、图例、数据标签，比Excel手动做的还规整；插入图片、超链接也没问题。

### 优缺点

优点就是“美且强”：格式控制精细到像素，图表专业度高；支持内存优化，生成几十MB的大报表也不崩；API清晰，看示例就会用。缺点也明确：只能新建Excel，不能读也不能改已有文件；只认.xlsx，老格式.xls不支持。

### 适用场景

汇报场景必用：做月度业绩报表，加个专业柱状图；做库存预警表，低于安全库存自动标红；做公司统一的报销单、申请表模板，格式固定不混乱。

### 安装与示例

安装一行命令：`pip install xlsxwriter`

给新手整个“带条件格式+图表”的汇报报表示例：

```python

import xlsxwriter

# 新建工作簿和工作表
workbook = xlsxwriter.Workbook("业绩报表.xlsx")
worksheet = workbook.add_worksheet("销售趋势")  # 工作表命名

# 定义样式（表头样式+预警样式）
header_style = workbook.add_format({
    "bold": True, "bg_color": "#4472C4", "font_color": "white"
})
warning_style = workbook.add_format({"font_color": "red"})  # 销售额低标红

# 写表头和数据
headers = ["月份", "销售额（元）"]
data = [["1月", 50000], ["2月", 65000], ["3月", 48000], ["4月", 72000]]
worksheet.write_row("A1", headers, header_style)  # 写表头+加样式

# 写数据，销售额低于5万标红
for row, (month, sales) in enumerate(data, 1):
    worksheet.write(row, 0, month)  # 写月份
    # 条件判断：低于5万加预警样式
    if sales < 50000:
        worksheet.write(row, 1, sales, warning_style)
    else:
        worksheet.write(row, 1, sales)

# 做柱状图（销售趋势）
chart = workbook.add_chart({"type": "column"})
# 关联数据（月份为X轴，销售额为Y轴）
chart.add_series({
    "name": "销售额",
    "categories": ["销售趋势", 1, 0, 4, 0],  # 月份数据范围
    "values": ["销售趋势", 1, 1, 4, 1],      # 销售额数据范围
})
# 给图表加标题和轴标签
chart.set_title({"name": "2025年1-4月销售趋势"})
chart.set_x_axis({"name": "月份"})
chart.set_y_axis({"name": "销售额（元）"})

# 插入图表到D2位置
worksheet.insert_chart("D2", chart)

# 关闭工作簿（必写！不然文件会损坏）
workbook.close()
print("报表生成完成！打开‘业绩报表.xlsx’看效果～")
```

## 五、pywin32：Windows下的“全能操控手”

pywin32是Windows用户的“Excel全能遥控器”——靠调用本地Microsoft Excel的COM接口干活，相当于用Python替你手动点鼠标操作Excel。所以Excel能做的事，它全能干，宏、密码保护、高级图表这些都不在话下，堪称“无上限”工具。

![image.png](https://raw.atomgit.com/user-images/assets/5027920/a9a65d37-6226-4b78-87c4-959433d261c3/image.png 'image.png')

### 核心功能

Excel原生功能全复刻：启动/关闭Excel、新建/打开文件都能控制，还能让Excel后台偷偷运行不弹窗；.xls/.xlsx/.xlsm不管啥格式都能处理；宏能运行能录制，带宏的财务报表直接自动化；转PDF精度拉满，和手动转的一模一样；带密码的Excel文件也能处理。

### 优缺点

优点就是“全能”：Excel能做的它都能做，复杂报表、宏操作全拿下；格式转换精度第一，投标文件这种关键文档转PDF必用；能和Word、PPT联动（比如从Word提数据写Excel）。缺点很明显：仅限Windows，Mac/Linux用不了；必须装正版Excel；后台运行容易残留进程，忘关会占内存。

### 适用场景

复杂场景救星：处理带宏的自动计算报表（比如财务的利润表，改数据自动算结果）；投标报价表转PDF（要求和原表格格式完全一致）；做Office联动流程（Excel取数→Word写报告→PDF存档）。

### 安装与示例

安装命令：`pip install pywin32`

高频场景“Excel转PDF”示例，精度拉满：

```python

import win32com.client as win32

# 启动Excel（后台运行，不弹窗）
excel = win32.Dispatch("Excel.Application")
excel.Visible = 0  # 0=后台，1=显示界面
excel.DisplayAlerts = 0  # 关闭弹窗警告（比如文件已存在的提示）

# 打开Excel文件（路径要写全，注意用双反斜杠或r前缀）
workbook = excel.Workbooks.Open(r"C:\你的文件路径\投标报价表.xlsx")

# 转PDF（17是PDF的固定编码，记住就行）
pdf_path = r"C:\你的文件路径\投标报价表.pdf"
workbook.SaveAs(pdf_path, FileFormat=17)

# 关键！一定要关文件和Excel，不然后台会残留进程
workbook.Close()
excel.Quit()

print(f"PDF已生成：{pdf_path}")
```

## 终极选型指南：按需pick不踩坑

不用再纠结！按场景直接挑：

→ **新手入门/日常.xlsx处理**：openpyxl（免费跨平台，看示例就会）；

→ **旧版.xls文件处理**：xlrd+xlwt（专属兼容，老报表不慌）；

→ **批量数据汇总/清洗**：pandas（效率之王，一行代码顶一小时人工）；

→ **高颜值报表/图表**：xlsxwriter（汇报神器，格式专业拿得出手）；

→ **Windows+Excel深度操控**：pywin32（全能选手，宏、高精度转格式全搞定）。

其实80%的办公场景，openpyxl（基础操作）+pandas（批量处理）就够了！练熟这俩，基本能告别重复的Excel操作，效率直接翻倍～
> （注：文档部分内容可能由 AI 生成）



## 说干就干

接下来我的账号会转向**以AI编程为中心，分享和AI有关的内容**。

和2019年做自动化办公，录制了一套自动化办公的教程，并且围绕这套教程更新了接近5年类似。我也在整理了自己的经验后，打造了一套全新的课程：**给小白的《30讲 · AI编程训练营》**。

- 面向小白：不需要会编程，因为AI本来就是为了解放大脑，加入以后，我会循序渐进的带大家学习AI编程
- 项目为主：这也是我一直以来的风格，**大家都不是深入研究大模型的，用的溜更重要，对吧？**
- 内容详实：从必备的原理到实践，从文档到视频、软件，有关AI编程有关的，我能接触到的所有内容，我都会制作分享
- 特色内容：**BAT的合作资源，各家大厂的AI福利，我作为一个编程博主都能拿到的**，作为这套核心课程的学员，我也会毫无保留的分享

以下是这次课程的目录（只展示主干必学部分）：



<p align="center" id='AI编程训练营'>
    <a target="_blank" href='https://www.python-office.com/course-002/AICoding/version-001/all.html'>
    <img src="https://raw.gitcode.com/user-images/assets/5027920/688bcc16-4fe8-4a10-8e5d-784cb4815d7f/30讲.jpg" />
    </a>   
</p>




目前计划的课程价格是299元。预售留的50个名额已经秒空了30个。

这也是我接下来的重点破局项目，现在价格是**199元**，最后再剩下的20个名额，满人后就恢复原价299了。大家想学习就加直接我微信：**wfdev7**，备注：AI编程

<p align="center" id='30个名额'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/7rH5U6s91hnTKCKZy4BHCg'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/71bd2ff3-ac85-43a4-8288-164cc66e119d/image.png" width="350" height='600'/>
    </a>   
</p>


<p align="center" id='老粉的认可'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/7rH5U6s91hnTKCKZy4BHCg'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/6d5a3b73-0367-455a-ab69-4b47ca2646af/image.png" width="350" height='600'/>
    </a>   
</p>

<p align="center" id='学习群的氛围'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/7rH5U6s91hnTKCKZy4BHCg'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/b89b206c-8f44-4e1b-a9e3-4f168531b9da/image.png" width="350" height='600'/>
    </a>   
</p>

## 常见问题

Q：不会编程可以学吗？
<br/>A：可以学习，我的粉丝大多是编程小白。

Q：学习形式是什么？
<br/>A：按顺序看视频，边学边练。文档用来扩展知识，课程群用来分享资料和答疑。

Q：老粉丝有其他优惠吗？
<br/>A：我所有付过费的老粉丝，都有额外的降价优惠，最低我也会送一本书，作为再次支持的感谢。如果是已经购买了这套课程，再想学其它课程，也会有专属的优惠。

Q：有其他更高级的课程吗？
<br/>A：我后续打算还会出：AI编程出海、智能体、工作流、AI创作营，都会以本次的AI编程为基础。





## **关于作者**  

先给新朋友介绍一下我自己，你可以叫我晚枫。

从2019年至今，我成为科技博主已经5年多了,期间没有停止过更新，也很幸运获得了一些值得自豪的收获：物质/精神的都有。

- 物质收获，详见atomgit在2025年初对我的一次采访：[DeepSeek浪潮下如何撑过35岁职场危机？跨界程序员晚枫：我不焦虑，40岁就退休](https://mp.weixin.qq.com/s/3KvzA0ZOKJCz11Sk-karOw)
- 2023年也加入了Python中国组委会，[2024年加入了Python基金会](https://mp.weixin.qq.com/s/G_Ro4UVdgv2tOE_6pHdnUA)。这是我在Python中国大会的演讲：[非程序员如何学习和使用 Python？](https://mp.weixin.qq.com/s/pJAOgaQ8vA08NrNpJzngFw)
- 我的开源项目[python-office](https://mp.weixin.qq.com/s/7aA0KoXGJuSFkTns-MZYjA)也获得了：[Github上的1200+star 和 atomgit百大开源项目](https://mp.weixin.qq.com/s/pJAOgaQ8vA08NrNpJzngFw)
- 有了一套全网播放量过百万的课程：[给小白的《50讲 · Python自动化办公》（完结）](https://mp.weixin.qq.com/s/tKlzVee4kmJk4dGfKvVnFQ)

> 以上这些，我把它称为我在all in AI之前的经历。之前建立的Python主题的付费群，也有430多人加入：[Python学习 · 读者交流群](https://mp.weixin.qq.com/s/0GrWWSQ8sKs-WA8WoN3Ztg?payreadticket=HPsk3SM42QLKkwlPgzoQN00eTUDy7x7I70-jcY9jIG2bWFmjZvB7r1mF10OiNSkxknfiN08&scene=1&click_id=8)，如果你是想单纯学习Python的朋友，建议直接加这个Python群。我一直在运营中，也还会继续运营下去。

![Python群的付费记录](https://raw.atomgit.com/user-images/assets/5027920/4926e0f9-3647-45da-accb-34d132eb1385/image.png 'image.png')

从2023年接触到AI开始，我看到了AI和各行各业结合的机会，以及我作为一个博主可以分享、创作的方向，并且和小伙伴一起创立了：白开水AI社区。

开始转型AI，根本停不下来，每天都在尝试、分享、获得反馈后继续尝试，如此正向循环，犹如新生儿快速进步。

如果大家对AI感兴趣，可以加入我的AI交流群，和我一起交流成长！👇

<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='http://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

> 以下是最近一些有用、开始运行的AI探索：
- [我也吃上了AI的红利！分享一个邪修思路](https://mp.weixin.qq.com/s/RGakg6tIc_jcYTvjeh3zjw)
- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/7rH5U6s91hnTKCKZy4BHCg)
- [花了一个月终于搞定了！公开我的 AI 自动发文智能体，小白也能用](https://mp.weixin.qq.com/s/96CYtR9IFpGNJwOVzPDx4Q)
- [AI短视频还有红利！coze书单号，给我冲](https://mp.weixin.qq.com/s/qokwWMcCdr0PSSm3aGhssA)
- [我用AI写了一个发票批量识别软件，免费分享给大家](https://mp.weixin.qq.com/s/1V6w9CjQV8S8z8NRSc3L_w)


---

> 另外，大家去给小明的小红书👇账号点点赞吧~！我不想努力了，想吃软饭了。

![小红书：爱吃火锅的小明](https://raw.atomgit.com/user-images/assets/5027920/24fb7a85-b1f1-43ab-a208-7ebf008933b2/image.png 'image.png')


![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  

![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '4dbea2fec93c415c75311666f19a1022.jpg')

![滴滴红包](https://raw.atomgit.com/user-images/assets/5027920/d79c7834-a008-4512-a8ca-88a0b5a990a5/c14141a45d3b671ae94a11bd0556d1dc.jpg 'c14141a45d3b671ae94a11bd0556d1dc.jpg')




