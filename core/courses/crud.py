# op.create_table(
#     "courses",
#     sa.Column("url", sa.String(length=2083), nullable=False),
#     sa.Column("title", sa.String(length=60), nullable=False),
#     sa.Column("last_update", sa.DateTime(), nullable=True),
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.PrimaryKeyConstraint("id"),
#     sa.UniqueConstraint("title"),
# )


from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Course


async def add_course(session: AsyncSession, url: str, title: str) -> Course:
    course = Course(title=title, url=url)
    session.add(course)
    await session.commit()
    return course
