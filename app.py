from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv() ### initializing the environment variables

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

### prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Your are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)


### streamlit framework

st.title("CHATBOT USING LANGCHAIN AND OLLAMA")
input = st.text_input("Ask your Question")

### ollama LLama3 LLM
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


if input:
    st.write(chain.invoke({"question": input}))