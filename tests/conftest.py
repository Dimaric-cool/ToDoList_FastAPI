import json

import allure
import pytest
from assertpy import assert_that
from steps.todo_steps import create_todo, delete_todo

from tests.clients.todolist_client import ToDoListClient


@pytest.fixture(scope="session")
def todolist_client():
    with ToDoListClient() as client:
        yield client

@pytest.fixture(scope="session")
def authorize_client(todolist_client):
    todolist_client.get_token()
    yield

@pytest.fixture(scope="function")
def todo_create(todolist_client, authorize_client):
    todo_id = create_todo(todolist_client)

    yield todo_id  # или сам объект задачи
    # опционально: удалить задачу после теста
    with allure.step("Удалить задачу"):
        endpoint = f"/todo/delete_by_id/{todo_id}"

        with allure.step(f"http: DELETE {endpoint}"):
            todolist_client.delete(endpoint)

