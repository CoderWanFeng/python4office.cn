---
title: 手把手教程：用AI编程30分钟做出MBTI测试网站，完整代码可复制
keywords: 程序员晚枫, MBTI测试网站, AI编程教程, 30分钟做网站, AI代码生成, 编程入门, 项目源码
description: 程序员晚枫手把手教你用AI编程30分钟做出MBTI性格测试网站。提供完整Prompt和代码，零基础也能跟着做出来，快速上手AI编程开发。
date: 2026-04-11 13:00:00
tags: 
  - 程序员晚枫
  - MBTI测试
  - AI编程教程
  - 手把手教学
  - 源码分享
categories: 
  - AI编程教程
  - 实战案例
author: 程序员晚枫
---

<!-- more -->
> **本文作者：程序员晚枫 | AI编程布道者 | 专注AI工具测评与教学**
> 全网50万+粉丝，6年Python开发经验，开源项目python-office作者

---

## 前言

上一篇文章我分享了用AI编程做MBTI测试网站的想法，很多朋友私信问我具体怎么做。

今天直接上干货：**完整的Prompt + 实现步骤 + 核心代码**，你跟着做，30分钟就能做出自己的MBTI测试网站。

---

## 准备工作

### 需要的工具

1. **AI编程工具**：Cursor、Trae、Windsurf 或 GitHub Copilot（任选其一）
2. **代码编辑器**：VS Code（推荐）
3. **Node.js环境**：用于运行项目

### 安装AI编程工具

以Cursor为例：
1. 访问 https://cursor.sh 下载安装
2. 用GitHub账号登录
3. 选择"Continue with Free Plan"

---

## 第一步：创建项目

打开Cursor，按 `Ctrl+L` 打开AI对话框，输入：

```
帮我创建一个MBTI性格测试网站，要求：
1. 使用Vue 3 + Vite技术栈
2. 包含40道测试题目，每道题2个选项
3. 题目分为4个维度：E/I、S/N、T/F、J/P
4. 答题完成后显示16种人格类型之一
5. 结果页面包含人格解析、适合职业、人际关系建议
6. 界面美观，支持响应式布局
7. 使用中文

请生成完整的项目结构和代码。
```

AI会自动生成：
- 项目目录结构
- package.json配置文件
- Vue组件代码
- 样式文件
- MBTI题库数据

---

## 第二步：核心代码解析

### 1. 题库数据（mbti-questions.js）

```javascript
export const mbtiQuestions = [
  {
    id: 1,
    dimension: 'EI', // E/I维度
    question: '在社交场合中，你通常：',
    options: [
      { text: '主动与人交流，享受社交', value: 'E' },
      { text: '更喜欢和熟悉的人待在一起', value: 'I' }
    ]
  },
  {
    id: 2,
    dimension: 'SN', // S/N维度
    question: '你更关注：',
    options: [
      { text: '具体的事实和细节', value: 'S' },
      { text: '整体的概念和可能性', value: 'N' }
    ]
  },
  // ... 共40道题
]

export const mbtiTypes = {
  'INTJ': {
    name: '建筑师',
    description: '富有想象力和战略性的思想家...',
    careers: ['科学家', '工程师', '战略规划师'],
    relationships: '重视深度交流，追求精神层面的连接...'
  },
  // ... 其他15种类型
}
```

### 2. 计分逻辑（mbti-calculator.js）

```javascript
export function calculateMBTI(answers) {
  const scores = { E: 0, I: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0 }
  
  answers.forEach(answer => {
    scores[answer.value]++
  })
  
  const type = [
    scores.E > scores.I ? 'E' : 'I',
    scores.S > scores.N ? 'S' : 'N',
    scores.T > scores.F ? 'T' : 'F',
    scores.J > scores.P ? 'J' : 'P'
  ].join('')
  
  return type
}
```

### 3. 主页面组件（App.vue）

