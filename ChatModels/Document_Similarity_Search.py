from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

# creating the embedding model
embedding = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query ="tell me about virat kohli"

doc_embeddings = embedding.embed_documents(documents)

query_embedding = embedding.embed_query(query)

# now creating the cosine similarty
# this will give the simialrity between the query and those lines
scores=cosine_similarity([query_embedding], doc_embeddings)[0]

index ,scores=sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print("Query is:", query)
print("Most similar document is:", documents[index])
print("Similarity score is:", scores)