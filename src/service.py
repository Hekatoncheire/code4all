import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from src.agent.agent import Agent
from src.utils.models import ConversationTurn
from src.client.mcp_client import MCPClient
from src.agent.tools import ToolBox

async def invoke_agent(query: str) -> ConversationTurn:
    load_dotenv()
    model = ChatMistralAI(model="codestral-2508", temperature=0)
    toolbox = ToolBox(mcp_client=MCPClient(os.getenv("MCP_SERVER_URL"), os.getenv("MCP_API_KEY")))
    tools = await toolbox.tools()
    agent = Agent(model=model, tools=tools)
    return agent.invoke(query)
