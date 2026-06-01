# Day 3 | 2026-06-03 | 周三 | 学习时长：3h

## 🎯 今日目标
- [ ] 深入理解 Function Calling / Tool Use 的工作原理
- [ ] 掌握 JSON Schema 定义 Tool 的方法
- [ ] 实现完整的 Tool Calling 循环（含错误处理与自动重试）
- [ ] 完成一个带 Tool Calling 的天气查询 Agent

---

## 📚 学习内容

### 1. 技术阅读（20min）
- 阅读内容：[OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- 核心收获（3句话以内）：
  - 
  - 
  - 

### 2. Function Calling 原理（40min）
#### 2.1 模型是如何学会"调用工具"的？
- [ ] 理解训练数据中的 Tool Call 格式
- [ ] 理解 API 层面的 tool_choice 参数（auto / none / required / 指定工具）
- [ ] 看懂一次完整的 function_call 请求/响应 JSON
- 笔记：

#### 2.2 手写 Tool Schema（30min）
- [ ] 练习：定义 3 个不同复杂度的 Tool Schema
  1. 简单：`get_current_time()` — 无参数
  2. 中等：`search_paper(query, max_results)` — 有参数+类型约束+描述
  3. 复杂：`analyze_code(file_path, check_types=["bug","security","style"])` — 枚举参数
  ```python
  # 练习文件：projects/hello-agent/day03_tool_schema.py
  ```
- [ ] 完成练习代码

### 3. Tool Calling 循环实战（80min）
#### 3.1 实现基础 Tool Calling 循环
```python
# 练习文件：projects/hello-agent/day03_tool_loop.py
```
实现逻辑：
1. 用户输入 → LLM 判断是否需要调用工具
2. 如果需要 → 执行工具 → 结果返回 LLM → LLM 生成最终回答
3. 如果不需要 → 直接生成回答

- [ ] 完成基础循环代码

#### 3.2 增强：错误处理与重试
- [ ] 工具执行超时处理（asyncio.timeout）
- [ ] Tool 返回异常时让 LLM 重新决策
- [ ] 防止无限循环（最大重试次数 + Token 预算）
- [ ] 完成增强版代码

#### 3.3 完整 Demo：天气查询 Agent
- 目标：用户问"杭州明天天气怎么样？适合出去玩吗？"
  - Agent 调用 `get_weather(city, date)` 获取天气
  - 基于天气数据 + 用户意图给出建议
- [ ] 完成完整 Demo

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- LangChain 核心概念：Chain / LCEL / Runnable 接口
- Prompt Template / Output Parser 进阶
- Memory 机制（ConversationBuffer / Summary）

## ⏱️ 实际时间分配
- 技术阅读：___min
- 原理学习：___min
- Tool Loop 实战：___min
