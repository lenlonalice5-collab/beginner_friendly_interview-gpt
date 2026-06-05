# InterviewGPT

基于 Ollama + Qwen3 + Gradio 的 AI 模拟面试系统。

## 项目简介

InterviewGPT 是一个本地运行的 AI 面试助手，能够模拟 AI 应用开发工程师岗位面试，对用户回答进行实时评分，并生成针对性的反馈建议。

本项目旨在帮助求职者进行面试练习，同时学习大模型应用开发的基本流程。

---

## 功能特性

### V1.0

* AI 自动面试提问
* 用户在线作答
* Qwen3 自动评分
* 输出回答优点
* 输出回答缺点
* 本地运行，无需调用云端 API

---

## 技术栈

* Python
* Gradio
* Ollama
* Qwen3
* Prompt Engineering

---

## 项目结构

```text
interview-gpt
│
├── app.py
├── scorer.py
├── questions.py
├── README.md
└── requirements.txt
```

---

## 安装步骤

### 1. 克隆项目

```bash
git clone https://github.com/你的用户名/interview-gpt.git
cd interview-gpt
```

### 2. 创建虚拟环境

```bash
python -m venv venv
```

Windows：

```bash
venv\Scripts\activate
```

### 3. 安装依赖

```bash
pip install gradio
pip install ollama
```

### 4. 安装 Ollama

下载：

https://ollama.com

检查版本：

```bash
ollama --version
```

### 5. 下载模型

```bash
ollama run qwen3:8b
```

---

## 运行项目

```bash
python app.py
```

启动成功后访问：

```text
http://127.0.0.1:7860
```

---

## 使用示例

面试题：

```text
什么是RAG？
```

用户回答：

```text
RAG由检索和生成两个阶段组成。
```

AI评价：

```text
评分：8/10

优点：
回答正确描述了RAG基本流程

缺点：
未解释Embedding与向量检索过程
```

---

## 项目亮点

* 基于本地大模型实现
* 支持面试场景模拟
* Prompt驱动自动评分
* 易于扩展题库
* 可升级为多轮面试系统

---

## 未来规划

### V2

* 多轮面试
* 下一题功能
* 历史记录保存

### V3

* 自动生成面试报告
* 能力画像分析
* AI学习建议

### V4

* 多岗位支持

  * AI应用开发工程师
  * Python开发工程师
  * 数据分析师
  * 机器学习工程师

### V5

* PDF面试报告导出
* FastAPI接口
* Docker部署

---

## 作者

连明凡

数据科学与大数据技术专业

研究方向：

* AI应用开发
* 大模型应用
* RAG系统
* Agent开发

---

## License

MIT License
