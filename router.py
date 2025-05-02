from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import STask, STaskAdd, STaskId


# Создание роутера с базовыми настройками:
# - prefix="/tasks" - все эндпоинты будут начинаться с /tasks
# - tags=["Tasks"] - группировка в Swagger документации
router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# Эндпоинт для добавления новой задачи
@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    # Используем TaskRepository для сохранения задачи в БД
    # STaskAdd автоматически валидируется FastAPI перед вызовом
    task_id = await TaskRepository.add_one(task)
    
    # Возвращаем JSON-ответ с ID созданной задачи
    # Формат ответа соответствует схеме STaskId
    return {"ok": True, "task_id": task_id}

# Эндпоинт для получения списка всех задач
# GET /tasks
@router.get("")
async def get_tasks() -> list[STask]:
    # Получаем все задачи через репозиторий
    tasks = await TaskRepository.find_all()
    
    # Возвращаем задачи в формате {"tasks": список}
    # Каждая задача автоматически конвертируется в STask
    return {"tasks": tasks}