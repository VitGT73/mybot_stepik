# op.create_table(
#     "step_types",
#     sa.Column("name", sa.String(length=10), nullable=False),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("name"),
# )
import asyncio

from core.models import StepType, db_helper

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.step_types import StepTypeUpdate,StepTypeCreate


async def create_step_type(session: AsyncSession, name: str) -> StepType:
    step_type = StepType(name=name)
    session.add(step_type)
    await session.commit()
    return step_type



async def get_all_modules(session: AsyncSession) -> list[StepType]:
    stmt = select(StepType).order_by(StepType.id)
    result: Result = await session.execute(statement=stmt)
    modules = result.scalars().all()
    return list(modules)


async def get_module(session: AsyncSession, module_id: int) -> StepType | None:
    return await session.get(StepType, module_id)


async def create_step_types(session: AsyncSession, step_type_create: StepTypeCreate) -> StepType:
    step_type = StepTypeCreate(**step_type_create.model_dump())
    session.add(step_type)
    await session.commit()
    return step_type


async def update_step_types(
        session: AsyncSession,
        step_types: StepType,
        step_types_update: StepTypeUpdate
) -> StepType:
    for name, value in step_types_update.model_dump(exclude_unset=True).items():
        print(name, value)
        setattr(step_types, name, value)
        print(step_types)
    await session.commit()
    return step_types

async def delete_step_types(session: AsyncSession, step_types: list[StepType]) -> None:
    # module = Module(id=id)
    # x = await session.get(ident=id)
    await session.delete(step_types)
    await session.commit()


async def delete_step_types_by_id(session: AsyncSession, id: int) -> None:
    # module = Module(id=id)
    # x = await session.get(ident=id)
    step_types = await session.get(StepType, id)
    await session.delete(step_types)
    await session.commit()




async def main():
    async with db_helper.session_factory() as session:
        step_names = ("review", "easy-quiz", "hard-quiz", "blank")
        for name in step_names:
            await create_step_type(session=session, name=name)


if __name__ == "__main__":
    asyncio.run(main())
