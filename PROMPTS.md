# Prompts

This file records useful prompts for working on Learning Journey OS Lite.

Prompts should support learning-first development, documentation quality, and consistent project workflow.

## Prompt Rules

- Read `START_HERE.md` before using any implementation prompt.
- Keep prompts focused on the MVP.
- Do not request RAG, embeddings, LangGraph, Google ADK, ChromaDB, PostgreSQL, multi-user SaaS, or agent systems for Version 1.
- Ask for documentation updates as part of every feature.
- Ask for an explanation of what changed and what was learned.

## Documentation Generation Prompt

```text
Read START_HERE.md.

Generate or update project documentation while keeping the project MVP-focused.

Pay special attention to:

- Documentation quality
- Git workflow
- Commit conventions
- Learning-first development
- Code commenting standards

Do not generate application code.
START_HERE.md is the source of truth.
```

## Feature Planning Prompt

```text
Read START_HERE.md, PROJECT_DOCUMENT.md, CODEX.md, AGENTS.md, ARCHITECTURE_DECISIONS.md, CODING_STANDARDS.md, ROADMAP.md, TASKS.md, and CHANGELOG.md.

Summarize your understanding of the project.

Create a small implementation plan for this feature:

[feature name]

Keep the plan aligned with Flask, SQLite, SQLAlchemy, Flask-Migrate, Jinja2, Bootstrap 5, and Pytest.

Do not include AI systems, embeddings, vector databases, or multi-user architecture.

List the documentation files that must be updated.
```

## Feature Implementation Prompt

```text
Implement this MVP feature:

[feature description]

Follow START_HERE.md as the source of truth.

Use the existing Flask + SQLite project structure.

Keep the implementation simple and maintainable.

Add or update focused tests.

Update TASKS.md, CHANGELOG.md, and LEARNING_LOG.md.

Use clear names, public function docstrings, and comments only where they explain why something exists.
```

## Code Review Prompt

```text
Review the current changes against START_HERE.md and the project documentation.

Focus on:

- MVP scope
- Simplicity
- Flask + SQLite alignment
- Searchability and asset model consistency
- Test coverage
- Documentation updates
- Commit convention readiness

List issues by severity with file references.
```

## Learning Reflection Prompt

```text
Create a LEARNING_LOG.md entry for the work completed today.

Include:

- What was built
- What was learned
- What challenge occurred
- How the challenge was solved
- What question should be explored next

Keep the entry concise and useful for future review.
```

## Changelog Prompt

```text
Update CHANGELOG.md for the current change.

Use the project changelog style.

Include:

- Added
- Changed
- Fixed, if applicable
- Learned

Keep the entry factual and tied to the project mission.
```
