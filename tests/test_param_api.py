import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions  # Добавим использование Assertions
from faker import Faker


class TestFirstApi(BaseCase):
    fake = Faker()  # Выносим на уровень класса (без self)

    names = [
        fake.user_name(),
        fake.user_name(),
        fake.user_name(),
        "",
        "Кириллица",
        "12345",
        "Name With Spaces",
        "X" * 100  # Длинное имя
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        # Arrange
        url = f"{self.API_URL}/hello"
        params = {"name": name}  # Для GET-запросов правильнее использовать params

        # Act
        response = requests.get(url, params=params)

        # Assert
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "answer")

        response_dict = response.json()
        expected_response = f"Hello, {name}" if name else "Hello, someone"
        actual_response = response_dict["answer"]

        assert actual_response == expected_response, (
            f"Unexpected response text. "
            f"Expected: '{expected_response}', "
            f"Actual: '{actual_response}'"
        )
