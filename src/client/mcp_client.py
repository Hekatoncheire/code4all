from typing import List
import asyncio
import os
from dotenv import load_dotenv
from langchain_core.tools import BaseTool, StructuredTool
from urllib.parse import urlencode
from langchain_mcp_adapters.client import MultiServerMCPClient


class MCPClient:
    def __init__(self, server_url: str, api_key: str | None = None):
        self.url = f"{server_url}?{urlencode({"api_key": api_key})}"
    
    async def get_tools(self) -> List[BaseTool]:
        mcp_client = MultiServerMCPClient({
            "context7": {
                "url": self.url,
                "transport": "streamable_http",
            }
        })
        return await mcp_client.get_tools()