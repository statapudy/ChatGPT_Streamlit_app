import streamlit as st
import hmac
import pandas as pd
import random
import os
import time
import base64
import logging
import io
import config
from openai import OpenAi


st.set_page_config(layout="centered")

# Streamlit app layout
st.title(config.app_title)
st.caption(config.app_author)
# st.markdown(config.intro_para)
with st.expander("INSTRUCTIONS:"):
    st.markdown(config.instructions)
st.sidebar.title(config.sidebar_title)
with st.sidebar:
        with st.expander("Click here for instructions."):
            st.write(config.sidebar_instructions)

#if  'user_input' not in st.session_state:
 #   st.session_state['user_input']=''

#st.title('SABER Conference App')

#st.write('Hello World! This is practice for the final streamlit app')

#user_input = st.text_input('Enter a custom message:', 'Hello streamlit')
#if user_input:
#    st.session_state['user_input']=user_input

#st.write(f"You entered: {st.session_state['user_input']}")

#st.write('Customized Message:',user_input)
