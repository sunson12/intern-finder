# Day 1 | 2026-06-01 | 周一 | 学习时长：3h

## 🎯 今日目标
- [ ] 理解四周冲刺路线全貌，明确每周里程碑
- [ ] 搭建 Python 开发环境（Python 3.11+, venv, 核心依赖）
- [ ] 注册至少 1 个 LLM API 并成功调用
- [ ] 运行第一个 LangChain "Hello World"

---

## 📚 学习内容

### 1. 路线理解（30min）
- 阅读内容：通读 [ROADMAP.md](../ROADMAP.md) 全文
- 核心收获（3句话以内）：
  - 
  - 
  - 
- 标记出自己最薄弱的 3 个环节：
  1. 
  2. 
  3. 

### 2. 环境搭建（60min）
- [ ] 检查 Python 版本：`python --version`（需要 >= 3.11）
- [ ] 创建虚拟环境：`python -m venv venv`
- [ ] 激活虚拟环境：`venv\Scripts\activate`（Windows）
- [ ] 安装核心包：
  ```bash
  pip install langchain langchain-openai langchain-anthropic langchain-community
  pip install langgraph chromadb
  pip install fastapi uvicorn[standard] pydantic
  pip install python-dotenv tiktoken
  ```
- [ ] 配置 VS Code（安装 Python/Pylance 插件）
- 踩坑记录：

### 3. API Key 获取与测试（50min）
- [ ] 注册 **[阿里百炼](https://bailian.console.aliyun.com/)**（推荐首选，免费额度足）
  - 获取 DashScope API Key
  - 配置 `.env` 文件：`DASHSCOPE_API_KEY=sk-xxx`
- [ ] 备选：注册 **[DeepSeek](https://platform.deepseek.com/)** 或 **[智谱 AI](https://open.bigmodel.cn/)**
- [ ] 测试 API 连通性 —— 运行下面的脚本验证：
  ```python
  import os
  from dotenv import load_dotenv
  from langchain_openai import ChatOpenAI
  
  load_dotenv()
  
  # 阿里百炼（兼容 OpenAI 格式）
  llm = ChatOpenAI(
      model="qwen-plus",
      api_key=os.getenv("DASHSCOPE_API_KEY"),
      base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
  )
  
  response = llm.invoke("用一句话解释什么是 AI Agent")
  print(response.content)
  ```
- API 测试结果：✅ / ❌
- 遇到的问题 + 解决方案：

### 4. 第一个 LangChain Chain（40min）
- 目标：跑通一个最简单的 Prompt Template → LLM → Output Parser 链
  ```python
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import StrOutputParser
  
  prompt = ChatPromptTemplate.from_messages([
      ("system", "你是一个{role}，请用{style}风格回答问题。"),
      ("user", "{question}")
  ])
  
  chain = prompt | llm | StrOutputParser()
  
  result = chain.invoke({
      "role": "AI Agent 工程师",
      "style": "简洁",
      "question": "什么是 Function Calling？"
  })
  print(result)
  ```
- 代码产出：`d:\intern_finder\projects\hello-agent\day01_hello_chain.py`
- 遇到的问题 + 解决方案：

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- 深入学习 Prompt Engineering（Few-shot / CoT / ReAct / 结构化输出）
- 理解 Token 与 Context Window 机制
- 动手写 10+ 条不同场景的高质量 Prompt

## ⏱️ 实际时间分配
- 路线理解：___min
- 环境搭建：___min
- API 测试：___min
- 代码实战：___min
