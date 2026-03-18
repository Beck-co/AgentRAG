from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_ollama import OllamaLLM

example_template = PromptTemplate.from_template("单词:{word},反义词:{antonym}")

example_data = [
    {"word": "大", "antonym": "小"},
    {"word": "上", "antonym": "下"}
]
few_shot_prompt = FewShotPromptTemplate(
    example_prompt=example_template,
    examples=example_data,
    prefix="给出给定词的反义词，有如下示例",
    suffix="基于示例告诉我：{input_word}的反义词是？",
    input_variables=['input_word']
)

prompt_text = few_shot_prompt.invoke(input={"input_word": "右"}).to_string()
# print(prompt_text)
model = OllamaLLM(model="gemma3:4b")
print(model.invoke(input=prompt_text))

