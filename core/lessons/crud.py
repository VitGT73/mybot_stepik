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
from sqlalchemy.orm import selectinload

from core.models import Lesson, db_helper, BaseCRUD
from core.lessons import LessonCreate, LessonUpdate


class Lessons(BaseCRUD):
    ModelClass = Lesson

    async def get_lesson_with_steps(session: AsyncSession, lesson_id: int) -> Lesson:
        stmt = select(Lesson).options(selectinload(Lesson.step),)
        result: Result = await session.execute(stmt)
        # хер знает что тут вернули в lesson, нужно проверить и создать вспомогательный класс в схемах
        lesson = result.scalars()
        return lesson

async def create_lessons(session: AsyncSession, lessons_create: list[Lesson])->list[Lesson]:
    session.add_all(lessons_create)
    await session.commit()
    return lessons_create







async def update_module(
        session: AsyncSession,
        lesson: Lesson,
        lesson_update: LessonUpdate
) -> Lesson:
    for name, value in lesson_update.model_dump(exclude_unset=True).items():
        print(name, value)
        setattr(lesson, name, value)
        print(lesson)
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
