"""
Day 02 — Few-shot Prompting 练习
先理解：什么是 Few-shot？
你点菜时，如果服务员直接问"吃什么？"你可能会懵。但如果服务员说："比如你可以点红烧肉配米饭，或者清蒸鱼配馒头，或者蛋炒饭配紫菜汤——请问你想吃什么？"你瞬间就懂了。
Few-shot = 在 Prompt 里放几个示例，让模型照猫画虎。
核心概念：在 Prompt 中放入示例，让模型按照示例的格式和逻辑回答新问题
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

llm = ChatOpenAI(
    model="qwen3.7-max",
    base_url=os.getenv("QWEN_BASE_URL"),
    api_key=os.getenv("QWEN_API_KEY")
)

# ============================================================
# 任务：论文研究方向分类器
# 给模型 3 个示例（论文标题 → 研究方向），让它分类新论文
# ============================================================

# ── 方法一：直接在 User Message 中手写示例 ──
# 最原始也最灵活的 Few-shot 方式

user_message = """
请根据以下论文标题，判断它属于哪个研究方向。
研究方向可选：NLP（自然语言处理）、CV（计算机视觉）、RL（强化学习）、System（系统）、Agent

示例 1：
论文标题：Attention Is All You Need
研究方向：NLP

示例 2：
论文标题：Mastering Chess and Shogi by Self-Play
研究方向：RL

示例 3：
论文标题：MapReduce: Simplified Data Processing on Large Clusters
研究方向：System

现在请分类以下论文：
论文标题：Training Language Models to Follow Instructions with Human Feedback
研究方向：
"""

response = llm.invoke(user_message)
print("=== 方法一：手写 Few-shot ===")
print(response.content)
print()

# ============================================================
# 方法二：用 LangChain 的 ChatPromptTemplate 组织 Few-shot
# 好处：示例和输入分离，方便批量替换不同的示例和测试标题
# ============================================================

from langchain_core.prompts import ChatPromptTemplate

# 把示例写成结构化数据（方便增删改）
examples = [
    {"title": "Attention Is All You Need",              "field": "NLP"},
    {"title": "Mastering Chess and Shogi by Self-Play", "field": "RL"},
    {"title": "MapReduce: Simplified Data Processing",  "field": "System"},
]

# 把示例拼成文本
example_text = ""
for i, ex in enumerate(examples, 1):
    example_text += f"示例 {i}：\n论文标题：{ex['title']}\n研究方向：{ex['field']}\n\n"

# 用 Prompt 模板：system 设定规则，user 放入示例 + 待分类标题
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个论文研究方向分类器。可选方向：NLP、CV、RL、System、Agent。只输出方向名称。"),
    ("user", "{examples}\n现在请分类以下论文：\n论文标题：{title}\n研究方向：")
])

chain = prompt | llm
result = chain.invoke({
    "examples": example_text,
    "title": "Training Language Models to Follow Instructions with Human Feedback"
})
print("=== 方法二：ChatPromptTemplate 组织 Few-shot ===")
print(result.content)
print()

# ============================================================
# 🧪 你的练习
# 1. 把 examples 列表换成你博士方向相关的 3 篇论文
# 2. 把 title 换成你想测试的论文
# 3. 看模型能不能正确分类（没有标准答案，看推理是否合理即可）
# ============================================================
