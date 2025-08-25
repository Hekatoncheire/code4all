# Source Tree

This document defines the expected repository structure for Code4all. It consolidates and extends the structure shown in `02-architecture-details.md` and aligns with Story 1.1 deliverables.

## Top-level Layout
```plaintext
code4all/
├── README.md
├── requirements.txt
├── main.py                 # CLI/UI entry
├── .env.example            # Example env vars (do not commit secrets)
├── .gitignore              # Git ignore file
├── docs/
│   ├── prd.md
│   ├── project-brief.md
│   ├── epics/
│   │   └── epic-1.md
│   ├── stories/
│   │   ├── story-1.1.md
│   │   ├── story-1.2.md
│   │   ├── story-1.3.md
│   │   └── story-1.4.md
│   └── architecture/
│       ├── 01-overview.md
│       ├── 02-architecture-details.md
│       ├── 03-data-and-apis.md
│       ├── 04-core-workflows.md
│       ├── 05-quality-and-operations.md
│       ├── 06-dev-setup.md
│       ├── 07-coding-standards.md
│       ├── 08-tech-stack.md
│       └── 09-source-tree.md
├── src/
│   ├── agent/
│   │   ├── agent.py        # ReAct loop implementation
│   │   └── tools.py        # MCP tool wrappers
│   ├── client/
│   │   └── mcp_client.py   # Context7 MCP client
│   ├── ui/
│   │   └── interface.py    # Gradio ChatInterface UI
│   ├── utils/
│   │   └── models.py       # Pydantic models
│   └── service.py          # Orchestration between UI and agent
└── tests/
    └── test_agent.py       # Agent tests
```

## Notes
- Keep app code inside `src/` with importable modules.
- `main.py` bootstraps the Gradio ChatInterface.
- Documentation organized by type (epics, stories, architecture).

## References
- `docs/architecture/02-architecture-details.md`
- `docs/architecture/06-dev-setup.md`
