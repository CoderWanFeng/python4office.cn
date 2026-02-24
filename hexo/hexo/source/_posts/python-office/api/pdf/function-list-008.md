---
title: python-office库中，pdf转word怎么用？
date: 2026-01-10 06:25:17
tags: python-office
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
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="http://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>


大家好，这里是程序员晚枫，正在all in [AI编程实战](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)，小红书/小破站都叫这个名。

---

## pdf2docx 使用说明

### 功能简介

`pdf2docx` 用于将 PDF 文件转换为 Word（`.docx`）文档。  
支持：

- 单个 PDF 文件转换为单个 DOCX 文件
- 通过输入输出目录进行批量转换（依赖底层 `popdf.pdf2docx` 的实现）
- 保持对旧参数 `file_path` 的向后兼容（已弃用，不推荐继续使用）

---

### 函数签名

```python
from office.api.pdf import pdf2docx

pdf2docx(
    input_file: str | None = None,
    output_file: str | None = None,
    input_path: str | None = None,
    output_path: str = '.',
    file_path: str | None = None,  # 已弃用
)
```

---

### 参数说明

- `input_file`：  
  - 类型：`str`  
  - 说明：输入的单个 PDF 文件路径（包含文件名和扩展名）。  
  - 示例：`"D:/docs/input.pdf"`  
  - 注意：当前实现中，这是**必填参数**（除非你依赖底层 `popdf` 的目录模式，用 `input_path` + `output_path`）。

- `output_file`：  
  - 类型：`str`，可选  
  - 说明：输出的单个 Word 文件完整路径（包含文件名和 `.docx` 扩展名）。  
  - 若传入该参数，则优先使用此路径作为输出文件位置。

- `input_path`：  
  - 类型：`str`，可选  
  - 说明：批量转换时的 PDF 输入目录路径。  
  - 使用方式取决于底层 `popdf.pdf2docx` 的具体实现（目录批量模式）。

- `output_path`：  
  - 类型：`str`，可选，默认值：`'.'`  
  - 说明：  
    - 当只传 `input_file` 且未传 `output_file` 时：  
      函数会自动将输出文件路径设置为  
      `output_path` + `input_file` 的文件名（去掉原扩展名，追加 `.docx`）。  
      例如：  
      - `input_file="D:/docs/a.pdf"`  
      - `output_path="E:/out"`  
      - 最终输出：`E:/out/a.docx`  
    - 当使用目录模式时（`input_path` + `output_path`），会传递给底层 `popdf.pdf2docx` 进行处理。

- `file_path`（已弃用）：  
  - 类型：`str`，可选  
  - 说明：旧版使用的 PDF 输入路径参数，已被 `input_file` 替代。  
  - 当前行为：  
    - 如果传入了 `file_path`，且未传 `input_file`，函数会自动将 `file_path` 的值赋给 `input_file`，并发出 `DeprecationWarning` 警告。  
    - 新代码中不推荐继续使用 `file_path`，请统一改为 `input_file`。

---

### 调用优先级与分支逻辑

根据当前实现，参数组合的处理顺序如下：

1. **处理弃用参数 `file_path`**  
   - 如果 `file_path` 不为 `None` 且 `input_file` 为空：  
     - 发出弃用警告  
     - 用 `file_path` 填充 `input_file`

2. **必须提供 `input_file`**  
   - 若最终 `input_file` 仍为 `None`：  
     - 直接抛出：  
       ```python
       ValueError("必须提供 input_file 参数来指定PDF文件路径")
       ```

3. **优先使用 `input_file` + `output_path` 模式（当前兼容路径组合逻辑）**

   ```python
   if input_file is not None and output_path is not None:
       input_path_obj = Path(input_file)
       output_file = str(Path(output_path) / f"{input_path_obj.stem}.docx")
       popdf.pdf2docx(input_file=input_file, output_file=output_file)
   ```

4. **若显式提供了 `output_file`，则优先使用：**

   ```python
   elif input_file is not None and output_file is not None:
       popdf.pdf2docx(input_file=input_file, output_file=output_file)
   ```

5. **目录模式（依赖底层库的批量实现）：**

   ```python
   elif input_path is not None and output_path is not None:
       popdf.pdf2docx(input_path=input_path, output_path=output_path)
   ```

---

### 使用示例

#### 1. 最常用：单个 PDF → 同名 DOCX（指定输出目录）

```python
from office.api.pdf import pdf2docx

pdf2docx(
    input_file=r"D:\docs\report.pdf",
    output_path=r"D:\output"
)
# 结果：在 D:\output 目录下生成 report.docx
```

#### 2. 单个 PDF → 指定完整输出文件名

```python
from office.api.pdf import pdf2docx

pdf2docx(
    input_file=r"D:\docs\report.pdf",
    output_file=r"D:\output\my_report_v2.docx"
)
# 结果：生成 D:\output\my_report_v2.docx
```

#### 3. 兼容旧代码：使用已弃用的 `file_path`

```python
from office.api.pdf import pdf2docx

pdf2docx(
    file_path=r"D:\docs\old_api.pdf",
    output_path=r"D:\output"
)
# 行为等同于：
# pdf2docx(input_file=r"D:\docs\old_api.pdf", output_path=r"D:\output")
# 同时会抛出 DeprecationWarning，提示不要再使用 file_path
```

#### 4. 目录模式（依赖底层 popdf 行为）

```python
from office.api.pdf import pdf2docx

pdf2docx(
    input_path=r"D:\pdf_folder",
    output_path=r"D:\output_folder"
)
# 具体批量转换行为由 popdf.pdf2docx 决定
```

---

如果你希望，我可以再帮你把这份使用文档，整理成适合直接放到 README / API 文档里的 Markdown 版本（当前答案已经基本是 Markdown 格式，你可以直接复制过去用）。

-------

以上所有仓库的功能介绍，我都加入了原创课程:[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)都是1行Python代码就能实现的，适合纯小白的课程，需要可以加入学习哟~

- 加入学习👉[给小白的《50讲Python自动化办公》](https://mp.weixin.qq.com/s/3eVM6XX8DHRVjp2PDWOhsA)

大家学习 或 使用代码过程中，有任何问题，都可以加入读者群交流哟~👇


![](https://cos.python-office.com/group/0816.jpg)

![](https://cos.python-office.com/course/50%E8%AE%B2%E8%87%AA%E5%8A%A8%E5%8C%96%E5%8A%9E%E5%85%AC/free-link.jpg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/BXWg_LXreNCI-UlrckZrTw)就能上手做AI项目。