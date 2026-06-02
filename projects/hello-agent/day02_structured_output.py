"""
Day 02 — 结构化输出（Structured Output）练习
核心概念：让模型输出固定格式的 JSON/Pydantic 对象，而不是自由文本
用途：当你需要程序解析模型输出时（填表单、调 API、入库）
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-v4-pro",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

# ============================================================
# 问题场景：你要解析一篇论文的信息
# ============================================================

paper_text = """
本文提出了一种基于多智能体强化学习的任务分配框架 MARL-TA。
实验在 50 个节点的集群上进行，任务完成时间平均缩短了 23%。
作者来自清华大学计算机系，发表于 NeurIPS 2025。
"""

# ============================================================
# 方法一：with_structured_output() — 最简单，推荐首选
# 用 Pydantic 定义输出格式，LangChain 自动处理 JSON Schema 注入
# ============================================================

from pydantic import BaseModel, Field
from typing import Optional

# 第一步：定义你想要的数据结构
class PaperInfo(BaseModel):
    """论文信息"""
    title_en: str = Field(description="英文论文标题或简称")
    method: str = Field(description="论文提出的核心方法名称")
    institution: str = Field(description="作者所属机构")
    venue: str = Field(description="发表的会议或期刊名称")
    year: Optional[int] = Field(default=None, description="发表年份")
    key_result: str = Field(description="论文的核心实验结果")

# 第二步：绑定到这个 LLM 实例
# ⚠️ 注意：with_structured_output() 依赖 API 的 response_format 参数
# DeepSeek / 部分国产模型不支持该参数 → 会报 400 BadRequestError
# 因此方法一仅供支持该特性的 API 使用（OpenAI / Qwen 官方 API 等）
# 下面方法二、方法三不依赖 API 参数，兼容所有模型 ↓
structured_llm = llm.with_structured_output(PaperInfo)

try:
    result = structured_llm.invoke(f"从以下文本中提取论文信息：\n{paper_text}")
    print("=== 方法一：with_structured_output() ===")
    print(f"类型：{type(result).__name__}")
    print(f"标题：{result.title_en}")
    print(f"方法：{result.method}")
    print(f"机构：{result.institution}")
    print(f"会议：{result.venue}")
    print(f"年份：{result.year}")
    print(f"结果：{result.key_result}")
    print()
except Exception as e:
    print(f"=== 方法一：with_structured_output() ===")
    print(f"❌ 当前模型不支持 response_format 参数，跳过方法一")
    print(f"   错误详情：{e}")
    print(f"   请使用下面的方法二或方法三 ↓")
    print()

# ============================================================
# 方法二：PydanticOutputParser — 更灵活（自定义 Prompt + 错误重试）
# 适合：需要在 Prompt 中融入更多上下文时
# ============================================================

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

parser = PydanticOutputParser(pydantic_object=PaperInfo)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个论文信息提取器。\n{format_instructions}"),
    ("user", "从以下文本提取信息：\n{text}")
])

# parser.get_format_instructions() 自动生成 JSON Schema 说明
chain = prompt | llm | parser

result2 = chain.invoke({
    "format_instructions": parser.get_format_instructions(),
    "text": paper_text
})
print("=== 方法二：PydanticOutputParser ===")
print(f"类型：{type(result2).__name__}")
print(f"提取结果：{result2.model_dump()}")
print()

# ============================================================
# 方法三：JsonOutputParser — 输出原始 dict
# 适合：数据结构简单、不想定义 Pydantic 类时
# ============================================================

from langchain_core.output_parsers import JsonOutputParser

# 只定义字段名和描述（文字形式）
json_parser = JsonOutputParser()
json_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个 JSON 数据提取器。输出以下格式的 JSON：\n"
               '{{"title": "论文标题", "year": 年份数字, "method": "方法名", "score": 创新性评分1-10}}'),
    ("user", "{text}")
])

json_chain = json_prompt | llm | json_parser
result3 = json_chain.invoke({"text": paper_text})
print("=== 方法三：JsonOutputParser ===")
print(f"类型：{type(result3).__name__}")
print(f"结果：{result3}")
print()

# ============================================================
# 🧪 你的练习
# 1. 把 paper_text 换成你自己最近读的一篇论文摘要，看提取准不准
# 2. 定义一个新的 Pydantic 类，提取 Python 函数的信息（函数名、参数、返回值、功能描述）
# 3. 思考：结构化输出 + Function Calling（Day 03）有什么联系？
#    （提示：Function Calling 本质就是模型输出结构化的工具调用请求）
# ============================================================
