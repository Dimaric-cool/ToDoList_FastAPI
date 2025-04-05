from datetime import datetime
from typing import Optional


class Todo:
    """Модель задачи без привязки к базе данных."""
    
    def __init__(self,title: str = "",description: Optional[str] = None,completed: bool = False,id: Optional[int] = None,created_at: datetime = None,updated_at: datetime = None):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()
    
    def mark_as_completed(self) -> None:
        """Отметить задачу как выполненную."""
        self.completed = True
        self.updated_at = datetime.utcnow()
    
    def mark_as_incomplete(self) -> None:
        """Отметить задачу как невыполненную."""
        self.completed = False
        self.updated_at = datetime.utcnow()
    
    # def update(self, title: Optional[str] = None, description: Optional[str] = None) -> None:
    #     """Обновить данные задачи."""
    #     if title is not None:
    #         self.title = title
    #     if description is not None:
    #         self.description = description
    #     self.updated_at = datetime.utcnow()
