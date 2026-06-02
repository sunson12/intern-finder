"""
Day 02 — Token 机制深入
Token 是 LLM 的"计价单位"和"理解单位"
理解 Token 才能控制成本、设计 Prompt、选择模型
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-v4-pro",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
)

import tiktoken

# 加载 GPT-4 的编码器
enc = tiktoken.encoding_for_model("gpt-4")

def estimate_cost(input_tokens: int, output_tokens: int,
                  input_price_per_m: float = 3.0,
                  output_price_per_m: float = 6.0):
    """估算一次 API 调用的费用（单位：元）"""
    input_cost = input_tokens / 1_000_000 * input_price_per_m
    output_cost = output_tokens / 1_000_000 * output_price_per_m
    return input_cost + output_cost

result = llm.invoke(f'解释一下什么是token')
print(f"回答：{result.content[:50]}...")
meta = result.response_metadata
tu = meta['token_usage'] if 'token_usage' in meta else meta['usage']
prompt_usage = tu.get('prompt_tokens')
out_usage = tu.get('completion_tokens')

cost = estimate_cost(prompt_usage, out_usage)
print(cost)

# ============================================================
# 6. Context Window（上下文窗口）
# ============================================================
# 每个模型有最大 Token 限制，超过就报错
# DeepSeek-V3: 128K Tokens ≈ 一本《三体》的篇幅
# GPT-4o: 128K Tokens
# Claude: 200K Tokens
#
# Agent 场景中，ReAct 循环每步都在消耗 Context Window：
#   Step 1: Prompt(500) + Thought(200) + Observation(500) = 1200
#   Step 2: 以上全部(1200) + Thought(200) + Observation(500) = 1900
#   Step 3: 1900 + 200 + 500 = 2600
#   ...
#   10 步后轻松上万 Token ← 这是 Agent 的核心成本问题

# ============================================================
# 🧪 你的练习
# 1. 用 tiktoken.encode("你博士论文的标题") 数一下多少 Token
# 2. 改 estimate_cost 里的价格为你用的模型真实价格，算一笔账
# 3. 思考：如果 Agent 平均 5 步完成任务，每步 2000 Token
#    一天 100 个用户，一个月要花多少钱？
# ============================================================
# ans: 5 * 2000 * 100 = 1000000token 一天 4块钱，1个月120块钱