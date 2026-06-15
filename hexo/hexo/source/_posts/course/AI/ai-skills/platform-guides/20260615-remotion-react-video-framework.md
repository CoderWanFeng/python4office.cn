---
title: Remotion 入门指南：用 React 代码写视频，AI 一键生成 MP4
date: 2026-06-15 22:45:00
tags: [Remotion, React, AI视频, AI Skills, 视频生成, 程序员晚枫]
categories: [AI Skills, 平台攻略]
cover: https://images.unsplash.com/photo-1633356122544-f134324a6cee?q=80&w=1200&auto=format&fit=crop
---


大家好，我是程序员晚枫。

今天给大家介绍一个**让 React 工程师兴奋**的工具——**Remotion**。

它做的事情很颠覆：

> **写 React 组件，渲染出 MP4 视频。**

而且最近还加了 **Agent Skills**，AI 代理（Claude Code / Cursor）能直接帮你写 Remotion 代码，**不用写一行代码也能出视频**。

---

## 一、Remotion 是什么？

**一句话**：用 React 写视频的框架。

跟传统视频工具完全不同：

| 你熟悉的 | Remotion |
|---|---|
| 剪映/PR 时间线 | 写 React 组件 |
| Keyframe 调动画 | 写 `interpolate()` 插值函数 |
| 改文案重导出 | 改 React props，浏览器实时刷新 |
| 1 个视频 1 个文件 | 1 个模板 → 100 个参数化视频 |

**本质上：视频 = 帧函数的序列执行**。给定任意帧数，组件返回该帧的画面。

---

## 二、为什么值得用？

### 1. 批量生成（杀手锏）

写一个"GitHub 贡献墙"模板 → 传 100 个用户名 → 一键出 100 个个性化视频。

**传统方式**：100 个视频做 100 次。
**Remotion**：1 个模板 + 100 次 API 调用 = 100 个视频。

### 2. 数据驱动

接 API，实时更新视频内容：

```tsx
<MyComp
  userName="晚枫"
  favoriteColor="#FF6B35"
  score={9527}
/>
```

颜色、名字、分数全在 props 里。**改一个 prop，视频就更新**。

### 3. 精确控制

不像剪映靠手动对齐——**代码定义动画，毫秒级精确**：

```tsx
const frame = useCurrentFrame();
const opacity = interpolate(frame, [0, 30], [0, 1]);
const scale = spring({ frame, config: { damping: 10 } });
```

### 4. Git 友好

视频是 React 项目 → **天然版本控制** → 团队协作无障碍。

---

## 三、Remotion 三件套

| 产品 | 干什么 | 谁用 |
|---|---|---|
| **Remotion** | 框架本体，写代码做视频 | 开发者 |
| **Remotion Player** | 在 React App 里嵌入可交互视频预览 | 给最终用户 |
| **Remotion Lambda** | 云端渲染（AWS Lambda），并行出 MP4 | 批量生产 |

---

## 四、上手：3 步出第一个视频

### 第 1 步：脚手架

```bash
npx create-video@latest --blank
```

生成结构：
```
my-video/
├── src/
│   ├── index.ts          # 入口（注册根组件）
│   ├── Root.tsx           # 根（声明视频规格）
│   └── MyComp.tsx         # 视频组件
├── package.json
└── remotion.config.ts
```

### 第 2 步：写一个组件

**src/Root.tsx**（视频规格）：
```tsx
import {Composition} from 'remotion';
import {MyComp} from './MyComp';

export const Root: React.FC = () => (
  <Composition
    id="MyComp"
    component={MyComp}
    durationInFrames={120}   // 4 秒 @ 30fps
    width={1920}
    height={1080}
    fps={30}
    defaultProps={{}}
  />
);
```

**src/MyComp.tsx**（视频内容）：
```tsx
import {AbsoluteFill, useCurrentFrame, interpolate, spring} from 'remotion';

export const MyComp: React.FC = () => {
  const frame = useCurrentFrame();

  // 0-30 帧淡入，0-1 透明度
  const opacity = interpolate(frame, [0, 30], [0, 1]);

  // 弹性缩放
  const scale = spring({frame, config: {damping: 10}});

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#1a1a1a',
        justifyContent: 'center',
        alignItems: 'center',
      }}
    >
      <h1
        style={{
          fontSize: 120,
          color: 'white',
          opacity,
          transform: `scale(${scale})`,
        }}
      >
        Hello, Remotion!
      </h1>
    </AbsoluteFill>
  );
};
```

### 第 3 步：浏览器预览 + 渲染

```bash
# 启动开发服务器（实时预览）
npm start
# → 浏览器打开 http://localhost:3000

# 渲染成 MP4
npx remotion render MyComp out.mp4
# → 输出 out.mp4 (1920x1080, 4s, 30fps)
```

**恭喜，你的第一个 Remotion 视频出来了！**

---

## 五、核心 API 速查

