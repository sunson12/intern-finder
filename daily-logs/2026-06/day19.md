# Day 19 | 2026-06-19 | 周五 | 学习时长：3h

## 🎯 今日目标
- [ ] Portfolio 项目 2 启动（或项目 1 深度迭代：加 UI + Streaming）
- [ ] 用 Chainlit 为 Agent 搭建交互式 UI
- [ ] 实现 SSE Streaming 端到端输出
- [ ] 项目代码通过 AI Code Review

---

## 📚 学习内容

> ⚠️ 今天主要是工程产出。如果只有一个 Portfolio 项目，用它来加 UI 和 Streaming。

### 1. 决策：项目 2 还是深化项目 1？（10min）
- [ ] 如果项目 1 已经功能完整 → 用今天加 **Chainlit UI + Streaming + Docker**
- [ ] 如果项目 1 功能还不完整 → 继续开发功能
- [ ] 如果项目 1 已经很完善 → 启动项目 2（选题见 projects/README.md）
- 我的选择：___________

### 2. Chainlit UI 实战（80min）
```python
# projects/<项目名>/app.py
```
#### 2.1 Chainlit 基础（20min）
- [ ] 安装：`pip install chainlit`
- [ ] 第一个 Chainlit 应用：`chainlit run app.py`
- [ ] 理解 `@cl.on_message` / `@cl.on_chat_start` / `@cl.step`
- [ ] 理解 Chainlit 的元素：Message / Step / Element / Action

#### 2.2 将 Agent 接入 Chainlit（40min）
- [ ] 在 `@cl.on_chat_start` 中初始化 Agent
- [ ] 在 `@cl.on_message` 中调用 Agent 并流式返回
- [ ] 用 `@cl.step` 展示 Agent 的中间步骤（Thought → Action → Observation）
- [ ] 用 `cl.Message` 实现流式输出

#### 2.3 UI 美化（20min）
- [ ] 自定义 Chainlit 配置（`chainlit.md` / `config.toml`）
- [ ] 设计 Welcome Message
- [ ] 添加示例问题按钮
- [ ] 截图保存到项目 README

### 3. Streaming 输出实现（50min）
#### 3.1 LangGraph Streaming 模式
```python
# 练习文件：projects/<项目名>/src/streaming.py
```
- [ ] `graph.stream(input, stream_mode="values")` — 每个 Superstep 后输出 State
- [ ] `graph.stream(input, stream_mode="updates")` — 只输出变化
- [ ] `graph.astream_events()` — 最细粒度的 Token 级 Streaming
- 笔记：

#### 3.2 SSE 端到端实现
- [ ] FastAPI + SSE（Server-Sent Events）
- [ ] Chainlit 自动处理 Streaming（LangChain callback → Chainlit Step）
- [ ] 验证：用户可以看到 Agent 逐 Token 输出 + 中间推理过程

### 4. AI Code Review（40min）
- [ ] 将项目核心代码（graph.py / tools.py）交给 Claude 做 Code Review
  - Prompt："Review this AI Agent code for bugs, performance issues, and security concerns."
- [ ] 根据 Review 意见修改代码
- [ ] 记录 3 个 Review 发现的问题：
  1. 
  2. 
  3. 

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- 项目收尾：测试 + 文档完善
- Docker 容器化
- 论文精读（3 篇 Agent 核心论文）

## ⏱️ 实际时间分配
- 决策：___min
- Chainlit UI：___min
- Streaming：___min
- Code Review：___min
