---
status: accepted
date: 2026-04-18
---

# Use FastAPI instead of Flask

## Context and Problem Statement

The backend needs an HTTP API framework for the Raspberry Pi 4. The two most common Python choices are Flask and FastAPI.

## Considered Options

- FastAPI
- Flask

## Decision Outcome

**Chosen: FastAPI.**

### Reasons

- Async-native — download and ML tasks run as asyncio background tasks without extra setup
- Auto-generated Swagger UI at `/docs` (useful during development and for thesis documentation)
- Request/response validation via Pydantic — catches bad input at the boundary without boilerplate
- Type hints are enforced by the framework, which aligns with mypy usage in CI

### Consequences

- Requires Python 3.11+ (already the project baseline)
- Slightly steeper learning curve than Flask, but well-documented
