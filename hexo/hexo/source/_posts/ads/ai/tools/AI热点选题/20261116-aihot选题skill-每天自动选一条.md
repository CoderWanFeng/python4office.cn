---
title: 我做了个「AI 热点选题」Skill：每天自动筛出 1 条值得写的
date: 2026-11-16 21:00:00
tags:
  - Skill
  - 自媒体
  - 选题
  - AI热点
  - 效率工具
categories: AI工具评测
cover: https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop
---

> **一句话总结**：AI 圈一天几十条热点，大部分跟你没关系。这个 Skill 每天替你筛出**唯一一条**值得写的，并告诉你为什么是它。

大家好，我是程序员晚枫。

上一篇我写了「选题雷达」，管的是**全网**——跨 7 个平台，什么火都看。

但对我这种只写 AI 的号来说，全网热搜有个致命问题：**AI 只占很小一块，剩下九成是娱乐八卦和明星塌房。** 你得从一堆不相干的东西里，把 AI 的那几条捞出来。

捞出来还不算完。AI 圈一天几十条热点摆在面前，**写哪一条？**

我给自己定的规矩是：**一天只写一条。** 写两条就是都没写好，写三条就是三篇都没写好。

但「只写一条」意味着必须敢取舍。于是我把取舍这件事，也交给了一个 Skill：**AI 热点选题（aihot-topic-selector）**。

