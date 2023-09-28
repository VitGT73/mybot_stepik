from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.types import String, LargeBinary
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from .base import Base, BaseHeader

if TYPE_CHECKING:
    from core.models.lesson import Lesson


class StepType(Base):
    __tablename__ = "step_types"

    name: Mapped[str] = mapped_column(String(10), unique=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (id={self.id!r}, step_type={self.name!r})"
