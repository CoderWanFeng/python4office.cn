---
title: 第八讲：CI/CD 跨平台打包  
date: 2025-07-14 08:41:49
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
	<a href="https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>

<!-- more -->



大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)，全网同名。


——用 GitHub Actions 在 5 分钟内同时产出 Win / macOS / Linux 三系统可执行文件

--------------------------------------------------
开场 20 秒  
“手动打包 3 个平台，每次发版 2 小时？”  
本讲 15 分钟，教你把 pyinstaller 写进 GitHub Actions，Push 即出 Release，附带版本号、校验和、代码签名。

--------------------------------------------------
8.1 整体思路（1 min）

• 单仓库 + 多 job 并行  
• 每 job 使用对应平台 runner  
• 缓存 pip & pyinstaller 缓存目录  
• 产物自动上传到 Release

--------------------------------------------------
8.2 仓库目录约定（1 min）

```
myapp/
├─ src/
│  └─ main.py
├─ assets/
│  ├─ icon.ico
│  └─ icon.icns
├─ requirements.txt
├─ main.spec          # 统一 spec
├─ .github/workflows/release.yml
└─ version.txt        # 写入 1.2.3
```

--------------------------------------------------
8.3 GitHub Actions 完整 workflow（直接抄）

`.github/workflows/release.yml`
```yaml
name: Multi-OS Build

on:
  push:
    tags: [ "v*.*.*" ]        # 推送 v1.2.3 即触发

jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    runs-on: ${{ matrix.os }}

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"

    - name: Cache pip
      uses: actions/cache@v4
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}

    - name: Install deps
      run: |
        python -m pip install -U pip
        pip install -r requirements.txt pyinstaller

    - name: Build binary
      run: |
        pyinstaller main.spec

    - name: Upload artifact
      uses: actions/upload-artifact@v4
      with:
        name: myapp-${{ runner.os }}
        path: dist/*

  release:
    needs: build
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - name: Download all artifacts
      uses: actions/download-artifact@v4
      with:
        path: artifacts

    - name: Create Release & Upload
      uses: softprops/action-gh-release@v2
      with:
        tag_name: ${{ github.ref_name }}
        name: Release ${{ github.ref_name }}
        files: |
          artifacts/myapp-Linux/*
          artifacts/myapp-Windows/*.exe
          artifacts/myapp-macOS/*
        generate_release_notes: true
```

--------------------------------------------------
8.4 统一版本号注入（1 min）

在 `main.spec` 顶部读 tag：
```python
import os
VERSION = os.getenv("GITHUB_REF_NAME", "dev").lstrip("v")
```

再把 `VERSION` 写进 EXE：
```python
exe = EXE(
    ...
    version=f'build/{VERSION}.txt'
)
```
GitHub Actions 自动把 `v1.2.3` 注入，无需手动改文件。

--------------------------------------------------
8.5 代码签名 & Notarization（macOS 专属，2 min）

secrets 配置  
- `MACOS_CERTIFICATE`：Base64 的 p12  
- `MACOS_CERTIFICATE_PWD`  
- `APPLE_ID`, `APPLE_TEAM_ID`, `APPLE_APP_PASSWORD`

workflow 片段
```yaml
    - name: Import cert & sign
      if: runner.os == 'macOS'
      run: |
        echo ${{ secrets.MACOS_CERTIFICATE }} | base64 -d > cert.p12
        security import cert.p12 -k ~/Library/Keychains/login.keychain -P ${{ secrets.MACOS_CERTIFICATE_PWD }} -T /usr/bin/codesign
        codesign --force --options=runtime --sign "Developer ID Application: Your Name" dist/MyApp.app
```

Notarization 可用 `xcrun notarytool submit`（略）。

--------------------------------------------------
8.6 产物示例（1 min）

Release 页面自动出现：  
```
myapp-v1.2.3-linux.tar.gz
myapp-v1.2.3-windows.exe
myapp-v1.2.3-macos.dmg
```
带 SHA256 校验和 Release Notes。

--------------------------------------------------
8.7 本地验证小技巧（1 min）

```bash
# 模拟 CI 环境
act -j build --matrix os:ubuntu-latest
```

--------------------------------------------------
8.8 常见坑速查

| 坑 | 症状 | 解决 |
|---|---|---|
| Windows 长路径 | 构建失败 | `git config --system core.longpaths true` |
| UPX 被 Defender 误杀 | 上传 exe 报毒 | CI 里 `--upx-exclude` 或关掉 UPX |
| macOS 签名失败 | “unsealed contents present” | 用 `codesign --verify --deep --strict` 先自检 |

--------------------------------------------------
小结 & 作业（30 秒）

• 一条 workflow 产出三平台可执行文件  
• 版本号、签名、Release 全自动  
• 作业：把你的项目按本讲模板 push v0.1.0，检查 Release 是否成功生成 3 个产物。

下节课《第九讲：运行时问题定位与解决》教你“用户打不开”时如何远程诊断。


----

大家在学习课程中有任何问题，欢迎+微信和我交流👉[我的联系方式：微信、读者群、1对1、福利](http://www.python4office.cn/wechat-qrcode/)


![](https://cos.python-office.com/ads/gzh/sub-py.jpg)

![扫一扫，领红包](https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg '6152d8017a3595256e51cbd9e08e148b.png')
  
![美团红包](https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg '6d283319df13b09a3f74a9f19bf18a97.jpg')







程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。