import asyncio

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Solution, db_helper, BaseCRUD
from core.solutions import SolutionCreate, SolutionSchema, SolutionUpdate


class Solutions(BaseCRUD):
    ModelClass = Solution
    CreateClass = SolutionCreate


async def main():
    async with db_helper.session_factory() as session:
        await Solutions.delete_all(session=session)


if __name__ == "__main__":
    asyncio.run(main())