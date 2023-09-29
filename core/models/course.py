from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from core.models.base import Base, TitleMixin, LastUpdateMixin

if TYPE_CHECKING:
    from core.models.module import Module


class Course(Base, LastUpdateMixin, TitleMixin):
    __tablename__ = "courses"

    url: Mapped[str] = mapped_column(String(2083))

    module: Mapped[list["Module"]] = relationship(
        back_populates="course", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"{self.__class__.__name__}: (id={self.id!r}, title={self.title!r}, " \
               f"url={self.url!r}, last_update={self.last_update!r})"
    # lesson: Mapped[list["Lesson"]] = relationship(
    #     back_populates="course", cascade="all, delete-orphan"
    # )
    # step: Mapped[list["Step"]] = relationship(
    #     back_populates="course", cascade="all, delete-orphan"
    # )
