# Learning Journey OS Lite

## Read This First

This file is the single source of truth for this repository.

Before making any code, architecture, database, UI, documentation, or feature decision, read this file first.

If another document conflicts with this file, this file wins.

## Founder Story

I am a software developer, data science student, AI engineer, educator, and lifelong learner.

Over the last several years I have learned from:

- BS Degree in Data Science
- Flask projects
- AI and Machine Learning projects
- Google Colab notebooks
- Kaggle notebooks
- GitHub repositories
- Online courses
- Certificates
- Research papers
- Documentation
- YouTube
- Coding platforms

Examples of work already completed:

- Flask applications
- Music Streaming App
- Quiz Master Project
- Stock Prediction Project
- AI and ML assignments
- Competitive programming practice
- Educational content creation

## Core Problem

I learn a lot.

I build a lot.

I document a lot.

But everything is scattered.

Examples:

- Python notes are stored in folders.
- Colab notebooks are in Google Drive.
- GitHub repositories contain important learnings.
- Certificates exist across multiple platforms.
- Code snippets exist inside old projects.
- Learning notes are difficult to locate.
- Project documentation is inconsistent.
- Learning history is fragmented.

As time passes I forget:

- Where I learned something.
- Which project used a technology.
- Where a notebook is stored.
- Which course taught a topic.
- Where a useful code snippet exists.
- What I learned months ago.

The problem is not lack of learning.

The problem is knowledge fragmentation.

## Project Mission

Build a personal Learning Operating System.

The system should become my:

- Knowledge vault
- Learning tracker
- Project archive
- Certificate vault
- Resource directory
- Search engine
- Professional portfolio

One place to store everything.

## Definition Of Success

Six months from now I should be able to answer:

- Where did I learn Flask Security?
- Which project used Redis?
- What do I know about LangGraph?
- Show all resources about RAG.
- Which certificate covered MLOps?
- Which notebook contains vector database experiments?
- What did I learn in 2026?

without manually searching folders.

If I can answer those questions, the project is successful.

## Version 1 Goal

Version 1 is intentionally small.

This is not:

- A startup
- A SaaS platform
- An AI product
- A multi-user system

Version 1 exists to solve my own problem first.

## MVP Features

### Dashboard

Show:

- Total assets
- Total projects
- Total notes
- Total certificates
- Total links
- Recent activity

### Asset System

Everything is an asset.

Examples:

- Note
- Course
- Project
- Certificate
- Link

Every asset should support:

- Title
- Description
- Tags
- Source
- URL
- Local path
- Date created

### Search

Search everything.

Search should work across:

- Titles
- Descriptions
- Tags

The search experience is one of the most important features.

### Links Hub

Store important links.

Examples:

- GitHub
- LinkedIn
- Kaggle
- LeetCode
- HackerRank
- Google Colab
- YouTube playlists
- Documentation

### Timeline

Create a chronological learning history.

Examples:

2024:

- Flask
- Upload App

2025:

- Music App
- Quiz Master

2026:

- AI Agents
- ADK
- LangGraph

### Markdown Notes

Store learning notes.

Support:

- Markdown
- Code blocks
- Learning documentation

## Non Goals

Do not implement these in Version 1:

- RAG
- LangGraph
- Google ADK
- Agent systems
- ChromaDB
- Embeddings
- PostgreSQL
- Multi-user SaaS

Not now.

## Technology Stack

Frontend:

- Jinja2
- Bootstrap 5

Backend:

- Flask

Database:

- SQLite

ORM:

- SQLAlchemy

Migrations:

- Flask-Migrate

Testing:

- Pytest

Version control:

- Git
- GitHub

Documentation:

- Markdown

## Architecture Principles

1. Everything is an asset.
2. Every asset is searchable.
3. Every asset can be tagged.
4. Every asset can appear on the timeline.
5. Simple is better than complex.
6. Future AI integration must remain possible.

## Git Workflow

Use this branch model:

- `main`: stable releases only
- `develop`: integration branch
- `feature/*`: active work

Never commit directly to `main`.

Feature development process:

1. Create a feature branch from `develop`.
2. Implement one focused feature.
3. Update documentation.
4. Commit changes.
5. Push the branch.
6. Merge into `develop`.

Recommended feature branch examples:

- `feature/project-setup`
- `feature/asset-system`
- `feature/search`
- `feature/dashboard`
- `feature/timeline`
- `feature/links-hub`

## Commit Convention

Use these commit prefixes:

- `feat:`
- `fix:`
- `docs:`
- `refactor:`
- `test:`
- `style:`
- `chore:`

Use specific examples instead of vague commit messages:

- `feat: implement asset creation page`
- `feat: add search functionality`
- `fix: resolve asset filtering issue`
- `docs: update roadmap for sprint 2`
- `refactor: move asset logic into service layer`
- `test: add asset model tests`
- `chore: configure flask migration setup`

## Documentation Discipline

Every feature must update:

- `TASKS.md`
- `CHANGELOG.md`
- `LEARNING_LOG.md`

This repository should document both:

1. The product
2. My learning journey

Major features should record:

- What was built
- Why it was built
- What was learned
- What challenges occurred
- How challenges were solved

The repository should become a portfolio, documentation system, learning archive, and engineering journal at the same time.

## Codex And Agent Instructions

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

1. Summarize understanding.
2. Create an implementation plan.
3. Wait for approval if requirements are unclear.

Do not generate application code during documentation-only tasks.

## Code Documentation Philosophy

Code should be self-documenting whenever possible.

Use descriptive names.

Good:

```python
get_asset_by_id()
```

Bad:

```python
ga()
```

Every public function should have a docstring.

Example:

```python
"""
Create a learning asset and generate a corresponding timeline event.
"""
```

Comments should explain:

- Why something exists
- Business logic
- Architectural decisions
- Future extension points

Comments should not explain obvious code.

Bad:

```python
# Increment counter
counter += 1
```

Good:

```python
# Timeline events are stored separately to support future AI-generated learning summaries.
```

## Learning First Development

This project is not only software.

It is also a learning artifact.

Future me should understand:

- What was built
- Why it was built
- What was learned
- What challenges occurred
- How challenges were solved

Every major feature should be documented.

## Final Rule

When choosing between a complicated solution and a simple maintainable solution, choose the simple maintainable solution.

The purpose of this project is to solve knowledge fragmentation and preserve learning history.
