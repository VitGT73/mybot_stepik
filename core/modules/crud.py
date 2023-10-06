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

from sqlalchemy import select, Result, delete
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




async def main():
    async with db_helper.session_factory() as session:
        await Modules.delete_all(session=session)




if __name__ == "__main__":
    asyncio.run(main())
