from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

chat_histroy = [
    SystemMessage(content='You are a helful AI assistant')
]

while True:
    user_input = input('You:')
    chat_histroy.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_histroy)
    chat_histroy.append(AIMessage(content=result.content))
    print("ZORDEX:",result.content)

print(chat_histroy)
