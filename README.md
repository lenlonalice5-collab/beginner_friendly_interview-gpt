# SurveySpark

<p align="center">
  <b>Enterprise-Level AI Interview Simulation Platform</b><br>
  企业级 AI 面试模拟与能力成长分析平台
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue">
  <img src="https://img.shields.io/badge/Gradio-WebUI-orange">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green">
  <img src="https://img.shields.io/badge/SQLite-Database-blue">
  <img src="https://img.shields.io/badge/DeepSeek-LLM-green">
  <img src="https://img.shields.io/badge/Whisper-ASR-purple">
  <img src="https://img.shields.io/badge/Version-v6.6-red">
</p>

---

# 📖 Project Overview | 项目简介

InterviewGPT 是一个基于大语言模型（LLM）的智能面试平台。

不仅能够模拟真实技术面试流程，还能够长期记录用户成长轨迹，分析面试表现变化趋势，并生成专业能力成长报告。

InterviewGPT is an AI-powered interview simulation platform built with Large Language Models.

It provides interview question generation, answer evaluation, follow-up questioning, speech recognition, user management, ranking systems, interview history tracking, and long-term growth analysis.

---

# 🚀 Current Features | 当前功能

## 🤖 AI Interview Simulation

* AI 自动生成岗位面试题
* 多岗位扩展支持
* 动态追问机制
* 模拟真实技术面试

---

## 🧠 AI Answer Evaluation

* 回答自动评分
* 优缺点分析
* 综合能力评价
* 提升建议生成

---

## 🔄 Dynamic Follow-up Questions

* AI智能追问
* 基于上下文继续提问
* 控制追问轮次
* 模拟真实面试官

---

## 🎤 Whisper Speech Recognition

* 本地 Whisper 部署
* 麦克风录音
* 中文语音转文字
* 离线运行

---

## 👤 User System

用户系统

* 用户注册
* 用户登录
* 用户数据隔离
* 个人中心

---

## 🏆 Leaderboard System

排行榜系统

* 平均分排行
* 面试次数排行
* 用户成长比较
* Top 用户展示

---

## 💾 SQLite Database

数据库系统

使用 SQLite 持久化存储：

### interviews

保存每道面试题

* question
* answer
* score
* skill

### users

保存用户信息

* username
* total_score
* interview_count

### interview_sessions

保存每场面试

* avg_score
* duration
* create_time

### mistakes

错题记录

* question
* answer
* score

---

## 📈 Growth Trend Analysis

成长趋势分析

自动记录：

* 每场面试平均分
* 面试时间
* 面试次数

生成：

* 历史成绩趋势图
* 成长曲线
* 学习效果分析

---

## 📊 Statistics Dashboard

统计分析

支持：

* 平均分
* 最高分
* 最低分
* 面试时长
* 技能维度统计

---

## 🎯 Skill Profile Analysis

能力画像

支持：

* Python
* Machine Learning
* Deep Learning
* NLP
* Data Analysis
* LLM Engineering

能力维度分析

---

## 📈 Radar Chart

能力雷达图

自动生成：

* 技能评分
* 能力分布
* PDF嵌入

---

## 📄 AI Interview Report

自动生成：

* 综合评价
* 优势分析
* 不足分析
* 学习建议

---

## 📑 PDF Export

导出：

* AI报告
* 面试统计
* 能力画像
* 雷达图
* 面试时长

---

## 🌐 FastAPI Backend

接口化架构

已实现：

* /question
* /score

支持：

* 前后端分离
* Web部署
* 移动端接入
* 企业级扩展

---

# 🏗️ Architecture

Gradio UI

↓

FastAPI Backend

↓

Interview Engine

├── Question Generator

├── Scoring Engine

├── Follow-up Engine

├── Whisper ASR

├── User System

├── Leaderboard

├── Growth Analysis

↓

SQLite Database

↓

Reports & Visualization

---

# 📂 Project Structure

InterviewGPT/

├── app.py

├── api.py

├── database.py

├── speech.py

├── history.py

├── scorer.py

├── followup.py

├── report.py

├── trend_chart.py

├── radar_chart.py

├── pdf_export.py

├── question_generator.py

├── interview.db

├── history.json

└── README.md

---

# 📊 Version Timeline

## V6.1

* AI面试系统
* AI评分
* PDF导出
* 能力画像

## V6.2

* Whisper语音识别
* 本地ASR
* 麦克风录音

## V6.3

* SQLite数据库
* 数据持久化
* 历史记录优化

## V6.4

* 用户系统
* 登录功能

## V6.5

* 排行榜系统
* 用户统计

## V6.6

* 面试场次记录
* 成长趋势分析
* 趋势图生成
* FastAPI接口化

---

# 🛣️ Roadmap

## V7.0

计划开发：

* JWT认证
* 错题本系统
* AI成长报告
* RAG知识库面试
* 本地大模型支持
* Docker部署
* Vue前端重构

---

# 🧑‍💻 Author

Developed by Lenlon

Built with

* Python
* Gradio
* FastAPI
* SQLite
* DeepSeek
* Whisper
* Matplotlib
* ReportLab

---

# 📜 License

MIT License

Feel free to use, modify and contribute.

欢迎 Star ⭐ 和 Fork 🍴
