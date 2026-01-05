# Python Office Tools

## 项目说明
本项目基于python-office库，精选20个核心办公自动化功能，使用PySide6实现图形界面，并打包为可执行文件。

## 项目结构
```
code/
├── common/                    # 公共模块
│   ├── __init__.py
│   ├── ui_base.py            # 基础UI组件
│   └── styles.qss            # 样式表文件
├── excel_tools/              # Excel相关工具
├── word_tools/               # Word相关工具
├── pdf_tools/                # PDF相关工具
├── other_tools/              # 其他办公自动化工具
├── requirements.txt          # 依赖包列表
└── build_all.py             # 一键打包脚本
```

## 安装依赖
```bash
pip install -r requirements.txt
```

## 打包为可执行文件
```bash
python build_all.py
```

## 功能列表
1. Excel表格合并
2. Excel数据筛选
3. Excel数据透视表生成
4. Excel图表生成
5. Excel公式批量应用
6. Word文档批量替换
7. Word文档合并
8. Word文档转PDF
9. Word报告生成
10. Word表格处理
11. PDF合并
12. PDF拆分
13. PDF水印添加
14. PDF转图片
15. PDF加密解密
16. 文件批量重命名
17. 邮件批量发送
18. 图片批量处理
19. 数据清洗
20. 定时任务自动化