---
title: 23个Python爬虫开源项目代码：微信、淘宝、豆瓣、知乎、微博...
date: 2022-11-30 20:43:07
tags:
---



<p align="center" id='大礼包-banner'>
    <a target="_blank" href='http://python4office.cn/fuli/fuli-source-0726/'>
    <img src="https://banner-1300615378.cos.ap-guangzhou.myqcloud.com/%E6%A8%AA%E6%9D%A1/Python%E5%A4%A7%E7%A4%BC%E5%8C%85.jpg" width="100%"/>
    </a>   
</p>

<p align="center" id='1w副业-banner'>
    <a target="_blank" href='http://t.cn/A6KiaiqK'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F1w-pro.jpg" width="100%"/>
    </a>   
</p>






<p align="center" name="图标-github">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng/python-office'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
<a href="https://mp.weixin.qq.com/s/7rH5U6s91hnTKCKZy4BHCg">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>
</p>



# 1、入门项目

1行Python代码下载图片：https://mp.weixin.qq.com/s/H9NVBxwo_po8WsqsIRJ7YQ

微博爬虫：https://mp.weixin.qq.com/s/z9ToYLZSbDxOOKgdxd2Kww

<p align="center" id='52讲爬虫-banner'>
    <a target="_blank" href='http://gk.link/a/11FsN'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F52%E8%AE%B2%E7%88%AC%E8%99%AB.jpg" width="100%"/>
    </a>   
</p>

# 2、高级项目

1. WechatSogou – 微信公众号爬虫

基于搜狗微信搜索的微信公众号爬虫接口，可以扩展成基于搜狗搜索的爬虫，返回结果是列表，每一项均是公众号具体信息字典。

github地址：

https://github.com/Chyroc/WechatSogou



2. DouBanSpider – 豆瓣读书爬虫

可以爬下豆瓣读书标签下的所有图书，按评分排名依次存储，存储到Excel中，可方便大家筛选搜罗，比如筛选评价人数>1000的高分书籍；可依据不同的主题存储到Excel不同的Sheet ，采用User Agent伪装为浏览器进行爬取，并加入随机延时来更好的模仿浏览器行为，避免爬虫被封。

github地址：

https://github.com/lanbing510/DouBanSpider



3. zhihu_spider – 知乎爬虫

此项目的功能是爬取知乎用户信息以及人际拓扑关系，爬虫框架使用scrapy，数据存储使用mongo

github地址：

https://github.com/LiuRoy/zhihu_spider

<p align="center" id='100本电子书-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/6bM_3tROqdY_2WbBShzqyw'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Febook.jpg" width="100%"/>
    </a>   
</p>


<p align="center" id='25个学习资源-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/-mlsV7PFc27JElOTCskMsg'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fpy-25-source.jpg" width="100%"/>
    </a>   
</p>


4. bilibili-user – Bilibili用户爬虫

总数据数：20119918，抓取字段：用户id，昵称，性别，头像，等级，经验值，粉丝数，生日，地址，注册时间，签名，等级与经验值等。抓取之后生成B站用户数据报告。

github地址：

https://github.com/airingursb/bilibili-user



5. SinaSpider – 新浪微博爬虫

主要爬取新浪微博用户的个人信息、微博信息、粉丝和关注。代码获取新浪微博Cookie进行登录，可通过多账号登录来防止新浪的反扒。主要使用 scrapy 爬虫框架。

github地址：

https://github.com/LiuXingMing/SinaSpider

<p align="center" id='52讲爬虫-banner'>
    <a target="_blank" href='http://gk.link/a/11FsN'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F52%E8%AE%B2%E7%88%AC%E8%99%AB.jpg" width="100%"/>
    </a>   
</p>

6. distribute_crawler – 小说下载分布式爬虫

使用scrapy,Redis, MongoDB,graphite实现的一个分布式网络爬虫,底层存储MongoDB集群,分布式使用Redis实现,爬虫状态显示使用graphite实现，主要针对一个小说站点。

github地址：

