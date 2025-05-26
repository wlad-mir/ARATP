import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from faker import Faker


class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        self.fake = Faker()
        data = {
            'username': self.fake.user_name(),
            'firstName': self.fake.first_name(),
            'lastName': self.fake.last_name(),
            'password': self.fake.password(length=10),
            'email': self.fake.email()
        }

        response = requests.post(f"{self.API_URL}/user/", data=data)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        data = {
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': self.TEST_USER_PASSWORD,
            'email': self.TEST_USER_EMAIL
        }

        response = requests.post(f"{self.API_URL}/user/", data=data)

        Assertions.assert_status_code(response, 400)