from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.types import String, LargeBinary
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from .base import Base, BaseHeader

if TYPE_CHECKING:
    from core.models.lesson import Lesson


class Step(BaseHeader):
    __tablename__ = "steps"

    number: Mapped[int]
    url: Mapped[str] = mapped_column(String(2083))
    image: Mapped[LargeBinary] = mapped_column(LargeBinary)
    # course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    # module_id: Mapped[int] = mapped_column(ForeignKey("modules.id"))
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))

    # course: Mapped["Course"] = relationship(back_populates="step")
    # module: Mapped["Module"] = relationship(back_populates="step")
    lesson: Mapped["Lesson"] = relationship(back_populates="step")


