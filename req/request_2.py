import requests



payload = {"name": "Alex"}

response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)

print(response.text) #   {"answer":"Hello, Alex"}
