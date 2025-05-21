import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAuth(BaseCase):
    def test_auth_user(self):
        # Arrange
        auth_data = {
            "email": self.TEST_USER_EMAIL,
            "password": self.TEST_USER_PASSWORD
        }

        # Act - First request (login)
        login_response = requests.post(
            f"{self.API_URL}/user/login",
            data=auth_data
        )

        # Assert - Login response
        Assertions.assert_status_code(login_response, 200)
        Assertions.assert_json_has_key(login_response, "user_id")

        assert "auth_sid" in login_response.cookies, "Auth cookie not found"
        assert "x-csrf-token" in login_response.headers, "CSRF token not found"

        # Extract auth tokens
        auth_sid = login_response.cookies.get("auth_sid")
        token = login_response.headers.get("x-csrf-token")
        user_id_from_login = login_response.json()["user_id"]

        # Act - Second request (auth check)
        auth_check_response = requests.get(
            f"{self.API_URL}/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        # Assert - Auth check response
        Assertions.assert_status_code(auth_check_response, 200)
        Assertions.assert_json_has_key(auth_check_response, "user_id")

        user_id_from_check = auth_check_response.json()["user_id"]

        assert user_id_from_login == user_id_from_check, (
            f"User ID mismatch. Login: {user_id_from_login}, Check: {user_id_from_check}"
        )

            # Checking the response time
        assert login_response.elapsed.total_seconds() < 1, "Response too slow"

        # Checking Content-Type
        assert login_response.headers["Content-Type"] == "application/json"
