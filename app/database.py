from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.config import settings

# Создаем движок базы данных
engine = create_engine(settings.database_url)

# Базовый класс для моделей
Base = declarative_base()

# Фабрика сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """Зависимость FastAPI: выдать сессию БД и закрыть после запроса."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
