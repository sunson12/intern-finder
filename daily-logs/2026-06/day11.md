# Day 11 | 2026-06-11 | 周四 | 学习时长：3h

## 🎯 今日目标
- [ ] 理解 MCP 协议的设计动机与架构（类比 USB 协议）
- [ ] 实现一个 MCP Server（暴露 Tool + Resource + Prompt）
- [ ] 实现一个 MCP Client（连接 Server + 调用 Tool）
- [ ] 将 Day 5 的 Arxiv 检索功能封装为 MCP Tool

---

## 📚 学习内容

### 1. 技术阅读（30min）
- 阅读内容：[MCP 官方文档](https://modelcontextprotocol.io/) Introduction + Core Architecture
- 核心收获（3句话以内）：
  - 
  - 
  - 
- MCP 要解决的核心问题：
  - 

### 2. MCP 协议架构理解（30min）
#### 2.1 三种原语
| 原语 | 用途 | 类比 |
|------|------|------|
| **Tool** | 模型调用外部功能（执行操作） | REST API POST |
| **Resource** | 模型读取外部数据（只读） | REST API GET |
| **Prompt** | 预置提示词模板（可参数化） | Prompt Library |

#### 2.2 Client-Server 通信
- [ ] 理解初始化握手流程：`initialize` → `initialized` → 能力协商
- [ ] 理解 JSON-RPC 2.0 消息格式
- [ ] 理解 Transport 层：stdio / SSE / Streamable HTTP
- 笔记：

### 3. 实现 MCP Server（60min）
```python
# 练习文件：projects/hello-agent/day11_mcp_server.py
```
#### 3.1 从零编写 MCP Server
- [ ] 创建 Server 实例，设置名称和版本
- [ ] 注册 Tool：`search_arxiv(query: str, max_results: int) -> list[dict]`
- [ ] 注册 Resource：`arxiv://recent/{category}` — 读取某分类最新论文
- [ ] 注册 Prompt：`paper_review_template` — 论文审稿 Prompt 模板
- [ ] 用 stdio transport 启动 Server

#### 3.2 测试 MCP Server
- [ ] 用 MCP Inspector 测试（可选）
- [ ] 写一个简单的测试脚本手动验证

### 4. 实现 MCP Client + LangChain 集成（60min）
```python
# 练习文件：projects/hello-agent/day11_mcp_client.py
```
#### 4.1 MCP Client 实现
- [ ] 连接 MCP Server（stdio transport）
- [ ] `list_tools()` 获取可用工具列表
- [ ] `call_tool()` 调用工具并获取结果
- [ ] `read_resource()` 读取资源
- [ ] `get_prompt()` 获取预置 Prompt

#### 4.2 与 LangChain/LangGraph 集成
- [ ] 将 MCP Tools 转换为 LangChain Tool 格式
- [ ] 将 MCP Tools 注入 LangGraph Agent 的工具列表
- [ ] 跑通完整流程：用户输入 → Agent → MCP Tool → 结果 → Agent → 最终回答

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- 向量数据库进阶：Embedding 模型选型 + 索引优化
- Hybrid Search（BM25 + 稠密向量）实现
- 检索质量量化对比（MRR / NDCG / Recall）

## ⏱️ 实际时间分配
- 技术阅读：___min
- 协议理解：___min
- Server 实现：___min
- Client+集成：___min
