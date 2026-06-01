# Day 20 | 2026-06-20 | 周六 | 学习时长：3h

## 🎯 今日目标
- [ ] 为 Portfolio 项目编写 Dockerfile + docker-compose.yml
- [ ] 补充单元测试（核心逻辑覆盖率 > 60%）
- [ ] 项目文档完善（API 文档 + 架构图 + 注释）
- [ ] 最终检查：项目在全新环境能一键跑通

---

## 📚 学习内容

### 1. Docker 容器化（60min）
#### 1.1 编写 Dockerfile
```dockerfile
# projects/<项目名>/Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "8000"]
```
- [ ] 编写 Dockerfile
- [ ] `docker build -t <项目名> .`
- [ ] `docker run -p 8000:8000 <项目名>`
- [ ] 验证：浏览器访问 `localhost:8000` 能正常使用
- 踩坑记录：

#### 1.2 docker-compose.yml（如果需要 ChromaDB / Redis 等依赖）
- [ ] 编写 compose 文件，将 Agent + 依赖服务编排在一起
- [ ] `docker compose up` 一键启动全部服务

### 2. 单元测试（60min）
```python
# projects/<项目名>/tests/
```
#### 2.1 测试分级
- [ ] **单元测试**：每个 Tool 函数独立测试
- [ ] **集成测试**：LangGraph 单 Node 测试
- [ ] **端到端测试**：完整 Agent 流程测试（Mock LLM）

#### 2.2 Mock LLM 的技巧
- [ ] 用 FakeLLM / 固定返回值替代真实 LLM 调用
- [ ] 确保测试快速（全部在 10s 内完成）且可重复

#### 2.3 测试清单
- [ ] Tool 函数测试（至少 3 个 Tool）
- [ ] State Reducer 测试
- [ ] 条件路由测试（各分支都覆盖）
- [ ] 错误处理测试（LLM 调用失败 / Tool 超时 / 异常输入）
- 覆盖率：___%

### 3. 项目文档完善（40min）
- [ ] 更新 README：加入架构 Mermaid 图 + Demo 截图 + 安装/运行步骤
- [ ] 代码注释：每个 Node 函数有 docstring
- [ ] API 文档（如果用 FastAPI 暴露了 API）：访问 `/docs` 自动生成
- [ ] 添加一个 `CONTRIBUTING.md` 或 `ARCHITECTURE.md`

### 4. "一键跑通"验证（20min）
- [ ] 在新的终端窗口中 clone 项目（或删掉 venv 重装）
- [ ] 严格按 README 步骤操作
- [ ] 确认不需要任何额外的手动配置
- [ ] 修复 README 中的遗漏步骤

---

## 📊 Portfolio 项目最终检查
- [ ] README.md（含架构图 / Demo 截图 / 快速开始）
- [ ] Dockerfile + docker-compose.yml
- [ ] 单元测试（核心覆盖率 > 60%）
- [ ] 错误处理完善
- [ ] 日志 / Token 统计
- [ ] 全新环境一键跑通
- [ ] 项目已 Push 到 GitHub（Public）

---

## 💡 今日收获
1. 
2. 
3. 

## 🔮 明日计划
- 论文精读日：3 篇 Agent 核心论文深度阅读
- 写技术博客一篇（Portfolio 项目经验总结）
- 本周复盘

## ⏱️ 实际时间分配
- Docker：___min
- 测试：___min
- 文档：___min
- 验证：___min
