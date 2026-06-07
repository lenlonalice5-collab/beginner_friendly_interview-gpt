# InterviewGPT

基于 Ollama + Qwen3 + Gradio 构建的本地 AI 模拟面试系统。

---

# 项目简介

InterviewGPT 是一个本地运行的 AI 面试助手。

系统能够模拟真实技术面试流程，通过大语言模型自动完成：

- AI面试提问
- AI回答评分
- AI反馈分析
- AI面试报告生成
- 能力画像分析
- 雷达图可视化
- 面试历史记录保存
- PDF报告导出

项目无需 OpenAI API，完全基于本地 Ollama 大模型运行。

---

# 功能演示流程

```text
开始面试
    ↓
AI提出问题
    ↓
用户回答
    ↓
Qwen3自动评分
    ↓
记录成绩
    ↓
进入下一题
    ↓
完成面试
    ↓
生成AI面试报告
    ↓
生成能力画像
    ↓
统计分析
    ↓
生成雷达图
    ↓
导出PDF报告
```

---

# 版本迭代

## V1.0

- 单轮面试
- AI评分
- AI反馈

---

## V2.0

- 多轮面试
- 自动切换题目
- 面试成绩统计
- 面试记录保存

---

## V3.0

- AI面试报告生成
- 优势分析
- 不足分析
- 学习建议
- 录用建议
- 能力画像分析

---

## V4.0

- PDF报告导出
- 历史记录系统
- JSON数据持久化
- 面试结果查询

---

## V4.1

- 平均分统计
- 最高分统计
- 最低分统计
- 能力雷达图
- 面试能力可视化分析

---

## V4.2（当前版本）

- 中文PDF支持
- PDF报告美化
- PDF嵌入雷达图
- 面试时长统计
- PDF显示统计信息
- 完整面试分析报告

---

# 技术栈

## AI能力

- Ollama
- Qwen3:8B
- Prompt Engineering

## 前端

- Gradio

## 后端

- Python

## 数据处理

- List
- Dictionary
- JSON
- Pandas

## 数据可视化

- Matplotlib

## PDF生成

- ReportLab

## Web服务

- FastAPI
- Uvicorn

## 版本管理

- Git
- GitHub

---

# 项目结构

```text
interview-gpt
│
├── app.py
├── scorer.py
├── report.py
├── history.py
├── pdf_export.py
├── radar_chart.py
├── questions.py
├── history.json
├── radar_chart.png
├── requirements.txt
└── README.md
```

---

# 核心功能

## 多轮AI面试

支持连续技术面试流程。

当前题库包含：

- RAG
- Embedding
- LangChain
- Prompt Engineering
- Agent

---

## AI自动评分

根据回答内容自动评估：

- 准确性
- 完整性
- 专业性

示例：

```text
评分：8

优点：
理解核心概念

缺点：
缺少实际应用案例
```

---

## AI面试报告

自动生成：

- 总体评价
- 优势分析
- 不足分析
- 学习建议
- 录用建议

---

## 能力画像

根据知识点统计得分：

```text
RAG         8/10
Embedding   7/10
LangChain   8/10
Prompt      9/10
Agent       6/10
```

帮助用户发现知识短板。

---

## 面试统计分析

自动统计：

```text
总题数：5

平均分：8.2

最高分：10

最低分：6
```

---

## 雷达图能力分析

根据各知识点得分生成能力雷达图。

分析维度：

- RAG
- Embedding
- LangChain
- Prompt Engineering
- Agent

帮助用户直观了解能力分布情况。

---

## 面试时长统计（V4.2）

自动记录：

```text
开始时间

结束时间

总耗时
```

示例：

```text
开始时间：
14:00

结束时间：
14:08

面试耗时：
8分钟
```

---

## 历史记录系统

自动保存面试记录：

```json
{
  "time": "2026-06-08 14:30:00",
  "score": 8,
  "skill": "RAG"
}
```

支持历史结果查看。

---

## PDF报告导出

支持导出完整面试分析报告：

包含：

- AI面试报告
- 能力画像
- 雷达图
- 面试统计
- 面试时长
- 学习建议

生成文件：

```text
Interview_Report.pdf
```

---

# 数据处理方法

项目使用 Python 基础数据结构完成数据管理。

## List

存储多轮面试记录：

```python
results = []
```

---

## Dictionary

结构化保存面试数据：

```python
{
    "skill":"RAG",
    "question":"什么是RAG？",
    "answer":"...",
    "score":8
}
```

---

## JSON

用于保存历史记录：

```text
history.json
```

---

## Prompt Engineering

通过Prompt设计引导Qwen3完成：

- 自动评分
- AI反馈
- 面试报告生成
- 学习建议生成

---

## 数据统计

根据面试结果计算：

- 平均分
- 最高分
- 最低分

形成能力画像。

---

## 数据可视化

利用 Matplotlib 生成：

```text
radar_chart.png
```

用于展示用户能力雷达图。

---

# 环境要求

```text
Python 3.11+
Ollama
Qwen3:8B
```

---

# 安装教程

## 克隆项目

```bash
git clone https://github.com/你的用户名/interview-gpt.git

cd interview-gpt
```

---

## 创建虚拟环境

```bash
python -m venv venv
```

Windows：

```bash
venv\Scripts\activate
```

---

## 安装依赖

```bash
pip install -r requirements.txt
```

---

# 核心依赖

```text
gradio==6.16.0
ollama==0.6.2
reportlab==4.5.1
matplotlib
numpy==2.4.6
pandas==3.0.3
fastapi==0.136.3
uvicorn==0.49.0
```

---

# 下载模型

```bash
ollama run qwen3:8b
```

首次运行会自动下载模型。

---

# 启动项目

```bash
python app.py
```

启动后访问：

```text
http://127.0.0.1:7860
```

---

# 项目亮点

- 本地大模型应用
- 无需OpenAI API
- 多轮AI面试
- AI自动评分
- AI面试报告生成
- 能力画像分析
- 雷达图能力可视化
- 面试时长统计
- 历史记录系统
- PDF报告导出
- 可扩展题库架构

---

# 下一步规划

## V5.0

多岗位面试系统

支持：

- AI应用开发工程师
- Python开发工程师
- 数据分析师
- 前端开发工程师
- Java开发工程师

---

## V6.0

AI动态出题系统

根据岗位自动生成面试题。

---

## V7.0

SQLite数据库

替代 history.json

支持：

- 面试记录查询
- 用户管理
- 数据统计

---

## V8.0

FastAPI接口化

实现前后端分离部署。

---

# License

MIT License