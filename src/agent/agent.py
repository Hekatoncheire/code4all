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
            ("system", """You are an autonomous AI assistant specialized in helping developers with programming questions and technical documentation.

            You have access to documentation search tools that can help you find accurate, up-to-date information. Use your judgment to determine:
                - When to search for documentation vs. using your existing knowledge
                - Which tools to use and in what order
                - How much information you need before providing an answer
                - Whether to combine multiple sources or focus on specific areas

            Your goal is to provide helpful, accurate responses. You decide the best approach for each question based on:
                - The complexity and specificity of the question
                - Whether current documentation would be beneficial
                - The user's apparent level of expertise
                - The context of the ongoing conversation

            Available tools:
                - resolve-library-id
                - get-library-docs

            Trust your reasoning and adapt your approach to best serve each user's needs."""),
            ("placeholder", "{messages}"),
        ])

        
        graph = create_react_agent(
            model=self.model,
            tools=self.tools,
            prompt=prompt,
            checkpointer=self.checkpointer,
        )
        return graph