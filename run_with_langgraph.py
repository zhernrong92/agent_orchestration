from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from agents_config import AGENTS
from prompts import RESEARCH_PROMPT
from tools import dummy_search_tool
from typing import TypedDict

# Define state
class AgentState(TypedDict):
    input: str
    context: str
    summary: str

# Nodes
def researcher_node(state: AgentState) -> AgentState:
    # Simulate a search result (in real use case, use tool or call LLM)
    context = dummy_search_tool(state["input"])
    return {"input": state["input"], "context": context, "summary": ""}

def writer_node(state: AgentState) -> AgentState:
    llm = ChatOpenAI(model="gpt-4o").bind(system_message=AGENTS["writer"]["system_message"])
    summary = llm.invoke(f"{state['context']}")
    return {"input": state["input"], "context": state["context"], "summary": summary.content}

# Build LangGraph
def build_graph():
    builder = StateGraph(AgentState)
    builder.add_node("research", researcher_node)
    builder.add_node("write", writer_node)
    builder.set_entry_point("research")
    builder.add_edge("research", "write")
    builder.set_finish_point("write")
    return builder.compile()

if __name__ == "__main__":
    graph = build_graph()
    result = graph.invoke({"input": RESEARCH_PROMPT, "context": "", "summary": ""})
    print("\n✅ Final Output:\n")
    print(result["summary"])
