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

## 3.2 Data Contracts (External Docs Chunks)
```python
from typing import TypedDict, Optional

class DocumentChunk(TypedDict):
    content: str
    source: Optional[str]
    score: Optional[float]
```

## 3.3 Internal Service API
```python
from src.data_models import ConversationTurn

def invoke_agent(query: str, session_id: str) -> ConversationTurn:
    """Invoke the ReAct agent and return a structured result."""
    ...
```

## 3.4 External APIs (Context7 MCP)
- Purpose: Retrieve LangGraph documentation for grounding.
- Auth: `MCP_API_KEY` via environment (.env).
- Endpoints / Rate limits / Schemas: TBD.
