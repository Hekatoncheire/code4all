# 4. Core Workflows

## 4.1 ReAct Agent Workflow
The core workflow follows the ReAct (Reasoning and Acting) pattern:

1. **User Input**: Query received via Gradio chat interface
2. **Memory Retrieval**: Agent retrieves existing conversation history from checkpoint
3. **ReAct Loop**: 
   - **Thought**: Agent reasons about the query and determines next action
   - **Action**: Agent selects and executes appropriate MCP tool
   - **Observation**: Agent processes tool output and continues reasoning
   - **Repeat**: Loop continues until final answer is reached
4. **Response**: Final answer streamed back to user interface

## 4.2 MCP Tool Integration
Documentation search workflow:

1. **Tool Selection**: Agent determines need for documentation lookup
2. **MCP Client**: Async call to Context7 MCP server
3. **Tool Execution**: Search performed against LangGraph documentation
4. **Result Processing**: Documentation chunks returned and integrated into reasoning

## 4.3 Multi-tool Resolution Flow
![Core workflow sequence](diagrams/core_workflow.png)
