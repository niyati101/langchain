import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPEN_API_KEY']=apikey;

st.title('YouTube GPT')
prompt=st.text_input('plug in your prompt here')
