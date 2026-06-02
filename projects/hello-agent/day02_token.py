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

# ============================================================
# 1. Token 是什么？
# ============================================================
# 模型不认字，只认数字。把文本切成小块，每块对应一个数字 → 这就是 Token
#
# 中英文切法完全不同：
#   英文 "Hello world" → ["Hello", " world"] → 2 个 Token
#   中文 "你好世界"     → ["你好", "世界"]    → 2 个 Token
#   但 "苹果"           → ["苹", "果"]       → 也可能 2 个 Token
#   英文擅长（空格分词），中文吃亏（逐字分，Token 数大约是字数的 1.5 倍）

# ============================================================
# 2. 用 tiktoken 数 Token
# ============================================================
# tiktoken 是 OpenAI 开源的 Token 计数库
# pip install tiktoken

import tiktoken

# 加载 GPT-4 的编码器
enc = tiktoken.encoding_for_model("gpt-4")

# 对比实验：同样意思，中英文 Token 数差多少？
cn_text = "人工智能正在改变软件开发的方式"
en_text = "Artificial intelligence is changing the way software is developed"

cn_tokens = len(enc.encode(cn_text))
en_tokens = len(enc.encode(en_text))

print("=== 中英文 Token 数对比 ===")
print(f"中文（{len(cn_text)}字）：{cn_tokens} Tokens")
print(f"英文（{len(en_text)}字符）：{en_tokens} Tokens")
print(f"结论：同样含义，中文 Token 数约是英文的 {cn_tokens/en_tokens:.1f} 倍")
print()

# ============================================================
# 3. 看 Token 是怎么切的
# ============================================================
print("=== Token 切分演示 ===")
sample = "LangChain is great for building AI Agents."
tokens = enc.encode(sample)
print(f"原文：{sample}")
print(f"Token IDs：{tokens}")
print(f"共 {len(tokens)} 个 Token")

# 把每个 Token ID 解码回文字，看切在哪
print("逐个 Token 解码：")
for tid in tokens:
    decoded = enc.decode([tid])
    print(f"  ID {tid:>6} → '{decoded}'")
print()

# ============================================================
# 4. 计算一次 API 调用的费用
# ============================================================
# DeepSeek V4 价格（大致）：
#   输入：约 ¥3 / 百万 Token
#   输出：约 ¥6 / 百万 Token
# （实际价格查官网，这里只是演示计算方法）

def estimate_cost(input_tokens: int, output_tokens: int,
                  input_price_per_m: float = 3.0,
                  output_price_per_m: float = 6.0):
    """估算一次 API 调用的费用（单位：元）"""
    input_cost = input_tokens / 1_000_000 * input_price_per_m
    output_cost = output_tokens / 1_000_000 * output_price_per_m
    return input_cost + output_cost

print("=== 费用估算示例 ===")
print("场景：一个 Agent 单次任务")
print(f"  System Prompt: 500 Tokens")
print(f"  历史对话: 2000 Tokens")
print(f"  当前问题: 100 Tokens")
print(f"  模型输出: 500 Tokens")
cost = estimate_cost(500 + 2000 + 100, 500)
print(f"  预估费用：¥{cost:.4f}（不到 1 分钱）")
print()

print("场景：一个 Agent 复杂任务（10 步循环）")
print(f"  每步输入 ~3000 Tokens × 10 步")
print(f"  每步输出 ~200 Tokens × 10 步")
cost2 = estimate_cost(3000 * 10, 200 * 10)
print(f"  预估费用：¥{cost2:.4f}")
print()

# ============================================================
# 5. 实战：用 LangChain 获取真实调用的 Token 消耗
# ============================================================
print("=== 真实调用 Token 消耗 ===")
response = llm.invoke("用一句话解释什么是 Token")
print(f"回答：{response.content[:50]}...")
print()

# response_metadata 里藏着本次调用的 Token 统计
meta = response.response_metadata
print(f"本次调用 Token 统计：")
# 不同模型返回的字段名略有不同，常见的是：
# token_usage / usage / usage_metadata
if "token_usage" in meta:
    tu = meta["token_usage"]
    print(f"  输入 Tokens：{tu.get('prompt_tokens', '?')}")
    print(f"  输出 Tokens：{tu.get('completion_tokens', '?')}")
    print(f"  总计 Tokens：{tu.get('total_tokens', '?')}")
