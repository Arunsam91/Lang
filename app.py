import streamlit as st

from PIL import Image



#opening the image

image = Image.open('img.jpg')



#displaying the image on streamlit app

st.image(image, caption='Future is here')


import streamlit as st




import os 


import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory


os.environ['OPENAI_API_KEY'] = st.secrets["apikey"]


st.title('🦜🔗 LangChain DEMO BY ARUN')
prompt = st.text_input('Type in your prompt here') 


title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='{topic}'
)



title_memory = ConversationBufferMemory(input_key='topic', memory_key=100000)




llm = OpenAI(temperature=0.7) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)




if prompt: 
    title = title_chain.run(prompt)
    st.write(title) 
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)
hide_streamlit_style = """
<style>
.css-hi6a2p {padding-top: 0rem;}
</style>

"""
st.title("Test")
if st.checkbox('Remove padding'):
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
