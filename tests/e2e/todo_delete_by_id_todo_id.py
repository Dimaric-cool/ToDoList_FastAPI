import json

from steps.todo_steps import delete_todo
import allure
from assertpy import assert_that

from steps.assert_steps import assert_status_code, assert_error_message


@allure.epic("Todo")
@allure.title("Удаление задачи")
@allure.description("Удаление задачи через метод delete")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_todo(todolist_client, authorize_client, todo_create):

    todo_id = todo_create

    delete_todo(todolist_client, todo_id)

    with allure.step("Проверить что задача удалена"):
        with allure.step("Получить созданую задачу"):
            endpoint = f"/todo/get_by_id/{todo_id}"

            with allure.step(f"http: GET {endpoint}"):
                response = todolist_client.get(endpoint)
                allure.attach(
                    json.dumps(response.json(), indent=4, ensure_ascii=False),
                    name="response",
                    attachment_type=allure.attachment_type.JSON,
                )

            assert_status_code(response,404)
            assert_error_message(response,f"Задача с ID {todo_id} не найдена")

@allure.epic("Todo")
@allure.title("Негативный: Удаление несуществующей задачи ")
@allure.description("Корректная обработка попытки удаления несуществующей задачи")
def test_delete_not_existed_todo(todolist_client, authorize_client, todo_create):
    todo_id = todo_create

    delete_todo(todolist_client, todo_id)

    with allure.step("Повторно удалить удаленную задачу"):

        endpoint = f"/todo/delete_by_id/{todo_id}"

        with allure.step(f"http: DELETE {endpoint}"):
            response = todolist_client.delete(endpoint)

            with allure.step("http status 404"):
                assert_that(response.status_code, description="http status 404").is_equal_to(404)
                allure.attach(
                    f"exp: 404\nrec: {response.status_code}",
                    attachment_type=allure.attachment_type.TEXT,
                )

