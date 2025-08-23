# Tech Stack

This document summarizes the technologies used in Code4all. It builds on:
- `docs/architecture/01-overview.md`
- `docs/architecture/02-architecture-details.md`
- PRD: `docs/prd.md`

## Languages & Runtime
- Python 3.11.x (local execution)

## Core Libraries & Frameworks
- LangGraph — Agent graph and ReAct loop implementation
- Gradio — UI (Blocks) for user interaction
- Requests/HTTPX (TBD) — HTTP client for MCP server
- Logging — Python standard library `logging`

## Agent & Tools
- ReAct agent orchestrated by LangGraph
- Tools:
  - `documentation_search` — calls Context7 MCP server
  - `code_generator` — LLM-backed code snippet generation

## Models
- Open-source models only (no paid APIs), from Hugging Face where applicable
- Model selection is swappable per PRD NFR5

## Testing & Quality
- pytest — unit testing
- Black — code formatter (line length 100)
- isort — import sorter (profile black)
- Ruff (or Flake8 fallback) — linting

## Configuration & Secrets
- `.env` in repo root for secrets like `MCP_API_KEY`

## Packaging & Dependencies
- `requirements.txt` with pinned versions

## Execution
- CLI/entry: `python main.py` or `python -m src.app` for UI

## References
- See `02-architecture-details.md` for component layout
- See `06-dev-and-next-steps.md` for local dev commands
