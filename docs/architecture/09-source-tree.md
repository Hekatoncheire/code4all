# Source Tree

This document defines the expected repository structure for Code4all. It consolidates and extends the structure shown in `02-architecture-details.md` and aligns with Story 1.1 deliverables.

## Top-level Layout
```plaintext
code4all/
├── README.md
├── requirements.txt
├── main.py                 # CLI/UI entry
├── .env.example            # Example env vars (do not commit secrets)
├── docs/
│   ├── prd.md
│   ├── epics/
│   ├── stories/
│   └── architecture/
├── src/
│   ├── agent/
│   │   ├── agent.py        # ReAct loop implementation
│   │   └── tools.py        # documentation_search, code_generator tools
│   ├── client/
│   │   └── mcp_client.py   # Context7 MCP client
│   ├── ui/
│   │   └── interface.py    # Gradio Blocks UI
│   ├── service.py          # Orchestration between UI and agent
│   └── data_models.py      # Pydantic models / DTOs (TBD)
├── tests/
│   ├── conftest.py (TBD)
│   └── test_*.py
└── .bmad-core/
```

## Notes
- Keep app code inside `src/` with importable modules.
- Tests mirror `src/` package layout.
- `main.py` can bootstrap the UI (e.g., create and launch Gradio app) or provide a CLI entry.
- Add additional subpackages under `src/` as features grow (e.g., `src/rag/`, `src/eval/`).

## References
- `docs/architecture/02-architecture-details.md`
- `docs/architecture/06-dev-and-next-steps.md`
