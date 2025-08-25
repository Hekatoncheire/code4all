from typing import List
from langchain_core.language_models.chat_models import BaseChatModel
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import BaseTool
from langchain_core.messages import HumanMessage, SystemMessage
from src.utils.models import ConversationTurn, ContentBlock

class Agent:
    def __init__(self, model: str | BaseChatModel, tools: List[BaseTool]):
        self.model = model
        self.tools = tools
        self.checkpointer = InMemorySaver()
        self.graph = self.build()
        self.config = {"configurable": {"thread_id": "1"}}
        
    def invoke(self, query: str):
        # Get existing messages from the checkpoint
        try:
            current_state = self.graph.get_state(config=self.config)
            past_messages = current_state.values.get("messages", []) if current_state.values else []
        except:
            past_messages = []
        
        # Append new human message to existing conversation
        messages = past_messages + [HumanMessage(content=query)]
        
        response = self.graph.invoke({"messages": messages}, config=self.config)
        
        # Extract the final message content
        messages = response.get("messages", [])
        final_content = messages[-1].content if messages else "No response"
        
        return ConversationTurn(
            query=query,
            final_answer=[ContentBlock(type="text", content=str(final_content))],
            intermediate_steps=[]
        )
    
    def build(self):
        from langchain_core.prompts import ChatPromptTemplate
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful assistant with access to documentation search tools. You MUST use your tools to answer ANY question about programming, libraries, or technical topics.

                        For ANY programming question:
                        1. Use the resolve-library-id tool first with the relevant library/framework name
                        2. Then use the get-library-docs tool with the returned library ID  
                        3. Use the documentation to provide a comprehensive answer

                        Your available tools: resolve-library-id, get-library-docs

                        Example: If asked "What is LangGraph?", call resolve-library-id with "LangGraph", then get-library-docs with the result."""),
            ("placeholder", "{messages}"),
        ])

        
        graph = create_react_agent(
            model=self.model,
            tools=self.tools,
            prompt=prompt,
            checkpointer=self.checkpointer,
        )
        return graph