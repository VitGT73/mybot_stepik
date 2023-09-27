from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return str(self)

    # Автоматическое создание имени таблицы в нижнем регистре во множественном числе!
    # (если оно не указано явно в свойстве __tablename__
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

#
#
class BaseHeader(Base):
    __abstract__ = True

    title: Mapped[str] = mapped_column(String(60),unique=True)
    last_update: Mapped[datetime | None]

    def __str__(self):
        return f"{self.__class__.__name__} (id={self.id!r}, title={self.title!r}, last_update={self.last_update!r})"
