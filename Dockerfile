# Официальный образ Python 3.13.3 на базе slim-версии Linux (уменьшенный размер)
FROM python:3.13.3-slim

# Первый . — копирует все файлы из текущей директории (где находится Dockerfile) в контейнер.
# Второй . — целевая директория в контейнере (/app по умолчанию).
COPY . .

RUN pip install -r requirements.txt

# uvicorn — ASGI-сервер для запуска FastAPI-приложений
# main:app — файл main.py с объектом app = FastAPI().
# --host 0.0.0.0 — сервер доступен снаружи контейнера.
# --port 80 — слушает 80-й порт (стандартный HTTP).
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]