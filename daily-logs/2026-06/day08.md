# Day 8 | 2026-06-08 | 周一 | 学习时长：3h

## 🎯 今日目标
- [ ] 理解 LangGraph 的核心设计思想（Graph / State / Node / Edge）
- [ ] 手写第一个 StateGraph：顺序执行 → 条件分支 → 循环
- [ ] 理解 Checkpointing 机制与状态持久化
- [ ] 对比 LangGraph 和传统 Chain 的适用场景

---

## 📚 学习内容

### 1. 技术阅读（20min）
- 阅读内容：[LangGraph 官方 Quick Start](https://langchain-ai.github.io/langgraph/tutorials/introduction/)
- 核心收获（3句话以内）：
  - 
  - 
  - 

### 2. LangGraph 核心概念（60min）
#### 2.1 第一个 StateGraph
```python
# 练习文件：projects/hello-agent/day08_first_graph.py
```
- [ ] 定义 State（TypedDict / Pydantic）
- [ ] 创建 Node（处理函数）
- [ ] 连接 Edge（普通边 + 条件边）
- [ ] compile() 并 invoke()
- 踩坑记录：

#### 2.2 三种控制流模式
- [ ] **顺序执行**：A → B → C
- [ ] **条件分支**：根据 State 字段 → 路由到不同 Node
- [ ] **循环**：条件边指回上游 Node（需设置 recursion_limit）
- [ ] 练习文件：`projects/hello-agent/day08_control_flow.py`

#### 2.3 State 的 Reducer 机制
- [ ] 默认覆盖 vs append（用 `Annotated[list, operator.add]`）
- [ ] 自定义 Reducer 函数
- [ ] 练习文件：`projects/hello-agent/day08_state_reducer.py`

### 3. Checkpointing 与持久化（50min）
#### 3.1 Checkpointing 基础
- [ ] 理解每个 Superstep 自动保存 State
- [ ] `MemorySaver`：内存级保存（开发/测试用）
- [ ] `SqliteSaver`：持久化保存（生产用）
- [ ] 练习文件：`projects/hello-agent/day08_checkpoint.py`

#### 3.2 Human-in-the-Loop
- [ ] `interrupt_before`：在指定 Node 前暂停
- [ ] `interrupt_after`：在指定 Node 后暂停
- [ ] `Command(resume=...)`：人工审批后继续
- [ ] 练习：实现一个"代码生成→人工审批→自动提交"的工作流
- 踩坑记录：

### 4. LangGraph vs Chain 对比（50min）
#### 实战：用 LangGraph 重构 Day 5 的 RAG Pipeline
```python
# 练习文件：projects/hello-agent/day08_rag_graph.py
```
Graph 设计：
```
Retrieve → Grade Documents → [相关] → Generate
                           → [不相关] → Rewrite Query → Retrieve
```
- [ ] 完成重构
- [ ] 对比 LangGraph 版 vs Chain 版：代码量 / 灵活性 / 可调试性
- 对比结论：

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- ReAct Agent 从零实现（不依赖 LangChain 预置 Agent）
- 对比手写版 vs LangChain create_react_agent
- 理解 Agent 循环中的 Token 消耗与优化

## ⏱️ 实际时间分配
- 技术阅读：___min
- 核心概念：___min
- Checkpointing：___min
- 对比重构：___min
