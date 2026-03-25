---
title: Google Python开源项目风格指南——中文版
date: 2021-12-30 14:41:27
tags: [代码规范,开源项目]
---




<p align="center">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://raw.atomgit.com/CoderWanFeng1/website/raw/main/github-nav.jpg" alt="github license"/>
    </a>   
</p>
<p align="center">
	<strong>🍬python for office</strong>
</p>
<p align="center">
	👉 <a href="https://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>


<p align="center" name="图标-github">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/contributors/CoderWanFeng/python-office" alt="github contributors"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/forks/CoderWanFeng/python-office" alt="github forks"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues/CoderWanFeng/python-office" alt="github issues"/>
    </a>	
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/issues-pr/CoderWanFeng/python-office" alt="github license"/>
    </a>
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/license/CoderWanFeng/python-office" alt="github license"/>
    </a>   
</p>

<p align="center" name="gitee">
	<a target="_blank" href='https://gitee.com/CoderWanFeng/python-office/'>
		<img src='https://gitee.com/CoderWanFeng/python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
		<img src="https://gitee.com/CoderWanFeng/python-office/badge/fork.svg?theme=white" alt="gitee fork"/>
	</a>
	<a href="https://mp.weixin.qq.com/s/yaSmFKO3RrBpyanW3nvRAQ">
	<img src="https://img.shields.io/badge/QQ-163434413-orange"/></a>
</p>





# Python 风格指南 - 内容目录
Google Python开源项目风格十分流行，我把其中自己关注的内容摘抄如下。
> 如需查看原手册：[传送门](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/)
## Python语言规范

<!-- more -->

- [Lint](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/#lint)
  - 使用[pylint](http://www.logilab.org/project/pylint)检查python代码
- [导入](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/#id3)
    - 使用 `import x` 来导入包和模块.
    - 使用 `from x import y` , 其中x是包前缀, y是不带前缀的模块名.
    - 使用 `from x import y as z`, 如果两个要导入的模块都叫做y或者y太长了.
    - 仅当缩写 `z` 是通用缩写时才可使用 `import y as z`.(比如 `np` 代表 `numpy`.)
- [包](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/#id6)
    - 所有的新代码都应该用完整包名来导入每个模块.
- [异常](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/#id7)
    - 永远不要使用 `except:` 语句来捕获所有异常, 也不要捕获 `Exception` 或者 `StandardError` , 除非你打算重新触发该异常, 或者你已经在当前线程的最外层(记得还是要打印一条错误消息). 在异常这方面, Python非常宽容, `except:` 真的会捕获包括Python语法错误在内的任何错误. 使用 `except:` 很容易隐藏真正的bug.
- [全局变量](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/#id8)
    - 避免使用全局变量. 鼓励使用模块级的常量。
    - 注意常量命名必须全部大写,用 `_` 分隔.具体参见 [命名规则](https://google.github.io/styleguide/pyguide.html#s3.16-naming) 
- [函数与方法装饰器](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/#id18)
- [线程](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/#id20)
- [威力过大的特性](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/#id21)
- [现代python: python3 和from __future__ imports](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/#python-python3-from-future-imports)
- [代码类型注释](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_language_rules/#id24)
## Python风格规范
- [分号](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id1)
- [行长度](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#line-length)
- [括号](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id6)
- [缩进](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#indentation)
- [序列元素尾部逗号](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id8)
- [空行](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id10)
- [空格](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id11)
- [Shebang](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#shebang)
- [注释](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#comments)
- [标点符号,拼写和语法](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id15)
- [类](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id16)
- [字符串](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id17)
- [文件和sockets](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#sockets)
- [TODO注释](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#todo)
- [导入格式](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id18)
- [语句](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id19)
- [访问控制](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id20)
- [命名](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id21)
- [Main](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#main)
- [函数长度](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id22)
- [类型注释](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#id23)
## [临别赠言](https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/parting_words/)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://www.bilibili.com/cheese/play/ss982042944)


程序员晚枫专注AI编程培训，小白看完他和图灵社区合作的教程[《30讲 · AI编程训练营》](https://www.bilibili.com/cheese/play/ss982042944)就能上手做AI项目。