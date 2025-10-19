from app.repositories.todo_repository import TodoRepository
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdateFields, TodoUpdateStatus, TodoFilter
from typing import Optional
from datetime import datetime, timezone
from sqlalchemy.orm import Session


class TodoService:
    """Сервис для работы с задачами."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = TodoRepository(db)
    
    def get_all_todos(self, filters: TodoFilter, user_id: int):
        """Получить все задачи."""
        todos = self.repository.get_all(filters, user_id)
        return [self._to_response(todo) for todo in todos]
    
    def get_todo_by_id(self, todo_id, user_id):
        """Получить задачу по ID."""
        todo = self.repository.get_by_id(todo_id, user_id)
        if not todo:
            return None
        return self._to_response(todo)
    
    def create_todo(self, todo_data, user_id):
        """Создать новую задачу."""
        # Создаем модель из данных схемы
        todo = Todo(
            user_id=user_id,
            title=todo_data.title,
            description=todo_data.description,
            completed=False
        )
        
        # Сохраняем через репозиторий
        created_todo = self.repository.create(todo)
        
        # Преобразуем в DTO для ответа
        return self._to_response(created_todo)
    
    
    def delete_todo(self, todo_id, user_id):
        """Удалить задачу."""
        return self.repository.delete(todo_id, user_id)
    
    def update_todo_fields(self, todo_id, todo_data: TodoUpdateFields, user_id: int):
        """Обновить поля задачи (без статуса)."""
        existing_todo = self.repository.get_by_id(todo_id, user_id)
        if not existing_todo:
            return None
        
        # Обновляем только поля title и description
        isupdated = False
        if todo_data.title is not None:
            existing_todo.title = todo_data.title
            isupdated = True
        if todo_data.description is not None:
            existing_todo.description = todo_data.description
            isupdated = True
            
        if isupdated:
            existing_todo.updated_at = datetime.now(timezone.utc)
            updated_todo = self.repository.update(todo_id, existing_todo)
            return self._to_response(updated_todo)
        return False

    def update_todo_status(self, todo_id, todo_data: TodoUpdateStatus, user_id: int):
        """Обновить только статус задачи."""
        existing_todo = self.repository.get_by_id(todo_id, user_id)
        if not existing_todo:
            return None
        
        # Обновляем только статус
        if existing_todo.completed == todo_data.completed:
            return False
            
        existing_todo.completed = todo_data.completed
        existing_todo.updated_at = datetime.now(timezone.utc)
        updated_todo = self.repository.update(todo_id, existing_todo)
        return self._to_response(updated_todo)
    
    def _to_response(self, todo):
        """Преобразовать модель в DTO для ответа."""
        return TodoResponse(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
            created_at=todo.created_at,
            updated_at=todo.updated_at,
            comment=None
        )
