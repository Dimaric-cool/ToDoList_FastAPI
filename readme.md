# ToDo API с FastAPI и PostgreSQL

## Описание проекта

Полнофункциональное API для управления списком задач (ToDo), разработанное с использованием FastAPI и PostgreSQL.

## Функциональность

- Получение списка всех задач
- Получение задачи по ID
- Создание новой задачи
- Обновление существующей задачи
- Удаление задачи

## Технологии

- Python 3.13
- FastAPI
- Pydantic
- Uvicorn
- PostgreSQL
- Docker & Docker Compose
- Goose (миграции базы данных)

## Быстрый старт

### 1. Запуск контейнера с базой данных
```bash
docker-compose up -d
```

### 2. Накатывание миграций
```bash
goose -dir .\migrations\ postgres "postgres://postgres:postgres@localhost:5432/todolist?sslmode=disable" up
```

### 3. Запуск приложения
```bash
docker-compose up
```

### 4. Открыть в браузере
```
http://localhost:8000/docs
```

## Установка Goose (если не установлен)

```bash
goose install github.com/pressly/goose/v3/cmd/goose@latest
```

## Структура проекта

```
ToDoList_FastAPI/
├── app/
│   ├── models/         # Модели данных
│   ├── repositories/   # Репозитории для работы с данными
│   ├── routes/         # Маршруты API
│   ├── schemas/        # Pydantic схемы для валидации
│   ├── services/       # Бизнес-логика
│   └── config.py       # Конфигурация приложения
├── migrations/         # Файлы миграций базы данных
├── main.py             # Точка входа в приложение
├── requirements.txt    # Зависимости проекта
├── docker-compose.yml  # Конфигурация Docker Compose
├── Dockerfile          # Docker образ
```