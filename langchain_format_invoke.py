from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import ChatPromptTemplate


template =PromptTemplate.from_template("所以这个是什么:{value}")

res =template.format(value="足球")
print(res,type(res))

res =template.invoke(input="篮球")
print(res,type(res))