```vue
<template>
  <div class="min-h-screen bg-gradient-to-br from-purple-50 to-blue-50">
    <!-- 首页 -->
    <div v-if="currentStep === 'home'" class="container mx-auto px-4 py-16">
      <h1 class="text-4xl font-bold text-center mb-4">MBTI性格测试</h1>
      <p class="text-gray-600 text-center mb-8">40道题，发现真实的自己</p>
      <button 
        @click="startTest"
        class="bg-purple-600 text-white px-8 py-3 rounded-full mx-auto block hover:bg-purple-700"
      >
        开始测试
      </button>
    </div>
    
    <!-- 答题页 -->
    <div v-else-if="currentStep === 'quiz'" class="container mx-auto px-4 py-8 max-w-2xl">
      <div class="mb-4 text-center">
        <span class="text-purple-600 font-semibold">{{ currentIndex + 1 }} / {{ questions.length }}</span>
      </div>
      <div class="bg-white rounded-2xl shadow-lg p-8">
        <h2 class="text-xl font-semibold mb-6">{{ currentQuestion.question }}</h2>
        <div class="space-y-4">
          <button
            v-for="option in currentQuestion.options"
            :key="option.value"
            @click="selectAnswer(option.value)"
            class="w-full p-4 text-left border-2 border-gray-200 rounded-xl hover:border-purple-500 hover:bg-purple-50 transition"
          >
            {{ option.text }}
          </button>
        </div>
      </div>
    </div>
    
    <!-- 结果页 -->
    <div v-else-if="currentStep === 'result'" class="container mx-auto px-4 py-8 max-w-2xl">
      <div class="bg-white rounded-2xl shadow-lg p-8 text-center">
        <h2 class="text-3xl font-bold text-purple-600 mb-2">{{ resultType }}</h2>
        <h3 class="text-xl text-gray-700 mb-6">{{ resultData.name }}</h3>
        <p class="text-gray-600 mb-6">{{ resultData.description }}</p>
        
        <div class="text-left mb-6">
          <h4 class="font-semibold mb-2">适合职业：</h4>
          <div class="flex flex-wrap gap-2">
            <span v-for="career in resultData.careers" :key="career" class="bg-purple-100 text-purple-700 px-3 py-1 rounded-full text-sm">
              {{ career }}
            </span>
          </div>
        </div>
        
        <button @click="restart" class="bg-purple-600 text-white px-6 py-2 rounded-full hover:bg-purple-700">
          重新测试
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { mbtiQuestions, mbtiTypes } from './data/mbti-data'
import { calculateMBTI } from './utils/mbti-calculator'

const currentStep = ref('home')
const currentIndex = ref(0)
const answers = ref([])

const questions = mbtiQuestions
const currentQuestion = computed(() => questions[currentIndex.value])

const startTest = () => {
  currentStep.value = 'quiz'
  currentIndex.value = 0
  answers.value = []
}

const selectAnswer = (value) => {
  answers.value.push({
    questionId: currentQuestion.value.id,
    dimension: currentQuestion.value.dimension,
    value
  })
  
  if (currentIndex.value < questions.length - 1) {
    currentIndex.value++
  } else {
    showResult()
  }
}

const resultType = ref('')
const resultData = ref({})

const showResult = () => {
  resultType.value = calculateMBTI(answers.value)
  resultData.value = mbtiTypes[resultType.value]
  currentStep.value = 'result'
}

const restart = () => {
  currentStep.value = 'home'
}
</script>
```

---

## 第三步：运行项目

在终端中执行：

```bash
# 进入项目目录
cd mbti-test

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

打开浏览器访问 `http://localhost:5173`，就能看到你的MBTI测试网站了！

---

## 第四步：部署上线

### 方案1：Vercel（推荐）

```bash
# 安装Vercel CLI
npm i -g vercel

# 部署
vercel
```

### 方案2：腾讯云COS

1. 执行 `npm run build` 生成dist文件夹
2. 上传到腾讯云COS静态网站托管
3. 绑定自己的域名

---

## 你可能会遇到的问题

### Q1：AI生成的代码有bug怎么办？

把错误信息复制给AI，说："运行时报错：[粘贴错误信息]，请修复"。

### Q2：想修改样式但不知道怎么描述？

直接说："把按钮改成圆角"、"背景换成渐变色"、"字体调大一点"，AI会帮你改。

### Q3：题目数量能增减吗？

可以！告诉AI："把题目增加到60道"或"减少到20道"，它会自动调整。

---

## 学会更多AI编程技能

这个MBTI测试网站只是开始。

如果你想系统学习AI编程，掌握更多实战项目的开发方法，欢迎加入我的**《AI编程实战课》**。

课程包含：
- ✅ 10+完整项目实战（从需求到上线）
- ✅ AI编程工具深度使用技巧
- ✅ 前端/后端/小程序全栈开发
- ✅ 项目部署和运维知识
- ✅ 专属答疑社群

🎬 **课程试听**：https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA

📚 **系统学习**：``https://r7up9.xetslk.com/s/1uP5YW``

---

> 💬 **互动话题**：你跟着教程做出来了吗？遇到了什么问题？欢迎在评论区交流！
> 
> 📌 **关注程序员晚枫**，获取更多AI编程教程和源码分享！

---

*本文首发于程序员晚枫技术博客，转载请注明出处。*
