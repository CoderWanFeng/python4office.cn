---
title: "我用RAG做了一个企业知识库问答系统：从0到1完整实战记录"
date: "2025-04-05T20:00:00+08:00"
tags:
---


<!-- more -->
<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

最近帮一个客户做了企业知识库问答系统，用的是RAG（检索增强生成）技术。

作为一个写了6年代码、做了5年自媒体的程序员，从需求分析到上线，我花了2周时间。

**我的看法是：RAG是目前最实用的企业AI应用方案，值得每个程序员掌握。**

说到这儿，想起我在python-office项目中也用过类似的技术。

python-office有大量的文档和教程，用户经常问重复的问题。为了提高效率，我搭建了一个文档问答系统：
- 用户提问
- 系统从文档中检索相关内容
- 基于检索结果生成答案

**这个系统和RAG的原理是一样的。**

不过企业级的RAG项目要复杂得多。这次帮客户做的项目，让我学到了很多实战经验。下面完整分享给你。

---

## 一、什么是RAG？

RAG = Retrieval Augmented Generation（检索增强生成）

**简单说：** 让大模型在回答问题之前，先从知识库里检索相关信息，然后再生成答案。

### 为什么需要RAG？

**大模型的问题：**
- ❌ 不知道企业私有知识
- ❌ 容易产生"幻觉"（胡说八道）
- ❌ 无法追溯答案来源

**RAG的解决方案：**
- ✅ 先检索企业文档
- ✅ 基于检索结果生成答案
- ✅ 可溯源、可验证

---

## 二、项目需求分析

### 客户背景
- 中型互联网公司，500+员工
- 内部文档分散在Confluence、钉钉、邮件里
- 新员工培训成本高，老员工查资料效率低

### 核心需求
1. **知识问答**：员工可以用自然语言提问，快速找到答案
2. **多源整合**：整合Confluence、钉钉文档、PDF等多种来源
3. **权限控制**：不同部门只能看到自己有权限的文档
4. **可追溯**：每个答案都要标注来源文档

---

## 三、技术架构设计

### 整体架构

```
用户提问
    ↓
[查询理解] → 意图识别、关键词提取
    ↓
[向量检索] → 从向量数据库检索相关文档
    ↓
[重排序] → 对检索结果排序，选出最相关的
    ↓
[上下文构建] → 构建Prompt，包含检索到的内容
    ↓
[大模型生成] → GPT-4/Claude生成答案
    ↓
[答案后处理] → 格式化、标注来源
    ↓
返回答案
```

### 技术选型

| 组件 | 选型 | 理由 |
|------|------|------|
| 向量数据库 | Chroma | 轻量、易部署、Python生态好 |
| Embedding模型 | text-embedding-3-small | 性价比高、支持中文 |
| 大模型 | GPT-4 | 生成质量高、支持长上下文 |
| 框架 | LangChain | 生态完善、文档齐全 |
| 前端 | Streamlit | 快速搭建Demo、适合MVP |

---

## 四、核心代码实现

### 1. 文档加载和切分

```python
from langchain.document_loaders import (
    ConfluenceLoader,
    PyPDFLoader,
    TextLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 加载不同来源的文档
def load_documents():
    documents = []
    
    # 加载Confluence文档
    confluence_loader = ConfluenceLoader(
        url="https://your-domain.atlassian.net",
        username="your-email",
        api_key="your-api-key"
    )
    documents.extend(confluence_loader.load())
    
    # 加载PDF文档
    pdf_loader = PyPDFLoader("path/to/document.pdf")
    documents.extend(pdf_loader.load())
    
    return documents

# 文档切分
def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,      # 每个块1000字符
        chunk_overlap=200,    # 重叠200字符，保证上下文连贯
        separators=["\n\n", "\n", "。", "！", "？"]
    )
    
    chunks = text_splitter.split_documents(documents)
    return chunks
```

**踩坑记录：**
- 一开始chunk_size设得太小（500），导致上下文丢失
- 后来调到1000，效果明显改善
- 中文文档要用中文标点做分隔符

说到文档切分，这和我处理python-office文档的经历很像。

python-office的文档有几百页，如果整篇加载，会超出模型的上下文限制。如果切得太碎，又会丢失上下文。

我的解决方案是：
1. **按功能模块切分**：每个功能一篇文档
2. **保留上下文信息**：在metadata中记录前后文
3. **重要内容重复**：关键信息在多个chunk中都出现

比如python-office的Excel模块，我会这样组织：
```
excel/
  ├── 入门指南.md（概述+安装）
  ├── 读取Excel.md（详细用法）
  ├── 写入Excel.md（详细用法）
  ├── 数据处理.md（高级功能）
  └── 常见问题.md（FAQ）
```

每个文件独立成篇，既方便检索，又保证上下文完整。

### 2. 向量存储和检索

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# 创建向量数据库
def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )
    
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    
    return vectorstore

# 检索相关文档
def retrieve_documents(query, vectorstore, k=5):
    results = vectorstore.similarity_search(query, k=k)
    return results
```

**踩坑记录：**
- 一开始用本地Embedding模型，速度慢、效果差
- 换成OpenAI的API后，质量和速度都提升很多
- 成本其实不高，1000次查询约$0.1

### 3. RAG问答链

```python
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# 自定义Prompt模板
RAG_PROMPT_TEMPLATE = """你是一个企业知识库助手。请基于以下检索到的信息回答问题。

检索到的信息：
{context}

用户问题：{question}

要求：
1. 如果检索到的信息足够回答问题，请基于这些信息回答
2. 如果信息不足，请明确说明"根据现有资料无法回答"
3. 回答要简洁明了，突出重点
4. 在回答末尾标注信息来源

回答："""

