# как в этом коде перенести методы delete_by_parent_id из дочерних классов в родительский?
#
# from sqlalchemy import delete
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from core.courses import CourseCreate
# from core.lessons import LessonCreate
# from core.models import Course, Module, Lesson
# from core.modules import ModuleCreate
#
#
# class BaseCRUD:
#     class ModelClass:
#         pass
#
#     class CreateClass:
#         pass
#
#     @classmethod
#     async def create(cls, session: AsyncSession, item_create: CreateClass):
#         item = cls.ModelClass(**item_create.model_dump())
#         session.add(item)
#         await session.commit()
#         return item
#
#
# class Courses(BaseCRUD):
#     ModelClass = Course
#     CreateClass = CourseCreate
#
# class Modules(BaseCRUD):
#     ModelClass = Module
#     CreateClass = ModuleCreate
#
#     @staticmethod
#     async def delete_by_parent_id(session: AsyncSession, course_id: int) -> None:
#         stmt = delete(Module).where(Module.course_id == course_id)
#         await session.execute(stmt)
#         await session.commit()
#
#
# class Lessons(BaseCRUD):
#     ModelClass = Lesson
#     CreateClass = LessonCreate
#
#     @staticmethod
#     async def delete_by_parent_id(session: AsyncSession, module_id: int) -> None:
#         stmt = delete(Lesson).where(Lesson.module_id == module_id)
#         await session.execute(stmt)
#         await session.commit()

