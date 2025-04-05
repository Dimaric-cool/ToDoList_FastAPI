from app.repositories.todo_repository import TodoRepository
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoResponse


class TodoService:
    """Сервис для работы с задачами."""
    
    def __init__(self, todo_repository=None):
        self.repository = todo_repository or TodoRepository()
    
    def get_all_todos(self):
        """Получить все задачи."""
        todos = self.repository.get_all()
        return [self._to_response(todo) for todo in todos]
    
    def get_todo_by_id(self, todo_id):
        """Получить задачу по ID."""
        todo = self.repository.get_by_id(todo_id)
        if not todo:
            return None
        return self._to_response(todo)
    
    def create_todo(self, todo_data):
        """Создать новую задачу."""
        # Создаем модель из данных схемы
        todo = Todo(
            title=todo_data.title,
            description=todo_data.description,
            completed=todo_data.completed
        )
        
        # Сохраняем через репозиторий
        created_todo = self.repository.create(todo)
        
        # Преобразуем в DTO для ответа
        return self._to_response(created_todo)
    
    def update_todo(self, todo_id, todo_data):
        """Обновить существующую задачу."""
        # Получаем существующую задачу
        existing_todo = self.repository.get_by_id(todo_id)
        if not existing_todo:
            return None
        
        # Обновляем поля
        existing_todo.title = todo_data.title
        existing_todo.description = todo_data.description
        existing_todo.completed = todo_data.completed
        
        # Сохраняем изменения
        updated_todo = self.repository.update(todo_id, existing_todo)
        
        # Преобразуем в DTO для ответа
        return self._to_response(updated_todo)
    
    def delete_todo(self, todo_id):
        """Удалить задачу."""
        return self.repository.delete(todo_id)
    
    def _to_response(self, todo):
        """Преобразовать модель в DTO для ответа."""
        return TodoResponse(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
            created_at=todo.created_at,
            updated_at=todo.updated_at,
            comment="Bla-bla-bla!!!"
        )
