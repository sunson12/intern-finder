"""
Day 01 - 第一个 LangChain Hello World
使用 DeepSeek API（兼容 OpenAI 格式）
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # 自动读取项目根目录的 .env 文件

# DeepSeek 兼容 OpenAI 格式
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1",
)

# 最简单的调用
response = llm.invoke("用一句话解释什么是 AI Agent")
print("=== 基础调用 ===")
print(response.content)
print()

# LCEL 链式调用
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}，请用{style}风格回答问题。"),
    ("user", "{question}")
])

chain = prompt | llm | StrOutputParser()

result = chain.invoke({
    "role": "AI Agent 工程师",
    "style": "简洁",
    "question": "什么是 Function Calling？"
})
print("=== LCEL 链式调用 ===")
print(result)
