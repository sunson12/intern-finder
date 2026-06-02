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

question = "一个项目原本计划 6 个人 10 天完成。做了 3 天后，增加了 2 个人。问实际提前了几天完成？"

# ── 实验 A：直接回答（不用 CoT）──
print("=== 实验 A：直接回答（无 CoT）===")
response_a = llm.invoke(question)
print(response_a.content)
print()

# ── 实验 B：Zero-shot CoT（只加一句"一步一步思考"）──
print("=== 实验 B：Zero-shot CoT（加了一句提示）===")
cot_question = question + "\n\n请一步一步思考，先写出计算步骤，再给出最终答案。"
response_b = llm.invoke(cot_question)
print(response_b.content)
print()

# ============================================================
# 方法二：Few-shot CoT — 给带推理过程的示例
# 适用场景：需要模型按特定格式输出推理步骤
# ============================================================

from langchain_core.prompts import ChatPromptTemplate

# 给一个带完整推理过程的示例
cot_example = """
问题：一项工程，5 个人 8 天可以完成。做了 2 天后，增加了 3 个人。问实际提前了几天完成？

一步一步思考：
步骤 1：总工作量 = 5 × 8 = 40（人·天）
步骤 2：前 2 天完成的工作量 = 5 × 2 = 10（人·天）
步骤 3：剩余工作量 = 40 - 10 = 30（人·天）
步骤 4：增加 3 人后，总人数 = 5 + 3 = 8 人
步骤 5：剩余工作需要的时间 = 30 ÷ 8 = 3.75 天
步骤 6：实际总天数 = 2 + 3.75 = 5.75 天
步骤 7：提前的天数 = 8 - 5.75 = 2.25 天
最终答案：提前了 2.25 天
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个数学解题助手。请按照示例的格式，一步一步推理，最后给出最终答案。"),
    ("user", "{example}\n\n现在请解答以下问题：\n{question}")
])

chain = prompt | llm
print("=== 实验 C：Few-shot CoT（给了一个示例）===")
response_c = chain.invoke({
    "example": cot_example,
    "question": question
})
print(response_c.content)

# ============================================================
# 🧪 你的练习
# 1. 对比实验 A 和 B 的输出——哪个更可信？
# 2. 把 question 换成你研究中的复杂推理问题，试一下 CoT 效果
# 3. 试试在 CoT 示例中加入"如果条件不够 → 指出缺少什么"
# ============================================================
