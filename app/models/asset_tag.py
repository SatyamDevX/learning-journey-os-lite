"""Association model connecting assets and tags."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, func
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db


class AssetTag(db.Model):
    """Connect one asset to one tag while preventing duplicate tag assignments."""

    __tablename__ = "asset_tags"
    __table_args__ = (
        Index("ix_asset_tags_tag_asset", "tag_id", "asset_id"),
    )

    asset_id: Mapped[int] = mapped_column(
        ForeignKey("assets.id", ondelete="CASCADE"),
        primary_key=True,
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey("tags.id", ondelete="CASCADE"),
        primary_key=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
