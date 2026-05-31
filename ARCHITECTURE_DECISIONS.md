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

## ADR-007: Use A Simple Asset Type Field For Version 1

- Date: 2026-06-01
- Status: Accepted

### Context

Assets can represent notes, courses, projects, certificates, links, notebooks, documentation resources, and coding platform profiles. It would be possible to create separate tables for each asset type, but Version 1 needs a small and searchable system first.

### Decision

Use one central `Asset` concept with a simple type field for Version 1. Do not create separate type-specific tables until repeated real behavior requires them.

### Consequences

The MVP remains easier to build, search, test, and explain. Some type-specific fields may need to remain optional or generic at first, but that is acceptable for a personal archive.

## ADR-008: Use Normalized Tags

- Date: 2026-06-01
- Status: Accepted

### Context

Tags are central to search and retrieval. Storing tags as comma-separated text would be quick, but it would make filtering, reuse, cleanup, and future search behavior harder.

### Decision

Represent tags as reusable records connected to assets through a many-to-many relationship.

### Consequences

Tag search and filtering stay reliable. The data model is slightly more complex than a text field, but the complexity supports a core project requirement.

## ADR-009: Start With Simple Database Search

- Date: 2026-06-01
- Status: Accepted

### Context

Search is one of the most important MVP features. The project must search asset titles, descriptions, and tags, but Version 1 should not introduce AI search, embeddings, vector databases, or external search infrastructure.

### Decision

Start with simple SQLite-backed search over titles, descriptions, and tags. Consider SQLite FTS only if basic search becomes too limited.

### Consequences

The first search implementation stays understandable and aligned with the stack. Advanced search can be added later without changing the product mission.

## ADR-010: Keep Timeline Events Connected To Assets

- Date: 2026-06-01
- Status: Accepted

### Context

The timeline should show chronological learning history. Some timeline entries will naturally come from assets, while others may represent broader learning milestones.

### Decision

Represent timeline events separately from assets, with an optional connection back to an asset.

### Consequences

Assets can appear on the timeline without forcing every learning event to be a full asset. This keeps the timeline flexible while preserving the asset-first architecture.
