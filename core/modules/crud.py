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

    @staticmethod
    async def delete_by_course_id(session: AsyncSession, course_id: int) -> None:
        stmt = delete(Module).where(Module.course_id == course_id)
        await session.execute(stmt)
        await session.commit()



async def add_modules(session: AsyncSession):
    start_modules = (
        ("1  Первое знакомство", 1),
        ("2  Мои первые шаги в Python", 1),
        ("1  Постижение строк и списков", 2),
    )

    for module in start_modules:
        module_create = ModuleCreate(
            title=module[0],
            course_id=module[1],
        )
        await Modules.create(session, module_create)

async def main():
    async with db_helper.session_factory() as session:
        await Modules.delete_all(session=session)
        await add_modules(session=session)
        # await Modules.delete_by_course_id(session=session,course_id=1)



if __name__ == "__main__":
    asyncio.run(main())
