# InterviewGPT

<p align="center">
  <b>AI-Powered Technical Interview Simulator</b><br>
  基于 Large Language Model 的智能技术面试模拟平台
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue">
  <img src="https://img.shields.io/badge/Gradio-WebUI-orange">
  <img src="https://img.shields.io/badge/DeepSeek-LLM-green">
  <img src="https://img.shields.io/badge/Whisper-ASR-purple">
  <img src="https://img.shields.io/badge/Version-v6.2-red">
</p>

---

## 📖 Project Overview | 项目简介

InterviewGPT 是一个基于大语言模型（LLM）的 AI 模拟面试系统。

系统能够根据目标岗位自动生成面试题，实时分析候选人回答，进行评分、追问、能力评估，并自动生成专业面试报告。

InterviewGPT is an AI-powered mock interview platform built with Large Language Models.

It automatically generates interview questions, evaluates candidate responses, provides follow-up questions, analyzes competencies, and generates professional interview reports.

---

## ✨ Features | 核心功能

### 🤖 AI Interview Simulation

智能面试模拟

* 根据岗位自动生成面试题
* 支持多岗位扩展
* 模拟真实技术面试流程
* 支持重新生成题目

---

### 🧠 AI Answer Evaluation

AI 回答评分

* 自动评分
* 回答优缺点分析
* 面试表现反馈
* 综合能力评估

---

### 🔄 Dynamic Follow-up Questions

智能追问机制

* 基于回答内容生成追问
* 模拟真实面试官提问逻辑
* 自动控制追问轮次
* 提高面试真实性

---

### 🎤 Local Speech Recognition

本地语音识别

* Whisper 本地部署
* 麦克风录音
* 中文语音转文字
* 无需云端 ASR 服务
* 支持离线运行

---

### 📊 Interview Statistics

面试数据统计

* 已完成题目数
* 平均得分
* 面试时长统计
* 技能维度分析

---

### 🎯 Skill Profile Analysis

能力画像分析

自动统计：

* Python
* Machine Learning
* Deep Learning
* NLP
* Data Analysis
* LLM Engineering

等能力维度表现。

---

### 📈 Radar Chart Visualization

能力雷达图

自动生成：

* 技能维度评分
* 能力分布分析
* 中文字体支持
* PDF集成展示

---

### 📄 AI Interview Report

AI面试报告

自动生成：

* 综合评价
* 优势分析
* 不足分析
* 提升建议
* 后续学习方向

---

### 📑 PDF Export

PDF导出

导出内容包括：

* 面试报告
* 面试统计
* 面试时长
* 能力雷达图
* 岗位信息

---

### 💾 Interview History

历史记录管理

* 本地保存面试记录
* 历史面试回顾
* 成绩追踪

---

## 🏗️ System Architecture | 系统架构

```text
┌──────────────┐
│   Gradio UI  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ InterviewGPT │
└──────┬───────┘
       │
 ┌─────┼─────┐
 ▼     ▼     ▼

Question  Scorer  Follow-up
Generator Engine  Generator

 ▼
DeepSeek API

 ▼

Report System
 │
 ├── Statistics
 ├── Skill Profile
 ├── Radar Chart
 └── PDF Export

 ▼

Whisper ASR
(Voice → Text)
```

---

## 📂 Project Structure | 项目结构

```text
InterviewGPT/
│
├── app.py
├── scorer.py
├── followup.py
├── question_generator.py
├── report.py
├── radar_chart.py
├── pdf_export.py
├── history.py
├── speech.py
│
├── reports/
├── history/
├── charts/
│
├── requirements.txt
└── README.md
```

---

## 🚀 Installation | 安装

### 1. Clone Repository

```bash
git clone https://github.com/yourname/interview-gpt.git

cd interview-gpt
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Whisper

```bash
pip install openai-whisper
```

---

### 5. Install FFmpeg

Windows 用户需要安装 FFmpeg 并加入环境变量。

验证：

```bash
ffmpeg -version
```

---

## ▶️ Run

```bash
python app.py
```

访问：

```text
http://127.0.0.1:7860
```

---

## 📊 Current Capabilities | 当前能力

| Module              | Status |
| ------------------- | ------ |
| Question Generation | ✅      |
| AI Scoring          | ✅      |
| Follow-up Questions | ✅      |
| Statistics          | ✅      |
| Skill Analysis      | ✅      |
| Radar Chart         | ✅      |
| PDF Export          | ✅      |
| History Records     | ✅      |
| Whisper ASR         | ✅      |

---

## 🛣️ Roadmap

### V6.3

计划开发：

* 多轮追问优化
* 流式输出
* 面试难度调节
* 岗位知识库
* SQLite数据库
* 用户登录系统
* 面试排行榜

### V7.0

长期规划：

* RAG知识库面试
* 本地大模型支持
* 多模态面试
* 在线部署版本
* 企业级面试平台

---

## 🧑‍💻 Author

Developed by Lenlon

Built with:

* Python
* Gradio
* DeepSeek API
* Whisper
* ReportLab
* Matplotlib

---

## 📜 License

MIT License

Feel free to use, modify and contribute.

欢迎 Star ⭐ 和 Fork 🍴
