"""
E2e против локально поднятого сервиса (uvicorn/docker).
URL: переменная окружения E2E_BASE_URL или http://127.0.0.1:8000.
"""


import allure
from assertpy import assert_that






def test_openapi_schema_available(todolist_client, authorize_client):
    with allure.step("Получить информацию о сервисе todolist"):
        response = todolist_client.put("/todo/get_all", json={})
        assert_that(response.status_code).is_equal_to(200)

    with allure.step("Получить информацию о сервисе todolist"):
        response = todolist_client.get("/openapi.json")
        assert_that(response.status_code).is_equal_to(200)

        body = response.json()
        assert_that(body.get("openapi")).is_not_empty()
        assert_that(body.get("info", {}).get("title")).is_equal_to("ToDo API")
