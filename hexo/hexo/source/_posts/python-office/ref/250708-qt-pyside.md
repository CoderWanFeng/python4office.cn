---
title: pyqt和pyside全面对比
date: 2025-07-08 10:41:04
tags: 开源
---

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)。

我们团队最近在基于腾讯的OCR接口，开发一个桌面GUI软件，功能是实现发票识别。

项目地址：[发票识别的源码](https://atomgit.com/python4office/poui/blob/develop/poocr_gui/exe.py)

因为技术选型问题，之前选择的是pyqt5这个框架，现在想出售软件，发现了一些商业使用方面的问题，所以打算换成开源免费的

PySide和PyQt都是基于Qt框架的Python绑定，用于开发图形用户界面（GUI）应用程序，它们各自有多个版本，并且存在一些关键区别。

## 精简版

- 如开发商业软件，pyqt需要购买授权，pyside不需要
- 有意思的地方：pyside才是qt公司开发的，pyqt不是
- pyqt替换成pyside，成本很低，接口基本一致

## PySide的版本

PySide目前主要有两个主要的版本系列：

1. **PySide2**：基于Qt5框架，为Python开发者提供了Qt5的完整功能。
2. **PySide6**：基于Qt6框架，是PySide2的升级版本，提供了对Qt6新特性的支持，并且使用了更宽松的LGPL许可证。

### PyQt的版本

PyQt同样有多个版本，与Qt框架的版本相对应：

1. **PyQt5**：基于Qt5框架，是PyQt系列中较为成熟和广泛使用的版本。
2. **PyQt6**：基于Qt6框架，是PyQt5的升级版本，提供了对Qt6新特性的支持，但默认使用GPL许可证，对于商业应用可能需要购买商业授权。

## PySide和PyQt的区别

1. **开源协议**：
    - PySide：使用LGPL许可证，相对宽松，允许开发者自由使用、修改代码，并在分发时不受太多限制。自己开发出来的应用想用啥协议都行，只要把库本身修改的部分按照LGPL协议处理好就行。
    - PyQt：默认使用GPL许可证，要求使用PyQt开发的应用在分发时也必须开源。不过，PyQt也提供了商业授权选项，允许开发者支付费用后闭源使用。

2. **开发和维护团队**：
    - PySide：由Qt的商业拥有者Digia开发和维护，旨在让更多开发者能轻松用上Qt框架。
    - PyQt：由Riverbank Computing公司开发和维护，这家公司在Python和C++软件解决方案领域有深厚积累。

3. **API设计和功能支持**：
    - PySide和PyQt在API设计上非常相似，因为它们都是基于Qt框架的Python绑定。然而，由于开发和维护团队的不同，可能在某些细节上存在差异。
    - 两者都提供了对Qt库的完全封装，支持信号/槽机制，并提供了一整套种类繁多的窗口控件。

4. **社区支持和生态**：
    - PyQt由于历史悠久，拥有更广泛的社区支持和更丰富的生态系统，包括更多的教程、示例和第三方库。
    - PySide虽然社区支持可能相对较少，但它是Qt官方支持的Python绑定，因此与Qt框架的集成更加紧密，且随着Qt6的发布，PySide6也在不断发展壮大。

5. **使用体验**：
    - 对于熟悉Qt框架的开发者来说，PySide和PyQt的使用体验非常相似，因为它们都提供了对Qt功能的Python封装。
    - 选择哪个框架可能取决于项目的具体需求、开源协议的限制以及开发者对社区支持和生态系统的偏好。

----

大家在学习课程中有任何问题，欢迎+微信和我交流~[我的联系方式：微信、读者群、1对1、福利](http://www.python4office.cn/wechat-qrcode/)



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
    <a target="_blank" href='https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/71bd2ff3-ac85-43a4-8288-164cc66e119d/image.png" width="350" height='600'/>
    </a>   
</p>


<p align="center" id='老粉的认可'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/6d5a3b73-0367-455a-ab69-4b47ca2646af/image.png" width="350" height='600'/>
    </a>   
</p>

<p align="center" id='学习群的氛围'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/b6fpU-oXSo8qKP_Nc8w0Zg'>
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





![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')


