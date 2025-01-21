import os
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint



api_key = os.getenv("HF_API")

os.environ["HF_API"]=api_key 
repo_id = "mistralai/Mistral-Nemo-Instruct-2407"


# checking LLM model runs well or not.
llm=HuggingFaceEndpoint(repo_id=repo_id,
                        max_new_tokens=100, 
                        temperature=0.7, 
                        huggingfacehub_api_token=api_key)


st.title("Questions & Answers Chatbot")
input = st.text_input("Search anythings...You want..")

if input:
    st.write(llm.invoke(input))

