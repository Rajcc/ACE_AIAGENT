This is Multi AI agent which has 4 Agents.
Problem:-Make an research specific ai agent which can find,analyse search paper.which also able to parapharase and explain certain topics.

Solution:-This Multi ai agent has research,analyse,write and google search agent.it can find papers,analyse them also if needed can explain certain topics using google search.

Architecture:-

<img width="4483" height="1472" alt="Untitled diagram-2025-11-29-081937" src="https://github.com/user-attachments/assets/604707ac-5f98-47db-96c4-76a388a17f30" />

# 🚀 AI Agent Orchestrator System

This project implements a modular **AI agent architecture** capable of intelligent task delegation, personalized interaction, and dynamic multi-agent execution.  
The central controller — **the Orchestrator** — decides how to route user input and ensures seamless communication between different system components.

---

## 🏗 System Architecture

The architecture consists of:

| Component | Responsibility |
|----------|----------------|
| **Orchestrator** | Core controller that manages the workflow |
| **Session Service** | Stores short-term conversation history |
| **Memory Bank** | Stores long-term user preferences & personal details |
| **Router** | Decides which agent should handle the user’s request |
| **Agents** | Specialized executors (Research, Analysis, Writer, Google Search etc.) |

---

## 📌 Responsibilities of Each Component

### 🔹 Session Service
- Holds **temporary / session-based context** in system RAM
- Contains information only relevant to the current conversation
- Used when the user says:
  - “continue”
  - “as I said before”
  - “refer to last topic”

### 🔹 Memory Bank
- Holds **long-term user information**, such as:
  - “My favourite movie is Interstellar”
  - “I like pizza”
  - “Remember that I prefer formal writing style”
- Triggered by keywords like:
  - `I like`, `I prefer`, `my favourite`, `remember this`, etc.
- Helps personalize the system across multiple sessions

### 🔹 Router
- Determines **which agent** should fulfill a user request
- Uses **router prompts** that describe the purpose & activation criteria of each agent
- **Fallback rule:**  
  If the Router cannot decide, it defaults to the **Google Search Agent**

### 🔹 Agents
Each agent performs a specific type of task using its own **prompt file**, for example:  
| Agent | Prompt File | Responsibility |
|-------|-------------|----------------|
| Research Agent | `research_prompt` | Find information, search the web, gather data |
| Analysis Agent | `analysis_prompt` | Perform reasoning, breakdowns, comparisons |
| Writer Agent | `writer_prompt` | Generate professional writing content |
| Google Search Agent | `google_search_agent` | Find results from internet when internal agents are insufficient |

All agents use **Groq LLM** to generate responses aligned with the respective prompt instructions.

---

## 🔁 Workflow — End-to-End

User Input → Orchestrator
├─► If input contains memory trigger → store in Memory Bank
├─► Else → store in Session Service
├─► Send processed query to Router
├─► Router (via Groq API + router prompt) returns best agent
├─► Orchestrator calls selected Agent
├─► Agent loads its prompt → Groq LLM generates response
└─► Orchestrator sends final answer to frontend

## 🌟 Why This Architecture?

| Benefit | Reason |
|--------|--------|
| ⚡ Fast | Session context stored in RAM |
| 🧠 Personalized | Memory Bank keeps long-term user preferences |
| 🔌 Extensible | New agents can be added without changing core logic |
| 🧭 Autonomous | Router avoids manual switching between agents |

---

## 📍 Example Interaction

| User Message | System Behavior |
|--------------|----------------|
| “I love sci-fi movies” | Memory Bank stores user preference |
| “Continue from the last topic” | Session Service provides previous conversation |
| “Search latest news on AI” | Router selects Research / Google Search agent |
| “Rewrite this paragraph professionally” | Router selects Writer Agent |


