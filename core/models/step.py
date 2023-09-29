from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.types import String, LargeBinary
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from .base import Base, BaseHeader

if TYPE_CHECKING:
    from core.models.lesson import Lesson
    from core.models.step_types import StepType
    from core.models.solutions import Solution


class Step(BaseHeader):
    __tablename__ = "steps"

    number: Mapped[int]
    url: Mapped[str] = mapped_column(String(2083))
    image: Mapped[LargeBinary] = mapped_column(LargeBinary)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))

    lesson: Mapped["Lesson"] = relationship(back_populates="step")
    step_type: Mapped["StepType"] = relationship(back_populates="step")
    solution: Mapped["Solution"] = relationship(
        back_populates="step",
        cascade="all, delete-orphan"
    )



