from app.models.todo import Todo


class TodoRepository:
    """Репозиторий для работы с задачами (in-memory реализация)."""
    
    def __init__(self):
        self._storage = {}  # "сырое" хранилище: {id: {title: "...", ...}}
        self.next_id = 1
    
    def get_all(self):
        """Получить все задачи."""
        return [self.get_by_id(todo_id) for todo_id in self._storage.keys()]
    
    def get_by_id(self, todo_id):
        """Получить задачу по ID."""
        raw_data = self._storage.get(todo_id)
        if not raw_data:
            return None
        
        # Преобразуем "сырые" данные в доменную модель - как будем делать с ORM
        return Todo(
            id=todo_id,
            title=raw_data["title"],
            description=raw_data["description"],
            completed=raw_data["completed"],
            created_at=raw_data["created_at"],
            updated_at=raw_data["updated_at"]
        )
    
    def create(self, todo):
        """Создать новую задачу."""
        todo.id = self.next_id
        self._storage[self.next_id] = {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "completed": todo.completed,
            "created_at": todo.created_at,
            "updated_at": todo.updated_at
        }
        self.next_id += 1
        return todo
    
    def update(self, todo_id, todo):
        """Обновить существующую задачу."""
        if todo_id not in self._storage:
            return None
        
        # Сохраняем доменную модель как "сырые" данные - как будем делать с ORM
        self._storage[todo_id] = {
            "title": todo.title,
            "description": todo.description,
            "completed": todo.completed,
            "created_at": todo.created_at,
            "updated_at": todo.updated_at
        }
        
        return todo  # Возвращаем обновленную модель напрямую
    
    def delete(self, todo_id):
        """Удалить задачу."""
        if todo_id not in self._storage:
            return False
        
        del self._storage[todo_id]
        return True
