from datetime import datetime, timezone
from typing import Optional


class Todo:
    """Модель задачи без привязки к базе данных."""
    
    def __init__(self,title: str = "",description: Optional[str] = None,completed: bool = False,id: Optional[int] = None,created_at: datetime = None,updated_at: datetime = None):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now(timezone.utc)
        self.updated_at = updated_at or datetime.now(timezone.utc)
    
    def update(self, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None) -> None:
        """Обновить данные задачи."""
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if completed is not None:
            self.completed = completed
        self.updated_at = datetime.now(timezone.utc)

   
