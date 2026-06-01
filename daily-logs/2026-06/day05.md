# Day 5 | 2026-06-05 | 周五 | 学习时长：3h

## 🎯 今日目标
- [ ] 从零实现完整的 RAG Pipeline（文档加载→分块→向量化→检索→生成）
- [ ] 对比不同分块策略的效果（固定大小 vs 语义分块 vs 递归分块）
- [ ] 动手优化检索质量（MMR / 相似度阈值 / Hybrid Search）
- [ ] 用 ChromaDB 搭建本地向量存储

---

## 📚 学习内容

### 1. 技术阅读（20min）
- 阅读内容：[LlamaIndex RAG Guide](https://docs.llamaindex.ai/en/stable/understanding/rag/) 或 LangChain RAG Tutorial
- 核心收获（3句话以内）：
  - 
  - 
  - 

### 2. RAG Pipeline 从零搭建（90min）
#### 2.1 文档加载与解析（15min）
- [ ] 加载 PDF（pypdf）
- [ ] 加载网页（BeautifulSoup / WebBaseLoader）
- [ ] 加载 Markdown
- [ ] 练习文件：`projects/hello-agent/day05_document_loader.py`

#### 2.2 分块策略对比实验（30min）
- [ ] 固定大小分块（chunk_size=500, overlap=50）
- [ ] 递归字符分块（RecursiveCharacterTextSplitter）
- [ ] 语义分块（SemanticChunker）
- [ ] 实验：同一篇论文，3 种分块方式，后续检索对比 Top-3 命中率
- [ ] 练习文件：`projects/hello-agent/day05_chunking.py`
- 实验结论：

#### 2.3 Embedding 与向量存储（25min）
- [ ] 选择 Embedding 模型（OpenAI text-embedding-3-small / 阿里 text-embedding-v2 / 本地 BGE）
- [ ] 创建 ChromaDB Collection
- [ ] 批量向量化并存入 ChromaDB
- [ ] 练习文件：`projects/hello-agent/day05_embedding.py`

#### 2.4 检索 + 生成（20min）
- [ ] 基础检索：相似度搜索
- [ ] 将检索结果注入 Prompt
- [ ] LLM 基于上下文生成答案（带引用）
- [ ] 练习文件：`projects/hello-agent/day05_rag_complete.py`

### 3. 检索优化实战（40min）
- [ ] MMR（最大边际相关性）：平衡相关性与多样性
- [ ] 相似度阈值过滤：低于阈值的 chunk 丢弃
- [ ] Multi-Query Retrieval：从多个角度改写 Query 再检索
- [ ] 实验：同一 Query，对比 3 种策略的检索结果
- 实验结论：

### 4. LangChain vs LlamaIndex RAG 对比（30min）
- [ ] 用 LlamaIndex 实现相同的 RAG Pipeline
- [ ] 对比代码量和抽象层级
- [ ] 练习文件：`projects/hello-agent/day05_llamaindex_rag.py`
- 对比结论：

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- 简历优化：按 AI Agent 方向重写项目经历
- 技术关键词全覆盖检查
- 英文简历初稿

## ⏱️ 实际时间分配
- 技术阅读：___min
- RAG Pipeline：___min
- 检索优化：___min
- 框架对比：___min
