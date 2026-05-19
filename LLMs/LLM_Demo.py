from langchain_openai import OpenAI
from dotenv import load_dotenv

# envoking dotenv
load_dotenv()

# creating the LLM(Open ai) object
LLM = OpenAI(model="gpt-3.5-turbo-instruct")

# invoking methotd of LLM object
result = LLM.invoke("What is the capital of India?")

print(result)

# dont used that much now a days