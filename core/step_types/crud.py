from sqlalchemy.ext.asyncio import AsyncSession

from core.models import StepType


async def add_step_type(session: AsyncSession, name: str) -> StepType:
    steptype = StepType(name=name)
    session.add(steptype)
    await session.commit()
    return steptype