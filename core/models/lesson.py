from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from core.models.base import BaseHeader

if TYPE_CHECKING:
    from core.models.module import Module
    from core.models.step import Step


class Lesson(BaseHeader):
    __tablename__ = "lessons"

    url: Mapped[str] = mapped_column(String(2083))

    # course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    module_id: Mapped[int] = mapped_column(ForeignKey("modules.id"))

    # course: Mapped["Course"] = relationship(back_populates="lesson")
    module: Mapped["Module"] = relationship(back_populates="lesson")
    step: Mapped[list["Step"]] = relationship(
        back_populates="lesson", cascade="all, delete-orphan"
    )
