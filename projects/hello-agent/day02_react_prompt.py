"""
Day 02 — ReAct Prompting 练习
ReAct = Reasoning（推理）+ Acting（行动）
核心循环：Thought → Action → Observation → Thought → ... → Final Answer

这是所有 AI Agent 框架的底层逻辑，面试必问。
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

llm = ChatOpenAI(
    model="qwen3.7-max",
    base_url=os.getenv("QWEN_BASE_URL"),
    api_key=os.getenv("QWEN_API_KEY")
)

# ============================================================
# 手写 ReAct Prompt 模板
# 这个模板定义了 Agent 的"思考-行动"格式
# ============================================================

REACT_PROMPT = """你是一个能使用工具的 AI Agent。你的任务是逐步推理并解决用户的问题。

你可以使用以下工具：
- search(query: str) — 搜索互联网信息
- calculate(expression: str) — 计算数学表达式
- get_weather(city: str, date: str) — 查询天气

你必须严格按照以下格式输出，每次只输出一个步骤：

Thought: [你对当前情况的思考，决定下一步做什么]
Action: [工具名称]
Action Input: [传给工具的参数]
Observation: [工具返回的结果]

... (重复 Thought/Action/Action Input/Observation 直到找到答案)

Thought: 我已经有了足够的信息来回答问题
Final Answer: [最终回答]

现在开始！
用户问题：{question}
"""

# ============================================================
# 模拟工具（因为没有真的 API，用字典模拟）
# ============================================================
def search(query: str) -> str:
    """模拟搜索引擎"""
    fake_db = {
        "杭州": "杭州是浙江省省会，著名景点有西湖、灵隐寺、浙江自然博物馆。",
        "室内景点": "杭州室内景点包括：浙江自然博物馆（免费）、杭州大厦购物城、中国丝绸博物馆。",
    }
    return fake_db.get(query, f"未找到关于'{query}'的信息")

def calculate(expression: str) -> str:
    """模拟计算器"""
    try:
        return str(eval(expression))
    except:
        return "计算错误"

def get_weather(city: str, date: str) -> str:
    """模拟天气查询"""
    return f"{city} {date}天气：阴天，18°C-24°C，下午有阵雨，湿度75%"


# ============================================================
# 运行 ReAct 循环
# 注意：这里我们手动模拟 Observation，
# 因为真正的 Agent 会在 LangGraph（Day 08-09）中实现自动循环
# ============================================================

question = "杭州今天适合出去玩吗？"

# 第一步：把 ReAct Prompt + 用户问题发给模型
prompt = REACT_PROMPT.format(question=question)
print("=== 发给模型的 System Prompt（ReAct 格式定义）===")
print(prompt)
print()

# 第二步：模型输出 Thought + Action
step1 = llm.invoke(prompt)
print("=== Agent 第 1 步输出 ===")
print(step1.content)
print()

# 第三步：手动模拟 Observation + 继续
# （后面的 Day 09 会用代码自动完成这个循环）
print("=== 如果这是真正的 Agent 循环 ===")
print("接下来应该：")
print("1. 解析模型输出的 Action 和 Action Input")
print("2. 执行对应的工具函数")
print("3. 把结果作为 Observation 追加到对话历史")
print("4. 再次调用模型，让它基于 Observation 继续思考")
print("5. 重复直到模型输出 Final Answer")

# ============================================================
# 🧪 你的练习
# 1. 换一个问题试试（比如"北京今天多少度，适合跑步吗？"）
# 2. 观察模型输出的格式是否严格遵循 Thought → Action → Observation
# 3. 想想看：如果工具执行出错了，模型该怎么知道并重试？
#    （这是 Day 03 Function Calling 的核心内容）
# ============================================================
