"""
Day 02 — Chain of Thought (CoT) 练习
核心概念：让模型"一步一步思考"，把推理过程写出来，再给最终答案
效果：复杂推理任务的准确率大幅提升（数学、逻辑、代码分析等）

核心原理
模型生成 Token 是从左到右逐个预测的。如果你让它直接说答案，它没有机会"回头检查"。
但如果你让它写步骤，写步骤 1 时产生的 Token 会作为步骤 2 的上下文——相当于模型在用自己的输出给自己搭梯子。
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

# ============================================================
# 对比实验：同一个问题，不加 CoT vs 加 CoT
# ============================================================

question = "以下 Python 代码有一个隐藏的并发 Bug，在生产环境每 1000 次请求会触发一次死锁。请分析可能的原因并给出修复方案。"

# ── 实验 A：直接回答（不用 CoT）──
print("=== 实验 A：直接回答（无 CoT）===")
response_a = llm.invoke(question)
print(response_a.content)
print()

# ── 实验 B：Zero-shot CoT（只加一句"一步一步思考"）──
print("=== 实验 B：Zero-shot CoT（加了一句提示）===")
cot_question = question + "\n\n请一步一步思考，先给出步骤，再给出最终答案。"
response_b = llm.invoke(cot_question)
print(response_b.content)
print()
# ============================================================
# 🧪 你的练习
# 1. 对比实验 A 和 B 的输出——哪个更可信？
# 2. 把 question 换成你研究中的复杂推理问题，试一下 CoT 效果
# 3. 试试在 CoT 示例中加入"如果条件不够 → 指出缺少什么"
# ============================================================
