from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents =[
    "The capital of China is Beijing.",
    "The capital of France is Paris.",  
    "The capital of Japan is Tokyo."
]

# creatig the embedding model
embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

# creating the embedding for the documents
embedding_creation = embedding.embed_documents(documents)
# printing them
print(str(embedding_creation))