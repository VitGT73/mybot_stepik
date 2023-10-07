from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from .base import Base, LastUpdateMixin

if TYPE_CHECKING:
    from core.models.lesson import Lesson
    from core.models.step_types import StepType
    from core.models.solutions import Solution


class Step(Base, LastUpdateMixin):
    __tablename__ = "steps"

    number: Mapped[int]
    url: Mapped[str] = mapped_column(String(2083))
    image: Mapped[str] = mapped_column(String(255),nullable=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    step_type_id: Mapped[int] = mapped_column(ForeignKey("step_types.id"))

    lesson: Mapped["Lesson"] = relationship(back_populates="steps")
    step_type: Mapped["StepType"] = relationship(back_populates="steps")
    solution: Mapped["Solution"] = relationship(
        back_populates="step",
        cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"{self.__class__.__name__}: (id={self.id!r}, image={self.image!r}, " \
               f"last_update={self.last_update!r}, parent_id={self.parent_id!r})"
