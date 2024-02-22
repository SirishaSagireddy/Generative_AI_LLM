from langchain_community.llms import HuggingFaceHub

from dotenv import load_dotenv

load_dotenv() # take environment variables from .env

import streamlit as st

import os

# Function to load HuggingFace model and get response

def get_huggingface_response(question):
    llm_huggingface = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":0, "max_length":1000})
    response = llm_huggingface(question)
    return response
# Initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

submit = st.button("Ask the Question")

input = st.text_input("Input: ", key="input")
response = ""

# If ask button is clicked

if submit:
    response = get_huggingface_response(input)
    st.subheader("The Response is")
    st.write(response)
