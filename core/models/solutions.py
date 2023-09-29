from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text
from sqlalchemy.types import LargeBinary
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from .base import BaseHeader

if TYPE_CHECKING:
    from core.models.step import Step


class Solution(BaseHeader):
    __tablename__ = "solutions"

    step_id: Mapped[int] = mapped_column(ForeignKey("steps.id"))
    image: Mapped[LargeBinary] = mapped_column(LargeBinary)
    code: Mapped["Text"] = mapped_column(Text)
    step: Mapped["Step"] = relationship(back_populates="solution")