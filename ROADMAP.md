# 🎯 AI Agent 实习冲刺学习路线

> **目标**：2026年6月30日前拿到 AI Agent 开发相关暑期/日常实习 Offer  
> **起点**：浙江工业大学 CS 博士研究生  
> **时间预算**：每天 3 小时 × 约29天 = 约87小时  
> **当前日期**：2026年6月1日  

---

## 📋 一、你的优势与短板

### ✅ 博士生的核心优势
- **研究能力**：能读论文、复现实验、做创新——这在 AI Agent 方向是巨大优势（领域变化快，论文驱动）
- **理论基础**：ML/DL 基础扎实，理解 Transformer、RL、搜索算法等
- **学历门槛**：大厂 AI 岗位对博士有天然偏好，简历通过率高

### ❌ 需要补的短板
- **工程化能力**：学术代码 ≠ 生产代码。需要学 async、错误处理、日志、测试
- **框架熟悉度**：LangChain/LangGraph/AutoGen 等工业界常用框架
- **面试技巧**：国内大厂面试有固定套路（八股文 + 算法 + 系统设计 + 项目深挖）
- **实习信息差**：很多实习岗位在内部渠道/实验室推荐中消化，需要主动 networking

---

## 📅 二、四周冲刺时间表

### 🔥 第一周：基础夯实 + 简历武装（6/1 - 6/7）

| 天 | 主题 | 具体任务 | 产出 |
|----|------|---------|------|
| 1 | 环境搭建 | 配置 Python 3.11+ 虚拟环境、安装 LangChain/LangGraph/LlamaIndex、注册 OpenAI/Claude/通义千问 API、配置 VS Code/Cursor | 可运行的开发环境 |
| 2 | LLM 基础 | Prompt Engineering（Few-shot/CoT/ReAct/结构化输出）、Token 与 Context Window 机制、Temperature/Top-P 参数调优 | 20+条高质量 Prompt 示例 |
| 3 | Function Calling | OpenAI/Claude Function Calling 实战、JSON Schema 定义、错误处理与重试、Streaming 输出 | 一个完整的 Tool Calling Demo |
| 4 | LangChain 核心 | Chain/LCEL/Runnable 接口、Prompt Template、Output Parser、Memory（ConversationBuffer/Summary） | LangChain 笔记 + Demo |
| 5 | RAG 基础 | 文档加载→分块→Embedding→向量检索→生成、ChromaDB/Qdrant/Faiss 选型对比、检索优化（MMR/相似度阈值） | 一个可运行的 RAG 系统 |
| 6 | 简历优化 | 用 AI Agent 视角重写项目经历、量化成果、提炼技术关键词、英文简历初稿 | 中英文简历 v1 |
| 7 | 复盘 & 投递准备 | 整理一周学习产出到 GitHub、筛选目标公司/部门、开始制作投递追踪表 | GitHub README + 投递清单 |

**本周目标**：能独立用 LangChain 写一个带 Tool Calling 的 Agent，简历投递版就绪。

---

### 🚀 第二周：Agent 核心能力（6/8 - 6/14）

| 天 | 主题 | 具体任务 | 产出 |
|----|------|---------|------|
| 8 | LangGraph 入门 | StateGraph/Node/Edge/条件路由、Checkpointing 与状态持久化、Human-in-the-Loop 模式 | LangGraph 笔记 |
| 9 | ReAct Agent | 从零实现 ReAct 循环（Thought→Action→Observation→...）、对比 LangChain 预置 Agent | 手写 ReAct Agent |
| 10 | Multi-Agent 系统 | Agent 通信模式（顺序/并行/辩论）、AutoGen 入门、CrewAI 角色定义 | Multi-Agent Demo |
| 11 | MCP 协议 | Anthropic MCP 协议原理、Server/Client 实现、Tool/Resource/Prompt 三种原语、与 LangChain 集成 | MCP Server+Client 代码 |
| 12 | 向量数据库进阶 | Embedding 模型选型（BGE/GTE/OpenAI）、索引优化（IVF/HNSW）、Hybrid Search（稀疏+稠密） | 检索性能对比报告 |
| 13 | Agent 记忆系统 | 短期记忆（窗口/摘要）、长期记忆（向量持久化）、语义记忆与情节记忆、Mem0/MemGPT 调研 | 带记忆的 Agent Demo |
| 14 | 复盘 & 项目启动 | 确定 1-2 个 Portfolio 项目选题、搭框架、写项目 Proposal | 项目设计文档 |

