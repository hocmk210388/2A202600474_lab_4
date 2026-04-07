from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

# ===== 1. Define State =====
class GraphState(TypedDict):
    user_input: str
    system_prompt: str
    response: str

# ===== 2. Init LLM =====
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# ===== 3. Node chatbot =====
def chatbot_node(state: GraphState):
    messages = [
        SystemMessage(content=state["system_prompt"]),
        HumanMessage(content=state["user_input"])
    ]
    
    res = llm.invoke(messages)
    
    return {"response": res.content}

# ===== 4. Build Graph =====
builder = StateGraph(GraphState)
builder.add_node("chatbot", chatbot_node)

builder.set_entry_point("chatbot")
builder.add_edge("chatbot", END)

graph = builder.compile()

# ===== 5. Chat loop =====
# system_prompt = "You are a helpful assistant in coding. Answer the user's questions about programming in a clear and concise manner."
system_prompt = """
You are a coding assistant.

- Only answer questions related to programming, software development, or computer science.
- If the user asks about anything outside of coding, politely refuse to answer.
- Keep answers clear, concise, and practical.
- When possible, include code examples.

If the question is not related to coding, respond with:
"Sorry, I can only help with programming-related questions."
"""
while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        break

    result = graph.invoke({
        "user_input": user_input,
        "system_prompt": system_prompt
    })

    print("Bot:", result["response"])