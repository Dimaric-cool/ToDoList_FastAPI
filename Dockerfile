# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Создаем пользователя без root привилегий
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Открываем порт для приложения
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"] 