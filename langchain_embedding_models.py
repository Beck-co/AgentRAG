from langchain_ollama import OllamaEmbeddings
embed = OllamaEmbeddings(model="nomic-embed-text")

print(embed.embed_query("你好呀ollama"))
print(embed.embed_documents(["早上吃啥","晚上吃啥","中午吃啥"]))