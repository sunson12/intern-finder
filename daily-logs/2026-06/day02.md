# Day 2 | 2026-06-02 | 周二 | 学习时长：3h

## 🎯 今日目标
- [ ] 掌握 Prompt Engineering 核心技巧（Few-shot / CoT / ReAct / 结构化输出）
- [ ] 理解 Token 与 Context Window 机制（tiktoken 实操）
- [ ] 学习 Temperature / Top-P / Stop Sequence 等参数调优
- [ ] 编写 10+ 条不同场景的高质量 Prompt

---

## 📚 学习内容

### 1. 技术阅读（20min）
- 阅读内容：[Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- 核心收获（3句话以内）：
  - 
  - 
  - 

### 2. Prompt Engineering 实战（90min）
#### 2.1 Few-shot Prompting（20min）
- 概念：在 Prompt 中给出示例，引导模型按期望格式输出
- 练习：写一个"论文研究方向分类器"，给出 3 个示例后让模型分类新输入
  ```python
  # 练习文件：projects/hello-agent/day02_fewshot.py
  ```
- [ ] 完成练习代码

#### 2.2 Chain of Thought（CoT）（20min）
- 概念：让模型"一步一步思考"，提升推理准确率
- 练习：写一个"代码 Bug 分析器"，要求模型先分析后给出修复
  ```python
  # 练习文件：projects/hello-agent/day02_cot.py
  ```
- [ ] 完成练习代码
- COT的作用：
  面试时如果有人问你"怎么提高 LLM 推理准确率"，CoT 是第一个要说的答案。记住这句：

  "加一句 Let's think step by step 就能显著提升推理准确率——这是 Wei et al. 2022 论文验证过的，成本为零，效果显著，是 Prompt Engineering 的第一条原则。"
#### 2.3 ReAct Prompting（25min）
- 概念：Thought → Action → Observation 循环的 Prompt 模板
- 练习：手写一个最小 ReAct Prompt 模板（不依赖 LangChain）
  ```python
  # 练习文件：projects/hello-agent/day02_react_prompt.py
  ```
- [ ] 完成练习代码

#### 2.4 结构化输出（25min）
- 概念：让模型输出固定格式的 JSON
- 练习：使用 LangChain `with_structured_output()` 或 Pydantic 定义输出 Schema
  ```python
  # 练习文件：projects/hello-agent/day02_structured_output.py
  ```
- [ ] 完成练习代码

### 3. Token 机制深入（40min）
- [ ] 用 tiktoken 实测：同一段中英文的 Token 数量差异
- [ ] 理解不同模型的 Tokenizer 差异（GPT vs Claude vs Qwen）
- [ ] 手动计算一次 API 调用的 Token 消耗和费用
- [ ] 实验：把一段文本从 100 Token 扩充到 1000 Token，观察输出质量变化
- 踩坑记录：

### 4. 参数调优实验（30min）
- [ ] Temperature=0 vs 0.7 vs 1.5 的输出对比（同一 Prompt 跑 3 次）
- [ ] Top-P 的效果实验
- [ ] Stop Sequence 的实际用途（控制 Agent 停止条件）
- 结论：

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- 深入 Function Calling 原理
- 手写 Tool Schema 定义
- 实现完整的 Tool Calling 循环（含错误处理与重试）

## ⏱️ 实际时间分配
- 技术阅读：___min
- Prompt 实战：___min
- Token 实验：___min
- 参数实验：___min