| API | 干什么 |
|---|---|
| `useCurrentFrame()` | 拿当前帧数（从 0 开始）|
| `interpolate(frame, [0, 30], [0, 1])` | 帧数 → 任意值的线性映射 |
| `spring({frame, config})` | 弹性动画（自动算 velocity）|
| `measureSpring({...})` | 算出 spring 总时长（提前布局）|
| `<Composition>` | 声明一个视频（id、时长、尺寸、fps）|
| `<Sequence from={10} durationInFrames={20}>` | 元素延后出现 |
| `<AbsoluteFill>` | 全屏容器（视频的"画布"）|
| `<Video>` / `<Audio>` / `<Img>` / `<Gif>` | 媒体元素 |

---

## 六、Agent Skills：让 AI 帮你写

**这是 Remotion 2026 年 1 月的新功能**。

### 装 skills

```bash
npx skills add remotion-dev/skills
```

装好后，**Claude Code / Cursor / Codex / Gemini CLI** 都会自动知道怎么写 Remotion。

### 用自然语言出视频

直接跟 AI 说：

```
用 Remotion 给我做一个 10 秒的产品介绍：
深色背景，白色标题淡入，淡出时加个粒子效果。

做一个 30 秒的柱状图动画，
数据是过去 5 年的销售额，每年柱子从下往上长出来。

把这段 React 代码改成 Remotion 视频：https://...
```

AI 会自动：
- 创建项目结构
- 写 Composition 和组件
- 处理时间轴和动画
- 渲染出 MP4

### Skills 编码了什么

**Remotion 的"内部约定"**——AI 不会忘的：

- `<Composition>` 必备字段
- `useCurrentFrame` 的正确用法
- `interpolate` / `spring` 选择
- `<Video>`、`<Audio>`、`<Img>` 的差别
- `staticFile` 引用 `public/` 资源
- `AbsoluteFill` 层级关系

**没有 skills**：AI 写出来大概率跑不起来。
**有 skills**：AI 一次就写对。

---

## 七、实战场景

| 场景 | 怎么做 |
|---|---|
| 📊 **数据可视化动画** | 传 JSON → 渲染柱状图/折线图动画 |
| 📱 **个性化营销视频** | 1 模板 + 用户名/头像 → 批量生成 |
| 📈 **股票/财经播报** | 抓 API → 自动生成每日复盘视频 |
| 🎓 **教育内容** | 公式/图表自动动画化 |
| 🎂 **节日贺卡** | 1 模板 → 几千人定制 |
| 📺 **短视频矩阵** | 1 模板 + 100 主题 = 100 视频 |

---

## 八、Remotion vs 视频生成 AI

| 维度 | Remotion | 视频生成 AI（Sora、可灵）|
|---|---|---|
| **输入** | 代码 + props | 文本/图片 prompt |
| **输出** | 精确可控的 MP4 | 视觉惊艳但不可控 |
| **批量** | 100 视频 = 1 模板 | 100 视频 = 100 次生成 |
| **可重复** | 100% 一致 | 有随机性 |
| **适合** | 营销/数据/教育 | 创意/特效/演示 |

**两者是互补**，不是替代。

---

## 九、定价（重要）

Remotion 4 层许可：

| 许可 | 价格 | 限制 |
|---|---|---|
| **Free** | $0 | 个人、员工 < 4 人的小公司 |
| **Company** | $15/月/人 | 公司使用，无限制 |
| **Enterprise** | 定制 | 大企业 |
| **试用** | 4 周免费 | 完整功能 |

**重点**：Free 许可**个人和小公司可以商用**！对独立开发者友好。

---

## 十、常见问题

### Q: 必须会 React 吗？

**是的**。Remotion 是 React 框架，零 React 基础写不了。但 React 学起来不难，几天入门。

### Q: 不会写代码能用 Remotion 吗？

**装 skills 后可以**。AI 代理能根据你的描述自动写代码并渲染。

### Q: 渲染很慢吗？

- **预览**：浏览器实时（30 fps）
- **小视频**：本地几秒到几十秒
- **大批量**：用 **Remotion Lambda**（AWS Lambda 并行，云端渲染）

### Q: 移动端能看吗？

**输出就是标准 MP4**，所有平台都能播。

---

## 总结

Remotion = **用代码做视频**。

- 想精确可控？**写 React 组件**
- 想批量生产？**1 模板 + 数据 API**
- 想偷懒？**装 skills，AI 帮你写**
- 想白嫖？**Free 许可个人可商用**

不是"剪映杀手"，是"**视频创作的新姿势**"。

**科技不高冷，AI 很好用。**
我是晚枫，关注我，带你一起玩 AI！

💬 **来评论区聊聊**

你做过哪些"参数化批量"的视频？
Remotion + AI Skills 哪个组合你最想试？

---

## 🔗 快速链接

- 📖 官方文档：https://www.remotion.dev/
- 💻 GitHub：https://github.com/remotion-dev/skills
- ⚡ Skills 安装：`npx skills add remotion-dev/skills`
- 🎬 Examples：https://www.remotion.dev/docs/templates
- 📚 System Prompt（给 LLM 用的提示词）：https://www.remotion.dev/docs/ai/system-prompt

---

*本文基于 Remotion 官方文档（2026-06）整理。*
