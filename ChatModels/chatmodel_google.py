from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# creatig the object of load_dotenv
load_dotenv()

# creating the object of the googlegenerativeai chatmodel
Gmodel = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5, max_completion_tokens=100)

# now invoking th method of the google generative ai chatmodel
results = Gmodel.invoke("write 5 chinese local names")

print(results.content)