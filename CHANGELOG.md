# Changelog

All meaningful project changes should be recorded here.

This project follows a simple learning-first changelog format. Use dates and commit-style categories.

## Format

```markdown
## YYYY-MM-DD

### Added

- New behavior, docs, or features.

### Changed

- Updates to existing behavior or documentation.

### Fixed

- Bug fixes.

### Learned

- Short note linking product progress to learning progress.
```

## 2026-06-01

### Added

- Added Flask application factory setup.
- Added configuration classes for development, testing, and production.
- Added blueprint registration structure for dashboard, assets, search, links, timeline, and notes.
- Connected Flask-SQLAlchemy and Flask-Migrate initialization to the application factory.

### Changed

- Updated setup documentation with the Flask app entry point for migration commands.

### Learned

- The application factory pattern keeps the project testable and modular while preserving the MVP boundary.

## 2026-06-01

### Added

- Added the first SQLAlchemy 2.x model layer for assets, tags, asset-tag associations, and timeline events.
- Added shared database extension setup for typed Flask-SQLAlchemy models.
- Added project dependency list and Git ignore rules for local virtual environments and generated Python files.

### Changed

- Moved the project from documentation-only foundation into initial model implementation while keeping routes, forms, templates, and UI out of scope.

### Learned

- SQLAlchemy 2.x typed models make relationships and nullable fields explicit, which supports the project goal of readable learning-first code.

## 2026-06-01

### Added

- Added architecture decisions for MVP asset typing, normalized tags, simple SQLite-backed search, and timeline events connected to assets.

### Changed

- Clarified the intended data architecture before generating application code.

### Learned

- Explicit architecture decisions help protect the MVP from premature table splitting, external search systems, and AI-driven scope creep.

## 2026-06-01

### Added

- Created documentation set for Learning Journey OS Lite.
- Added project overview, roadmap, agent instructions, coding standards, architecture decisions, tasks, changelog, learning log, and prompt archive.
- Established Version 1 as a Flask + SQLite personal learning system.

### Changed

- Expanded `README.md` from a placeholder into a project orientation document.

### Learned

- Clear documentation before application code helps protect scope and supports learning-first development.

## 2026-06-01

### Added

- Defined project vision and constraints in `START_HERE.md`.
- Documented the project mission, MVP features, non-goals, architecture principles, Git workflow, commit convention, documentation discipline, and code commenting philosophy.

### Learned

- The project should solve knowledge fragmentation first and defer advanced AI ideas until the core archive is useful.

## 2026-05-31

### Added

- Initialized repository structure.
- Created initial project folders for app, data, docs, instance, and tests.

### Learned

- A clear folder structure makes the project easier to grow without adding application complexity too early.
