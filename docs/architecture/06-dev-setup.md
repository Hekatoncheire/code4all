# 6. Development & Next Steps

## 6.1 Local Development
- Python 3.13.x
- Setup: `python3.13 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
- Run: `python3 main.py` or `python3 -m main`
- Test: `pytest`

## 6.2 Environment
`.env` in repo root:
```env
MCP_SERVER_URL="your_mcp_server_url"
MCP_API_KEY="your_mcp_api_key_here"

# Optional
MISTRAL_API_KEY="your_mistral_api_key_here"
```
