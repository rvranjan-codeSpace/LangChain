from langchain.chat_models import  init_chat_model
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import openai_key

gpt_turbo_llm = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_key, temperature=0.6)
system_msg= SystemMessage(content="you are a java-Selenium AI assistant")
print(type(system_msg))
print(system_msg)
output = gpt_turbo_llm.invoke([
    SystemMessage(content="you are a java-Selenium AI assistant"),
    HumanMessage(content="what is explicit wait")
])
print(type(output))
print(output)