https://github.com/gnemoug/distribute_crawler



7. CnkiSpider – 中国知网爬虫。

设置检索条件后，执行src/CnkiSpider.py抓取数据，抓取数据存储在/data目录下，每个数据文件的第一行为字段名称。

github地址：

https://github.com/yanzhou/CnkiSpider



8. LianJiaSpider – 链家网爬虫。

爬取北京地区链家历年二手房成交记录。涵盖链家爬虫一文的全部代码，包括链家模拟登录代码。

github地址：

https://github.com/lanbing510/LianJiaSpider



9. scrapy_jingdong – 京东爬虫。

基于scrapy的京东网站爬虫，保存格式为csv。

github地址：

https://github.com/taizilongxu/scrapy_jingdong



10. QQ-Groups-Spider – QQ 群爬虫。

批量抓取 QQ 群信息，包括群名称、群号、群人数、群主、群简介等内容，最终生成 XLS(X) / CSV 结果文件。

github地址：

https://github.com/caspartse/QQ-Groups-Spider



11. wooyun_public -乌云爬虫。

 乌云公开漏洞、知识库爬虫和搜索。全部公开漏洞的列表和每个漏洞的文本内容存在MongoDB中，大概约2G内容；如果整站爬全部文本和图片作为离线查询，大概需要10G空间、2小时（10M电信带宽）；爬取全部知识库，总共约500M空间。漏洞搜索使用了Flask作为web server，bootstrap作为前端。

https://github.com/hanc00l/wooyun_public



12. spider – hao123网站爬虫。

以hao123为入口页面，滚动爬取外链，收集网址，并记录网址上的内链和外链数目，记录title等信息，windows7 32位上测试，目前每24个小时，可收集数据为10万左右

https://github.com/simapple/spider


<p align="center" id='30讲自动化办公-banner'>
    <a target="_blank" href='https://www.python-office.com/video/video.html'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/%E5%BC%95%E5%AF%BC%E8%B6%85%E9%93%BE%E6%8E%A5%2Fauto-work.jpg" width="100%"/>
    </a>   
</p>


13. findtrip – 机票爬虫（去哪儿和携程网）。

Findtrip是一个基于Scrapy的机票爬虫，目前整合了国内两大机票网站（去哪儿 + 携程）。

https://github.com/fankcoder/findtrip



14. 163spider – 基于requests、MySQLdb、torndb的网易客户端内容爬虫

https://github.com/leyle/163spider



15. doubanspiders – 豆瓣电影、书籍、小组、相册、东西等爬虫集

https://github.com/fanpei91/doubanspiders



16. QQSpider – QQ空间爬虫，包括日志、说说、个人信息等，一天可抓取 400 万条数据。

https://github.com/LiuXingMing/QQSpider



17. baidu-music-spider – 百度mp3全站爬虫，使用redis支持断点续传。

https://github.com/Shu-Ji/baidu-music-spider



18. tbcrawler – 淘宝和天猫的爬虫,可以根据搜索关键词,物品id来抓去页面的信息，数据存储在mongodb。

https://github.com/pakoo/tbcrawler

<p align="center" id='0基础数据分析-banner'>
    <a target="_blank" href='http://gk.link/a/10EfJ'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2Fpython%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90.jpg" width="100%"/>
    </a>   
</p>

19. stockholm – 一个股票数据（沪深）爬虫和选股策略测试框架。根据选定的日期范围抓取所有沪深两市股票的行情数据。支持使用表达式定义选股策略。支持多线程处理。保存数据到JSON文件、CSV文件。

https://github.com/benitoro/stockholm



20. BaiduyunSpider - 百度云盘爬虫。

https://github.com/k1995/BaiduyunSpider



21. Spider - 社交数据爬虫。支持微博,知乎,豆瓣。

https://github.com/Qutan/Spider



22. proxy pool - Python爬虫代理IP池(proxy pool)。

https://github.com/jhao104/proxy_pool



23. music-163 - 爬取网易云音乐所有歌曲的评论。

https://github.com/RitterHou/music-163