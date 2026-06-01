# Day 16 | 2026-06-16 | 周二 | 学习时长：3h

## 🎯 今日目标
- [ ] 完善 MVP：错误处理 + 边界情况 + 超时保护
- [ ] 添加结构化日志 + 调试信息
- [ ] 录制 Demo 短视频 / 截 GIF
- [ ] 完成项目 README（含架构图 + 快速开始）

---

## 📚 学习内容

### 1. MVP 加固（90min）
#### 1.1 错误处理（30min）
- [ ] LLM 调用失败重试（with_retry / exponential backoff）
- [ ] Tool 执行超时保护（asyncio.timeout）
- [ ] Tool 返回异常时的优雅降级
- [ ] 用户输入校验（空输入 / 超长输入 / 恶意注入）
- [ ] 每个错误场景写一个对应测试

#### 1.2 边界情况（30min）
- [ ] 极端输入测试（超长文本 / 特殊字符 / 纯数字）
- [ ] 并发安全性（如果需要）
- [ ] 状态一致性验证

#### 1.3 日志与可观测性（30min）
- [ ] 添加结构化日志（`logging` 模块，记录每一步的 input/output/latency）
- [ ] 打印 State 在各 Node 之间的变化（调试用）
- [ ] Token 消耗统计（每个 Node + 总计）
- [ ] 关键指标埋点：LLM 调用次数 / Tool 调用次数 / 总耗时

### 2. Demo 制作（40min）
#### 2.1 准备 Demo 场景
- [ ] 选 2-3 个最能展示项目亮点的 Demo 场景
- [ ] 准备输入数据和预期输出

#### 2.2 录制
- [ ] 用终端录制工具（如 asciinema / terminalizer）或直接录屏
- [ ] 时长控制：每个 Demo 1-2 分钟
- [ ] 录制完成后保存到 `docs/demo/` 目录

### 3. README 撰写（50min）
参考优秀开源项目的 README 结构：
```markdown
# 项目名称
一句话描述 + 徽章（Python版本 / License）

## 📸 Demo（放 GIF/截图）

## 🎯 核心功能
- bullet points

## 🏗️ 架构
（画 ASCII 图或 Mermaid 图展示 Agent 工作流）

## 🚀 快速开始
### 环境要求
### 安装
### 配置 API Key
### 运行

## 🧪 示例
（展示输入→输出）

## 📁 项目结构

## 🔧 技术栈

## 📝 License
```
- [ ] 完成 README
- [ ] 让 AI 帮忙 review README（"假设你是一个面试官，看完这个 README 你还有什么疑问？"）

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- Agent 评估：指标体系 + LangSmith/Braintrust 实操
- 为 Portfolio 项目建立自动化评估 Pipeline

## ⏱️ 实际时间分配
- 错误处理：___min
- 日志+监控：___min
- Demo 制作：___min
- README：___min
