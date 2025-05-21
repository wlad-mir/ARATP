import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestFirstApi(BaseCase):
    """Tests for the /hello endpoint with detailed checks"""

    @pytest.mark.positive
    def test_hello_call(self):
        # Arrange (Подготовка)
        endpoint = "/hello"
        url = f"{self.API_URL}{endpoint}"
        test_name = "Zambron"
        params = {"name": test_name}

        # Act (Действие)
        response = requests.get(url, params=params)

        # Assert (Проверки)
        Assertions.assert_status_code(response, 200)

        response_data = response.json()
        Assertions.assert_json_has_keys(response, ["answer"])  # Checking for a key

        expected_response = f"Hello, {test_name}"
        Assertions.assert_json_value_by_name(
            response,
            "answer",
            expected_response,
            f"Incorrect server response. Expected: '{expected_response}'"
        )
