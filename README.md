# InterviewGPT

<p align="center">
  <b>AI-Powered Technical Interview Simulator</b><br>
  基于 Large Language Model 的智能技术面试模拟平台
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue">
  <img src="https://img.shields.io/badge/Gradio-WebUI-orange">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green">
  <img src="https://img.shields.io/badge/SQLite-Database-blue">
  <img src="https://img.shields.io/badge/DeepSeek-LLM-success">
  <img src="https://img.shields.io/badge/Whisper-ASR-purple">
  <img src="https://img.shields.io/badge/Version-v6.5-red">
</p>

---

# 📖 Project Overview | 项目简介

InterviewGPT 是一个基于大语言模型（LLM）的智能面试模拟系统。

系统能够根据岗位自动生成面试题、实时评分、生成追问、构建能力画像、生成面试报告，并支持本地语音识别、数据库存储、用户管理以及 API 接口化部署。

InterviewGPT is an AI-powered mock interview platform built with Large Language Models.

It automatically generates interview questions, evaluates answers, creates follow-up questions, analyzes competencies, stores interview records, and supports local speech recognition and API deployment.

---

# ✨ Features | 核心功能

## 🤖 AI Interview Simulation

智能面试模拟

* 自动生成面试题
* 支持多岗位面试
* 模拟真实技术面试流程
* 重新生成题目

---

## 🧠 AI Answer Evaluation

AI 回答评分

* 自动评分
* 回答分析
* 优缺点评估
* 综合反馈

---

## 🔄 Dynamic Follow-up Questions

智能追问机制

* 根据回答生成追问
* 模拟真实面试官逻辑
* 自动控制追问轮次

---

## 🎤 Whisper Speech Recognition

本地语音识别

* Whisper 本地部署
* 中文语音转文字
* 麦克风录音输入
* 离线运行
* 无需第三方 ASR 服务

---

## 📊 Interview Statistics

面试统计

* 完成题目数
* 平均得分
* 面试时长
* 技能统计

---

## 🎯 Skill Profile Analysis

能力画像分析

支持：

* Python
* Machine Learning
* Deep Learning
* NLP
* Data Analysis
* LLM Engineering

等多个维度分析。

---

## 📈 Radar Chart

能力雷达图

自动生成：

* 技能评分
* 能力分布
* 图形可视化

---

## 📄 AI Interview Report

AI 面试报告

自动输出：

* 综合评价
* 优势分析
* 不足分析
* 提升建议

---

## 📑 PDF Export

PDF 导出

包含：

* 面试报告
* 面试统计
* 能力雷达图
* 岗位信息
* 面试时长

---

## 💾 SQLite Database

数据库管理

InterviewGPT V6.3 开始支持 SQLite。

支持存储：

* 用户信息
* 面试记录
* 成绩记录
* 错题记录

---

## 👤 User System

用户系统

InterviewGPT V6.4 新增：

* 用户注册
* 用户登录
* 用户成绩统计
* 面试次数统计
* 用户档案

---

## 🏆 Leaderboard

排行榜系统

根据：

* 平均成绩
* 面试次数

自动生成排行榜。

---

## 🚀 FastAPI Backend

接口化部署

InterviewGPT V6.5 开始支持：

* FastAPI REST API
* Swagger 文档
* 前后端分离
* API 调用评分服务
* API 调用题目生成服务

实现从单体应用向 AI SaaS 架构升级。

---

# 🏗️ System Architecture | 系统架构

```text
                    ┌───────────────┐
                    │    Gradio UI   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    FastAPI     │
                    └───────┬───────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼

 Question API        Score API        Follow-up API

        ▼                   ▼                   ▼

                 DeepSeek LLM Service

                            │
                            ▼

                     SQLite Database

                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼

      Users          Interviews        Mistakes

                            │
                            ▼

                    Report System

                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼

      Statistics      Radar Chart      PDF Export

                            │
                            ▼

                     Whisper ASR
```

---

# 📂 Project Structure | 项目结构

```text
InterviewGPT/

├── app.py
├── api.py
│
├── database.py
├── history.py
│
├── scorer.py
├── followup.py
├── question_generator.py
│
├── report.py
├── radar_chart.py
├── pdf_export.py
│
├── speech.py
│
├── interview.db
├── history.json
│
├── reports/
├── charts/
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation | 安装

## Clone Repository

```bash
git clone https://github.com/yourname/interview-gpt.git

