from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from core.models.base import Base, LastUpdateMixin

if TYPE_CHECKING:
    from core.models.step import Step


class Solution(Base, LastUpdateMixin):
    __tablename__ = "solutions"

    parent_id: Mapped[int] = mapped_column(ForeignKey("steps.id"))
    type: Mapped[int] = mapped_column(nullable=True)
    code: Mapped["Text"] = mapped_column(Text, nullable=True)
    image: Mapped[str] = mapped_column(String(255), nullable=True)
    step: Mapped["Step"] = relationship(back_populates="solution")

    def __str__(self):
        return f"{self.__class__.__name__}: (id={self.id!r}, image={self.image!r}, " \
               f"last_update={self.last_update!r}, parent_id={self.parent_id!r})"
