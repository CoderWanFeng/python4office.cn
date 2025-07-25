---
title: 第十讲：进阶主题 —— 自解压安装包、插件化架构、商业级保护一次打通
date: 2025-07-14 04:42:49
tags: [第三方库,pyinstaller]
---




<p align="center" id='进群-banner'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/dfdNNrlnxGCOsDHV4fq6iQ'>
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
</p>
<p align="center" name="gitcode">
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
    	<a href="http://www.python4office.cn/wechat-group/">
	<img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E4%BA%A4%E6%B5%81%E7%BE%A4-brightgreen"/>
  </a>

</p>

<!-- more -->



大家好，这里是程序员晚枫，全网同名。




> 目标：让用户像安装 QQ 一样双击 setup.exe；让开发者像 VS Code 一样动态装插件；让老板像卖商业软件一样防止破解。  
> 本讲 20 分钟，三条路线任选其一即可落地。

--------------------------------------------------
10.1 自解压安装包（Inno Setup / NSIS / pkgbuild）

10.1.1 Windows：Inno Setup 5 行脚本  
`installer.iss`
```pascal
[Setup]
AppName=MyTool
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\MyTool
OutputBaseFilename=MyTool_Setup
SetupIconFile=assets\app.ico

[Files]
Source: "dist\MyTool.exe"; DestDir: "{app}"; Flags: ignoreversion
[Icons]
Name: "{autoprograms}\MyTool"; Filename: "{app}\MyTool.exe"
```
一键打包  
```bash
iscc installer.iss   # 生成 MyTool_Setup.exe
```

10.1.2 macOS：pkgbuild + productbuild  
```bash
pkgbuild --root dist/MyTool.app --identifier com.acme.myapp --version 1.2.3 MyTool.pkg
productbuild --sign "Developer ID Installer" MyTool.pkg
```

10.1.3 Linux：AppImage 单文件  
```bash
wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
./appimagetool-x86_64.AppImage dist/MyTool.AppDir MyTool-x86_64.AppImage
```

--------------------------------------------------
10.2 插件化架构：运行时动态加载外部 `.py`

10.2.1 核心思路  
- 主程序仅打包最小依赖  
- 插件目录 `plugins/` 随安装包一起释放  
- 启动时 `importlib.import_module` 加载

10.2.2 spec 最小骨架  
```python
a = Analysis(
    ['main.py'],
    excludes=['sklearn', 'transformers'],  # 插件用
    datas=[('plugins', 'plugins')],
)
```

10.2.3 插件热更新流程  
1. 用户点击“检查更新”  
2. 下载 zip → 解压到 `plugins/`  
3. 重启主程序即可生效  
示例代码  
```python
import zipfile, pathlib, importlib
def install_plugin(zip_path):
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(pathlib.Path(__file__).parent / 'plugins')
    importlib.invalidate_caches()
```

--------------------------------------------------
10.3 商业级保护三板斧

10.3.1 代码混淆 + 加密字节码  
- pyinstaller 自带 `--key mypass`（弱加密，仅防窥）  
- 商业级：Nuitka + `--lto` + `--clang` 编译为原生二进制  

10.3.2 授权校验（在线 + 离线）  
- 在线：启动时调用 `https://license.xxx.com/activate`  
- 离线：RSA 公钥验证 license 文件  
示例（简化）  
```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
def check_license(lic_file):
    with open(lic_file, 'rb') as f:
        return pub_key.verify(f.read(), signature, padding.PKCS1v15(), hashes.SHA256())
```

10.3.3 反调试 & 反虚拟机  
- 检测调试器 (`ctypes.windll.kernel32.IsDebuggerPresent()`)  
- 检测沙箱 (`sys.platform == 'linux' and os.path.exists('/.dockerenv')`)  
> 注意：过度保护易被误报，需权衡。

--------------------------------------------------
10.4 一条龙示例仓库（可复制）

```
myapp-pro/
├─ src/
├─ plugins/           # 空目录，CI 打包时带空壳
├─ assets/
├─ installer.iss      # Inno Setup
├─ main.spec          # 已排除插件依赖
├─ .github/workflows/release.yml
└─ tools/
   ├─ build_pkg.sh    # macOS pkg
   └─ make_appimage.sh
```
`make all` 一键出：  
- `MyTool_Setup.exe`（带签名）  
- `MyTool.pkg`（已 Notarize）  
- `MyTool-x86_64.AppImage`

--------------------------------------------------
10.5 常见疑问 60 秒速答

Q1：插件需要重新打包吗？  
A：不需要，只要插件目录在 `_MEIPASS` 外即可。

Q2：Nuitka 和 pyinstaller 能混用吗？  
A：不能，但可把核心算法先用 Nuitka 打成 `.pyd`，再由 pyinstaller 收集。

Q3：加密后杀毒误报？  
A：提交 VT 白名单 + 代码签名 + 减少可疑 API 调用。

--------------------------------------------------
小结 & 作业

• 安装包：Inno / pkgbuild / AppImage 三选一即可  
• 插件化：主程序瘦身 + 动态加载  
• 商业保护：混淆 → 授权 → 反调试，按预算递进

作业：  
1. 用 Inno Setup 把自己的项目做成安装包  
2. 加一个“插件市场”按钮，能下载并热加载 zip 插件  
下节课《实战串讲》把 3 个真实项目（CLI、GUI、ML）完整复盘。


----

大家在学习课程中有任何问题，欢迎+微信和我交流👉[我的联系方式：微信、读者群、1对1、福利](http://www.python4office.cn/wechat-qrcode/)

![](https://cos.python-office.com/ads/gzh/sub-py.jpg)


