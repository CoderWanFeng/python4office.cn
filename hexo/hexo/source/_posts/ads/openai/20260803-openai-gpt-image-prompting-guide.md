---
title: GPT 图像生成模型提示词（Prompt）工程指南
date: 2026-08-03 10:00:00
tags: [openai, gpt图像生成, 提示词工程, ai绘画, 图像模型, 翻译]
categories: [AI工具评测]
keywords: [GPT图像生成, 提示词工程, gpt-image-2, AI绘画, OpenAI Cookbook]
description: OpenAI 官方 Cookbook《GPT 图像生成模型提示词指南》中文翻译。系统讲解 gpt-image-2 的参数、提示词基本原则，以及信息图、写实摄影、Logo、广告、UI 原型、风格迁移、虚拟试穿、产品精修、光照变换等 20+ 生产级用例与可运行代码。
cover: https://images.unsplash.com/photo-1456324504439-367cee3b3c32?q=80&w=1200&auto=format&fit=crop
---

> 📖 本文翻译自 OpenAI 官方 Cookbook：[GPT Image Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)（原文发布页）。
>
> 源码 Notebook 与示例图可在 [GitHub 仓库](https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb) 查看。文中所有「输出/输入效果图」均为运行对应代码后由模型生成，原文示例图见上方仓库链接。代码中的提示词已翻译为中文，gpt-image-2 原生支持中文提示词，可直接运行。

---

# GPT 图像生成模型提示词（Prompt）工程指南

## 1. 简介

OpenAI 的 gpt-image 系列图像生成模型，专为**生产级视觉内容**和**高度可控的创意工作流**而设计。它们既适合专业设计任务，也适合迭代式内容创作，并可根据工作流在「高质量渲染」与「低延迟」之间灵活取舍。

核心能力包括：

- **高保真写实**：自然的光照、准确的材质、丰富的色彩还原
- **灵活的质量—延迟权衡**：在低质量档位下也能更快出图，且视觉质量仍优于上一代图像模型
- **稳健的人脸与身份保留**：适用于编辑、角色一致性、多步骤工作流
- **可靠的文字渲染**：字距清晰、版式一致、对比强烈
- **复杂的结构化视觉**：包括信息图、示意图、多宫格拼图
- **精准的风格控制与风格迁移**：只需极少量提示词即可实现，从品牌设计系统到艺术风格都能覆盖
- **强大的现实世界知识与推理能力**：能准确描绘物体、环境与场景

本指南提炼了 `gpt-image-2` 在真实生产用例中的提示词模式、最佳实践和示例提示词。`gpt-image-2` 是目前能力最强的图像模型，图像质量更高、编辑表现更好、对生产工作流的支持更全面。其中 `low` 质量档位对延迟敏感的场景尤其好用，而当你需要最高保真度时，`medium` 和 `high` 仍是合适的选择。

## 1.1 OpenAI 图像模型参数

本节作为本指南所涵盖图像模型的参考，重点关注：

- 模型名称
- 支持的 `outputQuality` 取值
- 支持的 `input_fidelity` 取值
- 支持的 `size` / 分辨率行为
- 按工作流推荐的适用场景

### 模型概览

截至 2026 年 4 月 21 日，OpenAI 提供以下图像模型。

| 模型 | `outputQuality` | `input_fidelity` | 分辨率 | 推荐使用场景 |
| --- | --- | --- | --- | --- |
| `gpt-image-2` | `low`、`medium`、`high` | 不支持。该模型输出默认即为高保真，故 `input_fidelity` 不生效 | 满足下列约束的任意分辨率 | 新建项目时的默认推荐。用于最高质量的生成与编辑、文字密集图、写实摄影、图像合成、身份敏感编辑，以及「少重试比最低成本更重要」的工作流。 |
| `gpt-image-1.5` | `low`、`medium`、`high` | `low`、`high` | `1024x1024`、`1024x1536`、`1536x1024`、`auto` | 迁移期间保留已有的、经过验证的工作流。新项目优先用 `gpt-image-2`，尤其是质量、编辑可靠性或灵活尺寸重要的场景。 |
| `gpt-image-1` | `low`、`medium`、`high` | `low`、`high` | `1024x1024`、`1024x1536`、`1536x1024`、`auto` | 仅用于旧版兼容。若启动新工作流或更新提示词，请迁移到 `gpt-image-2`；仅在需要短期稳定性来验证升级时保留 `gpt-image-1`。 |
| `gpt-image-1-mini` | `low`、`medium`、`high` | `low`、`high` | `1024x1024`、`1024x1536`、`1536x1024`、`auto` | 当成本和吞吐量是主要约束时使用：大批量变体生成、快速构思、预览、轻量个性化，以及不需要最强生成/编辑性能的草稿素材。 |

