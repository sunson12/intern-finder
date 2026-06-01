# Day 4 | 2026-06-04 | 周四 | 学习时长：3h

## 🎯 今日目标
- [ ] 掌握 LangChain 核心抽象：Chain / LCEL / Runnable 接口
- [ ] 深入 Prompt Template 设计模式
- [ ] 掌握 Output Parser（StrOutputParser / JsonOutputParser / PydanticOutputParser）
- [ ] 理解并实践 Conversation Memory（Buffer / Summary / Window）

---

## 📚 学习内容

### 1. 技术阅读（20min）
- 阅读内容：[LangChain Expression Language (LCEL)](https://python.langchain.com/docs/concepts/lcel/)
- 核心收获（3句话以内）：
  - 
  - 
  - 

### 2. LCEL 与 Runnable 接口（60min）
#### 2.1 LCEL 运算符
- [ ] `|`（管道）：串联两个 Runnable
- [ ] `.bind()`：预绑定参数
- [ ] `.with_config()`：运行时配置
- [ ] `.with_retry()`：自动重试
- [ ] `.with_fallbacks()`：降级策略
- [ ] 练习文件：`projects/hello-agent/day04_lcel_basics.py`

#### 2.2 Runnable 分支与并行
- [ ] `RunnableParallel`：并行执行多个 Chain
- [ ] `RunnableBranch`：条件路由
- [ ] `RunnableLambda`：自定义函数包装
- [ ] 练习文件：`projects/hello-agent/day04_runnable_advanced.py`

#### 2.3 实战：构建一个分析 Pipeline
```python
# 输入一段代码 → 并行分析（安全检查 + 性能分析 + 风格审查）→ 汇总报告
```
- [ ] 完成 Pipeline 代码

### 3. Output Parser 进阶（40min）
- [ ] `StrOutputParser`：纯文本输出
- [ ] `JsonOutputParser`：JSON 结构化输出（含自动重试修复格式错误）
- [ ] `PydanticOutputParser`：用 Pydantic 模型约束输出
- [ ] 练习文件：`projects/hello-agent/day04_output_parser.py`

### 4. Memory 机制（60min）
#### 4.1 三种记忆对比实现
- [ ] `ConversationBufferMemory`：全量保存（适合短对话）
- [ ] `ConversationBufferWindowMemory`：滑动窗口（最近 K 轮）
- [ ] `ConversationSummaryMemory`：LLM 自动摘要（适合长对话）
- [ ] 练习文件：`projects/hello-agent/day04_memory.py`

#### 4.2 记忆的 Token 管理
- [ ] 计算不同记忆策略的 Token 消耗
- [ ] 实现 Token 预算感知的记忆裁剪
- 结论：

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- RAG 全流程实战（文档加载→分块→向量化→检索→生成）
- 对比 LangChain 和 LlamaIndex 的 RAG 实现
- ChromaDB 实战

## ⏱️ 实际时间分配
- 技术阅读：___min
- LCEL 实战：___min
- Output Parser：___min
- Memory：___min
