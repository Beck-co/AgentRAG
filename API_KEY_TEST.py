# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os

from openai import OpenAI

client = OpenAI(
    # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    base_url="http://localhost:11434/v1"
)
completion = client.chat.completions.create(
    model="gemma3:4b",
    messages=[
        # {"role": "system", "content": "你是python专家，写的代码非常优秀"},
        # {"role": "assistant", "content": "我是python代码助手，任何不动的代码都可以问我"},
        # {"role": "user", "content": "介绍一下python的学习指南"},
        {"role": "system", "content": "你是AI助手"},
        {"role": "user", "content": "小明有三只宠物"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有6只宠物"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "请问总共有多少只宠物呢？"},
    ],
    stream=True  # 开启流式输出功能
)

for chunk in completion:
    print(chunk.choices[0].delta.content, end=" ", flush=True)