**本周目标**：深入理解 Agent 架构模式，完成 MCP 协议实践，启动 Portfolio 项目。

---

### 🎓 第三周：项目实战 + 深度进阶（6/15 - 6/21）

| 天 | 主题 | 具体任务 | 产出 |
|----|------|---------|------|
| 15-16 | Portfolio 项目 1 | 选一个方向深挖（见下文项目选题），完整实现 MVP | 可 Demo 的项目 v1 |
| 17 | Agent 评估 | 评估指标体系（任务完成率/工具选择准确率/幻觉率）、LangSmith/Braintrust 使用、自动化评测 Pipeline | 评估框架代码 |
| 18 | Agent 性能优化 | Token 消耗优化、Prompt Caching 策略、并发与批处理、模型蒸馏与路由（大模型→小模型 fallback） | 优化笔记 |
| 19-20 | Portfolio 项目 2 | 第二个项目或项目1的深度迭代，加上 UI（Gradio/Chainlit） | 可 Demo 项目 v2 |
| 21 | 论文 & 前沿 | 精读 3-5 篇 Agent 核心论文（ReAct/ AutoGPT/ MetaGPT/ SWE-Agent/ Generative Agents）、写博客/笔记 | 论文笔记 + 技术博客 |

**本周目标**：完成2个高质量 Portfolio 项目，建立技术博客/笔记产出。

#### Portfolio 项目选题建议（选 1-2 个）

1. **智能客服 Agent**（实用、面试高频）
   - RAG + Multi-Agent + Human-in-the-Loop
   - 技术栈：LangGraph + ChromaDB + FastAPI + Chainlit
   
2. **代码助手 Agent**（体现博士工程能力）
   - 代码搜索 + 代码生成 + 代码审查 + 自动修复
   - 技术栈：LangGraph + MCP + AST 解析 + Git 操作

3. **数据分析 Agent**（贴合研究背景）
   - 自然语言→SQL/Python→可视化→洞察报告
   - 技术栈：LangChain + Pandas + Matplotlib + Text-to-SQL

4. **个人知识管理 Agent**（差异化竞争）
   - 论文检索→自动摘要→知识图谱→研究灵感推荐
   - 技术栈：LangGraph + Neo4j + Arxiv API + Embedding

---

### 🎯 第四周：面试冲刺 + 海投收割（6/22 - 6/30）

| 天 | 主题 | 具体任务 | 产出 |
|----|------|---------|------|
| 22 | 算法复习 | LeetCode Hot 100 精选 30 题（重点：字符串/树/DP/图）、Python 常见面试题 | AC 记录 |
| 23 | AI 八股文 | Transformer 架构细节、Attention 计算复杂度、RLHF/DPO 原理、Agent 相关概念（ planning/reasoning/tool-use/memory） | 八股文笔记 |
| 24 | 系统设计 | 设计一个 AI Agent 平台（类似 Coze/Dify）、设计一个 RAG 系统、设计一个 Multi-Agent 编排系统 | 系统设计文档 |
| 25 | 行为面试 | "自我介绍"打磨、"项目难点"STAR 法则、"为什么做 Agent"故事线、反向提问清单 | 面试话术稿 |
| 26 | 模拟面试 | 找同学/学长模拟 1-2 场技术面、AI 模拟面试工具练习、录音复盘 | 面试反馈记录 |
| 27-29 | 集中投递 + 面试 | 每天投递 5-10 家、跟进已有投递、根据面试反馈快速迭代、记录面经 | 面经 + 投递状态 |
| 30 | 复盘 & 调整 | 复盘所有面试反馈、调整策略、制定后续计划 | 复盘文档 |

**本周目标**：面试能力全面提升，至少完成 30+ 投递，拿到面试机会。

---

## 📚 三、核心知识点清单

### 必须精通（面试必问）

