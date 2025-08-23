# Coding Standards

This document defines development standards for the Code4all project. It complements existing architecture docs:
- `docs/architecture/01-overview.md`
- `docs/architecture/02-architecture-details.md`
- `docs/architecture/03-data-and-apis.md`
- `docs/architecture/04-core-workflows.md`
- `docs/architecture/05-quality-and-operations.md`
- `docs/architecture/06-dev-and-next-steps.md`

## Languages & Versions
- Python 3.11.x

## Style & Formatting
- Formatter: Black (line length 100)
- Imports: isort (profile black)
- Linting: Ruff (or Flake8 if Ruff unavailable)
- Type hints: Required for all public functions and modules
- Docstrings: Google-style or NumPy-style

## Project Structure
- Application code in `src/`
- Tests in `tests/` mirroring package structure
- Scripts/entry points should live under `src/` (e.g., `src/app.py`)

## Testing
- Framework: pytest
- Minimum: unit tests for core logic (as per PRD)
- Naming: `test_*.py`
- Coverage: target >70% for core modules (MVP)

## Logging & Errors
- Use Python `logging`; avoid bare prints in library code
- Log levels: DEBUG for dev logs, INFO for high-level flow, WARNING/ERROR for issues
- Provide actionable error messages and avoid silent failures

## Dependencies
- Pin versions in `requirements.txt`
- Prefer lightweight, widely used OSS packages
- Avoid paid APIs; prefer Hugging Face and other open-source sources (per PRD)

## Commit & PR Hygiene
- Small, focused commits with imperative messages
- Include a brief summary of changes and rationale in PR description

## Security & Config
- Do not commit secrets; use `.env` as specified in `06-dev-and-next-steps.md`
- Validate and sanitize inputs where applicable

## Performance
- Keep functions small and composable
- Optimize only after profiling or demonstrated need

## Documentation
- Keep `README.md` setup steps current with actual commands
- Update `docs/` when architecture/design decisions change
