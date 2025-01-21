import os
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint

# Prompting
from langchain_core.prompts import PromptTemplate

# Storing the conversation in memory
from langchain.memory import ConversationBufferMemory

# chain morethan 1 prompt.
from langchain.chains.sequential import SequentialChain

#chaining all components
from langchain.chains.llm import LLMChain

 

api_key = os.getenv("HF_API")

os.environ["HF_API"]=api_key 
repo_id = "mistralai/Mistral-Nemo-Instruct-2407"




# prompting

first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

# Memory for savving the data/conversession.

person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
descr_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')


# LLM model from huggingface call direct through langchain hugginfaceEndpoint.
llm=HuggingFaceEndpoint(repo_id=repo_id,
                        max_new_tokens=500, 
                        temperature=0.7, 
                        huggingfacehub_api_token=api_key)


# chains
chain = LLMChain(
    llm=llm, prompt=first_input_prompt,verbose=True,output_key='person',memory=person_memory)


# Prompting

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="when was {person} born"
)

chain2 = LLMChain(
    llm=llm, prompt=second_input_prompt,verbose=True, output_key='dob',memory=dob_memory)


third_input_prompt=PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events happened around {dob} in the world")


chain3=LLMChain(llm=llm,prompt=third_input_prompt,verbose=True,output_key='description',memory=descr_memory)


# chaing all prompts together.

parent_chain=SequentialChain(
    chains=[chain,chain2,chain3],input_variables=['name'],output_variables=['person','dob','description'],verbose=True)


# streamlit framework

st.title("Celebratity Search Results")
input_text = st.text_input("Search the topic you want")

if input_text:
    st.write(parent_chain({'name':input_text}))

    with st.expander('Person Name'): 
        st.info(person_memory.buffer)

    with st.expander('Major Events'): 
        st.info(descr_memory.buffer)

