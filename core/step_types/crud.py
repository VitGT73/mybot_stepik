# op.create_table(
#     "step_types",
#     sa.Column("name", sa.String(length=10), nullable=False),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("name"),
# )
import asyncio

from core.models import StepType, db_helper, BaseCRUD

from core.step_types import StepTypeCreate


class StepTypes(BaseCRUD):
    ModelClass = StepType
    CreateClass = StepTypeCreate


async def main():
    async with db_helper.session_factory() as session:
        await StepTypes.delete_all(session=session)


if __name__ == "__main__":
    asyncio.run(main())
