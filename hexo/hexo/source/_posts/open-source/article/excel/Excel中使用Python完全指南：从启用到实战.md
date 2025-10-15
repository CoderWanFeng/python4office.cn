---
title: Excel 中使用 Python 完全指南：从启用到实战
date: 2025-10-15 18:25:17
tags: 自动化办公
---


<p align="center" id='进群-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/0GrWWSQ8sKs-WA8WoN3Ztg?payreadticket=HPsk3SM42QLKkwlPgzoQN00eTUDy7x7I70-jcY9jIG2bWFmjZvB7r1mF10OiNSkxknfiN08&scene=1&click_id=1'>
    <img src="https://raw.gitcode.com/user-images/assets/5027920/d78ad96d-6a5e-49fa-9a6d-ba98ec1a1293/image.png" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>




<p align="center" name="gitcode">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
		<img src='https://gitcode.com/CoderWanFeng1/python-office/star/badge.svg?theme=dark' alt='gitcode star'/>
	</a>	
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
  	<a href="https://mp.weixin.qq.com/s/yaSmFKO3RrBpyanW3nvRAQ">
	<img src="https://img.shields.io/badge/QQ-163434413-orange"/>
  </a>
    	<a href="http://www.python4office.cn/wechat-group/">
	<img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E4%BA%A4%E6%B5%81%E7%BE%A4-brightgreen"/>
  </a>

</p>



<div align="center">
    <a href="https://github.com/CoderWanFeng"> <img src="https://badgen.net/badge/Github/%E7%A8%8B%E5%BA%8F%E5%91%98?icon=github&color=red"></a>
    <a href="http://www.python4office.cn/account-display/"> <img src="https://badgen.net/badge/follow/%E5%85%AC%E4%BC%97%E5%8F%B7?icon=rss&color=green"></a>
    <a href="https://space.bilibili.com/259649365"> <img src="https://badgen.net/badge/pick/B%E7%AB%99?icon=dependabot&color=blue"></a>
    <a href="http://www.python4office.cn/wechat-group/"> <img src="https://badgen.net/badge/join/%E4%BA%A4%E6%B5%81%E7%BE%A4?icon=atom&color=yellow"></a>
</div>

<!-- more -->



大家好，这里是程序员晚枫。
  

## 你的 Excel 其实藏着 Python 引擎，2025 年最值得学的办公技能  

2025 年 3 月，微软宣布 Excel 内置 Python 功能全面开放，Windows、Mac 和网页版用户终于能直接在单元格中运行 Python 代码。这不是简单的插件集成，而是将 Python 生态（如 pandas、matplotlib）直接嵌入 Excel，意味着你不用切换窗口就能用 Python 处理数据、生成图表，甚至跑机器学习模型。  

但多数人还不知道：你的 Excel 可能已经支持这项功能。打开 Excel 看看「公式」选项卡是否有「插入 Python」按钮？如果没有，检查你的版本是否符合要求——这是解锁高效办公的第一道门槛。  


## 先确认：你的 Excel 能跑 Python 吗？  

微软对 Excel 中的 Python 支持有明确的版本限制，不同平台差异很大：  

- **Windows 用户**：需 Office 365 企业版/商业版，当前频道（版本 2408+）或每月企业频道（版本 2408+）；家庭/个人版需通过预览体验计划开启。  
- **Mac 用户**：需 Office 365 企业版/商业版，Current Channel（版本 16.96+）；家庭/个人版需加入 Beta 频道预览。  
- **网页版用户**：企业/商业版直接支持，家庭/个人版可预览，需登录微软账户。  

*如何检查版本？* 打开 Excel，按「文件 > 账户 > 关于 Excel」，查看版本号和频道。如果版本不支持，企业用户可联系 IT 部门升级，个人用户可在「文件 > 账户 > 加入预览体验计划」中切换到 Beta 频道（可能有稳定性风险）。  


## 3 步启用 Excel 中的 Python，比安装插件还简单  

