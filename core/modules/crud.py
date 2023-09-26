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

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Module, db_helper


async def add_module(session: AsyncSession, title: str, course_id: int) -> Module:
    module = Module(title=title, course_id=course_id)
    session.add(module)
    await session.commit()
    return module


async def del_module(session: AsyncSession, id: int) -> Module:
    # module = Module(id=id)
    # x = await session.get(ident=id)
    module = await session.get(Module, id)
    await session.delete(module)
    await session.commit()
    return id


async def main():
    async with db_helper.session_factory() as session:
        # record = ("1.1 ВВедение",1)
        # await add_module(session=session, title=record[0],course_id= record[1])
        await del_module(session=session, id=1)


if __name__ == "__main__":
    asyncio.run(main())
