# Epic 1: "Code4all" ReAct Agent Implementation

## Summary
Build and demonstrate a complete, tool-using ReAct agent from project setup to a functional Gradio UI, fulfilling all core project requirements in a single, streamlined workflow.

## Goals
- Establish project scaffolding and reproducible environment
- Implement MCP client integration for documentation retrieval
- Provide a coder tool for Python snippet generation
- Create a ReAct agent using LangGraph with a clear reasoning loop
- Integrate the agent into a Gradio UI with visible reasoning logs

## Success Metrics
- Working CLI + Gradio demo that satisfies FR1–FR7 and NFR1–NFR6 from `docs/prd.md`
- Agent can answer a complex query using both documentation_search and code_generator tools within a single reasoning loop
- Setup reproducible on a clean machine following README

## In Scope
- Monorepo, single-service Python implementation
- Open-source models only (no paid APIs)
- Minimalist developer-focused UI in Gradio
- Basic unit tests for critical paths

## Out of Scope (MVP)
- Cloud deployment
- Comprehensive E2E automated test suite
- Advanced branding or accessibility targets beyond basic best practices

## Dependencies & References
- PRD: `docs/prd.md`
- Tech assumptions and standards: `docs/architecture/`

## User Stories and Acceptance Criteria

### Story 1.1: Project Scaffolding & Environment Setup - Completed
User Story: As a developer, I want a well-defined project structure and a reproducible environment, so that I can start building the application efficiently and consistently.

Acceptance Criteria:
1. A Git repository is initialized with a standard Python project structure (e.g., `src/`, `tests/`).
2. A `requirements.txt` file is created listing initial dependencies (e.g., LangGraph, Gradio).
3. A `README.md` includes project title and setup/run instructions.
4. A basic "hello world" Gradio application launches from a main Python script.

### Story 1.2: MCP Client Implementation - Completed
User Story: As a developer, I want to implement a client that connects to the MCP server's documentation tool and wrap it for agent use, so that the system can retrieve documentation on demand.

Acceptance Criteria:
1. A Python function queries the Context7 MCP server's documentation tool/API.
2. The function is wrapped into a LangChain Tool (e.g., `documentation_search`) with a clear description.
3. A basic LangGraph agent is configured with access to this tool.
4. The agent can invoke the tool with a test query and process the returned documentation snippet.

### Story 1.3: Implement the ReAct Agent - Completed
User Story: As a developer, I want to implement a ReAct-style agent that can use a set of tools through a 'thought-action-observation' reasoning loop, so that it can autonomously solve multi-step problems.

Acceptance Criteria:
1. A ReAct agent is created using LangGraph.
2. The agent has a toolkit containing `documentation_search`.
3. The agent's reasoning process (Thought, Action, Observation) is logged clearly.
4. The agent answers a complex query by using the tool within one reasoning loop.

### Story 1.4: Integrate ReAct Agent into the Gradio UI - Completed
User Story: As a user, I want the Gradio UI to use the ReAct agent, so that I can ask complex questions and see the agent work through the problem to provide a final answer.

Acceptance Criteria:
1. The Gradio UI backend calls the ReAct agent.
2. The UI displays the final answer (text or code).

## Risks & Mitigations
- Model performance variability with open-source LLMs → Choose a small, locally runnable model known to work with LangChain; keep model easily swappable (NFR5).
- Time constraints → Prioritize MVP scope and defer non-critical polish.
- Integration complexity → Build incrementally, validating each tool in isolation before composing.

## Milestones
- M1: Scaffolding + Hello Gradio
- M2: MCP client tool integrated
- M3: Functional ReAct agent 
- M4: Gradio UI integration
