from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt
load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")  # ✅ model name required

paper_input = st.selectbox("Select Research Paper Name", [
    "Attention is all you need",
    "BERT: pre-training of Deep Bidirectional Transformers",
    "GPT-3: language models are few-shot learners",
    "Diffusion models beat GANs on Image Synthesis"
])
style_input = st.selectbox("Select explanation style", [
    "Beginner-friendly", "Technical", "Code-Oriented", "Mathematical"
])
length_input = st.selectbox("Select explanation length", [
    "Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"
])

template = load_prompt('template.json')

if st.button('Summarize'):

    chain = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result.content)  # ✅ display in Streamlit UI