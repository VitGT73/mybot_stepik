from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True, sort_order=-10)

    def __repr__(self) -> str:
        return str(self)

    # Автоматическое создание имени таблицы в нижнем регистре во множественном числе!
    # (если оно не указано явно в свойстве __tablename__
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


class TitleMixin:
    @declared_attr
    def title(cls) -> Mapped[str]:
        return mapped_column(String(60), unique=True, sort_order=-1)


class LastUpdateMixin:
    @declared_attr
    def last_update(cls) -> Mapped[datetime | None]:
        return mapped_column(sort_order=10)
