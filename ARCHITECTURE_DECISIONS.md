# Architecture Decisions

This file records important architecture decisions for Learning Journey OS Lite.

`START_HERE.md` remains the source of truth. If a decision here conflicts with it, `START_HERE.md` wins.

## Decision Format

Use this format for future decisions:

```markdown
## ADR-000: Decision Title

- Date: YYYY-MM-DD
- Status: Proposed | Accepted | Superseded

### Context

What problem or tradeoff led to this decision?

### Decision

What was decided?

### Consequences

What becomes easier, harder, or intentionally deferred?
```

## ADR-001: Use Flask For The MVP

- Date: 2026-06-01
- Status: Accepted

### Context

The project is a personal learning operating system and should remain small, understandable, and easy to extend.

### Decision

Use Flask as the backend framework for Version 1.

### Consequences

Flask keeps the project lightweight and familiar. It supports learning-first development and avoids the overhead of a larger framework.

## ADR-002: Use SQLite For Version 1

- Date: 2026-06-01
- Status: Accepted

### Context

Version 1 is a personal single-user system. It does not need networked database infrastructure or multi-user scale.

### Decision

Use SQLite for the MVP database.

### Consequences

Local development remains simple. PostgreSQL is intentionally deferred until there is a real need.

## ADR-003: Use SQLAlchemy And Flask-Migrate

- Date: 2026-06-01
- Status: Accepted

### Context

The project needs structured data models and a migration path without committing to a larger architecture.

### Decision

Use SQLAlchemy for ORM behavior and Flask-Migrate for database migrations.

### Consequences

Models remain explicit and testable. Future migration to another relational database remains possible if needed.

## ADR-004: Model The System Around Assets

- Date: 2026-06-01
- Status: Accepted

### Context

The project must organize many types of learning material without creating separate complex systems for each type.

### Decision

Use `Asset` as the central domain concept. Notes, projects, courses, certificates, and links are all assets.

### Consequences

Search, tagging, dashboard metrics, and timeline behavior can build around one consistent concept.

## ADR-005: Keep AI Features Out Of Version 1

- Date: 2026-06-01
- Status: Accepted

### Context

The founder has interest and experience in AI, but the immediate problem is knowledge fragmentation, not AI automation.

### Decision

Do not implement RAG, embeddings, LangGraph, Google ADK, ChromaDB, or agent systems in Version 1.

### Consequences

The MVP remains focused. Future AI integration should remain possible through clean data modeling and documentation, but AI should not drive current architecture.

## ADR-006: Use Markdown For Project Documentation

- Date: 2026-06-01
- Status: Accepted

### Context

The repository should act as software, portfolio, learning archive, and engineering journal.

### Decision

Use Markdown files for project documentation, planning, changelog, prompts, and learning notes.

### Consequences

Documentation stays version-controlled, readable on GitHub, and easy to update with every feature.
