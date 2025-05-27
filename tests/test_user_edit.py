from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER - регистрируем нового пользователя
        register_data = self.prepare_registration_data()
        response_register = MyRequests.post("/user/", data=register_data)
        
        Assertions.assert_status_code(response_register, 200)
        Assertions.assert_json_has_key(response_register, 'id')
        
        user_id = self.get_json_value(response_register, 'id')
        email = register_data['email']
        password = register_data['password']
        
        # LOGIN - авторизуемся
        login_data = {
            'email': email,
            'password': password
        }
        
        response_login = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response_login, 'auth_sid')
        token = self.get_header(response_login, 'x-csrf-token')
        
        # EDIT - изменяем данные
        new_name = self.fake.first_name()  # Генерируем новое случайное имя
        
        print(response_login.text)
        
        response_edit = MyRequests.put(
            f"/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
            data={'firstName': new_name}
        )
        
        Assertions.assert_status_code(response_edit, 200)
        print(response_edit.text)
        
        # GET - проверяем изменения
        response_get = MyRequests.get(
            f"/user/{user_id}",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid}
        )
        
        Assertions.assert_json_value_by_name(
            response_get,
            'firstName',
            new_name,
            'Имя пользователя не изменилось после редактирования'
        )
     