import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from faker import Faker

class TestCreateUser(BaseCase):
    def setup_method(self):
        self.fake = Faker()
        self.url = f"{self.API_URL}/user/"

    def test_create_user_successfully(self):
        data = {
            'username': self.fake.user_name(),
            'firstName': self.fake.first_name(),
            'lastName': self.fake.last_name(),
            'password': self.fake.password(length=10),
            'email': self.fake.email()
        }

        try:
            response = requests.post(self.url, data=data)

            # Checking the status code (201 Created) 200
            Assertions.assert_status_code(response, 200)

            # Check that the response contains the “id” key
            Assertions.assert_json_has_key(response, "id")

            # Get the user ID for further tests (e.g. GET request)
            user_id = response.json()["id"]
            print(f"User created with ID: {user_id}")  # To debug

        except requests.exceptions.RequestException as e:
            pytest.fail(f"Request failed: {e}")
