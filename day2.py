import streamlit as st
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama

st.title('Welcome to My Streamlit App for OpenAI Chat')
st.markdown("""
This is a sample markdown
""")

openai_api_key = st.sidebar.text_input("open AI key")
name = st.text_input("Enter text", "here")
option = st.radio("Choose one option:", options = ["Option1", "Option2"], index=0)

value = st.slider("Enter a value: ", 0, 100, 20)
print(value)
print(option)

def gen_response(txt):
    llm = OpenAI(temperature = 0.7, openai_api_key=openai_api_key)
    st.info(llm(txt))

with st.form("Examp APP"):
    txt = st.text_area("Enter text:", "What does GPT stand for:")
    subm = st.form_submit_button("SUBMIT")
    if subm:
        gen_response(txt)