elif "usage" in meta:
    u = meta["usage"]
    print(f"  输入 Tokens：{u.get('prompt_tokens', '?')}")
    print(f"  输出 Tokens：{u.get('completion_tokens', '?')}")
    print(f"  总计 Tokens：{u.get('total_tokens', '?')}")
else:
    print(f"  Token 数据在以下字段中：{list(meta.keys())}")
print()

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
# 7. 实验：从 100 Token 扩充到 1000 Token，输出质量怎么变？
# ============================================================
question = "什么是闭包（Closure）？"

# ── 版本 A：极简 Prompt（~30 Token）──
prompt_short = f"用一句话回答：{question}"
tokens_short = len(enc.encode(prompt_short))
response_short = llm.invoke(prompt_short)

# ── 版本 B：标准 Prompt（~100 Token）──
prompt_medium = f"""你是一个编程导师。请用简洁清晰的语言回答以下问题：
{question}

要求：给出定义 + 一个简单的代码示例。"""
tokens_medium = len(enc.encode(prompt_medium))
response_medium = llm.invoke(prompt_medium)

# ── 版本 C：冗长 Prompt（~500 Token）──
# 加入角色设定、详细要求、输出格式、一个示例
prompt_long = f"""你是一位拥有 15 年经验的资深 Python 架构师和技术导师。
你的讲解风格兼顾深度与通俗，既能让新手听懂，也能让有经验的开发者有所收获。

请回答以下问题：{question}

请严格遵循以下结构输出：
1. 【一句话定义】用最精炼的语言概括
2. 【为什么需要它】解释它解决了什么实际问题
3. 【核心机制】解释它背后的工作原理
4. 【代码示例】提供一个可直接运行的 Python 代码示例，带详细注释
5. 【常见误区】指出初学者最容易犯的 2 个错误理解
6. 【延伸思考】这个问题与以下概念的关联：作用域、装饰器、函数式编程

注意：
- 每个部分用标题分隔
- 代码示例必须完整可运行
- 控制总字数在 500 字以内"""
tokens_long = len(enc.encode(prompt_long))

response_long = llm.invoke(prompt_long)
# ── 对比输出 ──
print("=== 实验：Prompt 长度对输出质量的影响 ===")
print()
print(f"│  版本  │ Prompt Token 数 │ 输出长度（字） │ 输出质量观察           │")
print(f"│--------│-----------------│----------------│------------------------│")
print(f"│ A 极简 │ {tokens_short:>5}           │ {len(response_short.content):>3}            │ 一句话，可能过于笼统   │")
print(f"│ B 标准 │ {tokens_medium:>5}           │ {len(response_medium.content):>3}            │ 定义+示例，信息密度高   │")
print(f"│ C 冗长 │ {tokens_long:>5}          │ {len(response_long.content):>3}            │ 结构化，但 Token 成本高 │")
print()

print("── 版本 A（极简 Prompt ~30 Token）──")
print(f"Prompt 内容：{prompt_short}")
print(f"模型输出：{response_short.content[:200]}...")
print()

print("── 版本 B（标准 Prompt ~100 Token）──")
print(f"Prompt 内容：{prompt_medium}")
print(f"模型输出：{response_medium.content[:200]}...")
print()

print("── 版本 C（冗长 Prompt ~500 Token）──")
print(f"Prompt 内容（截取前 100 字）：{prompt_long[:100]}...")
print(f"模型输出（截取前 200 字）：{response_long.content[:200]}...")
print()

# ── 费用对比 ──
print("── 费用对比 ──")
cost_a = estimate_cost(tokens_short, len(enc.encode(response_short.content)))
cost_b = estimate_cost(tokens_medium, len(enc.encode(response_medium.content)))
cost_c = estimate_cost(tokens_long, len(enc.encode(response_long.content)))
print(f"版本 A（极简）：¥{cost_a:.6f}")
print(f"版本 B（标准）：¥{cost_b:.6f}")
print(f"版本 C（冗长）：¥{cost_c:.6f}")
print(f"版本 C 是版本 A 的 {cost_c/cost_a:.1f} 倍价格，但质量提升是否值这个差价？")
print()

# ============================================================
# 🧪 你的练习
# 1. 用 tiktoken.encode("你博士论文的标题") 数一下多少 Token
# 2. 改 estimate_cost 里的价格为你用的模型真实价格，算一笔账
# 3. 思考：如果 Agent 平均 5 步完成任务，每步 2000 Token
#    一天 100 个用户，一个月要花多少钱？
# ============================================================
