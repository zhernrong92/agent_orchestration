from crewai import CrewAgent, Task, Crew
from agents_config import AGENTS
from prompts import RESEARCH_PROMPT, WRITE_PROMPT_TEMPLATE
from tools import dummy_search_tool

# Define agents using config and tools
researcher = CrewAgent(
    role=AGENTS["researcher"]["role"],
    goal=AGENTS["researcher"]["goal"],
    backstory=AGENTS["researcher"]["backstory"],
    tools=[dummy_search_tool],
    verbose=True
)

writer = CrewAgent(
    role=AGENTS["writer"]["role"],
    goal=AGENTS["writer"]["goal"],
    backstory=AGENTS["writer"]["backstory"],
    verbose=True
)

# Tasks
task1 = Task(
    description=RESEARCH_PROMPT,
    expected_output="A list of 3 major LLM trends with short descriptions.",
    agent=researcher
)

task2 = Task(
    description="Summarize the research findings for a technical newsletter.",
    expected_output="A 1-paragraph summary.",
    agent=writer
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\n✅ Final Output:\n")
    print(result)
