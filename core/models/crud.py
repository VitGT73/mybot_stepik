import asyncio

from sqlalchemy import select, delete
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper


class BaseCRUD:
    class ModelClass:
        pass

    class CreateClass:
        pass

    @classmethod
    async def create(cls, session: AsyncSession, item_create: CreateClass):
        item = cls.ModelClass(**item_create.model_dump())
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def create_all(cls, session: AsyncSession, items_create: list[CreateClass]):
        items = [cls.ModelClass(**item.model_dump()) for item in items_create]
        session.add_all(items)
        await session.commit()
        return items

    @classmethod
    async def get(cls, session: AsyncSession, item_id: int):
        return await session.get(cls.ModelClass, item_id)

    @classmethod
    async def get_all(cls, session: AsyncSession):
        stmt = select(cls.ModelClass).order_by(cls.ModelClass.id)
        result: Result = await session.execute(statement=stmt)
        items = result.scalars().all()
        return list(items)

    @classmethod
    async def update(cls, session: AsyncSession, item_id: int,
                     item_update):
        item = await cls.get(session=session, item_id=item_id)
        for name, value in item_update.model_dump(exclude_unset=True).items():
            setattr(item, name, value)
        await session.commit()
        return item

    @classmethod
    async def delete(cls, session: AsyncSession, item_id: int) -> None:
        item = await session.get(cls.ModelClass, item_id)
        await session.delete(item)
        await session.commit()

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        stmt = delete(cls.ModelClass)
        await session.execute(stmt)
        await session.commit()


async def main():
    async with db_helper.session_factory() as session:
        pass


if __name__ == "__main__":
    asyncio.run(main())
