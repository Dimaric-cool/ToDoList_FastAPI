from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Настройки приложения."""
    app_name: str = "ToDo API"
    debug: bool = True
    
    # # Настройки базы данных
    # database_url: str = "sqlite:///./todo.db"
    
    # # Настройки безопасности
    # secret_key: str = "your-secret-key"
    # token_expire_minutes: int = 60
    
    # # Настройки сервера
    # host: str = "0.0.0.0"
    # port: int = 8000
    
    # class Config:
    #     env_file = ".env"

settings = Settings()
