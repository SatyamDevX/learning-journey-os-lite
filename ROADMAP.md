# Roadmap

This roadmap follows `START_HERE.md` and keeps Version 1 intentionally small.

## Current Phase: Foundation

Goal: establish project structure, documentation, workflow, and development rules before application code grows.

Status:

- Repository structure created
- `START_HERE.md` created as source of truth
- Project documentation being generated
- `develop` branch active

## Version 1 MVP

Goal: build a personal Learning Operating System that reduces knowledge fragmentation.

### Milestone 1: Project Setup

- Confirm Flask project structure
- Configure development environment
- Configure SQLite and SQLAlchemy
- Configure Flask-Migrate
- Configure Pytest
- Add basic app factory if appropriate
- Document setup decisions

### Milestone 2: Asset System

- Define asset model
- Support title, description, tags, source, URL, local path, and date created
- Add asset create, list, detail, edit, and delete flows
- Add basic validation
- Add tests for asset behavior

### Milestone 3: Dashboard

- Show total assets
- Show total projects
- Show total notes
- Show total certificates
- Show total links
- Show recent activity

### Milestone 4: Search

- Search titles
- Search descriptions
- Search tags
- Make search easy to access
- Add tests for search behavior

### Milestone 5: Links Hub

- Store important profile, platform, learning, and documentation links
- Support tags and source metadata
- Keep links searchable through the asset system

### Milestone 6: Timeline

- Display learning history chronologically
- Group learning activity by year when useful
- Keep timeline connected to assets

### Milestone 7: Markdown Notes

- Store Markdown learning notes
- Support code blocks
- Keep notes searchable and taggable

## Future Possibilities

These are not Version 1 commitments:

- AI-assisted summaries
- RAG over personal learning assets
- Embeddings
- Vector database search
- LangGraph workflows
- Google ADK experiments
- Portfolio export views
- Advanced analytics

Future features should be considered only after the core MVP is useful.

## Roadmap Rule

If a feature does not help answer the success questions in `START_HERE.md`, defer it.
