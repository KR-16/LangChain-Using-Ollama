import requests
import streamlit as st

def getOllamaEssayResponse(input):
    response = requests.post(
        url="http://localhost:8000/essay/invoke",
        json={"input":{"topic": input}}
    )
    return response.json()["output"]

def getOllamaPoemResponse(input):
    response = requests.post(
        url="http://localhost:8000/poem/invoke",
        json={"input": {"topic": input}}
    )
    return response.json()["output"]

### streamlit framework

st.title("LANGCHAIN LLAMA3 WITH FASTAPI")
inputColumn1, inputColumn2 = st.columns(2)
outputColumn1, outputColumn2 = st.columns(2)
input_essay = inputColumn1.text_input("Write an Essay on ")
input_poem = inputColumn2.text_input("Write a Poem on ")


if input_essay:
    with outputColumn1:
        st.write(getOllamaEssayResponse(input_essay))

if input_poem:
    with outputColumn2:
        st.write(getOllamaPoemResponse(input_poem))