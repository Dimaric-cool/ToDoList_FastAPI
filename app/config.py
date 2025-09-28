from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    """Настройки приложения."""
    app_name: str = "ToDo API"
    debug: bool = True
    
    
    database_url: str = Field(default="postgresql://postgres:postgres@postgres:5432/todolist", env="SQLALCHEMY_DATABASE_URL")
    
    class Config:
        env_file = ".env"

settings = Settings()
