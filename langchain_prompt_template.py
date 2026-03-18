from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender}，你帮忙起个名字，简单回答"
)

# 调用.format方法注入信息
# prompt_text = prompt_template.format(lastname ="张", gender="女儿")
#
# model = OllamaLLM(model="gemma3:4b")
# res = model.invoke(input = prompt_text)
# print(res)
model = OllamaLLM(model="gemma3:4b")

chain = prompt_template | model

res = chain.invoke(input = {"lastname":"张","gender":"女儿"})
print(res)

