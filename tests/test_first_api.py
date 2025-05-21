import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestFirstApi(BaseCase):  # Added inheritance from BaseCase
    def test_hello_call(self):
        url = f"{self.API_URL}/hello"
        name = "Zambron"
        params = {"name": name}

        try:
            response = requests.get(url, params=params)

            # Response Checks
            Assertions.assert_status_code(response, 200)

            response_dict = response.json()

            Assertions.assert_json_has_key(response, 'answer')
            expected_response_text = f"Hello, {name}"
            actual_response_text = response_dict["answer"]

            assert actual_response_text == expected_response_text, \
                f"Actual text in the response is not correct. " \
                f"Expected: '{expected_response_text}', Actual: '{actual_response_text}'"

        except requests.exceptions.RequestException as e:
            raise AssertionError(f"Request execution failed: {e}")