### `gpt-image-2` 的尺寸选项

`gpt-image-2` 支持在 `size` 参数中传入任意分辨率，只要同时满足以下所有约束：

- 最长边必须小于 `3840px`
- 两条边都必须是 `16` 的倍数
- 长边与短边的比例不得超过 `3:1`
- 总像素数不得超过 `8,294,400`
- 总像素数不得低于 `655,360`

若输出图像超过 `2560x1440` 像素（即 `3,686,400` 总像素，俗称 2K），应视为**实验性**——超过该尺寸后结果可能更不稳定。

### `gpt-image-2` 常用尺寸

以下符合上述约束、便于参考的尺寸：

| 名称 | 分辨率 | 说明 |
| --- | --- | --- |
| HD 竖图 | `1024x1536` | 标准竖版选项 |
| HD 横图 | `1536x1024` | 标准横版选项 |
| 正方形 | `1024x1024` | 通用默认首选 |
| 2K / QHD | `2560x1440` | 流行的宽屏格式，也是 `gpt-image-2` 推荐的可靠性上限 |
| 4K / UHD | `3840x2160` | 实验性上限目标。若严格按「小于 3840」执行最大边规则，可向下取整到最近合法尺寸，如 `3824x2144` |

### 如何选择模型

- 大多数生产工作流默认选 `gpt-image-2`。它是综合能力最强的模型，也是当前使用 `gpt-image-1.5` 或 `gpt-image-1` 做高质量输出的团队的正确升级目标。
- 当「速度」和「单位成本」主导决策时，选 `gpt-image-2` 的 `quality: low`。该档位对大量用例质量已经足够，非常适合高吞吐量生成与实验。这些场景也可以尝试 `gpt-image-1-mini`，但我们实测 `quality: low` 效果同样出色。
- 仅在你验证提示词迁移、回归测试输出，或维护尚未准备好迁移的旧工作流时，保留 `gpt-image-1.5` 或 `gpt-image-1` 以做向后兼容。

### 从 `gpt-image-1.5` 与 `gpt-image-1` 的推荐升级路径

对于当前使用 `gpt-image-1.5` 或 `gpt-image-1` 的工作流，建议：

- 面向客户 assets、写实生成、重编辑流、品牌敏感创意、图中文字、以及「更好的首次通过率能减少人工复核或重跑」的工作流，升级到 `gpt-image-2`。
- 仅当主要目标是为大批量的探索性、低风险的图降低成本时，才考虑用 `gpt-image-1-mini` 替代旧模型。
- 迁移期间，先尽量保持提示词不变，待你在真实负载上对比了输出质量、延迟和重试率之后，再针对性调优。

## 2. 提示词基本原则

以下基本原则适用于 GPT 图像生成模型，源自在生成、编辑、信息图、广告、人物图、UI 原型和合成等工作流中反复出现的规律。

- **结构 + 目标**：按一致的顺序写提示词（背景/场景 → 主体 → 关键细节 → 约束），并写明预期用途（广告、UI 原型、信息图），以设定「模式」和精细程度。复杂需求用带简短标签的段落或换行，而不是一整段长句。

- **提示词格式**：用最容易维护的格式。极简提示词、描述性段落、类 JSON 结构、指令式提示词、标签式提示词都能用，只要意图和约束清晰。生产系统优先用「一眼能扫完的模板」，而不是花哨的提示词语法。

- **具体性 + 质量杠杆**：对材质、形状、纹理和视觉媒介（照片、水彩、3D 渲染）要具体，只在必要时加入有针对性的「质量杠杆」（如 *胶片颗粒*、*有质感的笔触*、*微距细节*）。要写实，直接在提示词里写「photorealistic（写实）」以强力触发模型的写实模式。类似表达如「真实照片」「用真实相机拍摄」「专业摄影」「iPhone 照片」也有帮助，但具体的相机参数可能被宽松解读，所以主要用于整体观感和构图，而非精确的物理模拟。

- **延迟 vs 保真度**：对延迟敏感或高吞吐场景，先用 `quality="low"` 评估是否满足视觉要求。多数情况下它能提供足够保真度且出图明显更快。对于小字号或密集文字、精细信息图、特写人像、身份敏感编辑和高分辨率输出，在发布前对比 `medium` 或 `high`。

- **构图**：指定取景与视角（特写、广角、俯拍）、透视/角度（平视、低角度），以及光照/氛围（柔和漫射、黄金时刻、高对比），以控制镜头。若版式重要，明确位置（如「logo 在右上角」「主体居中、左侧留白」）。对于宽幅、电影感、弱光、雨天或霓虹场景，要补充关于尺度、氛围和色彩的额外细节，以免模型用表面写实牺牲氛围。