| 知识点 | 掌握程度 | 学习资源 |
|--------|---------|---------|
| Python async/await | 能手写异步 Agent 循环 | Python 官方文档 + 实战 |
| LangChain Core (LCEL/Runnable) | 能解释设计原理 | LangChain 官方文档 |
| LangGraph (StateGraph/Checkpoint) | 能设计复杂 Agent 流程 | LangGraph 官方 Tutorial |
| Function Calling (OpenAI/Claude) | 能手写 Tool Schema 和调用循环 | 各平台 API 文档 |
| RAG 全流程 | 能独立搭建并优化检索 Pipeline | LlamaIndex 文档 |
| Prompt Engineering | 能设计 System Prompt 和 Few-shot | Anthropic Prompt Library |
| MCP 协议 | 能实现 MCP Server 和 Client | Anthropic MCP 官方文档 |
| 向量数据库 (ChromaDB/Milvus) | 能选型并优化检索性能 | 各数据库文档 |

### 应该掌握（加分项）

| 知识点 | 掌握程度 | 学习资源 |
|--------|---------|---------|
| AutoGen / CrewAI | 了解 Multi-Agent 框架差异 | 官方 Quickstart |
| LangSmith / Braintrust | 能用于 Agent 调试和评估 | 官方文档 |
| FastAPI / Flask | 能将 Agent 封装为 API | FastAPI 官方 Tutorial |
| Docker | 能容器化 Agent 应用 | Docker 官方 Get Started |
| Chainlit / Gradio | 能为 Agent 搭建 UI Demo | 官方 Quickstart |
| Prompt Caching | 理解 Anthropic/OpenAI 的缓存机制 | 平台 Pricing 页 |
| Streaming | 能实现 SSE/WebSocket 流式输出 | FastAPI SSE 文档 |
| LlamaIndex | 了解与 LangChain 的差异和适用场景 | 官方文档 |

### 了解即可（锦上添花）

| 知识点 | 学习资源 |
|--------|---------|
| Fine-tuning (LoRA/QLoRA) | HuggingFace PEFT 文档 |
| RLHF / DPO | 论文 + Lil'Log 博客 |
| AI Agent 安全 (Prompt Injection) | OWASP LLM Top 10 |
| MLOps / LLMOps | LangSmith / MLflow 文档 |
| WebAssembly / Sandboxed Execution | E2B / Fly.io 文档 |
| 多模态 Agent (视觉/语音) | GPT-4V / Gemini 文档 |

---

## 🏢 四、目标公司与部门

### Tier 1：大厂核心 AI 部门

| 公司 | 相关部门 | 业务方向 | 备注 |
|------|---------|---------|------|
| 字节跳动 | 豆包/扣子(Coze)/Flow | Agent 平台、AI 应用 | 国内 Agent 平台最激进 |
| 阿里巴巴 | 通义实验室/钉钉 AI | 企业 AI Agent、大模型 | 通义千问生态完善 |
| 腾讯 | 混元大模型/元宝 | AI Agent、AI 搜索 | 微信生态 Agent 场景多 |
| 百度 | 文心一言/千帆 | AgentBuilder、行业 Agent | 百度 AI 技术积累深 |
| 蚂蚁集团 | AI Force/支小宝 | 金融 Agent | 金融场景 Agent 落地多 |
| 美团 | AI 平台部 | 本地生活 Agent | 业务+AI 结合 |

### Tier 2：AI 独角兽与明星创业公司

| 公司 | 方向 | 备注 |
|------|------|------|
| 智谱 AI (ChatGLM) | 大模型 + Agent 平台 | 清华系，Agent 生态完善 |
| MiniMax | 多模态大模型 + Agent | 技术实力强 |
| 月之暗面 (Kimi) | 长上下文 + Agent | Kimi 生态 |
| 阶跃星辰 | 多模态 Agent | 技术驱动 |
| 百川智能 | 大模型 + 行业 Agent | 王小川创业 |
| 面壁智能 | Agent 框架 | 清华系，Agent 技术栈深 |
| Dify | 开源 LLMOps 平台 | 国际化开源项目 |
| FastGPT | 开源知识库 + Agent | 国内热门开源 |

### Tier 3：外企与研究院

| 公司 | 部门 | 备注 |
|------|------|------|
| Microsoft | STCA/RAI | AI Agent 研究 + 工程 |
| Amazon | AWS AI | Bedrock Agent |
| NVIDIA | AI Research | Agent 基础设施 |
| 上海 AI Lab | 大模型 + Agent | 科研型实习 |
| 智源研究院 | Agent 研究 | 学术氛围浓 |

---

## 🔧 五、每日学习节奏模板

