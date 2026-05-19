from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# creating the object of load_dotenv
load_dotenv()

# creating the object of chatopenai
model = ChatOpenAI(model="gpt-3.5-turbo-instruct", temperature=0, max_completion_tokens=10)

# invoking the method of chatopenai object
result = model.invoke("What is the capital of India?")

# printing the results
print(result.content)