- **人物、姿势与动作**：对于场景中的人物，描述尺度、身体取景、视线与物体互动。例如：「全身可见、包括脚」「相对于桌子是儿童体型」「低头看摊开的书、而非看镜头」「双手自然握住车把」。这些细节有助于身体比例、动作几何和视线对齐。

- **约束（什么该改、什么该保留）**：明确写出排除项与不变项（如「无 watermark」「无多余文字」「无 logo/商标」「保留身份/几何/版式/品牌元素」）。编辑时用「只改 X」+「其他一切保持不变」，并在每次迭代重复保留清单以减少漂移。若编辑要「外科手术式精确」，还要说明不要改动饱和度、对比度、版式、箭头、标签、相机角度或周围物体。

- **图中的文字**：把字面文字用**引号**或**全大写**标出，并把排版细节（字体风格、大小、颜色、位置）作为约束写明。对难词（品牌名、不常见拼写），逐字母拼出以提高字符准确度。小字号文字、密集信息面板、多字体版式用 `medium` 或 `high` 质量。

- **多图输入**：用**编号 + 描述**引用每张输入图（「图 1：产品照片……图 2：风格参考……」），并描述它们如何互动（「把图 2 的风格应用到图 1」）。合成时，明确哪些元素移到哪里（「把图 1 里的鸟放到图 2 的大象身上」）。

- **迭代而非一次性堆砌**：长提示词可以很好用，但从一个干净的基础提示词开始、用小的单点改动逐步精修（「让光照更暖」「去掉多余的树」「还原原始背景」），调试会更容易。用「和之前同款风格」「该主体」等引用借助上下文，但如果关键细节开始漂移，要重新写明。

## 3. 环境准备

运行一次即可。它会：

- 创建 API 客户端
- 在 images 文件夹下创建 `output_images/`
- 添加一个保存 base64 图片的小工具函数

把编辑用的参考图放进 `input_images/`（或更新示例中的路径）。

```python
import os
import base64
from openai import OpenAI

client = OpenAI()

os.makedirs("../../images/input_images", exist_ok=True)
os.makedirs("../../images/output_images", exist_ok=True)

def save_image(result, filename: str) -> None:
    """
    把返回的第一张图片保存到 output_images 文件夹下的指定文件名。
    """
    image_base64 = result.data[0].b64_json
    out_path = os.path.join("../../images/output_images", filename)
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(image_base64))

from IPython.display import HTML, Image, display

def display_image_grid(items, width=240):
    cards = []
    for item in items:
        title = item.get("title", "")
        label = f'<div style="font-weight:600;margin-bottom:8px">{title}</div>' if title else ""
        cards.append(
            '<div style="text-align:center">'
            + label
            + f'<img src="{item["path"]}" width="{width}" style="max-width:100%;height:auto;" />'
            + '</div>'
        )
    display(HTML('<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start">' + ''.join(cards) + '</div>'))
```

> 以下示例均使用我们能力最强的图像模型 `gpt-image-2`。

## 4. 用例 — 生成（文本 → 图像）

## 4.1 信息图（Infographics）

用信息图向特定受众解释结构化信息：学生、高管、客户或大众。示例包括科普图、海报、带标注的示意图、时间线和「可视化维基」素材。对于密集版式或图中大量文字，建议把生成质量设为 `high`。

```python
prompt = """
制作一张详细的自动咖啡机（类似 Jura）工作原理与流程图信息图。
从豆仓、研磨、称重、水箱、锅炉等环节，
让我从技术和视觉上理解整个流程。
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "infographic_coffee_machine_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。原始示例图见 [OpenAI Cookbook 仓库](https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb)。

## 4.2 图中的文字翻译（Translation in Images）

用于将已有设计（广告、UI 截图、包装、信息图）本地化到另一种语言，而无需从零重建版式。关键是**除了文字之外全部保留**——保持字体风格、位置、间距和层级一致——同时逐字、准确地翻译，不增减词、非必要不重排，也绝不意外改动 logo、图标或图像。

```python
prompt = """
把信息图中的文字翻译成西班牙语。图片的其他任何部分都不要改动。
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../images/output_images/infographic_coffee_machine_gpt-image-2.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)


save_image(result, "infographic_coffee_machine_sp_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 4.3 自然写实的照片（Photorealistic Images that Feel "Natural"）

要获得可信的写实效果，像「正在此刻捕捉一张真实照片」那样写提示词。使用摄影语言（镜头、光照、取景），并明确要求真实的质感（毛孔、皱纹、织物磨损、瑕疵）。避免暗示影棚打磨或摆拍的词。细节重要时，设置 `quality="high"`。

```python
prompt = """
创作一张写实风格的抓拍照片：一位年长的老水手站在小渔船上。
他皮肤饱经风霜，可见皱纹、毛孔和日晒纹理，手臂上有几处淡化的传统水手纹身。
他正平静地整理渔网，狗在旁边甲板上蹲着。用 35mm 胶片摄影的手法拍摄，
平视中近景，50mm 镜头。柔和的沿海日光、浅景深、细微胶片颗粒、自然的色彩平衡。
画面应显得真诚、不摆拍，有真实的皮肤质感、磨损的材质和日常细节。不要美化，不要重度修图。
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "photorealism-gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 4.4 世界知识（World Knowledge）

