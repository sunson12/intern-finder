# Day 9 | 2026-06-09 | 周二 | 学习时长：3h

## 🎯 今日目标
- [ ] 从零手写 ReAct Agent 循环（不依赖 LangChain 预置 Agent）
- [ ] 深入理解 Thought → Action → Observation 的 Token 流转
- [ ] 对比手写版 vs LangChain `create_react_agent` 的差异
- [ ] 实现带记忆的 ReAct Agent（多轮对话）

---

## 📚 学习内容

### 1. 技术阅读（20min）
- 阅读内容：重读 ReAct 论文 Section 3（ReAct Prompting 设计）+ LangChain ReAct Agent 源码
- 核心收获（3句话以内）：
  - 
  - 
  - 

### 2. 手写 ReAct Agent（80min）
#### 2.1 最小 ReAct 循环（40min）
```python
# 练习文件：projects/hello-agent/day09_react_from_scratch.py
```
实现伪代码：
```
while not finished and steps < max_steps:
    thought = llm.generate_reasoning(state)    # 模型思考下一步
    if thought contains "FINISH": break
    action = parse_action(thought)              # 解析出工具名+参数
    observation = execute_tool(action)          # 执行工具
    state.add(thought, action, observation)     # 更新状态
final_answer = llm.generate_final(state)       # 基于完整轨迹生成最终回答
```
- [ ] 完成手写 ReAct 循环
- [ ] 关键细节处理：
  - 模型输出格式不稳定时的解析容错
  - 工具执行异常时的重试机制
  - 防止无限循环的终止条件
- 踩坑记录：

#### 2.2 Token 消耗分析（20min）
- [ ] 打印每一步的 System Prompt + 历史轨迹 + 当前 Thought 的总 Token 数
- [ ] 观察：随着步数增加，Token 消耗如何增长？
- [ ] 实验：第 1 步 vs 第 5 步的 Token 消耗差异
- 结论：

#### 2.3 优化策略（20min）
- [ ] 历史压缩：用 LLM 摘要前几步的 Thought-Observation 对
- [ ] 滑动窗口：只保留最近 K 步的完整内容
- [ ] 对比优化前后的 Token 消耗和回答质量

### 3. 对比 LangChain 预置 Agent（50min）
#### 3.1 使用 create_react_agent
```python
# 练习文件：projects/hello-agent/day09_langchain_react.py
from langgraph.prebuilt import create_react_agent
agent = create_react_agent(llm, tools)
```
- [ ] 用相同的 tools 跑相同的问题
- [ ] 对比输出轨迹

#### 3.2 差异分析
| 维度 | 手写版 | LangChain 版 |
|------|--------|-------------|
| 代码量 | | |
| 灵活性 | | |
| 容错性 | | |
| Prompt 控制 | | |
| 适用场景 | | |

### 4. 带记忆的 ReAct Agent（30min）
- [ ] 在多轮对话中保持 Agent 的上下文
- [ ] 实现 Conversation Summary 自动压缩
- [ ] 练习文件：`projects/hello-agent/day09_react_with_memory.py`

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- Multi-Agent 系统：通信模式 + AutoGen + CrewAI
- 实现一个 Multi-Agent 代码审查系统

## ⏱️ 实际时间分配
- 技术阅读：___min
- 手写 ReAct：___min
- 框架对比：___min
- 记忆增强：___min
