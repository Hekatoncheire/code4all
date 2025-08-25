# Code4all - Autonomous, local-first coding assistant that helps developers work with LangGraph

## Planning Decisions

### Strategic Approach
We adopted an **incremental, story-driven development methodology** structured around Epic 1 with four sequential stories (1.1-1.4). This approach prioritized:

- **MVP-first mindset**: Focus on core functionality before polish
- **Reproducible development**: Every step documented
- **Monolithic simplicity**: Single Python application to minimize complexity
- **Open-source commitment**: No paid APIs, using Mistral Codestral model

### Key Design Decisions
- **ReAct structure**: Chose ReAct agent pattern for autonomous reasoning vs. simple Retrieval-Augmented Generation (RAG)
- **LangGraph framework**: Selected for robust agent orchestration and built-in memory management
- **MCP integration**: Leveraged Model Context Protocol for standardized tool access to documentation
- **Gradio interface**: Prioritized developer experience with minimal, chat-focused UI
- **Memory persistence**: Implemented conversation state to support multi-turn interactions

### Development Philosophy
The planning emphasized **working prototype over comprehensive features**, ensuring each component could be validated independently before integration. This allowed rapid iteration while maintaining code quality through structured documentation and testing.

## Applied Architecture

### High-Level Design Principles
Code4all implements a **layered monolithic architecture** optimized for local development and easy deployment:

```
UI Layer (Gradio) → Service Layer → Agent Layer (ReAct) → Tool Layer (MCP)
```

### Core Architectural Choices

**ReAct Agent Pattern**: The system uses LangGraph's `create_react_agent` to implement the Reasoning-Acting loop:
- **Thought**: Agent analyzes the query and plans approach
- **Action**: Selects and executes appropriate documentation tools
- **Observation**: Processes results and continues reasoning until complete

**MCP Tool Integration**: Documentation access through Context7 MCP server provides:
- Standardized tool interface for LangGraph documentation
- Async communication for responsive user experience
- Grounded responses from authoritative sources

**Memory Management**: LangGraph's `InMemorySaver` maintains conversation context:
- Session-scoped memory for follow-up questions
- Persistent reasoning chains across interactions
- Lightweight state management without external dependencies

### Architectural Benefits
- **Modularity**: Clear separation between UI, service, agent, and tool layers
- **Extensibility**: New tools can be added without changing core agent logic
- **Maintainability**: Well-defined interfaces and single responsibility principle

## Core Logic Advantages

### Why ReAct Over Simple LLM Chains

**Autonomous Reasoning**: Unlike linear LLM chains, the ReAct agent can:
- **Adapt strategy dynamically** based on intermediate results
- **Use multiple tools in sequence** when needed for complex queries
- **Self-correct** by observing tool outputs and adjusting approach
- **Handle uncertainty** by gathering more information before responding

**Tool-Use Intelligence**: The agent demonstrates sophisticated tool selection:
- **Context-aware decisions** about when to search documentation vs. use existing knowledge
- **Multi-step problem solving** combining multiple documentation sources
- **Efficient resource usage** by determining optimal information gathering strategy

### Technical Implementation Benefits

**Memory-Aware Conversations**: The checkpoint system enables:
- **Contextual follow-ups** without re-explaining previous concepts
- **Progressive disclosure** building on earlier interactions
- **Conversation continuity** across complex multi-turn discussions

**Structured Response Generation**: Enhanced agent prompting ensures:
- **Comprehensive answers** with context, code examples, and explanations
- **Consistent formatting** using markdown for readability
- **Actionable guidance** rather than just information retrieval

**Performance Optimization**: The architecture provides:
- **Lazy tool loading** only when documentation search is needed
- **Singleton agent pattern** preventing expensive re-initialization
- **Async streaming** for responsive user experience

### Comparison to Alternatives
- **vs. Simple RAG**: ReAct can reason about what information to retrieve and how to combine sources
- **vs. Function Calling**: More sophisticated reasoning loop with observation and adaptation
- **vs. Chain-of-Thought**: Grounds reasoning in actual tool outputs rather than just internal reasoning

## Prerequisites
- Python 3.13.x

## Setup
```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Environment
Copy the example file and set any required secrets:
```bash
cp .env.example .env
```
`.env` variables:
- `MCP_API_KEY` — API key for the Context7 MCP server
- `MCP_SERVER_URL` — URL of the Context7 MCP server

## Run
```bash
python3 main.py
```
or
```bash
python3 -m main
```

This launches the Gradio UI (ChatInterface) with a textbox to ask questions and panes for answers and logs.

## Tests
```bash
pytest
```

## Project Structure
See `docs/architecture/09-source-tree.md`. Core components:
- UI: `src/ui/interface.py`
- Service: `src/service.py`
- Agent: `src/agent/agent.py`
- Tools: `src/agent/tools.py`
- MCP Client: `src/client/mcp_client.py`

## Architecture & Standards
- Overview: `docs/architecture/01-overview.md`
- Details: `docs/architecture/02-architecture-details.md`
- Dev Setup: `docs/architecture/06-dev-setup.md`
- Coding Standards: `docs/architecture/07-coding-standards.md`
- Tech Stack: `docs/architecture/08-tech-stack.md`
- Source Tree: `docs/architecture/09-source-tree.md`

## Product Docs
- PRD: `docs/prd.md`
- Epic 1: `docs/epics/epic-1.md`

