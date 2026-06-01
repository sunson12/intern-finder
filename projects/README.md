# 🛠️ Portfolio 项目规划

> **原则**：宁精勿多。2 个高质量项目 > 5 个 Demo。

---

## 项目选题池

### 项目 1：智能科研助手 Agent

**核心功能**：
- 用户输入研究方向/问题 → Agent 自动搜索 Arxiv 论文
- 多轮对话式论文筛选（"这个方向最近有什么新进展？"）
- 自动生成论文对比分析报告
- 支持论文全文问答（RAG）

**技术栈**：LangGraph + ChromaDB + FastAPI + Chainlit

**差异化亮点**：
- 体现博士研究背景
- Multi-Agent 协作（检索Agent + 分析Agent + 写作Agent）
- MCP 协议接入（将 Arxiv API 封装为 MCP Tool）

**面试能展示的点**：
- ReAct 循环实现
- RAG 全流程优化
- Agent 状态管理
- 异步并发处理

---

### 项目 2：代码审查 Agent

**核心功能**：
- GitHub Webhook 触发，自动审查 PR
- 多维度分析：安全检查、性能分析、代码风格
- 将审查意见自动发布为 PR Comment
- 支持人工确认后自动修复

**技术栈**：LangGraph + MCP + GitHub API + AST 解析

**差异化亮点**：
- Multi-Agent 分工（安全Agent + 性能Agent + 风格Agent）
- Human-in-the-Loop（关键修复需人工确认）
- 使用 AST 而不是简单的正则匹配

---

### 项目 3：个人知识管理 Agent

**核心功能**：
- 自动从网页/论文/笔记中提取知识
- 构建个人知识图谱
- 基于知识图谱的智能问答
- 研究灵感推荐

**技术栈**：LangGraph + Neo4j + LlamaIndex + Embedding

**差异化亮点**：
- 知识图谱 + 向量检索的 Hybrid 方案
- 图数据库的使用体现工程能力
- 长期记忆管理

---

## 我选择的项目（2 选 1 或都做）

### 项目 A：_____________
- **启动日期**：
- **MVP 日期**：
- **迭代完成日期**：

### 项目 B：_____________
- **启动日期**：
- **MVP 日期**：
- **迭代完成日期**：

---

## 每个项目必须包含

- [ ] README.md（项目介绍、架构图、快速开始、技术栈、Demo 截图/GIF）
- [ ] `requirements.txt` 或 `pyproject.toml`
- [ ] 可运行的最小 Demo
- [ ] 单元测试（至少核心逻辑）
- [ ] Dockerfile（加分项）
- [ ] 技术博客一篇（选做但强烈推荐）

---

## 项目开发节奏

```
Day 1: 项目初始化 + 核心流程跑通（硬编码的 Happy Path）
Day 2: 完善工具集成 + 错误处理
Day 3: UI 包装 + Demo 录制 + README 完善
Day 4: 测试 + 迭代 + 博客
```
