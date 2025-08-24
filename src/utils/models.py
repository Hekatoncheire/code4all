from typing import List
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