# 5. Quality & Operations

## 5.1 Security
- Load `MCP_API_KEY` and `MCP_SERVER_URL` from `.env`; never hardcode secrets.
- Environment variables managed via python-dotenv for secure configuration.

## 5.2 Performance
- Target P95 < 10s for agent responses.
- Singleton agent instance to maintain conversation state efficiently.
- InMemorySaver for fast checkpoint operations.

## 5.3 Testing Strategy
- Pytest unit tests for agent (see `tests/test_agent.py`).
- Mock-based testing for MCP client integration.
- Manual verification for Gradio UI.

## 5.4 Coding Standards
- PEP 8; Pydantic for models.
- Async/await patterns for MCP client operations.

## 5.5 Deployment
- Local-only for MVP; no cloud deployment required.
- Single Python process with Gradio server.

