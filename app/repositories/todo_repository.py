from app.models.todo import Todo


class TodoRepository:
    """Репозиторий для работы с задачами (in-memory реализация)."""
    
    def __init__(self):
        self.todos = {}  # словарь для хранения задач: {id: Todo}
        self.next_id = 1
    
    def get_all(self):
        """Получить все задачи."""
        return list(self.todos.values())
    
    def get_by_id(self, todo_id):
        """Получить задачу по ID."""
        return self.todos.get(todo_id)
    
    def create(self, todo):
        """Создать новую задачу."""
        todo.id = self.next_id
        self.todos[self.next_id] = todo
        self.next_id += 1
        return todo
    
    def update(self, todo_id, todo):
        """Обновить существующую задачу."""
        if todo_id not in self.todos:
            return None
        
        todo.id = todo_id
        self.todos[todo_id] = todo
        return todo
    
    def delete(self, todo_id):
        """Удалить задачу."""
        if todo_id not in self.todos:
            return False
        
        del self.todos[todo_id]
        return True
