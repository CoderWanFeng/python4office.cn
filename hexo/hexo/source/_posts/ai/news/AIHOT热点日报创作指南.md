# AIHOT 热点日报创作指南

> 本指南记录如何使用 `ai-hotspot-tracker` Skill 搜索 AI 热点，并把它写成 python4office.cn 的日报文章。
>
> 适用场景：每天从 AIHOT 拉取当日热点，筛选适合 Python/AI 办公自动化读者的选题，输出成 Hexo 文章。

---

## 一、这个技能能做什么？

`ai-hotspot-tracker` 连接 [AIHOT](https://aihot.virxact.com) 的数据源，可以：

| 能力 | 说明 |
|------|------|
| 拉日报 | 获取当天 AI 圈精选条目 |
| 拉 24h 精选 | 获取最近 24 小时官方精选 |
| 拉全量 | 获取指定时间窗口内的所有条目，含摘要、评分、分类、来源、链接 |
| 筛选选题 | 基于评分、分类、话题相关性，判断哪些值得写 |
| 生成文章 | 按 Hexo 格式写入 `hexo/hexo/source/_posts/ai/news/YYYYMMDD-ai-hotspot-daily.md` |

---

## 二、一句话用法

装完 Skill 后直接说：

```text
今天 AI 圈有啥适合写 python4office.cn 教程的？
```

也可以更具体：

```text
今天的 AI 热点，全部记录下来，放在 hexo/hexo/source/_posts/ai/news/
```

---

## 三、完整工作流程

### 步骤 1：拉数据

优先用这两个接口：

- **日报接口**：`https://aihot.virxact.com/api/public/daily`
- **精选接口**：`https://aihot.virxact.com/api/public/items?mode=selected&since=<24h 前的 ISO 时间>`
- **全量接口**：`https://aihot.virxact.com/api/public/items?mode=all&since=<时间>`

建议用 Python `urllib` 直接调，因为当前脚本路径可能不存在，但 API 是稳定的。

```python
import urllib.request, json, urllib.parse
from datetime import datetime, timedelta, timezone

BASE = 'https://aihot.virxact.com'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Accept': 'application/json',
}

def get(path, params=None):
    url = BASE + path
    if params:
        url += '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

# 全量拉取最近 30 小时
since = (datetime.now(timezone.utc) - timedelta(hours=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
data = get('/api/public/items', {'mode': 'all', 'since': since})
items = data.get('items', [])
```

### 步骤 2：按北京时间过滤出"今天"

```python
def to_cst(iso):
    dt = datetime.fromisoformat(iso.replace('Z', '+00:00'))
    return dt.astimezone(timezone(timedelta(hours=8)))

today = '2026-06-21'  # 改成当天
today_items = []
for item in items:
    pub = item.get('publishedAt', '')
    if not pub:
        continue
    cst = to_cst(pub)
    if cst.date().isoformat() == today:
        item['cst_time'] = cst.strftime('%H:%M')
        today_items.append(item)
```

### 步骤 3：按 python4office.cn 读者群筛选选题

参考下表：

| 标签 | 写不写 | 原因 |
|------|--------|------|
| 有代码/可复现 | ✅ 强推 | 读者能跟着跑，转化率高 |
| 国产开源/平替国外工具 | ✅ 强推 | 粉丝对国产替代天然感兴趣 |
| 大厂 AI 应用（美团、阿里、腾讯） | ✅ 可写 | 贴近国内读者使用场景 |
| Agent / MCP / RAG 工程方案 | ✅ 强推 | 当前 hottest 工程话题 |
| 纯人事变动 | ❌ 不写 | 无代码，无教程角度 |
| 医疗/健康问答 | ❌ 不写 | 合规禁忌 |
| 纯政策/法案 | ❌ 不写 | 无技术切入点 |
| 硬件发布 | ❌ 不写 | 和 Python/办公自动化无关 |
| 纯营销/节日活动 | ❌ 不写 | 无价值 |

### 步骤 4：生成文章

输出到：

```text
hexo/hexo/source/_posts/ai/news/YYYYMMDD-ai-hotspot-daily.md
```

文件命名规则：`YYYYMMDD-ai-hotspot-daily.md`

---

## 四、文章结构模板

### 标题公式

标题必须突出"AI 新闻/AI 热点"属性，建议结构：

```
时间 + AI热点/AI日报 + 最大看点
```

示例：

- `2026年6月21日 AI热点日报：Codex会录屏学习了，美团免费送GPT-5.5`
- `AI圈今天3件大事：OpenAI让AI会学你干活，美团tabbit白嫖旗舰模型`
- `AI日报0621：国产模型被Vercel CEO点名，Agent记忆层有工业级方案`

**标题原则**：

- 必须出现"AI"、"AI热点"、"AI日报"之一
- 带具体数字、大厂名、模型名
- 让读者一眼知道这是"今天 AI 圈发生了啥"
- 不超过 28 个字（含标点）

---

### 正文模板

```markdown
---
title: 2026年6月21日 AI热点日报：Codex会录屏学习，美团tabbit免费接旗舰模型
date: 2026-06-21 23:29:00
tags: ["AI热点", "AI日报", "AI资讯", "AI工具", "OpenAI", "Codex", "美团", "GLM-5.2"]
categories: ["AI资讯"]
description: "2026年6月21日 AI热点日报：OpenAI Codex Record & Replay演示一次永久复用；美团tabbit国际版免费集成GPT-5.5、Claude Opus 4.8；GLM-5.2编码能力被Vercel CEO公开称赞。"
cover: https://picsum.photos/seed/aihot-YYYYMMDD/1200/630
---

<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<!-- more -->

大家好，我是程序员晚枫。

今天 AI 圈又热闹了。我把 AIHOT 的全量数据拉了一遍，**共 N 条**，按时间顺序给你整理好了。每一条都补了我的点评和参考链接，官方精选用 ★ 标出。

---

## 今日 AI 热点速览

一句话说完今天最重要的 3 件事：

1. **OpenAI Codex 会"录屏学习"了**：你演示一次，AI 自动生成可复用 Skill。
2. **美团 tabbit 国际版上线**：GPT-5.5、Claude Opus 4.8 全免费，不用订阅。
3. **GLM-5.2 编码能力出圈**：Vercel CEO 公开称赞，国产模型被海外认可。

---

## 官方精选条目 ★

### 1. 美团 tabbit 国际版：免费接入 GPT-5.5 / Claude Opus 4.8

- **发布时间**：12:30
- **分类**：AI 产品
- **AIHOT 评分**：78
- **来源**：@AYi_AInotes
- **原文链接**：https://x.com/AYi_AInotes/status/2068637890247016607
- **AIHOT 永久页**：https://aihot.virxact.com/item/...

**核心信息**：
美团上线了 tabbit 国际版，集成 GPT-5.5、Claude Opus 4.8、Gemini 3.5 Flash、Kimi-2.6、GLM-5.1、MiniMax-M3，全免费，不用单独开订阅。国内版只有国内模型，想用海外旗舰模型得切国际版。

**晚枫点评**：
这是典型"大厂抢 AI 入口"的动作。对读者来说，最实用的信息是：能不能稳定访问？有没有使用限制？输出质量跟官方比差多少？建议实测后再写教程。

**是否值得写教程**：⭐⭐⭐⭐⭐（免费 + 旗舰模型，流量稳）

**教程方向**：
《不花钱用 GPT-5.5 和 Claude？美团 tabbit 国际版实测》

---

## 全量记录（按北京时间倒序）

### 02. 18:45 · 模型 · OpenAI Codex Record & Replay

- **AIHOT 评分**：85
- **来源**：@shao__meng
- **原文链接**：https://x.com/shao__meng/status/2068688034493878396
- **AIHOT 永久页**：https://aihot.virxact.com/item/...

**核心信息**：
用户"录制"一次操作流程，Codex 自动分析并生成 Skill（含触发时机、输入变量、执行步骤、验证规则）。下次遇到同类任务，提供新参数，Codex 自动执行。官方给出5条录制原则：短而完整、提前声明变量、真实但脱敏、补录隐性规则、及时停止。

**晚枫点评**：
这个功能把"AI 工具"从聊天窗口推进到了"工作流自动化"层面。对我这种天天用 Codex 的人来说，录制一次→永久复用，想象空间很大。尤其适合办公自动化、重复性操作、批量处理类场景。

**是否值得写教程**：⭐⭐⭐⭐⭐（亲身可用，示范性强）

**参考链接**：
- OpenAI 官方说明：...
- Skill 录制最佳实践：...

---

### 03. 14:20 · 模型 · GLM-5.2 编码能力被 Vercel CEO 称赞

- **AIHOT 评分**：72
- **来源**：@kimmonismus
- **原文链接**：https://x.com/kimmonismus/status/2068624184297562490

**核心信息**：
GLM-5.2 开源、开放权重，编码能力强到 Vercel CEO 主动发推称"印象深刻"。

**晚枫点评**：
国产模型被海外大厂 CEO 公开点名是好事，但这条信息量太少。如果要写，不能止于"被称赞"，必须拿具体代码任务实测：代码生成、Debug、解释、单元测试各跑一轮，给出可复现结论。

**是否值得写教程**：⭐⭐⭐（有话题性，但需实测补干货）

---

## 今日 AI 圈观察

1. **AI 从"对话"进入"学习你的工作流"**：Codex Record & Replay、ClickUp Brain 自主创建 Agent，都是同一个趋势——AI 不再等你下指令，而是观察你、记住你、复刻你。
2. **大厂开始抢 AI 入口**：美团 tabbit、阿里 Zvec、腾讯元宝，都在把 AI 能力塞进自己的超级 App。
3. **国产模型从"自嗨"到"被海外认可"**：GLM-5.2 被 Vercel CEO 点名是信号，但持续性的模型评测和代码实测更关键。

---

## 最值得写公众号文章/口播稿脚本的 2 条

> 每条同时给出「公众号」和「口播稿」两个方向，便于直接复用。

### 1. OpenAI Codex Record & Replay

**推荐理由**：你正在用 Codex，有真实使用场景。"演示一次，永久复用"对办公自动化读者极度友好，公众号和短视频双平台通吃。

**公众号文章方向**：
- **方向**：实操演示 + 录屏截图，文章分步骤拆解 Skill 录制流程
- **标题候选**：《你只需演示一次，Codex 帮你把操作打包成永久工具》

**口播稿脚本方向**：
- **方向**：60 秒短视频，开场用"我演示一遍，AI 帮我打包成永久工具"做 hook，正文 30 秒讲原理 + 30 秒演示
- **开场白候选**：「你以为 AI 只会聊天？OpenAI 最新功能：你演示一次，它帮你做成永久工具，全程不用写代码」

**参考资源**：
- 官方视频：...
- 录制原则原文：...
- 你上次的 Codex 使用记录：...

---

### 2. 美团 tabbit 国际版

**推荐理由**：你的读者天然关注"免费平替"，美团跨界 AI 也有新鲜感。口播稿天然适合"白嫖/省钱"话题，传播力强。

**公众号文章方向**：
- **方向**：注册流程截图 + 各模型对比表 + 实测响应速度
- **标题候选**：《美团卖外卖，顺手送了你个免费 GPT-5.5》

**口播稿脚本方向**：
- **方向**：90 秒横评脚本，用 5 个真实 prompt 对比 GPT-5.5、Claude、GLM-5.2 的输出
- **开场白候选**：「GPT-5.5、Claude、GLM-5.2 全免费？美团这个新 App 让海外旗舰模型直接白嫖」

**参考资源**：
- tabbit 下载/注册地址：...
- 各模型对比表：...

---

## 深度阅读 & 工具资源

| 资源 | 链接 | 说明 |
|------|------|------|
| 前一天日报 | https://www.python4office.cn/ai/news/20260620-ai-hotspot-daily/ | 方便对比连续趋势 |
| OpenAI 官方博客 | https://openai.com/blog | 发布 Codex 新功能时优先引用 |
| AIHOT 数据源 | https://aihot.virxact.com | 原始热点聚合站 |
| 晚枫 AI 工具评测系列 | https://www.python4office.cn/ai/ | 站内历史文章回链 |

---

## 写在最后

今天 AI 圈的热闹集中在三件事：**Agent 会学习、大厂抢入口、国产模型出海**。

建议优先写 Codex Record & Replay，因为它既是新闻，又是你现在就能上手的工具。tabbit 是流量保底，实测后再发更稳。

**科技不高冷，AI 很好用。**

我是晚枫，关注我，带你一起玩 AI！

---

## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **免费试看**：[网盘链接，免费试看前3讲](https://pan.quark.cn/s/8f7886f79569)
- 👉 **课程报名**：[点击这里报名，现在报名还送书📖](https://mp.weixin.qq.com/s/VXmJjQwsQlY-2IHjA3OAYA)
```

---

### 模板使用要点

| 模块 | 写作要求 |
|------|----------|
| 标题 | 必须包含"AI热点/AI日报/AI圈" + 时间 + 最大看点 |
| 速览 | 用 3 句话概括今天最重要的 3 条，降低阅读门槛 |
| 官方精选 | 单独展开，加评分、来源、原文链接、AIHOT 永久页 |
| 全量记录 | 每条包含：核心信息、晚枫点评、参考链接、是否值得写 |
| 今日观察 | 不是简单罗列，要给出趋势判断和因果分析 |
| 内容推荐 | 选出 2-3 条，说明理由、公众号方向 + 标题、口播稿方向 + 开场白、参考资源 |
| 深度阅读 | 用表格整理回链和外部资源，提升文章信息密度 |

---

### 干货密度 checklist

写完一篇文章后，检查是否满足：

- [ ] 至少 3 条原文链接
- [ ] 至少 2 条我的独立点评
- [ ] 至少 1 个趋势判断
- [ ] 至少 2 条公众号/口播稿脚本推荐
- [ ] 至少 1 个参考资源表格
- [ ] 标题明确出现"AI"或"AI热点"或"AI日报"
- [ ] 不出现医疗、法律、政治敏感内容
```

---

## 五、标题优化技巧

按晚枫公众号风格，优先三选一：

| 风格 | 示例 | 适用 |
|------|------|------|
| 数字型 | `今天AI圈3件大事：第2个免费替代Pinecone，第3个召回率0.89` | 多篇汇总 |
| 痛点型 | `Pinecone太贵？阿里开源向量库，一行命令搞定` | 有替代/省钱属性 |
| 反常识型 | `AI写代码还会自动测试？Salesforce CodeGen这次玩真的` | 单篇深度，制造好奇 |

**标题原则**：

- 不超过 25 个字
- 带数字、带问号、带感叹号优先
- 让读者一眼知道"他能得到什么"
- 避免术语堆叠，如"LLM + RAG + MCP 框架发布"太干

---

## 六、选题深度判断表

拿到一条热点，问自己 5 个问题：

| 问题 | 如果答案为"是" |
|------|----------------|
| 有原文链接吗？ | 可以引用，降低事实风险 |
| 能跑通代码吗？ | 可以写教程，粉丝获得感强 |
| 和 Python/办公自动化有关吗？ | 符合站点定位 |
| 读者能省钱/省时间/长见识吗？ | 有传播价值 |
| 能在 2 小时内写完吗？ | 适合自己当前节奏 |

---

## 七、常见坑和注意点

1. **脚本路径可能不存在**：`skills/ai-hotspot-tracker/scripts/fetch_aihot.py` 不一定还在，建议直接用 API 调用。
2. **API 时间要用 UTC**：`since` 参数传 UTC 时间，过滤成北京时间 CST（UTC+8）后再写文件。
3. **医疗/法律/政治不写**：这是硬约束，过滤时直接 pass。
4. **官方精选条目有限**：精选不够时，全量里按评分从高到低补。
5. **相关阅读要回链**：尽量链回站内已有同类文章，增加停留和转化。
6. **封面图用 `picsum.photos/seed/aihot-YYYYMMDD`**：固定 seed 保证同天封面一致，方便复用。

---

## 八、速查表

| 操作 | 命令/路径 |
|------|-----------|
| 看当前目录现有文章 | `ls hexo/hexo/source/_posts/ai/news/` |
| 新建当天文章 | `hexo/hexo/source/_posts/ai/news/YYYYMMDD-ai-hotspot-daily.md` |
| 调用日报 API | `https://aihot.virxact.com/api/public/daily` |
| 调用全量 API | `https://aihot.virxact.com/api/public/items?mode=all&since=...` |
| 调用精选 API | `https://aihot.virxact.com/api/public/items?mode=selected&since=...` |
| 记录每日工作 | `hexo/hexo/../../.workbuddy/memory/YYYY-MM-DD.md` |

---

## 九、实战示例

### 示例：2026-06-21 的选题决策

- **OpenAI Codex Record & Replay** → 强推，可写教程，演示一次永久复用
- **美团 tabbit 国际版免费旗舰模型** → 强推，省钱平替，有流量
- **GLM-5.2 被 Vercel CEO 称赞** → 可写，但信息量薄，需实测
- **刘强东"将来不需要快递员"** → 不写，纯观点
- **京东 AI 培训 70 万蓝领** → 不写，社会话题非技术
- **华为鸿蒙 HarmonyOS 7** → 不写，与 Python 办公无关

---

## 十、总结

每天 5 步：

1. 拉 AIHOT 全量数据
2. 过滤出北京时间"今天"
3. 按选题表筛选
4. 套用模板写 Hexo 文章
5. 记工作日志，优化标题

核心原则：**只写有代码、有链接、有教程角度的东西**。不追八卦，不碰医疗法律，只给读者能落地的东西。

---

**版本**：v1.1  
**更新日期**：2026-06-22  
**更新说明**：强化标题 AI 新闻属性，增加每条热点的核心信息、参考链接、晚枫点评、教程推荐度评估。
**作者**：程序员晚枫 & 枫灵
