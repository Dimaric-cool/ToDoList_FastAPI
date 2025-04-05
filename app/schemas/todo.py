from pydantic import BaseModel, Field
from datetime import datetime


class TodoCreate(BaseModel):
    """Базовая схема для задачи с общими полями."""
    title: str = Field(..., min_length=1, max_length=100, description="Заголовок задачи")
    description: str = Field(None, max_length=1000, description="Описание задачи")
    completed: bool = Field(False, description="Статус выполнения задачи")


class TodoResponse(BaseModel):
    """Схема для ответа с данными задачи."""
    id: int
    title: str = Field(..., min_length=1, max_length=100, description="Заголовок задачи")
    description: str = Field(None, max_length=1000, description="Описание задачи")
    completed: bool = Field(False, description="Статус выполнения задачи")
    created_at: datetime
    updated_at: datetime
    comment: str
