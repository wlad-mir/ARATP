from json.decoder import JSONDecodeError
import requests


# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "Ivan"})

# parsed_response_text = response.json()

# print(parsed_response_text["answer"])  #  Hello, Ivan


response = requests.get("https://playground.learnqa.ru/api/get_text")

print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text["text"])
except JSONDecodeError:
    print("Response is not in JSON format")








