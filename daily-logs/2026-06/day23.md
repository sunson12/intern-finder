# Day 23 | 2026-06-23 | 周二 | 学习时长：3h

## 🎯 今日目标
- [ ] 算法复习：树 / 递归 / 回溯 / 简单 DP（10 题）
- [ ] AI 八股文：能流畅推导 Transformer Self-Attention + 复杂度
- [ ] 能讲清楚 RLHF vs DPO 的核心区别

---

## 📚 学习内容

### 1. 算法复习（60min）
#### 树与递归
- [ ] ⭐ **二叉树的中序遍历**（#94）：递归 + 迭代（栈）
- [ ] ⭐ **二叉树的层序遍历**（#102）：BFS 队列
- [ ] ⭐ **二叉树的最大深度**（#104）：递归
- [ ] **验证二叉搜索树**（#98）：中序遍历递增

#### 回溯
- [ ] ⭐ **全排列**（#46）：回溯模板
- [ ] **子集**（#78）：回溯 / 迭代
- [ ] **括号生成**（#22）：回溯+剪枝

#### 简单 DP
- [ ] ⭐ **爬楼梯**（#70）：Fib DP
- [ ] **最大子数组和**（#53）：Kadane O(n)
- [ ] **打家劫舍**（#198）：一维 DP

### 2. AI 八股文（90min）
#### 2.1 Transformer 推导（40min）
**必须能手写公式 + 讲清楚**：
- [ ] Self-Attention：Q、K、V 的来源（X × W_Q, W_K, W_V）
- [ ] Attention Score = softmax(QK^T / √d_k)
- [ ] √d_k 的作用（防止点积过大 → 梯度消失）
- [ ] Multi-Head Attention：拼接 → 线性变换
- [ ] 复杂度：O(n²d)，n 是序列长度
- [ ] Position Encoding：正弦编码 + 可学习编码
- [ ] Layer Norm：Post-LN vs Pre-LN
- [ ] 练习：在一张白纸上画出完整的 Transformer 结构图并标注每一层的输入/输出维度

#### 2.2 Attention 变体（15min）
- [ ] MHA（Multi-Head Attention）：标准版
- [ ] MQA（Multi-Query Attention）：所有 Head 共享 K、V → 推理加速
- [ ] GQA（Grouped-Query Attention）：分组共享 → MHA 与 MQA 的折中
- [ ] FlashAttention：IO-aware 分块计算 → 不改变结果但快 2-4x

#### 2.3 RLHF vs DPO（20min）
- [ ] RLHF 三阶段：SFT → Reward Model → PPO
- [ ] RLHF 的问题：3 个模型（Policy + Ref + Reward）、训练不稳定
- [ ] DPO 核心思想：直接在偏好数据上用 Pairwise Loss，不需要显式 Reward Model
- [ ] DPO 的数学直觉：等价于 RLHF 在 Bradley-Terry 模型下的最优解
- [ ] DPO 的局限：不能 online exploration

#### 2.4 Agent 相关八股（15min）
- [ ] ReAct 原理（参考 Day 9 笔记）
- [ ] Function Calling 实现原理（参考 Day 3 笔记）
- [ ] RAG 全流程及优化策略（参考 Day 5/12 笔记）
- [ ] Agent 记忆系统三层架构（参考 Day 13 笔记）
- [ ] MCP 协议设计（参考 Day 11 笔记）

---

## 💡 今日收获
1. 八股文最薄弱环节：
2. 
3. 

## 🔮 明日计划
- 系统设计：设计一个 AI Agent 平台 + 设计一个 RAG 系统
- 练习口头表达系统设计思路

## ⏱️ 实际时间分配
- 算法：___min
- Transformer：___min
- Attention 变体：___min
- RLHF/DPO：___min
- Agent 八股：___min
