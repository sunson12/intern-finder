# Day 18 | 2026-06-18 | 周四 | 学习时长：3h

## 🎯 今日目标
- [ ] 掌握 Token 消耗优化策略（Prompt 精简 / 历史压缩 / Caching）
- [ ] 理解并实践 Prompt Caching（Anthropic 的 cache_control + OpenAI 的 automatic caching）
- [ ] 实现模型路由（简单问题用小模型，复杂问题用大模型）
- [ ] 量化优化效果：优化前后 Token 消耗和延迟对比

---

## 📚 学习内容

### 1. 技术阅读（20min）
- 阅读内容：Anthropic Prompt Caching 文档 + OpenAI Prompt Caching 文档
- 核心收获（3句话以内）：
  - 
  - 
  - 

### 2. Token 消耗优化（60min）
#### 2.1 Token 消耗分析
- [ ] 分析 Portfolio 项目中最大的 Token 消耗源
  - System Prompt：___ tokens
  - 历史轨迹：___ tokens
  - Tool 返回结果：___ tokens
  - 最终生成：___ tokens
- [ ] 识别优化优先级

#### 2.2 优化策略逐一实践
- [ ] **Prompt 精简**：重写 System Prompt，在保持效果的前提下减少 30% Token
- [ ] **历史压缩**：对 Agent 中间步骤做 LLM 摘要，替代原文
- [ ] **Tool 结果截断**：限制 Tool 返回内容的长度（如只保留前 500 字）
- [ ] **滑动窗口**：只保留最近 K 步的完整状态
- 练习文件：`projects/<项目名>/eval/token_optimization.py`
- 优化效果记录：

| 优化策略 | 优化前 Token | 优化后 Token | 节省比例 | 对效果的影响 |
|---------|------------|------------|---------|------------|
| Prompt精简 | | | | |
| 历史压缩 | | | | |
| 结果截断 | | | | |
| 滑动窗口 | | | | |

### 3. Prompt Caching 实战（50min）
#### 3.1 Anthropic Prompt Caching
```python
# 练习文件：projects/hello-agent/day18_anthropic_cache.py
```
- [ ] 理解 `cache_control: {"type": "ephemeral"}` 标记
- [ ] 在 System Prompt 和 Tool Definitions 上标记缓存
- [ ] 实测：连续 5 次请求的延迟和费用变化
- 结论：

#### 3.2 OpenAI Automatic Caching
- [ ] 理解自动缓存的条件（前缀匹配 1024 Token 以上）
- [ ] 实测 OpenAI 的缓存命中情况
- [ ] 对比 Anthropic 手动标记 vs OpenAI 自动检测的差异

### 4. 模型路由策略（50min）
```python
# 练习文件：projects/hello-agent/day18_model_router.py
```

#### 4.1 路由逻辑设计
- [ ] 简单问题 → 小模型（如 GPT-4o-mini / Qwen-Turbo / Haiku）
- [ ] 复杂推理 → 大模型（如 GPT-4o / Qwen-Plus / Sonnet）
- [ ] 路由判断依据：Query 复杂度分类器 / 关键词匹配 / LLM 自动判断

#### 4.2 实现 Fallback 链
- [ ] 小模型 → 失败/质量不达标 → 自动升级到大模型
- [ ] 定义"质量不达标"的判断标准
- [ ] 统计路由比例和成本节省

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- Portfolio 项目 2 启动（或项目 1 深度迭代）
- 加入 UI（Chainlit / Gradio）
- Streaming 输出实现

## ⏱️ 实际时间分配
- 技术阅读：___min
- Token 优化：___min
- Prompt Caching：___min
- 模型路由：___min
