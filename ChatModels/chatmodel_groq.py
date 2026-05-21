from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# creating the llm 
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.9)

#creating the chat model invoke function
response = llm.invoke("what is the capital of china and india?")

print(response.content)