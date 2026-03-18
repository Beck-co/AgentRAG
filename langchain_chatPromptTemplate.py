from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import OllamaLLM

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人，可以作诗"),
        MessagesPlaceholder("history"),  # 后面读取history_data
        ("human", "请再来一首唐诗"),

    ]
)
history_data = [
    ("human", "请作一首边塞唐诗"),
    ("ai", "秦时明月汉时关，万里长征人未还。但使龙城飞将在，不教胡马度阴山。"),

    ("human", "再来一首豪迈风格的"),
    ("ai", "青海长云暗雪山，孤城遥望玉门关。黄沙百战穿金甲，不破楼兰终不还。")
]

prompt_text = chat_prompt_template.invoke({"history":history_data}).to_string()

model=OllamaLLM(model="gemma3:4b")
res=model.invoke(input=prompt_text)
print(res,type(res))