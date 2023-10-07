# op.create_table(
#     "courses",
#     sa.Column("url", sa.String(length=2083), nullable=False),
#     sa.Column("title", sa.String(length=60), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("title"),
# )
import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.courses import CourseCreate
from core.models import Course, db_helper, BaseCRUD


class Courses(BaseCRUD):
    ModelClass = Course
    CreateClass = CourseCreate

    @staticmethod
    async def get_by_title(session: AsyncSession, title: str) -> Course | None:
        stmt = select(Course).where(Course.title == title)
        item: Course | None = await session.scalar(statement=stmt)
        return item



    # @classmethod
    # async def create_all(cls, session: AsyncSession, items_create: list[CourseCreate]):
    #     # item = cls.ModelClass(**items_create.model_dump())
    #     items = [cls.ModelClass(**item.model_dump()) for item in items_create]
    #     session.add_all(items)
    #     await session.commit()
    #     return items


async def main():
    async with db_helper.session_factory() as session:
        pass


if __name__ == "__main__":
    asyncio.run(main())
