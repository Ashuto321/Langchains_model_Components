from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# creating the embedding model
embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

# creating the embedding for the query
embedding_creation = embedding.embed_query("what is the capital of china?")

# printing them
print(str(embedding_creation))