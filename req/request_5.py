import requests



# response = requests.post("https://playground.learnqa.ru/api/check_type")

# response = requests.post("https://playground.learnqa.ru/api/get_500")

# response = requests.post("https://playground.learnqa.ru/api/somethig")

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)

first_response = response.history[0]

second_response = response

print(first_response.url)   #  https://playground.learnqa.ru/api/get_301

print(second_response.url)   #  https://www.learnqa.ru/

# print(response.status_code)  # 200  500  404 301 

# print(response.text) #  This is 404 error!   You will be redirected










