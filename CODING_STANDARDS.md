# Coding Standards

These standards apply to Learning Journey OS Lite.

The project is a learning-first Flask + SQLite application. Code should be easy to read, easy to explain, and easy to revisit months later.

## Core Principles

- Prefer clarity over cleverness.
- Keep the MVP small.
- Use descriptive names.
- Keep functions focused.
- Avoid premature abstraction.
- Make future AI integration possible without building AI features now.

## Python Standards

- Use clear function, variable, class, and module names.
- Use snake_case for functions and variables.
- Use PascalCase for classes.
- Keep route logic thin when possible.
- Move reusable business logic into service modules when it becomes meaningful.
- Keep database access predictable and explicit.
- Add tests for behavior that affects assets, search, timeline, and dashboard metrics.

## Flask Standards

- Keep routes organized by feature area.
- Use templates for page rendering.
- Use forms for validated user input when form handling is needed.
- Keep configuration separate from business logic.
- Use Flask-Migrate for schema changes.
- Avoid adding large frameworks or services that are outside the MVP.

## Database Standards

- Use SQLite for Version 1.
- Use SQLAlchemy models.
- Keep model fields aligned with the asset system in `START_HERE.md`.
- Use migrations for schema changes.
- Do not introduce PostgreSQL in Version 1.

## Template Standards

- Use Jinja2 templates.
- Use Bootstrap 5 for layout and components.
- Keep pages simple, readable, and useful.
- Prioritize search, navigation, and asset visibility over decorative UI.

## Testing Standards

- Use Pytest.
- Add tests for core model behavior.
- Add tests for search behavior.
- Add tests for important route behavior when routes are implemented.
- Keep tests focused on real project behavior.

## Code Documentation Philosophy

Code should be self-documenting whenever possible.

Good names:

```python
get_asset_by_id()
create_timeline_event()
search_assets_by_tag()
```

Poor names:

```python
ga()
cte()
s()
```

Every public function should have a docstring.

Example:

```python
"""
Create a learning asset and generate a corresponding timeline event.
"""
```

## Commenting Standards

Comments should explain:

- Why something exists
- Business logic
- Architectural decisions
- Future extension points

Comments should not explain obvious code.

Poor comment:

```python
# Increment counter
counter += 1
```

Useful comment:

```python
# Timeline events are stored separately to support future learning summaries.
```

## Commit Standards

Use the project commit convention:

- `feat: implement asset creation page`
- `feat: add search functionality`
- `fix: resolve asset filtering issue`
- `docs: update roadmap for sprint 2`
- `refactor: move asset logic into service layer`
- `test: add asset model tests`
- `chore: configure flask migration setup`

## Documentation Requirement

Every feature must update:

- `TASKS.md`
- `CHANGELOG.md`
- `LEARNING_LOG.md`
