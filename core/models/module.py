from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from core.models.base import Base, LastUpdateMixin, TitleMixin

if TYPE_CHECKING:
    from core.models.lesson import Lesson
    from core.models.course import Course


class Module(Base, LastUpdateMixin, TitleMixin):
    __tablename__ = "modules"

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    course: Mapped["Course"] = relationship(back_populates="modules")
    lessons: Mapped[list["Lesson"]] = relationship(
        back_populates="module", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"{self.__class__.__name__}: (id={self.id!r}, title={self.title!r}, " \
               f"last_update={self.last_update!r}, id={self.course_id!r})"
