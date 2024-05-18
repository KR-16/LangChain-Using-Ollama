from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv() ### initializing the environment variables

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Simple API Server"
)

add_routes(
    app,
    Ollama(),
    path="/ollama"
)
model = Ollama(model="llama3")

prompt1 = ChatPromptTemplate.from_template("Write me an Essay on {topic} in 200 words")
prompt2 = ChatPromptTemplate.from_template("Write a poem on {topic} in 200 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|model,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)