cd interview-gpt
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Whisper

```bash
pip install openai-whisper
```

---

## Install FastAPI

```bash
pip install fastapi uvicorn
```

---

## Install FFmpeg

验证：

```bash
ffmpeg -version
```

---

# ▶️ Run Gradio

```bash
python app.py
```

访问：

```text
http://127.0.0.1:7860
```

---

# ▶️ Run FastAPI

```bash
python -m uvicorn api:app --reload
```

访问：

```text
http://127.0.0.1:8000
```

Swagger：

```text
http://127.0.0.1:8000/docs
```

---

# 📊 Current Capabilities

| Module              | Status |
| ------------------- | ------ |
| Question Generation | ✅      |
| AI Scoring          | ✅      |
| Follow-up Questions | ✅      |
| Whisper ASR         | ✅      |
| SQLite Database     | ✅      |
| User System         | ✅      |
| Leaderboard         | ✅      |
| Statistics          | ✅      |
| Skill Analysis      | ✅      |
| Radar Chart         | ✅      |
| PDF Export          | ✅      |
| FastAPI             | ✅      |

---

# 🛣️ Roadmap

## V6.6

计划开发：

* JWT 用户认证
* Token 登录
* API 权限控制
* 用户会话管理
* 用户错题本

---

## V7.0

长期规划：

* RAG 面试知识库
* 本地大模型支持
* 多模态面试
* Docker部署
* Vue 前端
* 在线部署版本
* 企业级 AI 面试平台

---

# 🧑‍💻 Author

Developed by Lenlon

Built with:

* Python
* Gradio
* FastAPI
* SQLite
* DeepSeek API
* Whisper
* Matplotlib
* ReportLab

---

# 📜 License

MIT License

Feel free to use, modify and contribute.

欢迎 Star ⭐ 和 Fork 🍴
      Statistics      Radar Chart      PDF Export

                            │
                            ▼

                     Whisper ASR
```

---

# 📂 Project Structure | 项目结构

```text
InterviewGPT/

├── app.py
├── api.py
│
├── database.py
├── history.py
│
├── scorer.py
├── followup.py
├── question_generator.py
│
├── report.py
├── radar_chart.py
├── pdf_export.py
│
├── speech.py
│
├── interview.db
├── history.json
│
├── reports/
├── charts/
│
├── requirements.txt
└── README.md
```

---

# 🚀 Installation | 安装

## Clone Repository

```bash
git clone https://github.com/yourname/interview-gpt.git

cd interview-gpt
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Whisper

```bash
pip install openai-whisper
```

---

## Install FastAPI

```bash
pip install fastapi uvicorn
```

---

## Install FFmpeg

验证：

```bash
ffmpeg -version
```

---

# ▶️ Run Gradio

```bash
python app.py
```

访问：

```text
http://127.0.0.1:7860
```

---

# ▶️ Run FastAPI

```bash
python -m uvicorn api:app --reload
```

访问：

```text
http://127.0.0.1:8000
```

Swagger：

```text
http://127.0.0.1:8000/docs
```

---

# 📊 Current Capabilities

| Module              | Status |
| ------------------- | ------ |
| Question Generation | ✅      |
| AI Scoring          | ✅      |
| Follow-up Questions | ✅      |
| Whisper ASR         | ✅      |
| SQLite Database     | ✅      |
| User System         | ✅      |
| Leaderboard         | ✅      |
| Statistics          | ✅      |
| Skill Analysis      | ✅      |
| Radar Chart         | ✅      |
| PDF Export          | ✅      |
| FastAPI             | ✅      |

---

# 🛣️ Roadmap

## V6.6

计划开发：

* JWT 用户认证
* Token 登录
* API 权限控制
* 用户会话管理
* 用户错题本

---

## V7.0

长期规划：

* RAG 面试知识库
* 本地大模型支持
* 多模态面试
* Docker部署
* Vue 前端
* 在线部署版本
* 企业级 AI 面试平台

---

# 🧑‍💻 Author

Developed by Lenlon

Built with:

* Python
* Gradio
* FastAPI
* SQLite
* DeepSeek API
* Whisper
* Matplotlib
* ReportLab

---

# 📜 License

MIT License

Feel free to use, modify and contribute.

欢迎 Star ⭐ 和 Fork 🍴
