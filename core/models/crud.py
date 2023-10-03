import asyncio

from sqlalchemy import select, delete
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.courses import CourseUpdate, CourseCreate
from core.models import Course, db_helper, StepType


class BaseCRUD:
    class ModelClass:
        pass

    @classmethod
    async def create(cls, session: AsyncSession, item_create):
        item = cls.ModelClass(**item_create.model_dump())
        session.add(item)
        await session.commit()
        return item

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        stmt = delete(cls.ModelClass)
        await session.execute(stmt)
        await session.commit()

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


class Courses(BaseCRUD):
    ModelClass = Course

    @classmethod
    async def get_by_title(cls, session: AsyncSession, title: str) -> ModelClass | None:
        stmt = select(cls.ModelClass).where(cls.ModelClass.title == title)
        item: cls.ModelClass | None = await session.scalar(statement=stmt)
        return item


class StepTypes(BaseCRUD):
    ModelClass = StepType


async def add_courses(session: AsyncSession):
    start_courses = (
        ("Добрый, добрый Python - обучающий курс от Сергея Балакирева", "https://stepik.org/course/100707"),
        ("Поколение Python: курс для начинающих", "https://stepik.org/course/58852"),
        ("Поколение Python: курс для продвинутых", "https://stepik.org/course/68343"),
        ("Инди-курс программирования на Python", "https://stepik.org/course/63085"),
    )

    for course in start_courses:
        course_create = CourseCreate(
            title=course[0],
            url=course[1],
        )
        await Courses.create(session, course_create)


async def main():
    async with db_helper.session_factory() as session:
        await Courses.delete_all(session=session)
        await add_courses(session)
        aaa = await Courses.get(session, 2)
        print(aaa)


if __name__ == "__main__":
    asyncio.run(main())
