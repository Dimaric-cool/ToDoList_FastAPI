from app.models.todo import Todo
from app.schemas.todo import TodoFilter
from datetime import datetime, timedelta

class TodoRepository:
    """Репозиторий для работы с задачами (in-memory реализация)."""
    
    def __init__(self):
        self._storage = {}  # "сырое" хранилище: {id: {title: "...", ...}}
        now = datetime.utcnow()
        tasks = [
            {
                "title": "Первая задача",
                "description": "Описание первой задачи",
                "completed": False,
                "created_at": now,
                "updated_at": now + timedelta(minutes=15)
            },
            {
                "title": "Вторая задача",
                "description": "Описание второй задачи",
                "completed": True,
                "created_at": now + timedelta(minutes=10),
                "updated_at": now + timedelta(minutes=12)
            },
            # Добавьте больше задач по желанию
        ]
        self.next_id = 1
        for task in tasks:
            todo = Todo(
                id=None,  # id будет присвоен в create
                title=task["title"],
                description=task["description"],
                completed=task["completed"],
                created_at=task["created_at"],
                updated_at=task["updated_at"]
            )
            self.create(todo)
    
    def get_all(self, filters: TodoFilter):
        """Получить все задачи с фильтрацией и сортировкой."""
        # Фильтрация
        if filters.only_active and filters.only_completed:
            raise ValueError("Нельзя одновременно фильтровать только активные и только завершённые задачи.")
        if filters.only_active:
            todos = [self.get_by_id(todo_id) for todo_id in self._storage.keys() if not self._storage[todo_id]["completed"]]
        elif filters.only_completed:
            todos = [self.get_by_id(todo_id) for todo_id in self._storage.keys() if self._storage[todo_id]["completed"]]
        else:
            todos = [self.get_by_id(todo_id) for todo_id in self._storage.keys()]

        # Сортировка
        if filters.sort_by and filters.sort_by in {"id", "created_at", "updated_at"}:
            sort_field = filters.sort_by  # теперь точно str, не None
            reverse = filters.sort_order == "desc"
            todos.sort(key=lambda todo: getattr(todo, sort_field), reverse=reverse)

        return todos
    
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
