# Architecture Decision Records

Architecture Decision Records (ADRs) document important technical decisions made during the development of Archie.

---

## ADR-001

### Title

Use the `src/` project layout.

### Status

Accepted

### Reason

Separates application code from project files and follows modern Python packaging practices.

---

## ADR-002

### Title

Use `uv` for dependency management.

### Status

Accepted

### Reason

Provides fast dependency resolution, isolated environments, and reproducible development.

---

## ADR-003

### Title

Adopt an async-first architecture.

### Status

Accepted

### Reason

Archie will eventually perform multiple concurrent tasks such as speech recognition, language model inference, browser automation, Android communication, memory indexing, and streaming.

Building on `asyncio` from the beginning avoids a large future refactor.

---

## ADR-004

### Title

Rename `core` to `app`.

### Status

Accepted

### Reason

The directory represents the application lifecycle rather than generic "core" functionality.

The name `app` better communicates its responsibility.

---

## ADR-005

### Title

Treat every subsystem as a service.

### Status

Accepted

### Reason

Memory, speech, language models, browser automation, and future integrations all share the same lifecycle.

A common service framework keeps the platform consistent and extensible.

---

## ADR-006

### Title

Prefer composition over inheritance.

### Status

Accepted

### Reason

The Archie application owns components instead of inheriting behaviour.

This reduces coupling and improves testability.

---

## ADR-007

### Title

No global application state.

### Status

Accepted

### Reason

All shared state should belong to the Archie application instance.

Avoiding global variables improves testing, modularity, and future scalability.