GPT 图像生成模型能把强大的推理与现实世界知识结合起来。例如，当要求生成「1969 年 8 月纽约州 Bethel 的场景」时，它能推断出 Woodstock（伍德斯托克音乐节），并在没有明确告知该事件的情况下，生成准确、符合语境的图像。

```python
prompt = """
创作一个写实的户外人群场景，地点是 1969 年 8 月 16 日纽约州 Bethel。
写实风格，服装、布景和环境符合时代特征。
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "world_knowledge-gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 4.5 Logo 生成

优秀的 Logo 生成来自清晰的品牌约束与简洁。先描述品牌的个性与用途，再要求一个干净、原创的标记，具有强形状、平衡的留白，以及跨尺寸的缩放能力。

你可以通过参数 `n` 指定要生成的变体数量。

```python
prompt = """
为一家叫 Field & Flour 的本地面包店，创作一个原创、不侵权的 logo。
logo 应给人温暖、简洁、永恒的感觉。使用干净的、类矢量的形状、醒目的轮廓和平衡的留白。
宁可简单也不要堆细节，确保在小尺寸和大尺寸下都清晰可读。扁平设计、极简线条，除非必要不使用渐变。
纯色背景。交付一个居中、留白充足的单一 logo。无 watermark。
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
    n=4     # 生成 4 个版本的 logo
)

# 把 4 张图分别保存
for i, item in enumerate(result.data, start=1):
    image_base64 = item.b64_json
    image_bytes = base64.b64decode(image_base64)
    with open(f"../../images/output_images/logo_generation_{i}_gpt-image-2.png", "wb") as f:
        f.write(image_bytes)
```

> 🖼️ **输出 4 个 Logo 变体**：运行上方代码生成。

## 4.6 广告生成（Ads Generation）

广告生成在提示词「写得像一份创意简报」而非「纯技术图像规格」时效果最好。描述品牌、受众、文化、概念、构图和确切文案，然后让模型在这些边界内做出有品味的创意决策。这对早期 campaign 探索很有用，因为模型能解读受众线索、推断美术方向，并提出让广告显得「经过考量」而非「仅仅被渲染」的视觉细节。

要获得更强效果，把品牌定位、想要的调性、目标受众、场景和标语都写进同一条提示词。如果文字必须出现在图中，精确引用它，并要求干净、清晰的排版。

```python
prompt = """
为叫 Thread 的品牌做一张有文化感的酷炫广告 / 时尚大片。
这是一个时髦的年轻街头品牌。广告展现一群朋友聚在一起玩，
标语是 "Yours to Create."
让它像一张面向年轻街头服饰受众的精致 campaign 图：时尚、当代、有活力、有品味。
使用干净的构图、强烈的色彩方向、自然的姿势和高端时尚摄影的质感。
把标语精确渲染一次，清晰可读，融入广告版式。
不要多余文字，不要 watermark，不要无关 logo。
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "thread_ad_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 4.7 故事转漫画分镜（Story-to-Comic Strip）

做故事转漫画时，把叙事定义成一系列清晰的视觉节拍，每格一个。描述要具体、以动作导向，这样模型才能把故事翻译成可读、节奏得当的分镜。

```python
prompt = """
创作一个 4 格等宽竖版漫画分镜。
第 1 格：主人从前门离开。宠物被框在身后的窗户里，在玻璃后显得很小，眼睛睁大，爪子高高扒着，屋里突然安静下来。
第 2 格：门咔哒关上。寂静被打破。宠物缓缓转向空荡的屋子，姿态一变，眼神敏锐、似有所图。
第 3 格：屋子变了样。宠物像当家作主一样瘫在沙发上，旁边有碎屑，阳光像聚光灯一样斜切过房间。
第 4 格：门开了。宠物端坐在门口，警觉而镇定，仿佛什么都没发生过。
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "comic_reel-gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 4.8 UI 原型（UI Mockups）

UI 原型在「把产品描述得好像它已经存在」时效果最好。聚焦版式、层级、间距和真实的界面元素，避免概念艺术语言，这样结果看起来像可用、已上线的界面，而非设计草图。

```python
prompt = """
为一个本地农贸市场的移动 App 创作写实的 UI 原型。
展示今日市场：简单的页头、带小图和分类的供应商短列表、一个「今日特价」小板块，以及位置和营业时间的基本信息。
设计要实用、易用。白色背景、微妙的自然点缀色、清晰的字体、最少的装饰。
它应像一个真实、设计精良、美观的小型本地市场 App。
把 UI 原型放进 iPhone 边框里。
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "ui_farmers_market_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 4.9 科学 / 教育视觉（Scientific / Educational Visuals）

科学和教育视觉非常适合生物、化学、课堂科普、扁平科学图标系统、示意图和学习素材。把它们当教学设计的简报来写：定义受众、教学目标、视觉格式、所需标签和科学约束。要获得最佳效果，要求一套干净、扁平的视觉系统，图标风格一致、箭头清晰、标签可读，并留足空白让学生能快速扫读概念。

准确性重要时，显式列出所需组件，并说明不应包含什么。对于密集标签、示意图，或将用于幻灯片或课程素材的素材，使用 `quality="high"`。

```python
prompt = """
为高中生创作一张名为「细胞呼吸一览」的简单生物示意图。

