from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdateFields, TodoUpdateStatus, TodoGetAll
from app.services.todo_service import TodoService

router = APIRouter(prefix="/todo", tags=["todo"])
todo_service = TodoService()

@router.put("/get_all", response_model=List[TodoResponse])
async def get_all_todos(filters: TodoGetAll):
    """Получить все задачи."""
    if filters.only_active and filters.only_completed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Невозможно одновременно отображать только активные и только выполненные задачи"
        )
    return todo_service.get_all_todos(filters)

@router.get("/get_by_id/{todo_id}", response_model=TodoResponse, status_code=status.HTTP_200_OK)
async def get_todo(todo_id: int):
    """Получить задачу по ID."""
    todo = todo_service.get_todo_by_id(todo_id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Задача с ID {todo_id} не найдена"
        )
    return todo

@router.post("/create", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(todo_data: TodoCreate):
    """Создать новую задачу."""
    return todo_service.create_todo(todo_data)

@router.put("/update_fields/{todo_id}", response_model=TodoResponse)
async def update_todo_fields(todo_id: int, todo_data: TodoUpdateFields):
    """Обновить поля задачи (без статуса)."""
    todo = todo_service.update_todo_fields(todo_id, todo_data)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Задача с ID {todo_id} не найдена"
        )
    if todo is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Не указаны поля для обновления"
        )
    return todo

@router.put("/update_status/{todo_id}", response_model=TodoResponse)
async def update_todo_status(todo_id: int, todo_data: TodoUpdateStatus):
    """Обновить статус задачи."""
    todo = todo_service.update_todo_status(todo_id, todo_data)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Задача с ID {todo_id} не найдена"
        )
    if todo is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Задача уже имеет указанный статус"
        )
    return todo

@router.delete("/delete_by_id/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    """Удалить задачу."""
    success = todo_service.delete_todo(todo_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Задача с ID {todo_id} не найдена"
        )
