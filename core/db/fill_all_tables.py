if __name__ == "__main__":
    import asyncio

    from sqlalchemy import String

    from core.models import db_helper
    from core.step_types import add_step_type

    step_names = ("review", "easy-quiz", "hard-quiz", "blank")

    # async def fill_step_types(names: list[String(10)]) :
    #     async with db_helper.session_factory() as session:
    #         for name in names:
    #             await add_step_type(session=session, name=name)

    if __name__ == "__main__":
        asyncio.run(fill_step_types(step_names))