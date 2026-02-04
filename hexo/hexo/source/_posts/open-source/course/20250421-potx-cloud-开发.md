---
title: 怎么发布、更新Python第三方库？以potx-cloud为例
date: 2025-04-21 00:41:49
tags: [个人网站,开源]
--- 


![](http://python4office.cn/images/open-source/course/20250421-potx-cloud-开发/pypi.png)

大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，全网同名。

熟悉我的朋友都知道，我的账号内容80%都是关于开源项目的功能文档，剩下20%是关于开发这些功能的周边。

今年开始邀请了小伙伴们参与开源项目的开发和维护，今天就以potx-cloud为例，讲一下怎么成为一个Python库的发布者。

## potx-cloud是什么

potx-cloud是专门用来调用腾讯云平台的工具库，目前的核心功能是：**1行代码，实现文字识别。**

```shell
pip install potx-cloud
```

```python
import potx

# 发票识别
potx.ocr.VatInvoiceOCR()
```

## 怎么参与potx-cloud的开发

potx的源码，全部在atomgit开源：[https://atomgit.com/python4office/potx-cloud](https://atomgit.com/python4office/potx-cloud)，在gitee和GitHub，也都是同步更新的。

```shell
git clone https://atomgit.com/python4office/potx-cloud.git

cd potx-cloud

pip install .
```

修改代码后，提交pr到仓库的develop分支即可。

## 怎么发布新版本？

经历过上面几步，你开发的功能，就有机会加入下一个版本里面，给所有人使用了。

**为了防止出现问题，目前发布新版本主要是我自己在操作，但我手里的库实在是多，而且我发现小伙伴们的水平并不比我差，只要有责任心，也不会出现大问题。**

所以大家对一个库有足够的了解以后，可以根据下面的内容，自己主动实现对该库的发布/更新。

### 注册账号

目前所有的python第三方库，都在这个网站托管：[https://pypi.org](https://pypi.org)，你需要在这里注册一个账号，注意：名字只能是字母和数字，不建议用标点符号。

注册以后，给我说一下你的昵称，我邀请你成为该库的maintainer，比如potx-cloud库的maintainer有：

![请在此添加图片描述](https://developer-private-1258344699.cos.ap-guangzhou.myqcloud.com/column/article/6652786/20250421-14b489bb.png?x-cos-security-token=A0lUDACmIP6YC6yXfJ5joh1UISkrZRea69f9aa167e1cc720fcaa40320bbe7416ndNIf1BzbE67ePIriYfw0_V_zPg2V0HqfwsxyW67U0eA9spKmrcsCZeMivy7gY7lBGoZVQCYguCOb77jtzylSpleMHpUy0vqorot1YMdQNuSc6meUi2ivvJgF9NcgtpkcnqEy0kgUUvYrMvdI8C1kQ_SWjfTtOqueEt0PTaA2BQDgL9GuqDdd3inr3UqrJ2HEcd0oqTXZF6ygOagD_ILA5X9gwPDjXwzOnpzMTkWM7PFAbnI6KbVcPcBBa8RAbq8TkHzb2djOVEo2xdoMkhrGKZAGnke-4WMUMNi3gOV5wemgLA1BP9QrA8_94Axi-MElEwXdYOlpE_DLqWpBMC7G-xicpNUtDMD1WY-yxBaYvH4va1wyU67JvfyQIhVLRWoomDNbLn7ebAXMszrZSeoMA&q-sign-algorithm=sha1&q-ak=AKIDg3AvsPmq6MuADSc-l0sUoQuVxsx1yWWJh6kLUhnInwq3sAA9zmeQn-IfnL9GILel&q-sign-time=1745241695%3B1745248890&q-key-time=1745241695%3B1745248890&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=223af4d22bdf896df13e5c888e6a381821b8fc3e)

在平台收到成为maintainer的邀请后，同意即可。

### 单元测试

回到代码目录，请务必通过单元测试，测试完你所有的修改后，再执行下面的操作。

### 修改版本号

pypi规定，同一个版本号，只能发布一次。

所以发布之前， 请修改2处地方的版本号，如下图所示：

- setup.cfg：这里面的版本号，是真正影响代码版本的地方。关于这个文档里每个参数填写的意义，查看：[Configuring setuptools using setup.cfg files](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)。
- **init**.py：和setup.cfg里的版本保持一致。代码里可以调用的版本号，对发布没有实际影响。

另外说明一下版本号的规则：

**主版本号.次版本号.修订号**

- 修订号：每个新库都是从0.0.1开始递增，最后一位也是用的最多的。后续用于修复bug
- 次版本号/主版本号：1个新库，功能较为完备了，会发布1.0.0，以后每次新增功能，会更新次版本号。

> 建议：更新主版本号之前，一定要经过充分讨论和测试！！

![请在此添加图片描述](https://developer-private-1258344699.cos.ap-guangzhou.myqcloud.com/column/article/6652786/20250421-133cc78c.png?x-cos-security-token=A0lUDACmIP6YC6yXfJ5joh1UISkrZRea851d2b023b346acaa0515b03d92b06c1ndNIf1BzbE67ePIriYfw0_V_zPg2V0HqfwsxyW67U0eA9spKmrcsCZeMivy7gY7lBGoZVQCYguCOb77jtzylSpleMHpUy0vqorot1YMdQNuSc6meUi2ivvJgF9NcgtpkcnqEy0kgUUvYrMvdI8C1kQ_SWjfTtOqueEt0PTaA2BQDgL9GuqDdd3inr3UqrJ2HEcd0oqTXZF6ygOagD_ILA0uk-ZsOhlXYeQ6U7W9k8e9STQ1afLtdYahAX13nw-Rwz2mwVPwIB0qzHGnesyEaYIS4KIUBim12clXb4vzdd6Z9vxfmS9PfKtZ8qIp-e5W-DtBM7nQN4Rh8brNFxOA6zOkESmgA-8j5-aWGEhpVdkh_bpl4iDMQEODJtziW1Tig5Q1KYLlKonMbSQEaoqRxgQ&q-sign-algorithm=sha1&q-ak=AKID5Md6QdJTaPItqRKn3_NTm-D9zHE-L1vGLYKcb7tZUl91IsEpBXSMHwd5Mu4UuWeu&q-sign-time=1745241695%3B1745248890&q-key-time=1745241695%3B1745248890&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=95e869cbe464b8e3ea4b0e92ed0eb482b2b96158)

![请在此添加图片描述](https://developer-private-1258344699.cos.ap-guangzhou.myqcloud.com/column/article/6652786/20250421-884f98bc.png?x-cos-security-token=A0lUDACmIP6YC6yXfJ5joh1UISkrZReab78c9243d90371670733a589dd1afc16ndNIf1BzbE67ePIriYfw0_eKOExizE_0-KHgLZwKgwBMExtq3vMdPejkKC8C66DmahAfRIibTOCsmsvcUe4faX9r_Ay6NukVMX2ErrMk8AdmWPwj57Q60goKS5DpI8JAksk-Rsaql_zV-mK6mNuUp93FtSQrrfLimETLBeVsgJFKVnI9SVMOY_oa2UEdhVhp3NjPGA2npqj08rcMUuwh8aw50EW5tblvJaOfIo7-IPSzii8-dHXvHb8toOoJvVJYDP0qrApjGcG02EA7sLImI1jbHbua1NsoW7duF7jQKBdmmbwBZ6fPZUpEMT_--QG9X_HWf0spzTl3J_Wke4_SgZpVgTzlVfvy-1LGttSY7MMyCoo9WMCAZSjNr6yiurmpAxZQ-pdRz9RkqiblMdizdA&q-sign-algorithm=sha1&q-ak=AKIDocRxqyJYXk21REhHdCUuNbl2E0QdwblyJu3l0UJ1UldmghaHjM13yyyG8JJdZiKH&q-sign-time=1745241696%3B1745248891&q-key-time=1745241696%3B1745248891&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=b658a5e60b376e975fa408b84899460597599fe0)

### 运行脚本

在potx-cloud目录下，运行以下命令：

```shell
pip install twine

sh script/upload.sh
```

不要进入script目录！！具体原因可以看脚本是怎么写的。

第一次运行这个脚本可能会报错，因为现在pypi网站时双因子认证了，可能会让你在发布的电脑上，做一些token或者其它双因子认证的设置，根据它提示的文档做就可以了。英文不好，或者干脆找不到也可以问我。

发布以后，请把最新的版本号及时同步到开发小组的群里.

## 待优化项

现在pypi官网，已经开始建议使用更为方便的pyproject.toml来管理和发布第三方库了：[https://packaging.python.org/en/latest/guides/section-build-and-publish/](https://packaging.python.org/en/latest/guides/section-build-and-publish/)。

希望新加入的小伙伴可以学习研究一下，对我们第三方库的管理，也进行一个升级换代~



## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/gtR2MRs3mQCNXIO6MxUuQA)就能上手做AI项目。