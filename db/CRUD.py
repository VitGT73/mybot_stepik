import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Course, Module, Lesson, Step, StepType


async def add_step_type(session: AsyncSession, type: str) -> StepType:
    steptype = StepType(step_type=type)
    session.add(steptype)
    await session.commit()
    return steptype


async def main():
    async with db_helper.session_factory() as session:
        step_types = ("review", "easy-quiz", "hard-quiz", "blank")


if __name__ == "__main__":
    asyncio.run(main())
