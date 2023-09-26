from typing import TYPE_CHECKING

from pydantic import HttpUrl

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from core.models.base import BaseHeader

if TYPE_CHECKING:
    from core.models.module import Module


class Course(BaseHeader):
    __tablename__ = "courses"

    url: Mapped[HttpUrl] = mapped_column(String(2083))

    module: Mapped[list["Module"]] = relationship(
        back_populates="course", cascade="all, delete-orphan"
    )
    # lesson: Mapped[list["Lesson"]] = relationship(
    #     back_populates="course", cascade="all, delete-orphan"
    # )
    # step: Mapped[list["Step"]] = relationship(
    #     back_populates="course", cascade="all, delete-orphan"
    # )
