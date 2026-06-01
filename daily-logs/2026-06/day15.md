# Day 15 | 2026-06-15 | 周一 | 学习时长：3h

## 🎯 今日目标
- [ ] Portfolio 项目 MVP 开发 Day 1：搭建核心 Agent 工作流
- [ ] LangGraph 图结构设计 + 实现（所有 Node + Edge）
- [ ] 跑通 Happy Path（完整的端到端流程）
- [ ] 第一个可 Demo 的 MVP 版本

---

## 📚 学习内容

> ⚠️ 今天主要是写代码，不是学新知识。目标是产出能跑的代码。

### 1. 项目启动检查（15min）
- [ ] 回顾 Day 14 写的项目设计文档 (`projects/<项目名>/DESIGN.md`)
- [ ] 确认今天的 MVP 边界：
  - 必须要有的功能（核心流程）：___________
  - 今天不做的功能（留给迭代）：___________
- [ ] Git：创建功能分支 `git checkout -b feat/mvp`

### 2. Agent 工作流实现（90min）
#### 2.1 搭建 LangGraph 骨架（30min）
```python
# projects/<项目名>/src/graph.py
```
- [ ] 定义 State Schema（TypedDict）
- [ ] 创建所有 Node（每个 Node 先写最简单的逻辑，能跑就行）
- [ ] 定义 Edge（普通边 + 条件边）
- [ ] compile() + 测试空调用

#### 2.2 实现核心 Node（40min）
- [ ] Node 1：___________
- [ ] Node 2：___________
- [ ] Node 3：___________
- [ ] Node 4：___________
- [ ] 每个 Node 写完后单独测试

#### 2.3 联调 + 端到端测试（20min）
- [ ] 整体 invoke，观察 State 流转
- [ ] 记录 3 个不同输入的完整轨迹

### 3. Tool 集成（40min）
#### 3.1 实现项目特定的 Tools
- [ ] Tool 1：___________
- [ ] Tool 2：___________
- [ ] Tool 3：___________
#### 3.2 将 Tools 注册到 Agent
- [ ] 确保 Tool Schema 的描述清晰、参数类型正确
- [ ] 测试每个 Tool 的独立调用

### 4. 跑通 Happy Path（35min）
- [ ] 准备 3 个典型测试场景
- [ ] 每个场景从输入到输出全流程测试
- [ ] 记录输出质量 + 执行时间
- [ ] 标记已知 Bug / 待优化点（加入 Issue）

---

## 📊 MVP 交付物检查
- [ ] `src/graph.py` — Agent 工作流图
- [ ] `src/tools.py` — 项目专用 Tools
- [ ] `src/state.py` — State 定义
- [ ] `main.py` — 入口，能直接 `python main.py` 运行
- [ ] `requirements.txt` — 依赖清单
- [ ] 至少 1 个 Happy Path 测试通过

---

## 💡 今日收获
1. （写代码中的技术决策与踩坑）
2. 
3. 

## 🔮 明日计划
- MVP 完善：错误处理 + 边界情况
- 添加日志 + 调试信息
- 录制 Demo 视频 / 截 GIF
- 写 README 初稿

## ⏱️ 实际时间分配
- 启动检查：___min
- 工作流实现：___min
- Tool 集成：___min
- Happy Path 测试：___min
