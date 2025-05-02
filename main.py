import logging
from set_logger import setup_logging
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


# Настройка логирования для текущего модуля
setup_logging("main")  
logger = logging.getLogger(__name__)

# Асинхронный менеджер контекста для управления жизненным циклом приложения
@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()  
    logger.info("База очищена")  
    await create_tables()  
    logger.info("База готова к работе")  
    
    yield  # Точка разделения: здесь приложение переходит в режим работы
    
    # Этап завершения (после yield):
    logger.info("Выключение")  

# Создание экземпляра FastAPI с кастомным жизненным циклом
app = FastAPI(lifespan=lifespan)  

# Подключение роутера с задачами
# (все эндпоинты из tasks_router будут доступны в API)
app.include_router(tasks_router)  