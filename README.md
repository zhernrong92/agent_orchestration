# 🧠 Role-Based AI Agent Examples

This repository demonstrates multiple ways to implement a role-based AI agent pipeline using:

- 🧩 [CrewAI](https://github.com/joaomdmoura/crewAI) — for role-based agent orchestration
- 🔄 [LangGraph](https://github.com/langchain-ai/langgraph) — for stateful, multi-step workflows
- 🪶 Plain Python — lightweight, no external orchestration

## 💡 Use Case

A **researcher agent** performs a simulated search on LLM trends.  
A **writer agent** summarizes the findings into a paragraph.

---

## 🗂️ Folder Structure
```
.
├── agents_config.py # Role, goal, and prompt metadata
├── prompts.py # Reusable task prompt templates
├── tools.py # Example tools (e.g., dummy search)
├── run_with_crewai.py # CrewAI orchestration example
├── run_with_langgraph.py # LangGraph state machine example
├── run_without_crewai.py # Plain Python agent chaining
├── requirements.txt # Dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://gitlab.com/your-namespace/your-repo-name.git
cd your-repo-name
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set OpenAI API Key
```bash
export OPENAI_API_KEY=sk-...
```

## 🧪 Run Examples
### CrewAI
```bash
python run_with_crewai.py
```

### LangGraph
```bash
python run_with_langgraph.py
```

### Plain Python (No Orchestration)
```bash
python run_without_crewai.py
```


## 🛠️ Customize
1. Modify agents_config.py to change agent roles and goals

2. Update tools.py to integrate real tools or RAG pipelines

3. Extend with memory, file I/O, or async workflows