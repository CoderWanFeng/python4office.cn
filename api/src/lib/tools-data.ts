import { Tool } from './tools-registry';

export const TOOLS_DATA: Tool[] = [
  {
    id: 'openai-whisper',
    name: 'OpenAI Whisper',
    nameEn: 'Whisper',
    description: 'OpenAI开源的语音识别模型，支持多语言转录',
    descriptionForAI: 'Whisper是OpenAI开源的自动语音识别系统。能准确将语音转换为文字，支持99种语言和方言。适合转录、翻译、字幕生成等场景。Python接口简单易用。',
    category: 'audio-processing',
    capabilities: [
      'speech-to-text',
      'multilingual',
      'transcription',
      'translation'
    ],
    endpoints: {
      api: 'https://github.com/openai/whisper',
      docs: 'https://github.com/openai/whisper#readme'
    },
    auth: {
      type: 'none',
      registrationUrl: 'https://github.com/openai/whisper',
      authDocs: 'https://github.com/openai/whisper#setup'
    },
    pricing: {
      hasFreeTier: true,
      pricingModel: 'freemium'
    },
    metadata: {
      tags: ['语音识别', '开源', 'Python', '多语言'],
      useCases: [
        '会议录音转文字',
        '视频字幕生成',
        '语音翻译',
        '内容分析'
      ],
      examples: [
        'import whisper\nmodel = whisper.load_model("base")\nresult = model.transcribe("audio.mp3")'
      ]
    },
    openclaw: {
      compatible: true,
      difficulty: 'easy',
      configTemplate: {
        model: 'base'
      },
      setupGuide: 'pip install openai-whisper'
    },
    stats: {
      popularity: 95,
      rating: 4.8
    },
    lastUpdated: '2026-05-15'
  },
  {
    id: 'langchain',
    name: 'LangChain',
    nameEn: 'LangChain',
    description: '构建LLM应用的Python框架',
    descriptionForAI: 'LangChain是用于构建LLM应用的框架。提供链式调用、记忆、工具调用等功能。支持多种LLM后端，可以快速构建聊天机器人、问答系统等应用。',
    category: 'python-library',
    capabilities: [
      'llm-integration',
      'chain-building',
      'memory-management',
      'tool-calling',
      'rag'
    ],
    endpoints: {
      api: 'https://python.langchain.com/',
      docs: 'https://python.langchain.com/docs'
    },
    auth: {
      type: 'none',
      registrationUrl: 'https://python.langchain.com/',
      authDocs: 'https://python.langchain.com/docs/get_started'
    },
    pricing: {
      hasFreeTier: true,
      pricingModel: 'freemium'
    },
    metadata: {
      tags: ['LLM', '框架', 'RAG', '聊天机器人'],
      useCases: [
        '构建聊天机器人',
        '文档问答系统',
        '自动化工作流',
        '数据处理管道'
      ],
      examples: [
        'from langchain.chat_models import ChatOpenAI\nllm = ChatOpenAI(model="gpt-4")'
      ]
    },
    openclaw: {
      compatible: true,
      difficulty: 'medium',
      configTemplate: {
        openai_api_key: '{{user_api_key}}'
      },
      setupGuide: 'pip install langchain openai'
    },
    stats: {
      popularity: 98,
      rating: 4.6
    },
    lastUpdated: '2026-05-18'
  },
  {
    id: 'transformers',
    name: 'Hugging Face Transformers',
    nameEn: 'Transformers',
    description: '最流行的NLP预训练模型库',
    descriptionForAI: 'Transformers是Hugging Face的核心库，提供数千个预训练模型。支持文本分类、命名实体识别、问答、文本生成等任务。开箱即用，文档完善。',
    category: 'text-generation',
    subcategory: 'nlp',
    capabilities: [
      'text-classification',
      'named-entity-recognition',
      'question-answering',
      'text-generation',
      'translation',
      'summarization'
    ],
    endpoints: {
      api: 'https://huggingface.co/docs/transformers',
      docs: 'https://huggingface.co/docs/transformers',
      playground: 'https://huggingface.co/inference-api'
    },
    auth: {
      type: 'none',
      registrationUrl: 'https://huggingface.co/',
      authDocs: 'https://huggingface.co/docs/transformers/quicktour'
    },
    pricing: {
      hasFreeTier: true,
      pricingModel: 'freemium'
    },
    metadata: {
      tags: ['NLP', '预训练模型', '开源', '文本处理'],
      useCases: [
        '情感分析',
        '文本分类',
        '智能问答',
        '文本生成'
      ],
      examples: [
        'from transformers import pipeline\nclassifier = pipeline("sentiment-analysis")'
      ]
    },
    openclaw: {
      compatible: true,
      difficulty: 'easy',
      configTemplate: {
        model: 'distilbert-base-uncased-finetuned-sst-2-english'
      },
      setupGuide: 'pip install transformers torch'
    },
    stats: {
      popularity: 100,
      rating: 4.9
    },
    lastUpdated: '2026-05-10'
  },
  {
    id: 'gradio',
    name: 'Gradio',
    nameEn: 'Gradio',
    description: '快速构建机器学习Web界面的Python库',
    descriptionForAI: 'Gradio让你快速创建机器学习模型的Web演示界面。无需前端知识，几行代码就能创建交互式界面。支持图像、文本、音频等多种输入输出类型。',
    category: 'python-library',
    capabilities: [
      'web-interface',
      'model-deployment',
      'interactive-demo',
      'api-generation'
    ],
    endpoints: {
      api: 'https://gradio.app/',
      docs: 'https://gradio.app/docs'
    },
    auth: {
      type: 'none',
      registrationUrl: 'https://gradio.app/',
      authDocs: 'https://gradio.app/quickstart'
    },
    pricing: {
      hasFreeTier: true,
      pricingModel: 'freemium'
    },
    metadata: {
      tags: ['Web界面', '机器学习', '快速开发', '演示'],
      useCases: [
        'AI模型演示',
        '快速原型开发',
        '交互式测试',
        'API分享'
      ],
      examples: [
        'import gradio as gr\niface = gr.Interface(fn=model.predict, inputs="text", outputs="text")'
      ]
    },
    openclaw: {
      compatible: true,
      difficulty: 'easy',
      configTemplate: {},
      setupGuide: 'pip install gradio'
    },
    stats: {
      popularity: 92,
      rating: 4.7
    },
    lastUpdated: '2026-05-12'
  },
  {
    id: 'openai-api',
    name: 'OpenAI API',
    nameEn: 'OpenAI',
    description: 'GPT系列模型的官方API',
    descriptionForAI: 'OpenAI提供GPT-4、GPT-3.5等强大语言模型的API。支持文本生成、代码编写、图像理解等多种功能。是目前最流行的AI API之一。',
    category: 'api-service',
    capabilities: [
      'text-generation',
      'code-generation',
      'image-understanding',
      'function-calling',
      'fine-tuning'
    ],
    endpoints: {
      api: 'https://api.openai.com/v1',
      docs: 'https://platform.openai.com/docs',
      playground: 'https://platform.openai.com/playground'
    },
    auth: {
      type: 'api-key',
      registrationUrl: 'https://platform.openai.com/signup',
      authDocs: 'https://platform.openai.com/docs/api-reference/authentication'
    },
    pricing: {
      hasFreeTier: true,
      freeCredits: 5,
      startingPrice: 0.002,
      pricingModel: 'per-call'
    },
    metadata: {
      tags: ['GPT', 'LLM', 'API', 'OpenAI'],
      useCases: [
        '聊天机器人',
        '内容创作',
        '代码助手',
        '数据分析'
      ],
      examples: [
        'import openai\nresponse = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": "Hello!"}])'
      ]
    },
    openclaw: {
      compatible: true,
      difficulty: 'easy',
      configTemplate: {
        apiKey: '{{user_api_key}}',
        model: 'gpt-4'
      },
      setupGuide: 'pip install openai && export OPENAI_API_KEY=your_key'
    },
    stats: {
      popularity: 100,
      rating: 4.9
    },
    lastUpdated: '2026-05-20'
  }
];
