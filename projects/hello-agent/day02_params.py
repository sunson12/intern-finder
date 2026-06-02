"""
Day 02 — 参数调优实验
核心参数：Temperature（创造性）、Top-P（候选范围）、Stop Sequence（停止条件）

面试金句：
"Temperature 控制输出的随机性——0 是完全确定性，1 是高度随机。
 Agent 的 Planning 阶段用低温（0-0.3）保证逻辑一致性，
 创意生成阶段用高温（0.7-1.0）保证多样性。"
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# ============================================================
# 1. Temperature 实验
# ============================================================
# Temperature = 0   → 每次输出几乎一样（最确定）
# Temperature = 0.7 → 有一定随机性（推荐值）
# Temperature = 1.5 → 天马行空，可能胡言乱语

prompt = "用一句话描述春天的西湖"

print("=" * 60)
print("实验 1：Temperature 对输出的影响")
print("同一个 Prompt，不同 Temperature，各跑 3 次")
print("=" * 60)

for temp in [0.0, 0.7, 1.5]:
    print(f"\n── Temperature = {temp} ──")
    for i in range(3):
        llm = ChatOpenAI(
            model="deepseek-v4-pro",
            base_url=os.getenv("DEEPSEEK_BASE_URL"),
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            temperature=temp,
        )
        resp = llm.invoke(prompt)
        # 只显示前 60 个字
        text = resp.content.replace("\n", " ")
        print(f"  第{i+1}次：{text[:60]}...")

# ============================================================
# 2. Temperature 在 Agent 场景中的最佳实践
# ============================================================
print("\n" + "=" * 60)
print("实验 2：Agent 不同阶段该用什么 Temperature？")
print("=" * 60)

# Planning（规划）：需要逻辑严密 → 低温
# Reasoning（推理）：需要逻辑严密 → 低温
# Creative（创意生成）：需要多样性  → 高温
# Tool Calling（工具调用）：需要精确 → 低温

planning_prompt = '你是一个 AI Agent。用户问"帮我规划一个杭州三日游"。请列出你的执行步骤。'

for temp, label in [(0.0, "低温 0.0（Planning 用）"), (0.7, "中温 0.7（通用）")]:
    llm = ChatOpenAI(
            model="deepseek-v4-pro",
            base_url=os.getenv("DEEPSEEK_BASE_URL"),
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            temperature=temp,
        )
    resp = llm.invoke(planning_prompt)
    print(f"\n{label}：")
    print(resp.content[:200])

# ============================================================
# 3. Stop Sequence 实验
# ============================================================
print("\n" + "=" * 60)
print("实验 3：Stop Sequence — 让模型在指定位置停止")
print("=" * 60)

stop_prompt = """列出 5 个 AI Agent 框架的名称和一句话描述：
1. LangGraph"""

# 不加 stop：模型会输出全部 5 个
llm = ChatOpenAI(
            model="deepseek-v4-pro",
            base_url=os.getenv("DEEPSEEK_BASE_URL"),
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            temperature=temp,
        )
print("\n不加 Stop Sequence：")
resp = llm.invoke(stop_prompt)
print(resp.content[:150])

# 加 stop=["3."]：模型输出到 "3." 之前就停止
llm_stop = ChatOpenAI(
            model="deepseek-v4-pro",
            base_url=os.getenv("DEEPSEEK_BASE_URL"),
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            temperature=temp,
            stop=["3."],  # 遇到 "3." 立即停止
        )

print("\n加了 stop=['3.']：")
resp_stop = llm_stop.invoke(stop_prompt)
print(resp_stop.content)

# 为什么 Agent 需要 Stop Sequence？
print("\n💡 Agent 中 Stop Sequence 的核心用途：")
print("  - ReAct 循环中，用 'Observation:' 作为停止条件")
print("  - 防止模型在工具调用后继续胡编")
print("  - 精确控制输出边界，方便程序解析")

# ============================================================
# 4. Top-P 实验（补充）
# ============================================================
print("\n" + "=" * 60)
print("实验 4：Top-P — 限制候选 Token 的范围")
print("=" * 60)
print("""
Top-P（也叫 Nucleus Sampling）：
  模型生成每个词时，从概率最高的词开始累加，
  直到累计概率达到 P 值为止，只从这些词中选。

  Top-P=0.1 → 只考虑概率最高的少数几个词 （极保守）
  Top-P=0.9 → 考虑大多数合理选项       （推荐）
  Top-P=1.0 → 所有词都考虑             （等同于关闭）

实际使用建议：
  ┌──────────────┬──────────┬──────────┐
  │ 场景          │ Temperature │ Top-P    │
  ├──────────────┼──────────┼──────────┤
  │ Tool Calling  │ 0        │ 0.1-0.3  │  ← 精度优先
  │ 事实问答      │ 0-0.3    │ 0.5-0.7  │
  │ 通用对话      │ 0.5-0.7  │ 0.8-0.9  │  ← 推荐默认值
  │ 创意写作      │ 0.7-1.0  │ 0.9-1.0  │  ← 多样性优先
  └──────────────┴──────────┴──────────┘

⚠️ 注意：一般只调 Temperature 就够了，Top-P 是精细控制手段。
""")

# ============================================================
# 🧪 你的练习
# 1. 把 Temperature=0 和 1.5 的输出对比截图保存
# 2. 思考：Agent 的 Function Calling 阶段为什么必须用 Temperature=0？
#    （提示：如果 Tool 名称被随机改了一个字会怎样？）
# 3. 面试被问"你是怎么调 Agent 参数的"时，用上面的表格回答
# ============================================================
