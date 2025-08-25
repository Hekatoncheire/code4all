# 2. Architecture Details

## 2.1 Frontend
- Single-page Gradio `ChatInterface` built by `create_interface()`.
- Event wiring: Chat interface calls `invoke_agent()` for responses.
- State: conversation memory via LangGraph-managed session with InMemorySaver.

## 2.2 Backend
- Service: `src/service.py` accepts UI calls, manages singleton agent instance, provides response.
- Agent: ReAct loop with thought–action–observation in `src/agent/agent.py` using LangGraph.
- Tools: MCP documentation tools wrapped in `src/agent/tools.py`.
- Client: `src/client/mcp_client.py` for Context7 MCP server communication.
- Models: Pydantic data models in `src/utils/models.py`.

## 2.3 Project Structure
```plaintext
code4all/
├── README.md
├── requirements.txt
├── main.py                 # CLI/UI entry
├── .env.example            # Example env vars (do not commit secrets)
├── .gitignore              # Git ignore file
├── docs/
│   ├── prd.md
│   ├── project-brief.md
│   ├── epics/
│   ├── stories/
│   └── architecture/
├── src/
│   ├── agent/
│   │   ├── agent.py        # ReAct loop implementation
│   │   └── tools.py        # documentation_search, code_generator tools
│   ├── client/
│   │   └── mcp_client.py   # Context7 MCP client
│   ├── ui/
│   │   └── interface.py    # Gradio Blocks UI
│   ├── service.py          # Orchestration between UI and agent
│   └── utils/
│       └── models.py       # Pydantic models
│── tests/
    └── test_agent.py       # Agent test
```
