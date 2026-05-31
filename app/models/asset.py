"""Asset model for the central learning archive concept."""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from sqlalchemy import Date, DateTime, Index, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.extensions import db

if TYPE_CHECKING:
    from app.models.tag import Tag
    from app.models.timeline_event import TimelineEvent


class Asset(db.Model):
    """Represent a searchable learning asset such as a note, course, project, certificate, link, or notebook."""

    __tablename__ = "assets"
    __table_args__ = (
        Index("ix_assets_type_created_at", "asset_type", "created_at"),
        Index("ix_assets_date_created", "date_created"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True, index=True)
    asset_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    source: Mapped[str | None] = mapped_column(String(150), nullable=True, index=True)
    url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    local_path: Mapped[str | None] = mapped_column(String(500), nullable=True)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    date_created: Mapped[date | None] = mapped_column(Date, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        index=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    tags: Mapped[list[Tag]] = relationship(
        "Tag",
        secondary="asset_tags",
        back_populates="assets",
    )
    timeline_events: Mapped[list[TimelineEvent]] = relationship(
        "TimelineEvent",
        back_populates="asset",
        passive_deletes=True,
    )
