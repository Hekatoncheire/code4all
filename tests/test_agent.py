import asyncio
from unittest.mock import Mock, AsyncMock
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

from src.agent.agent import Agent
from src.agent.tools import ToolBox
from src.client.mcp_client import MCPClient


class MockToolInput(BaseModel):
    query: str = Field(description="The search query")


def test_agent():
    """Simple smoke test for the agent."""
    mock_client = Mock(spec=MCPClient)
    mock_tool = StructuredTool(
        name="test-tool",
        description="A test tool", 
        args_schema=MockToolInput,
        func=lambda query: f"Mock result for: {query}"
    )
    mock_client.get_tools = AsyncMock(return_value=[mock_tool])
    
    toolbox = ToolBox(mcp_client=mock_client)
    
    tools = asyncio.run(toolbox.tools())
    
    mock_model = Mock()
    mock_model.name = "test-model"
    
    agent = Agent(model=mock_model, tools=tools)
    
    assert agent.model == mock_model
    assert len(agent.tools) == 1
    assert agent.graph is not None
