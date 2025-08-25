import asyncio
from typing import List
from langchain_core.tools import BaseTool, StructuredTool
from src.client.mcp_client import MCPClient


class ToolBox:
    def __init__(self, mcp_client: MCPClient | None = None):
        self.mcp_client = mcp_client
    
    async def documentation_search_tools(self) -> List[BaseTool]:
        return await self.mcp_client.get_tools()
    
    def _wrap_async_tool(self, async_tool: BaseTool) -> BaseTool:
        # Convert async MCP tools to sync for LangGraph compatibility
        def sync_invoke(**kwargs):
            try:
                return asyncio.run(async_tool.ainvoke(kwargs))
            except RuntimeError:
                # Handle case where event loop is already running
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(asyncio.run, async_tool.ainvoke(kwargs))
                    return future.result()
        
        return StructuredTool(
            name=async_tool.name,
            description=async_tool.description,
            args_schema=async_tool.args_schema,
            func=sync_invoke
        )
    
    async def tools(self) -> List[BaseTool]:
        async_tools = await self.documentation_search_tools()
        return [self._wrap_async_tool(tool) for tool in async_tools]