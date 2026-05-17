from langchain_ollama import ChatOllama
# No API key needed!
model = ChatOllama(model="llama3.2")

result = model.invoke("what is the capital of nepal?")
print(result)