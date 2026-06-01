# Day 12 | 2026-06-12 | 周五 | 学习时长：3h

## 🎯 今日目标
- [ ] 深入对比主流 Embedding 模型（OpenAI / BGE / GTE / 通义）
- [ ] 理解向量索引原理（Flat / IVF / HNSW）并做性能对比
- [ ] 实现 Hybrid Search（BM25 + 稠密向量）
- [ ] 完成检索质量量化对比实验

---

## 📚 学习内容

### 1. 技术阅读（20min）
- 阅读内容：MTEB Leaderboard + ChromaDB / Milvus 索引文档
- 核心收获（3句话以内）：
  - 
  - 
  - 

### 2. Embedding 模型选型（50min）
#### 2.1 候选模型对比
| 模型 | 维度 | 中文能力 | 成本 | 本地部署 |
|------|------|---------|------|---------|
| OpenAI text-embedding-3-small | 1536 | 中 | $0.02/1M tokens | ❌ |
| BGE-M3 (BAAI) | 1024 | 强 | 免费 | ✅ |
| GTE-Qwen2-7B | 3584 | 强 | 免费 | ✅ (需GPU) |
| 阿里 text-embedding-v3 | 1024 | 强 | 约 0.01/1M | ❌ |

#### 2.2 实验：同一批文档，不同 Embedding 模型的检索效果
```python
# 练习文件：projects/hello-agent/day12_embedding_benchmark.py
```
- [ ] 准备测试集：20 篇论文摘要 + 10 个 Query
- [ ] 用 3 种 Embedding 模型分别建索引
- [ ] 评测 Top-5 Recall 和 MRR
- 实验结论：

### 3. 向量索引优化（50min）
#### 3.1 三种索引方式
- [ ] **Flat（暴力搜索）**：精确但慢，适合 < 10 万向量
- [ ] **IVF（倒排索引）**：先聚类再搜索，速度↑ 精度↓
- [ ] **HNSW（分层可导航小世界图）**：图索引，速度与精度的最佳平衡
- 练习文件：`projects/hello-agent/day12_index_comparison.py`

#### 3.2 实验：10 万向量的检索性能对比
- [ ] 用 ChromaDB / Qdrant 分别测试不同索引
- [ ] 指标：QPS / P99 延迟 / Recall@10
- 实验结论：

### 4. Hybrid Search 实战（40min）
#### 4.1 稠密检索 + 稀疏检索
- [ ] **稠密检索**（语义）：Embedding 向量相似度 — 适合语义相近的查询
- [ ] **稀疏检索**（关键词）：BM25（Elasticsearch / Milvus）— 适合精确关键词匹配
- [ ] **Hybrid**：融合两路结果（加权求和 / RRF 倒数秩融合）

#### 4.2 实现 Hybrid Search
```python
# 练习文件：projects/hello-agent/day12_hybrid_search.py
```
- [ ] BM25 路：用 `rank_bm25` 库实现
- [ ] 稠密路：ChromaDB 相似度搜索
- [ ] RRF 融合：`score = Σ 1/(k + rank_i)`
- [ ] 实验：对比 Pure Dense vs Pure BM25 vs Hybrid 的检索效果
- 实验结论：

### 5. 检索质量评测（20min）
- [ ] 计算 MRR（Mean Reciprocal Rank）
- [ ] 计算 NDCG@5 / NDCG@10
- [ ] 计算 Recall@5 / Recall@10
- [ ] 练习文件：`projects/hello-agent/day12_eval_metrics.py`

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- Agent 记忆系统：短期记忆 / 长期记忆 / 语义记忆
- Mem0 / MemGPT 调研
- 实现带长期记忆的 Agent Demo

## ⏱️ 实际时间分配
- 技术阅读：___min
- Embedding 对比：___min
- 索引优化：___min
- Hybrid Search：___min
- 评测指标：___min
