from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model , parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'Explanation': RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)
print(final_chain.invoke({'topic':'football'}))