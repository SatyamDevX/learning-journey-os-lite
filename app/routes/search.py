"""Search blueprint registration placeholder."""

from flask import Blueprint


search_bp = Blueprint("search", __name__, url_prefix="/search")
"""Blueprint for future search routes."""
