# op.create_table(
#     "step_types",
#     sa.Column("name", sa.String(length=10), nullable=False),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("name"),
# )
import asyncio

from core.models import StepType, db_helper

from sqlalchemy import select, Result, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core.step_types import StepTypeUpdate, StepTypeCreate


class StepTypes(BaseCRUD):
    ModelClass = StepType

class StepTypes:

    @classmethod
    async def create(cls, session: AsyncSession, step_type_create: StepTypeCreate) -> StepType:
        step_type = StepType(**step_type_create.model_dump())
        session.add(step_type)
        await session.commit()
        return step_type

    @classmethod
    async def get(cls, session: AsyncSession, step_type_id: int) -> StepType | None:
        return await session.get(StepType, step_type_id)

    @classmethod
    async def get_all(cls, session: AsyncSession) -> list[StepType]:
        stmt = select(StepType).order_by(StepType.id)
        result: Result = await session.execute(stmt)
        step_types = result.scalars().all()
        return list(step_types)

    @classmethod
    async def update_step_types(cls, session: AsyncSession, step_types_id: int,
                                step_types_update: StepTypeUpdate) -> StepType | None:
        step_type = await session.get(StepType, step_types_id)
        for name, value in step_types_update.model_dump(exclude_unset=True).items():
            setattr(step_type, name, value)
        await session.commit()
        return step_type

    @classmethod
    async def delete(cls, session: AsyncSession, step_types_id: int) -> None:
        step_type = await session.get(StepType, step_types_id)
        await session.delete(step_type)
        await session.commit()

    @classmethod
    async def delete_all(cls, session: AsyncSession) -> None:
        stmt = delete(StepType)
        await session.execute(stmt)
        await session.commit()


async def add_step_types(session: AsyncSession):
    step_names = ("review", "easy-quiz", "hard-quiz", "blank")
    for name in step_names:
        step_types = StepTypeCreate(
            name=name,
        )
        await StepTypes.create(session=session, step_type_create=step_types)


async def main():
    async with db_helper.session_factory() as session:
        await StepTypes.delete_all(session=session)
        await add_step_types(session=session)


if __name__ == "__main__":
    asyncio.run(main())
