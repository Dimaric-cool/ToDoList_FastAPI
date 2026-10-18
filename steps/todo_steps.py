import json

import allure
from assertpy import assert_that
from tests.clients.todolist_client import ToDoListClient

def create_todo(todolist_client: ToDoListClient) -> int:
    with allure.step("Создать задачу"):
        endpoint = "/todo/create"

        with allure.step(f"http: POST {endpoint}"):
            request_body = {
                "title": "test_title",
                "description": "test_description",
                "due_date": "2026-08-16",
                "tags": []
            }
            response = todolist_client.post(endpoint, json=request_body)

            allure.attach(
                json.dumps(request_body, indent=4, ensure_ascii=False),
                name="request body",
                attachment_type=allure.attachment_type.JSON,
            )
            allure.attach(
                json.dumps(response.json(), indent=4, ensure_ascii=False),
                name="response",
                attachment_type=allure.attachment_type.JSON,
            )

        with allure.step("http status 201"):
            assert_that(response.status_code, description="http status 201").is_equal_to(201)
            allure.attach(
                f"exp: 201\nrec: {response.status_code}",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("todo id > 0"):
            assert_that(response.json()["id"], description="todo id > 0").is_greater_than(0)

        return response.json()["id"]

def delete_todo(todolist_client, todo_id):
    with allure.step("Удалить задачу"):
        endpoint = f"/todo/delete_by_id/{todo_id}"

        with allure.step(f"http: DELETE {endpoint}"):
            response = todolist_client.delete(endpoint)

            with allure.step("http status 204"):
                assert_that(response.status_code, description="http status 200").is_equal_to(204)
                allure.attach(
                    f"exp: 204\nrec: {response.status_code}",
                    attachment_type=allure.attachment_type.TEXT,
                )

