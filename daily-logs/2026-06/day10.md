# Day 10 | 2026-06-10 | 周三 | 学习时长：3h

## 🎯 今日目标
- [ ] 理解 Multi-Agent 系统的核心通信模式
- [ ] AutoGen 入门：实现一个双 Agent 对话
- [ ] CrewAI 入门：定义角色/任务/工具
- [ ] 完成一个小型 Multi-Agent 代码审查 Demo

---

## 📚 学习内容

### 1. 技术阅读（20min）
- 阅读内容：AutoGen 官方 Quickstart + CrewAI 官方 Quickstart
- 核心收获（3句话以内）：
  - 
  - 
  - 

### 2. Multi-Agent 通信模式（40min）
#### 2.1 四种核心拓扑
- [ ] **顺序（Sequential）**：A → B → C，链式传递
- [ ] **层级（Hierarchical）**：Manager Agent 分派任务给 Worker Agents
- [ ] **对等（Peer-to-Peer）**：Agent 之间自由对话
- [ ] **辩论（Debate）**：多个 Agent 讨论后投票/收敛
- 练习文件：`projects/hello-agent/day10_topology.py`
  （用 LangGraph 实现这 4 种拓扑的框架代码）
- [ ] 完成 4 种拓扑的代码框架

#### 2.2 Multi-Agent 的核心挑战
- [ ] 信息共享：共享记忆 vs 消息传递
- [ ] 冲突解决：投票 / 仲裁Agent / 人工介入
- [ ] 上下文膨胀：N 个 Agent 对话 = O(N²) Token 增长
- 笔记：

### 3. AutoGen 实战（50min）
#### 3.1 双 Agent 对话
```python
# 练习文件：projects/hello-agent/day10_autogen_dual.py
```
- [ ] 创建 UserProxyAgent + AssistantAgent
- [ ] 实现一个"论文审稿"场景：UserProxy 提供论文，AssistantAgent 逐段给出审稿意见
- [ ] 理解 AutoGen 的 `max_consecutive_auto_reply` 和 `termination_msg`

#### 3.2 GroupChat 模式
```python
# 练习文件：projects/hello-agent/day10_autogen_groupchat.py
```
- [ ] 创建 3 个 Agent：安全审查员 / 性能分析师 / 代码风格审查员
- [ ] 用 GroupChat + GroupChatManager 管理多 Agent 讨论
- [ ] 观察对话流向和最终输出质量

### 4. CrewAI 实战（40min）
```python
# 练习文件：projects/hello-agent/day10_crewai_demo.py
```
#### 4.1 角色定义
- [ ] Agent：定义 role / goal / backstory / tools / allow_delegation
- [ ] Task：定义 description / expected_output / agent
- [ ] Crew：aggregate agents + tasks，设置 process（sequential / hierarchical）

#### 4.2 完整 Demo
- [ ] 场景：代码 PR 审查
  - Agent 1（安全审查员）：检查 SQL 注入、XSS、敏感信息泄露
  - Agent 2（性能分析师）：检查 N+1 查询、不合理的循环、内存泄漏
  - Agent 3（风格审查员）：检查命名规范、代码重复、注释缺失
  - Agent 4（汇总员）：整合各方意见，生成审查报告

### 5. Multi-Agent 框架对比（30min）
| 维度 | AutoGen | CrewAI | LangGraph（手写） |
|------|---------|--------|-------------------|
| 通信模式 | 对话式 | 任务式 | 图式（最灵活） |
| 学习曲线 | | | |
| 灵活性 | | | |
| 生产就绪度 | | | |
| 选型建议 | | | |

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- MCP 协议深度实战：Server / Client 实现
- 将 Arxiv API 封装为 MCP Tool
- MCP 与 LangChain 集成

## ⏱️ 实际时间分配
- 技术阅读：___min
- 通信模式：___min
- AutoGen：___min
- CrewAI：___min
- 框架对比：___min
