from datetime import datetime, timezone

from sqlalchemy import JSON, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class WaterReading(Base):
    __tablename__ = "water_readings"

    # Basic information
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    device_id: Mapped[str] = mapped_column(
        String(100),
        index=True
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        index=True
    )

    # Raw sensor / GPS values
    ph: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    turbidity_ntu: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    # Backend-computed values
    wqi_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    quality_status: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )

    detected_contaminants: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True
    )

    ai_recommendation: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )