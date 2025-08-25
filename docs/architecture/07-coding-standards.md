# Coding Standards

This document defines development standards for the Code4all project. It complements existing architecture docs:
- `docs/architecture/01-overview.md`
- `docs/architecture/02-architecture-details.md`
- `docs/architecture/03-data-and-apis.md`
- `docs/architecture/04-core-workflows.md`
- `docs/architecture/05-quality-and-operations.md`
- `docs/architecture/06-dev-setup.md`

## Languages & Versions
- Python 3.13.x

## Project Structure
- Application code in `src/`
- Tests in `tests/` mirroring package structure
- Scripts/entry points should live in the root of the repository

## Testing
- Framework: pytest
- Minimum: unit tests for core logic (as per PRD)
- Naming: `test_agent.py`
- Coverage: target 100% for core modules (MVP)

## Dependencies
- Pin versions (for base dependencies) in `requirements.txt`
- Prefer lightweight, widely used OSS packages
- Avoid paid APIs; use only open-source alternatives

## Security & Config
- Do not commit secrets; use `.env` as specified in `06-dev-setup.md`

## Documentation
- Keep `README.md` setup steps current with actual commands
- Update `docs/` when architecture/design decisions change
