# A minimal version using just prompts and functions
from agents_config import AGENTS
from prompts import RESEARCH_PROMPT, WRITE_PROMPT_TEMPLATE
from tools import dummy_search_tool

def researcher_agent(prompt):
    print(f"[Researcher: {AGENTS['researcher']['role']}] {prompt}")
    return dummy_search_tool(prompt)

def writer_agent(context):
    print(f"[Writer: {AGENTS['writer']['role']}] Writing summary...")
    return WRITE_PROMPT_TEMPLATE.format(context)

if __name__ == "__main__":
    research = researcher_agent(RESEARCH_PROMPT)
    final_output = writer_agent(research)
    print("\n✅ Final Output:\n")
    print(final_output)
