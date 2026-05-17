from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()  # add GROQ_API_KEY to .env

llm = ChatGroq(model="llama-3.3-70b-versatile")  # free & fast
result = llm.invoke("What is the capital of Nepal")
print(result.content)