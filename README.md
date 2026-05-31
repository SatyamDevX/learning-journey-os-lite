# Learning Journey OS Lite

Learning Journey OS Lite is a personal learning operating system for organizing projects, notes, certificates, links, notebooks, and learning history in one searchable place.

This repository is intentionally small and learning-first. Version 1 is built for one user, one local knowledge base, and one clear problem: reducing knowledge fragmentation.

## Source Of Truth

Read [START_HERE.md](START_HERE.md) before making any product, code, architecture, database, UI, or documentation decision.

If any document conflicts with `START_HERE.md`, `START_HERE.md` wins.

## MVP Scope

Version 1 focuses on:

- Dashboard summary metrics
- Asset management
- Search across titles, descriptions, and tags
- Links hub
- Learning timeline
- Markdown learning notes

Version 1 does not include RAG, embeddings, LangGraph, Google ADK, ChromaDB, PostgreSQL, multi-user features, or SaaS behavior.

## Technology Stack

- Backend: Flask
- Frontend: Jinja2 and Bootstrap 5
- Database: SQLite
- ORM: SQLAlchemy
- Migrations: Flask-Migrate
- Testing: Pytest
- Documentation: Markdown
- Version control: Git and GitHub

## Local Setup

Create and activate the virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

The Flask CLI discovers the application through `wsgi.py`. If you prefer an explicit app target, set:

```powershell
$env:FLASK_APP = "wsgi:app"
```

Initialize migrations for a new checkout only if the `migrations/` directory does not exist:

```powershell
flask db init
```

Create a migration after model changes:

```powershell
flask db migrate -m "initial schema"
```

Apply migrations to the local SQLite database:

```powershell
flask db upgrade
```

Verify migration state:

```powershell
flask db current
flask routes
```

Expected MVP tables after upgrade:

- `assets`
- `tags`
- `asset_tags`
- `timeline_events`

## Project Principles

- Everything is an asset.
- Every asset is searchable.
- Every asset can be tagged.
- Every asset can appear on the timeline.
- Simple, maintainable solutions are preferred.
- Future AI integration should remain possible without shaping the MVP around AI.

## Git Workflow

Use this branch model:

- `main`: stable releases only
- `develop`: integration branch
- `feature/*`: active feature work

Never commit directly to `main`.

Recommended flow:

1. Create a `feature/*` branch from `develop`.
2. Implement the focused change.
3. Update required documentation.
4. Commit using the project commit convention.
5. Push the branch.
6. Merge into `develop`.

## Commit Convention

Use clear conventional prefixes:

- `feat: implement asset creation page`
- `feat: add search functionality`
- `fix: resolve asset filtering issue`
- `docs: update roadmap for sprint 2`
- `refactor: move asset logic into service layer`
- `test: add asset model tests`
- `chore: configure flask migration setup`

## Documentation Discipline

Every feature must update:

- [TASKS.md](TASKS.md)
- [CHANGELOG.md](CHANGELOG.md)
- [LEARNING_LOG.md](LEARNING_LOG.md)

The repository should document both the product and the learning journey behind it.

## Current Status

The repository has documentation, architecture decisions, the asset model layer, Flask application foundation, and initial migration setup. The next work should remain MVP-focused and avoid routes, templates, CRUD, and UI until their sprint begins.
