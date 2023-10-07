from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from core.models.base import Base, LastUpdateMixin, TitleMixin

if TYPE_CHECKING:
    from core.models.module import Module
    from core.models.step import Step


class Lesson(Base, LastUpdateMixin, TitleMixin):
    __tablename__ = "lessons"

    url: Mapped[str] = mapped_column(String(2083))

    # course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    parent_id: Mapped[int] = mapped_column(ForeignKey("modules.id"))

    # course: Mapped["Course"] = relationship(back_populates="lesson")
    module: Mapped["Module"] = relationship(back_populates="lessons")
    steps: Mapped[list["Step"]] = relationship(
        back_populates="lesson", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"{self.__class__.__name__}: (id={self.id!r}, title={self.title!r}, url={self.url!r}, " \
               f" parent_id={self.parent_id!r},last_update={self.last_update!r})"
