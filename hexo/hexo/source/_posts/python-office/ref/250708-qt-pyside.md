---
title: pyqt和pyside全面对比
date: 2025-07-08 10:41:04
tags: 开源
---

大家好，这里是程序员晚枫。

我们团队最近在基于腾讯的OCR接口，开发一个桌面GUI软件，功能是实现发票识别。

项目地址：[发票识别的源码](https://gitcode.com/python4office/poui/blob/develop/poocr_gui/exe.py)

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

![](https://cos.python-office.com/ads/gzh/sub-py.jpg)
