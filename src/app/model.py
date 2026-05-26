import uuid
from src.app.db import Base
from datetime import datetime
from sqlalchemy import DateTime, func, String, Boolean, Text
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects.postgresql import UUID


class PromptData(Base):
    __tablename__ = "prompt_data"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    prompt: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        index=True
    )

    error: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    success: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    model: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    answer: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
