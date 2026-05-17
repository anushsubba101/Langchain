from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = [
    "kathmandu is the capital of Nepal",
    "paris it the capital of France",
    "Jhapa is a district"
]

vector=embedding.embed_documents(text)
print(str(vector))