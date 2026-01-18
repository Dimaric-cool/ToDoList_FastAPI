from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict

class Settings(BaseSettings):
    """Настройки приложения."""
    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"  # Игнорировать лишние переменные окружения (HOST, PORT, EXTRA_ARGS, RELOAD)
    )
    
    app_name: str = "ToDo API"
    debug: bool = True
    
    
    database_url: str = Field(default="postgresql://postgres:postgres@postgres:5432/todolist", env="SQLALCHEMY_DATABASE_URL")
    
    # JWT
    secret_key: str = Field(default="CHANGE_ME_SUPER_SECRET_KEY", env="SECRET_KEY")
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(default=60, env="ACCESS_TOKEN_EXPIRE_MINUTES")

settings = Settings()
