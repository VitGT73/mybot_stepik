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

from core.models import Module, db_helper
from core.modules import ModuleCreate, ModuleUpdate



async def create_module(session: AsyncSession, module_create: ModuleCreate) -> Module:
    module = Module(**module_create.model_dump())
    session.add(module)
    await session.commit()
    return module

async def get_all_modules(session: AsyncSession) -> list[Module]:
    stmt = select(Module).order_by(Module.id)
    result: Result = await session.execute(statement=stmt)
    modules = result.scalars().all()
    return list(modules)


async def get_module(session: AsyncSession, module_id: int) -> Module | None:
    return await session.get(Module, module_id)


async def update_module(
        session: AsyncSession,
        module: Module,
        module_update: ModuleUpdate
) -> Module:
    for name, value in module_update.model_dump(exclude_unset=True).items():
        print(name, value)
        setattr(module, name, value)
        print(module)
    await session.commit()
    return module

async def delete_modules(session: AsyncSession, modules: list[Module]) -> None:
    # module = Module(id=id)
    # x = await session.get(ident=id)
    await session.delete(modules)
    await session.commit()


async def delete_module_by_id(session: AsyncSession, id: int) -> None:
    # module = Module(id=id)
    # x = await session.get(ident=id)
    module = await session.get(Module, id)
    await session.delete(module)
    await session.commit()



async def main():
    async with db_helper.session_factory() as session:
        module = ModuleCreate(title="1.1 ВВедение", course_id=1)
        await create_module(session=session, module_create=module)
        # await delete_module_by_id(session=session, id=1)
        get_modules = await get_all_modules(session=session)
        # await delete_modules(session=session, modules=get_modules)
        print(get_modules)


if __name__ == "__main__":
    asyncio.run(main())
