# Story 1.2: MCP Client Implementation

## Status
Completed

## User Story
As a developer, I want to implement a client that connects to the MCP server's documentation tool and wrap it for agent use, so that the system can retrieve documentation on demand.

## Context
Derived from Epic 1 in `docs/epics/epic-1.md` and PRD in `docs/prd.md`.

## Acceptance Criteria
1. A Python function queries the Context7 MCP server's documentation tool/API.
2. The function is wrapped into a LangChain Tool (e.g., `documentation_search`) with a clear description.
3. A basic LangGraph agent is configured with access to this tool.
4. The agent can invoke the tool with a test query and process the returned documentation snippet.

## Deliverables
- MCP client function/module to query documentation (e.g., `src/client/mcp_client.py`).
- LangChain Tool wrapper `documentation_search_tools` and `_wrap_async_tool` (e.g., in `src/agent/tools.py`).
- Minimal LangGraph agent wired with the tool (e.g., `src/agent/agent.py`).
- Unit test proving the tool invocation and result handling (e.g., `tests/test_agent.py`).

## Constraints & Non-Functional Requirements
- Use open-source components only; no paid APIs.
- Keep monorepo, single-service Python implementation.
- Provide clear error handling, timeouts, and retries for MCP calls.
- Configuration via environment variables; document keys in `.env.example`.

## Implementation Plan (Tasks)
- Create MCP client class in `src/client/mcp_client.py`.
- Add environment/config handling (e.g., MCP endpoint, auth if needed) and update `.env.example`.
- Wrap the client tools as LangChain Tools named `documentation_search_tools` in `src/agent/tools.py` with description and input schema.
- Register the tool in the minimal LangGraph agent in `src/agent/agent.py` for initial wiring.
- Add a smoke test in `tests/test_agent.py` that mocks the MCP response and validates tool output flow.

## Definition of Done
- All acceptance criteria satisfied.
- Tests run locally without errors and show the agent using `documentation_search_tools`.

## References
- PRD: `docs/prd.md`
- Epic: `docs/epics/epic-1.md`
