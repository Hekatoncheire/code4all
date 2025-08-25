# 3. Data & APIs

## 3.1 Data Models
```python
from typing import List, Optional
from pydantic import BaseModel

class ContentBlock(BaseModel):
    type: str  # 'text' or 'code'
    content: str

class AgentStep(BaseModel):
    thought: str
    tool_name: str
    tool_input: str
    tool_output: str

class ConversationTurn(BaseModel):
    query: str
    final_answer: List[ContentBlock]
    intermediate_steps: List[AgentStep]
```

## 3.2 Internal Service API
```python
from src.utils.models import ConversationTurn

def invoke_agent(query: str) -> ConversationTurn:
    """Invoke the ReAct agent and return a structured result."""
    ...
```

## 3.3 External APIs (Context7 MCP)
- Purpose: Retrieve LangGraph documentation for grounding.
- Auth: `MCP_API_KEY` and `MCP_SERVER_URL` via environment variables.
- Protocol: MCP (Model Context Protocol) over HTTP transport.
- Tools: Documentation search and retrieval via async MCP client.
