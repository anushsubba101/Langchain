from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGroq(model="llama-3.3-70b-versatile")
model2 = ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz} ',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chains = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chains | merge_chain

text = """ 
What is Data Science?
Last Updated : 16 Apr, 2026
Data science is the study of data used to extract meaningful insights for business decisions. It combines mathematics, computing and domain knowledge to solve real-world problems and uncover hidden patterns.

file.webpfile.webp
It processes raw data to address business challenges and predict future trends. For example, from large company datasets, data science can help answer questions like:

What do customer want?
How can we improve our services?
What will the upcoming trend in sales?
How much stock they need for upcoming festival.
Steps Involved
Data Collection: Gathering raw data from various sources, such as databases, sensors or user interactions.
Data Cleaning: Ensuring the data is accurate, complete and ready for analysis.
Data Analysis: Applying statistical and computational methods to identify patterns, trends or relationships.
Data Visualization: Creating charts, graphs and dashboards to present findings clearly.
Decision-Making: Using insights to inform strategies, create solutions or predict outcomes.
Increasing Demand
Decision-Making & Forecasting: Businesses analyze data to identify trends, reduce risks and predict future demand.
Efficiency & Optimization: Helps in saving time and resources by improving processes like supply chain and operations.
Personalization: Enables customized recommendations in platforms like e-commerce and marketing.
Fraud Detection & Security: Identifies unusual patterns in financial transactions to prevent fraud.
Healthcare Improvements: Supports early diagnosis using medical data and predictive models.
Marketing & Sentiment Analysis: Helps businesses understand customer behavior and public opinion through data insights.
Important Skills
Programming: Proficiency in programming languages like Python, R or SQL is crucial for analyzing and processing data effectively.
Statistics and Mathematics: A strong foundation in statistics and linear algebra helps in understanding data patterns and building predictive models.
Machine Learning: Knowledge of machine learning algorithms and frameworks is key to creating intelligent data-driven solutions.
Data Visualization: The ability to present data insights through tools like Tableau, Power BI or Matplotlib ensures findings are clear and actionable.
Data Wrangling: Skills in cleaning, transforming and preparing raw data for analysis are vital for maintaining data quality.
Big Data Tools: Familiarity with tools like Hadoop, Spark or cloud platforms helps in handling large datasets efficiently.
Non-Technical Skills: Critical thinking and communication help analyze data effectively and clearly explain insights to stakeholders.
"""
result = chain.invoke({'text':text})
print(result)