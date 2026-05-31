"""Shared Flask extension instances for the application."""

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for SQLAlchemy 2.x typed declarative models."""


db = SQLAlchemy(model_class=Base)
"""Database extension used by application models and migrations."""

migrate = Migrate()
"""Migration extension used by Flask-Migrate."""
