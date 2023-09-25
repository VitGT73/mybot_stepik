from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, relationship
from core.models.base import BaseHeader

if TYPE_CHECKING:
    from core.models.lesson import Lesson
    from core.models.module import Module
    from core.models.step import Step

class Course(BaseHeader):
    __tablename__ = "courses"

    module: Mapped[list["Module"]] = relationship(
        back_populates="course", cascade="all, delete-orphan"
    )
    lesson: Mapped[list["Lesson"]] = relationship(
        back_populates="course", cascade="all, delete-orphan"
    )
    step: Mapped[list["Step"]] = relationship(
        back_populates="course", cascade="all, delete-orphan"
    )
