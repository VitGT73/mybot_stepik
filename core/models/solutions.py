from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from .base import Base, LastUpdateMixin

if TYPE_CHECKING:
    from core.models.step import Step


class Solution(Base, LastUpdateMixin):
    __tablename__ = "solutions"

    step_id: Mapped[int] = mapped_column(ForeignKey("steps.id"))
    image: Mapped[str] = mapped_column(String(255))
    code: Mapped["Text"] = mapped_column(Text)
    step: Mapped["Step"] = relationship(back_populates="solution")

    def __str__(self):
        return f"{self.__class__.__name__}: (id={self.id!r}, image={self.image!r}, " \
               f"last_update={self.last_update!r}, id={self.step_id!r})"
