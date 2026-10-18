import allure
from assertpy import assert_that
from httpx import Response

def assert_status_code(response: Response, expected_status: int) -> None:
    with allure.step(f"http status is {expected_status}"):
        assert_that(response.status_code, description=f"http status {expected_status}").is_equal_to(expected_status)
        allure.attach(
            f"exp: {expected_status}\nrec: {response.status_code}",
            attachment_type=allure.attachment_type.TEXT,
        )

def assert_error_message(response: Response, expected_substring: str) -> None:
    with allure.step(f"message contains: {expected_substring}"):
        resp_msg = response.json()["detail"]
        assert_that(resp_msg, description=f"message contains: {expected_substring}").contains(expected_substring)
        allure.attach(
            f"exp: {expected_substring}\nrec: {resp_msg}",
            attachment_type=allure.attachment_type.TEXT,
        )