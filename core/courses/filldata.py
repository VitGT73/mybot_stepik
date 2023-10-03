from sqlalchemy.ext.asyncio import AsyncSession

from core.courses import CourseCreate
from core.models import Course, StepType
from core.step_types import StepTypeCreate


class Courses:
    @classmethod
    async def create(cls, session: AsyncSession, course_create: CourseCreate) -> Course:
        course = Course(**course_create.model_dump())
        session.add(course)
        await session.commit()
        return course

class StepTypes:
    @classmethod
    async def create(cls, session: AsyncSession, step_type_create: StepTypeCreate) -> StepType:
        step_type = StepType(**step_type_create.model_dump())
        session.add(step_type)
        await session.commit()
        return step_type


