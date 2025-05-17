from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class TodoCreate(BaseModel):
    """Базовая схема для задачи с общими полями."""
    title: str = Field(..., min_length=1, max_length=100, description="Заголовок задачи")
    description: str = Field(None, max_length=1000, description="Описание задачи")


class TodoUpdate(BaseModel):
    """Схема для обновления задачи."""
    title: Optional[str] = Field(None, min_length=1, max_length=100, description="Заголовок задачи")
    description: Optional[str] = Field(None, max_length=1000, description="Описание задачи")
    completed: Optional[bool] = Field(None, description="Статус выполнения задачи")


class TodoResponse(BaseModel):
    """Схема для ответа с данными задачи."""
    id: int
    title: str = Field(..., min_length=1, max_length=100, description="Заголовок задачи")
    description: str = Field(None, max_length=1000, description="Описание задачи")
    completed: bool = Field(False, description="Статус выполнения задачи")
    created_at: datetime
    updated_at: datetime
    comment: Optional[str] = Field(None, description="Комментарий к задаче")
