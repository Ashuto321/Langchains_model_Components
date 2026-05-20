from langchain_huggingface import HuggingFaceEmbeddings

# creating the embeddding model
embedding = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

# taking a local text
text = "The capital of China is Beijing."

# creating the embedding for the local text
embedding_creation = embedding.embed_query(text)
print(str(embedding_creation))