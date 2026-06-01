# 🤖 AI Agent 面试常见问答

> 持续更新中——每场面试后补充新题。

---

## 一、Agent 基础

### Q1：什么是 AI Agent？它和传统的 LLM Chatbot 有什么区别？

**答题要点**：
- Agent = LLM + 规划(Planning) + 工具使用(Tool Use) + 记忆(Memory) + 行动(Action)
- Chatbot 是单轮/多轮对话，Agent 是自主完成任务的实体
- Agent 的核心循环：感知→思考→行动→观察→调整
- 举例：Chatbot 回答"今天天气怎么样"，Agent 调用天气 API → 拿到数据 → 判断是否需要提醒用户带伞 → 主动建议

### Q2：ReAct 模式的原理是什么？为什么它有效？

**答题要点**：
- Thought → Action → Observation 循环
- Thought：分析当前状态，决定下一步
- Action：调用工具或执行操作
- Observation：获取反馈
- 有效的原因：将推理和行动交织在一起，减少幻觉（因为每个步骤都有外部反馈来校准）
- 可以提 Yao et al. 2022 的论文

### Q3：Function Calling 和 Tool Use 的实现原理？

**答题要点**：
- 模型层面：通过在训练数据中加入工具调用的格式，模型学会输出特定的 JSON/tool_call 格式
- API 层面：开发者定义 JSON Schema，模型返回 function_call 而不是 text
- 框架层面：LangChain 等框架封装了 tool_call → 执行 → 结果注入 → 继续生成 的循环
- 关键技术点：tool description 质量、schema 设计、错误处理与重试

---

## 二、Agent 架构

### Q4：LangGraph 的核心设计思想是什么？

**答题要点**：
- 图（Graph）作为 Agent 流程的抽象：Node（处理节点）+ Edge（流转）+ State（状态）
- 与传统 Chain 的区别：Chain 是线性的，Graph 支持条件分支、循环、并行
- Checkpointing 机制：每个 Node 执行后自动保存状态，支持断点续传和时间旅行
- Human-in-the-Loop：在关键节点中断，等待人工审批后继续
- 实际使用场景：复杂的多步 Agent 工作流，如代码审查 Agent（拉代码→分析→生成建议→人工审批→提交PR）

### Q5：如何设计一个 Multi-Agent 系统？

**答题要点**：
- 通信拓扑：顺序(Sequential)、层级(Hierarchical)、对等(Peer-to-Peer)、辩论(Debate)
- 角色分配：每个 Agent 有明确的 System Prompt 和工具集
- 信息共享：共享记忆/黑板模式 vs 消息传递
- 冲突解决：投票、仲裁Agent、人工介入
- 实际案例：代码审查中，一个 Agent 负责安全检查，一个负责性能分析，一个负责风格审查，最后由汇总 Agent 整合

### Q6：MCP 协议是什么？解决了什么问题？

**答题要点**：
- Model Context Protocol，Anthropic 提出的标准化协议
- 解决的问题：每个 LLM 应用都要重复实现工具连接逻辑（OAuth、数据格式转换等）
- 三种原语：Tool（模型调用外部功能）、Resource（模型读取外部数据）、Prompt（预置提示词模板）
- Client-Server 架构：MCP Client（AI 应用） ↔ MCP Server（工具/数据提供方）
- 意义：类似 USB 协议之于外设，MCP 让 Agent 和工具的连接标准化
- 与 Function Calling 的关系：MCP 是 Function Calling 的上层协议，定义了工具从发现到调用的完整生命周期

---

## 三、RAG

### Q7：RAG 的核心流程和常见优化策略？

**答题要点**：
- 流程：文档加载→分块(Chunking)→向量化(Embedding)→索引存储→检索(Retrieval)→重排序(Rerank)→生成(Generation)
- 分块策略：固定大小 vs 语义分块 vs 递归分块；chunk size 和 overlap 的 trade-off
- 检索优化：Hybrid Search（BM25 + 稠密向量）、MMR（最大边际相关性）、Multi-Query Retrieval
- 生成优化：上下文压缩、引用标注、Self-RAG
- 评估：MRR、NDCG、Hit Rate、Faithfulness

### Q8：什么时候用 RAG，什么时候用 Fine-tuning？

