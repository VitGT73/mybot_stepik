import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Course, Module, Lesson, Step, StepType


async def add_step_type(session: AsyncSession, name: str) -> StepType:
    steptype = StepType(name=name)
    session.add(steptype)
    await session.commit()
    print("Type:", steptype)
    return steptype


async def main():
    async with db_helper.session_factory() as session:
        step_names = ("review", "easy-quiz", "hard-quiz", "blank")
        for name in step_names:
            await add_step_type(session=session, name=name)



if __name__ == "__main__":
    asyncio.run(main())
