#!/bin/sh
# Скрипт запуска приложения: сначала миграции, затем сервер

set -e

echo "==> Применяем миграции базы данных через Goose..."

# Используем переменную окружения SQLALCHEMY_DATABASE_URL
# Goose требует формат: goose postgres "DATABASE_URL" up
if [ -z "$SQLALCHEMY_DATABASE_URL" ]; then
    echo "ОШИБКА: SQLALCHEMY_DATABASE_URL не установлена"
    exit 1
fi

# Применяем миграции (используем полный путь к goose, если он есть в /usr/local/bin)
GOOSE_BIN="/usr/local/bin/goose"
if [ -f "$GOOSE_BIN" ]; then
    "$GOOSE_BIN" -dir ./migrations postgres "$SQLALCHEMY_DATABASE_URL" up
else
    # Если goose в PATH
    goose -dir ./migrations postgres "$SQLALCHEMY_DATABASE_URL" up
fi

if [ $? -eq 0 ]; then
    echo "==> Миграции успешно применены"
else
    echo "ОШИБКА: Не удалось применить миграции"
    exit 1
fi

echo "==> Запускаем FastAPI приложение..."

# Запускаем приложение
exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}

