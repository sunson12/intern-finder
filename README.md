# 🎯 Intern Finder — AI Agent 实习冲刺

> **目标**：2026年6月30日前拿到 AI Agent 开发相关暑期/日常实习 Offer  
> **身份**：浙江工业大学 CS 博士研究生  
> **节奏**：每天 3 小时，约 29 天冲刺  

---

## 📂 项目结构

```
intern-finder/
├── README.md                    # 本文件 — 总览
├── ROADMAP.md                   # 🗺️ 核心学习路线（先看这个！）
├── resume/
│   ├── resume-guide.md          # 简历优化指南 + 关键词清单
│   ├── resume-cn.md             # 中文简历（待填充）
│   └── resume-en.md             # 英文简历（待填充）
├── internship-positions/
│   └── tracking.md              # 实习投递追踪表
├── daily-logs/
│   ├── template.md              # 每日日志模板
│   └── 2026-06/                 # 按月份归档
│       ├── day01.md
│       └── ...
├── projects/                    # Portfolio 项目代码
│   └── README.md                # 项目选题与规划
├── resources/                   # 学习资源汇总
│   ├── papers.md                # 论文阅读清单
│   ├── tools.md                 # 常用工具与配置
│   └── interview-qa.md          # 面试常见问答
└── memory/                      # Claude Code 记忆（自动生成）
```

---

## 🚀 快速开始

### 1. 阅读核心路线
→ [ROADMAP.md](./ROADMAP.md) — 四周冲刺计划、知识点清单、目标公司

### 2. 搭建开发环境
```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装核心依赖
pip install langchain langgraph langchain-openai langchain-anthropic
pip install chromadb llama-index fastapi uvicorn
pip install chainlit gradio  # UI 框架
pip install autogen-agentchat crewai  # Multi-Agent 框架
```

### 3. 开始打卡
```bash
# 复制每日日志模板
cp daily-logs/template.md daily-logs/2026-06/day01.md
```

### 4. 更新投递进度
→ [internship-positions/tracking.md](./internship-positions/tracking.md)

---

## 📊 进度概览

| 阶段 | 时间 | 核心目标 | 状态 |
|------|------|---------|------|
| 第一周 | 6/1 - 6/7 | 基础夯实 + 简历武装 | 🔵 进行中 |
| 第二周 | 6/8 - 6/14 | Agent 核心能力 | ⚪ 待开始 |
| 第三周 | 6/15 - 6/21 | 项目实战 + 深度进阶 | ⚪ 待开始 |
| 第四周 | 6/22 - 6/30 | 面试冲刺 + 海投收割 | ⚪ 待开始 |

| 指标 | 当前 | 目标 |
|------|------|------|
| 投递数 | 0 | 30+ |
| Portfolio 项目 | 0 | 2 |
| 面试 | 0 | 5+ |
| Offer | 0 | 1+ |

---

## 🔗 快捷链接

- [简历优化指南](./resume/resume-guide.md)
- [投递追踪表](./internship-positions/tracking.md)
- [每日日志模板](./daily-logs/template.md)
- [论文阅读清单](./resources/papers.md)
- [面试常见问答](./resources/interview-qa.md)
- [项目选题规划](./projects/README.md)

---

## 💪 一句话共勉

> "The best way to get an AI Agent internship is to build AI Agents."  
> 最好的学习方法就是动手构建。Keep building, keep shipping. 🚀
