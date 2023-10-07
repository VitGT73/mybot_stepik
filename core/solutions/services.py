import asyncio

from sqlalchemy import select, Result, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from core.courses import Courses
from core.models import Step, db_helper, BaseCRUD
from core.step import StepSchema, StepCreate, StepUpdate, Steps


async def generate_solution_image_filename(session: AsyncSession, step_id: int) -> str:
    step: Step = await Steps.get(session=session, item_id=step_id)
    filename = step.image
    return str(f"{filename}_sol.jpg")


async def main():
    async with db_helper.session_factory() as session:
        image_filename = await generate_solution_image_filename(session=session, step_id=10)
        print(image_filename)



if __name__ == "__main__":
    asyncio.run(main())
