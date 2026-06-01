# 📄 AI Agent 实习简历优化指南

> **核心原则**：简历不是你的自传，是你"能干活"的证据集合。  
> 面试官看一份简历的时间约为 6-15 秒，必须第一眼就抓住关键词。

---

## 🎯 一、简历结构（一页纸原则）

```
1. 个人信息（2行）
2. 教育背景（3-4行）
3. 技术技能（按类别排列，6-8行）
4. 项目经历（2-3个核心项目，每个5-8行）← 最重要的部分
5. 科研/论文（选最相关的1-2篇）
6. 竞赛/获奖（如有）
```

---

## 🔑 二、AI Agent 岗位关键词清单

### 必须在简历中出现的关键词（根据真实经历自然融入）

**基础层**
- Python (async/await, asyncio)
- LangChain, LangGraph, LlamaIndex
- OpenAI API, Claude API, 通义千问 API
- Prompt Engineering, Few-shot, CoT, ReAct

**Agent 核心**
- Function Calling / Tool Use
- Multi-Agent Systems
- RAG (Retrieval-Augmented Generation)
- Agentic Workflow, Planning, Reasoning
- MCP (Model Context Protocol)
- Memory Management (短期/长期/语义记忆)

**工程化**
- FastAPI / Flask
- Docker, Git, CI/CD
- Streaming (SSE/WebSocket)
- Vector Database (ChromaDB/Milvus/Qdrant)
- Embedding Models (BGE/GTE/OpenAI)

**评估与优化**
- Agent Evaluation (LangSmith/Braintrust)
- Prompt Caching, Token Optimization
- Model Routing / Fallback

---

## ✍️ 三、项目经历的 STAR-L 写法

> STAR-L = Situation + Task + Action + Result + Learning

### ❌ 错误示范（流水账）
> "使用 LangChain 开发了一个聊天机器人，可以回答用户问题。"

### ✅ 正确示范（量化 + 技术细节 + 结果）
> **智能科研助手 Agent** | LangGraph, ChromaDB, FastAPI | 2026.05
> - 设计并实现了一个基于 ReAct 范式的科研文献检索 Agent，支持 Arxiv 论文自动检索、精炼与对比分析
> - 使用 LangGraph 构建多节点 Agent 工作流（Search → Filter → Summarize → Compare），支持人机协同的中断-审批-继续机制
> - 基于 BGE-M3 Embedding + ChromaDB 实现语义检索，在 10 万论文数据集中达到 Top-5 召回率 91%
> - 封装为 FastAPI 服务并部署，支持 SSE 流式输出，单次查询平均响应时间从 12s 优化到 3.5s

### 每个项目应该包含的元素
- [ ] 用了什么技术栈（具体到框架/模型/数据库）
- [ ] 解决了什么问题（场景）
- [ ] 你做了什么（你的角色和贡献，用动词开头）
- [ ] 结果如何（量化指标：QPS/延迟/准确率/用户数/Star 数）
- [ ] 遇到了什么技术挑战，如何解决的（面试时展开讲）

---

## 🎓 四、博士经历的包装策略

### 研究方向与 Agent 的关联

| 如果你的研究方向是... | 可以这样关联到 Agent |
|----------------------|---------------------|
| NLP/对话系统 | Agent 的语言理解与生成基础 |
| 强化学习 | RLHF/DPO 对齐、Agent 决策优化 |
| 知识图谱 | Agent 的知识检索与推理 |
| 推荐系统 | Agent 的信息过滤与个性化 |
| 计算机视觉 | 多模态 Agent 的视觉理解 |
| 分布式系统 | Multi-Agent 协调与通信 |
| 软件工程 | SWE-Agent、代码生成 Agent |
| 任何方向 | 你使用 Agent 辅助研究的经验！ |

### 即使研究方向不直接相关
简历中一定要有一段体现你的 Agent 实践经历。哪怕不是正式发表的工作，以下也算：
- GitHub 开源项目
- 技术博客/教程
- 课程大作业（如果方向是 Agent）
- Hackathon 项目
- 给开源项目提的 PR

---

## 🔧 五、简历自检清单

### 格式
- [ ] 一页纸以内（博士经历多也不要超过一页半）
- [ ] PDF 格式（不要发 Word）
- [ ] 文件名：`姓名-学校-岗位-电话.pdf`
- [ ] 中文版 + 英文版各一份
- [ ] 没有错别字、语法错误

### 内容
- [ ] 每个项目都有技术栈标注
- [ ] 每个项目都有可量化结果
- [ ] AI Agent 相关关键词覆盖 70%+ 上述清单
- [ ] 没有"精通"这种容易被挑战的词，用"熟练使用/深入理解/有实践经验"
- [ ] GitHub 链接可访问、项目有 README

### 适配
- [ ] 针对不同公司/岗位有微调版本（如大厂强调工程能力，创业公司强调独立交付能力）
- [ ] 投字节版简历突出工程+产品思维，投蚂蚁版突出可靠性+安全

---

## 📝 六、简历对应面试问题的准备

简历上每一句话，面试官都可能追问。准备时自问：

1. **"这个项目你遇到的最大技术挑战是什么？"**
2. **"为什么选这个技术方案而不是另一个？"**
3. **"这个项目如果重新做一次，你会怎么改进？"**
4. **"你在这个项目中具体写了多少代码？哪些模块是你负责的？"**
5. **"这个量化指标是怎么测出来的？实验设置是怎样的？"**

每个项目准备 3 分钟的"电梯演讲"版介绍，包含：背景 → 挑战 → 方案 → 结果 → 反思。

---

## 🚫 七、常见硬伤

| 硬伤 | 为什么是硬伤 | 怎么改 |
|------|-------------|--------|
| "精通 Python" | 面试官会追问到你不精通为止 | "熟练使用 Python，掌握 async/await 异步编程" |
| 项目只写"参与了" | 不知道你干了什么 | 用具体动词："设计/实现/优化/主导" |
| 堆砌技术名词不解释 | 像是复制粘贴 JD | 每个技术名词必须在项目中有体现 |
| 没有 GitHub 链接 | AI 岗必须看代码 | 贴链接，且保证项目 README 完整 |
| 项目时间线有空洞 | 看起来像什么都没做 | 博士期间的项目按研究方向组织，不以时间组织 |
| 个人信息冗余 | 性别/年龄/民族/政治面貌与能力无关 | 保留：姓名/电话/邮箱/GitHub/城市 |
