from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional, List


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Заголовок задачи")
    description: str = Field(..., max_length=1000, description="Описание задачи")
    due_date: Optional[date] = Field(None, description="Срок выполнения задачи (дедлайн)")
    tags: Optional[List[str]] = Field(default=[], description="Теги задачи")

class TodoCreate(TodoBase):
    pass

class TodoUpdateFields(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100, description="Заголовок задачи")
    description: Optional[str] = Field(None, max_length=1000, description="Описание задачи")
    due_date: Optional[date] = Field(None, description="Срок выполнения задачи (дедлайн)")
    tags: Optional[List[str]] = Field(None, description="Теги задачи")

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
    only_overdue: Optional[bool] = Field(False, description="Только просроченные задачи (дедлайн прошел, задача не выполнена)")
    only_upcoming: Optional[bool] = Field(False, description="Только задачи с приближающимся дедлайном (в течение 7 дней)")
    days_to_due: Optional[int] = Field(7, description="Количество дней до дедлайна")
    tags: Optional[List[str]] = Field(None, description="Теги задачи")
    sort_by: Optional[str] = Field(
        None, 
        description="Сортировка задач по полю: id, created_at, updated_at, due_date"
    )
    sort_order: Optional[str] = Field(
        "asc", 
        description="Направление сортировки: asc (по возрастанию), desc (по убыванию)"
    )
