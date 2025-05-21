import requests



payload = {"login":"secret_login", "password":"secret_pass"}


response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print(response.text)

print(response.status_code) #  200

print(dict(response.cookies)) #  {'auth_cookie': '284778'}


print(response.headers)






















