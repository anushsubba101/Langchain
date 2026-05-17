from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2")
result = model.invoke("what it the capital of nepal")
print(result.content)