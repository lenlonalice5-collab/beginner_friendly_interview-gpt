# InterviewGPT

<div align="center">

### 🚀 AI-Powered Multi-Role Interview Simulation Platform

基于 **Ollama + Gradio + Python** 构建的智能面试系统，支持多岗位面试、AI评分、追问机制、能力分析、雷达图可视化与 PDF 报告生成。

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Gradio](https://img.shields.io/badge/Gradio-6.x-orange)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-green)
![Version](https://img.shields.io/badge/Version-v6.1.1-red)

</div>

---

# ✨ 项目简介

InterviewGPT 是一个本地运行的 AI 面试官系统。

用户选择目标岗位后，系统将自动生成专业面试题，对回答进行智能评分，并根据回答质量生成追问问题，最终形成完整的能力分析报告。

项目从 V1 持续迭代至 V6，目前已具备完整的 AI 面试流程。

---

# 🎯 核心功能

## 多岗位面试

支持以下岗位：

* AI应用开发工程师
* Python开发工程师
* 数据分析师
* Java开发工程师
* 前端开发工程师
* 测试工程师
* 产品经理
* 算法工程师
* 机器学习工程师

---

## AI智能评分

根据回答内容进行分析：

* 技术准确性
* 逻辑表达能力
* 解决问题能力
* 项目经验匹配度

输出：

* 分数
* 优点分析
* 缺点分析
* 改进建议

---

## AI追问机制

当回答质量较高时：

```text
面试题
 ↓
用户回答
 ↓
AI分析
 ↓
生成追问问题
 ↓
用户继续作答
```

模拟真实技术面试过程。

---

## 面试统计分析

自动统计：

* 完成题数
* 平均分
* 最高分
* 最低分

帮助用户了解整体面试表现。

---

## 技能雷达图

自动生成能力画像：

* Python
* RAG
* Prompt Engineering
* LangChain
* Agent
* Embedding

支持中文显示。

---

## PDF报告导出

生成完整面试报告：

包含：

* 岗位名称
* 面试时间
* 面试记录
* AI评价
* 能力雷达图
* 综合分析

---

# 🏗️ 技术架构

```text
                ┌────────────┐
                │   Gradio   │
                └─────┬──────┘
                      │
                      ▼
              ┌─────────────┐
              │ InterviewGPT│
              └─────┬───────┘
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼

 Question      AI Scoring      Follow-up

     ▼              ▼              ▼

 History      Statistics      PDF Report

     ▼

 Radar Chart
```

---

# 📁 项目结构

```text
interview-gpt/

├── app.py
├── questions.py
├── scorer.py
├── report.py
├── history.py
├── pdf_export.py
├── radar_chart.py
├── history.json
├── requirements.txt
└── README.md
```

---

# ⚙️ 环境配置

## 创建虚拟环境

```bash
python -m venv venv
```

Windows：

```bash
venv\Scripts\activate
```

Mac / Linux：

```bash
source venv/bin/activate
```

---

## 安装依赖

```bash
pip install -r requirements.txt
```

---

## 启动 Ollama

确保本地模型已安装：

```bash
ollama run qwen3
```

或：

```bash
ollama run llama3
```

---

## 运行项目

```bash
python app.py
```

浏览器访问：

```text
http://127.0.0.1:7860
```

---

# 📊 当前版本

## V6.1.1

已实现：

✅ 多岗位面试

✅ AI评分系统

✅ AI追问机制

✅ 回答质量检测

✅ 面试统计分析

✅ 技能雷达图

✅ PDF报告导出

✅ 中文图表支持

✅ 历史记录保存

---

# 🚀 后续规划

## V6.2

* 语音输入
* 语音面试

## V7.0

* RAG知识库面试
* 企业岗位定制题库

## V8.0

* 面试聊天记录数据库
* 用户登录系统
* 面试成绩排行榜

---

# 👨‍💻 Author

Lenlon Alice

Data Analysis & AI Application Development

Built with ❤️ using Python + Gradio + Ollama
