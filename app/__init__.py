"""Application factory for Learning Journey OS Lite."""

from __future__ import annotations

from importlib import import_module
from pathlib import Path

from flask import Flask

from app.extensions import db, migrate
from config import DevelopmentConfig, config_by_name


def create_app(config_name: str | None = None) -> Flask:
    """Create and configure the Flask application instance."""

    app = Flask(__name__, instance_relative_config=True)
    config_class = config_by_name.get(config_name or "development", DevelopmentConfig)
    app.config.from_object(config_class)
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask) -> None:
    """Initialize Flask extensions with the application."""

    import_module("app.models")

    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app: Flask) -> None:
    """Register application blueprints."""

    from app.routes.assets import assets_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.links import links_bp
    from app.routes.notes import notes_bp
    from app.routes.search import search_bp
    from app.routes.timeline import timeline_bp

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(assets_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(links_bp)
    app.register_blueprint(timeline_bp)
    app.register_blueprint(notes_bp)
