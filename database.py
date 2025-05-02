from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Создание асинхронного движка для работы с SQLite
engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"  # Подключение к файлу tasks.db в той же директории
)

# Создание фабрики асинхронных сессий с отключенным expire_on_commit
new_session = async_sessionmaker(engine, expire_on_commit=False)

# Базовый класс для всех ORM-моделей
class Model(DeclarativeBase):
    pass

# ORM-модель таблицы tasks
class TasksOrm(Model):
    __tablename__ = "tasks"  

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

# Функция создания всех таблиц
async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Model.metadata.create_all)

# Функция удаления всех таблиц
async def delete_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Model.metadata.drop_all)