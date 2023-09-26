from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return str(self)


#
#
class BaseHeader(Base):
    __abstract__ = True

    title: Mapped[str] = mapped_column(String(60))
    last_update: Mapped[datetime | None]

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id!r}, title={self.title!r}, last_update={self.last_update!r})"
