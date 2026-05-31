# Agent Guide

This repository may be supported by AI coding agents, but the project itself is not an agent system. Version 1 must remain a simple Flask + SQLite application.

## Source Of Truth

`START_HERE.md` is the source of truth.

Agents must follow it before following any other instruction file.

## Agent Responsibilities

Agents working in this repository should:

- Protect the MVP scope.
- Preserve the learning-first development style.
- Keep documentation current.
- Use the Git workflow defined by the project.
- Prefer readable and maintainable code over clever code.
- Ask for clarification when requirements are unclear.
- Avoid generating application code during documentation-only tasks.

## Required Context Before Implementation

Before implementing code, agents must read:

- `START_HERE.md`
- `PROJECT_DOCUMENT.md`
- `CODEX.md`
- `AGENTS.md`
- `ARCHITECTURE_DECISIONS.md`
- `CODING_STANDARDS.md`
- `ROADMAP.md`
- `TASKS.md`
- `CHANGELOG.md`

Agents should then provide:

- A short understanding summary
- A focused implementation plan
- Any assumptions or open questions

## Git Workflow For Agents

Agents must respect this branch model:

- `main` is stable.
- `develop` is the integration branch.
- `feature/*` is for active work.

Agents must not commit directly to `main`.

Preferred branch examples:

- `feature/project-setup`
- `feature/asset-system`
- `feature/search`
- `feature/dashboard`
- `feature/timeline`
- `feature/links-hub`

## Commit Messages

Use the project commit convention:

- `feat: implement asset creation page`
- `feat: add search functionality`
- `fix: resolve asset filtering issue`
- `docs: update roadmap for sprint 2`
- `refactor: move asset logic into service layer`
- `test: add asset model tests`
- `chore: configure flask migration setup`

## Documentation Discipline

For every feature, agents must update:

- `TASKS.md`
- `CHANGELOG.md`
- `LEARNING_LOG.md`

For architecture decisions, agents must update:

- `ARCHITECTURE_DECISIONS.md`

For new or changed prompts, agents should update:

- `PROMPTS.md`

## Boundaries

Agents must not introduce these into Version 1:

- RAG
- LangGraph
- Google ADK
- Agent systems
- Embeddings
- Vector databases
- ChromaDB
- PostgreSQL
- Multi-user SaaS architecture

Future AI integration should remain possible, but it should not complicate the MVP.
