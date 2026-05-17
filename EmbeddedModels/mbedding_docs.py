from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",output_dimensionality=32)
documents = [
    "kathmandu is capital of Nepal",
    "There are 7 proviences",
    "Paris is the capital of France"
]
result = embeddings.embed_documents(documents)
print(str(result))