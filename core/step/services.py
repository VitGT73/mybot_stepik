import asyncio

from sqlalchemy import select, Result, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from core.models import Step, db_helper, BaseCRUD
from core.step import StepSchema, StepCreate, StepUpdate, Steps






async def main():
    async with db_helper.session_factory() as session:
        pass


if __name__ == "__main__":
    asyncio.run(main())