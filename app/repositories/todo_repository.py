from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import ARRAY as PG_ARRAY
from sqlalchemy import Text, type_coerce
from app.models.todo import Todo
from app.schemas.todo import TodoFilter
from app.models.db.todo import TodoModel
from datetime import datetime, timedelta, date
from typing import List, Optional

class TodoRepository:
    """Репозиторий для работы с задачами (PostgreSQL реализация)."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self, filters: TodoFilter, user_id: int) -> List[Todo]:
        """Получить все задачи с фильтрацией и сортировкой."""
        query = self.db.query(TodoModel)
        
        # Фильтрация
        if filters.only_active and filters.only_completed:
            raise ValueError("Нельзя одновременно фильтровать только активные и только завершённые задачи.")
        
        if filters.only_active:
            query = query.filter(TodoModel.completed == False)
        elif filters.only_completed:
            query = query.filter(TodoModel.completed == True)
        
        # Фильтрация по дедлайнам
        today = date.today()
        if filters.only_overdue:
            # Просроченные задачи: дедлайн прошел, задача не выполнена
            query = query.filter(
                TodoModel.due_date < today,
                TodoModel.completed == False,
                TodoModel.due_date.isnot(None)
            )
        elif filters.only_upcoming:
            # Приближающиеся задачи: дедлайн в течение 7 дней, задача не выполнена
            week_from_now = today + timedelta(days=filters.days_to_due)
            query = query.filter(
                TodoModel.due_date >= today,
                TodoModel.due_date <= week_from_now,
                TodoModel.completed == False,
                TodoModel.due_date.isnot(None)
            )
        
        # Сортировка
        if filters.sort_by and filters.sort_by in {"id", "created_at", "updated_at", "due_date"}:
            sort_field = getattr(TodoModel, filters.sort_by)
            if filters.sort_order == "desc":
                query = query.order_by(sort_field.desc())
            else:
                query = query.order_by(sort_field.asc())
            
        if filters.tags:
            # Фильтруем задачи, у которых есть все указанные теги (оператор PostgreSQL @>)
            query = query.filter(TodoModel.tags.op('@>')(type_coerce(filters.tags, PG_ARRAY(Text))))
        # Выполняем запрос и преобразуем в доменные модели
        todo_models = query.filter(TodoModel.user_id == user_id).all()
        return [self._convert_to_todo(model) for model in todo_models]
    
    def get_by_id(self, todo_id: int, user_id: int) -> Optional[Todo]:
        """Получить задачу по ID."""
        todo_model = self.db.query(TodoModel).filter(TodoModel.id == todo_id, TodoModel.user_id == user_id).first()
        if not todo_model:
            return None
        
        return self._convert_to_todo(todo_model)
    
    def create(self, todo: Todo) -> Todo:
        """Создать новую задачу."""
        # Создаем SQLAlchemy модель прямо в репозитории
        todo_model = TodoModel(
            user_id=todo.user_id,
            title=todo.title,
            description=todo.description,
            tags=todo.tags if todo.tags else [],
            completed=todo.completed,
            due_date=todo.due_date,
            created_at=todo.created_at,
            updated_at=todo.updated_at
        )
        
        self.db.add(todo_model)
        self.db.commit()
        
        # Обновляем ID в доменной модели
        todo.id = todo_model.id
        return todo
    
    def update(self, todo_id: int, todo: Todo) -> Optional[Todo]:
        """Обновить существующую задачу."""
        todo_model = self.db.query(TodoModel).filter(TodoModel.id == todo_id).first()
        if not todo_model:
            return None
        
        # Обновляем поля
        if todo.title is not None:
            todo_model.title = todo.title
        if todo.description is not None:
            todo_model.description = todo.description
        if todo.tags is not None:
            todo_model.tags = todo.tags
        if todo.completed is not None:
            todo_model.completed = todo.completed
        if todo.due_date is not None:
            todo_model.due_date = todo.due_date
        
        # Обновляем время изменения
        todo_model.updated_at = datetime.utcnow()
        
        self.db.commit()
        
        # Возвращаем обновленную доменную модель
        return self._convert_to_todo(todo_model)
    
    def delete(self, todo_id: int, user_id: int) -> bool:
        """Удалить задачу."""
        todo_model = self.db.query(TodoModel).filter(TodoModel.id == todo_id, TodoModel.user_id == user_id).first()
        if not todo_model:
            return False
        
        self.db.delete(todo_model)
        self.db.commit()
        return True
    
    def _convert_to_todo(self, model: TodoModel) -> Todo:
        """Преобразовать SQLAlchemy модель в доменную модель."""
        return Todo(
            id=model.id,
            user_id=model.user_id,
            title=model.title,
            description=model.description,
            tags=model.tags if model.tags else [],
            completed=model.completed,
            due_date=model.due_date,
            created_at=model.created_at,
            updated_at=model.updated_at
        )
