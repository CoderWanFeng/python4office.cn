---
title: Python办公实战！​按姓名拆分Excel为单独文件，微信自动发给相应联系人
date: 2022-09-28 20:30:14
tags: python-office
---



![python-office](https://cos.python-office.com/wechat%2Fqr-code.jpg)
作者：culljores

原文链接：https://blog.csdn.net/culljores/article/details/127080680

大家好，这里是Python程序员晚枫，今天给大家分享一篇[读者群](http://www.python4office.cn/wechat-group/)里的来稿：**Python + Excel自动化办公，在工作中的实际应用**。

欢迎大家总结[python-office](https://mp.weixin.qq.com/s/QhaUoB7Q4CJHR29uD6JSHQ)的使用经验，联系我投稿哟~




## 一、前言
最近遇到一个需求:
- 把员工信息汇总表excel，**按员工姓名拆分**成单独的excel，新excel以员工姓名命名，里面第一行是表头，第二行是员工信息。
- 然后把excel通过**微信**单独发送给每位员工。

>这个需求适用于发送月度工资表、学校学生信息统计等场景。

在B站上找到``@程序员晚枫``，大神制作的python-office库可以完美实现这个功能，在此拜谢，给大佬端茶。动手操作过程中遇到一些困难，把我的解决思路写下，供大家参考。

## 二、准备环境
### 1、请适用python 3.8.9 64位版本
其他版本在安装python-office库时会遇到各种问题，解决起来费时费力，建议直接使用python 3.8.9 64位版本，只需要在pycharm上搭建一个新环境，就可以轻松安装使用了。

- Python所有版本：[下载链接](https://mp.weixin.qq.com/s/d7VWKV_3Bd0fyThATpvhjA)
- Python开发工具：[下载链接](https://mp.weixin.qq.com/s/ktmQafdstwep_A5vae_Ymw)

### 2、安装python-office
```
pip install python-office
```
### 3、还会使用openpyxl这个库，用来处理excel。
## 三、思路分析
### 1、读取excel
用``openpyxl``库的``load_workbook()``读取相应的表格，表单和单元格都用列表的形式使用就行，例如['Sheet1'].['B1']

### 2、删除excel不用的行
openpyxl库的删除整行命令是``ws.delete_rows()``，括号中输入行号，删除行时要注意从后往前删除，否则行号会出现错误:

>比如删除了第二行后要删第三行，这时第三行已经变成了第二行，给删除造成麻烦，从后往前删就不会出现这个问题。

这里会用到最大行，命令为``ws.max_row``，接着用for遍历，需要倒着数，``for i in range(ws.max_row, 1, -1)``，这样就从最后一行开始遍历，一直遍历到第二行，把不想要的用``ws.delete_rows(i)``删除就行。

### 3、保存成单独excel。
``wb.save()``，括号中写新的文件名

### 4、利用python-office库发送微信消息。

只需要用到一行命令，简单背后的复杂都由``python-office``库的开发者帮我们封装好了，吃水不忘挖井人，给晚枫大神献上膝盖。

``office.wechat.send_file(who=, file=)``，分别在括号里写上微信昵称和文件地址。

- 微信机器人：[视频教程](https://mp.weixin.qq.com/s/6slx8hyv_WuK7v5Nzt3XKQ)

发到

## 四、代码展示

上代码~
```
import openpyxl, office #导入两个库，第一个处理excel，第二个用到微信发消息功能，第二个库还有很多强大便捷的功能。
 
wb = openpyxl.load_workbook('C:/Users/./././???.xlsx') #括号中写汇总文件地址
ws = wb['Sheet1']              #获取excel表单
Names = ws['B']                #获取表单中第二列，我的表单第二列是微信昵称，可以根据实际进行调整
max_row = ws.max_row           #获取excel的最大行数
 
for Name in Names:             #第5行代码获得的昵称需要遍历
    Name = Name.value          #遍历出来的是元祖，需要用value进行取值
    if Name == 'Nick Name':    #我的excel B1单元格写的是Nick Name，大家可以根据实际调整
        continue
    else:
        wb = openpyxl.load_workbook('C:/Users/./././???.xlsx')
        ws = wb['Sheet1']
        for j in range(max_row, 1, -1):   #倒着遍历，方便删除时不错序
            if ws[f'B{j}'].value != Name:
                ws.delete_rows(j)         #删除行
        file_path = f'C:/Users/./././{Name}.xlsx'  #重命名
        wb.save(file_path)  #保存excel
        office.wechat.send_file(who=Name, file=file_path)  #通过微信发送文件，分别在括号里写上微信昵称和文件地址。
```
----




---

![](https://cos.python-office.com/ads/fuli/all-1.jpg)

![](https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)就能上手做AI项目。