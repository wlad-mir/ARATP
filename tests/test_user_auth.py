import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAuth(BaseCase):
    exclude_params = [
        "no_cookie",
        "no_token"
    ]

    def setup_method(self):
        print(f"API_URL: {self.API_URL}")
        print(f"Test user: {self.TEST_USER_EMAIL}")

        """Подготовка тестовых данных и аутентификации"""
        auth_data = {
            'email': self.TEST_USER_EMAIL,
            'password': self.TEST_USER_PASSWORD
        }

        # Первый запрос на аутентификацию
        login_response = MyRequests.post("/user/login", data=auth_data)

        # Проверки успешной аутентификации
        Assertions.assert_status_code(login_response, 200)
        Assertions.assert_json_has_key(login_response, "user_id")
        assert "auth_sid" in login_response.cookies, "Auth cookie not found"
        assert "x-csrf-token" in login_response.headers, "CSRF token not found"

        # Сохраняем данные для последующих запросов
        self.auth_sid = login_response.cookies.get("auth_sid")
        self.token = login_response.headers.get("x-csrf-token")
        self.user_id_from_auth = login_response.json()["user_id"]

    def test_auth_user(self):
        """Позитивный тест проверки аутентификации"""
        auth_check_response = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_status_code(auth_check_response, 200)
        Assertions.assert_json_has_key(auth_check_response, "user_id")

        user_id_from_check = auth_check_response.json()["user_id"]
        assert self.user_id_from_auth == user_id_from_check, (
            f"User ID mismatch. Auth: {self.user_id_from_auth}, Check: {user_id_from_check}"
        )

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):
        """Негативные тесты проверки аутентификации"""
        if condition == "no_cookie":
            response = MyRequests.get(
                "/user/auth",
                headers={"x-csrf-token": self.token}
            )
        else:
            response = MyRequests.get(
                "/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "user_id")

        user_id = response.json()["user_id"]
        assert user_id == 0, f"User should not be authorized with condition: {condition}"
