from pydantic import BaseModel


# Схема для добавления задачи (входные данные API)
class STaskAdd(BaseModel):
    name: str  # Обязательное поле - название задачи
    description: str | None = None  # Опциональное поле - описание

# Схема для возвращаемой задачи (расширяет STaskAdd)
class STask(STaskAdd):
    id: int  # Добавляем идентификатор, который генерируется в БД

# Схема для ответа после создания задачи
class STaskId(BaseModel):
    ok: bool = True  # Флаг успешного выполнения (по умолчанию True)
    task_id: int  # ID созданной задачи