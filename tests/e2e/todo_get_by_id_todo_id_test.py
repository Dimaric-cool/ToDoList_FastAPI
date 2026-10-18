#Написать позитивный тест на чтение задачи(сильно похож на тест создания)

import json

import allure
from assertpy import assert_that

from steps.assert_steps import assert_status_code


@allure.epic("Todo")
@allure.title("Чтение задачи")
@allure.description("Чтение задачи через метод get")
def test_get_todo(todolist_client, authorize_client, todo_create):
    allure.title = "Чтение задачи",
    allure.description="Чтение задачи через метод get"

    todo_id = todo_create

    with allure.step("Получить созданую задачу"):
        endpoint = f"/todo/get_by_id/{todo_id}"

        with allure.step(f"http: GET {endpoint}"):
            response = todolist_client.get(endpoint)

            allure.attach(
                json.dumps(response.json(), indent=4, ensure_ascii=False),
                name="response",
                attachment_type=allure.attachment_type.JSON,
            )

        assert_status_code(response, 200)

        with allure.step("Заголовок задачи корректный"):
            assert_that(response.json()["title"],description="Заголовок задачи корректный").is_equal_to("test_title")
            allure.attach(
                f"exp: test_title\nrec: {response.json()["title"]}",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Описание задачи корректное"):
            assert_that(response.json()["description"],description="Описание задачи корректное").is_equal_to("test_description")
            allure.attach(
                f"exp: test_description\nrec: {response.json()["description"]}",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Дата задачи корректная"):
            assert_that(response.json()["due_date"],description="Дата задачи корректная").is_equal_to("2026-08-16")
            allure.attach(
                f"exp: 2026-08-16\nrec: {response.json()["due_date"]}",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Тэги задачи корректны"):
            assert_that(response.json()["tags"],description="Тэги задачи корректны").is_empty()
            allure.attach(
                f"exp: []\nrec: {response.json()["tags"]}",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("ID задачи корректно"):
            assert_that(response.json()["id"],description="ID задачи корректно").is_equal_to(todo_id)
            allure.attach(
                f"exp: {todo_id}\nrec: {response.json()["id"]}",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Статус завершенности задачи - False"):
            assert_that(response.json()["completed"],description="Статус завершенности задачи - False").is_false()
            allure.attach(
                f"exp: False\nrec: {response.json()["completed"]}",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Время создания задачи не пустое"):
            assert_that(response.json()["created_at"],description="Время создания задачи не пустое").is_not_empty()
            allure.attach(
                f"rec: {response.json()["created_at"]}",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Время обновления задачи не пустое"):
            assert_that(response.json()["updated_at"],description="Время обновления задачи не пустое").is_not_empty()
            allure.attach(
                f"rec: {response.json()["updated_at"]}",
                attachment_type=allure.attachment_type.TEXT,
            )

        with allure.step("Комментарий задачи пустой"):
            assert_that(response.json()["comment"],description="Комментарий задачи пустой").is_none()
            allure.attach(
                f"rec: {response.json()["comment"]}",
                attachment_type=allure.attachment_type.TEXT,
            )
