import asyncio

from core.models import db_helper, Course, Module, Lesson, Step, StepType

async def

async def main():
    async with db_helper.session_factory() as session:
        pass

if __name__ == "__main__":
    asyncio.run(main())

step_types = (review, easy-quiz, hard-quiz, blank)
