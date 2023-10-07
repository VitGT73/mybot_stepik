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

from sqlalchemy import select, delete
from sqlalchemy.engine import row
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Module, db_helper, BaseCRUD, Course
from core.modules import ModuleCreate, ModuleUpdate



class Modules(BaseCRUD):
    ModelClass = Module
    CreateClass = ModuleCreate
    @staticmethod
    async def delete_by_course_id(session: AsyncSession, course_id: int) -> None:
        stmt = delete(Module).where(Module.course_id == course_id)
        await session.execute(stmt)
        await session.commit()

    @staticmethod
    async def get_by_course_id(session: AsyncSession, course_id: int) -> row:
        stmt = select(Module).where(Module.course_id == course_id)
        items = await session.scalars(stmt)
        return items


async def main():
    async with db_helper.session_factory() as session:
        # await Modules.delete_all(session=session)
        items = await Modules.get_by_course_id(session=session, course_id=3)
        for item in items:
            print(item.title)



if __name__ == "__main__":
    asyncio.run(main())
