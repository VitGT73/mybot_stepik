from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from .base import Base, BaseHeader

if TYPE_CHECKING:
    from core.models.lesson import Lesson
    from core.models.course import Course
    from core.models.module import Module


class Step(BaseHeader):
    __tablename__ = "steps"

    number: Mapped[int]
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    module_id: Mapped[int] = mapped_column(ForeignKey("modules.id"))
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))

    course: Mapped["Course"] = relationship(back_populates="step")
    module: Mapped["Module"] = relationship(back_populates="step")
    lesson: Mapped["Lesson"] = relationship(back_populates="step")


class StepType(Base):
    __tablename__ = "step_types"

    step_type: Mapped[str] = mapped_column((String(10)))

    def __repr__(self) -> str:
        return f"{self.__name__} (id={self.id!r}, step_type={self.step_type!r})"
