# InterviewGPT

基于 Ollama + Qwen3 + Gradio 构建的本地 AI 模拟面试系统。

## 项目简介

InterviewGPT 是一个面向 AI 应用开发岗位的智能面试助手。

系统能够模拟真实技术面试流程，通过大模型自动完成：

* 面试提问
* 回答评分
* AI反馈
* 能力画像分析
* AI面试报告生成
* PDF报告导出
* 历史记录保存
* 雷达图能力分析

项目完全本地运行，无需调用 OpenAI API 或其他云端服务。

---

## 功能流程

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
保存历史记录
    ↓
导出PDF报告
```

---

## 功能版本

### V1.0

* 单轮面试
* AI评分
* 回答反馈

### V2.0

* 多轮面试
* 自动切换题目
* 面试成绩统计
* 面试记录保存

### V3.0

* AI面试报告
* 优势分析
* 不足分析
* 学习建议
* 录用建议
* 能力画像

### V4.0

* PDF报告导出
* 历史记录系统
* JSON数据持久化
* 面试结果查询

### V4.1（当前版本）

* 平均分统计
* 最高分统计
* 最低分统计
* 能力雷达图
* 面试能力分析可视化

---

## 技术栈

### AI能力

* Ollama
* Qwen3:8B
* Prompt Engineering

### 前端界面

* Gradio

### 后端逻辑

* Python

### 数据处理

* List
* Dictionary
* JSON
* Pandas

### 数据可视化

* Matplotlib

### 报告生成

* ReportLab

### Web服务

* FastAPI
* Uvicorn

### 版本管理

* Git
* GitHub

---

## 项目结构

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

## 核心功能

### 多轮AI面试

支持连续技术面试流程。

当前题库包含：

* 什么是RAG？
* 什么是Embedding？
* LangChain有什么作用？
* 什么是Prompt Engineering？
* 什么是Agent？

---

### AI自动评分

根据回答内容自动评估：

* 准确性
* 完整性
* 专业性

示例输出：

```text
评分：8

优点：
理解了核心概念

缺点：
缺少实际应用说明
```

---

### AI面试报告

自动生成：

* 总体评价
* 优势分析
* 不足分析
* 学习建议
* 录用建议

---

### 能力画像

根据知识点统计得分：

```text
RAG         8/10
Embedding   7/10
LangChain   8/10
Prompt      9/10
Agent       5/10
```

帮助用户发现知识短板。

---

### 面试统计分析

自动统计：

```text
总题数：5

平均分：8.2

最高分：10

最低分：6
```

帮助用户快速了解整体表现。

---

### 雷达图能力分析

根据各知识点得分生成能力雷达图。

示例维度：

* RAG
* Embedding
* LangChain
* Prompt Engineering
* Agent

通过可视化方式展示知识掌握情况。

---

### 历史记录系统

自动保存面试结果：

```json
{
    "time": "2026-06-08 10:30:00",
    "results": [
        {
            "skill": "RAG",
            "score": 8
        }
    ]
}
```

支持历史记录查看。

---

### PDF报告导出

支持导出完整面试报告：

* 面试成绩
* AI分析结果
* 能力画像
* 学习建议
* 面试统计信息

方便保存和分享。

---

## 数据处理方法

项目使用 Python 基础数据结构完成数据管理。

### List

用于存储多轮面试记录：

```python
results = []
```

### Dictionary

用于结构化保存面试数据：

```python
{
    "skill": "RAG",
    "question": "什么是RAG",
    "answer": "...",
    "score": 8
}
```

### JSON

用于历史记录持久化：

```python
history.json
```

### Prompt Engineering

通过构造 Prompt 引导 Qwen3 完成：

* 自动评分
* 优势分析
* 不足分析
* 学习建议生成

### 数据统计

根据不同知识点分类统计：

* 平均分
* 最高分
* 最低分

生成用户能力画像。

### 数据可视化

使用 Matplotlib 生成：

```text
radar_chart.png
```

用于展示能力雷达图。

---

## 环境要求

### Python版本

```text
Python 3.11+
```

---

## 安装教程

### 克隆项目

```bash
git clone https://github.com/你的用户名/interview-gpt.git
cd interview-gpt
```

### 创建虚拟环境

```bash
python -m venv venv
```

Windows：

```bash
venv\Scripts\activate
```

### 安装依赖

```bash
pip install -r requirements.txt
```

---

## 核心依赖

```text
gradio==6.16.0
ollama==0.6.2
reportlab==4.5.1
matplotlib==3.x
pandas==3.0.3
fastapi==0.136.3
uvicorn==0.49.0
numpy==2.4.6
```

---

## 下载模型

```bash
ollama run qwen3:8b
```

首次运行会自动下载模型。

---

## 启动项目

```bash
python app.py
```

启动后访问：

```text
http://127.0.0.1:7860
```

---

## 项目亮点

* 本地大模型应用
* 无需OpenAI API
* 多轮AI面试
* AI自动评分
* AI面试报告生成
* 能力画像分析
* 雷达图能力可视化
* 历史记录系统
* PDF报告导出
* 可扩展题库架构

---

## 开发路线

### 已完成

* [x] V1 单轮面试
* [x] V2 多轮面试
* [x] V3 AI面试报告
* [x] V4 PDF导出与历史记录
* [x] V4.1 统计分析与雷达图

### 下一版本 V4.2

* [ ] 中文PDF支持
* [ ] PDF排版优化
* [ ] PDF嵌入雷达图
* [ ] 面试时间统计

### V5

* [ ] SQLite数据库
* [ ] 用户系统
* [ ] 登录注册
* [ ] FastAPI接口
* [ ] Docker部署

---

## License

MIT License
