# Tech Stack

This document summarizes the technologies used in Code4all. It builds on:
- `docs/architecture/01-overview.md`
- `docs/architecture/02-architecture-details.md`
- PRD: `docs/prd.md`

## Languages & Runtime
- Python 3.11.x (local execution)

## Core Libraries & Frameworks
- LangGraph — Agent graph and ReAct loop implementation
- LangChain MistralAI — Mistral Codestral model integration
- Gradio — UI (ChatInterface) for user interaction
- MCP (Model Context Protocol) — Context7 server integration
- Pydantic — Data models and validation
- python-dotenv — Environment variable management

## Agent & Tools
- ReAct agent orchestrated by LangGraph
- MCP tools via Context7 server:
  - Documentation search and retrieval from LangGraph docs
- InMemorySaver for conversation checkpoints

## Models
- Mistral Codestral (open-source) via LangChain MistralAI
- Model selection is swappable per PRD NFR5

## Testing
- pytest — unit testing

## Configuration & Secrets
- `.env` in repo root for secrets like `MCP_API_KEY` and `MCP_SERVER_URL`

## Packaging & Dependencies
- `requirements.txt` with pinned versions for base dependencies

## Execution
- CLI/entry: `python3 main.py` or `python3 -m main` for Gradio UI

## References
- See `02-architecture-details.md` for component layout
- See `06-dev-setup.md` for local dev commands
