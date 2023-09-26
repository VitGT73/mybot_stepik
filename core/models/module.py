from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from core.models.base import BaseHeader

if TYPE_CHECKING:
    from core.models.lesson import Lesson
    from core.models.course import Course



class Module(BaseHeader):
    __tablename__ = "modules"

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    course: Mapped["Course"] = relationship(back_populates="module")
    lesson: Mapped[list["Lesson"]] = relationship(
        back_populates="module", cascade="all, delete-orphan"
    )
    # step: Mapped[list["Step"]] = relationship(
    #     back_populates="module", cascade="all, delete-orphan"
    # )