prompt = PromptTemplate(
    template=RAG_PROMPT_TEMPLATE,
    input_variables=["context", "question"]
)

# 创建RAG链
def create_rag_chain(vectorstore):
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.3  # 降低随机性，保证回答稳定
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    
    return qa_chain

# 问答
def ask_question(question, qa_chain):
    result = qa_chain({"query": question})
    
    answer = result["result"]
    sources = result["source_documents"]
    
    # 格式化来源
    source_info = "\n\n**参考来源：**\n"
    for i, doc in enumerate(sources[:3], 1):
        source = doc.metadata.get("source", "未知")
        source_info += f"{i}. {source}\n"
    
    return answer + source_info
```

### 4. 权限控制实现

```python
# 在文档metadata中标注权限
def add_permission_metadata(documents, user_role):
    for doc in documents:
        # 根据文档路径或内容判断权限
        if "财务" in doc.metadata["source"]:
            doc.metadata["permission"] = ["finance", "admin"]
        elif "技术" in doc.metadata["source"]:
            doc.metadata["permission"] = ["tech", "admin"]
        else:
            doc.metadata["permission"] = ["all"]
    
    return documents

# 检索时过滤权限
def retrieve_with_permission(query, vectorstore, user_role):
    # 先检索所有相关文档
    all_results = vectorstore.similarity_search(query, k=20)
    
    # 过滤有权限的文档
    filtered_results = [
        doc for doc in all_results
        if user_role in doc.metadata.get("permission", ["all"])
    ]
    
    return filtered_results[:5]  # 返回前5个
```

---

## 五、效果评估

### 测试数据
- 文档数量：5000+篇
- 总字数：约1000万字
- 测试问题：100个

### 评估指标

| 指标 | 数值 | 说明 |
|------|------|------|
| 准确率 | 85% | 答案正确且完整 |
| 召回率 | 78% | 能找到相关文档 |
| 平均响应时间 | 3.2秒 | 从提问到返回答案 |
| 用户满意度 | 4.2/5 | 内部调研 |

### 典型问答示例

**Q: 我们公司的年假政策是什么？**

**A:** 根据公司《员工手册》规定：
- 工作满1年不满10年：年假5天
- 工作满10年不满20年：年假10天
- 工作满20年：年假15天

年假需在当年使用，可累计至次年3月。

**参考来源：**
1. 员工手册_v2024.pdf
2. HR政策文档/休假制度

---

## 六、踩过的坑和解决方案

### 坑1：文档切分导致上下文丢失

**问题：** 切分后的chunk缺少上下文，导致理解错误。

**解决：**
- 增加chunk_overlap（重叠区域）
- 在metadata中保存前后文信息
- 对重要文档做人工标注

### 坑2：检索结果不相关

**问题：** 用户问"Python教程"，检索到"Python招聘要求"。

**解决：**
- 使用重排序（Rerank）模型
- 增加关键词过滤
- 对文档打标签，提高检索精度

### 坑3：大模型"幻觉"

**问题：** 即使给了检索内容，模型还是会编造信息。

**解决：**
- 降低temperature参数
- 在Prompt中明确约束"只能基于给定信息回答"
- 增加"无法回答"的兜底策略

### 坑4：成本过高

**问题：** 初期Embedding和API调用成本超出预算。

**解决：**
- 使用更小的Embedding模型（text-embedding-3-small）
- 对高频问题做缓存
- 限制单次检索的文档数量

---

## 七、写在最后

RAG是目前最实用的企业AI应用方案之一。

它的优势在于：
- 技术成熟，有完整的开源方案
- 成本可控，适合中小企业
- 效果可预期，风险较低

如果你也想做类似的项目，建议：
1. 先从小范围试点开始
2. 重视数据质量和文档整理
3. 持续优化Prompt和检索策略

希望这篇实战记录对你有帮助。

---

## 🎁 福利时间

送你一份**《RAG项目实战资料包》**：
- 完整项目代码
- 部署文档
- 常见问题解决方案

👉 [点击免费领取](https://mp.weixin.qq.com/s/aGZoRDIX7hXexrHcNKBA2Q)

---

## 📚 想系统学习AI编程？

<p align="center" id='AI编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/643070fe-42e2-48ab-933d-148e85f059e4/527bb1299e6e9c65811d7ce15ebeb284.png" width="80%"/>
    </a>   
</p>

**《30讲 · AI编程训练营》** —— 从0到1掌握AI编程实战。

---

> 另外，大家去给小明的小红书👇账号点点赞吧~！

<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/41a33db6-85a2-4525-8ff9-18fce0d0397a/img_v3_02vr_8a1f882f-6ee0-4075-b794-7104e93746ag.jpg" width="60%"/>
</p>

---

<p align="center">
    <img src="https://cos.python-office.com/ads/gzh/sub-py.jpg" width="80%"/>
</p>

---

**🧧 领个红包再走呗~**

<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/fad13012-c22f-4c3a-b56e-c70787a55699/172ca166340cd6d0f52d356402901d4f.jpg" width="40%"/>
</p>

<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/6aa9a60e-bb4a-423c-a75d-cbd6ecf6f370/4dbea2fec93c415c75311666f19a1022.jpg" width="40%"/>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/d79c7834-a008-4512-a8ca-88a0b5a990a5/c14141a45d3b671ae94a11bd0556d1dc.jpg" width="40%"/>
</p>

---

程序员晚枫，专注AI编程培训，法律硕士转行的Python程序员，开源项目 [python-office](https://www.python-office.com/) 作者。


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