展示葡萄糖如何在细胞内转化为能量。包含糖酵解、三羧酸循环（Krebs cycle）和电子传递链。
用箭头连接各步骤，并标注主要分子：葡萄糖、丙酮酸、ATP、NADH、FADH2、CO2、O2、H2O。
让它像一份干净的课堂讲义或幻灯片，白色背景、简洁图标、清晰标签、易读文字。

避免小字号文字、多余装饰，或任何让示意图难以理解的东西。
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1536x1024",
    quality="high",
)

save_image(result, "scientific_educational_cellular_respiration_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 4.10 幻灯片、示意图、图表与生产力图像（Slides, Diagrams, Charts）

生产力视觉在提示词「写得像一份制品规格」而非「插图请求」时效果最好。写明确切交付物（幻灯片、工作流图、图表、页面图）、定义画布与层级、提供真实文字或数据，并描述视觉语言。这些提示词应包含实用约束：可读排版、精致间距、无装饰性杂乱、不做通用图库照处理。

对于幻灯片、图表和重示意图的素材，把数字和标签直接写进提示词。deck 风格的输出用横版尺寸，当图像含小字号文字、图例、坐标轴或脚注时用 `quality="high"`。

```python
prompt = """
创作一张名为 **「市场机会（Market Opportunity）」** 的融资演讲稿单页，
看起来像一家 YC 孵化、已拿到 Series A 的初创公司的真实单页。

使用干净的白色背景、类似 Inter 的现代无衬线字体，以及清晰、极简的版式。单页应包含：

* 一个 TAM/SAM/SOM 的同心圆示意图，用柔和的蓝灰色
* 具体、可信的市场规模数字：

  * **TAM：** $42B
  * **SAM：** $8.7B
  * **SOM：** $340M
* 下方一个展示 2021 到 2026 市场增长的干净柱状图，带微妙上升趋势
* 小字脚注：**「AGI Research, 2024」** 和 **「Internal analysis」**
* 右下角的公司 logo 占位符

设计应像真正能融到钱的 deck：文字高度可读、数据层级清晰、间距精致、专业的初创风格视觉语言。

避免剪贴画、图库摄影、渐变、阴影、装饰元素，或任何显得通用或过度设计的东西。
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1536x864",
    quality="high",
)

save_image(result, "market_opportunity_slide_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 5. 用例 — 编辑（文本 + 图像 → 图像）

## 5.1 风格迁移（Style Transfer）

当你想保留参考图的*视觉语言*（色板、纹理、笔触、胶片颗粒等）而改变主体或场景时，风格迁移很有用。要获得最佳效果，写明什么必须保持一致（风格线索）和什么必须改变（新内容），并加上硬约束如背景、取景和「无多余元素」以防止漂移。

```python
prompt = """
使用输入图的相同风格，生成一个人骑摩托车、白色背景的图像。
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../images/input_images/pixels.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "motorcycle_gpt-image-2.png")
```

> 📥 **输入图片**：需将参考图 `pixels.png` 放入 `input_images/` 目录（见原文仓库 `examples/multimodal/images/`）。
>
> 🖼️ **输出效果图**：运行上方代码即可生成。

## 5.2 虚拟试穿（Virtual Clothing Try-On）

虚拟试穿非常适合身份保留至关重要的电商预览。关键是明确「锁定人物」（脸、体型、姿势、发型、表情），只允许改动*服装*，然后要求真实的贴合度（垂坠、褶皱、遮挡）以及一致的光照/阴影，让衣服看起来是自然穿着，而非贴上去的。

```python
prompt = """
编辑图像，用提供的服装图给这位女性换装。不要以任何方式改变她的脸、面部特征、肤色、体型、姿势或身份。
保留她完全一致的样貌、表情、发型和比例。只替换服装，让衣物自然地贴合她现有的姿势和身体几何，
呈现真实的布料行为。匹配原照片的光照、阴影和色温，使服装以写实方式融合，而非像贴上去的。
不要改变背景、相机角度、取景或图像质量，也不要添加配饰、文字、logo 或 watermark。
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../images/input_images/woman_in_museum.png", "rb"),
        open("../../images/input_images/tank_top.png", "rb"),
        open("../../images/input_images/jacket.png", "rb"),
        open("../../images/input_images/tank_top.png", "rb"),
        open("../../images/input_images/boots.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "outfit_gpt-image-2.png")
```

> 📥 **输入图片**：需将 `woman_in_museum.png`、`tank_top.png`、`jacket.png`、`boots.png` 放入 `input_images/` 目录。
>
> 🖼️ **输出效果图**：运行上方代码即可生成。

## 5.3 草图转图像（Drawing → Image / Rendering）

草图转渲染工作流非常适合把粗糙手绘变成写实概念，同时保留原始意图。把提示词当规格来写：保留版式和透视，然后通过指定合理的材质、光照和环境*增加写实感*。加上「不要新增元素/文字」以避免创意性重新诠释。

```python
prompt = """
把这张草图变成写实图像。
保留精确的版式、比例和透视。
选择与原草图意图一致的写实材质和光照。
不要新增元素或文字。
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../images/input_images/drawings.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "realistic_valley_gpt-image-2.png")
```

> 📥 **输入图片**：需将 `drawings.png` 放入 `input_images/` 目录。
>
> 🖼️ **输出效果图**：运行上方代码即可生成。

## 5.4 产品精修（Product Mockups，干净背景 + 标签完整）

产品抠图与精修常用于商品目录、电商平台和设计系统。成功取决于边缘质量（干净的轮廓、无碎片/光晕）和标签完整性（文字保持清晰不变）。对于 `gpt-image-2`，让输出背景不透明；若需要最终透明素材，再用下游去背步骤。若要写实而不重新设计风格，要求只做轻度打磨，并可选地在平面背景上加一层微妙的接触阴影。

```python
prompt = """
从输入图中抠出产品，放到纯白不透明背景上。
输出：居中产品、清晰轮廓、无光晕/碎片。
精确保留产品几何与标签可读性。
只做轻度打磨和一层微妙的写实接触阴影。
不要重新设计产品风格；只去背景并轻度打磨。
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../images/input_images/shampoo.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
    background="opaque",
)

save_image(result, "extract_product_gpt-image-2.png")
```

> 📥 **输入图片**：需将 `shampoo.png` 放入 `input_images/` 目录。
>
> 🖼️ **输出效果图**：运行上方代码即可生成。

## 5.5 含真实图中文字的营销创意（Marketing Creatives with Real Text In-Image）

带真实图中文字的营销创意很适合快速广告构思，但排版需要显式约束。把确切文案放进引号、要求逐字渲染（无多余字符），并描述位置和字体风格。若文字保真度不理想，保持提示词严格并迭代——小的措辞/版式微调通常能提升可读性。

```python
prompt = """
创作一张写实的广告牌原型：洗发水放在高速公路旁日落场景中的广告牌上。
广告牌文字（精确、逐字、无多余字符）：
"Fresh and clean"
排版：粗体无衬线、高对比、居中、字距干净。
确保文字只出现一次且完全清晰可读。
无 watermark，无 logo。
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../images/input_images/shampoo.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "billboard_gpt-image-2.png")
```

> 📥 **输入图片**：复用 `shampoo.png`。
>
> 🖼️ **输出效果图**：运行上方代码即可生成。

## 5.6 光照与天气变换（Lighting and Weather Transformation）

用于为照片重新布景，呈现不同的情绪、季节或时段变体（如晴天 → 阴天、白天 → 黄昏、晴朗 → 下雪），同时保持场景构图不变。关键是只改变环境条件——光照方向/质量、阴影、氛围、降水和地面湿度——同时保留身份、几何、相机角度和物体位置，使其仍读作同一张原始照片。

```python
prompt = """
让它看起来像一个冬夜，正在下雪。
"""

result = client.images.edit(
    model="gpt-image-2",
    input_fidelity="high", 
    image=[
        open("../../images/output_images/billboard_gpt-image-2.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "billboard_winter_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 5.7 物体移除（Object Removal）

物体移除用于「只去掉画面中某个元素、其他一切保持不变」的场景，例如去掉人物手中多余的花、移除干扰物等。关键是明确「只移除 X」，并重复保留清单（身份、几何、光照、构图、背景均不变），以避免漂移。

```python
prompt = """
把男人手中的花去掉。其他什么都不要改。
"""

result = client.images.edit(
    model="gpt-image-2",
    input_fidelity="high", 
    image=[
        open("../../images/output_images/man_with_blue_hat.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "man_with_no_flower_gpt-image-2.png")
```

> 📥 **输入图片**：需将 `man_with_blue_hat.png` 放入 `output_images/` 目录（或由前序步骤生成）。
>
> 🖼️ **输出效果图**：运行上方代码即可生成。

## 5.8 把人物放进场景（Insert the Person Into a Scene）

人物入镜合成适用于故事板、campaign，以及「面部/身份保留很重要」的假设性场景。通过指定扎实的摄影观感（自然光照、可信细节、无电影感调色）来锚定写实度，并锁定主体不可改变的部分。在进行较大场景编辑时，更高的输入保真度有助于保持相似度。

```python
prompt = """
生成一张高度写实的动作场景：这个人正从一头庞大、写实的棕熊袭击营地的场景中逃跑。
图像应像某人真实拍到的照片，而非过度增强或电影海报式的图像。
她居中于画面但背对镜头，穿着户外露营装，脸上有泥、衣服有破口。她显然害怕但专注于逃脱，
正逃离在她身后摧毁营地的熊。
营地在优胜美地国家公园（Yosemite National Park），有可信的自然细节。时间是黄昏，自然光照、真实色彩。
一切都应显得扎实、真实、未加风格化，仿佛捕捉于真实瞬间。避免电影感光照、戏剧化调色或风格化构图。
"""

result = client.images.edit(
    model="gpt-image-2",
    input_fidelity="high", 
    image=[
        open("../../images/input_images/woman_in_museum.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "scene_gpt-image-2.png")
```

> 📥 **输入图片**：复用 `woman_in_museum.png`。
>
> 🖼️ **输出效果图**：运行上方代码即可生成。

## 5.9 多图引用与合成（Multi-Image Referencing and Compositing）

用于将多个输入中的元素组合成一张可信的图像——非常适合「把这个物体/人放进那个场景」的工作流，而无需重新生成一切。关键是明确指定要移植什么（图 2 里的狗）、它应去哪里（图 1 里女人正旁边）、以及什么必须保持不变（场景、背景、取景），同时匹配光照、透视、尺度和阴影，使合成看起来像在原始照片中自然捕捉到的。

```python
prompt = """
把第二张图里的狗放进第一张图的场景中，紧挨着女人，使用相同的光照、构图和背景风格。其他什么都不要改。
"""

result = client.images.edit(
    model="gpt-image-2",
    input_fidelity="high", 
    image=[
        open("../../images/output_images/test_woman.png", "rb"),
        open("../../images/output_images/test_woman_2.png", "rb"),
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)


save_image(result, "test_woman_with_dog_gpt-image-2.png")
```

> 📥 **输入图片**：需将 `test_woman.png`、`test_woman_2.png` 放入 `output_images/` 目录。
>
> 🖼️ **输出效果图**：运行上方代码即可生成。

## 6. 其他高价值用例

## 6.1 室内设计「替换」（Interior Design "Swap"，精准编辑）

用于在不重新渲染整个场景的情况下，可视化真实空间中的家具或装饰变化。目标是「外科手术式」的写实：替换单个物体，同时保留相机角度、光照、阴影和周围上下文，使编辑看起来像真实照片，而非重新设计。

```python
prompt = """
在这张房间照片中，只把白色（椅子）替换成木制椅子。
保留相机角度、房间光照、地面阴影和周围物体。
图像其他所有方面保持不变。
写实的接触阴影和织物纹理。
"""

result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../images/input_images/kitchen.jpeg", "rb"),
    ],
    prompt=prompt,
    size="1536x1024",
    quality="medium",
)

save_image(result, "kitchen-chairs_gpt-image-2.png")
```

> 📥 **输入图片**：需将 `kitchen.jpeg` 放入 `input_images/` 目录。
>
> 🖼️ **输出效果图**：运行上方代码即可生成。

## 6.2 3D 立体弹出式节日卡片（3D Pop-up Holiday Card，产品风格原型）

适合季节性营销概念和印刷预览。强调触感写实——纸张层、纤维、折痕和柔和的影棚光照——使结果读起来像被拍摄的实体产品，而非扁平插画。

```python
scene_description = (
    "一个温馨的圣诞场景：一只略显陈旧的小泰迪熊坐在纪念盒里，"
    "绒毛微微磨损，有柔软的缝补痕迹，放在窗边，窗外飘着雪。"
    "场景暗示孩子已经长大，但回忆仍在。"
)

short_copy = "Merry Christmas — some memories never fade."

prompt = f"""
创作一张圣诞节日卡片插画。

场景：
{scene_description}

氛围：
温暖、怀旧、温柔、感性。

风格：
高端节日卡片摄影，柔和的电影感光照，
真实的质感，浅景深，
得体的散景光点，高印刷质量的构图。

约束：
- 仅原创作品
- 无商标
- 无 watermark
- 无 logo

只包含这段卡片文字（逐字）：
"{short_copy}"
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "christmas_holiday_card_teddy_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 6.3 收藏级人偶 / 毛绒挂件（Collectible Action Figure / Plush Keychain，周边概念）

用于早期周边构思和提案视觉。聚焦高端产品摄影质感（材质、包装、印刷清晰度），同时保持设计原创、不侵权。很适合快速测试多个角色或包装变体。

```python
# ---- 输入 ----
character_description = (
    "一架复古风格的玩具螺旋桨飞机，圆润的机翼，"
    "前置旋转螺旋桨，漆面边缘略有磨损，"
    "经典的童年比例，设计为怀旧节日收藏品"
)

short_copy = "Christmas Memories Edition"

# ---- 提示词 ----
prompt = f"""
创作一个收藏级人偶：{character_description}，装在吸塑包装（blister packaging）中。

概念：
一个怀旧的节日收藏品，灵感来自孩子们过去在冬季节日里玩的简易玩具飞机。
唤起温暖、想象力和童年的惊奇。

风格：
高端玩具摄影，真实的塑料和喷漆金属质感，
影棚光照，浅景深，
清晰的标签印刷，高端零售陈列感。

约束：
- 仅原创设计
- 无商标
- 无 watermark
- 无 logo

只包含这段包装文字（逐字）：
"{short_copy}"
"""

result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "christmas_collectible_toy_airplane_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 6.4 童书插画与角色一致性（Children's Book Art with Character Consistency，多图工作流）

为多页插画流水线设计，其中角色漂移不可接受。可复用的「角色锚点」确保跨场景、跨姿势、跨页面的视觉连续性，同时允许环境和叙事变化。

### 1️⃣ 角色锚点 — 建立可复用的主角

目标：锁定角色的外貌、比例、服装和基调。

```python
prompt = """
创作一张童书插画，介绍一位主角。

角色：
一位年轻的、绘本风格英雄，灵感来自小小的森林绿林好汉，
穿着简单的绿色带帽束腰外衣、柔软的棕色靴子和个小腰带包。
角色神情和善、眼神温柔，勇敢而温暖。
携带一把只用于帮助、绝不伤害的小木弓。

主题：
该角色保护和救助松鼠、小鸟、兔子等小型森林动物。

风格：
童书插画，手绘水彩感，
柔和的轮廓，温暖的大地色系，奇幻而友好。
适合绘本的比例（略大的头部、富有表现力的脸）。

约束：
- 原创角色（无版权角色）
- 无文字
- 无 watermark
- 纯森林背景以清晰展示角色
"""

# ---- 图像生成 ----
result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "childrens_book_illustration_1_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

### 2️⃣ 故事延续 — 复用角色，推进叙事

目标：同一角色，新场景 + 新动作。角色外貌必须保持不变。

```python
prompt = """
用同一角色继续童书故事。

场景：
同一位年轻森林英雄正温柔地帮助一只受惊的松鼠，
它在一场冬暴后卡在了倒下的树里。
角色单膝跪在松鼠旁，给予安抚。

角色一致性：
- 同样的绿色带帽外衣
- 同样的面部特征、比例和配色
- 同样的温柔、英勇个性

风格：
童书水彩插画，
柔和光照，雪中森林环境，
温暖而令人安心的氛围。

约束：
- 不要重新设计角色
- 无文字
- 无 watermark
"""

# ---- 图像生成 ----
result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("../../images/output_images/childrens_book_illustration_1_gpt-image-2.png", "rb"),  # 使用第 1 步的图像
    ],
    prompt=prompt,
    size="1024x1536",
    quality="medium",
)

save_image(result, "childrens_book_illustration_2_gpt-image-2.png")
```

> 🖼️ **输出效果图**：运行上方代码即可生成。

## 结语

在本 Notebook 中，我们演示了如何使用 gpt-image 图像生成模型，构建在真实生产环境中站得住脚的高质量、可控的图像生成与编辑工作流。本 Cookbook 强调以**提示词结构、显式约束和小的迭代改动**作为控制写实度、版式、文字准确度和身份保留的主要工具。我们覆盖了生成和编辑两类模式，从信息图、写实摄影、UI 原型、Logo，到翻译、风格迁移、虚拟试穿、合成和光照变换。贯穿所有示例，本 Cookbook 一再强调**清晰区分「什么该改变」与「什么必须保持不变」**，并在每次迭代中重申这些不变项以防止漂移。我们也强调了质量与输入保真度设置如何让你根据用例，在延迟与视觉精度之间做有意的权衡。这些示例共同构成了一份实用、可复现的 playbook，用于在生产的图像工作流中应用 gpt-image 图像生成模型。
