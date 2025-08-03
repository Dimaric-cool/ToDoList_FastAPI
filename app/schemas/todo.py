from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Заголовок задачи")
    description: str = Field(..., max_length=1000, description="Описание задачи")

class TodoCreate(TodoBase):
    pass

class TodoUpdateFields(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100, description="Заголовок задачи")
    description: Optional[str] = Field(None, max_length=1000, description="Описание задачи")

class TodoUpdateStatus(BaseModel):
    completed: bool = Field(..., description="Статус выполнения задачи")

class TodoResponse(TodoBase):
    id: int
    completed: bool = Field(False, description="Статус выполнения задачи")
    created_at: datetime
    updated_at: datetime
    comment: Optional[str] = Field(None, description="Комментарий к задаче")

    class Config:
        from_attributes = True

class TodoFilter(BaseModel):
    only_active: Optional[bool] = Field(False, description="Только активные задачи")
    only_completed: Optional[bool] = Field(False, description="Только завершённые задачи")
    sort_by: Optional[str] = Field(
        None, 
        description="Сортировка задач по полю: id, created_at, updated_at"
    )
    sort_order: Optional[str] = Field(
        "asc", 
        description="Направление сортировки: asc (по возрастанию), desc (по убыванию)"
    )
