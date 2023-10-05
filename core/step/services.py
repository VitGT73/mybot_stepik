import asyncio

from sqlalchemy import select, Result, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from core.models import Step, db_helper, BaseCRUD
from core.step import StepSchema, StepCreate, StepUpdate, Steps


start_steps = (
    (1, "https://habr.com/", 1, 1),
    (2, "https://habr.com/", 1, 2),
    (3, "https://habr.com/", 1, 3),
    (4, "https://habr.com/", 1, 1),
    (1, "https://habr.com/", 2, 2),
    (2, "https://habr.com/", 2, 3),
    (3, "https://habr.com/", 2, 4),
    (4, "https://habr.com/", 2, 1),
    (5, "https://habr.com/", 2, 2),
    (1, "https://habr.com/", 3, 3),
    (2, "https://habr.com/", 3, 4),
    (3, "https://habr.com/", 3, 1),
    (4, "https://habr.com/", 3, 1),
    (5, "https://habr.com/", 3, 1),
)

async def add_steps(session: AsyncSession):
    for step in start_steps:
        with open(filename, 'rb') as file:
            data = file.read()
        step_create = StepCreate(
            number=step[0],
            url=step[1],
            image=step[2],
            step_type_id=step[2],
            lesson_id=step[3],

        )
        await Steps.create(session, step_create)


async def main():
    async with db_helper.session_factory() as session:
        await add_steps(session=session)


if __name__ == "__main__":
    asyncio.run(main())