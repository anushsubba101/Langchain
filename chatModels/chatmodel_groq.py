from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile",temperature=1)

result = model.invoke("suggest me 5 nepali male names")

print(result.content)