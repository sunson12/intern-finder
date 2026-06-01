# Day 17 | 2026-06-17 | 周三 | 学习时长：3h

## 🎯 今日目标
- [ ] 掌握 Agent 评估的核心指标体系（任务完成率 / 工具选择准确率 / 幻觉率）
- [ ] LangSmith / Braintrust 实操：为 Portfolio 项目建立评估
- [ ] 写自动化评测脚本（批量测试用例 + 指标计算）
- [ ] 跑通完整的"改代码 → 跑评测 → 看指标"循环

---

## 📚 学习内容

### 1. 技术阅读（20min）
- 阅读内容：[LangSmith Evaluation Guide](https://docs.smith.langchain.com/evaluation) + [Braintrust Docs](https://www.braintrust.dev/docs)
- 核心收获（3句话以内）：
  - 
  - 
  - 

### 2. Agent 评估指标体系（40min）
#### 2.1 核心指标定义
| 维度 | 指标 | 计算方式 | 目标值 |
|------|------|---------|--------|
| 任务完成 | 任务成功率 | 最终输出满足需求 / 总测试数 | > 85% |
| 工具使用 | 工具选择准确率 | 正确选择的工具数 / 总工具调用数 | > 90% |
| 推理质量 | 平均步数 | 完成任务的平均 Agent 步数 | 越少越好 |
| 效率 | Token 消耗 | 单次任务的 Token 消耗 | 控制预算 |
| 可靠性 | 幻觉率 | 编造事实/数据的比例 | < 5% |
| 用户体验 | 首次响应时间 | 从请求到第一条流式输出 | < 2s |

#### 2.2 为 Portfolio 项目设计评测集
- [ ] 准备 10-20 条测试用例（覆盖正常/边界/异常场景）
- [ ] 每条用例标注预期结果（Ground Truth）
- [ ] 练习文件：`projects/<项目名>/eval/test_cases.json`

### 3. LangSmith 实操（50min）
#### 3.1 接入 LangSmith
```python
# 练习文件：projects/<项目名>/eval/langsmith_eval.py
```
- [ ] 注册 LangSmith + 获取 API Key
- [ ] 在 Agent 代码中设置环境变量 `LANGCHAIN_TRACING_V2=true`
- [ ] 跑 3 个测试用例，观察 LangSmith Trace
- [ ] 理解 Trace / Run / Span 的层级关系

#### 3.2 创建自动化评估
- [ ] 使用 LangSmith 的 `evaluate()` 函数
- [ ] 定义自定义 Evaluator（如 `correctness_evaluator` / `tool_accuracy_evaluator`）
- [ ] 批量运行评测，查看结果 Dashboard

### 4. 自动化评测 Pipeline（40min）
```python
# 练习文件：projects/<项目名>/eval/auto_eval.py
```
- [ ] 批量读取 `test_cases.json`
- [ ] 依次运行 Agent，收集结果
- [ ] 用 LLM-as-Judge 评判输出质量（正确性 / 完整性 / 相关性）
- [ ] 汇总计算各指标
- [ ] 输出评测报告（JSON + Markdown 格式）

### 5. 建立持续评测习惯（30min）
- [ ] 每次修改 Agent 代码后，跑一遍评测
- [ ] 对比改前/改后的指标变化
- [ ] 记录 3 个"改完代码后指标反而下降"的教训（如果有）
- 笔记：

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- Agent 性能优化：Token 消耗优化 + Prompt Caching + 并发批处理
- 模型路由策略（大模型 → 小模型 Fallback）

## ⏱️ 实际时间分配
- 技术阅读：___min
- 指标体系：___min
- LangSmith：___min
- 自动化评测：___min
