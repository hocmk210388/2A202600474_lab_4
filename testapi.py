import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# llm = ChatOpenAI(model="gpt-4o-mini")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
print(llm.invoke("Xin chào?").content[0]['text'])