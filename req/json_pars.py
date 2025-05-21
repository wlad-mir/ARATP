import json



string_as_json_format = '{"answer": "Hello, User"}'

obj = json.loads(string_as_json_format)

# print(obj['answer'])  # Hello, User

key = "answer9"

if key in obj:
    print(obj[key])  # Hello, User

else:
    print(f"Key {key} not found in the JSON object.")











