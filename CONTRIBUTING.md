# Contributing to Archie

Thank you for your interest in contributing to Archie.

Archie is a long-term, local-first AI platform focused on maintainability, modularity, and high engineering standards.

## Development Setup

Clone the repository and install dependencies:

```bash
uv sync
```

Run the application:

```bash
uv run python main.py
```

## Before Opening a Pull Request

Please make sure the following commands all succeed:

```bash
uv run ruff format .
uv run ruff check .
uv run basedpyright
uv run pytest
```

## Coding Standards

* Python 3.14+
* Use type hints for all public code.
* Follow Google-style docstrings.
* Prefer `pathlib` over `os.path`.
* Write asynchronous code when appropriate.
* Keep classes focused on a single responsibility.
* Avoid global state.

## Commit Messages

This project follows the Conventional Commits specification.

Examples:

```text
feat(memory): add memory service
fix(runtime): prevent duplicate startup
docs: update architecture documentation
chore(ci): add GitHub Actions workflow
```

## Design Philosophy

Before adding a new feature, ask:

* Does it have one clear responsibility?
* Does it fit the existing architecture?
* Can it be tested independently?
* Will it still make sense in five years?

Quality is preferred over speed.

## Documentation

If your changes affect the architecture or developer workflow, update the relevant files in the `docs/` directory.

Thank you for helping improve Archie.
