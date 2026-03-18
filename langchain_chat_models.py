from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 初始化模型
chat = ChatOllama(model="gemma3:4b")
name = "beck";
# 准备消息list   system/human/AI
messages = [
    SystemMessage(content="你是一名来自边塞的诗人"),
    HumanMessage(content="给我写一首宋词，句字数、平仄、押韵固定，必须有词牌名"),
    AIMessage(
        content=f"好的，{name},大漠西风卷铁衣，寒星冷月照征旗。万里关山人未老，霜天晓，角声吹断长安道。"),
HumanMessage(content="给我写一首宋词，句字数、平仄、押韵固定，必须有词牌名"),
    AIMessage(
        content=f"好的，{name},黄沙万里秋风老，落日孤烟绕。角声吹断雁南飞，满目关山霜冷、梦难归。"),
    HumanMessage(content=f"根据你上面回答的格式，再来一首宋词")
]

# 流式输出
for chunk in chat.stream(input=messages):
    print(chunk.content, end="", flush=True)
