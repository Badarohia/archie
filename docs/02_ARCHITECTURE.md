# Archie Platform Architecture

## Overview

Archie is designed as a **local-first, modular AI platform**.

The architecture prioritizes:

* Modularity
* Scalability
* Replaceable components
* Long-term maintainability
* Hardware independence

The goal is that new capabilities can be added as services without redesigning the application.

---

# Architecture Layers

```text
┌──────────────────────────────┐
│        User Interfaces       │
├──────────────────────────────┤
│ CLI │ Desktop │ Android │ API│
└──────────────┬───────────────┘
               │
               ▼
        Archie Application
               │
     ┌─────────┴─────────┐
     │                   │
 Runtime          Service Manager
     │
     ▼
 Base Services
     │
 ┌───┼────────┬──────────┬─────────┐
 │   │        │          │         │
Memory Speech  LLM      Vision   Tools
```

---

# Directory Responsibilities

## app/

Contains the application lifecycle.

Responsibilities:

* Application object
* Bootstrap
* Runtime
* Service manager
* Metadata
* Console
* Startup banner

The application layer should never depend on higher-level AI modules.

---

## services/

Defines the common service framework.

Responsibilities:

* Base service
* Service lifecycle
* Service exceptions

Every future subsystem should inherit from the service framework.

---

## Feature Modules

Feature modules provide AI capabilities.

Examples:

* brain/
* memory/
* speech/
* vision/
* tools/
* avatar/

Each feature module should solve one problem only.

---

# Dependency Rules

Dependencies always point downward.

```text
Application
      │
      ▼
Infrastructure
      │
      ▼
Services
      │
      ▼
Features
```

Higher layers may depend on lower layers.

Lower layers must never depend on higher layers.

---

# Application Lifecycle

```text
main.py
    │
Bootstrap
    │
Archie
    │
Runtime
    │
Service Manager
    │
Registered Services
```

Startup order:

1. Bootstrap
2. Runtime
3. Service Manager
4. Registered Services

Shutdown happens in reverse order.

---

# Engineering Principles

* Composition over inheritance
* Explicit dependencies
* No global state
* One responsibility per class
* Async-first architecture
* Every component is independently testable
* Every service follows the same lifecycle

---

This document describes the current architecture of Archie and will evolve as the platform grows.
