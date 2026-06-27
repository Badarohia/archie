# Archie Architecture Specification

Version: 1.0

---

# 1. Vision

Archie is a modular, local-first AI platform designed for long-term development.

The project is intended to scale from a personal AI assistant running on a laptop to a multi-agent AI platform capable of speech, vision, planning, memory, streaming, and plugin-based extensions without requiring architectural redesign.

---

# 2. Goals

- Local-first
- Modular
- Strongly typed
- Provider-independent
- Async-first
- Event-driven
- Testable
- Extensible

---

# 3. Non-goals

Archie is NOT:

- a LangChain clone
- a chatbot script
- a collection of utilities
- a monolithic AI application

Archie is a platform.

---

# 4. Core Principles

## Single Responsibility

Every module has one responsibility.

Example:

Conversation manages conversations.

Memory manages memory.

Brain generates responses.

Nothing more.

---

## Dependency Injection

Subsystems receive dependencies through constructors.

No global state.

---

## Provider Independence

Outside provider implementations, Archie must never depend directly on:

- Ollama
- OpenAI
- Gemini
- Anthropic

Everything depends on interfaces.

---

## Configuration Driven

Nothing important is hardcoded.

Configuration controls:

- providers
- models
- prompts
- storage
- plugins

---

## Strong Typing

Public APIs require explicit type annotations.

BasedPyright should remain clean.

---

## Testability

Every subsystem must be independently testable.

---

# 5. Package Responsibilities

app/
Application lifecycle.

brain/
Language model abstraction.

conversation/
Current conversation.

memory/
Long-term memory.

personality/
System prompts.

tools/
External capabilities.

events/
Event bus.

speech/
Speech recognition and synthesis.

vision/
Vision models.

planner/
Planning.

reasoning/
Reasoning.

plugins/
Plugin loading.

scheduler/
Background jobs.

---

# 6. Dependency Rules

Allowed:

Application

↓

Container

↓

Subsystems

↓

Utilities

Forbidden:

Brain → App

Memory → UI

Conversation → Speech

Tool → Runtime

Subsystems must not depend on the application layer.

---

# 7. Quality Standards

Every merge should satisfy:

- Ruff clean
- BasedPyright clean
- Tests passing
- Documentation updated

---

# 8. Development Workflow

1. Design
2. Document
3. Implement
4. Test
5. Commit

Architecture is decided before implementation.

---

# 9. Long-Term Roadmap

Phase 1
Core Platform

✓ Configuration

✓ Logging

✓ Brain

✓ Conversation

✓ Personality

---

Phase 2

Memory

Retrieval

Planning

Reasoning

---

Phase 3

Tool System

Plugin System

Workflow Engine

---

Phase 4

Speech

Vision

Avatar

Emotion

---

Phase 5

API

Desktop

Android

Streaming

---

# 10. Philosophy

Build systems that can evolve without redesign.

Implement features incrementally.

Design architecture permanently.
