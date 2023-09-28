# op.create_table(
#     "steps",
#     sa.Column("number", sa.Integer(), nullable=False),
#     sa.Column("url", sa.String(length=2083), nullable=False),
#     sa.Column("image", sa.LargeBinary(), nullable=False),
#     sa.Column("lesson_id", sa.Integer(), nullable=False),
#     sa.Column("title", sa.String(length=60), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.ForeignKeyConstraint(
#         ["lesson_id"],
#         ["lessons.id"],
#     ),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("title"),
# )

import asyncio

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Step, db_helper
from core.step import StepSchema, StepCreate, StepUpdate


async def get_all_steps(session: AsyncSession) -> list[Step]:
    stmt = select(Step).order_by(Step.id)
    result: Result = await session.execute(statement=stmt)
    steps = result.scalars().all()
    return list(steps)


async def get_step(session: AsyncSession, module_id: int) -> Step | None:
    return await session.get(Step, module_id)


async def create_step(session: AsyncSession, step_create: StepCreate) -> Step:
    step = Step(**step_create.model_dump())
    session.add(step)
    await session.commit()
    return step


async def delete_steps(session: AsyncSession, steps: list[Step]) -> None:
    # module = Module(id=id)
    # x = await session.get(ident=id)
    await session.delete(steps)
    await session.commit()


async def delete_step_by_id(session: AsyncSession, id: int) -> None:
    # module = Module(id=id)
    # x = await session.get(ident=id)
    step = await session.get(Step, id)
    await session.delete(step)
    await session.commit()


async def main():
    async with db_helper.session_factory() as session:
        step = StepCreate(title="1.1 Урок ВВедение", url="https://ya.ru", lesson_id=1)
        await create_step(session=session, step_create=step)
        # await delete_module_by_id(session=session, id=1)
        get_lessons = await get_all_steps(session=session)
        # await delete_modules(session=session, modules=get_modules)
        print(get_lessons)


if __name__ == "__main__":
    asyncio.run(main())