**答题要点**：
- RAG：需要实时/私有知识、数据更新频繁、需要可解释性（引用来源）
- Fine-tuning：需要模型学习特定风格/格式/推理模式、知识相对稳定
- 两者不是互斥的，可以结合（Fine-tuned 模型 + RAG 检索）
- 成本考量：RAG 检索成本低但推理 Token 多，Fine-tuning 训练一次性成本高

---

## 四、LLM 基础

### Q9：Transformer 的 Self-Attention 计算过程？

**标准八股文，必须能流畅推导**：
- Q、K、V 的来源（输入 X 分别乘以 W_Q, W_K, W_V）
- Attention Score = softmax(QK^T / √d_k)
- 为什么要除以 √d_k（防止点积过大导致 softmax 梯度消失）
- Multi-Head Attention：多个头并行，最后拼接
- 时间复杂度 O(n²d)，空间复杂度 O(n²)
- 优化：FlashAttention（分块计算、IO-aware）、MQA/GQA（KV 共享）

### Q10：RLHF 和 DPO 的区别？

**答题要点**：
- RLHF：SFT → 训练 Reward Model → PPO 优化。需要 3 个模型（Policy + Reference + Reward），训练不稳定
- DPO：直接在偏好数据上用 Pairwise Loss 优化，不需要显式的 Reward Model。数学上等价于 RLHF 在 Bradley-Terry 模型下的最优解
- DPO 的优点：简单、稳定、计算量小
- DPO 的局限：不能处理 online exploration（无法在线收集新数据）

---

## 五、系统设计

### Q11：设计一个类似 Coze/Dify 的 AI Agent 构建平台

**答题框架**：
1. **需求澄清**：目标用户（开发者/非开发者）、核心功能（Agent 编排/知识库/工作流/插件市场）
2. **核心架构**：
   - 前端：React 拖拽式工作流编辑器
   - 后端：Python/Go 微服务
   - Agent 引擎：LangGraph 或自研图执行引擎
   - 模型层：统一模型网关（路由/限流/降级）
3. **关键模块**：
   - 工作流引擎（DAG 编排、条件分支、循环、并行）
   - 插件/Tool 系统（类似 MCP，标准化接入）
   - 知识库（多源数据接入、向量化、检索）
   - 记忆系统（短期+长期，用户级别隔离）
   - 评估与监控（Token 消耗、延迟、成功率）
4. **技术难点**：
   - 流式输出的端到端实现
   - 多人并发下的 Agent 状态隔离
   - 模型调用失败的重试与降级
   - MCP 等协议的安全性（沙箱执行）

### Q12：设计一个支持 10 万 DAU 的 RAG 问答系统

**答题框架**：
1. **容量估算**：QPS、数据量、延迟要求
2. **架构设计**：
   - 接入层：CDN + API Gateway + 限流
   - 检索层：Milvus 集群（读写分离、索引优化）
   - 生成层：模型服务（vLLM/TGI 部署、Prompt Caching）
   - 缓存层：Redis（Query→Answer 缓存、Embedding 缓存）
3. **优化策略**：
   - 热门 Query 缓存（命中率 30-50%）
   - 语义路由（简单问题用小模型、复杂问题用大模型）
   - 批量推理提高 GPU 利用率
   - 异步预加载（预测用户下一个问题）

---

## 六、行为面试

### Q13：你为什么选择 AI Agent 方向？

**建议话术**：
- 从研究兴趣出发（如果博士方向相关）
- 从技术趋势出发（LLM 从工具变成自主实体，Agent 是下一波浪潮）
- 从实践经历出发（做了什么 Agent 项目、得到什么洞察）
- 真诚比完美重要

### Q14：你未来 3-5 年的职业规划？

**建议话术**：
- 短期（实习+毕业前）：在工业界深入 Agent 工程实践
- 中期（毕业后 1-3 年）：成为 Agent 方向的 Tech Lead
- 长期：在 Agent 基础设施或 Agent 产品方向深耕
- 体现"想留在这个领域"的意愿（公司花钱培养你，不希望你去刷个经历就跑）

---

## 💡 面试中的反问（向面试官提问）

- "团队目前在 Agent 方向的探索中，遇到的最大技术挑战是什么？"
- "您认为一个好的 Agent 平台/框架，最关键的三个技术决策是什么？"
- "团队内部如何评估一个 Agent 的质量？有哪些指标？"
- "如果有机会加入，我可能会负责哪类工作？"
