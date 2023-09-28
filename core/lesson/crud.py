# op.create_table(
#     "modules",
#     sa.Column("course_id", sa.Integer(), nullable=False),
#     sa.Column("title", sa.String(length=60), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.ForeignKeyConstraint(
#         ["course_id"],
#         ["courses.id"],
#     ),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("title"),
# )
import asyncio

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Lesson, db_helper
from core.lesson import LessonCreate, LessonUpdate, LessonSchema


async def get_all_lessons(session: AsyncSession) -> list[Lesson]:
    stmt = select(Lesson).order_by(Lesson.id)
    result: Result = await session.execute(statement=stmt)
    lessons = result.scalars().all()
    return list(lessons)


async def get_lesson(session: AsyncSession, module_id: int) -> Lesson | None:
    return await session.get(Lesson, module_id)


async def create_lesson(session: AsyncSession, lesson_create: LessonCreate) -> Lesson:
    lesson = Lesson(**lesson_create.model_dump())
    session.add(lesson)
    await session.commit()
    return lesson


async def delete_lessons(session: AsyncSession, lessons: list[Lesson]) -> None:
    # module = Module(id=id)
    # x = await session.get(ident=id)
    await session.delete(lessons)
    await session.commit()


async def delete_lesson_by_id(session: AsyncSession, id: int) -> None:
    # module = Module(id=id)
    # x = await session.get(ident=id)
    lesson = await session.get(Lesson, id)
    await session.delete(lesson)
    await session.commit()


async def main():
    async with db_helper.session_factory() as session:
        lesson = LessonCreate(title="1.1 Урок ВВедение", url="https://ya.ru", module_id=1)
        await create_lesson(session=session, lesson_create=lesson)
        # await delete_module_by_id(session=session, id=1)
        get_lessons = await get_all_lessons(session=session)
        # await delete_modules(session=session, modules=get_modules)
        print(get_lessons)


if __name__ == "__main__":
    asyncio.run(main())
