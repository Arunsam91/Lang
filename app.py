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


