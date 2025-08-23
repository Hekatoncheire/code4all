# Code4all - Autonomous, local-first coding assistant that helps developers work with LangGraph using a simple Gradio UI and an agentic workflow. Responses are grounded in documentation via an MCP client.

## Prerequisites
- Python 3.11.x

## Setup
```bash
python3.11 -m venv venv
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

## Run
```bash
python3 -m main.py
```
This launches the Gradio UI (Blocks) with a textbox to ask questions and panes for answers and logs.

## Tests
```bash
pytest -q
```

## Linting & Formatting
```bash
# Format
black .
isort .

# Lint
ruff .
```

## Project Structure (expected)
See `docs/architecture/09-source-tree.md`. Core components:
- UI: `src/ui/interface.py`
- Service: `src/service.py`
- Agent: `src/agent/agent.py`
- Tools: `src/agent/tools.py`
- MCP Client: `src/client/mcp_client.py`

## Architecture & Standards
- Overview: `docs/architecture/01-overview.md`
- Details: `docs/architecture/02-architecture-details.md`
- Dev & Next Steps: `docs/architecture/06-dev-and-next-steps.md`
- Coding Standards: `docs/architecture/07-coding-standards.md`
- Tech Stack: `docs/architecture/08-tech-stack.md`
- Source Tree: `docs/architecture/09-source-tree.md`

## Product Docs
- PRD: `docs/prd.md`
- Epic 1: `docs/epics/epic-1.md`
- Story 1.1: `docs/stories/story-1.1.md`

## Notes
- Open-source models only (no paid APIs) per PRD NFRs.
- Further agent/tool implementation is covered by subsequent stories in Epic 1.
