# Project Brief: Code4all
## Executive Summary
Code4all is a ReAct agent application that provides LangGraph documentation assistance through MCP (Model Context Protocol) integration. It demonstrates agentic AI principles by using a thought-action-observation loop to answer developer questions about LangGraph directly from official documentation sources.

## Problem Statement
Developers learning LangGraph need quick access to accurate documentation while coding. Traditional approaches involve context-switching between development environments and web documentation, which slows development and breaks concentration.

## Proposed Solution
Code4all implements a ReAct agent using LangGraph that:
- Connects to Context7 MCP server for documentation access
- Uses thought-action-observation reasoning to answer queries
- Provides a simple Gradio chat interface
- Maintains conversation memory for follow-up questions

The agent specializes in LangGraph documentation, ensuring accurate and contextually relevant answers without hallucinations.

## Target Users

### Primary User: Python Developer Learning LangGraph
- **Profile:** Developer needing quick, accurate LangGraph documentation access
- **Workflow:** Currently switches between IDE and web documentation
- **Needs:** Fast, reliable answers without context-switching
- **Goals:** Implement LangGraph features efficiently

## Goals & Success Metrics

### Objectives
- Deliver a working ReAct agent demonstrating agentic principles
- Provide accurate documentation-grounded responses
- Maintain conversation context across interactions

### Success Metrics
- Agent successfully uses MCP tools to retrieve documentation
- Responses are grounded in official LangGraph documentation
- Conversation memory enables follow-up questions
- Application runs reproducibly from setup instructions

## Implementation Scope

### Core Features (Implemented)
- **ReAct Agent:** LangGraph-based agent with thought-action-observation loop
- **MCP Integration:** Connection to Context7 server for documentation tools
- **Conversational Memory:** InMemorySaver for conversation persistence
- **Gradio Interface:** Simple chat interface with example queries
- **Reproducible Setup:** Requirements file and clear instructions

### Architecture
- **Model:** Mistral Codestral (open-source) via langchain-mistralai
- **Agent Framework:** LangGraph create_react_agent
- **Memory:** InMemorySaver with thread-based persistence
- **Tools:** MCP client accessing resolve-library-id and get-library-docs
- **Interface:** Gradio ChatInterface

### Technical Implementation
The application consists of:
- `Agent` class implementing ReAct pattern with memory
- `MCPClient` for Context7 server integration
- `ToolBox` for async-to-sync tool wrapping
- Service layer for agent orchestration
- Gradio UI for user interaction

## Technical Considerations

### Platform Requirements
- Python 3.13+ environment
- Access to Context7 MCP server
- Local execution (no cloud deployment)

### Architecture
- **Repository:** Monorepo structure
- **Service:** Monolithic Python application
- **Integration:** Context7 MCP server, Mistral AI model
- **Security:** Environment variables for API keys

## Constraints & Assumptions

### Constraints
- Open-source models only (using Mistral Codestral)
- Local execution environment
- MCP server dependency for documentation access

### Key Assumptions
- Context7 MCP server provides reliable LangGraph documentation access
- Mistral Codestral model provides sufficient reasoning capabilities
- Local environment can run the required dependencies