### 第 1 步：插入 Python 公式  
两种方式启动 Python 模式：  
- **按钮启动**：选中单元格，点击「公式」选项卡中的「插入 Python」按钮，单元格会显示绿色「PY」图标，编辑栏同步出现该图标。  
![转到“公式”，然后选择“插入 Python”。](https://support.microsoft.com/images/zh-cn/38810a27-06ee-4cfb-984c-4ca83d944c4a)
- **手动输入**：在单元格中直接输入 `=PY(`，Excel 会自动弹出函数提示，按 Tab 键确认后进入编辑模式。  
![在单元格中输入 =PY 以启用 Python。](https://support.microsoft.com/images/zh-cn/83af2af0-533e-4408-bdbc-be764703347e)

*注意*：首次使用可能需要同意服务条款，并等待 Python 运行环境初始化（约 10 秒），后续使用会更快。  

### 第 2 步：用 xl() 函数引用 Excel 数据  
Excel 中的 Python 不能直接读取本地文件（如 `pandas.read_excel` 禁用），必须通过 `xl()` 函数引用工作表数据。语法规则如下：  
- 引用单个单元格：`xl("A1")`  
- 引用区域：`xl("B1:C4")`（B1 到 C4 的矩形区域）  
- 引用表格：`xl("MyTable[#All]", headers=True)`（MyTable 为表格名称，`#All` 表示整个表格，`headers=True` 保留表头）  

![使用自定义 Python 函数 xl() 在 Excel 和 Python 之间实现接口。](https://support.microsoft.com/images/zh-cn/04de5974-c4d4-4e69-998c-5dd61f403d60)
*示例*：在单元格中输入 `=PY(xl("A1") + xl("B1"))`，即可计算 A1 和 B1 的和，结果直接显示在单元格中。  

### 第 3 步：选择输出类型  
编辑栏右侧有「Python 输出」菜单，支持两种结果类型：  
- **Excel 值**：Python 计算结果转换为 Excel 原生格式（数字、文本、数组），可直接用于 Excel 公式、图表或条件格式。  
- **Python 对象**：保留原始 Python 对象（如 DataFrame、列表），单元格显示「卡片图标」，点击可查看对象详情，适合后续 Python 计算（如用 `df.groupby()` 进一步分析）。  

![使用 Python 输出菜单在输出类型之间切换。](https://support.microsoft.com/images/zh-cn/c4166cb5-98cc-44ac-83f2-678e4a6484ce)
*建议*：如果后续用 Excel 分析选「Excel 值」，如果继续用 Python 处理选「Python 对象」。  


## 实战：用 Excel 内置 Python 做销售数据分析  

假设你有一份销售数据表格（A1:D100，含「日期、产品、销售额、成本」列），目标是计算各产品利润率并生成趋势图。  

### 步骤 1：导入数据（关键！必须用 Power Query）  
由于 Excel 中的 Python 禁用本地文件读取，需先通过 Power Query 导入数据：  
1. 点击「数据 > 获取和转换数据 > 从文件 > 从 Excel 工作簿」，选择你的数据文件。  
2. 在 Power Query 编辑器中加载数据，点击「关闭并上载」，数据会显示在新工作表中（假设表名为「销售数据」）。  

### 步骤 2：用 Python 计算利润率  
在目标单元格输入公式：  
```python  
=PY(  
  df = xl("销售数据[#All]", headers=True);  
  df["利润率"] = (df["销售额"] - df["成本"]) / df["销售额"];  
  df[["产品", "利润率"]]  
)  
```  
- 解析：`xl("销售数据[#All]", headers=True)` 将表格导入为 DataFrame；  
- 新增「利润率」列，计算 (销售额-成本)/销售额；  
- 返回「产品」和「利润率」列，输出类型选「Excel 值」。  

*结果*：单元格会扩展为数组，显示产品名称和对应利润率，可直接用于 Excel 排序或筛选。  

### 步骤 3：生成动态图表  
1. 选中 Python 输出的利润率数据，点击「插入 > 图表 > 柱状图」。  
2. 右键图表 >「选择数据」，确保数据源包含 Python 输出的数组区域。  
3. 当原始销售数据更新时，按 F9 刷新 Python 计算，图表会自动同步更新。  


## 避坑指南：90% 的人会遇到的 3 类错误  

### 1. #PYTHON! 错误  
- **原因**：Python 代码语法错误（如括号缺失、变量未定义）或数据类型不匹配（如字符串减数字）。  
- **解决**：点击单元格旁的错误图标，选择「编辑 Python」，在编辑栏中检查代码，确保引用的单元格区域存在且格式正确。  

### 2. #BUSY! 错误  
- **原因**：Python 计算超时（如处理 10 万行数据）或资源占用过高。  
- **解决**：按 Esc 中断计算，简化代码（如分块处理数据），或切换到「手动计算」模式（「公式 > 计算选项 > 手动计算」），按需按 F9 刷新。  

### 3. 无法启用 Python 功能  
- **原因**：版本不符或管理员禁用。  
- **解决**：确认 Excel 版本和频道（参考前文），企业用户联系 IT 部门检查组策略，个人用户尝试重装 Office 365。  


## 为什么说这是 Excel 史上最颠覆的更新？  

过去处理 Excel 数据，你可能需要在 Excel 和 Python 之间反复切换：用 Excel 整理数据，导出为 CSV，再用 Python 分析，最后将结果复制回 Excel。现在，整个流程能在 Excel 中闭环：  
- **数据导入**：Power Query 替代 `pandas.read_excel`，直接对接数据库、网页数据或本地文件。  
- **分析计算**：单元格中写 Python 代码，调用 pandas、numpy 等库，无需安装环境。  
- **结果呈现**：Python 输出直接转为 Excel 值，无缝对接图表、透视表等功能。  

微软官方数据显示，该功能能将数据分析流程耗时减少 60%，尤其适合财务、市场等需要频繁处理表格数据的岗位。未来，随着 AI 功能的整合（如用 Copilot 自动生成 Python 代码），Excel 可能不再只是「电子表格」，而是变成集数据处理、编程、可视化于一体的综合平台。  

*现在就打开你的 Excel 试试吧——下一个效率革命，可能就藏在你每天使用的软件里。*  

（如果在使用中遇到问题，可通过 Excel 「帮助 > 反馈」提交，微软会优先处理高频问题。）  

![Excel 中的 Python 功能封面图](https://s.coze.cn/t/nBx8Ht5nwGw/)

### 参考文档
- [Excel 中使用 Python 完全指南](https://support.microsoft.com/zh-cn/office/excel-%E4%B8%AD%E7%9A%84-python-%E5%85%A5%E9%97%A8-a33fbcbe-065b-41d3-82cf-23d05397f53d)


---

> 另外，大家去给小明的小红书👇账号点点赞吧~！我不想努力了，想吃软饭了。

![小红书：爱吃火锅的小明](https://raw.gitcode.com/user-images/assets/5027920/24fb7a85-b1f1-43ab-a208-7ebf008933b2/image.png 'image.png')

![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.gitcode.com/user-images/assets/5027920/84b09492-5f26-4c39-8e30-f056839d1993/6152d8017a3595256e51cbd9e08e148b.png '6152d8017a3595256e51cbd9e08e148b.png')

![美团红包](https://raw.gitcode.com/user-images/assets/5027920/84f473b9-6373-46f4-beea-b671bddc637c/6d283319df13b09a3f74a9f19bf18a97.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')

