from datetime import datetime, timezone
from typing import Optional


class Todo:
    """Модель задачи без привязки к базе данных."""
    
    def __init__(self,title: str = "",description: Optional[str] = None, user_id: Optional[int] = None, completed: bool = False,id: Optional[int] = None,created_at: datetime = None,updated_at: datetime = None):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now(timezone.utc)
        self.updated_at = updated_at or datetime.now(timezone.utc)
    
    def update(self, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None) -> bool:
        """Обновить данные задачи."""
        isupdated = False
        if title is not None:
            self.title = title
            isupdated = True
        if description is not None:
            self.description = description
            isupdated = True
        if completed is not None and completed != self.completed:
            self.completed = completed
            isupdated = True
        if isupdated:
            # self.updated_at = datetime.now(timezone.utc)
            return True
        else:
            return False

   
