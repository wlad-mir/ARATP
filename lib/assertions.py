from requests import Response
import json
from typing import List, Optional  # Optional

class Assertions:
    @staticmethod
    def _get_json(response: Response):
        try:
            return response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

    @staticmethod
    def assert_json_value_by_name(response: Response, name: str, expected_value, error_message: str):
        response_dict = Assertions._get_json(response)
        assert name in response_dict, f"Response JSON doesn't have key '{name}'"
        assert response_dict[name] == expected_value, \
            f"{error_message}. Actual: '{response_dict[name]}', Expected: '{expected_value}'"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code! Expected: {expected_status_code}, Actual: {response.status_code}, URL: {response.url}"

    @staticmethod
    def assert_json_has_key(response: Response, name: str):
        response_json = Assertions._get_json(response)
        assert name in response_json, f"Response JSON doesn't have key '{name}'. JSON: {response_json}"

    @staticmethod
    def assert_json_has_not_key(response: Response, name: str):
        response_dict = Assertions._get_json(response)
        assert name not in response_dict, f"Response JSON shouldn't have key '{name}'. But it's present."

    @staticmethod
    def assert_json_has_keys(response: Response, names: List[str]):
        response_dict = Assertions._get_json(response)
        for name in names:
            assert name in response_dict, f"Response JSON doesn't have key '{name}'."

    @staticmethod
    def assert_success_response(response: Response):
        """Checks that the status code is in the range 2xx."""
        assert 200 <= response.status_code < 300, \
            f"Request failed with status code {response.status_code}. URL: {response.url}"
