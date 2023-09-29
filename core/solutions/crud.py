import asyncio

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Solution, db_helper
from core.solutions import SolutionCreate, SolutionSchema, SolutionUpdate



async def create_solution(session: AsyncSession, solution_create: SolutionCreate) -> Solution:
    solution = Solution(**solution_create.model_dump())
    session.add(solution)
    await session.commit()
    return solution


async def get_all_solutions(session: AsyncSession) -> list[Solution]:
    stmt = select(Solution).order_by(Solution.id)
    result: Result = await session.execute(statement=stmt)
    solutions = result.scalars().all()
    return list(solutions)


async def get_solution(session: AsyncSession, module_id: int) -> Solution | None:
    return await session.get(Solution, module_id)



async def update_solution(
        session: AsyncSession,
        solution: Solution,
        solution_update: SolutionUpdate
) -> Solution:
    for name, value in solution_update.model_dump(exclude_unset=True).items():
        setattr(solution, name, value)
    await session.commit()
    return solution

async def delete_solutions(session: AsyncSession, solutions: list[Solution]) -> None:
    await session.delete(solutions)
    await session.commit()


async def delete_solution_by_id(session: AsyncSession, id: int) -> None:
    solution = await session.get(Solution, id)
    await session.delete(solution)
    await session.commit()




async def main():
    async with db_helper.session_factory() as session:
        pass


if __name__ == "__main__":
    asyncio.run(main())