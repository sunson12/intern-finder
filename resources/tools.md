# 🔧 常用工具与配置

## 开发环境

### 推荐 IDE
- **VS Code** + GitHub Copilot / Cursor（AI 辅助编码）
- **Jupyter Lab**：快速实验、Prompt 调试

### VS Code 推荐插件
- Python / Pylance
- GitHub Copilot / Codeium
- Thunder Client（API 测试）
- Markdown Preview Enhanced
- GitLens

---

## API Key 获取

| 平台 | 注册地址 | 模型 | 免费额度 |
|------|---------|------|---------|
| OpenAI | https://platform.openai.com/ | GPT-4o, GPT-4.1 | 注册送 $5 |
| Anthropic | https://console.anthropic.com/ | Claude Opus 4, Sonnet 4 | 注册送 $5 |
| 阿里百炼 | https://bailian.console.aliyun.com/ | 通义千问系列 | 百万 Token 免费 |
| 智谱 AI | https://open.bigmodel.cn/ | GLM-4 系列 | 注册送额度 |
| DeepSeek | https://platform.deepseek.com/ | DeepSeek-V3 | 注册送额度 |
| 硅基流动 | https://siliconflow.cn/ | 多种开源模型 | 注册送额度 |

### 本地 API Key 配置
```bash
# ~/.bashrc 或 ~/.zshrc
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export DASHSCOPE_API_KEY="sk-..."
export ZHIPUAI_API_KEY="..."
```

---

## 常用 Python 包

### 核心框架
```bash
pip install langchain langchain-openai langchain-anthropic langchain-community
pip install langgraph  # Agent 编排
pip install llama-index llama-index-llms-openai  # RAG 框架
pip install autogen-agentchat crewai  # Multi-Agent
```

### 向量数据库
```bash
pip install chromadb  # 轻量级，开发首选
pip install qdrant-client  # 生产级
pip install pymilvus  # 大规模向量检索
```

### API 与服务
```bash
pip install fastapi uvicorn[standard]  # API 框架
pip install sse-starlette  # SSE 流式输出
pip install pydantic  # 数据验证
```

### UI 框架
```bash
pip install chainlit  # AI 应用 UI，推荐
pip install gradio  # 通用 ML Demo
```

### 数据处理
```bash
pip install pypdf beautifulsoup4 markdown  # 文档解析
pip install tiktoken  # Token 计数
pip install pandas numpy  # 数据处理
```

### 评估与监控
```bash
pip install langsmith  # LangChain 官方评估平台
pip install braintrust  # 开源评估框架
```

---

## 推荐关注的信息源

### 微信公众号
- 机器之心
- 量子位
- 夕小瑶的卖萌屋
- AIGC 开放社区
- 赛博禅心

### GitHub Projects（每日刷 Trending）
- https://github.com/trending/python

### Discord/微信群
- Anthropic Developer Discord
- LangChain Discord
- 各个大模型公司的开发者群

### 内推信息
- 牛客网：https://www.nowcoder.com/
- 脉脉：https://maimai.cn/
- 小红书（搜"实习内推"）
- 实验室学长学姐
