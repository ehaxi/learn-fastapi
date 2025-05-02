from sqlalchemy import select
from database import new_session, TasksOrm
from schemas import STask, STaskAdd
      

# Репозиторий для работы с задачами в БД
class TaskRepository():
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        # Создаем новую асинхронную сессию для работы с БД
        async with new_session() as session:
            # Преобразуем Pydantic-схему в словарь
            task_dict = data.model_dump()
            
            # Создаем экземпляр ORM-модели из словаря
            task = TasksOrm(**task_dict)

            # Добавляем задачу в сессию (подготовка к сохранению)
            session.add(task)
            
            # Отправляем запрос в БД без фиксации транзакции
            await session.flush()
            
            # Фиксируем транзакцию
            await session.commit()
            
            # Возвращаем ID созданной задачи
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        # Создаем новую асинхронную сессию
        async with new_session() as session:
            # Формируем SQL-запрос на выборку всех задач
            query = select(TasksOrm)
            
            # Выполняем запрос
            result = await session.execute(query)
            
            # Получаем все записи как ORM-объекты
            task_models = result.scalars().all()
            
            # Конвертируем ORM-модели в Pydantic-схемы
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            
            # Возвращаем список задач в формате Pydantic
            return task_schemas