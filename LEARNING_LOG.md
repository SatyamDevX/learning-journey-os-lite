# Learning Log

This file records what was learned while building Learning Journey OS Lite.

The project is both software and a learning artifact. Every meaningful feature should add an entry here.

## Entry Format

```markdown
## YYYY-MM-DD: Topic

### Built

- What changed in the project?

### Learned

- What concept, tool, pattern, or workflow became clearer?

### Challenge

- What was confusing, slow, or risky?

### Resolution

- How was the challenge solved?

### Next Question

- What should be explored next?
```

## 2026-06-01: Asset Model Foundation

### Built

- Created the core model layer for assets, tags, asset-tag relationships, and timeline events.
- Set up a local virtual environment and installed the required Flask, SQLAlchemy, migration, and testing packages.

### Learned

- The asset-first architecture maps cleanly to one central `Asset` model plus normalized tags.
- Timeline events should remain separate from assets so learning milestones can exist with or without a direct asset link.
- SQLAlchemy 2.x `Mapped` annotations make model intent easier to inspect before routes exist.

### Challenge

- The project needed enough setup to define models correctly without drifting into routes, forms, templates, or UI.

### Resolution

- Added only the database extension and model files needed for the model layer.

### Next Question

- What validation rules should the asset creation flow enforce before saving user-entered assets?

## 2026-06-01: Architecture Review

### Built

- Reviewed the MVP architecture against the source of truth.
- Added architecture decisions for asset typing, tags, search, and timeline events.

### Learned

- A single asset-centered model is the simplest starting point for notes, projects, certificates, courses, links, and notebooks.
- Tags deserve normalization because they are central to search and organization.
- Search can begin with SQLite-backed matching before considering more advanced options.

### Challenge

- The project needs to remain future-friendly without introducing future-level complexity too early.

### Resolution

- The architecture now explicitly defers type-specific tables, AI search, vector databases, and external search infrastructure.

### Next Question

- Which asset fields are truly required on day one, and which should remain optional?

## 2026-06-01: Documentation Foundation

### Built

- Generated the main project documentation files.
- Defined documentation roles for README, project document, agent instructions, architecture decisions, coding standards, roadmap, tasks, changelog, learning log, and prompts.

### Learned

- Documentation can protect project scope before application code exists.
- A learning-first repository should record product progress and personal understanding together.
- Git workflow and commit conventions are easier to follow when they are documented early.

### Challenge

- The project has future AI potential, but the MVP must stay simple.

### Resolution

- AI-related ideas were documented as future possibilities, not Version 1 requirements.

### Next Question

- What is the smallest Flask setup that supports assets, search, tags, and a timeline cleanly?

## 2026-06-01: Source Of Truth

### Built

- Created `START_HERE.md` as the project source of truth.

### Learned

- A source-of-truth file helps prevent scope drift and keeps future decisions aligned.

### Challenge

- The founder story includes many possible directions: portfolio, AI, certificates, notebooks, search, and projects.

### Resolution

- Version 1 was narrowed to a personal Flask + SQLite knowledge vault.

### Next Question

- How should the asset model represent different learning materials without becoming overcomplicated?

## 2026-05-31: Repository Initialization

### Built

- Created the initial repository and folder structure.

### Learned

- Starting with folders for app, tests, data, docs, and instance encourages separation of concerns.

### Challenge

- It is tempting to start writing application code immediately.

### Resolution

- Project documentation and workflow are being defined first.

### Next Question

- Which setup tasks should be completed before the first feature branch?
