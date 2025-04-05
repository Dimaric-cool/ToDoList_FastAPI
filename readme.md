# ToDo API

## Описание проекта

Это простое API для управления списком задач (ToDo), разработанное с использованием FastAPI. Приложение позволяет создавать, просматривать, обновлять и удалять задачи.

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

## Установка и запуск

### Предварительные требования

- Python 3.13 или выше
- pip (менеджер пакетов Python)

### Шаги по установке

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/todo-api.git
cd todo-api
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
# Для Windows
.venv\Scripts\activate
# Для Linux/Mac
source .venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

### Запуск приложения

```bash
python main.py
```

Приложение будет доступно по адресу: http://localhost:8000

## API документация

После запуска приложения, документация Swagger UI доступна по адресу:
http://localhost:8000/docs

## Структура проекта

```
todo-api/
├── app/
│   ├── models/         # Модели данных
│   ├── repositories/   # Репозитории для работы с данными
│   ├── routes/         # Маршруты API
│   ├── schemas/        # Pydantic схемы для валидации
│   ├── services/       # Бизнес-логика
│   └── config.py       # Конфигурация приложения
├── main.py             # Точка входа в приложение
└── requirements.txt    # Зависимости проекта
```

## Примеры использования API

### Получение всех задач

```bash
curl -X GET http://localhost:8000/todo/get_all
```

### Создание новой задачи

```bash
curl -X POST http://localhost:8000/todo/create \
  -H "Content-Type: application/json" \
  -d '{"title": "Новая задача", "description": "Описание задачи", "completed": false}'
```

### Получение задачи по ID

```bash
curl -X GET http://localhost:8000/todo/get_by_id/1
```

### Обновление задачи

```bash
curl -X PUT http://localhost:8000/todo/update_by_id/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Обновленная задача", "description": "Новое описание", "completed": true}'
```

### Удаление задачи

```bash
curl -X DELETE http://localhost:8000/todo/delete_by_id/1
```

## Лицензия

MIT
