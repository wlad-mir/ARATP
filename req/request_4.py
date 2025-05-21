import requests



response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})

# response = requests.post("https://playground.learnqa.ru/api/check_type")

# response = requests.put("https://playground.learnqa.ru/api/check_type")

# response = requests.delete("https://playground.learnqa.ru/api/check_type")

print(response.text)










