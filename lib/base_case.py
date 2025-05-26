from faker import Faker
import random
from requests import Response



class BaseCase:
    API_URL = "https://playground.learnqa.ru/api"
    fake = Faker()

    def prepare_registration_data(self, email=None):
        if email is None:
            email = self.fake.email()
            
        return {
            'username': self.fake.user_name(),
            'firstName': self.fake.first_name(),
            'lastName': self.fake.last_name(),
            'password': self.fake.password(length=10),
            'email': email
        }

    TEST_USER_EMAIL = "shams@wp.pl"
    TEST_USER_PASSWORD = "de89heu"

    def get_cookie(self, response:Response, cookie_name):
        assert cookie_name in response.cookies, f"Can't find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Can't find header with name {header_name} in the last response"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        return response_as_dict[name]