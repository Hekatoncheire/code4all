# 1. Overview

## 1.1 Introduction
Code4all is a local prototype of a ReAct-style agent that assists developers with LangGraph. It grounds answers in LangGraph documentation via the Context7 MCP server and exposes a simple Gradio UI with streaming responses. Conversational memory is included as short-term session state.

## 1.2 High-Level Architecture
- Monolithic Python app, runs locally.
- ReAct Agent (LangGraph) with MCP documentation tools via Context7 server
- LLM: Mistral Codestral (open-source)
- UI: Gradio Blocks with async streaming support
- Memory: Session-scoped conversation window managed by LangGraph InMemorySaver

### Diagram
![High-level architecture](diagrams/component_interaction.png)

## 1.3 Components (at a glance)
- UI Presentation Layer: `src/ui/interface.py`
- Agent Service Layer: `src/service.py`
- ReAct Agent: `src/agent/agent.py`
- Tools: `src/agent/tools.py`
- MCP Client: `src/client/mcp_client.py`
- Data Models: `src/utils/models.py`
