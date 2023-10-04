import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.modules import ModuleCreate
from core.modules import Modules


async def add_modules(session: AsyncSession):
    start_modules = (
        ("1  Первое знакомство", 1),
        ("2  Мои первые шаги в Python", 1),
        ("1  Постижение строк и списков", 2),
    )

    for module in start_modules:
        module_create = ModuleCreate(
            title=module[0],
            course_id=module[1],
        )
        await Modules.create(session, module_create)

async def main():
    async with db_helper.session_factory() as session:
        await Modules.delete_all(session=session)
        await add_modules(session=session)
        # await Modules.delete_by_course_id(session=session,course_id=1)



if __name__ == "__main__":
    asyncio.run(main())