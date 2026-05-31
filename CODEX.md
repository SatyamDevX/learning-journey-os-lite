# Codex Instructions

This file defines how Codex should work in this repository.

## First Rule

Before making code, architecture, database, UI, documentation, or feature decisions, read `START_HERE.md`.

If this file conflicts with `START_HERE.md`, follow `START_HERE.md`.

## Required Reading Before Code Changes

Before writing application code, read:

- `START_HERE.md`
- `PROJECT_DOCUMENT.md`
- `CODEX.md`
- `AGENTS.md`
- `ARCHITECTURE_DECISIONS.md`
- `CODING_STANDARDS.md`
- `ROADMAP.md`
- `TASKS.md`
- `CHANGELOG.md`

Then:

1. Summarize the current understanding.
2. Create an implementation plan.
3. Ask for approval if requirements are unclear.
4. Keep the implementation small and MVP-focused.

## Working Style

- Preserve the learning-first nature of the project.
- Prefer simple Flask, SQLite, SQLAlchemy, and Jinja2 solutions.
- Do not introduce AI systems, embeddings, vector databases, or agent frameworks in Version 1.
- Do not create application code when the task only asks for documentation.
- Avoid large abstractions until repeated real needs appear.
- Keep changes easy for future learning and review.

## Git Workflow

Use this branch model:

- `main`: stable releases only
- `develop`: integration branch
- `feature/*`: active work

Never commit directly to `main`.

Feature flow:

1. Branch from `develop`.
2. Implement one focused feature or documentation change.
3. Update project documentation.
4. Commit with the approved convention.
5. Push the feature branch.
6. Merge into `develop`.

## Commit Convention

Use these prefixes:

- `feat:`
- `fix:`
- `docs:`
- `refactor:`
- `test:`
- `style:`
- `chore:`

Examples:

- `feat: implement asset creation page`
- `feat: add search functionality`
- `fix: resolve asset filtering issue`
- `docs: update roadmap for sprint 2`
- `refactor: move asset logic into service layer`
- `test: add asset model tests`
- `chore: configure flask migration setup`

## Documentation Updates

Every feature must update:

- `TASKS.md`
- `CHANGELOG.md`
- `LEARNING_LOG.md`

When architecture changes, also update:

- `ARCHITECTURE_DECISIONS.md`
- `PROJECT_DOCUMENT.md` if product behavior changes

When coding style or workflow changes, also update:

- `CODING_STANDARDS.md`
- `CODEX.md`
- `AGENTS.md` if agent behavior changes

## Code Commenting Standard

Code should be self-documenting first:

- Use descriptive names.
- Keep functions focused.
- Make business logic readable.
- Avoid comments that repeat obvious code.

Every public function should have a docstring.

Comments should explain:

- Why something exists
- Business rules
- Architectural decisions
- Future extension points

Comments should not explain obvious statements.

## Decision Rule

When choosing between a complicated solution and a simple maintainable solution, choose the simple maintainable solution.