```
[20min]  论文/技术博客阅读 + 笔记
[90min]  核心学习/编码实战
[10min]  休息
[50min]  项目开发/面试准备
[10min]  每日复盘：今天学了什么？明天重点是什么？
```

---

## 📊 六、每周检查点

### Week 1 检查（6/7）
- [ ] 能用 LangChain 独立写一个带 Tool Calling 的 Agent
- [ ] 简历已按 AI Agent 方向重写
- [ ] GitHub 项目页整洁、有 README
- [ ] 投递清单至少有 20 个目标岗位

### Week 2 检查（6/14）
- [ ] 能解释 LangGraph 的 StateGraph 设计原理
- [ ] 能实现 MCP Server + Client
- [ ] Portfolio 项目选题确定，设计文档完成
- [ ] 开始投递第一批简历（5-10 家）

### Week 3 检查（6/21）
- [ ] 至少 1 个 Portfolio 项目可 Demo
- [ ] 有 Agent 评估指标和测试用例
- [ ] 完成 3+ 篇论文精读笔记
- [ ] 累计投递 15+ 家

### Week 4 检查（6/30）
- [ ] 算法 Hot 100 高频 30 题至少过一遍
- [ ] 能流利回答 AI Agent 系统设计题
- [ ] 至少完成 2 场面试（含模拟）
- [ ] 累计投递 30+ 家

---

## 📖 七、推荐学习资源

### 必读论文（精读）
1. **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al., 2022)
2. **Toolformer: Language Models Can Teach Themselves to Use Tools** (Schick et al., 2023)
3. **AutoGPT: The Heart of the AI Agent Ecosystem**
4. **Generative Agents: Interactive Simulacra of Human Behavior** (Park et al., 2023)
5. **SWE-Agent: Agent-Computer Interfaces for Automated Software Engineering** (Yang et al., 2024)
6. **MetaGPT: Meta Programming for Multi-Agent Collaborative Framework** (Hong et al., 2023)

### 必读技术博客
- [Lil'Log](https://lilianweng.github.io/) — OpenAI 研究员的博客，Agent 综述必读
- [Anthropic Engineering Blog](https://www.anthropic.com/engineering) — MCP/Tool Use 前沿
- [LangChain Blog](https://blog.langchain.dev/) — Agent 工程实践
- [Chip Huyen's Blog](https://huyenchip.com/blog/) — ML/AI 系统工程

### 推荐代码库（读源码）
- [LangGraph](https://github.com/langchain-ai/langgraph) — Agent 框架标杆
- [CrewAI](https://github.com/crewAIInc/crewAI) — Multi-Agent 框架
- [AutoGen](https://github.com/microsoft/autogen) — 微软 Multi-Agent 框架
- [Dify](https://github.com/langgenius/dify) — 开源 LLMOps 平台

---

## 💡 八、面试官视角：3 个决胜关键

### 1. 能用代码说话
> 不要只说"我了解 LangChain"，要展示你用 LangChain 构建了什么。  
> 面试官想看的是：GitHub 上的可运行项目、技术决策的理由、踩坑经历。

### 2. 能讲清楚"为什么"
> 为什么选 LangGraph 而不是 AutoGen？为什么用 ChromaDB 而不是 Milvus？  
> 技术选型背后的 trade-off 分析比"我用过"重要 10 倍。

### 3. 展现学习能力
> Agent 领域变化极快，今天的 SOTA 半年后可能过时。  
> 面试官更在意你如何追踪前沿、如何快速上手新技术。

---

## ⚠️ 九、常见坑与避坑指南

| 坑 | 避坑策略 |
|----|---------|
| 只看不写 | 每个概念都必须写代码验证，"看懂了"≠"会用了" |
| 贪多求全 | 87 小时不可能学完所有东西，聚焦核心，做减法 |
| 忽视简历 | 简历不过，学再好也没面试机会。简历要持续迭代 |
| 海投无策略 | 先投非第一志愿公司练手，梦想公司最后投 |
| 忽视软技能 | 自我介绍、项目故事线、反问环节都要提前打磨 |
| 闭门造车 | 加技术群、找内推、找学长学姐了解部门实际情况 |

---

> **最后的话**：作为博士，你的上限比大多数候选人高。29 天足够从入门到拿到面试，但你需要的不是"学完"，而是"能用代码证明你能干活"。Keep shipping, keep learning. 🚀
