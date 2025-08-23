# 2. Architecture Details

## 2.1 Frontend
- Single-page Gradio `Blocks` built by `create_interface()`.
- Event wiring: Button `.click()` calls `invoke_agent()`.
- State: conversation memory via LangGraph-managed session.

## 2.2 Backend
- Service: `src/service.py` accepts UI calls, invokes agent, shapes response.
- Agent: ReAct loop with thought–action–observation in `src/agent/agent.py`.
- Tools: `documentation_search`, `code_generator` in `src/agent/tools.py`.
- Client: `src/client/mcp_client.py` for Context7 MCP server.

## 2.3 Project Structure
```plaintext
code4all/
├── README.md
├── requirements.txt
├── main.py
└── src/
    ├── agent/
    │   ├── agent.py
    │   └── tools.py
    ├── client/
    │   └── mcp_client.py
    ├── ui/
    │   └── interface.py
    ├── service.py
    └── data_models.py
```
