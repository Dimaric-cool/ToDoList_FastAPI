# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем wget для загрузки goose (временно, как root)
USER root
RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

# Скачиваем готовый бинарник Goose для Linux amd64
RUN wget -q https://github.com/pressly/goose/releases/download/v3.20.0/goose_linux_amd64 -O /usr/local/bin/goose && \
    chmod +x /usr/local/bin/goose

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Делаем startup.sh исполняемым
RUN chmod +x startup.sh

# Создаем пользователя без root привилегий
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Открываем порт для приложения
EXPOSE 8000

# Команда для запуска приложения
# Скрипт startup.sh сначала применяет миграции через Goose, затем запускает сервер
CMD ["./startup.sh"] 