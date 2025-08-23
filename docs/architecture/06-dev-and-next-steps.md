# 6. Development & Next Steps

## 6.1 Local Development
- Python 3.11.x
- Setup: `python3.11 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
- Run: `python3 main.py`
- Test: `pytest`

## 6.2 Environment
`.env` in repo root:
```env
MCP_API_KEY="your_key_here"
```

## 6.3 Next Steps
- Story 1.1: Project scaffolding & environment setup.
- Define MCP server API specifics (auth, endpoints, schemas).
- Add PRD story for conversation memory implementation/testing under Epic 1.