**SkillHub 发布页**：[AI 热点选题：https://skillhub.cn/skills/user_bf8c5b73/wanfeng-aihot-topic-selector](https://skillhub.cn/skills/user_bf8c5b73/wanfeng-aihot-topic-selector)

<!-- more -->

## 一、它只做一件事：从一堆热点里挑 1 条

流程很短，五步：

```
① 拉 AIHOT 数据
② 立刻写当天的「每日热点汇总」文件（这一步不能省）
③ 过滤：只看今天的 + 评分 ≥ 50 的
④ 过「核心 2 问」，人工选 1 条
⑤ 建 task 目录，把选题依据写清楚
   → 到此结束
```

跑完你得到两样东西：

1. `每日热点/YYYYMMDD.md` —— 当天 AI 圈所有热点的快照，带评分、时间、来源、链接、简介
2. `task/20261116-<slug>/` —— 一个装好选题依据的文件夹，等着你去写

**它不写稿，不写标题，不写口播。** 选题完了就收工。

## 二、核心是「核心 2 问」

这是我给 AI 选题定的两条硬标准，**必须同时满足**：

| 问题 | 什么意思 | 例子 |
|---|---|---|
| **大众能听懂吗？** | 不需要专业背景，新闻本身就有传播性 | 「Netflix 省了 95% 的 AI 字费」✅ /「transformer 注意力机制的数学推导」❌ |
| **能借它讲清一个热门 AI 原理吗？** | 借新闻这个壳，讲 Token / 上下文窗口 / RAG / Agent / 思维链 | 「某个工具讲清了 Token 压缩原理」✅ /「某公司又融资了」❌ |

**两个都答「是」才继续，否则换题。**

为什么第二问这么重要？因为它是**一篇 AI 文章能不能活过三个月**的分水岭。

「某公司融资 3 亿美元」——写完当天就没人看了。但如果你写的是「顺便讲清楚这背后 Token 是怎么计费的」，那你顺手把一个热门概念讲透了，**半年后有人搜这个词还会找到你**。

**热点是流量入口，原理才是留下来的东西。**

## 三、4 个优先方向，我只从这四个里选

定了「能听懂」之后，还得定「写了对读者有用」。我的排序是固定的：

### 🥇 方向 1：AI 工具免费薅羊毛（最高优先级）

免费资格、注册步骤、访问要求、使用限制、避坑提示——**读者能立刻拿到好处**。

这类内容传播力最强，因为它有天然的转发理由：「我发现个白嫖的」，比「我来讲个原理」更容易被转发。

### 🥈 方向 2：AI 产品限时优惠 / 试用

优惠力度、时间限制、参与条件、使用步骤、风险提示。

关键词是**「限时」**。过了期限就是过期信息，转发出去反而招骂。

### 🥉 方向 3：AI 公司招聘机会

岗位信息、任职要求、申请流程、截止时间、公司福利。

大厂 AI Lab、AI 独角兽、海外大厂中国团队、校招实习、内推码——**这是读者的饭碗，比什么都实在**。

### 🏅 方向 4：AI 学习资源 / 课程免费学

大厂免费课、顶尖教授的课、认证折扣、训练营、开源教材。

资源类型、价格说明、学习路径、时长难度、证书值不值。

## 四、这 8 类我明确不写

排除清单和优先清单一样重要。因为**大部分热点是不该写的**，你不写它，它就自动出局了：

| 不写 | 为什么 |
|---|---|
| 纯人事变动 | 没有知识角度，读者也没有利益 |
| 医疗 / 健康问答 | 合规红线 |
| 纯政策 / 法案 | 没有技术切入点 |
| 硬件发布（芯片、显卡） | 读者没法参与，转发无意义 |
| 太底层的技术细节 | 大众听不懂 |
| 纯观点 / 纯评论 | 没有事实锚点 |
| AI 公司融资 | 除非附带招聘或产品免费信息 |
| AI 产品发布但无免费 / 优惠 | 读者无法立即参与 |

### 有三条特别容易搞混，我拆开说

**「人事变动」vs「AI 招聘机会」**
前者是任免、离职、跳槽这类组织行为；后者是**岗位开放、任职要求、申请流程、截止时间**——后者对读者是「工作机会」，可以写。

**「硬件发布」vs「免费薅羊毛」**
单纯的规格、价格新闻不写；但**硬件免费送、抽奖、试用**仍然算方向 1。

**「AI 公司融资」vs「AI 公司招聘」**
单纯融资不写；但融资新闻**附带招聘专场或内推码**时，按方向 3 写。

这三条其实都是同一个判断标准：**读者看完能做什么？** 能参与（报名、领取、申请）就写，围观式的信息不写。

## 五、没有合格选题怎么办

这是我觉得最实用的一个设计。

如果今天筛完之后，一条都不合格——**它不会硬选**。

它会先做一件事：**把时间窗从 30 小时拉到 168 小时（7 天），重试一次。** 今天的热点池太窄，就看这一周的。

还不行呢？在当天的汇总文件末尾追加一段：

```markdown
## 今日无合适选题
> 原因：2026-11-16 当日 N 条热点全部不符合核心 2 问
> 操作：跳过今日选题，下一个工作日继续
```

**然后真的跳过。**

> **宁可跳过，也不要把不达标的条目塞进选题。**

硬凑一篇的结果是：写得累、读者不买账、账号调性被拉低。**一天不发，比发一篇烂的强。**

## 六、每天还会留一份「热点档案」

选完题就完了，但我还让它多做一件事——**每次拉完数据，先把当天所有热点写一份汇总文件**，再去筛。

```markdown
# 每日AI热点汇总 · 2026-11-16

> 自动收集于 2026-11-16 08:30
> 文件用途：每日选题参考，可直接用作内部追溯

## 更新于 08:30:12

### 1. 某个热点标题
- **AIHOT 评分**：78
- **发布时间**：07:12
- **来源**：xxx
- **链接**：xxx
- **简介**：xxx

> 本次新增 23 条，跳过重复 4 条
```

文件按 `YYYYMMDD.md` 命名，一天一个。**一天跑多次就往同一个文件里追加区块**，不会覆盖。

为什么坚持留这个档案？因为**热点是有账本的**。你三个月后想「上个月那个 OpenAI 的事我写过吗」，翻一下就有；更常见的是——某条热点你今天没选，三天后它还在，因为它一直在被人讨论。**汇总文件就是那个池子。**

去重也做了：标题先做正则清洗（去掉 `【】`、`()`、`[]`、公众号名后缀、`- IT之家` 之类），再用模糊匹配（相似度 ≥ 90）判重。**重复的跳过，不更新评分。**

## 七、怎么用

**第一步：改配置**（`topic-config.yaml`）：

```yaml
daily_dir: workflow/每日热点/        # 每日热点汇总放哪
min_score: 50                       # 选题阶段的最低 AIHOT 评分
lookback_hours: 30                  # 拉数据的时间窗
fuzzy_match_threshold: 90           # 标题去重阈值
timezone: Asia/Shanghai
```

**第二步：跑。**

```bash
# 跑今天的
python scripts/fetch_aihot.py

# 只打印不写文件
python scripts/fetch_aihot.py --dry-run

# 指定日期
python scripts/fetch_aihot.py --date 20260701
```

**第三步：选一条，建目录。** 目录名是 `YYYYMMDD-<slug>`，里面的 `00-选题依据.md` 长这样：

```markdown
# 选题依据 · 2026-11-16 netflix-headroom-save-token

## 主题
一句话说清这条热点是什么

## 核心 2 问
- 大众能听懂吗？ ✅ <理由>
- 能解释一个热门 AI 知识/原理吗？ ✅ <理由>

## 对应 AI 知识
Token / 上下文窗口 / RAG / Agent / ...

## AIHOT 评分
78

## 资料
- 原文链接：<url>
- 截图：<imgs/ 下文件列表>
```

**为什么必须写这份文件？** 因为一周后你回头看，会问「我当时为什么选这条」。**把判断写下来，下次就不用重新想一遍。**

## 八、它和「选题雷达」怎么配合

上一篇写的那个是**跨平台全网**的，这个是**只盯 AI 圈**的。两者不冲突，并行跑：

- **选题雷达**：给你广度——今天全网什么火，哪些跟你有关
- **AI 热点选题**：给你准度——AI 圈里，今天唯一值得写的那条

**我的实际用法是：早上先跑雷达，看一眼全网有没有被我漏掉的 AI 大事；再跑 AI 热点选题，选出今天要写的那一条。**

## 九、怎么装

**方式一：从 GitHub 拉源码（本地用）**

```bash
git clone https://github.com/CoderWanFeng/wanfeng-skills.git
cd wanfeng-skills/skills/aihot-topic-selector
```

**方式二：从 SkillHub 一键安装（其他支持 Skill 的 AI 工具）**

打开发布页：

> [AI 热点选题：https://skillhub.cn/skills/user_bf8c5b73/wanfeng-aihot-topic-selector](https://skillhub.cn/skills/user_bf8c5b73/wanfeng-aihot-topic-selector)

在支持 Skill 安装的 AI 工具里，可以直接发送下面这句话：

```text
请根据 https://skillhub.cn/install/skillhub.md，安装 @user_bf8c5b73/aihot-topic-selector。
```

也可以在发布页下载 Zip 包手动安装。

**源码在这**：

> **GitHub**：[aihot-topic-selector：https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/aihot-topic-selector](https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/aihot-topic-selector)

> **整个仓库**：[wanfeng-skills 仓库首页：https://github.com/CoderWanFeng/wanfeng-skills](https://github.com/CoderWanFeng/wanfeng-skills)

**如果你每天也在「今天写什么」上纠结**，可以试试这个思路：**把选题单独拆成一个任务，每天只做一次，做完就扔。** 别让选题绑架你的写作节奏。

用的时候有问题，欢迎到 GitHub 提 Issue，也可以在文章下面留言。

科技不高冷，AI 很好用。我是晚枫，关注我，一起把 AI 真正用起来。

---

### 参考链接

- [aihot-topic-selector Skill 源码：https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/aihot-topic-selector](https://github.com/CoderWanFeng/wanfeng-skills/tree/main/skills/aihot-topic-selector)
- [AI 热点选题 SkillHub 发布页：https://skillhub.cn/skills/user_bf8c5b73/wanfeng-aihot-topic-selector](https://skillhub.cn/skills/user_bf8c5b73/wanfeng-aihot-topic-selector)
- [SkillHub 安装说明：https://skillhub.cn/install/skillhub.md](https://skillhub.cn/install/skillhub.md)
- [wanfeng-skills 仓库首页：https://github.com/CoderWanFeng/wanfeng-skills](https://github.com/CoderWanFeng/wanfeng-skills)
- [AIHOT 热点站：https://aihot.virxact.com](https://aihot.virxact.com)
- [rapidfuzz 官方文档：https://rapidfuzz.github.io/RapidFuzz/](https://rapidfuzz.github.io/RapidFuzz/)

## 相关阅读

- [OpenAI正在疯狂招人！721个岗位在招，非技术也能加入（附中文报名攻略）](https://mp.weixin.qq.com/s/oNpRBeNo-OAFXLMb_xf5Hw)
- [GitHub 2万星的开源神器：一个接口薅26家免费AI额度，但其中88个模型来路不明](https://mp.weixin.qq.com/s/SAzlEdE6_E83K0fkWjk88g)
- [别花钱买大模型了！OpenAI 开源了 gpt-oss，16G 内存就能跑](https://mp.weixin.qq.com/s/H_l-BJkzyLvw39KOYHMxcw)