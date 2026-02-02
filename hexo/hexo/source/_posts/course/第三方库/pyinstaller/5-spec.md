---
title: 第五讲：.spec 文件深度定制   
date: 2025-07-14 05:41:49
tags: [第三方库,pyinstaller]
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
</p>
<p align="center" name="atomgit">
	<a href="https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>

<!-- more -->



大家好，这里是程序员晚枫，正在all in [各种AI项目](https://mp.weixin.qq.com/s/XQhCrkbumDqtOZXuapMpVg)，全网同名。

  
（让 CLI 参数“退休”，进入 Python 脚本级打包）

--------------------------------------------------
开场 15 秒  
CLI 参数再多也有天花板；真正做产品级打包，90 % 时间都在改 `.spec`。  
本讲 15 分钟，把自动生成的 `.spec` 拆成 4 大对象，手把手改成“可维护、可扩展、可 CI/CD”的生产脚本。

--------------------------------------------------
5.0 回顾：从 CLI 到 spec 的两条路径

1) 先 CLI 后 spec（推荐新手）  
```bash
pyi-makespec --onefile --name MyApp --icon app.ico main.py
# 得到 MyApp.spec，接着手工改
```

2) 直接手写 spec（老司机）  
复制模板 → 按业务填参数 → 一次到位。

--------------------------------------------------
5.1 四大对象全景图（3 min）

| 对象 | 作用 | 常改字段 |
|---|---|---|
| Analysis | 依赖扫描与收集 | `scripts`, `pathex`, `datas`, `binaries`, `hiddenimports`, `excludes` |
| PYZ | 压缩字节码 archive | 一般不动 |
| EXE | 最终可执行文件 | `name`, `icon`, `console`, `upx`, `version` |
| COLLECT | 仅 `--onedir` 时用到，决定输出目录结构 | 很少改 |

--------------------------------------------------
5.2 最小可改模板（2 min）

```python
# -*- mode: python ; coding: utf-8 -*-
import pathlib
SRC = pathlib.Path('.').resolve()

a = Analysis(
    ['src/main.py'],                     # 入口
    pathex=[SRC/'src', SRC/'lib'],       # 额外 import 路径
    binaries=[],                         # 手动 DLL/SO
    datas=[                              # 资源文件
        (SRC/'assets/logo.png', 'assets'),
        (SRC/'assets/config.json', '.'),
    ],
    hiddenimports=['pkg.sub'],           # 动态 import
    excludes=['matplotlib.tests', 'tkinter'],  # 瘦身
    hookspath=[],
    runtime_hooks=['hooks/rth_persists.py'],   # 运行时钩子
    cipher=None,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz, a.scripts, a.binaries, a.zipfiles, a.datas,
    name='MyApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=['vcruntime140.dll'],
    runtime_tmpdir=None,
    console=False,            # GUI 程序
    icon=SRC/'assets/app.ico',
    version=SRC/'version.txt',
)

# 如果是 onedir，需要 COLLECT（本例 onedir 可省）
# coll = COLLECT(exe, ...)
```

--------------------------------------------------
5.3 高频场景 4 连击（每例 2 min）

① 多入口命令行工具  
把 3 个脚本打成 3 个 exe：
```python
entries = ['cli_a.py', 'cli_b.py', 'gui_c.py']
for e in entries:
    a = Analysis([f'src/{e}'], ...)
    exe = EXE(..., name=e.replace('.py', ''))
```

② 不同平台差异化构建  
```python
import sys
if sys.platform == 'darwin':
    exe = EXE(..., icon=SRC/'assets/app.icns')
elif sys.platform == 'win32':
    exe = EXE(..., icon=SRC/'assets/app.ico', version='version.txt')
```

③ 插件化：运行时加载外部 `.pyd`/`.so`  
```python
binaries=[(SRC/'plugins/*.pyd', 'plugins')]
```
运行时钩子 `rth_persists.py` 把 `plugins/` 加入 `sys.path`。

④ 加密字节码（轻度防窥）  
```python
from PyInstaller.building.api import PYZ
pyz = PYZ(a.pure, a.zipped_data, cipher='mykey')
```
⚠️ 仅轻度混淆，商业级仍需加壳。

--------------------------------------------------
5.4 与 CI/CD 结合（2 min）

GitHub Actions 片段  
```yaml
- name: Build with spec
  run: |
    pip install pyinstaller
    pyinstaller MyApp.spec
```
好处：  
- 版本号、图标统一维护在 spec，不污染 workflow。  
- 同一 spec 可在矩阵里跑 `windows-latest`、`macos-latest`、`ubuntu-latest`。

--------------------------------------------------
5.5 常见踩坑 & 调试技巧（2 min）

| 症状 | 排查命令 | 解决 |
|---|---|---|
| 资源路径找不到 | 打印 `sys._MEIPASS` | 统一用 `pathlib.Path(sys._MEIPASS) / 'relative'` |
| spec 里变量不生效 | `pyinstaller --log-level DEBUG MyApp.spec` | 看 Analysis 日志 |
| UPX 压坏 Qt DLL | `--upx-exclude "Qt5*.dll"` | 黑名单 |

--------------------------------------------------
小结 & 下节预告（15 秒）

• 记住四大对象：Analysis → PYZ → EXE → COLLECT  
• 把 CLI 参数“翻译”成 Python 变量，可读可维护  
• spec 就是打包项目的 Makefile，后续瘦身、签名、加密都在此一层层加料

下节课《第六讲：图形界面应用打包实战（Tkinter / PyQt5 / PySide6）》让窗口程序真正“像一款软件”。


----

大家在学习课程中有任何问题，欢迎+微信和我交流👉[我的联系方式：微信、读者群、1对1、福利](http://www.python4office.cn/wechat-qrcode/)


![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')






程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)就能上手做AI项目。