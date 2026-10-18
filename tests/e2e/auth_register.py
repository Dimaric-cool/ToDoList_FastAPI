# import json
#
# from steps.todo_steps import delete_todo
# import allure
# from assertpy import assert_that
#
# from steps.assert_steps import assert_status_code, assert_error_message
#
#
# @allure.epic("Auth")
# @allure.title("Регистрация нового пользователя")
# @allure.description("Регистрация нового пользователя через метод auth/register")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_delete_todo(todolist_client):
#
#     with allure.step("Создать пользователя"):
#         response = todolist_client.delete_todo()
#
#             with allure.step(f"http: GET {endpoint}"):
#                 response = todolist_client.get(endpoint)
#                 allure.attach(
#                     json.dumps(response.json(), indent=4, ensure_ascii=False),
#                     name="response",
#                     attachment_type=allure.attachment_type.JSON,
#                 )
#
#             assert_status_code(response,404)
#             assert_error_message(response,f"Задача с ID {todo_id} не найдена")
#
